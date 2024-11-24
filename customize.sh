echo "- Setting permissions and SELinux contexts..."
set_perm $MODPATH/system/bin/gsid 0 0 0700 u:object_r:gsid_exec:s0
