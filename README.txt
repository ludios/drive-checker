This tool tests new HDDs/SDDs by writing checksummed data and then verifying it.

Steps:
1.	write_bigfile.py X:/bigfile
2.	Wait for drive to fill up
3.	verify_bigfile.py X:/bigfile
	If no "Bad checksum at" messages, drive is probably fine.
4.	del X:/bigfile

TODO:
-	Test drive with a lot of random seeks too
