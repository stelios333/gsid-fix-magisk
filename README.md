## GSID Fix

Since Andrioid 14 QPR3 installing DSUs will not work devices with unencrypted /data. This is because some code required for installing DSUs on those devices was removed from an internal library. This Magisk module replaces the gsid binary with a modified version that has the removed code restored.

**Only arm64 is supported for now.**