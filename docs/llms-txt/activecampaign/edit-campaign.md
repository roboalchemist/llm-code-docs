# Source: https://developers.activecampaign.com/reference/edit-campaign.md

# Edit campaign

```json PUT /campaigns/{id}/edit (Example RESPONSE 200)
{
    "id": 29,
    "name": "MY SUPER CAMPAIGN",
    "type": "single",
    "canSplitContent": false,
    "segmentId": 0,
    "scheduledDate": null,
    "addressId": 2,
    "publicCampaignArchive": true,
    "googleAnalyticsLinkTrackingEnabled": true,
    "googleAnalyticsCampaignName": "",
    "readTrackingEnabled": false,
    "linkTrackingEnabled": false,
    "replyTrackingEnabled": true,
    "status": 0,
    "listIds": null,
    "selectedAddressInfo": {
        "id": "2",
        "companyName": "companyName",
        "address1": "Address line 1",
        "address2": "Address line 2",
        "city": "city",
        "state": "",
        "postalCode": "32-085",
        "countryCode": "PL",
        "isDefault": true
    },
    "automationId": 0,
    "selectedListInfo": [],
    "selectedSegmentInfo": null,
    "readTrackingAutomationsCount": 0,
    "replyTrackingAutomationsCount": 0
}
```

```Text PUT /campaigns/{id}/edit (Example RESPONSE 406)
{
    'message': 'Empty request body'
}
```

```Text PUT /campaigns/{id}/edit (Example RESPONSE 400)
{
    "message": "Campaign not found"
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
    "/campaigns/{id}/edit": {
      "put": {
        "summary": "Edit campaign",
        "description": "",
        "operationId": "edit-campaign",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "schema": {
              "type": "integer",
              "format": "int32"
            },
            "required": true
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {
                    "type": "string",
                    "description": "Campaign name"
                  },
                  "type": {
                    "type": "string",
                    "description": "Campaign type"
                  },
                  "segmentId": {
                    "type": "string",
                    "description": "Id of selected segment. Both integer segment id's and string based segment id's are supported."
                  },
                  "addressId": {
                    "type": "integer",
                    "description": "Id of selected address",
                    "format": "int32"
                  },
                  "listIds": {
                    "type": "array",
                    "description": "Array of selected lists ids",
                    "items": {
                      "type": "integer",
                      "format": "int32"
                    }
                  },
                  "replyTrackingEnabled": {
                    "type": "boolean",
                    "description": "Turn on/off reply tracking"
                  },
                  "linkTrackingEnabled": {
                    "type": "boolean",
                    "description": "Turn on/off link tracking"
                  },
                  "googleAnalyticsLinkTrackingEnabled": {
                    "type": "boolean",
                    "description": "Turn on/off google analytics link tracking"
                  },
                  "googleAnalyticsCampaignName": {
                    "type": "string",
                    "description": "Name of campaign in google analytics"
                  },
                  "readTrackingEnabled": {
                    "type": "boolean",
                    "description": "Turn on/off read tracking"
                  },
                  "sendToExistingSubscribers": {
                    "type": "boolean",
                    "description": "Should send only to existing customers"
                  },
                  "canSplitContent": {
                    "type": "boolean",
                    "description": "Campaign can contains split content"
                  },
                  "recurring": {
                    "type": "boolean",
                    "description": "Is campaign recurring"
                  },
                  "responderDaysOffset": {
                    "type": "integer",
                    "description": "Determine value of responder offset in days",
                    "format": "int32"
                  },
                  "responderHoursOffset": {
                    "type": "integer",
                    "description": "Determine value of responder offset in hours",
                    "format": "int32"
                  },
                  "scheduledDate": {
                    "type": "string",
                    "description": "Date of sending"
                  },
                  "reminderField": {
                    "type": "string",
                    "description": "Field basic on witch reminder will be triggered"
                  },
                  "reminderOffset": {
                    "type": "integer",
                    "description": "Value of reminder offset",
                    "format": "int32"
                  },
                  "reminderOffsetType": {
                    "type": "string",
                    "description": "Type of reminder offset"
                  },
                  "reminderType": {
                    "type": "string",
                    "description": "Format of reminder date"
                  },
                  "rssInterval": {
                    "type": "integer",
                    "description": "Interval for RSS",
                    "format": "int32"
                  },
                  "splitType": {
                    "type": "string",
                    "description": "Type of split campaign"
                  },
                  "splitWinnerWaitPeriod": {
                    "type": "integer",
                    "description": "Period wait time",
                    "format": "int32"
                  },
                  "splitWinnerWaitPeriodType": {
                    "type": "string",
                    "description": "Determine period type"
                  },
                  "publicCampaignArchive": {
                    "type": "boolean",
                    "description": "Is campaign public"
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