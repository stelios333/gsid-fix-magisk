import configparser,sys,re
import json,shutil,os

module_path = "./module/"
prop_file_path = os.path.join(module_path, "module.prop")
update_json_path = "./update.json"



if sys.argv.__len__() == 2:
    if re.fullmatch(r"([0-9]+(\.[0-9]+)+)", sys.argv[1]):
        new_version = sys.argv[1]
    else:
        print("Error: must specify version in format <major_number>.<minor_number>!")
        exit()
else:
    print("Error: None/Invalid arguments.")
    exit()

print("Setting version...")
new_version_int = int(new_version.replace(".",""))
magisk_props = configparser.ConfigParser(allow_unnamed_section=True)
# Make it case sensitive
magisk_props.optionxform = lambda option: option

magisk_props.read(prop_file_path)
magisk_props.set(configparser.UNNAMED_SECTION, "version", "v"+new_version)
magisk_props.set(configparser.UNNAMED_SECTION, "versionCode", str(new_version_int))
with open(prop_file_path, 'w') as new_props:
    magisk_props.write(new_props, space_around_delimiters=False)

update_json = json.load(open(update_json_path,"r"))
update_json["version"] = "v"+new_version
update_json["versionCode"] = new_version_int
download_url = f"https://github.com/stelios333/gsid-fix-magisk/releases/download/v{new_version}/gsid-fix-magisk-{new_version}.zip"
update_json["zipUrl"] = download_url
json.dump(update_json, open(update_json_path,"w"), indent=2)

archive_filename = f"gsid-fix-magisk-{new_version}"
print("Creating zip archive...")
shutil.make_archive(archive_filename, 'zip', module_path)
print("Complete!")