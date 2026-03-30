# Source: https://virustotal.readme.io/docs/compressed-files.md

# What type of compressed files are supported?

You can submit any compressed file that is supported by the 7z software. If succesfully decompressed, contained files appear as bundled files in the relationships tab of the archive file report. If it is password protected, the tools uses standard known passwords as "infected" or "password".

If it is a password protected ZIP file and includes just one single compressed file, the web interface will request a password. If you are using the API, the "password" parameter can be used for this purpose. VirusTotal will generate a report for the bundled file and not the ZIP file, but for this case the size limit is 3MBs. If the ZIP file is bigger than 3MBs, we will generate a report for the ZIP file itself.