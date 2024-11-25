print_modname() {
  ui_print "*******************************"
  ui_print "          GSID Fix             "
  ui_print "*******************************"
}

echo "- Setting permissions and SELinux contexts..."
set_perm $MODPATH/system/bin/gsid 0 0 0700 u:object_r:gsid_exec:s0
