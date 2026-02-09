# Source: https://clickwrap-developer.ironcladapp.com/docs/using-psjs-with-back-end-api-calls.md

# Sending Clickwrap Data Server-side

You may want to use PS.js to render the contracts on the page, populate a contract with app data, and more—but send the API call on the back-end. Here's how to do it!

## Overview

In this article, we'll cover how you can use the JavaScript library in tandem with our API to send acceptance of a contract or contracts on the back-end. You'll learn how to:

* Load PS.js and render the contract on the page
* Set the Signer ID of the signer programmatically
* Disable sending when the checkbox on a click-through agreement is clicked
* Send the payload that *would* be sent automatically to your back-end.

## Requirements

In order to complete this article, you'll need the following already working:

* A published Contract that's been marked "Public" and added to a Group
* A published Group with a Group Key
* Working knowledge of JavaScript

## When to Use

By default, when you load an embedded contract onto a page, we'll automatically send acceptance of a contract as soon as your signer checks the box. Some people don't want to do this, so we've got a couple of different ways to handle sending acceptance. Below you can see our proposed flow for:

1. Loading PS.js and embedding the contracts into your page, which will dynamically grab the right contracts and versions and inject them into the page.
2. Send acceptance *after a user completes the form* using the [Activity API](https://clickwrap-developer.ironcladapp.com/docs/activity-api-docs).

<Image title="Image 2018-07-26 at 4.15.26 PM.png" alt={769} align="center" width="100%" src="https://files.readme.io/e7e700f-Image_2018-07-26_at_4.15.26_PM.png" />

## Load the Embedded Clickwrap

Load the Clickwrap with `disable_sending` set to `false`. See [here](https://clickwrap-developer.ironcladapp.com/docs/manually-sending-acceptance#disable-automatic-sending).

## Send Acceptance Server-side

Collect the payload using the Group's `getPayload()` method ([reference](https://clickwrap-developer.ironcladapp.com/docs/clickwrapgroup-object#getpayload)) and pass it to your backend. This ensures that the record in Ironclad matches exactly what the counterparty saw and accepted. You can then call [Ironclad's API](https://clickwrap-developer.ironcladapp.com/reference/send-contracts-signedaccepted-by-signer) directly from your sever to generate the record. See the example below.

> 🚧 Example Only Code
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

```javascript
// Grab the payload (encoded URL params) to be sent once accepted and ready.
const myPayload = _ps.site.getByKey('clickwrap-example').getPayload();

/// ...
// The Backend receives the data from a hidden input field or some other mechanism

// Let's pretend we are using a node server that received the payload.
const fetch = require('node-fetch');
(async (myPayload) => {
  const response = await fetch('https://pactsafe.io/send?et=agreed&server_side=true&addr=123.123.123.123&' + myPayload, {
    method: null,
    headers: {'Content-Type': 'application/json'}
  });
  const json = await response.json();
  console.log(json);
})();
```