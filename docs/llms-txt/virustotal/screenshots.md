# Source: https://virustotal.readme.io/reference/screenshots.md

# Screenshots

screenshot objects

Screenshots are screen capture images obtained during the file execution in a behavior analysis sandbox machine. This object contains attributes identifying where and when the screenshot was generated:

* `sandbox_name` name of the sandbox setup where the file was executed
* `date` Epoch when the capture was made (as unix timestamp)
* `link` URL pointing to the actual image
* `analysed_file_sha256` relationship pointing to the file object that was executed

```json
{
  "data": {
    "type": "screenshot",
    "id": "<SCREENSHOT_NAME>",
    "attributes" : {
      "sandbox_name": "<string>",
      "date": "<unix_timestamp>",
      "link": "<string>",
      "analysed_file_sha256": <object>
    }
  } 
}
```