# Source: https://documentation.mailgun.com/docs/mailgun/sdk/nodejs_sdk.md

# Node.js

a
img

    Official Mailgun Node.JS SDK

### Installation

- Requires node.js >= 18.x


Install mailgun.js with:


```sh
npm install mailgun.js
```

## Setup Client

Next, require the module and instantiate a mailgun client by calling `new Mailgun(formData)` and then using `mailgun.client` setup the client with basic auth credentials `(username: 'api', key: 'key-yourkeyhere')`.

NOTE: starting from version 3.0 you need to pass FormData (we need this to keep library universal). For node.js you can use `form-data` library.

IMPORTANT: if you are using EU infrastructure, you need to also pass `url: 'https://api.eu.mailgun.net'` together with auth credentials as stated in [Mailgun docs](https://documentation.mailgun.com/en/latest/quickstart-sending.html#send-via-api)

### Imports

Once the package is installed, you can import the library using `import` or `require` approach:


```js
  const formData = require('form-data');
  const Mailgun = require('mailgun.js');
  const mailgun = new Mailgun(formData);
  const mg = mailgun.client({username: 'api', key: process.env.MAILGUN_API_KEY || 'key-yourkeyhere'});
```

### Usage

Here's a simple example on how to send an email. As always, please consult the repository readme for full details.


```JS
mg.messages.create('sandbox-123.mailgun.org', {
    from: "Excited User <mailgun@YOUR-SANDBOX-DOMAIN>",
    to: ["test@example.com"],
    subject: "Hello",
    text: "Testing some Mailgun awesomness!",
    html: "<h1>Testing some Mailgun awesomness!</h1>"
  })
  .then(msg => console.log(msg)) // logs response data
  .catch(err => console.error(err)); // logs any error
```