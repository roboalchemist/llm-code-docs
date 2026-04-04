# Source: https://developers.activecampaign.com/reference/list-all-contacts.md

# List, search, and filter contacts

Use this API endpoint to list all contacts, search contacts, or filter contacts by many criteria. For example, search for specific contacts by email, list, account.

> 🚧 Organization-Related Nodes Have Been Deprecated
>
> Contact-Organization relationships are now managed through [Account-Contact end points](reference#account-contacts)

> 👍 Performance Tip for Pagination
>
> Accounts with many Contacts may encounter slower responses when using the `offset` parameter to paginate with this endpoint. For best performance sort using `orders[id]=ASC` and use the `id_greater` parameter to paginate. This is especially important when calling this endpoint frequently, such as when retrieving many or all Contacts from an account.
>
> Note that when using the `segmentid` parameter, best performance will be achieved by: paginating using the `offset` parameter and not using any `orders` parameter.

```json GET /contacts (Example RESPONSE)
{
   "contacts":[
      {
         "cdate":"2017-01-25T23:58:14-06:00",
         "email":"janedoe@example.com",
         "phone":"3120000000",
         "firstName":"John",
         "lastName":"Doe",
         "orgid":"0",
         "segmentio_id":"",
         "bounced_hard":"0",
         "bounced_soft":"0",
         "bounced_date":"0000-00-00",
         "ip":"0",
         "ua":"",
         "hash":"31e076c964f4262817f9ba302c96e1c6",
         "socialdata_lastcheck":"0000-00-00 00:00:00",
         "email_local":"",
         "email_domain":"",
         "sentcnt":"0",
         "rating_tstamp":"0000-00-00",
         "gravatar":"3",
         "deleted":"0",
         "adate":"2017-02-22 15:26:24",
         "udate":"2017-01-25T23:58:14-06:00",
         "edate":"2017-01-27 14:44:13",
         "scoreValues":[

         ],
         "links":{
            "bounceLogs":"https://:account.api-us1.com/api/:version/contacts/68/bounceLogs",
            "contactAutomations":"https://:account.api-us1.com/api/:version/contacts/68/contactAutomations",
            "contactData":"https://:account.api-us1.com/api/:version/contacts/68/contactData",
            "contactGoals":"https://:account.api-us1.com/api/:version/contacts/68/contactGoals",
            "contactLists":"https://:account.api-us1.com/api/:version/contacts/68/contactLists",
            "contactLogs":"https://:account.api-us1.com/api/:version/contacts/68/contactLogs",
            "contactTags":"https://:account.api-us1.com/api/:version/contacts/68/contactTags",
            "contactDeals":"https://:account.api-us1.com/api/:version/contacts/68/contactDeals",
            "deals":"https://:account.api-us1.com/api/:version/contacts/68/deals",
            "fieldValues":"https://:account.api-us1.com/api/:version/contacts/68/fieldValues",
            "geoIps":"https://:account.api-us1.com/api/:version/contacts/68/geoIps",
            "notes":"https://:account.api-us1.com/api/:version/contacts/68/notes",
            "organization":"https://:account.api-us1.com/api/:version/contacts/68/organization",
            "plusAppend":"https://:account.api-us1.com/api/:version/contacts/68/plusAppend",
            "trackingLogs":"https://:account.api-us1.com/api/:version/contacts/68/trackingLogs",
            "scoreValues":"https://:account.api-us1.com/api/:version/contacts/68/scoreValues"
         },
         "id":"68",
         "organization":null
      },
      {
         "cdate":"2017-02-09T12:14:58-06:00",
         "email":"aaronallen@example.com",
         "phone":"",
         "firstName":"Aaron",
         "lastName":"Allen",
         "orgid":"14",
         "segmentio_id":"",
         "bounced_hard":"0",
         "bounced_soft":"0",
         "bounced_date":"0000-00-00",
         "ip":"0",
         "ua":"",
         "hash":"31b92c033c3e55de6d9eb9c44ee1bfa5",
         "socialdata_lastcheck":"0000-00-00 00:00:00",
         "email_local":"",
         "email_domain":"",
         "sentcnt":"0",
         "rating_tstamp":"0000-00-00",
         "gravatar":"1",
         "deleted":"0",
         "adate":"2017-03-16 13:18:12",
         "udate":"2017-02-09T12:14:58-06:00",
         "edate":"0000-00-00 00:00:00",
         "scoreValues":[

         ],
        "accountContacts": [
            "1"
         ],
         "links":{
            "bounceLogs":"https://:account.api-us1.com/api/:version/contacts/73/bounceLogs",
            "contactAutomations":"https://:account.api-us1.com/api/:version/contacts/73/contactAutomations",
            "contactData":"https://:account.api-us1.com/api/:version/contacts/73/contactData",
            "contactGoals":"https://:account.api-us1.com/api/:version/contacts/73/contactGoals",
            "contactLists":"https://:account.api-us1.com/api/:version/contacts/73/contactLists",
            "contactLogs":"https://:account.api-us1.com/api/:version/contacts/73/contactLogs",
            "contactTags":"https://:account.api-us1.com/api/:version/contacts/73/contactTags",
            "contactDeals":"https://:account.api-us1.com/api/:version/contacts/73/contactDeals",
            "deals":"https://:account.api-us1.com/api/:version/contacts/73/deals",
            "fieldValues":"https://:account.api-us1.com/api/:version/contacts/73/fieldValues",
            "geoIps":"https://:account.api-us1.com/api/:version/contacts/73/geoIps",
            "notes":"https://:account.api-us1.com/api/:version/contacts/73/notes",
            "organization":"https://:account.api-us1.com/api/:version/contacts/73/organization",
            "plusAppend":"https://:account.api-us1.com/api/:version/contacts/73/plusAppend",
            "trackingLogs":"https://:account.api-us1.com/api/:version/contacts/73/trackingLogs",
            "scoreValues":"https://:account.api-us1.com/api/:version/contacts/73/scoreValues"
         },
         "id":"73",
         "organization":"14"
      }
   ],
   "meta":{
      "total":"2",
      "page_input":{
         "segmentid":null,
         "formid":0,
         "listid":0,
         "tagid":0,
         "limit":20,
         "offset":0,
         "search":null,
         "sort":null,
         "seriesid":0,
         "waitid":0,
         "status":-1,
         "forceQuery":0,
         "cacheid":"895202850f4ca4144513c0962812f951"
      }
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
    "/contacts": {
      "get": {
        "summary": "List, search, and filter contacts",
        "description": "Use this API endpoint to list all contacts, search contacts, or filter contacts by many criteria. For example, search for specific contacts by email, list, account.",
        "operationId": "list-all-contacts",
        "parameters": [
          {
            "name": "ids",
            "in": "query",
            "description": "Filter contacts by ID. Can be repeated for multiple IDs. Example: ids[]=1&ids[]=2&ids[]=42",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "email",
            "in": "query",
            "description": "Email address of the contact you want to get",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "email_like",
            "in": "query",
            "description": "Filter contacts that contain the given value in the email address",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "exclude",
            "in": "query",
            "description": "Exclude from the response the contact with the given ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "formid",
            "in": "query",
            "description": "Filter contacts associated with the given form",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "id_greater",
            "in": "query",
            "description": "Only include contacts with an ID greater than the given ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "id_less",
            "in": "query",
            "description": "Only include contacts with an ID less than the given ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "listid",
            "in": "query",
            "description": "Filter contacts associated with the given list",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "phone",
            "in": "query",
            "description": "Filter contacts where the phone number starts with the given value",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "organization",
            "in": "query",
            "description": "(Deprecated) Please use Account-Contact end points. Filter contacts associated with the given organization ID",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "search",
            "in": "query",
            "description": "Filter contacts that match the given value in the contact names, organization, phone or email",
            "schema": {
              "type": "string",
              "default": "null"
            }
          },
          {
            "name": "segmentid",
            "in": "query",
            "description": "Return only contacts that match a list segment. The first API call within 1 hour or an API call with the param `forceQuery=1` will kick off an new segment request. When the segment results are ready, subsequent API calls without the `forceQuery` param will return contacts that match the segment - timeout 1hr)",
            "schema": {
              "type": "string",
              "default": null
            }
          },
          {
            "name": "seriesid",
            "in": "query",
            "description": "Filter contacts associated with the given automation",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "status",
            "in": "query",
            "description": "See [available values](https://developers.activecampaign.com/reference/contact)",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": -1
            }
          },
          {
            "name": "tagid",
            "in": "query",
            "description": "Filter contacts associated with the given tag",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "filters[created_before]",
            "in": "query",
            "description": "Filter contacts that were created prior to this date",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "filters[created_after]",
            "in": "query",
            "description": "Filter contacts that were created after this date",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "filters[updated_before]",
            "in": "query",
            "description": "Filter contacts that were updated before this date",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "filters[updated_after]",
            "in": "query",
            "description": "Filter contacts that were updated after this date",
            "schema": {
              "type": "string",
              "format": "date"
            }
          },
          {
            "name": "waitid",
            "in": "query",
            "description": "Filter by contacts in the wait queue of an automation block",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "orders[id]",
            "in": "query",
            "description": "Order contacts by unique ID",
            "schema": {
              "type": "string",
              "default": "ASC",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "orders[cdate]",
            "in": "query",
            "description": "Order contacts by creation date",
            "schema": {
              "type": "string",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "orders[email]",
            "in": "query",
            "description": "Order contacts by email",
            "schema": {
              "type": "string",
              "default": "ASC",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "orders[first_name]",
            "in": "query",
            "description": "Order contacts by first name",
            "schema": {
              "type": "string",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "orders[last_name]",
            "in": "query",
            "description": "Order contacts by last name",
            "schema": {
              "type": "string",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "orders[name]",
            "in": "query",
            "description": "Order contacts by full name",
            "schema": {
              "type": "string",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "orders[score]",
            "in": "query",
            "description": "Order contacts by score. Must be used in conjunction with the `sortId` parameter",
            "schema": {
              "type": "string",
              "enum": [
                "desc",
                "asc"
              ]
            }
          },
          {
            "name": "in_group_lists",
            "in": "query",
            "description": "Set this to \"true\" in order to return only contacts that the current user has permissions to see.",
            "schema": {
              "type": "string"
            }
          },
          {
            "in": "query",
            "name": "forceQuery",
            "schema": {
              "type": "number",
              "default": "0",
              "enum": [
                0,
                1
              ]
            },
            "description": "If present and equal to 1, a new segment request is kicked off which will return an updated result set. Otherwise, a segmented API request with a consistent sorting will return the same results for 1 hour. Note that re-ordering the results will also cause an updated result set to be returned."
          },
          {
            "in": "query",
            "name": "sortId",
            "schema": {
              "type": "number"
            },
            "description": "If sorting results by a score or custom field, this parameter holds the id of the score or custom field respectively"
          }
        ],
        "responses": {
          "200": {
            "description": "200",
            "content": {
              "application/json": {
                "examples": {
                  "Result": {
                    "value": "{\n    \"scoreValues\": [],\n    \"contacts\": [\n        {\n            \"cdate\": \"2018-09-12T16:53:50-05:00\",\n            \"email\": \"adam@activecampaign.com\",\n            \"phone\": \"\",\n            \"firstName\": \"\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": \"0000-00-00\",\n            \"ip\": \"0\",\n            \"ua\": \"\",\n            \"hash\": \"0d9c41ae7a4de516313673e2341f6003\",\n            \"socialdata_lastcheck\": \"0000-00-00 00:00:00\",\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": \"0000-00-00\",\n            \"gravatar\": \"1\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"udate\": \"2018-09-12T17:00:00-05:00\",\n            \"deleted_at\": \"0000-00-00 00:00:00\",\n            \"scoreValues\": [],\n            \"links\": {\n                \"bounceLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/bounceLogs\",\n                \"contactAutomations\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactAutomations\",\n                \"contactData\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactData\",\n                \"contactGoals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactGoals\",\n                \"contactLists\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactLists\",\n                \"contactLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactLogs\",\n                \"contactTags\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactTags\",\n                \"contactDeals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactDeals\",\n                \"deals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/deals\",\n                \"fieldValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/fieldValues\",\n                \"geoIps\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/geoIps\",\n                \"notes\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/notes\",\n                \"organization\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/organization\",\n                \"plusAppend\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/plusAppend\",\n                \"trackingLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/trackingLogs\",\n                \"scoreValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/scoreValues\"\n            },\n            \"id\": \"5\",\n            \"organization\": null\n        },\n        {\n            \"cdate\": \"2018-08-17T13:46:58-05:00\",\n            \"email\": \"kconnell2@gmailc.om\",\n            \"phone\": \"\",\n            \"firstName\": \"\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": \"0000-00-00\",\n            \"ip\": \"2130706433\",\n            \"ua\": \"\",\n            \"hash\": \"4641d20634346d27408557fde5e3ad3b\",\n            \"socialdata_lastcheck\": \"0000-00-00 00:00:00\",\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": \"0000-00-00\",\n            \"gravatar\": \"1\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": \"2018-08-31T11:58:25-05:00\",\n            \"udate\": \"2018-08-17T13:46:58-05:00\",\n            \"deleted_at\": \"0000-00-00 00:00:00\",\n            \"scoreValues\": [],\n            \"links\": {\n                \"bounceLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/bounceLogs\",\n                \"contactAutomations\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactAutomations\",\n                \"contactData\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactData\",\n                \"contactGoals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactGoals\",\n                \"contactLists\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactLists\",\n                \"contactLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactLogs\",\n                \"contactTags\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactTags\",\n                \"contactDeals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/contactDeals\",\n                \"deals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/deals\",\n                \"fieldValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/fieldValues\",\n                \"geoIps\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/geoIps\",\n                \"notes\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/notes\",\n                \"organization\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/organization\",\n                \"plusAppend\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/plusAppend\",\n                \"trackingLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/trackingLogs\",\n                \"scoreValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/4/scoreValues\"\n            },\n            \"id\": \"4\",\n            \"organization\": null\n        },\n        {\n            \"cdate\": \"2018-09-18T11:02:57-05:00\",\n            \"email\": \"test@gmail.com\",\n            \"phone\": \"\",\n            \"firstName\": \"\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": null,\n            \"ip\": \"0\",\n            \"ua\": null,\n            \"hash\": \"\",\n            \"socialdata_lastcheck\": null,\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": null,\n            \"gravatar\": \"1\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": null,\n            \"udate\": \"2018-09-18T11:02:57-05:00\",\n            \"edate\": null,\n            \"deleted_at\": null,\n            \"scoreValues\": [],\n            \"links\": {\n                \"bounceLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/bounceLogs\",\n                \"contactAutomations\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactAutomations\",\n                \"contactData\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactData\",\n                \"contactGoals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactGoals\",\n                \"contactLists\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactLists\",\n                \"contactLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactLogs\",\n                \"contactTags\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactTags\",\n                \"contactDeals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/contactDeals\",\n                \"deals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/deals\",\n                \"fieldValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/fieldValues\",\n                \"geoIps\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/geoIps\",\n                \"notes\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/notes\",\n                \"organization\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/organization\",\n                \"plusAppend\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/plusAppend\",\n                \"trackingLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/trackingLogs\",\n                \"scoreValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/6/scoreValues\"\n            },\n            \"id\": \"6\",\n            \"organization\": null\n        },\n        {\n            \"cdate\": \"2018-08-17T09:56:33-05:00\",\n            \"email\": \"test@test.com\",\n            \"phone\": \"9813764\",\n            \"firstName\": \"Test\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": \"0000-00-00\",\n            \"ip\": \"2130706433\",\n            \"ua\": \"\",\n            \"hash\": \"e4162c50b2edaf68b0d5012ef3cc82fd\",\n            \"socialdata_lastcheck\": \"0000-00-00 00:00:00\",\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": \"0000-00-00\",\n            \"gravatar\": \"1\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": \"2018-08-31T11:52:08-05:00\",\n            \"udate\": \"2018-08-17T09:56:33-05:00\",\n            \"edate\": \"2018-08-17T13:48:46-05:00\",\n            \"deleted_at\": \"0000-00-00 00:00:00\",\n            \"scoreValues\": [],\n            \"links\": {\n                \"bounceLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/bounceLogs\",\n                \"contactAutomations\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactAutomations\",\n                \"contactData\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactData\",\n                \"contactGoals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactGoals\",\n                \"contactLists\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactLists\",\n                \"contactLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactLogs\",\n                \"contactTags\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactTags\",\n                \"contactDeals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/contactDeals\",\n                \"deals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/deals\",\n                \"fieldValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/fieldValues\",\n                \"geoIps\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/geoIps\",\n                \"notes\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/notes\",\n                \"organization\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/organization\",\n                \"plusAppend\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/plusAppend\",\n                \"trackingLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/trackingLogs\",\n                \"scoreValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/2/scoreValues\"\n            },\n            \"id\": \"2\",\n            \"organization\": null\n        },\n        {\n            \"cdate\": \"2018-08-17T13:45:23-05:00\",\n            \"email\": \"test@testing.com\",\n            \"phone\": \"20405938\",\n            \"firstName\": \"testing\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": null,\n            \"ip\": \"2130706433\",\n            \"ua\": null,\n            \"hash\": \"e3eba337bb1ede3bd073b1832e3f3def\",\n            \"socialdata_lastcheck\": null,\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": null,\n            \"gravatar\": \"1\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": null,\n            \"udate\": \"2018-08-17T13:45:23-05:00\",\n            \"edate\": null,\n            \"deleted_at\": null,\n            \"scoreValues\": [],\n            \"links\": {\n                \"bounceLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/bounceLogs\",\n                \"contactAutomations\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactAutomations\",\n                \"contactData\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactData\",\n                \"contactGoals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactGoals\",\n                \"contactLists\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactLists\",\n                \"contactLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactLogs\",\n                \"contactTags\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactTags\",\n                \"contactDeals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/contactDeals\",\n                \"deals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/deals\",\n                \"fieldValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/fieldValues\",\n                \"geoIps\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/geoIps\",\n                \"notes\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/notes\",\n                \"organization\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/organization\",\n                \"plusAppend\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/plusAppend\",\n                \"trackingLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/trackingLogs\",\n                \"scoreValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/3/scoreValues\"\n            },\n            \"id\": \"3\",\n            \"organization\": null\n        },\n        {\n            \"cdate\": \"2018-09-19T23:11:11-05:00\",\n            \"email\": \"tjahn+test@activecampaign.com\",\n            \"phone\": \"\",\n            \"firstName\": \"\",\n            \"lastName\": \"\",\n            \"orgid\": \"0\",\n            \"segmentio_id\": \"\",\n            \"bounced_hard\": \"0\",\n            \"bounced_soft\": \"0\",\n            \"bounced_date\": \"0000-00-00\",\n            \"ip\": \"0\",\n            \"ua\": \"\",\n            \"hash\": \"853be08a2387ac13ca51dee72e586e9c\",\n            \"socialdata_lastcheck\": \"0000-00-00 00:00:00\",\n            \"email_local\": \"\",\n            \"email_domain\": \"\",\n            \"sentcnt\": \"0\",\n            \"rating_tstamp\": \"0000-00-00\",\n            \"gravatar\": \"0\",\n            \"deleted\": \"0\",\n            \"anonymized\": \"0\",\n            \"adate\": \"2018-09-19T23:24:43-05:00\",\n            \"udate\": \"2018-09-19T23:11:11-05:00\",\n            \"deleted_at\": \"0000-00-00 00:00:00\",\n            \"scoreValues\": [],\n            \"links\": {\n                \"bounceLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/bounceLogs\",\n                \"contactAutomations\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactAutomations\",\n                \"contactData\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactData\",\n                \"contactGoals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactGoals\",\n                \"contactLists\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactLists\",\n                \"contactLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactLogs\",\n                \"contactTags\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactTags\",\n                \"contactDeals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/contactDeals\",\n                \"deals\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/deals\",\n                \"fieldValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/fieldValues\",\n                \"geoIps\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/geoIps\",\n                \"notes\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/notes\",\n                \"organization\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/organization\",\n                \"plusAppend\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/plusAppend\",\n                \"trackingLogs\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/trackingLogs\",\n                \"scoreValues\": \"https://test-enterprise-13.staging.listfly.com/api/3/contacts/7/scoreValues\"\n            },\n            \"id\": \"7\",\n            \"organization\": null\n        }\n    ],\n    \"meta\": {\n        \"total\": \"6\",\n        \"page_input\": {\n            \"segmentid\": 0,\n            \"formid\": 0,\n            \"listid\": 0,\n            \"tagid\": 0,\n            \"limit\": 20,\n            \"offset\": 0,\n            \"search\": null,\n            \"sort\": null,\n            \"seriesid\": 0,\n            \"waitid\": 0,\n            \"status\": -1,\n            \"forceQuery\": 0,\n            \"cacheid\": \"522b5224f2007dca7483e08e7ebf5005\"\n        }\n    }\n}"
                  }
                },
                "schema": {
                  "oneOf": [
                    {
                      "type": "object",
                      "properties": {
                        "contacts": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "cdate": {
                                "type": "string",
                                "example": "2017-01-25T23:58:14-06:00"
                              },
                              "email": {
                                "type": "string",
                                "example": "janedoe@example.com"
                              },
                              "phone": {
                                "type": "string",
                                "example": "3120000000"
                              },
                              "firstName": {
                                "type": "string",
                                "example": "John"
                              },
                              "lastName": {
                                "type": "string",
                                "example": "Doe"
                              },
                              "orgid": {
                                "type": "string",
                                "example": "0"
                              },
                              "segmentio_id": {
                                "type": "string",
                                "example": ""
                              },
                              "bounced_hard": {
                                "type": "string",
                                "example": "0"
                              },
                              "bounced_soft": {
                                "type": "string",
                                "example": "0"
                              },
                              "bounced_date": {
                                "type": "string",
                                "example": "0000-00-00"
                              },
                              "ip": {
                                "type": "string",
                                "example": "0"
                              },
                              "ua": {
                                "type": "string",
                                "example": ""
                              },
                              "hash": {
                                "type": "string",
                                "example": "31e076c964f4262817f9ba302c96e1c6"
                              },
                              "socialdata_lastcheck": {
                                "type": "string",
                                "example": "0000-00-00 00:00:00"
                              },
                              "email_local": {
                                "type": "string",
                                "example": ""
                              },
                              "email_domain": {
                                "type": "string",
                                "example": ""
                              },
                              "sentcnt": {
                                "type": "string",
                                "example": "0"
                              },
                              "rating_tstamp": {
                                "type": "string",
                                "example": "0000-00-00"
                              },
                              "gravatar": {
                                "type": "string",
                                "example": "3"
                              },
                              "deleted": {
                                "type": "string",
                                "example": "0"
                              },
                              "adate": {
                                "type": "string",
                                "example": "2017-02-22 15:26:24"
                              },
                              "udate": {
                                "type": "string",
                                "example": "2017-01-25T23:58:14-06:00"
                              },
                              "edate": {
                                "type": "string",
                                "example": "2017-01-27 14:44:13"
                              },
                              "scoreValues": {
                                "type": "array"
                              },
                              "links": {
                                "type": "object",
                                "properties": {
                                  "bounceLogs": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/bounceLogs"
                                  },
                                  "contactAutomations": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactAutomations"
                                  },
                                  "contactData": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactData"
                                  },
                                  "contactGoals": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactGoals"
                                  },
                                  "contactLists": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactLists"
                                  },
                                  "contactLogs": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactLogs"
                                  },
                                  "contactTags": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactTags"
                                  },
                                  "contactDeals": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/contactDeals"
                                  },
                                  "deals": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/deals"
                                  },
                                  "fieldValues": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/fieldValues"
                                  },
                                  "geoIps": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/geoIps"
                                  },
                                  "notes": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/notes"
                                  },
                                  "organization": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/organization"
                                  },
                                  "plusAppend": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/plusAppend"
                                  },
                                  "trackingLogs": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/trackingLogs"
                                  },
                                  "scoreValues": {
                                    "type": "string",
                                    "example": "https://:account.api-us1.com/api/:version/contacts/68/scoreValues"
                                  }
                                }
                              },
                              "id": {
                                "type": "string",
                                "example": "68"
                              },
                              "organization": {}
                            }
                          }
                        },
                        "meta": {
                          "type": "object",
                          "properties": {
                            "total": {
                              "type": "string",
                              "example": "2"
                            },
                            "page_input": {
                              "type": "object",
                              "properties": {
                                "segmentid": {},
                                "formid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "listid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "tagid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "limit": {
                                  "type": "integer",
                                  "example": 20,
                                  "default": 0
                                },
                                "offset": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "search": {},
                                "sort": {},
                                "seriesid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "waitid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "status": {
                                  "type": "integer",
                                  "example": -1,
                                  "default": 0
                                },
                                "forceQuery": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "cacheid": {
                                  "type": "string",
                                  "example": "895202850f4ca4144513c0962812f951"
                                }
                              }
                            }
                          }
                        }
                      }
                    },
                    {
                      "type": "object",
                      "properties": {
                        "scoreValues": {
                          "type": "array"
                        },
                        "contacts": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "cdate": {
                                "type": "string",
                                "example": "2018-09-12T16:53:50-05:00"
                              },
                              "email": {
                                "type": "string",
                                "example": "adam@activecampaign.com"
                              },
                              "phone": {
                                "type": "string",
                                "example": ""
                              },
                              "firstName": {
                                "type": "string",
                                "example": ""
                              },
                              "lastName": {
                                "type": "string",
                                "example": ""
                              },
                              "orgid": {
                                "type": "string",
                                "example": "0"
                              },
                              "segmentio_id": {
                                "type": "string",
                                "example": ""
                              },
                              "bounced_hard": {
                                "type": "string",
                                "example": "0"
                              },
                              "bounced_soft": {
                                "type": "string",
                                "example": "0"
                              },
                              "bounced_date": {
                                "type": "string",
                                "example": "0000-00-00"
                              },
                              "ip": {
                                "type": "string",
                                "example": "0"
                              },
                              "ua": {
                                "type": "string",
                                "example": ""
                              },
                              "hash": {
                                "type": "string",
                                "example": "0d9c41ae7a4de516313673e2341f6003"
                              },
                              "socialdata_lastcheck": {
                                "type": "string",
                                "example": "0000-00-00 00:00:00"
                              },
                              "email_local": {
                                "type": "string",
                                "example": ""
                              },
                              "email_domain": {
                                "type": "string",
                                "example": ""
                              },
                              "sentcnt": {
                                "type": "string",
                                "example": "0"
                              },
                              "rating_tstamp": {
                                "type": "string",
                                "example": "0000-00-00"
                              },
                              "gravatar": {
                                "type": "string",
                                "example": "1"
                              },
                              "deleted": {
                                "type": "string",
                                "example": "0"
                              },
                              "anonymized": {
                                "type": "string",
                                "example": "0"
                              },
                              "udate": {
                                "type": "string",
                                "example": "2018-09-12T17:00:00-05:00"
                              },
                              "deleted_at": {
                                "type": "string",
                                "example": "0000-00-00 00:00:00"
                              },
                              "scoreValues": {
                                "type": "array"
                              },
                              "links": {
                                "type": "object",
                                "properties": {
                                  "bounceLogs": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/bounceLogs"
                                  },
                                  "contactAutomations": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactAutomations"
                                  },
                                  "contactData": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactData"
                                  },
                                  "contactGoals": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactGoals"
                                  },
                                  "contactLists": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactLists"
                                  },
                                  "contactLogs": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactLogs"
                                  },
                                  "contactTags": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactTags"
                                  },
                                  "contactDeals": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/contactDeals"
                                  },
                                  "deals": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/deals"
                                  },
                                  "fieldValues": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/fieldValues"
                                  },
                                  "geoIps": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/geoIps"
                                  },
                                  "notes": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/notes"
                                  },
                                  "organization": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/organization"
                                  },
                                  "plusAppend": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/plusAppend"
                                  },
                                  "trackingLogs": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/trackingLogs"
                                  },
                                  "scoreValues": {
                                    "type": "string",
                                    "example": "https://test-enterprise-13.staging.listfly.com/api/3/contacts/5/scoreValues"
                                  }
                                }
                              },
                              "id": {
                                "type": "string",
                                "example": "5"
                              },
                              "organization": {}
                            }
                          }
                        },
                        "meta": {
                          "type": "object",
                          "properties": {
                            "total": {
                              "type": "string",
                              "example": "6"
                            },
                            "page_input": {
                              "type": "object",
                              "properties": {
                                "segmentid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "formid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "listid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "tagid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "limit": {
                                  "type": "integer",
                                  "example": 20,
                                  "default": 0
                                },
                                "offset": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "search": {},
                                "sort": {},
                                "seriesid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "waitid": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "status": {
                                  "type": "integer",
                                  "example": -1,
                                  "default": 0
                                },
                                "forceQuery": {
                                  "type": "integer",
                                  "example": 0,
                                  "default": 0
                                },
                                "cacheid": {
                                  "type": "string",
                                  "example": "522b5224f2007dca7483e08e7ebf5005"
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  ]
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