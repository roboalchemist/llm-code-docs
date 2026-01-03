# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-templates.md

# Templates

Mailgun allows you to store predefined email templates and use them to send messages by simply referencing the template name. Each domain supports up to 100 templates, with each template allowing up to 10 versions.

For comprehensive information about templates, refer to the [Template API documentation](https://documentation.mailgun.com/docs/mailgun/api-reference/send/mailgun/templates). To learn about creating templates using the Template Builder interface, see [Email Templates](https://help.mailgun.com/hc/en-us/articles/360021380793-Email-Templates).

## Creating and Using Templates

You can create templates either through the Template API or using the Template Builder in the Mailgun UI.

### Creating a Template via API


```bash
curl -X POST -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/templates \
    --form-string template='<div class="entry"> <h1>{{title}}</h1> <div class="body"> {{body}} </div> </div>' \
    -F name='template.test' \
    -F description='Sample template'
```

The response returns stored template information:


```json
{
  "template": {
     "createdAt": "Wed, 29 Aug 2018 23:31:13 UTC",
     "description": "Sample template",
     "name": "template.test"
  },
  "message": "template has been stored"
}
```

### Sending Messages with Templates

Once your template is created, you can send messages using it:


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Excited User <postmaster@YOUR_DOMAIN_NAME>' \
    -F to=recipient@example.com \
    -F subject='Hello there!' \
    -F template="template.test" \
    -F t:variables='{"title": "API documentation", "body": "Sending messages with templates"}'
```

When sending MIME messages, pass template variables using the `X-Mailgun-Template-Variables` header instead of the `t:variables` parameter.

## Handlebars Template Engine

Mailgun templates use a customized version of Handlebars, a popular templating engine. To provide dynamic values for substitution, use the `t:variables` parameter or the `X-Mailgun-Template-Variables` header.

Mailgun supports the following Handlebars block helpers: `if`, `unless`, `each`, `with`, and `equal`.

### The `if` Block Helper

Use the `if` helper to conditionally render content based on variable values.

**Example: Dynamic language selection**


```html
{{#if english}}
<p>This text is in the English language.</p>
{{else if spanish}}
<p>Este texto estÃ¡ en idioma espaÃ±ol.</p>
{{else if french}}
<p>Ce texte est en langue franÃ§aise.</p>
{{/if}}
```

Pass this data via `t:variables`:


```json
{"spanish": true}
```

This renders the Spanish version of the text.

### The `unless` Block Helper

The `unless` helper renders a block only when the condition is false.

**Example: Payment reminder**


```html
{{#unless paid}}
<h3 class="warning">WARNING: Your account is past due and will be suspended shortly. Please contact our billing department for assistance</h3>
{{/unless}}
```

Pass this data via `t:variables`:


```json
{"paid": false}
```

This displays the warning when the account is unpaid.

### The `each` Block Helper

The `each` helper allows you to iterate over arrays or lists.

**Example: Listing scheduled services**


```html
{{#each user.services}}
<li>You scheduled {{this.service}} on {{this.date}}</li>
{{/each}}
```

Pass this data via `t:variables`:


```json
{
  "user": {
    "services": [
      {
        "date": "07/30/2019",
        "service": "deliverability consultation"
      },
      {
        "date": "08/05/2019",
        "service": "sales consultation"
      }
    ]
  }
}
```

This renders as:

* You scheduled deliverability consultation on 07/30/2019
* You scheduled sales consultation on 08/05/2019


### The `with` Block Helper

The `with` helper shifts the context for a section of your template, making it easier to access nested properties without repeating the parent object name.

**Example: Simplifying nested author information**


```html
<div class="entry">
  <h1>{{title}}</h1>

  {{#with author}}
  <h2>By {{firstName}} {{lastName}}</h2>
  <p>Email: {{email}}</p>
  {{/with}}
</div>
```

Pass this data via `t:variables`:


```json
{
  "title": "My first post!",
  "author": {
    "firstName": "Jean",
    "lastName": "Valjean",
    "email": "jean@example.com"
  }
}
```

This renders as:


```html
<div class="entry">
  <h1>My first post!</h1>

  <h2>By Jean Valjean</h2>
  <p>Email: jean@example.com</p>
</div>
```

### The `equal` Block Helper

The `equal` helper renders content when a variable exactly matches a specific value. This is useful for displaying different content based on user attributes like subscription tier, account status, or preferences.

**Example: Customizing content by subscription tier**


```html
{{#equal subscription "free"}}
<p>Upgrade to Pro to unlock advanced features!</p>
<a href="/upgrade">Upgrade Now</a>
{{/equal}}

{{#equal subscription "pro"}}
<p>Thanks for being a Pro member! Enjoy your premium features.</p>
{{/equal}}

{{#equal subscription "enterprise"}}
<p>Welcome back! Your dedicated account manager is here to help.</p>
{{/equal}}
```

Pass this data via `t:variables`:


```json
{"subscription": "pro"}
```

This displays the Pro member message.

**Note:** The `equal` helper converts both values to strings before comparing, so `{"count": 5}` and `{"count": "5"}` are treated as equal.

## Complete Example: Using All Handlebars Helpers

The following example demonstrates all supported Handlebars helpers working together in a single template. This comprehensive template shows how you can combine `with`, `equal`, `unless`, `if`, and `each` to create dynamic, personalized email content.

### Create the Template


```bash
curl -X POST -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/templates \
    -F name='comprehensive.test' \
    -F description='Complete test template with all Handlebars helpers' \
    --form-string template='<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; }
    .warning { color: red; }
    .premium { background-color: #f0f8ff; padding: 10px; }
  </style>
</head>
<body>
  <h1>Order Confirmation</h1>
  
  {{#with customer}}
  <p>Hello {{firstName}} {{lastName}},</p>
  <p>Email: {{email}}</p>
  {{/with}}
  
  {{#equal accountType "premium"}}
  <div class="premium">
    <p>ð Premium Member Perk: You have earned 2x points on this order!</p>
  </div>
  {{/equal}}
  
  {{#equal accountType "basic"}}
  <p>Upgrade to Premium for exclusive benefits and rewards!</p>
  {{/equal}}
  
  {{#unless paymentReceived}}
  <div class="warning">
    <p>â ï¸ WARNING: Payment pending. Your order will ship once payment is confirmed.</p>
  </div>
  {{/unless}}
  
  {{#if paymentReceived}}
  <p>â Payment confirmed! Your order is being processed.</p>
  {{/if}}
  
  <h2>Order Items:</h2>
  <ul>
  {{#each items}}
    <li>{{this.name}} - Quantity: {{this.quantity}} - ${{this.price}}</li>
  {{/each}}
  </ul>
  
  {{#if spanish}}
  <p>Gracias por su compra!</p>
  {{else if french}}
  <p>Merci pour votre achat!</p>
  {{else}}
  <p>Thank you for your purchase!</p>
  {{/if}}
  
</body>
</html>'
```

### Send a Message Using the Template


```bash
curl -s --user 'api:YOUR_API_KEY' \
    https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages \
    -F from='Order System <orders@YOUR_DOMAIN_NAME>' \
    -F to='recipient@example.com' \
    -F subject='Your Order Confirmation #12345' \
    -F template="comprehensive.test" \
    -F t:variables='{
      "customer": {
        "firstName": "Maria",
        "lastName": "Garcia",
        "email": "maria@example.com"
      },
      "accountType": "premium",
      "paymentReceived": true,
      "items": [
        {
          "name": "Wireless Headphones",
          "quantity": 1,
          "price": "79.99"
        },
        {
          "name": "Phone Case",
          "quantity": 2,
          "price": "24.99"
        },
        {
          "name": "USB Cable",
          "quantity": 3,
          "price": "12.99"
        }
      ],
      "spanish": false,
      "french": false
    }'
```

### Testing Different Scenarios

You can modify the JSON data to test different template behaviors:

* Change `accountType` to "basic" to see the upgrade message instead of the premium perk
* Set `paymentReceived` to false to display the payment warning
* Change `spanish` to true to see the Spanish thank you message
* Modify the `items` array to add or remove products from the order list
* Update customer information within the `customer` object to test the `with` helper