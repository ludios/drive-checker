This tool tests new HDDs/SDDs by writing checksummed data and then verifying it.

Usage:

```
(./write_bigfile_stdout | pv > /dev/sdN; ./verify_bigfile /dev/sdN) 2>&1 | tee -a drive-checker-log
```

If no "Bad checksum at" messages, drive is probably fine.

TODO:
-	Test drive with a lot of random seeks too
