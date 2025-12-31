# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/advanced-js-libraries.md

# Advance JS libraries

The Avaamo platform provides several wrapper functions on a list of native NodeJS libraries (npm packages) that can be used in Javascript during customization. See [NodeJS V8.16.0](https://nodejs.org/docs/latest-v8.x/api/), for more information.

### async&#x20;

* Supported version - **"async":"\~0.7.0".**  See [async npm package](https://www.npmjs.com/package/async/v/0.7.0), for more information.
* Provides functions for working with asynchronous JavaScript.
* The following is an example to use map function in async :

```javascript
async.map(['file1','file2','file3'], fs.stat, function(err, results){
    // results is now an array of stats for each file
});
```

### await

* Supported version -  **"asyncawait":"^1.0.6".** See [asyncawait npm package](https://www.npmjs.com/package/asyncawait/v/1.0.6), for more information.
* Used in asynchronous calls, when you must **await** for the returned promise.&#x20;
* The following is an example to use await in an API call:

```javascript
 return await(fetch(url, {
    method: 'POST',
    agent: agent,
    body: formBody,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    },
    timeout: 200000
  }).then((res) => {
  ....//Process the result
  }));
```

### AWS

* Supported version - **"aws-sdk":"^2.48.0".**  See [aws-sdk npm package](https://www.npmjs.com/package/aws-sdk/v/2.48.0), for more information.&#x20;
* Used to connect AWS SDK services.&#x20;
* The following is an example to display a list of S3 buckets in the console:

```javascript
// Set the region 
AWS.config.update({region: 'REGION'});

// Create S3 service object
s3 = new AWS.S3({apiVersion: '2006-03-01'});

// Call S3 to list the buckets
s3.listBuckets(function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data.Buckets);
  }
});
```

### Buffer

* Supported version - **"buffer":"^8.16.0".**  See [buffer npm package](https://nodejs.org/docs/latest-v8.x/api/buffer.html), for more information.
* Instances of the **Buffer** class are similar to arrays of integers but correspond to fixed-sized, raw memory allocations outside the V8 heap.
* The following are a few examples to use the **buffer** function:

```javascript
// Creates a zero-filled Buffer of length 10.
const buf1 = Buffer.alloc(10);

// Creates a Buffer of length 10, filled with 0x1.
const buf2 = Buffer.alloc(10, 1);

// Creates an uninitialized buffer of length 10.
// This is faster than calling Buffer.alloc() but the returned
// Buffer instance might contain old data that needs to be
// overwritten using either fill() or write().
const buf3 = Buffer.allocUnsafe(10);

// Creates a Buffer containing [0x1, 0x2, 0x3].
const buf4 = Buffer.from([1, 2, 3]);

// Creates a Buffer containing UTF-8 bytes [0x74, 0xc3, 0xa9, 0x73, 0x74].
const buf5 = Buffer.from('tést');

// Creates a Buffer containing Latin-1 bytes [0x74, 0xe9, 0x73, 0x74].
const buf6 = Buffer.from('tést', 'latin1');
```

### cipher

You can use **rijndaelEncrypt** in cipher function for encryption.

```javascript
let cipherText = cipher.rijndaelEncrypt(key, text)
```

### crypto

* Supported version - **"crypto":"\~8.16.1"**. See [Crypto npm package](https://nodejs.org/docs/latest-v8.x/api/crypto.html), for more information.
* Used for cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions
* The following is an example to use **crypto** function:

```javascript
const secret = 'abcdefg';
const hash = crypto.createHmac('sha256', secret)
                   .update('I love cupcakes')
                   .digest('hex');
console.log(hash);
```

### https

* Supported version - **"https":"\~8.16.1"**. See [Https npm package](https://nodejs.org/docs/latest-v8.x/api/https.html), for more information.
* Used for sending https requests in an API call.
* The following is an example to use **https.agent** function:

```javascript
const https = require('https');

https.get(<<url>>, (res) => {
  console.log('statusCode:', res.statusCode);
  console.log('headers:', res.headers);

  res.on('data', (d) => {
    process.stdout.write(d);
  });

}).on('error', (e) => {
  console.error(e);
});
```

### jsdom

* Supported version - **"jsdom":"^9.8.3"**. See [jsdom npm package](https://www.npmjs.com/package/jsdom/v/9.8.3), for more information.
* Used for testing and scraping real-world web applications.
* The following is an example that uses **jsdom** to parse a raw HTML:&#x20;

```javascript
jsdom.env(
  '<p><a class="the-link" href="https://github.com/tmpvar/jsdom">jsdom!</a></p>',
  ["http://code.jquery.com/jquery.js"],
  function (err, window) {
    console.log("contents of a.the-link:", window.$("a.the-link").text());
  }
);
```

### JWT

* Supported version - **"jsonwebtoken": "^7.4.0"**. See [JWT npm package](https://www.npmjs.com/package/jsonwebtoken/v/7.4.0), for more information.
* JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.&#x20;
* The following are a few examples of using JWT token:

```javascript
var token = JWT.sign({ foo: 'bar' }, 'shhhhh');
//backdate a jwt 30 seconds
var older_token = JWT.sign({ foo: 'bar', iat: Math.floor(Date.now() / 1000) - 30 }, 'shhhhh');
 
// sign with RSA SHA256
var cert = fs.readFileSync('private.key');  // get private key
var token = JWT.sign({ foo: 'bar' }, cert, { algorithm: 'RS256'});
 
// sign asynchronously
JWT.sign({ foo: 'bar' }, cert, { algorithm: 'RS256' }, function(err, token) {
  console.log(token);
});
```

### fetch

* Supported version - **"node-fetch":"^1.6.1"**. See [node-fetch npm package](https://www.npmjs.com/package/node-fetch), for more information.
* Used in API calls to fetch responses from a request.
* The following is an example to use fetch the response from API call:

```javascript
RequestF: function() {
 let body = "xml in the form of string";
 return fetch(API URL, {
 method: 'POST',
 headers: {
 "authorization": "Basic",
 "content-type": "application/xml",
 "cache-control": "no-cache",
 "username": "api username",
 "password": "api_pwd"
 },
 body: body
 }).then((res) => res.text()).then((xml) => {
 //parsing the XML for results
 let xmlDoc = new DOMParser().parseFromString(xml, 'text/xml');
 let documentElement = xmlDoc.documentElement;
 }
 });
 },
```

{% hint style="info" %}
**Note**: When you use the nodeJS fetch library and do not specify the user-agent, a default value is sent in the fetch call. This may not work based on the client API security policy. You can overwrite the default user-agent with any customized string that the client API accepts.
{% endhint %}

### lodash

* Supported version - **"lodash":"^4.14.1**"**.** See [lodash npm package](https://www.npmjs.com/package/lodash/v/4.14.1), for more information
* JS helper library for arrays, strings, and objects.
* The following is an example to use **\_.first()** and **\_.last()** in **lodash** function:

```javascript
var words = ['sky', 'wood', 'forest', 'falcon', 
    'pear', 'ocean', 'universe'];

let fel = _.first(words);
let lel = _.last(words);

console.log(`First element: ${fel}`);
console.log(`Last element: ${lel}`);
```

### moment

* Supported version - **"moment":"^2.20.1".** See [Moment npm package](https://momentjs.com/docs/), for more information
* Used for date and time operations.
* The following is an example to use **moment** function:

```javascript
moment("2010-10-20 4:30", "YYYY-MM-DD HH:mm"); 
```

### Promise

* Supported version - **"promise":"^7.1.1".** See [Promise npm package](https://www.npmjs.com/package/promise/v/7.1.1), for more information
* Used in asynchronous calls to indicate the completion of the processing carried out by the asynchronous function.
* The following is an example to use **promise** function:

```javascript
var promise = new Promise(function (resolve, reject) {
  fetch('http://www.google.com', function (err, res) {
    if (err) reject(err);
    else resolve(res);
  });
})
```

### Soap

* Supported version - **"soap":"^0.17.0".** See [SOAP npm package](https://www.npmjs.com/package/soap/v/0.17.0), for more information
* Used for making SOAP calls to an external source.&#x20;
* The following example demonstrates how to use **uuid** for generating unique identifiers:

**Example:**  The following is an example to create a new SOAP client from a WSDL URL:

```javascript
var url = 'http://example.com/wsdl?wsdl';
  var args = {name: 'value'};
  soap.createClient(url, function(err, client) {
      client.MyFunction(args, function(err, result) {
          console.log(result);
      });
  });
```

### uuid

* Supported version - **"uuid":"^2.0.2".** See [uuid npm package](https://www.npmjs.com/package/uuid/v/2.0.2), for more information
* Used for generating a unique identifier.
* The following is an example to use **uuid** for generating unique identifiers:

```javascript
// Generate a v1 (time-based) id
uuid.v1(); // -> '6c84fb90-12c4-11e1-840d-7b25c5ee775a'
 
// Generate a v4 (random) id
uuid.v4(); // -> '110ec58a-a0f2-4ac4-8393-c866d813b8d1'
```

### xmldom

* Supported version - **"xmldom":"^0.1.22".** See [XMLDOM npm package](https://www.npmjs.com/package/xmldom/v/0.1.22), for more information.
* Typically, used to parse XML response returned from API call.
* The following is an example demonstrates to use **xmldom** for parsing response received from SOAP call:

```javascript
// Response after SOAP call
let summaryDataResponse = apiRequests.dataService(params); 

if (summaryDataResponse !== errorMessage) {
    let DOMParser = xmldom.DOMParser;
    let doc = new DOMParser().parseFromString(summaryDataResponse, 'text/xml');
    .....//You can further parse as required.
```

### form-data

* Supported version - **"form-data":"^3.0.0".** See [form-data npm package](https://www.npmjs.com/package/form-data), for more information.
* A library to create readable `"multipart/form-data"` streams. Can be used to submit forms and file uploads to other web applications.
* The following is an example that demonstrates to use **form-data** for constructing a form with 3 fields that contain a string, a buffer, and a file stream and to use in use https-response stream

```javascript
var form = new FormData();
 
https.request('http://nodejs.org/images/logo.png', function(response) {
  form.append('my_field', 'my value');
  form.append('my_buffer', new Buffer(10));
  form.append('my_logo', response);
});
```
