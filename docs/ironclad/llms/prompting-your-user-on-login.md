# Source: https://clickwrap-developer.ironcladapp.com/docs/prompting-your-user-on-login.md

# Checking Acceptance on Login

## Overview

As a company grows and adapts to changing regulatory landscapes, it must also update its agreements. Ensuring that users/customers have accepted the latest version of the terms becomes very important.

Ironclad Clickwrap makes it easy to check acceptance status and present your clickwrap to users that haven't accepted the latest agreements. Keep reading to find out how this works with the JavaScript Library and/or Activity API.

## Requirements

To get started, you'll need to ensure that you have the following:

* Ironclad Clickwrap Site Access ID. More info in the [Authentication](https://clickwrap-developer.ironcladapp.com/docs/authentication-2) page.
* Group Key from a **published** [Ironclad Clickwrap Group](https://support.ironcladapp.com/hc/en-us/articles/13622003789207-Create-and-Manage-Clickwrap-Groups) that contains published contract templates.

## Checking Acceptance Status

### Using the JavaScript Library

> 🚧 Required Settings
>
> The Clickwrap Group must have `display_all` set to false.

The Group setting `display_all` must be disabled. This can be [configured in the Ironclad Clickwrap web app](https://support.ironcladapp.com/hc/en-us/articles/13622003789207-Create-and-Manage-Clickwrap-Groups) or when loading the Group via the JavaScript Library.

<Image align="center" className="border" border={true} src="https://files.readme.io/e2b803a-Show_based_on_acceptance.png" />

Once loaded, the JavaScript Library will automatically listen for the `signer_id` attribute to be set (whether manually or via a specified `signer_id_selector` HTML element).

This `signer_id` is used to query whether the user has accepted the [latest major versions](https://support.ironcladapp.com/hc/en-us/articles/12448331891223-Versions-major-versus-minor-) of the contracts in the group. Any and all contracts in the group whose latest major version this user has not accepted will be displayed on the page.

As an illustration, your configuration may look something like this:

```javascript
// The Ironclad Clickwrap Site Access ID (located in your settings).
var siteId = '1e8ddd9d-f32c-4dc7-9c13-62095e6d4317';

// The Ironclad Clickwrap Group key for a published group.
var groupKey = 'clickwrap-example-combined';

// The element's ID where we want the clickwrap to show.
var clickwrapElementid = 'contracts-container';

// The input field's ID that will be used to pass as the signer id.
var signerIdElementId = 'formEmailAddress';

// Create the Ironclad Clickwrap site.
_ps('create', siteId, {
   test_mode: true, // Allows you to clear test data from Ironclad Clickwrap.
});

/**
 * Load the Ironclad Clickwrap group with the specific Group Key
 * and any additional options.
 */
_ps('load', groupKey, {
  container_selector: clickwrapElementid,
  display_all: false, // We don't want to display unless they haven't accepted.
  signer_id_selector: signerIdElementId // Listening for the Signer Id to be entered in a form element
});
```

### Using the Activity API

To check the acceptance status using the Activity API, you'll need to have:

* A Site Access ID (located in your Site settings)
* A Group Key (located when creating and configuring a Group)
* A Signer ID to check

The example below takes the following approach:

1. Listen to when a form is submitted and then handle using a function.
2. Upon form submission, a signer ID is collected and passed to a function that calls the Ironclad Clickwrap API [latest endpoint](https://clickwrap-developer.ironcladapp.com/reference/get-the-latest-versions-signed) at `https://pactsafe.io/latest` with the site access id, the group key, and the signer ID as URL params.
3. The response is then checked to see if any of the present Contract IDs have not been accepted. A `false` value indicates that the given signer has not yet accepted the latest published [major version](https://support.ironcladapp.com/hc/en-us/articles/12448331891223-Versions-major-versus-minor-) of the contract.

With the response, you can then send a user to another page to review/accept the contracts or whatever other behavior fits your use case best.

> 🚧 Example Only Code
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

```javascript
// The Ironclad Clickwrap Site Access ID (located in your settings).
var siteId = "1e8ddd9d-f32c-4dc7-9c13-62095e6d4317";

// The Ironclad Clickwrap Group key for a published group.
var groupKey = "clickwrap-example-combined";

// The input field's ID that will be used to pass as the signer id.
var signerIdElementId = "formEmailAddress";

var submitButton;

function checkPactSafeAPI(signerIdValue) {
  var url = 'https://pactsafe.io/latest?sid=' +
    siteId +
    '&gkey=' + groupKey +
    '&sig=' + signerIdValue;

  fetch(url)
    .then(response => response.json())
    .then(data => {
      /*
        The response may look like the following:
        {
          92928: false,
          92931: true
        }
        Knowing that a contract hasn't been accepted, we can then
        appropriately handle the next step, which may be
        sending the user to another page to accept the contract.
      */
    })
    .catch(err => {
      alert(err);
    })
}

function handleFormSubmission(event) {
  event.preventDefault();
  // Grab the current signer ID field (this case an email address).
  var signerIdField = document.getElementById(signerIdElementId);
  if (!signerIdField) return; // If you don't have a signer id field here, there may be a problem.

  var signerIdValue = signerIdField.value;
  // Only continue if the field has a value.
  if (signerIdValue) {
    checkPactSafeAPI(signerIdValue);
  }
}

function handleInputChange() {
  var emailAddressField = document.getElementById('formEmailAddress');
  var passwordField = document.getElementById('formPassword');
  if (!emailAddressField || !passwordField) submitButton.disabled = true;
  if (emailAddressField.value === "" || passwordField.value === "") submitButton.disabled = true;
  else submitButton.disabled = false;
}

// In this example, the DOM is ready. In your environment, you
// may need to listen for the DOM being ready.
var pageForm = document.getElementById('login-form');
if (pageForm) pageForm.addEventListener('submit', function(event) {
  handleFormSubmission(event);
}, true);

// Hold reference of submit button
submitButton = document.getElementById('submitButton');

// Add fields listeners
var emailAddressField = document.getElementById('formEmailAddress');
var passwordField = document.getElementById('formPassword');
if (emailAddressField) emailAddressField.addEventListener('input', function() {
  handleInputChange()
});
if (passwordField) passwordField.addEventListener('input', function() {
  handleInputChange()
});
```