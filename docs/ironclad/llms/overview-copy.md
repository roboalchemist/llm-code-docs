# Source: https://clickwrap-developer.ironcladapp.com/reference/overview-copy.md

# Overview

Sites are individual entities underneath an Account. Groups, Contracts, and Versions are all contained within the Site context.

## Sites Overview

Sites have a number of properties, including some information that can be inherited from the Account (like address and company name for example). Here's an example of an array of objects returned when hitting `GET => /v1.1/sites`:

```json
{
  "page": 1,
  "per_page": 25,
  "count": 3,
  "data": [
    {
      "access_id": "1d2fd973-990a-4759-9583-9469d7b31326",
      "email_reply_address": "team@pactsafe.com",
      "name": "Site 1",
      "url": "http://www.site1.com",
      "created_by": 1,
      "updated_by": 1,
      "email_display_name": "Site 1",
      "account": 1,
      "time_zone": "EDT",
      "locale": "en-US",
      "sandbox": false,
      "primary": true,
      "verified_time": "foo",
      "verified": false,
      "updated_time": "2015-06-12T21:28:40.020Z",
      "created_time": "2015-06-12T21:28:40.010Z",
      "id": 1
    }
  ]
}
```