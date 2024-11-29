print_modname() {
  ui_print "*******************************"
  ui_print "          GSID Fix             "
  ui_print "*******************************"
}

# For now only arm64 gsid is distributed.
if [ "$ARCH" != "arm64" ]; then
  ui_print "Error: Only arm64 devices are supported (for now)."
  exit 1
fi

# This module isn't needed in older Android versions.
if [ $API -lt 34 ]; then
  ui_print "Error: This module requires Android 14+."
  exit 1
fi

ui_print "- Setting permissions and SELinux contexts..."
set_perm $MODPATH/system/bin/gsid 0 0 0700 u:object_r:gsid_exec:s0
