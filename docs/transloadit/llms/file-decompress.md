# Source: https://transloadit.com/docs/robots/file-decompress.md

This Robot supports the following archive formats:

* ZIP archives (with uncompressed or "deflate"-compressed entries)
* 7-Zip archives
* RAR archives
* GNU tar format (including GNU long filenames, long link names, and sparse files)
* Solaris 9 extended tar format (including ACLs)
* Old V7 tar archives
* POSIX ustar
* POSIX pax interchange format
* POSIX octet-oriented cpio
* SVR4 ASCII cpio
* POSIX octet-oriented cpio
* Binary cpio (big-endian or little-endian)
* ISO9660 CD-ROM images (with optional Rockridge or Joliet extensions)
* GNU and BSD "ar" archives
* "mtree" format
* Microsoft CAB format
* LHA and LZH archives
* XAR archives

This Robot also detects and handles any of the following before evaluating the archive file:

* uuencoded files
* Files with RPM wrapper
* gzip compression
* bzip2 compression
* compress/LZW compression
* lzma, lzip, and xz compression

For security reasons, archives that contain symlinks to outside the archived dir, will error out the Assembly. Decompressing password-protected archives (encrypted archives) is currently not fully supported but will not cause an Assembly to fail.
