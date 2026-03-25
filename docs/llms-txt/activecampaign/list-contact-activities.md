# Source: https://developers.activecampaign.com/reference/list-contact-activities.md

# List a contact's activities

View your contact's recent activity. The activity is generated when a contact is retrieved via /api/3/contacts/[contactID]. This endpoint should be used after retrieving a contact to obtain the latest data. This is useful for searching for contacts that match certain criteria - such as being part of a certain list, or having a specific custom field value.

> 📘 Contact ID parameter is now required
>
> A contact ID is required to access this endpoint. This endpoint does not support multiple contact IDs with a single call.

> 🚧 Organization-Related Nodes Have Been Deprecated
>
> Contact-Organization relationships are now managed through [Account-Contact end points](account-contacts)

<br />

### **Response Details**

* **`subscriberid`**: The unique ID representing the contact (or subscriber) associated with the activity.

* **`reference_type`**: Specifies the type of activity being recorded. The activity types can include, but are not limited to:
  * `SubscriberEmail`: Activity related to email interactions of a subscriber.
  * `DealTask`: Refers to tasks related to a deal, such as a task assignment or completion.
  * `SubscriberList`: Actions related to list subscriptions (e.g., subscribing or unsubscribing).
  * `SubscriberSeries`: Activities associated with an automation sequence, such as starting or completing a step.
  * `Log`: General logs related to subscriber actions.
  * `Update`: Logs an update to a contact, deal, or list.
  * `DealActivity`: Activities related to a deal, often involving interactions such as emails or tasks.
  * `Forward`: Forwarding actions related to emails.
  * `Reply`: Responses to emails or messages.
  * `Note`: Notes added to a subscriber or deal record.
  * `LinkData`: Tracks interactions with links, such as clicks in emails.
  * `MppLinkData`: Link interactions via Apple's Mail Privacy Protection.
  * `SmsLog`: Tracks SMS messages sent to a contact.
  * `SmsReply`: Tracks replies to SMS messages.
  * `SmsUnsub`: Unsubscribe actions via SMS.
  * `TrackingLog`: Tracks interactions through website or email link tracking.
  * `SeriesBlock`: A step or block in an automation series.
  * `SubscriberLog`: Logs general subscriber actions.
  * `SubscriberConversion`: Tracks a subscriber’s conversion event, such as completing a purchase.
  * `FbAudienceContactLog`: Tracks actions related to Facebook Custom Audience contact interactions.
  * `EcomOrderActivity`: Activities related to eCommerce orders, such as tracking purchases or cart interactions.

* **`reference_id`**: A unique ID referencing the specific object or event involved in the activity (e.g., a task, note, or automation step).

* **`reference_action`**: Describes the action performed in relation to the `reference_type`. Some common examples include:
  * `"start"`: Typically refers to the initiation of an automation or series step.
  * `"complete"`: Indicates the completion of an automation or series step.
  * `"subscribe"`: Refers to a subscription action, such as when a contact subscribes to a list.
  * Other actions might include `"add"`, `"update"`, or be left as an empty string (`""`) depending on the context.

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
    "/activities": {
      "get": {
        "summary": "List a contact's activities",
        "description": "View your contact's recent activity. The activity is generated when a contact is retrieved via /api/3/contacts/[contactID]. This endpoint should be used after retrieving a contact to obtain the latest data. This is useful for searching for contacts that match certain criteria - such as being part of a certain list, or having a specific custom field value.",
        "operationId": "list-contact-activities",
        "parameters": [
          {
            "name": "contact",
            "in": "query",
            "description": "Required Contact ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "after",
            "in": "query",
            "description": "Filter for activities after a specific DateTime",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "include",
            "in": "query",
            "description": "Activities to include: notes, notes.user, recipients, recipients.recipient, reference, reference.automation, reference.campaign, reference.campaign.campaignList, reference.campaign.campaignMessage, reference.campaignMessage, reference.contact, reference.contactList, reference.contactList.list, reference.deal, reference.deal.contact, reference.dealTasktype, reference.link, reference.list, reference.log, reference.log.campaign, reference.log.contact, reference.log.message, reference.message, reference.note, reference.sms, reference.sms.automation, user",
            "schema": {
              "type": "string",
              "default": "activities to include"
            }
          },
          {
            "name": "orders[tstamp]",
            "in": "query",
            "description": "Order activities by tstamp",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "emails",
            "in": "query",
            "description": "FALSE: Excludes email data fields under each activity. No specific connection to emails is mentioned in the JSON data.​ TRUE: Returns deal activities that include email data fields like \"connection_email.\" Each deal activity specifies the addition of email connection information along with timestamps and relevant metadata.",
            "schema": {
              "type": "boolean",
              "default": false
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
                    "value": "{\n\tcontacts: [{\n    cdate: \"2018-02-13T13:25:54-06:00\",\n    email: \"test@example.com\",\n    firstName: \"Test\",\n    lastName: \"Contact\",\n    created_timestamp: \"2019-11-13 16:18:00\",\n    updated_timestamp: \"2021-04-06 11:25:59\",\n    id: \"4\"\n  }],\n  activityRecipients: [{\n    reltype: \"Subscriber\",\n    relid: \"4\",\n    activityid: \"865\",\n    recipient: {\n    type: \"contact\",\n    id: \"4\"\n  }],\n\tactivities: [{\n    tstamp: \"2019-01-03T12:16:19-06:00\",\n    subscriberid: \"4\",\n    reference_type: \"SubscriberEmail\",\n    reference_id: \"13\",\n    reference_action: \"\",\n    jsonData: null,\n    userid: \"1\",\n    permission: \"\",\n    referenceModelName: \"contact-email\",\n    notes: [ ],\n    recipients: [\n\t    \"1496\"\n    ],\n    reference: {\n    type: \"contact-email\",\n    id: \"13\"\n    },\n    user: \"1\",\n    id: \"865\"\n  }],\n\tmeta: {\n\t\ttotal: \"1\"\n\t}\n}"
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
    "explorer-enabled": false,
    "proxy-enabled": false
  },
  "x-readme-fauxas": true
}
```