# Source: https://documentation.mailgun.com/docs/inboxready/inbox-placement-ir.md

# Inbox Placement

A seed list is an object that provides the mailing list for your inbox placement test. It also acts as a container for all the results of those tests and will aggregate the stats of all the tests.

When you create a seed list you will be provided a mailing list. You may adjust this mailing list as you see fit, but you must send to the `target_email` otherwise a placement test will not be run.

## Generate a seed list


```
POST /v4/inbox/seedlists
```

The available form fields to generate a seed list are as follows:

| Field | Description |
|  --- | --- |
| name | The name that you would like to use for this seed list. |
| seed_filter | A regular expression that will be applied to addresses in the mailing list. |



```JSON
curl -X POST https://api.mailgun.net/v4/inbox/seedlists \
  -F 'name=list' \
  --user 'api:<YOUR_API_KEY>'
```

Example response for creating a seed list.


```JSON
{
  "kid": "610abd2009b08f382ac86c45",
  "created_at": "2021-08-04T16:15:28.08Z",
  "updated_at": "2021-08-04T16:15:28.08Z",
  "last_result_at": "0001-01-01T00:00:00Z",
  "target_email": "ibp-12345678-1234-1234-1234-123456789012@domain.com",
  "sending_domains": [],
  "has_results": false,
  "name": "My campaign inbox test",
  "seed_filter": ".*",
  "mailing_list": "ibp-12345678-1234-1234-1234-123456789012@domain.com,another@email.com",
  "delivery_stats": {
    "all": {
      "delivered": 0,
      "missing": 0,
      "pending": 0,
      "spam": 0,
      "inbox": 0,
      "total": 0,
      "provider": "all"
    }
  },
  "results": []
}
```

Field Explanation:

| Name | Type | Description |
|  --- | --- | --- |
| kid | string | Unique identifier for a seed list. |
| created_at | datetime | Date and time that seed list was created. |
| updated_at | datetime | Date and time that seed list was updated. Will update whenever it is changed. |
| last_result_at | datetime | Date and time that seed list was updated. Will update whenever a new result comes in. |
| target_email | string | The required email address that must be included in a mailing list for an inbox placement test to work. |
| sending_domains | array | The list of possible domains that the messages must come from. |
| has_results | bool | A flag that is true when results exist for this seed list |
| name | string | The name of the seed list |
| seed_filter | string | A regular expression value that will be used to filter the list of seeds in the seed list. |
| mailing_list | string | A mailing list that contains the target email, and available seeds. |
| delivery_stats | object | An object that contains sub-objects that describe delivery stats. See below. |
| results | array | An array of results from the seed list's tests. |


# Delivery Stats

Delivery stats is an object that is included with seed list and results from the API. It is an attribute of the main object that is returned. A sample object:


```JSON
"delivery_stats": {
  "all": {
    "delivered": 10,
    "missing": 1,
    "pending": 0,
    "spam": 3,
    "inbox": 6,
    "total": 10,
    "provider": "all"
  },
  "yahoo.com": {
    "delivered": 4,
    "missing": 1,
    "pending": 0,
    "spam": 0,
    "inbox": 4,
    "total": 5,
    "provider": "yahoo.com"
  },
  "gmail.com": {
    "delivered": 5,
    "missing": 0,
    "pending": 0,
    "spam": 3,
    "inbox": 2,
    "total": 5,
    "provider": "gmail.com"
  }
}
```

Field Explanation:

| Name | Type | Description |
|  --- | --- | --- |
| sub-object -"subkey" | object | The sub-object of the main delivery_stats object is divided by provider. There will always be an "all" provider that is the total sum. |
| delivered | number | The amount of messages that were received by the system. |
| missing | number | The amount of messages that were not received by the required reporting time period. |
| pending | number | The amount of messages that have yet to be received within the required reporting time period. |
| spam | number | The amount of messages that were detected in the provider's spam folder. |
| inbox | number | The amount of messages that were detected in a non-spam folder. |
| total | number | The amount of messages that are expected. |
| provider | string | The provider that these mailboxes are a part of (identical to key). |


## Results

A result is an object summarizing Inbox Placement tests sent to the target_email.


```JSON
{
  "result_id": "12345678-1234-1234-1234-123456789012",
  "subject": "IBP Test - 1",
  "sender": "generated@yourdomain.com",
  "delivery_stats": {
    "all": {
      "delivered": 7,
      "missing": 0,
      "pending": 0,
      "spam": 2,
      "inbox": 5,
      "total": 7,
      "provider": "all",
      "categories": {}
    }
  }
}
```

Field Explanation:

| Name | Type | Description |
|  --- | --- | --- |
| result_id | string | Unique identifier for a received test. |
| subject | string | The subject of the email sent to the target_email. |
| sender | string | Sender address of the email sent to the target_email. |
| delivery_stats | object | An object that contains sub-objects that describe delivery stats. See above. |


## Get all seed lists


```
GET /v4/inbox/seedlists
```

Get a list of all of your seed lists. You can filter this using the available filters. These can be listed from the "Get all available filters for seed lists" endpoint described below.


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/seedlists
```

Example response for listing seed lists.


```JSON
{
  "items": [
    {
      "kid": "123456789123456789123456",
      "created_at": "2021-08-02T23:10:17.915Z",
      "updated_at": "2021-08-03T17:26:55.629Z",
      "last_result_at": "2021-08-03T17:26:55.629Z",
      "target_email": "ibp-12345678-1234-1234-1234-123456789012@domain.com",
      "sending_domains": [
        "mydomain.com"
      ],
      "has_results": true,
      "name": "Inbox Placement Test",
      "seed_filter": ".*",
      "mailing_list": "ibp-12345678-1234-1234-1234-123456789012@domain.com,some@where.com",
      "delivery_stats": {
        "all": {
          "delivered": 7,
          "missing": 0,
          "pending": 0,
          "spam": 2,
          "inbox": 5,
          "total": 7,
          "provider": "all"
        }
      },
      "results": [
        {
          "result_id": "12345678-1234-1234-1234-123456789012",
          "subject": "IBP Test - 1",
          "sender": "generated@yourdomain.com",
          "delivery_stats": {
            "all": {
              "delivered": 7,
              "missing": 0,
              "pending": 0,
              "spam": 2,
              "inbox": 5,
              "total": 7,
              "provider": "all",
              "categories": {}
            }
          }
        }
      ]
    }
  ],
  "paging": {
    "first": "http://domain.com/v4/inbox/seedlists?ascending=0&limit=1",
    "last": "http://domain.com/v4/inbox/seedlists?ascending=1&limit=1",
    "next": "http://domain.com/v4/inbox/seedlists?ascending=0&cursor=123987123981723987873497&limit=1",
    "previous": "http://domain.com/v4/inbox/seedlists?ascending=1&cursor=123987123981723987873487&limit=1"
  },
  "total": 32
}
```

Field Explanation:

| Name | Type | Description |
|  --- | --- | --- |
| items | array | A list of seed list objects (same fields as above). |
| paging | object | A paging sub-object to navigate through sections of data. |
| total | number | The total amount of seed lists. |


## **Paging sub-object**

The paging sub-object assists with navigating paginated responses. For a variety of reasons the number of items that can be returned in a response has been limited. This object contains the following fields:

| Name | Type | Description |
|  --- | --- | --- |
| first | url | A url address to the first item of this set |
| last | url | A url address to the last item of this set |
| next | url | A url address to the next item of this set |
| previous | url | A url address to the previous item of this set |


Additionally you can interact with the pagination through a few fields added to the query-string of your request:

| Name | Type | Description |
|  --- | --- | --- |
| limit | number | A limit on the number of items that can be returned (defaults to 25) |
| offset | number | A the amount of items to "move" by |
| ascending | bool | A flag that will set the order of the pagination |
| cursor | string | A unique id that can be used as a "pivot" of where you are in the set |
| sort | string | The parameter to sort by (EXPERIMENTAL) |


Note: cursor and offset may not both be used at the same time

## Get a seed list

You can select a single seed list with this endpoint.


```
GET /v4/inbox/seedlists/ibp-seedlist-address@domain.net
```

Example response of getting a single seed list.


```JSON
{
  "kid": "610abd2009b08f382ac86c45",
  "created_at": "2021-08-04T16:15:28.08Z",
  "updated_at": "2021-08-04T16:15:28.08Z",
  "last_result_at": "0001-01-01T00:00:00Z",
  "target_email": "ibp-seedlist-address@domain.net",
  "sending_domains": [
    "yourdomain.com"
  ],
  "has_results": false,
  "name": "My campaign inbox test",
  "seed_filter": ".*",
  "mailing_list": "ibp-seedlist-address@domain.net,another@email.com",
  "delivery_stats": {
    "all": {
      "delivered": 0,
      "missing": 0,
      "pending": 0,
      "spam": 0,
      "inbox": 0,
      "total": 0,
      "provider": "all"
    }
  },
  "results": [
    {
      "result_id": "12345678-1234-1234-1234-123456789012",
      "subject": "IBP Test - 1",
      "sender": "generated@yourdomain.com",
      "delivery_stats": {
        "all": {
          "delivered": 7,
          "missing": 0,
          "pending": 0,
          "spam": 2,
          "inbox": 5,
          "total": 7,
          "provider": "all",
          "categories": {}
        }
      }
    }
  ]
}
```

| Name | Type | Description |
|  --- | --- | --- |
| kid | string | Unique identifier for a seed list. |
| created_at | datetime | Date and time that seed list was created. |
| updated_at | datetime | Date and time that seed list was updated. Will update whenever it is changed. |
| last_result_at | datetime | Date and time that seed list was updated. Will update whenever a new result comes in. |
| target_email | string | The required email address that must be included in a mailing list for an inbox placement test to work. |
| sending_domains | array | The list of possible domains that the messages must come from. |
| has_results | bool | A flag that is true when results exist for this seed list |
| name | string | The name of the seed list |
| seed_filter | string | A regular expression value that will be used to filter the list of seeds in the seed list. |
| mailing_list | string | A mailing list that contains the target email, and available seeds. |
| delivery_stats | object | An object that contains sub-objects that describe delivery stats. See below. |
| results | array | An array of results from the seed list's tests. |


## Get all iterable attributes of seed lists

You can use this endpoint to find all attributes that are available for listing values of.


```
GET /v4/inbox/seedlists/a
```

| Name | Type | Description |
|  --- | --- | --- |
| attribute | string | A string describing what was selected. |
| values | array | A list of attributes that can be retrieved from the API. |


## Get all values of a specific attribute of your seed lists

You can use this endpoint to find all the values for a particular attribute. This can be used to produce autocomplete or suggestions from a frontend.


```
GET /v4/inbox/seedlists/a/attribute
```


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/inbox/seedlists/a/ATTRIBUTE
```

Example response of seed list attribute values.


```JSON
{
 "items": {
   "attribute": "name",
   "values": [
     "Inbox Placement Test",
     "My email campaign"
   ]
 }
}
```

| Name | Type | Description |
|  --- | --- | --- |
| attribute | string | A string describing what was selected. |
| values | array | A list of attributes that can be retrieved from the API. |


## Get all available filters for seed lists

You can use this endpoint to list the available filters for seed lists.


```
GET /v4/inbox/seedlists/\_filters
```


```JSON
{
 "items": {
   "attribute": "name",
   "values": [
     "Inbox Placement Test",
     "My email campaign"
   ]
 }
}
```

Example response of seed list filters.


```JSON
{
 "supported_filters": {
   "filters": [
     {
       "parameter": "name",
       "description": "Get seedlists by name"
     },
     {
       "parameter": "time_before",
       "description": "Get seedlists before date"
     },
     {
       "parameter": "time_after",
       "description": "Get seedlists after date"
     }
   ]
 }
}
```

| Name | Type | Description |
|  --- | --- | --- |
| parameter | string | The key of the parameter you can pass in your query string. |
| description | string | A description of the filter |


## Delete a seed list

You can delete a seed list with this endpoint. The results under it will not be kept.


```
DELETE /v4/inbox/seedlists/ibp-seedlist-address@domain.net
```


```JSON
curl -s --user 'api:YOUR_API_KEY' -X DELETE -G \
    https://api.mailgun.net/v4/inbox/seedlists/TARGET_EMAIL
```

This does not return any value.

## Update a seed list

You can update a seed list with this endpoint. Modifying the sending domains or the seed filter will not affect historical results.


```
PUT /v4/inbox/seedlists/ibp-seedlist-address@domain.net
```

Update a seed list. The available form fields are as follows:

| Field | Description |
|  --- | --- |
| sending_domains | Update the sending domains of the seed list. You can specify this multiple times. |
| name | Update the name of the seed list. |
| seed_filter | Update the regular expression that will be applied to addresses in the mailing list. |



```JSON
curl -X PUT https://api.mailgun.net/v4/inbox/seedlists/TARGET_EMAIL \
  -F 'sending_domains=domain.com' \
  --user 'api:<YOUR_API_KEY>'
```

Example Response


```JSON
{
"kid": "610abd2009b08f382ac86c45",
"created_at": "2021-08-04T16:15:28.08Z",
"updated_at": "2021-08-04T16:15:28.08Z",
"last_result_at": "0001-01-01T00:00:00Z",
"target_email": "ibp-seedlist-address@domain.net",
"sending_domains": [
  "yourdomain.com"
],
"has_results": false,
"name": "My campaign inbox test",
"seed_filter": ".*",
"mailing_list": "ibp-seedlist-address@domain.net,another@email.com",
"delivery_stats": {
  "all": {
    "delivered": 0,
    "missing": 0,
    "pending": 0,
    "spam": 0,
    "inbox": 0,
    "total": 0,
    "provider": "all"
  }
},
"results": []
}
```

| Name | Type | Description |
|  --- | --- | --- |
| kid | string | Unique identifier for a seed list. |
| created_at | datetime | Date and time that seed list was created. |
| updated_at | datetime | Date and time that seed list was updated. Will update whenever it is changed. |
| last_result_at | datetime | Date and time that seed list was updated. Will update whenever a new result comes in. |
| target_email | string | The required email address that must be included in a mailing list for an inbox placement test to work. |
| sending_domains | array | The list of possible domains that the messages must come from. |
| has_results | bool | A flag that is true when results exist for this seed list |
| name | string | The name of the seed list |
| seed_filter | string | A regular expression value that will be used to filter the list of seeds in the seed list. |
| mailing_list | string | A mailing list that contains the target email, and available seeds. |
| delivery_stats | object | An object that contains sub-objects that describe delivery stats. See below. |
| results | array | An array of results from the seed list's tests. |


## List Results

Test results are generated when a message has been received at the `target_email`. If a message is not received at the target email no seed test will be run. Results will contain the status of the monitored mail boxes and will provide stats of the test.


```
GET /v4/inbox/results
```

List all results for your account.

| Field | Description |
|  --- | --- |
| sender | Filter results by sender address |
| provider | Filter which results show up in seed_results by provider |
| subject | Filter results by a subject |
| target_email | Filter results by a target_email address |



```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/inbox/results
```

Example Response


```JSON
{
 "items": [
   {
     "rid": "123456789012345678901234",
     "result_id": "12345678-1234-1234-1234-123456789012",
     "keybox_email": "ibp-00410325-1c95-492e-bc35-c19899802494@mailgun.net",
     "subject": "A subject of things",
     "sender": "person@domain.com",
     "name": "Such list",
     "created_at": "2021-08-03T14:20:40.301Z",
     "updated_at": "2021-08-03T14:36:53.841Z",
     "seed_results": [
       {
         "email": "mail@box.com",
         "provider": "box.com",
         "destination": "inbox",
         "state": "delivered",
         "originating_ip": "123.123.123.123",
         "tags": [
           "inbox"
         ],
         "spf": "pass",
         "dkim": "pass",
         "dmarc": "pass"
       }
     ]
   }
 ]
}
```

| Name | Type | Description |
|  --- | --- | --- |
| rid | string | Unique identifier for a results. |
| keybox_email | string | The target email of the seed list associated with this result. |
| subject | string | The subject of the email received by the seed list mailbox (target_email) |
| sender | string | The email address of the sender received by the seed list mailbox (target_email). All other results must come from the same sender. |
| name | string | The name of the seed list. |
| created_at | datetime | Date and time that the results were created. |
| updated_at | datetime | Date and time that the results were updated. Will update whenever a mailbox within the test receives mail. |
| seed_results | object | A sub-object that contains the status of each individual seed mailbox. |
| status | string | Will show "processing" or "complete". |
| delivery_stats | object | A sub-object that provides the stats of this result. |


## Seed Results

The seed results sub-object will provide the details of the individual seed mail boxes.

Field Explanation:

| Name | Type | Description |
|  --- | --- | --- |
| email | string | The email address of the mailbox. |
| provider | string | The email provider of the mailbox (usually the domain). |
| destination | string | Either "inbox" or "spam" |
| state | string | Whether or not the mailbox has received a message |
| originating_ip | string | The IP address from which the message came from (if available) |
| tags | array | The folder, or labels of where the message ended up. |
| spf | string | SPF email authentication results (if available). Possible values are "pass", "fail", and "missing/not-set". |
| dkim | string | Results from DKIM evaluation (if available). Possible values are "pass", "fail", and "missing/not-set". |
| dmarc | string | DMARC email authentication results (if available). Possible values are "pass", "fail", and "missing/not-set". |


## 

Get Available Result Filters


```
GET /v4/inbox/results/\_filters
```


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/results/_filters
```

Example response of getting the available results filters.


```JSON
{
  "supported_filters": {
    "filters": [
      {
        "parameter": "senderaddr",
        "description": "Sender address"
      },
      {
        "parameter": "subject",
        "description": "Subject line"
      },
      {
        "parameter": "provider",
        "description": "E-mail provider"
      },
      {
        "parameter": "target_email",
        "description": "Seedlist target e-mail"
      },
      {
        "parameter": "time_before",
        "description": "Get results before date"
      },
      {
        "parameter": "time_after",
        "description": "Get results after date"
      }
    ]
  }
}
```

## Get all iterable attributes of results


```
GET /v4/inbox/results/a
```

Example response of getting the result attributes.


```JSON
{
  "items": {
    "attribute": "available attributes",
    "values": [
      "subject",
      "sender"
    ]
  }
}
```

## Get all values of a specific attribute of your results lists


```
GET /v4/inbox/results/a/attribute
```


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/inbox/results/a/ATTRIBUTE
```

You can use this endpoint to find all the values for a particular attribute. This can be used to produce autocomplete or suggestions from a frontend.

Example response of response attribute values.


```JSON
{
  "items": {
    "attribute": "subject",
    "values": [
      "This is a subject",
      "We've been trying to contact you",
      "about your car's extended warranty"
    ]
  }
}
```

## Get a specific result


```
GET /v4/inbox/results/UUID
```


```JSON
curl -s --user 'api:YOUR_API_KEY' -G \
    https://api.mailgun.net/v4/inbox/results/UUID
```

You can use this endpoint to get a single result.

| Name | Type | Description |
|  --- | --- | --- |
| rid | string | Unique identifier for a results. |
| keybox_email | string | The target email of the seed list associated with this result. |
| subject | string | The subject of the email received by the seed list mailbox (`target_email`) |
| sender | string | The email address of the sender received by the seed list mailbox (`target_email`). All other results must come from the same sender. |
| name | string | The name of the seed list. |
| created_at | datetime | Date and time that the results were created. |
| updated_at | datetime | Date and time that the results were updated. Will update whenever a mailbox within the test receives mail. |
| seed_results | object | A sub-object that contains the status of each individual seed mailbox. |
| status | string | Will show "processing" or "complete". |
| delivery_stats | object | A sub-object that provides the stats of this result. |


Example response


```JSON
{
 "result": {
   "rid": "123456789012345678901234",
   "result_id": "12345678-1234-1234-1234-123456789012",
   "keybox_email": "ibp-00410325-1c95-492e-bc35-c19899802494@mailgun.net",
   "subject": "A subject of things",
   "sender": "person@domain.com",
   "name": "Such list",
   "created_at": "2021-08-03T14:20:40.301Z",
   "updated_at": "2021-08-03T14:36:53.841Z",
   "seed_results": [
     {
       "email": "mail@box.com",
       "provider": "box.com",
       "destination": "inbox",
       "state": "delivered",
       "originating_ip": "123.123.123.123",
       "tags": [
         "inbox"
       ],
       "spf": "pass",
       "dkim": "pass",
       "dmarc": "pass"
     }
   ]
 }
}
```

## Delete results

Use this endpoint to delete a result.


```
DELETE /v4/inbox/results/UUID
```


```JSON
curl -s --user 'api:YOUR_API_KEY' -X DELETE -G \
    https://api.mailgun.net/v4/inbox/results/UUID
```

This does not return any value.

## Create a test

Use this endpoint to create an Inbox Placement test.


```
POST /v4/inbox/tests
```

Field Explanation:

| Name | Type | Description |
|  --- | --- | --- |
| from | string | Required. The email address from which the email should be sent. Note, the provided domain must be verified within your Mailgun account. |
| subject | string | Required. The subject of the email. |
| html | string | Required. The body of the email represented in HTML. |
| provider_filter | list | Optional. A list of provider domains. This field can be used to test inbox placement against a subset of provider(s). See the List Providers section for available providers. |
| seed_list | string | Optional. The identifier for the seedlist you wish to use. |



```JSON
curl -X POST https://api.mailgun.net/v4/inbox/tests \
  --data-raw '{
    "from": "user@domain.com",
    "subject": "testSubject",
    "html": "<html>HTML version of the body</html>"
  }
  ' \
  --user 'api:<YOUR_API_KEY'>'
```

Below is an example of the returned response body.


```JSON
{
   "result_id": "1a066d4a-2207-4240-9e89-9e1a55511f0e",
   "links": {
     "results": "https://api.mailgun.net/v4/inbox/results/1a066d4a-2207-4240-9e89-9e1a55511f0e"
   }
}
```

## List Providers

Use this endpoint to retrieve a list of providers available for Inbox Placement testing.


```
GET /v4/inbox/providers
```

Below is an example of the returned response body.


```JSON
{
  "items": [
    {
      "domain": "hotmail.com",
      "display_name": "Hotmail",
      "region": "Global",
    },
    {
      "domain": "gmail.com",
      "display_name": "Gmail",
      "region": "Global",
    },
    ...
  ]
}
```