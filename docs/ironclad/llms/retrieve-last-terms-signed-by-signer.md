# Source: https://clickwrap-developer.ironcladapp.com/docs/retrieve-last-terms-signed-by-signer.md

# Retrieve Last Contracts Signed by Signer

## Overview

The [Retrieve Contracts Accepted by Signer](https://clickwrap-developer.ironcladapp.com/reference/get-retrieve-contracts-by-signer-1) call allows you to query the API and pull back what a signer has previously agreed to. The response body will provide a list of Contract IDs and the Version ID accepted by the signer. This can be used to determine if a signer has signed the latest version of a contract.

## Example Code

> 🚧 Example Only Code
>
> Please note that the example code is only for demonstration purposes and may not work in all environments.

```javascript
/**
  * Uses the Fetch API, which is not compatible with all browsers.
  * Learn more here: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
  */

// Uses GET on /retrieve
fetch('https://pactsafe.io/retrieve?sid=SITE_ACCESS_ID&sig=ENCODED_SIGNER_ID')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    /*
      The data returned will be a JSON object with keys
      being the Contract ID and values being the Version ID.

    Example:
    {
      "1604": "5deea00c5d187b2830681313",
      "1618": "5df00251ef6fb9074d9264ec"
    }
    */
  })
  .catch(err => console.log(err));
```