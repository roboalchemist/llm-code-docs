# Source: https://developers.activecampaign.com/reference/retrieve-contact-geo-ips.md

# Retrieve a contacts list of geo-ips

```json GET /contacts/:id/geoIps (Example RESPONSE)
{
    "geoIps": [
        {
            "contact": "299",
            "campaignid": "0",
            "messageid": "0",
            "geoaddrid": "1",
            "ip4": "1234567890",
            "tstamp": "2023-12-20T13:26:08-06:00",
            "links": {
                "geoAddress": "https://:account.api-us1.com/api/3/geoIps/1/geoAddress"
            },
            "id": "1",
            "geoAddress": "1"
        },
        {
            "contact": "299",
            "campaignid": "0",
            "messageid": "0",
            "geoaddrid": "2",
            "ip4": "1234567890",
            "tstamp": "2023-12-20T13:35:23-06:00",
            "links": {
                "geoAddress": "https://:account.api-us1.com/api/3/geoIps/4/geoAddress"
            },
            "id": "4",
            "geoAddress": "2"
        }
    ]
}
```

> 📘 Geo Ips FAQ
>
> **Is the location accurate?**\
> IP address geolocation uses IP-to-location databases to determine which IP range the provided IP falls within. The primary source for IP address data is the regional Internet registries which allocate and distribute IP addresses amongst organizations located in their respective service regions. This will not be the *exact* location of the Contact.
>
> **How do I turn this into a Contact's coordinates or address info?**
>
> To get address information, use an `id` from a selected geo ip in the returned list, [and make a `GET` call to /geoAddress](https://developers.activecampaign.com/reference/retrieve-a-contacts-geo-ip-address)
>
> **Why are multiple locations listed?**
>
> If a Contact completes a form and the saved geo ip differs from the value currently saved, this list is appended. The highest `geoAddress` value is the most recent.
>
> **How is the geo ip saved?**\
> [A Contact's geo IP is retrieved when the Contact fills out any ActiveCampaign form.](https://help.activecampaign.com/hc/en-us/articles/115001663670-How-is-a-contact-s-location-determined-in-ActiveCampaign-)

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "v3",
    "version": "3"
  },
  "servers": [
    {
      "url": "https://{youraccountname}.api-us1.com/api/3",
      "variables": {
        "youraccountname": {
          "default": "youraccountname"
        }
      }
    }
  ],
  "components": {
    "securitySchemes": {
      "sec0": {
        "type": "apiKey",
        "name": "Api-Token",
        "in": "header",
        "x-default": ""
      }
    }
  },
  "security": [
    {
      "sec0": []
    }
  ],
  "paths": {
    "/contacts/{id}/geoIps": {
      "get": {
        "summary": "Retrieve a contacts list of geo-ips",
        "description": "",
        "operationId": "retrieve-contact-geo-ips",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of the contact",
            "schema": {
              "type": "integer",
              "format": "int32"
            },
            "required": true
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n\t\"geoIps\": [{\n\t\t\"contact\": \"49\",\n\t\t\"campaignid\": \"11\",\n\t\t\"messageid\": \"12\",\n\t\t\"geoaddrid\": \"2\",\n\t\t\"ip4\": \"1123637995\",\n\t\t\"tstamp\": \"2021-05-12T11:10:06-05:00\",\n\t\t\"links\": {\n\t\t\t\"geoAddress\": \"https://:account.api-us1.com/api/3/geoIps/4/geoAddress\"\n\t\t},\n\t\t\"id\": \"4\",\n\t\t\"geoAddress\": \"2\"\n\t}]\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "geoIps": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "contact": {
                            "type": "string",
                            "example": "49"
                          },
                          "campaignid": {
                            "type": "string",
                            "example": "11"
                          },
                          "messageid": {
                            "type": "string",
                            "example": "12"
                          },
                          "geoaddrid": {
                            "type": "string",
                            "example": "2"
                          },
                          "ip4": {
                            "type": "string",
                            "example": "1123637995"
                          },
                          "tstamp": {
                            "type": "string",
                            "example": "2021-05-12T11:10:06-05:00"
                          },
                          "links": {
                            "type": "object",
                            "properties": {
                              "geoAddress": {
                                "type": "string",
                                "example": "https://:account.api-us1.com/api/3/geoIps/4/geoAddress"
                              }
                            }
                          },
                          "id": {
                            "type": "string",
                            "example": "4"
                          },
                          "geoAddress": {
                            "type": "string",
                            "example": "2"
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          },
          "404": {
            "description": "404",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"message\": \"No Result found for Subscriber with id 100\"\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "message": {
                      "type": "string",
                      "example": "No Result found for Subscriber with id 100"
                    }
                  }
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
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```