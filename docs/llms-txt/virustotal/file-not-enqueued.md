# Source: https://virustotal.readme.io/docs/file-not-enqueued.md

# File from a URL scan was not enqueued for antivirus scanning

If you scan a URL, for example:

```
http://some-example.com/file.exe 
```

We will attempt to scan file.exe . The URL scanner will only enqueue for antivirus file scanning those files that are not text or similar formats (HTML, CSV, XML, etc.). Executables, images, music files, etc. will be always enqueued.

Sometimes the file does not get scanned because:

* The URL response content could not be retrieved at the time of analysis (due to some network error, because the response content is larger than 32MB in size, etc.)
* The download times out.
* The server blocks us.
* You need to be logged in,  have a browser cookie, or some type of javascript validation to download the file.