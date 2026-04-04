# Source: https://virustotal.readme.io/reference/get-objects-from-the-ioc-stream.md

# Get objects from the IoC Stream

The IoC stream endpoint returns different types of objects (files, URLs, domains, IP addresses) coming from multiple origins (you can restrict the returned types by using the filters explained below). In addition, depending on the origin of the notification there will be different context attributes added to these objects.

The possible context attributes in IoC Stream objects are:

* `notification_id`: <*string*> Always present. This string identifies the notification, and can be used to retrieve the notification individually (by using [GET /ioc\_stream\_notifications/{id}](https://virustotal.readme.io/reference/get-an-ioc-stream-notification)) or to delete it ([DELETE /ioc\_stream\_notifications/{id}](https://virustotal.readme.io/reference/delete-an-ioc-stream-notification)).
* `notification_date`: <*int*> Always present. Date when the notification was created (UTC timestamp).
* `origin`: <*string*> Always present. The notification's origin. In the case of Livehunt or Retrohunt the origin is `hunting`.
* `sources`: <*list of dictionaries*> Always present. The different sources associated to the notification. In the case of Livehunt the only source is always the hunting ruleset that triggered the notification.
* `tags`: <*list of strings*> List of notification's tags (if any). These tags can be used to filter the objects by using the `notification_tag:` filter.
* `hunting_info`: <*dictionary*> Only present for notifications of `hunting` origin. It contains additional contextual information from Livehunt. Its structure is the following:
  * `rule_name`: <*string*> matched rule name.
  * `rule_tags`: <*list of strings*> matched rule tags.
  * `snippet`: <*string*> matched contents inside the file as hexdump. Contains `begin_highlight` and `end_highlight` substrings to indicate the part of the file that produced the match and give additional context about surrounding bytes in the match.
  * `source_country`: <*string*> country where the matched file was uploaded from.
  * `source_key`: <*string*> unique identifier for the source in ciphered form.

Allowed filters with examples (they can be combined in the same filter string):

* `date:2023-02-07T10:00:00+`: Returns objects from notifications generated after 2023-02-07T10:00:00 (UTC)
* `date:2023-02-07-`: Returns objects from notifications generated before 2023-03-07T00:00:00 (UTC)
* `origin:hunting`: Returns objects from notifications coming from Livehunt. Allowed values: `hunting, subscriptions`.
* `entity_id:objectId`: Return objects whose ID is `objectId`
* `entity_type:file`: Return only file objects. Allowed values: `file, domain, url, ip_address`
* `source_type:hunting_ruleset`: The type of source object that triggered the notification. Allowed values: `hunting_ruleset, retrohunt_job, collection, threat_actor`.
* `source_id:objectId`: The ID of the source object that triggered the notification. In the case of hunting the notification's source object ID corresponds to the hunting ruleset's ID.
* `notification_tag:ruleName`: Notifications with `ruleName` in their tags. In the case of notifications coming from Livehunt there are several tags in each notification, like the rule name or the username of the ruleset's owner.

Allowed orders:

* `date-` (default): Sorts by most recent notifications first.
* `date+`: Sorts by oldest notification first.

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
    "/ioc_stream": {
      "get": {
        "summary": "Get objects from the IoC Stream",
        "description": "",
        "operationId": "get-objects-from-the-ioc-stream",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "Number of objects to retrieve (max 40)",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
            }
          },
          {
            "name": "descriptors_only",
            "in": "query",
            "description": "The response returns only objects descriptors instead of whole VT objects",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "filter",
            "in": "query",
            "description": "Filter string",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "cursor",
            "in": "query",
            "description": "Continuation cursor",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "order",
            "in": "query",
            "description": "Sort order",
            "schema": {
              "type": "string"
            }
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
                    "value": "{\n\t\"meta\": {\n\t\t\"cursor\": \"Ck0KEQoEZGF0ZRIJCLnz1ObJg_0CEjRqEXN-dmlydXN0b3RhbGNsb3Vkch8LEhVJT0NTdHJlYW1Ob3RpZmljYXRpb24YsK2w2iEMGAAgAQ==\"\n\t},\n\t\"data\": [\n\t\t{\n\t\t\t\"type\": \"file\",\n\t\t\t\"id\": \"c9c4ee34d9c9f769f884f720e1d37ce1e864aae1be81a4a274bb1a88704cb11c\",\n\t\t\t\"context_attributes\": {\n\t\t\t\t\"notification_id\": \"9047905968\",\n\t\t\t\t\"origin\": \"hunting\",\n\t\t\t\t\"hunting_info\": {\n\t\t\t\t\t\"rule_name\": \"vulnerability_weaponization\"\n\t\t\t\t},\n\t\t\t\t\"tags\": [\n\t\t\t\t\t\"c9c4ee34d9c9f769f884f720e1d37ce1e864aae1be81a4a274bb1a88704cb11c\",\n\t\t\t\t\t\"vulnerability_weaponization\",\n\t\t\t\t\t\"ransomware\"\n\t\t\t\t],\n\t\t\t\t\"sources\": [\n\t\t\t\t\t{\n\t\t\t\t\t\t\"type\": \"hunting_ruleset\",\n\t\t\t\t\t\t\"id\": \"7926136120\",\n\t\t\t\t\t\t\"label\": \"Ransomware\"\n\t\t\t\t\t}\n\t\t\t\t],\n\t\t\t\t\"notification_date\": 1675778611\n\t\t\t}\n\t\t}\n\t],\n\t\"links\": {\n\t\t\"self\": \"https://www.virustotal.com/api/v3/ioc_stream?limit=1&filter=date%3A2023-02-07T10%3A00%3A00%2B%20entity_type%3Afile%20origin%3Ahunting&descriptors_only=true\",\n\t\t\"next\": \"https://www.virustotal.com/api/v3/ioc_stream?filter=date%3A2023-02-07T10%3A00%3A00-+entity_type%3Afile+origin%3Ahunting&cursor=Ck0KEQoEZGF0ZRIJCLnz1ObJg_0CEjRqEXN-dmlydXN0b3RhbGNsb3Vkch8LEhVJT0NTdHJlYW1Ob3RpZmljYXRpb24YsK2w2iEMGAAgAQ%3D%3D&limit=1&descriptors_only=true\"\n\t}\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "meta": {
                      "type": "object",
                      "properties": {
                        "cursor": {
                          "type": "string",
                          "example": "Ck0KEQoEZGF0ZRIJCLnz1ObJg_0CEjRqEXN-dmlydXN0b3RhbGNsb3Vkch8LEhVJT0NTdHJlYW1Ob3RpZmljYXRpb24YsK2w2iEMGAAgAQ=="
                        }
                      }
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "type": {
                            "type": "string",
                            "example": "file"
                          },
                          "id": {
                            "type": "string",
                            "example": "c9c4ee34d9c9f769f884f720e1d37ce1e864aae1be81a4a274bb1a88704cb11c"
                          },
                          "context_attributes": {
                            "type": "object",
                            "properties": {
                              "notification_id": {
                                "type": "string",
                                "example": "9047905968"
                              },
                              "origin": {
                                "type": "string",
                                "example": "hunting"
                              },
                              "hunting_info": {
                                "type": "object",
                                "properties": {
                                  "rule_name": {
                                    "type": "string",
                                    "example": "vulnerability_weaponization"
                                  }
                                }
                              },
                              "tags": {
                                "type": "array",
                                "items": {
                                  "type": "string",
                                  "example": "c9c4ee34d9c9f769f884f720e1d37ce1e864aae1be81a4a274bb1a88704cb11c"
                                }
                              },
                              "sources": {
                                "type": "array",
                                "items": {
                                  "type": "object",
                                  "properties": {
                                    "type": {
                                      "type": "string",
                                      "example": "hunting_ruleset"
                                    },
                                    "id": {
                                      "type": "string",
                                      "example": "7926136120"
                                    },
                                    "label": {
                                      "type": "string",
                                      "example": "Ransomware"
                                    }
                                  }
                                }
                              },
                              "notification_date": {
                                "type": "integer",
                                "example": 1675778611,
                                "default": 0
                              }
                            }
                          }
                        }
                      }
                    },
                    "links": {
                      "type": "object",
                      "properties": {
                        "self": {
                          "type": "string",
                          "example": "https://www.virustotal.com/api/v3/ioc_stream?limit=1&filter=date%3A2023-02-07T10%3A00%3A00%2B%20entity_type%3Afile%20origin%3Ahunting&descriptors_only=true"
                        },
                        "next": {
                          "type": "string",
                          "example": "https://www.virustotal.com/api/v3/ioc_stream?filter=date%3A2023-02-07T10%3A00%3A00-+entity_type%3Afile+origin%3Ahunting&cursor=Ck0KEQoEZGF0ZRIJCLnz1ObJg_0CEjRqEXN-dmlydXN0b3RhbGNsb3Vkch8LEhVJT0NTdHJlYW1Ob3RpZmljYXRpb24YsK2w2iEMGAAgAQ%3D%3D&limit=1&descriptors_only=true"
                        }
                      }
                    }
                  }
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
                    "value": "{\n\t\"error\": {\n\t\t\"message\": \"origin \\\"notHunting\\\" is not valid. Valid origins are: hunting,subscriptions\",\n\t\t\"code\": \"BadRequestError\"\n\t}\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "error": {
                      "type": "object",
                      "properties": {
                        "message": {
                          "type": "string",
                          "example": "origin \"notHunting\" is not valid. Valid origins are: hunting,subscriptions"
                        },
                        "code": {
                          "type": "string",
                          "example": "BadRequestError"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "deprecated": false,
        "security": []
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