#!/usr/bin/env sh
version_hash=$(git rev-parse --short HEAD)
zip -r $(basename "$PWD")-$version_hash.zip ./ -x ./*.git* $(basename "$0") $(xargs -a .gitignore)