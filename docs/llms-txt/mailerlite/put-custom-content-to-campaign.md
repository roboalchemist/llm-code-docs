# Source: https://developers-classic.mailerlite.com/reference/put-custom-content-to-campaign.md

# /campaigns/:id/content

Upload your HTML template to created campaign [Rate limited]

You can use your custom HTML template and associate it with created campaign using this endpoint.

[block:api-header]
{
  "type": "basic",
  "title": "HTML template"
}
[/block]

HTML template must contain *head* and *body* tags,  a link for unsubscribing is also required.

Example of HTML template with unsubscribe link:

```
<html>
    <head>
        <title>Email template</title>
    </head>
    <body>
        <h1>Title</h1>
        <p>Content</p>
        <p>
            <small>
                <a href="{$unsubscribe}">Unsubscribe</a>
            </small>
        </p>
    </body>
</html>
```

[block:api-header]
{
  "type": "basic",
  "title": "Plain text mail"
}
[/block]

Some email clients do not support HTML emails so you need to set plain text email and it must contain these variables:

* {$unsubscribe} - unsubscribe link
* {$url} - URL to your HTML newsletter