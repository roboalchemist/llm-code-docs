# Source: https://api.emailonacid.com/docs/latest/email-clients

Title: Email on Acid - API Version 5.0 Documentation

URL Source: https://api.emailonacid.com/docs/latest/email-clients

Markdown Content:
Get Clients
-----------

This call returns a list of available email clients. If you are on a client-restricted plan, this will only show the clients that you are eligible to select. The object will be structured as shown here.

The object will contain a “clients” property, with properties corresponding to the client IDs. Each of these properties will contain an object containing the client ID, a printable client name, and OS. Clients are split into three “classes”: “Web”, “Application”, and “Mobile”. “Browser” type clients will contain a “browser” property.

The “rotate” and “image_blocking” describe client features. The “default” property shows whether or not this client will be processed when submitting a test without setting the clients.

Missing properties should be interpreted as a feature NOT being supported (i.e. equivalent to “false”). The API MAY respond with “false”.

URLs:
-----

```
GET https://api.emailonacid.com/v5/email/clients
```

Example Response:
-----------------

```
{
  "clients": {
    "iphone6p_9": {
      "id": "iphone6p_9",
      "client": "iPhone 6+ (iOS9)",
      "os": "iOS 9",
      "category": "Mobile",
      "rotate": true,
      "image_blocking": true,
      "default": true
    },
    "gmail_chr26_win": {
      "id": "gmail_chr26_win",
      "client": "Gmail",
      "os": "Windows",
      "category": "Web",
      "browser": "Chrome",
      "image_blocking": true,
      "default": true
    },
    "outlook16": {
      "id": "outlook16",
      "client": "Outlook 2016",
      "os": "Windows",
      "category": "Application",
      "image_blocking": true
    }
  }
}
```

### Response Details

| Element | Description |
| --- | --- |
| `id` | Our unique identifier for the email client. This code can be used when creating new Email Tests. |
| `client` | Name of the email client. |
| `os` | The name of the OS that this client is running on. |
| `category` | The type of client this is: one of "Application", "Mobile", or "Web" |
| `browser` | If this is client is in a browser, the name of the browser the client is running in. |
| `rotate` | A boolean value indicating if this client supports orientation changes. If it is missing, assume `false`. |
| `image_blocking` | A boolean value indicating if this client supports image blocking. If it is missing, assume `false`. |
| `free` | A boolean value indicating if this client can be used with free tests. If it is missing, assume `false`. |
| `default` | A boolean value indicating if this client will be included if no client key is sent with test creation. If it is missing, assume `false`. |

Get Default Clients
-------------------

This call returns a list of client IDs currently configured to be processed by default.

The object will contain a single property of “clients”, which will be an array of client IDs returned from the available client list.

URLs:
-----

```
GET https://api.emailonacid.com/v5/email/clients/default
```

Example Response:
-----------------

```
{
  "clients": [
    "iphone6p_9",
    "gmail_chr26_win",
    "outlook16"
  ]
}
```

Set Default Clients
-------------------

This call updates your configured default clients and returns the updated list of default clients.

The request must contain a property of “clients” that contains an array of client IDs as returned from the available client list.

The response will contain a property of “clients” that contains the array of client IDs as returned from the available client list. If your request contained invalid client IDs, the system will remove them from the list and report them in a separate “warnings” property. If you send no valid clients, your default client list will not change and an error will be reported. If you send an empty array, your default list will be cleared and ALL clients will be processed when you submit a test.

URLs:
-----

```
PUT https://api.emailonacid.com/v5/email/clients/default
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
  "clients": [
    "iphone6p_9",
    "gmail_chr26_win",
    "outlook16"
  ]
}
```
