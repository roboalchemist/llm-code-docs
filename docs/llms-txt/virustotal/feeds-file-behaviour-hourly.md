# Source: https://virustotal.readme.io/reference/feeds-file-behaviour-hourly.md

# Get an hourly file behaviour feed batch

> 🚧 Special privileges required
>
> Sandbox analyses feeds endpoints are only available to users with a Sandbox feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

This endpoint returns a single package containing all minutely packages returned in [/feeds/file\_behaviours/{time}](https://virustotal.readme.io/reference/feeds-file-behaviour) endpoint for a given hour. The returned file is a `.tar.bz2` file which contains the 60 minutely feeds for that hour.

The provided `time` argument must be in `YYYYMMDDhh` format. For example, time `2021012211` returns the batches correspoding to January 21st 2021 11:00 - 11:59 UTC. You can download batches up to 7 days old, and the most recent batch has always a 2 hours lag with respect with to the current time. This means that if the current time in UTC is T you can download batch T-2h but any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

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
    "/feeds/file_behaviours/hourly/{time}": {
      "get": {
        "summary": "Get an hourly file behaviour feed batch",
        "description": "",
        "operationId": "feeds-file-behaviour-hourly",
        "parameters": [
          {
            "name": "time",
            "in": "path",
            "description": "A string in format YYYYMMDDhh",
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
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
                }
              }
            }
          },
          "400": {
            "description": "400",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {}
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
              "code": "curl --location --remote-name --request GET \\\n  --url https://www.virustotal.com/api/v3/feeds/file_behaviours/hourly/{time} \\\n  --header 'x-apikey: <your API key>'"
            },
            {
              "language": "python",
              "code": "import requests\nimport io\nimport tarfile\nimport json\n\nurl = \"https://www.virustotal.com/api/v3/feeds/file-behaviours/hourly/{time}\"\n\nresponse = requests.get(\n    url.format(time=\"2021012211\"),\n    headers={'x-apikey': '<your VT API key>'})\n\nif response.status_code != 200:\n  raise Exception(response.content)\nelse:\n  file_behaviour_feed = []\n  with io.BytesIO(response.content) as f:\n    with tarfile.open(fileobj=f, mode='r:bz2')as t:\n      # process minutely batches\n      for batch in t.getmembers():\n        file_behaviour_feed.extend([json.loads(line) for line in t.extractfile(batch)])\n  # further processing"
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