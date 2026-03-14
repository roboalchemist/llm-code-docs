# Source: https://developers.activecampaign.com/reference/retrieve-a-contacts-geo-ip-address.md

# Retrieve a contacts geo IP address

> 📘 Getting a Contact's geo-ip ID
>
> Retrieve a contacts list of geo-ips with a **GET** call to: `/contacts/{id}/geoIps`
>
> [Documentation](https://developers.activecampaign.com/reference/retrieve-contact-geo-ips)

> 📘 Geo IP/Address FAQ:
>
> **Is the location accurate?**\
> IP address geolocation uses IP-to-location databases to determine which IP range the provided IP falls within. The primary source for IP address data is the regional Internet registries which allocate and distribute IP addresses amongst organizations located in their respective service regions. This will not be the exact location of the Contact.
>
> **How is the geo ip saved?**\
> [A Contact's geo IP is retrieved when the Contact fills out any ActiveCampaign form.](https://help.activecampaign.com/hc/en-us/articles/115001663670-How-is-a-contact-s-location-determined-in-ActiveCampaign-?_ga=2.3826032.110179971.1702919502-1284198313.1671482480)

```json GET /contacts/:id/geoIps (Example RESPONSE)
{
    "geoAddress": {
        "ip4": "1234567890",
        "country2": "US",
        "country": "United States",
        "state": "New York",
        "city": "New York",
        "zip": "10001",
        "area": "0",
        "lat": "40.7128",
        "lon": "-74.0060",
        "tz": "America/Chicago",
        "tstamp": "2023-12-20T14:14:46-06:00",
        "links": [],
        "id": "3"
    }
}
```

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
    "/geoIps/{geoAddressID}/geoAddress": {
      "get": {
        "summary": "Retrieve a contacts geo IP address",
        "description": "",
        "operationId": "retrieve-a-contacts-geo-ip-address",
        "parameters": [
          {
            "name": "geoAddressID",
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
                    "value": "{\n    \"geoAddress\": {\n        \"ip4\": \"1234567890\",\n        \"country2\": \"US\",\n        \"country\": \"United States\",\n        \"state\": \"New York\",\n        \"city\": \"New York\",\n        \"zip\": \"10001\",\n        \"area\": \"0\",\n        \"lat\": \"40.7128\",\n        \"lon\": \"-74.0060\",\n        \"tz\": \"America/Chicago\",\n        \"tstamp\": \"2023-12-20T14:14:46-06:00\",\n        \"links\": [],\n        \"id\": \"3\"\n    }\n}"
                  }
                },
                "schema": {
                  "type": "object",
                  "properties": {
                    "geoAddress": {
                      "type": "object",
                      "properties": {
                        "ip4": {
                          "type": "string",
                          "example": "1234567890"
                        },
                        "country2": {
                          "type": "string",
                          "example": "US"
                        },
                        "country": {
                          "type": "string",
                          "example": "United States"
                        },
                        "state": {
                          "type": "string",
                          "example": "New York"
                        },
                        "city": {
                          "type": "string",
                          "example": "New York"
                        },
                        "zip": {
                          "type": "string",
                          "example": "10001"
                        },
                        "area": {
                          "type": "string",
                          "example": "0"
                        },
                        "lat": {
                          "type": "string",
                          "example": "40.7128"
                        },
                        "lon": {
                          "type": "string",
                          "example": "-74.0060"
                        },
                        "tz": {
                          "type": "string",
                          "example": "America/Chicago"
                        },
                        "tstamp": {
                          "type": "string",
                          "example": "2023-12-20T14:14:46-06:00"
                        },
                        "links": {
                          "type": "array"
                        },
                        "id": {
                          "type": "string",
                          "example": "3"
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