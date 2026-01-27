# Source: https://clickwrap-developer.ironcladapp.com/docs/tracking-acceptance-via-pactsafe-api.md

# Sending Acceptance via Activity API

## Sending Acceptance via the Activity API

### Query Parameter Definitions

The following are definitions for various query parameters seen in the example API calls below:

* `sid` - Site Access ID. An ID that’s unique for each Site within your account. Information on finding your sid can be found in the [Authentication](https://clickwrap-developer.ironcladapp.com/docs/authentication-2) section.
* `sig` - Signer ID. The unique identifier used to save your signer’s signature. Can be email, mobile number, UUID, or any integer. Should be URL encoded.
* `gid` - Group ID. The ID of the Group associated with the acceptance event.
* `cid` - Contract IDs. A set of comma-separated values to specify which contracts a signer is accepting or confirming acceptance of.
* `vid` - Version IDs. **Note NOT an integer, this is a UUID string found in the version details of a contract**. A set of comma-separated values to specify which versions of which contracts a signer is accepting. Comma-separated values must correspond to Contract ID values.
* `et` - Event Type. The type of event being logged. Default values are displayed, updated, agreed, visited, sent, and disagreed.
* `slo` - Snapshot Location. The location key for the Snapshot Location that should be linked to this acceptance.
* `server_side` - Server-side Sending. When sending Acceptance to the Activity API server-side, we recommend setting this to true so that it returns a JSON response rather than a 1x1 pixel image.

> 📘 Required Parameters
>
> Please ensure your `/send` calls are always at a minimum sending the `sid`, `sig`, `vid`, and `et` parameters.

Additional details that we typically capture by default and outlined as recommended can be found on our [Possible URL Parameters to Track](https://clickwrap-developer.ironcladapp.com/reference/url-parameters-for-send) page.

### Example: Send Acceptance of Two Contracts for a Signer

Send a signer acceptance event for one or more contracts using the [Send Agreed](https://clickwrap-developer.ironcladapp.com/reference/send-contracts-signedaccepted-by-signer) API call. This call allows you to send an event for one or more contracts for a signer with the option to include a Group ID `gid` for relation to a specific group.

> 🚧 Example Only Code
>
> Please note that the example code is only for demonstration purposes and may not work in all environments.

```javascript
/**
  * For example purposes only.
  * Uses the Fetch API, which is not compatible with all browsers.
  * Learn more here: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
  */

// Example: Send as URL Params
fetch('https://pactsafe.io/send?sid=SITE_ACCESS_ID&sig=ENCODED_SIGNER_ID&vid=abc123&et=agreed&tm=true&server_side=true')
  .then(response => console.log(response.status)) // should return 200
  .catch(err => console.log(err));


// Example: Send within Request Body
const acceptanceBody = {
  sid: "my-site-access-id",
  sig: "myUrlEncodedSignerId",
  vid: "versionIdOne,versionIdTwo",
  et: "agreed",
  tm: true,
  server_side: true
};

fetch("https://pactsafe.io/send", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(acceptanceBody),
})
  .then((response) => {
    console.log(response.status); // Should return 200
  })
  .catch((err) => {
    // Handle errors
    console.log(err);
  });
```