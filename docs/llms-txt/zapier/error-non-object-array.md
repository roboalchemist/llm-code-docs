# Source: https://docs.zapier.com/platform/build/error-non-object-array.md

# Error: Got a non-object result in the array, expected only objects

> When using a REST Hook trigger, the data returned by the perform must be an array.

## Error shown

If an API returns a non-object result within the array, or an array of arrays, the following error will show.

`Got a non-object result in the array, expected only objects ( )`

The non-object result will be wrapped in the parentheses for the error message.

## Solution

If the data included in the webhook needs to be transformed, or includes multiple objects, you can add custom code to parse the response data in `bundle.cleanedRequest` within the Perform into an array of objects.

If your webhook already provides an array, remove the wrapping array that Zapier includes by default and simply return `bundle.cleanedRequest`.

<Frame>
  {" "}

  <img src="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5b01893a07e0712d9a9c6b0bd88b09a5" data-og-width="1128" width="1128" data-og-height="257" height="257" data-path="images/26459a11e1630fe8318c341bf598ab5a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?w=280&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=326c133f6757328cfe1ef5ec673036db 280w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?w=560&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=707540f0962881ed328a378cc01a93ee 560w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?w=840&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=5515e4e50baf48ee6a9df3704843bbaf 840w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?w=1100&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=6022055aefa1ccabe4128fdbf8f28ae5 1100w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?w=1650&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=9b0ce179d1f9459cf6381d5aa74899fb 1650w, https://mintcdn.com/zapier-82f0e938/1jtyk4mqAs_J-p30/images/26459a11e1630fe8318c341bf598ab5a.webp?w=2500&fit=max&auto=format&n=1jtyk4mqAs_J-p30&q=85&s=89759ed54b0753698a001d66729ad853 2500w" />

  {" "}
</Frame>

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
