# Source: https://virustotal.readme.io/reference/search-iocs-inside-a-collection.md

# 🔒 Search IoCs inside a collection

> 🚧 Deprecated endpoint. This has been replaced by Google Threat Intelligence
>
> We are gearing up to the transition into Google Threat Intelligence! The endpoints are documented at [**Threat Landscape** -> **Threat Actors, Malware & Tools, Campaigns, IoC Collections** section](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections). Note that when upgrading to Google Threat Intelligence you will enjoy a much larger knowledge base of IoC collections, threat actors, malware, toolkits and campaigns.
>
> * For **searching IoCs inside a collection**, refer to [`/collections/{id}/search` endpoint documented here](https://gtidocs.virustotal.com/reference/search-iocs-inside-a-threat).
> * Find the **new IoC collection object** definition [here](https://gtidocs.virustotal.com/reference/ioc-collection-object).
> * Find additional information related to the new endpoints [here](https://gtidocs.virustotal.com/reference/threat-actors-malware-tools-campaigns-ioc-collections).

> 🚧 Special privileges required
>
> This endpoint is only available to users with the [Threat Landscape module](https://www.virustotal.com/gui/threat-landscape-overview).

Allows to search IoCs inside a collection using VT Intelligence queries.

The expected input is the same as [/intelligence/search](https://virustotal.readme.io/reference/intelligence-search). By default it searches files, in order to search other entities use `entity:domain/ip/url`.

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
    "/collections/{id}/search": {
      "get": {
        "summary": "🔒 Search IoCs inside a collection",
        "description": "",
        "operationId": "search-iocs-inside-a-collection",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "Collection's ID",
            "schema": {
              "type": "string"
            },
            "required": true
          },
          {
            "name": "query",
            "in": "query",
            "description": "Intelligence query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of IoCs to retrieve (max 40)",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 10
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
            "description": "Sorting order",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "attributes",
            "in": "query",
            "description": "Comma-separated attributes to return from the resulting IoCs",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "relationships",
            "in": "query",
            "description": "Comma-separated name of relationships descriptors to return from the IoCs",
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
                    "value": "{\n\"meta\": {\n  \"cursor\": <string>,\n  \"total_hits\": <int>,\n  \"allowed_orders\": [<string>, ...]\n},\n\"data\": [\n  <IOC>,\n  <IOC>,\n  ...\n],\n\"links\": {\n  \"self\": <string>,\n  \"next\": <string>\n}"
                  }
                }
              },
              "text/plain": {
                "examples": {
                  "Example": {
                    "value": "{\n\t\"meta\": {\n\t\t\"cursor\": \"eJwNyTEOgzAMBdAroZSVhYJQkOwo6ANK1nao7GTqAFgcvn3ru3cbHZtvGOkIw_j1z7kS-k9GvMh6IZslQx__t7RvkiqdjEUTuNCwtlm0ZbwcybsQ9ODqHVm8AoqEiTVMq7HE05emu381USYK\",\n\t\t\"total_hits\": 138,\n\t\t\"allowed_orders\": [\n\t\t\t\"first_submission_date\",\n\t\t\t\"last_submission_date\",\n\t\t\t\"positives\",\n\t\t\t\"times_submitted\",\n\t\t\t\"size\",\n\t\t\t\"unique_sources\"\n\t\t]\n\t},\n\t\"data\": [\n\t\t{\n\t\t\t\"attributes\": {\n\t\t\t\t\"names\": [\n\t\t\t\t\t\"%windir%\\\\system32\\\\ZHANcETwJnzF\\\\jKbD.dll\",\n\t\t\t\t\t\"08039481f17de1a125763d6dadc9a91615fa027ad42a4f42d886b94063a94822.exe\",\n\t\t\t\t\t\"%windir%\\\\system32\\\\GRygLTtvoipYdeQ\\\\ooKzoWPK.dll\",\n\t\t\t\t\t\"emotet_epoch4.dll\"\n\t\t\t\t]\n\t\t\t},\n\t\t\t\"type\": \"file\",\n\t\t\t\"id\": \"08039481f17de1a125763d6dadc9a91615fa027ad42a4f42d886b94063a94822\",\n\t\t\t\"links\": {\n\t\t\t\t\"self\": \"https://www.virustotal.com/api/v3/files/08039481f17de1a125763d6dadc9a91615fa027ad42a4f42d886b94063a94822\"\n\t\t\t}\n\t\t},\n\t\t{\n\t\t\t\"attributes\": {\n\t\t\t\t\"names\": [\n\t\t\t\t\t\"E:\\\\\\\\2019\\\\\\\\VirusShare_371\\\\\\\\VirusShare_5e9e1b4354594e0e787c7a03afa0e677\",\n\t\t\t\t\t\"Trojan-Banker.Win32.Emotet.dilb.5e9e1b4354594e0e787c7a03afa0e677\",\n\t\t\t\t\t\"EncPEConstKey_OFS_0002d425_KEY_00000000_Emotet_InternetFile_dec_165.227.213.173_00000000.decompressed.cut\"\n\t\t\t\t]\n\t\t\t},\n\t\t\t\"type\": \"file\",\n\t\t\t\"id\": \"f10ae4230c32ce97563aecbc154da3e058f9857627e1906b634299c8cd8e3641\",\n\t\t\t\"links\": {\n\t\t\t\t\"self\": \"https://www.virustotal.com/api/v3/files/f10ae4230c32ce97563aecbc154da3e058f9857627e1906b634299c8cd8e3641\"\n\t\t\t}\n\t\t}\n\t],\n\t\"links\": {\n\t\t\"self\": \"https://www.virustotal.com/api/v3/collections/malpedia_win_emotet/search?query=name%3Aemotet&attributes=names&limit=2\",\n\t\t\"next\": \"https://www.virustotal.com/api/v3/collections/malpedia_win_emotet/search?cursor=eJwNyTEOgzAMBdAroZSVhYJQkOwo6ANK1nao7GTqAFgcvn3ru3cbHZtvGOkIw_j1z7kS-k9GvMh6IZslQx__t7RvkiqdjEUTuNCwtlm0ZbwcybsQ9ODqHVm8AoqEiTVMq7HE05emu381USYK&query=name%3Aemotet&limit=2&attributes=names\"\n\t}\n}"
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
                          "example": "eJwNyTEOgzAMBdAroZSVhYJQkOwo6ANK1nao7GTqAFgcvn3ru3cbHZtvGOkIw_j1z7kS-k9GvMh6IZslQx__t7RvkiqdjEUTuNCwtlm0ZbwcybsQ9ODqHVm8AoqEiTVMq7HE05emu381USYK"
                        },
                        "total_hits": {
                          "type": "integer",
                          "example": 138,
                          "default": 0
                        },
                        "allowed_orders": {
                          "type": "array",
                          "items": {
                            "type": "string",
                            "example": "first_submission_date"
                          }
                        }
                      }
                    },
                    "data": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "attributes": {
                            "type": "object",
                            "properties": {
                              "names": {
                                "type": "array",
                                "items": {
                                  "type": "string",
                                  "example": "%windir%\\system32\\ZHANcETwJnzF\\jKbD.dll"
                                }
                              }
                            }
                          },
                          "type": {
                            "type": "string",
                            "example": "file"
                          },
                          "id": {
                            "type": "string",
                            "example": "08039481f17de1a125763d6dadc9a91615fa027ad42a4f42d886b94063a94822"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "self": {
                                "type": "string",
                                "example": "https://www.virustotal.com/api/v3/files/08039481f17de1a125763d6dadc9a91615fa027ad42a4f42d886b94063a94822"
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
                          "example": "https://www.virustotal.com/api/v3/collections/malpedia_win_emotet/search?query=name%3Aemotet&attributes=names&limit=2"
                        },
                        "next": {
                          "type": "string",
                          "example": "https://www.virustotal.com/api/v3/collections/malpedia_win_emotet/search?cursor=eJwNyTEOgzAMBdAroZSVhYJQkOwo6ANK1nao7GTqAFgcvn3ru3cbHZtvGOkIw_j1z7kS-k9GvMh6IZslQx__t7RvkiqdjEUTuNCwtlm0ZbwcybsQ9ODqHVm8AoqEiTVMq7HE05emu381USYK&query=name%3Aemotet&limit=2&attributes=names"
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