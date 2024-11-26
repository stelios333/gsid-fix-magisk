#!/usr/bin/env sh
module_path=./module
version=$(jq .version update.json -r | cut -c2-)
prefix=$(basename "$PWD")-
rm $prefix*
zip -r $prefix$version.zip $module_path