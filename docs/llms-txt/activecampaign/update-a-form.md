# Source: https://developers.activecampaign.com/reference/update-a-form.md

# put

```json PUT /forms/:id (REQUEST Example)
{
  "form": {
    "name": "Form updated",
    "action": "",
    "actiondata": {
      "actions": [
        {
          "title": "Subscribe to a list",
          "type": "subscribe-to-list",
          "id": "df6ce7f4-c6de-42d9-a796-000d40bcf099",
          "listName": "Generall list",
          "list": "1"
        },
        {
          "title": "Subscribe to an SMS list",
          "type": "subscribe-to-sms-list",
          "sms_consent": true,
          "id": "bb7a4592-0265-4dfb-9810-a9a8f987c64f",
          "listName": "Master SMS List",
          "list": "7"
        },
        {
          "title": "Add a tag",
          "type": "add-a-tag",
          "tag": "Welcome",
          "id": "103b53ef-b234-4052-b342-a45d2f42259c"
        },
        {
          "title": "Add to a deal",
          "type": "add-to-deal",
          "id": "2d2ba5e7-2983-4161-8234-76b547767405",
          "pipeline": "1",
          "dealGroupTitle": "First Pipline",
          "email": "Enter an email address",
          "dealcurrency": "usd",
          "dealvalue": 0,
          "dealtitle": "New deal from form ",
          "stage": "2",
          "dealStageTitle": "In Contact"
        },
        {
          "title": "Email results",
          "type": "email-results",
          "email": "test@activecampaign.com",
          "subject": "Form submission results",
          "fromemail": "test@activecampaign.com",
          "fromname": "John Doe",
          "id": "b48080d2-732a-4865-bed5-72b37d88f442"
        }
      ]
    },
    "submit": "show-thank-you",
    "submitdata": {},
    "url": "",
    "layout": "inline-form",
    "title": "",
    "body": "",
    "button": "Submit",
    "thanks": "Thanks for signing up!",
    "style": {
      "ac_branding": true,
      "background": "FFFFFF",
      "border": {
        "color": "B0B0B0",
        "radius": 0,
        "style": "solid",
        "width": 0
      },
      "button": {
        "background": "004CFF",
        "border": {
          "color": "333333",
          "radius": 4,
          "style": "solid",
          "width": 0
        },
        "fontcolor": "FFFFFF",
        "padding": 10
      },
      "dark": true,
      "fontFamily": "\"IBM Plex Sans\", Helvetica, sans-serif",
      "fontcolor": "000000",
      "layout": "normal",
      "padding": {
        "bottom": 20,
        "left": 20,
        "right": 20,
        "top": 20
      },
      "width": 500
    },
    "options": {
      "blanks_overwrite": true,
      "confaction": "show-message",
      "sendoptin": true,
      "confform": "50",
      "optin_created": true,
      "optin_id": 108,
      "useBgColor": true,
      "useBgImage": false
    },
    "cfields": [
      {
        "type": "header",
        "header": "Subscribe for Email Updates",
        "class": "_x19620520"
      },
      {
        "type": "html",
        "html": "<p>Add a descriptive message telling what your visitor is signing up for here.</p>",
        "header": "undefined",
        "class": "_x90115161"
      },
      {
        "type": "fullname",
        "header": "Full Name",
        "default_text": "Type your name",
        "class": "_x21466802"
      },
      {
        "id": "email",
        "type": "email",
        "header": "Email",
        "default_text": "Type your email",
        "required": true,
        "class": "_x32875615"
      },
      {
        "header": "Phone",
        "default_text": "Type your phone number",
        "consent_message": "By submitting this form and signing up for texts, you consent to receive marketing text messages (e.g. promos, cart reminders) from [Your Company Name] at the number provided. Consent is not a condition of purchase. Msg & data rates may apply. Msg frequency varies. Unsubscribe at any time by replying STOP.",
        "id": "phone",
        "type": "phone",
        "required": true,
        "sms_consent": true,
        "request_confirmation": true,
        "phone_prefix": "IE",
        "phone_validation": true,
        "class": "_x64021393"
      },
      {
        "type": "image",
        "multiple": true,
        "reactField": true,
        "class": "_x25795271"
      }
    ],
    "parentformid": 0,
    "cdate": "2025-06-17T13:14:46.000Z",
    "screenshot": null,
    "defaultscreenshot": null,
    "sitescreenshot": null,
    "entries": 0,
    "contacts": null,
    "deals": null,
    "address": null
  }
}
```

```Text PUT /forms/:id (Example Response)
{
  "form": {
    "name": "Form Updated",
    "action": "",
    "actiondata": {
      "actions": [
        {
          "title": "Subscribe to a list",
          "type": "subscribe-to-list",
          "id": "df6ce7f4-c6de-42d9-a796-000d40bcf099",
          "listName": "Generall List",
          "list": "1"
        },
        {
          "title": "Subscribe to an SMS list",
          "type": "subscribe-to-sms-list",
          "sms_consent": true,
          "id": "bb7a4592-0265-4dfb-9810-a9a8f987c64f",
          "listName": "Master SMS List",
          "list": "7"
        },
        {
          "title": "Add a tag",
          "type": "add-a-tag",
          "tag": "Welcome",
          "id": "103b53ef-b234-4052-b342-a45d2f42259c"
        },
        {
          "title": "Add to a deal",
          "type": "add-to-deal",
          "id": "2d2ba5e7-2983-4161-8234-76b547767405",
          "pipeline": "1",
          "dealGroupTitle": "First Pipline",
          "email": "Enter an email address",
          "dealcurrency": "usd",
          "dealvalue": 0,
          "dealtitle": "New deal from form ",
          "stage": "2",
          "dealStageTitle": "In Contact"
        },
        {
          "title": "Email results",
          "type": "email-results",
          "email": "test@activecampaign.com",
          "subject": "Form submission results",
          "fromemail": "test@activecampaign.com",
          "fromname": "John Doe",
          "id": "b48080d2-732a-4865-bed5-72b37d88f442"
        }
      ]
    },
    "submit": "show-thank-you",
    "submitdata": {},
    "url": "",
    "layout": "inline-form",
    "title": "",
    "body": "",
    "button": "Submit",
    "thanks": "Thanks for signing up!",
    "style": {
      "ac_branding": true,
      "background": "FFFFFF",
      "border": {
        "color": "B0B0B0",
        "radius": 0,
        "style": "solid",
        "width": 0
      },
      "button": {
        "background": "004CFF",
        "border": {
          "color": "333333",
          "radius": 4,
          "style": "solid",
          "width": 0
        },
        "fontcolor": "FFFFFF",
        "padding": 10
      },
      "dark": true,
      "fontFamily": "\"IBM Plex Sans\", Helvetica, sans-serif",
      "fontcolor": "000000",
      "layout": "normal",
      "padding": {
        "bottom": 20,
        "left": 20,
        "right": 20,
        "top": 20
      },
      "width": 500
    },
    "options": {
      "blanks_overwrite": true,
      "confaction": "show-message",
      "sendoptin": true,
      "confform": "50",
      "optin_created": true,
      "optin_id": 108,
      "useBgColor": true,
      "useBgImage": false
    },
    "cfields": [
      {
        "type": "header",
        "header": "Subscribe for Email Updates",
        "class": "_x19620520"
      },
      {
        "type": "html",
        "html": "<p>Add a descriptive message telling what your visitor is signing up for here.</p>",
        "header": "undefined",
        "class": "_x90115161"
      },
      {
        "type": "fullname",
        "header": "Full Name",
        "default_text": "Type your name",
        "class": "_x21466802"
      },
      {
        "id": "email",
        "type": "email",
        "header": "Email",
        "default_text": "Type your email",
        "required": true,
        "class": "_x32875615"
      },
      {
        "header": "Phone",
        "default_text": "Type your phone number",
        "consent_message": "By submitting this form and signing up for texts, you consent to receive marketing text messages (e.g. promos, cart reminders) from [Your Company Name] at the number provided. Consent is not a condition of purchase. Msg & data rates may apply. Msg frequency varies. Unsubscribe at any time by replying STOP.",
        "id": "phone",
        "type": "phone",
        "required": true,
        "sms_consent": true,
        "request_confirmation": true,
        "phone_prefix": "IE",
        "phone_validation": true,
        "class": "_x64021393"
      },
      {
        "type": "image",
        "multiple": true,
        "reactField": true,
        "class": "_x25795271"
      }
    ],
    "parentformid": 0,
    "userid": "1",
    "addressid": 0,
    "cdate": "2025-06-17T08:14:46-05:00",
    "udate": "2025-06-18T00:36:22-05:00",
    "links": {
      "address": "https://test.activehosted.com/api/3/forms/49/address"
    },
    "id": "49",
    "address": null
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
    "/forms/{id}": {
      "put": {
        "description": "",
        "operationId": "put_forms{id}",
        "responses": {
          "200": {
            "description": ""
          }
        },
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "",
            "schema": {
              "type": "integer",
              "default": ""
            }
          }
        ]
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