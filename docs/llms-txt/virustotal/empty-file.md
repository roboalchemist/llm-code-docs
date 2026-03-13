# Source: https://virustotal.readme.io/docs/empty-file.md

# Empty file and VirusTotal uploads

The file with SHA256 hash [e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855](https://www.virustotal.com/gui/file/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855) represents an empty file, i.e. zero bytes in size. Being empty, it can't exhibit malicious behaviour by itself.

If you have arrived at this report it might be due to one of the following:

* You did indeed submit an empty file. Empty files can sometimes be used as a primitive synchronization mechanism, e.g. just checking whether a given file exists in the filesystem, as a store that will be written in the future, or for some other reason.

* Some process running in your computer/network device has blocked the file that you intended to upload from being read, this meant that the pertinent APIs were unable to read the file that you wanted to scan and so you ended up uploading an empty file. If this is the case, this scan report will not correspond to your file and might result in misleadingly believing that the file is inoquous. You should search for the process that is blocking the file from being read and kill its file handle, so that you are eventually able to perform the upload.

To understand which one of the two scenarios above applies to your case, please check the size of the file in your device, if it is not zero bytes then there is indeed some device or network element preventing the upload and you should not trust this report.