# Source: https://virustotal.readme.io/reference/feeds-file.md

# Get a per-minute file feed batch

> 🚧 Special privileges required
>
> File feeds endpoints are only available to users with a File feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

With this endpoint you can download an individual one-minute batch by providing a `time` consisting of a string with format `YYYYMMDDhhmm`. Time `201912010802` will return the batch corresponding to December 1st, 2019 08:02 UTC. You can download batches up to 7 days old, and the most recent batch has always a 60 minutes lag respecting to the current time. This means that if the current time in UTC is `T` you can download batch `T-60m` but not `T-59m` or any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

> 🚧 Missing batches
>
> Missing batches are rare, but still can happen occasionally. This doesn't mean that you are losing any files in the feed, it just means that no batches were generated on a specific minute. The client code should be ready to accept a `404` error while retrieving a batch and proceed with the following one. However, receiving multiple `404` errors in a row for consecutive batches shouldn't happen and should be treated as an error condition.

The downloaded file is a bzip2 compressed UTF-8 text file contains one JSON structure per line, where the structure represents a file object as returned by the [GET /files/{id}](https://virustotal.readme.io/reference/file-info) endpoint. Besides the standard attributes usually found in all file objects, two additional context attributes are also included: `download_url` and `submitter`. The `download_url` attribute is a link that can be used to download the file itself, while `submitter` is a dictionary with lossy-ciphered non-identifiable information about who submitted the file to VirusTotal. Notice however that `submitter` is not present in all files as some files are re-analyzed by VirusTotal without being submitted by some external user.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "vt-enterprise",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [],
  "paths": {
    "/feeds/files/{time}": {
      "get": {
        "summary": "Get a per-minute file feed batch",
        "description": "",
        "operationId": "feeds-file",
        "parameters": [
          {
            "name": "time",
            "in": "path",
            "description": "A string in format YYYYMMDDhhmm",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "x-apikey",
            "in": "header",
            "description": "Your API key",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "text/plain": {
                "examples": {
                  "Result": {
                    "value": ""
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl --location --remote-name --request GET \\\n  --url https://www.virustotal.com/api/v3/feeds/files/{time} \\\n  --header 'x-apikey: <your API key>'"
            },
            {
              "language": "python",
              "code": "import requests\nimport io\nimport bz2\nimport json\n\nurl = \"https://www.virustotal.com/api/v3/feeds/files/{time}\"\n\n\nresponse = requests.get(\n    url.format(time=\"202002070300\"),\n    headers={'x-apikey': '<your VT API key>'})\n\nif response.status_code != 200:\n  raise Exception(response.content)\nelse:\n  with io.BytesIO(response.content) as f:\n    file_feed = [json.loads(line) for line in bz2.decompress(f.read()).splitlines()]\n# further processing\n"
            }
          ],
          "samples-languages": [
            "curl",
            "python"
          ]
        }
      }
    }
  },
  "x-readme": {
    "headers": [],
    "explorer-enabled": true,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```