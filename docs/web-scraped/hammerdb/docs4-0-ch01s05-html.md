# Source: https://www.hammerdb.com/docs4.0/ch01s05.html

Title: 5. Checksum Verification

URL Source: https://www.hammerdb.com/docs4.0/ch01s05.html

Markdown Content:
Checksums for the installation files are shown alongside the download files in [GitHub Releases](https://github.com/TPC-Council/HammerDB/releases). The integrity of the HammerDB installation files can be verified on Windows with the Microsoft File Checksum Integrity Verifier which can be downloaded at no cost from Microsoft and run as follows:

fciv -both HammerDB-4.0-Win-x86-64-Setup.exe
and on Linux with md5sum and sha1sum as shown:

md5sum HammerDB-4.0-Linux.tar.gz 
sha1sum HammerDB-4.0-Linux.tar.gz
