# Source: https://developers-classic.mailerlite.com/docs/authentication.md

# Authentication

[block:api-header]
{
  "type": "basic",
  "title": "How to authenticate"
}
[/block]

Every request to MailerLite API should have HTTP header containing a valid API key that we use to authenticate the account:

`X-MailerLite-ApiKey` - your account's API key.

API key can be obtained from **Integrations** page when you are logged into the MailerLite application (screenshot below) or just simply click [here](https://app.mailerlite.com/integrations/api/).

![Where to find API key?](https://kb.mailerlite.com/wp-content/uploads/integrations.png)

[block:callout]
{
  "type": "danger",
  "title": "Usage of a key on a client side",
  "body": "When you make a request to API from a client side, you should see a similar message on your browser's console:\n\n```\nRequest header field x-mailerlite-apikey is not allowed by Access-Control-Allow-Headers in preflight response\n```\n\nAPI key is designed for server-side usage and it cannot be used directly on the client side making AJAX calls because it will be exposed publicly. So it is forbidden due to security concerns."
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Authenticated request example"
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl -v https://api.mailerlite.com/api/v2 \\\n-H \"X-MailerLite-ApiKey: {replace-it-with-your-api-key}\"\n-H \"Content-Type: application/json\"",
      "language": "curl",
      "name": "cURL"
    }
  ]
}
[/block]

[block:api-header]
{
  "type": "basic",
  "title": "Authentication errors"
}
[/block]

You might get errors described below when authentication fails. You can read more about response and errors [in this page](docs:response).

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"error\": {\n    \"code\": 1,\n    \"message\": \"Unauthorized\"\n  }\n}",
      "language": "json",
      "name": "HTTP response when API key is not provided"
    },
    {
      "code": "{\n  \"error\": {\n    \"code\": 302,\n    \"message\": \"API-Key Unauthorized\"\n  }\n}",
      "language": "json",
      "name": "HTTP response when API key is not valid"
    }
  ]
}
[/block]