# Source: https://docs.debricked.com/product/administration/settings/see-logged-events.md

# View logged events

{% hint style="info" %}
*Keep in mind that only users with admin rights have access to the event logs.*
{% endhint %}

To ensure transparency, OpenText Core SCA logs almost all events across the service.\
This enables you to track everything that happens in your company account and manage various aspects of security, performance, and transparency.

The logs can be accessed through OpenText Core SCA API, using the endpoints:

```
/api/{version}/open/admin/request-logs/get-request-logs/api/{version}/open/admin/request-logs/get-events
```

To get a list of event logs, simply call the *get-request-logs* endpoint with appropriate filters. Here is an example of a simple request, fetching all events:

```
curl -X 'GET' \'https://debricked.com/api/1.0/open/admin/request-logs/get-request-logs?start=2021-05-10T15%3A52%3A01&page=1&pageSize=20' \  -H 'accept: application/json' \  -H 'Authorization: Bearer <token>
```

In this case, a start date is specified, while the end date is not, which results in data on events from the start date, up to the current date and time. Since the endpoint is paginated, it is required to specify the pages and the page size.

Here is an example of a response:&#x20;

```
{  "page": 1,  "found": 2,  "requestLogs": [    {      "user": "tony.montana@debricked.com",      "event_name": "Created pull request",      "event_id": 2,      "url": "https://debricked.com/vulnerability/1/repository/2/commit/3/pull-request/generate",      "breadcrumbs": [],      "ip_address": "256.139.13.37",      "timestamp": "2021-11-06 19:45:14",      "method": "GET",      "status_code": 200    },    {      "user": "walter.white@debricked.com",      "eventName": "Visited repository page",      "eventId": 44,      "url": "/app/en/repository/24",      "breadcrumbs": [          {              "url": "../repositories",              "text": "Repositories"          },          {              "url": "",              "text": "owner/dependencies-relations-mess"          }      ],      "ipAddress": "256.139.13.38",      "timestamp": "2021-11-30T12:53:05",      "method": "GET",      "status_code": 200    }  ]}
```

The *breadcrumbs* list all the pages the user visited while using the tool. Note that the breadcrumbs are printed in reverse chronological order, that is, the latest event first and the oldest event last. The URLs in the *breadcrumbs* are relative to the event URL.

### **Filters**

You can customize the logs by selecting additional filters, such as:

* *userEmail -* Filter events performed only by a specific user.
* *url* - Filter events only affecting a given URL. For example, <https://debricked.com/app/en/vulnerability/6552>
* *eventTypeId -* Filter a specific event type.

To filter the logs based on events and get a list of all event names and IDs, you can query the *get-events* endpoint:

```
curl -X 'GET' \  'https://debricked.com/api/1.0/open/admin/request-logs/get-events'   -H 'accept: application/json' \  -H 'Authorization: Bearer <token>
```

Here is an excerpt of the response from the example:

```
[  {    "eventId": 17,    "eventName": "Added comment"  },  {    "eventId": 7,    "eventName": "Added token"  },  {    "eventId": 16,    "eventName": "Changed review status"  },  {    "eventId": 14,    "eventName": "Changed the use case"  },  {    "eventId": 26,    "eventName": "Changed user settings"  }]
```
