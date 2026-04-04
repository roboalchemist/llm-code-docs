# Source: https://clickwrap-developer.ironcladapp.com/docs/how-to-get-a-download-url-for-a-pdf-record-after-acceptance.md

# Get Acceptance Record Download URL

# Overview

After your Signer accepts your agreements, you may want to provide them with a link to a copy of the agreement. This can be helpful for allowing the user to immediately review the signed copy or for when your workflow is customized.

# Requirements

To get started, you'll need to have the following:

* Ironclad Clickwrap Site Access ID. More info on the [Authentication](https://developer.pactsafe.com/docs/authentication-2) page
* A Clickwrap set up and ready to go (refer to [Loading a Clickwrap 101](https://developer.pactsafe.com/docs/loading-a-clickwrap-101) if you haven’t gotten this far)

# Retrieving the URL

The most simple way of retrieving the URL is by listening for when the `download_url` parameter has been set from the JavaScript library.

## Considerations

There are two things to consider when using this method.

1. This parameter may be set more than once. For example, the parameter may be set once the `signer_id` has been set on the group. Once acceptance has been sent (you can monitor via the valid event), the URL provided should allow direct access to the completed agreement.
2. When manually sending acceptance using the JavaScript Library, you may be better off utilizing the `.get('download_url')` method on the Site object once you know acceptance has been sent.

## Example Code

> 🚧 Example Only Code
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

```javascript
// Within your Ironclad Clickwrap related code, add a listener for the parameter being set
_ps.on('set:download_url', function(downloadUrl, siteContext) {
  console.log('My download URL: ' + downloadUrl);
});
```

# Full Example Code

> 🚧 Example Only Code
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

```javascript
var siteId = '790d7014-9806-4acc-8b8a-30c4987f3a95';

// The Ironclad Clickwrap Group key for a published group.
var groupKey = 'example-web-group';

// The element's ID where we want the clickwrap to show.
var clickwrapElementid = 'contracts-container';

// The input field's ID that will be used to pass as the signer id.
var signerIdElementId = 'formEmailAddress';

// Create the Ironclad Clickwrap site.
_ps('create', siteId, {
  test_mode: true, // Allows you to clear test data from Ironclad Clickwrap.
});

// Optionally, turn on debugging.
_ps.debug = false;

/**
  * Load the Ironclad Clickwrap group with the specific Group Key
  * and any additional options.
  */
_ps('load', groupKey, {
  container_selector: clickwrapElementid,
  display_all: true,
  signer_id_selector: signerIdElementId
});

// As we're developing, we want to know if there's an alert!
_ps.on('error', function(message, event_type, context) {
  alert(message);
});

// The download URL value is the first parameter within the callback
_ps.on('set:download_url', function(downloadUrl, siteContext) {
  console.log('My download URL: ' + downloadUrl);
});

// Triggered once the contracts have been accepted.
_ps.on('valid', function(params, groupContext) {
  // Enable submit button once contracts have been accepted
  var submitButton = document.getElementById('submitButton');
  if (submitButton) submitButton.disabled = false;
});
```