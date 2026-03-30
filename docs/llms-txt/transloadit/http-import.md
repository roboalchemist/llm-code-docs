# Source: https://transloadit.com/docs/robots/http-import.md

The result of this Robot will carry a field `import_url` in their metadata, which references the URL from which they were imported. Further conversion results that use this file will also carry this `import_url` field. This allows you to to match conversion results with the original import URL that you used.

This Robot knows to interpret links to files on these services:

* Dropbox
* Google Drive
* Google Docs
* OneDrive

Instead of downloading the HTML page previewing the file, the actual file itself will be imported.
