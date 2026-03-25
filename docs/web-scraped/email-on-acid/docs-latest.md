# Source: https://api.emailonacid.com/docs/latest

Title: Email on Acid - API Version 5.0 Documentation

URL Source: https://api.emailonacid.com/docs/latest

Markdown Content:
[](https://api.emailonacid.com/docs/latest)

The Email on Acid API allows you to interact programatically with our system, enabling deeper integration with your internal tools. You can submit your emails to us either directly through the API calls, or you can use our Auto-Inbox feature to automatically process emailed content and use the API to check on the results.

You can also use our API to check your mail against spam filters with our Spam Test service.

* * *

[](https://api.emailonacid.com/docs/latest)
Postman Integration
-------------------

Email on Acid has a Postman Collection available for quick and easy exercise of our REST-based APIs. Variables for API credentials and other data elements can be found at the collection level. Use the button below for easy import into Postman. Don’t have Postman? Click [here](https://getpostman.com/).

[](https://api.emailonacid.com/docs/latest)
Authentication
--------------

All calls in this version are JSON, and must be authenticated with HTTP Basic Authentication. You will be provided with an API key, and your password is configurable through the web portal. The header should be the string `<api_key>:<account_password>` encoded in base-64. An example of this header is below.

Authorization: Basic WW91ck93bkFjY291bnRzRW1haWxPbkFjaWRBUElLZXkwMTIzNDU2Nzg5OllvdXJTZWN1cmVQYXNzd29yZA==
Testing Your Settings
---------------------

### URL:

`GET https://api.emailonacid.com/v5/auth`

### Example Response:

```
{
    "success": true
}
```

This URL will respond with error information if your request was set incorrectly.

[](https://api.emailonacid.com/docs/latest)
Sandbox
-------

If you wish to try our API, you can access it through a sandbox mode. Submit your request with the username and password of "sandbox".

[](https://api.emailonacid.com/docs/latest)
RESTful
-------

The API seeks to follow broad tenets of RESTful application within each resource type, but is not strictly constrained by those standards. Each method will describe an endpoint and HTTP method to use to access it.

### Headers:

We expect each request with a body to be provided as JSON, and if an Accept header is provided, it must accept `application/json`

Accept: application/json
Content-Type: application/json
If the header does not match, an error will be generated and sent as the response. [Details on errors](https://api.emailonacid.com/docs/latest#errors) can be found further down this page.

[](https://api.emailonacid.com/docs/latest)
Request Validation
------------------

This API seeks to be as permissive as possible with all requests — if we can understand it, we will use it. As you go through these docs, each call will explain which fields are required. If we cannot understand your request, [an error](https://api.emailonacid.com/docs/latest#errors) will be returned explaining how to fix your request.

[](https://api.emailonacid.com/docs/latest)
Client Frames
-------------

Client frames are images that test results are shown inside of. For example, on an iPhone 6 result, the image of an iPhone 6 is the "client frame". We provide these images free of charge to create a more immersive experience for your application.

[Download Client Frames](https://media.emailonacid.com/client_frames.zip)[](https://api.emailonacid.com/docs/latest)
Auto Inbox Submission
---------------------

Email Tests may be submitted by emailing your test content directly to us. This helps eliminate any potential discrepancies from the processing of your content prior to the send. We recommend this method if you do not control the final content of your send.

To submit an Auto-Inbox test, simply send your test email to the Auto-Inbox address provided to you with your credentials. If you need this information, please contact [support@emailonacid.com](mailto:support@emailonacid.com) for assistance.

To submit an Auto-Inbox test with a customer_id, you can use the "+" delimiter to attach the customer_id to your Auto-Inbox address, for example ZEv8x0fhjMAMSPL310MN+customer_id_here@api.mail.emailonacid.com. This allows our platform to accept emails directly from your customers and associate them with your API account.

### X-Headers (Enterprise Only)

Enterprise customers can supply custom X-Headers along with test content, which we store to assist in test retrieval. As a rule, all custom X-Headers beginning with "X-EOA" are reserved for our use, but we will track any other X-Header provided.

You may also use the following predefined X-Headers to overwrite the clients used for a single Email Test:

| X-Header | Description |
| --- | --- |
| `X-EOA-CLIENTS` | A comma-separated list of client IDs as returned from the [client list](https://api.emailonacid.com/docs/latest/email-clients#get-clients) method. |

A set of identifiers may be sent at once with proper concatenation with a character limit of up to 998 characters per line, per RFC #2822 and 5322. Below is an example of how the API expects the codes to be formatted. Input that does not follow this format will result in tests not being run for the malformed parameters:

`X-EOA-CLIENTS: outlook03,outlook10,iphone6p9,gmail_chr22_win`
Additionally, the following predefined X-Headers can be used to specify several parameters from the [email test creation](https://api.emailonacid.com/docs/latest/email-testing#create-test) call to assist in tracking:

| X-Header | Description |
| --- | --- |
| `X-EOA-USER-GUID` | Corresponds to `customer_id` in the [create email test](https://api.emailonacid.com/docs/latest/email-testing#create-test) request body. |
| `X-EOA-REFERENCE-ID` | Corresponds to `reference_id` in the [create email test](https://api.emailonacid.com/docs/latest/email-testing#create-test) request body. |

Below is an example of how the API expects these fields to be formatted. Input that does not follow this format may result in tests not being created:

```
X-EOA-USER-GUID: USER_GUID_VALUE
X-EOA-REFERENCE-ID: CUSTOMER_REFERENCE_ID_VALUE
```

For an example of how to set custom X-Headers for various clients, see the following link, or consult your ESP or mail client documentation:

*   [Thunderbird](http://kb.mozillazine.org/Custom_headers)
*   [Microsoft Exchange/Office 365](http://msdn.microsoft.com/en-us/library/office/dn596091(v=exchg.150).aspx)

### Test Retrieval

After sending a test, the Auto Inbox process will handle the email and submit it as an Email Test.

You can use the [get test list](https://api.emailonacid.com/docs/latest/test-search#get-test-list) API call to look up submitted tests.

[](https://api.emailonacid.com/docs/latest)
Test Storage
------------

Test results are stored on our servers for 90 days after a test has been processed. After 90 days the results will be removed from our system. This allows us to keep your results as fast as possible — though we will store the metadata internally for reporting purposes.

[](https://api.emailonacid.com/docs/latest)
Micro Versions
--------------

These are incremental updates to add new functionality to existing API calls. To access them, simply use the micro version in place of "v5" in your existing API calls. Current Micro versions and their features are detailed below.

### Current Micro Versions & Features

[](https://api.emailonacid.com/docs/latest)
#### v5.0.1

`GET https://api.emailonacid.com/v5.0.1/auth`

*    This version adds the "full thumbnail" element to the Email Testing [Get Results](https://api.emailonacid.com/docs/latest/email-testing#get-results) call, which provides a URL to full-length thumbnails for each result, instead of the fixed-height ones returned in the "thumbnail" element. 

[](https://api.emailonacid.com/docs/latest)
API Errors
----------

Our API will return an error if something goes wrong in the processing or your request contains incomplete/invalid data.

**Note:** All error responses will also have a Status Code of 400 or greater, depending on the error.

### Error Response:

```
{   "error":
    {   "name":"PermissionError",
        "message":"You do not have permission to access this resource"
    }
}
```

### Error Types and Messages:

| Type | Message |
| --- | --- |
| `NoAccept` | Invalid Accept header values. If set, this value must accept application/json. |
| `AccessDenied` | Your authentication to the API did not succeed. See the message for details on resolving the problem. |
| `RateLimited` | You have made more requests to the API than your pricing plan allows. If you need more requests, please contact support. |
| `InvalidJSON` | Your JSON failed to parse. Please check its validity. |
| `WrongVersion` | You are trying to access the API with an incompatible version. |
| `InvalidParameter` | Your GET query string was not parseable. See the message for further details. |
| `NotFound` | The URL you requested could not be found. |
| `BadMethod` | Your request used an unimplemented method. See the response's Accept header. |
| `BadRequest` | There was a problem with your request. See the message for more details. |
| `ServerError` | There was a problem processing your request. See the message for more details. |
| `ProcessingError` | There was a problem processing your request. See the message for more details. |
| `TestLimitReached` | For enterprise customers on a user-priced plan, the provided user has hit your established monthly test limit. |
| `PermissionError` | Your plan does not provide access to this feature. |
| `InvalidTestID` | The test ID provided could not be found or you do not have access to it. |
| `NoClient` | A required client code URL parameter is missing. |
| `NoClients` | A required `clients` parameter is missing. |
| `InvalidClient` | The client code(s) provided could not be found. |
| `InvalidFreeClient` | The mentioned `clients` are not included in free tests. |
| `InvalidTestClient` | The mentioned `clients` could not be found in this test. |
| `ClientNotFound` | The client code URL parameter provided could not be found in this test. |
| `NoSubject` | A required `subject` field was missing. |
| `NoSource` | You must provide either an HTML or URL source. |
| `InvalidURL` | The URL source provided was invalid. |
| `MissingCustomerID` | The enterprise package you are on requires a `customer_id` to be included. |
| `SMTPError` | The SMTP credentials had an invalid hostname. |
| `SMTPAuthenticationError` | The SMTP credentials provided could not be validated. |
| `InvalidSpamType` | You submitted a test with an invalid type. Must be one of "eoa", "smtp", or "seed" |
| `NoSpamResults` | This test was not run with spam processing. |
| `NoSeedList` | This test was not run with seed list spam processing. |
