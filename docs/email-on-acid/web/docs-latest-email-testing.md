# Source: https://api.emailonacid.com/docs/latest/email-testing

Title: Email on Acid - API Version 5.0 Documentation

URL Source: https://api.emailonacid.com/docs/latest/email-testing

Markdown Content:
Create Email Test
-----------------

This call creates a new email test and submits it to our system for processing.

All requests must contain a “subject” property and one source property (either “html” or “url”). Customers on a user-based reseller package must provide the “customer_id” as well. All other properties are optional. In the following table, each property and its default value is shown.

The response will include an “id” property that should be used to request the results or run processes on the email content.

If the seed list method of spam testing was used, the response will also include a spam property with the spam key which contains an object with an “address_list” property that contains the list of email addresses to send a copy of the email for spam testing purposes.

Enterprise customers’ responses will also include the customer_id and reference_id that were submitted with the test.

URL:
----

```
POST https://api.emailonacid.com/v5/email/tests
```

Example Request Body:
---------------------

```
{
  "subject": "My Email Subject",
  "html": "",
  "transfer_encoding": "8bit",
  "charset": "utf-8",
  "reference_id": "123ABC",
  "customer_id": "1",
  "clients": [
    "outlook16",
    "gmail_chr26_win",
    "iphone6p_9"
  ],
  "image_blocking": true,
  "spam": {
    "test_method": "seed",
    "from_address": "my.test@example.com"
  }
}
```

Example Response:
-----------------

```
{
  "id": "<UNIQUE ID>",
  "reference_id": "123ABC",
  "customer_id": "1",
  "spam": {
    "key": "<UNIQUE SPAM ID>",
    "address_list": [
      "spam_address1@example.com",
      "spam_address2@example.com"
    ]
  }
}
```

### Request Details

| Element | Type | Description | Default |
| --- | --- | --- | --- |
| `subject` | String | The subject line of your email, encoded as declared in `transfer_encoding`. | None; Required |
| `html` | String | The email source of your email, encoded as declared in `transfer_encoding`. | None; Required if no `url` |
| `url` | String | A URL pointing to the email source of your email. | None; Required if no `html` |
| `transfer_encoding` | String | One of `base64`, `quoted-printable`, `7bit`, or `8bit`. | `8bit`; `subject` and `html` should be encoded as described by this field. |
| `charset` | String | The character set your HTML is encoded in. | `utf-8`; `subject` and `html` should be encoded as described by this field. |
| `free_test` | Boolean | If true, run as a free test with limited features. | `false` |
| `sandbox` | Boolean | If true, run without creating any actual content. | `false` |
| `reference_id` | String | Enterprise customers can set this value for searching and internal reporting. | None; Enterprise only |
| `customer_id` | String | Enterprise customers can set this value for searching and internal reporting. | None; Enterprise only |
| `headers` | Object | Enterprise customers can populate this object with X-Header style key/value pairs whose keys begin with `"X-"`, but not with the reserved `"X-EOA"` prefix, to assist in test retrieval. ie: `{ "X-Cake":"Best123", "X-Fun":"Yes456" }` | None; Enterprise only |
| `clients` | Array of String | An array of string IDs as returned from [client list](https://api.emailonacid.com/docs/latest/email-clients) functions. | Default list as returned from `email/clients/default` |
| `image_blocking` | Boolean | If true, run a test with images blocked in clients that support it. | `false` |
| `spam` | Object | As below. | None; if set, a Spam Test will be run with the Email Test |
| `spam->test_method` | String | One of "eoa", "smtp", or "seed". The meanings of these values are explained in the [Spam Test](https://api.emailonacid.com/docs/latest/spam-testing#create-test) section. | "eoa" |
| `spam->smtp_info` | Object | An object containing the SMTP Authentication info. | None; Required if `test_method` is `"smtp"` |
| `spam->smtp_info->host` | String | The SMTP host. | None; Required |
| `spam->smtp_info->port` | Integer | The SMTP port. | 25 |
| `spam->smtp_info->secure` | String | One of "ssl", "tls", or "". | "" |
| `spam->smtp_info->username` | String | The SMTP username. | None |
| `spam->smtp_info->password` | String | The SMTP password. | None |
| `spam->from_address` | String | Address to send the email from. | None |
| `spam->key` | String | Seedlist Key to use. Generated ahead of time using [Reserve Seed List](https://api.emailonacid.com/docs/latest/spam-testing#reserve-seed-list). | None; Optional if `test_method` is `"seed"` |

Get Tests
---------

This call returns a list of all available Email Tests and some metadata about them. Email Tests are stored for 90 days.

URL:
----

```
GET https://api.emailonacid.com/v5/email/tests
```

Example Response:
-----------------

```
[
  {
    "id": "<test_id>",
    "date": 1773275003,
    "type": "email-test",
    "headers": {
        "X-EXAMPLE": "My Header"
    }
  },
  {
    "id": "<test_id>",
    "date": 1773275003,
    "type": "spam-test",
    "headers": {}
  }
]
```

Search Tests
------------

This call returns a list of Email Tests that match the criteria in the query string and some metadata about them. Its structure is identical to the above call.

The query string is a standard URL parameterized version containing any or all of the following parameters.

URL:
----

```
GET https://api.emailonacid.com/v5/email/tests?<query_string>
```

### Query String Details

| Name | Description | Example |
| --- | --- | --- |
| `from` | The starting point of your test date range. | `from=2026-03-12 00:23:23`, `from=1773275003`, `from=yesterday` |
| `to` | The ending point of your test date range. | `to=2026-03-12 00:23:23`, `to=1773275003`, `to=yesterday` |
| `subject` | The "subject" field of returned tests must contain the exact string. This search is case-insensitive. | `subject=My+example+test`, `subject=Another%20example`, `subject=A%2B tests` |
| `headers` | Enterprise users can use this field in a KV array of x-headers submitted with the test. This is an AND match, meaning all headers must be present to return. | `headers[x-fun]=most+fun&headers[x-cake]=best+cake` |
| `results` | The number of results to return. Must be between 1 and 200. The default value is 50 | `results=50` |
| `page` | The page number. If you submit a number higher than the number of pages in the data, an empty array will be returned. The default value is 1 | `page=2` |

Get Test Info
-------------

This call returns the subject and submission time in UNIX timestamp format. It will also contain one to three properties containing an array of clients. The “completed” property shows clients that have completed screenshots uploaded. The “processing” property contains clients which are still being processed by our system. The “bounced” property contains clients that were bounced by the destination and cannot be retried.

This call will automatically requeue screenshots if they stay in processing for more than three minutes.

URL:
----

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>
```

Example Response:
-----------------

```
{
  "subject": "Test Subject",
  "date": 1470034800,
  "completed": [
    "outlook13",
    "iphone6p_9"
  ],
  "processing": [
    "cc_chr26_win"
  ],
  "bounced": [
    "ffr_chr26_win"
  ]
}
```

Delete Test
-----------

This call marks an Email Test as deleted. Once it is deleted, it cannot be recovered.

URL:
----

```
DELETE https://api.emailonacid.com/v5/email/tests/<test_id>
```

Example Response:
-----------------

```
{
  "success": true
}
```

Get Results
-----------

This call returns detailed results for screenshots including their upload locations, send times, completion times, and information about bounces, if any. <test_id> is a test ID returned from test creation or the get test list functions. The <client_id> is optional and restricts the returned data to a single client if present. If the client is not present in the test or is invalid, an error will be returned.

Any reprocessing that is done will replace the images in these locations. The image locations are generated programmatically before the screenshots are complete, so the presence of a URL in the call is not a guarantee that the file will be present. Use the “status” property to determine whether or not the file is present in the location, or you can manually test the URL provided. If the file is not present, you will receive a 403 Forbidden response from the endpoint.

SCREENSHOT URLS
---------------

Screenshot URLs contain direct access to screenshot images, and remain valid throughout the life of the test (90 days from test creation). Access to screenshot URLs are done through either **Basic Authentication** or **Presigned URLs**.

### Basic Authentication

Screenshot URLs are accessed using the same authentication credentials used on all other API requests. When Basic Authentication is used, the temporary nature of presigned URLs are overridden and the same URL can be used through the life of a test (90 days), provided basic auth credentials are sent along with the request.

### Presigned URLs

If no basic authentication credentials are sent along with the request, the default authentication scheme is a form of presigned URLs that provide a time-limited URL (24 hours) for accessing screenshot images. With that in mind, it's important to note that **screenshot URLs are dynamic**, and it is strongly recommended that an API call to **Get Results** is made each time to retrieve a fresh set of screenshot URLs.

URL:
----

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>/results[/<client_id>]
```

Example Response:
-----------------

```
{
  "outlook03": {
    "id": "outlook03",
    "display_name": "Outlook 2003",
    "client": "Outlook 2003",
    "os": "Windows",
    "category": "Application",
    "screenshots": {
      "default": "<url>",
      "no_images": "<url>"
    },
    "thumbnail": "<url>",
    "full_thumbnail": "<url>",
    "status": "Processing",
    "status_details": {
      "submitted": 1468789495,
      "attempts": 1
    }
  },
  "iphone6p_9": {
    "id": "iphone6p_9",
    "display_name": "iPhone 6+ (iOS 9)",
    "client": "iPhone 6+",
    "os": "iOS9",
    "category": "Mobile",
    "screenshots": {
      "default": "<url>",
      "no_images": "<url>",
      "horizontal": "<url>",
      "horizontal_no_images": "<url>"
    },
    "thumbnail": "<url>",
    "full_thumbnail": "<url>",
    "status": "Complete",
    "status_details": {
      "submitted": 1468789495,
      "completed": 1468789503,
      "attempts": 1
    }
  },
  "ffr_chr26_win": {
    "id": "ffr_chr26_win",
    "display_name": "Free.fr Chrome (Windows)",
    "client": "Free.fr",
    "os": "Windows",
    "category": "Web",
    "browser": "Chrome",
    "screenshots": {
      "default": "<url>",
      "no_images": "<url>"
    },
    "thumbnail": "<url>",
    "full_thumbnail": "<url>",
    "status": "Bounced",
    "status_details": {
      "submitted": 1468789495,
      "bounce_code": "550 5.5.0",
      "bounce_message": "<message>"
    }
  }
}
```

### Response Details

| Element | Description |
| --- | --- |
| `id` | Our unique identifier for the email client. This code can be used when creating new Email Tests. |
| `display_name` | A presentable name of the email client. |
| `client` | Name of the email client. |
| `os` | The name of the OS that this client is running on. |
| `category` | The type of client this is: one of "Application", "Mobile", or "Web" |
| `browser` | If this is client is in a browser, the name of the browser the client is running in. |
| `screenshots` | An object of all screenshots available for this client. Possible properties of this object are `default`, `no_images` if `image_blocking` is true on both the test and the client, `horizontal` if `rotate` is true for the client, and `horizontal_no_images` if both `no_images` and `horizontal` exist. |
| `thumbnail` | The URL to the cropped result thumbnail. |
| `full_thumbnail` | The URL to the full result thumbnail. **Available in [API V5.0.1](https://api.emailonacid.com/docs/latest/overview#micro-versions-v5-0-1) and later** |
| `status` | A string describing the current status. One of `Complete`, `Processing`, `Bounced`, or `Pending`. |
| `status_details` | An object with properties depending on the status. |
| `status_details->submitted` | UNIX timestamp the screenshot was sent. |
| `status_details->completed` | UNIX timestamp the screenshot was completed. |
| `status_details->bounce_code` | If bounced, the code the remote server returned. |
| `status_details->bounce_message` | If bounced, the message the remote server returned. |

Reprocess Screenshots
---------------------

Sometimes strange things happen on the internet. If a strange result has come back in your screenshot, use this function to tell us to retake your screenshot free of charge.

The request should contain an object with a property of “clients” that contains a list of clients in the `<test_id>` provided. The object returned will have a “success” value indicating if the attempt was successful. If it is false, there will be a “reason” value describing the failure reason.

URL:
----

```
PUT https://api.emailonacid.com/v5/email/tests/<test_id>/results/reprocess
```

Example Request Body:
---------------------

```
{
  "clients": [
    "iphone6p_9",
    "gmail_chr26_win",
    "outlook16"
  ]
}
```

Example Response:
-----------------

```
{
  "iphone6p_9": {
    "success": true,
    "remaining_reprocesses": 19,
    "regional": false
  }
}
```

Get Test Content
----------------

Each of these calls will return an object with a single property “content” that contains the desired format of content. <test_id> is a test ID returned from test creation or the get test list functions.

Example Response:
-----------------

```
{
  "content": <html>
}
```

HTML Content
------------

This call returns the HTML associated with your Email Test. This is what is sent to our servers.

### URL:

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>/content
```

Inlined CSS Content
-------------------

This call returns HTML with all stylesheets inlined into the HTML.

### URL:

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>/content/inlinecss
```

Text Only Content
-----------------

This call returns a plain text version of your HTML. This approximates what will be displayed on devices that do not support HTML content. Our system does not currently support multipart emails, so if you send a separate text/plain section when you send your email, this may not be accurate to what users see. Additionally, devices may differ in their plain text renderings, so this function should be used more as a guide than as an exact preview.

### URL:

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>/content/textonly
```

Spam Results
------------

This call returns an object containing the status of your spam result, if you submitted your test with spam processing. If you did not submit with spam processing, you will receive an error. The object will be identical to that received from the [Spam Testing version of the function](https://api.emailonacid.com/docs/latest/spam-testing#get-results).

URL:
----

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>/spam/results
```

Example Response:
-----------------

```
[
  {
    "client": "SPAM CLIENT 1",
    "type": "b2c",
    "spam": 1,
    "details": "SPAM DETAILS"
  },
  {
    "client": "SPAM CLIENT 2",
    "type": "b2b",
    "spam": -1,
    "details": ""
  }
]
```

Spam Seed List
--------------

This call returns a list of email addresses to send to for your seed list type spam test. If your spam test was not a seed list type or you did not run the test with spam processing, you will receive an error.

URL:
----

```
GET https://api.emailonacid.com/v5/email/tests/<test_id>/spam/seedlist
```

Example Response:
-----------------

```
[
  "address1@example.com",
  "address2@example.com"
]
```
