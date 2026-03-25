# Source: https://docs.xano.com/the-function-stack/functions/apis-and-lambdas/lambda-functions/supported-libraries.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Libraries

## Math.js

The [Math.js](https://mathjs.org/) library provides support for advanced math formulas and expressions.

This library is accessible within the Lambda through the library variable `math`. The standard JavaScript Math library is accessible through the variable `Math`, so make sure you pay attention to case sensitivity, so that you are using the appropriate library.

Here is an example showing how to perform the negative square root of 4.

```cpp  theme={null}
return math.sqrt(-4);
// 2i
```

## Crypto

The [Crypto](https://nodejs.org/api/crypto.html) library is built into [Node.js](https://nodejs.org/) and useful for performing common routines related to cryptography.

This library is accessible within the Lambda through the library variable `crypto`.

Here is an example showing how to perform a SHA 256 digital signature.

```javascript  theme={null}
var data = 'test123';
return crypto.createHash('sha256').update(data).digest('hex');
// ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae
```

## Nodemailer

The [Nodemailer](https://nodemailer.com/about/) library provides support to send email using SMTP and other transport mechanisms.

This function is accessible within the Lambda through the function variable `nodemailer`.

Here is an example showing how to send a test email through ethereal.email. This example is taken from the Nodemailer documentation.

```csharp  theme={null}
let testAccount = await nodemailer.createTestAccount();

// create reusable transporter object using the default SMTP transport
let transporter = nodemailer.createTransport({
  host: 'smtp.ethereal.email',
  port: 587,
  secure: false, // true for 465, false for other ports
  auth: {
    user: testAccount.user, // generated ethereal user
    pass: testAccount.pass, // generated ethereal password
  },
});

// send mail with defined transport object
let info = await transporter.sendMail({
  from: '"Fred Foo 👻" <foo@example.com>', // sender address
  to: 'bar@example.com, baz@example.com', // list of receivers
  subject: 'Hello ✔', // Subject line
  text: 'Hello world?', // plain text body
  html: '<b>Hello world?</b>', // html body
});

return nodemailer.getTestMessageUrl(info);
// Preview URL: https://ethereal.email/message/WaQKMgKddxQDoou...
```

## Mailparser

The [Mailparser](https://nodemailer.com/about/) library is an addon for Nodemailer.

This function is accessible within the Lambda through the function variable `mailparser`.

Here is an example showing how to instantiate it.

```javascript  theme={null}
const MailParser = mailparser.MailParser;
let parser = new MailParser();

return typeof parser; // object
```

## Promisify

The [Promisify](https://nodejs.org/dist/latest-v8.x/docs/api/util.html#util_util_promisify_original)function is built into [Node.js](https://nodejs.org/) and is useful for converting legacy callback routines into a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) based variant. Promises are a standardization of how responses are received in asynchronous programming, which makes it possible to rely on shorthand keywords like [async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

This function is commonly used along with the Crypto library for those wishing to use that library with Promises instead of callbacks.

This function is accessible within the Lambda through the function variable `promisify`.

Here is an example showing how to use Promisify on the Crypto library to generate an [HMAC](https://en.wikipedia.org/wiki/HMAC) secret key.

```javascript  theme={null}
return (await promisify(crypto.generateKey)('hmac', {length: 64}))
    .export()
    .toString('hex');
```

## Node Libraries

The following node libraries are available within Xano's Lambda support: [DNS](https://nodejs.org/docs/latest-v16.x/api/dns.html), [HTTP](https://nodejs.org/docs/latest-v16.x/api/http.html), [HTTPS](https://nodejs.org/docs/latest-v16.x/api/https.html), and [NET](https://nodejs.org/docs/latest-v16.x/api/net.html).

They are accessible within the Lambda through the function variables: `dns`, `http`, `https`, and `net`.

Here is an example showing how to create a custom https agent.

```php  theme={null}
const httpsAgent = new https.Agent({
	keepAlive: true
});
```

## Socks

The [Socks](https://www.npmjs.com/package/socks) library is a fully featured SOCKS proxy client supporting SOCKSv4, SOCKSv4a, and SOCKSv5 protocols.

This library is accessible within the Lambda through the library variable `socks`.

Here is an example showing how to create a connection.

```javascript  theme={null}
const options = {
  proxy: {
    host: '159.203.75.200', // ipv4 or ipv6 or hostname
    port: 1080,
    type: 5 // Proxy version (4 or 5)
  },

  command: 'connect', // SOCKS command (createConnection factory function only supports the connect command)

  destination: {
    host: '192.30.253.113', // github.com (hostname lookups are supported with SOCKS v4a and 5)
    port: 80
  }
};

return await socks.SocksClient.createConnection(options);
```

## Ethers.js

This [library](https://docs.ethers.io/) aims to be a complete and compact library for interacting with the Ethereum Blockchain and its ecosystem.

This is accessible within the Lambda through the function variable `ethers`.

Here is an example of formatting a number in Ether.

```javascript  theme={null}
return ethers.utils.formatEther(10); // 0.0000000000000001
```

## Azure/Identity

This [library](https://learn.microsoft.com/en-us/javascript/api/@azure/identity/?view=azure-node-latest) provides [Azure Active Directory (Azure AD)](https://learn.microsoft.com/azure/active-directory/fundamentals/active-directory-whatis) token authentication through a set of convenient TokenCredential implementations.

This is accessible within the Lambda through the function variable `azure.identity`.

Here is an example of generating default Azure credentials with Azure/Identity.

```javascript  theme={null}
return new azure.identity.DefaultAzureCredential();
```

## Azure/Service-Bus

Here is an example of generating a service bus client connection with Azure/Service-Bus.

This is accessible within the Lambda through the function variable `azure.serviceBus`.

This [library](https://www.npmjs.com/package/@azure/service-bus) provides access to [Azure Service Bus](https://azure.microsoft.com/services/service-bus/), which is a highly-reliable cloud messaging service from Microsoft.

```javascript  theme={null}
return new azure.serviceBus.ServiceBusClient('your-connection-string');
```

## Zeebe

This [library](https://www.npmjs.com/package/zeebe-node) is a Node.js gRPC client for [Zeebe](https://zeebe.io/), the workflow engine in Camunda Platform 8.

This is accessible within the Lambda through the function variable `zeebe`.

Here is an example of generating a timeout duration with Zeebe:

```javascript  theme={null}
return zeebe.Duration.seconds.of(30);
```

## CryptoJS

This [library](https://www.npmjs.com/package/crypto-js) is a Node.js package of crypto standards.

This is accessible within the Lambda through the function variable `cryptojs`.

Here is an example of encrypting a string using CryptoJS:

```javascript  theme={null}
return cryptojs.AES.encrypt('my message', 'secret key 123').toString();
```

## UUID

This [library](https://www.npmjs.com/package/uuid) is a Node.js package for the creation of RFC4122 UUID's

This is accessible within the Lambda through the function variable `uuid`.

Here is an example of creating a UUID:

```javascript  theme={null}
return uuid.v4();
```

## JWT: Jose

This [library](https://www.npmjs.com/package/jose) is JavaScript module for JSON Object Signing and Encryption, providing support for JSON Web Tokens (JWT), JSON Web Signature (JWS), JSON Web Encryption (JWE), JSON Web Key (JWK), JSON Web Key Set (JWKS), and more

This is accessible within the Lambda through the function variable `jose`.

Here is an example of creating a signed JWT:

```javascript  theme={null}
const secret = new utils.TextEncoder().encode(
  "cc7e0d44fd473002f1c42167459001140ec6389b7353f8088f4d9a95f2f596f2"
);
const alg = "HS256";

const jwt = await new jose.SignJWT({ "urn:example:claim": true })
  .setProtectedHeader({ alg })
  .setIssuedAt()
  .setIssuer("urn:example:issuer")
  .setAudience("urn:example:audience")
  .setExpirationTime("2h")
  .sign(secret);

return jwt;
```

## Fast XML Parser

This [library](https://www.npmjs.com/package/fast-xml-parser) is a Node.js package for being able to parse, build, and validate XML.

This is accessible within the Lambda through the function variable `fastXmlParser`.

Here is an example of parsing an XML string:

```javascript  theme={null}
const parser = new fastXmlParser.XMLParser();

const result = parser.parse('<h1>Hey</h1>'); // { "h1": "Hey"}

return result;
```

## AWS4: Sign Request Signatures

This [library](https://www.npmjs.com/package/aws4) is a Node.js package for signing http/https requests using AWS Signature Version 4.

This is accessible within the Lambda through the function variable `aws4`.

Here is an example of parsing an XML string:

```javascript  theme={null}
var opts = { host: 'my-bucket.s3.us-west-1.amazonaws.com', path: '/my-object', service: 's3', region: 'us-west-1' }

aws4.sign(opts, { accessKeyId: '', secretAccessKey: '' })

https.request(opts, (res) => { ... });
```


Built with [Mintlify](https://mintlify.com).