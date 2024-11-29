import configparser
import sys
import re
import json
import shutil
import os

module_path = "./module/"
prop_file_path = os.path.join(module_path, "module.prop")
update_json_path = "./update.json"

update_json = json.load(open(update_json_path, "r"))
curr_version = update_json["version"][1:]
print(f"Current version: v{curr_version}")

if sys.argv.__len__() == 2:
    if re.fullmatch(r"([0-9]+(\.[0-9]+)+)", sys.argv[1]):
        version = sys.argv[1]
        print(f"Updating version to: v{version}")
        new_version_int = int(version.replace(".", "").ljust(5, '0'))
        magisk_props = configparser.ConfigParser(allow_unnamed_section=True)
        # Make it case sensitive
        magisk_props.optionxform = lambda option: option

        magisk_props.read(prop_file_path)
        magisk_props.set(configparser.UNNAMED_SECTION, "version", "v"+version)
        magisk_props.set(configparser.UNNAMED_SECTION, "versionCode", f"{new_version_int}")
        with open(prop_file_path, 'w') as new_props:
            magisk_props.write(new_props, space_around_delimiters=False)

        update_json["version"] = "v"+version
        update_json["versionCode"] = new_version_int
        download_url = f"https://github.com/stelios333/gsid-fix-magisk/releases/download/v{version}/gsid-fix-magisk-{version}.zip"
        update_json["zipUrl"] = download_url
        json.dump(update_json, open(update_json_path, "w"), indent=2)

    else:
        print("Error: must specify version in format <major_number>.<minor_number>!")
        exit()
else:
    version = curr_version


archive_filename = f"gsid-fix-magisk-{version}"
print("Creating zip archive...")
shutil.make_archive(archive_filename, 'zip', module_path)
print("Complete!")
