#!/usr/bin/env sh
version_hash=$(git rev-parse --short HEAD)
prefix=$(basename "$PWD")-
rm $prefix*
zip -r $prefix$version_hash.zip ./ -x ./*.git* $(basename "$0") $(xargs -a .gitignore)