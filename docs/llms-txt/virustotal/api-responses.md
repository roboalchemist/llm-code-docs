# Source: https://virustotal.readme.io/reference/api-responses.md

# API responses

Most endpoints in the VirusTotal API return a response in JSON format. Unless otherwise specified, a successful request's response returns a 200 HTTP status code and has the following format:

```json
{
  "data": <response data>
}
```

`<response data>` is usually an [object](https://virustotal.readme.io/reference/objects) or a list of objects, but that's not always the case. An example of this is the [/files/upload\_url](https://virustotal.readme.io/reference/files-upload-url) endpoint, which returns a URL. Refer to each endpoint's documentation to learn more about its return data structure.