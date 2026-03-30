# Source: https://screenshotone.com/docs/code-examples/javascript-and-typescript-nodejs/

# JavaScript and TypeScript (Node.js) SDK and Code Examples

:::note
If you have any questions, please, reach out at `support@screenshotone.com`.
:::

### Installation

Run the next command to install the JavaScript and TypeScript Node.js SDK to take screenshots:

```shell
npm install screenshotone-api-sdk --save
```

### Usage

Don't forget to [sign up](https://dash.screenshotone.com/sign-up) to get access and secret keys.

:::danger
By default, the generated URL by SDK is not signed, and you can't share it,
because the API key will be leaked.

Use the method designated to generate a signed URL specifically—`generateSignedTakeURL()`.

Notice, in the recent versions of the SDK, all methods are asynchronous.
:::

Generate a screenshot URL without executing the request. Or download the screenshot. It is up to you:

```javascript
import * as fs from "fs";
import * as screenshotone from "screenshotone-api-sdk";

// create API client
const client = new screenshotone.Client("<access key>", "<secret key>");

// set up options
const options = screenshotone.TakeOptions.url("https://example.com")
    .delay(3)
    .blockAds(true);

// generate URL
const url = client.generateTakeURL(options); // or generateSignedTakeURL(options) for signed URLs
console.log(url);
// expected output: https://api.screenshotone.com/take?url=https%3A%2F%2Fexample.com&delay=3&block_ads=true&access_key=%3Caccess+key%3E

// or download the screenshot
const imageBlob = await client.take(options);
const buffer = Buffer.from(await imageBlob.arrayBuffer());
fs.writeFileSync("example.png", buffer);
// the screenshot is store in the example.png file
```

Check out [other SDKs and code examples](/docs/code-examples/).