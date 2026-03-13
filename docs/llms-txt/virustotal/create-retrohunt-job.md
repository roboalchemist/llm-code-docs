# Source: https://virustotal.readme.io/reference/create-retrohunt-job.md

# Create a new Retrohunt job

This endpoint creates a new Retrohunt job. The request's body must have the following structure:

```json
{
  "data": {
    "type": "retrohunt_job",
    "attributes": {
      "rules": "rule foobar { strings: $ = \"foobar\" condition: all of them }",
      "notification_email": "notifications@acme.com",
      "corpus": "main",
      "time_range": {
        "start": 1545145761,
        "end": 1547737720
      }
    }
  }
}
```

The `rules` attribute is required, but `notification_email`, `corpus` and `time_range` are optional. You should provide  `notification_email` if you want to receive an email notification when the job is finished, while `corpus` allows you to select which dataset you want to scan with your job. There are two different corpuses: "main" and "goodware". The "main" corpus is the default one, composed of files sent to VirusTotal during the last few months. The "goodware" corpus is a random selection of \~1.000.000 files from the [NSRL](https://www.nist.gov/software-quality-group/national-software-reference-library-nsrl) that are not detected by any antivirus engine. This corpus contains multiple file types, and is useful for testing your YARA rules for false positives. If the `corpus` attribute is not specified the "main" corpus will be used.

> 🚧 Retrohunt limits
>
> Each user can run up to 10 Retrohunt jobs at the same time, when you reach that limit you must wait for one of the running jobs to finish before launching a new one. Additionally, each job can contain up to 300 YARA rules.

If you want your job to scan files sent to VirusTotal within a certain time range you can use the  `time_range` attribute to specify the desired range. Both the `start` and `end` fields in `time_range` should be the UNIX timestamp for the minimum and upper bound of the time range in UTC, and they should be within the maximum range allowed by your Retrohunt privileges. All users can scan up to 90 days back, and this can go up to 180 or 365 days for more privileged users. If `start` is not specified your Retrohunt job will scan back to the limit allowed by your privileges, and if `end` is not specified it will scan up to the most recent files.

Returns the newly created [Retrohunt Job](https://virustotal.readme.io/reference/retrohunt-job-object) object.

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
    "/intelligence/retrohunt_jobs": {
      "post": {
        "summary": "Create a new Retrohunt job",
        "description": "",
        "operationId": "create-retrohunt-job",
        "parameters": [
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
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "required": [
                  "data"
                ],
                "properties": {
                  "data": {
                    "type": "string",
                    "description": "A Retrohunt job",
                    "default": "{     \"type\": \"retrohunt_job\",     \"attributes\": {       \"rules\": \"rule foobar { strings: $ = \\\"foobar\\\" condition: all of them }\",       \"corpus\": \"main\"    }   }",
                    "format": "json"
                  }
                }
              }
            }
          }
        },
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
        "deprecated": false
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