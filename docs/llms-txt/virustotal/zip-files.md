# Source: https://virustotal.readme.io/reference/zip-files.md

# Zipping files

You can download individual files from VirusTotal by using the [GET /files/{id}/download](https://virustotal.readme.io/reference/zip-files-download) and [GET /files/{id}/download\_url](https://virustotal.readme.io/reference/zip-files-download-url) endpoints, however, sometimes you may want to download files in bulk in a password-protected ZIP file. This is specially useful in corporate environments where a gateway antivirus may be blocking your downloads because they contain malware (as expected from files downloaded from VirusTotal)