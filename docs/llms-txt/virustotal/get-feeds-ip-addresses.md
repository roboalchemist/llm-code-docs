# Source: https://virustotal.readme.io/reference/get-feeds-ip-addresses.md

# Get a minutely IP address feed batch

> 🚧 Special privileges required
>
> IP feeds endpoints are only available to users with a IP feeds license. [Contact us](https://www.virustotal.com/gui/contact-us/) for more information.

With this endpoint you can download an individual one-minute batch by providing a time consisting of a string with format `YYYYMMDDhhmm`. Time `201912010802` will return the batch corresponding to December 1st, 2019 08:02 UTC. You can download batches up to 7 days old, and the most recent batch has always a 60 minutes lag with respect with to the current time. This means that if the current time in UTC is `T` you can download batch `T-60m` but not `T-59m` or any more recent.

Successful calls to this endpoint will return a `302` redirect response to a URL from which the final batch file will be downloaded.

> 🚧 Missing batches
>
> Missing batches are rare, but still can happen occasionally. This doesn't mean that you are losing any IP addresses in the feed, it just means that no batches were generated on a specific minute. The client code should be ready to accept a `404` error while retrieving a batch and proceed with the following one. However, receiving multiple `404` errors in a row for consecutive batches shouldn't happen and should be treated as an error condition.

The downloaded file is a bzip2 compressed UTF-8 text file contains one JSON structure per line, where the structure represents a URL object as returned by the [GET /ip\_addresses/{ip}](https://virustotal.readme.io/reference/ip-info) endpoint.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "virustotal-api-v3",
    "version": "3.0"
  },
  "servers": [
    {
      "url": "https://www.virustotal.com/api/v3"
    }
  ],
  "security": [
    {}
  ],
  "paths": {
    "/feeds/ip_addresses/{time}": {
      "get": {
        "summary": "Get a minutely IP address feed batch",
        "description": "",
        "operationId": "get-feeds-ip-addresses",
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
        "security": [],
        "x-readme": {
          "code-samples": [
            {
              "language": "curl",
              "code": "curl --location --remote-name --request GET \\\n  --url https://www.virustotal.com/api/v3/feeds/ip_addresses/{time} \\\n  --header 'x-apikey: <your API key>'"
            },
            {
              "language": "python",
              "code": "import requests\nimport io\nimport bz2\nimport json\nimport os\n\nurl = \"https://www.virustotal.com/api/v3/feeds/ip_addresses/{time}\"\n\n\nresponse = requests.get(\n    url.format(time=\"202002070300\"),\n    headers={'x-apikey': '<your VT API key>'})\n\nif response.status_code != 200:\n  raise Exception(response.content)\nelse:\n  with io.BytesIO(response.content) as f:\n    url_feed = [json.loads(line) for line in bz2.decompress(f.read()).splitlines()]\n# further processing\n"
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