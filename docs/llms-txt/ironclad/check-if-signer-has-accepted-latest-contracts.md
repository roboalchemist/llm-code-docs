# Source: https://clickwrap-developer.ironcladapp.com/docs/check-if-signer-has-accepted-latest-contracts.md

# Check if Signer Has Accepted Latest Contracts

## Overview

Occasionally, you may want to know if a Signer has accepted the latest set of Contract Versions within a Group, which is especially helpful when you need to ask them to accept the latest Versions. You'll typically use this route when using Groups as part of your acceptance workflow but this can also be used to check on a specific Contract.

To get started, you'll be using the [Retrieve Latest Versions](https://developer.pactsafe.com/reference/get-the-latest-versions-signed) route.

## Example Code

> 🚧 Example Only Code
>
> Please note that the example code is only for demonstration purposes and may not work in all environments.

```javascript
/**
  * For example purposes only.
  * Uses the Fetch API, which is not compatible with all browsers.
  * Learn more here: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
  */

// Uses GET on /latest
fetch('https://pactsafe.io/latest?sid=SITE_ACCESS_ID&sig=ENCODED_SIGNER_ID&gkey=A_GROUP_KEY')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    /*
      The data returned will be a JSON object with keys
      being the contract ID and values being the accepted status.

      Example:
      {
        "282": true,
        "1241": false
      }
    */
  })
  .catch(err => console.log(err));
```