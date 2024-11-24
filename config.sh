# This will be the folder name under /magisk
# This should also be the same as the id in your module.prop to prevent confusion
MODID=template

# Set to true if you need to enable Magic Mount
# Most mods would like it to be enabled
AUTOMOUNT=true

# Set to true if you need to load system.prop
PROPFILE=false

# Set to true if you need post-fs-data script
POSTFSDATA=false

# Set to true if you need late_start service script
LATESTARTSERVICE=false


print_modname() {
  ui_print "*******************************"
  ui_print "          GSID FIX             "
  ui_print "*******************************"
}

