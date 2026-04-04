# Source: https://clickwrap-developer.ironcladapp.com/docs/how-to-use-dynamic-contracts-with-the-javascript-library.md

# Dynamically Render Contract Data

## Overview

With the Ironclad Clickwrap JavaScript Library, you can inject data to dynamically swap the values of tokens within a Contract or multiple Contacts. This can significantly improve and reduce the number of templates your workflows may need.

## Requirements

* A published Group
* A published Contract with tokens

## Published Contract with Tokens

In this example, we'll use a contract that contains tokens to be populated using the JavaScript SDK.

For example, my contract looks like this:

```text
Contract with Tokens for Dynamic Rendering
First Name: {{first_name}}
Last Name: {{last_name}}

This contract contains a few tokens, which allows the contract to be dynamic and personalized to the recipient. For example, the following value: {{first_token}} - was populated before being presented. The best part about this? It can all be automated as part of your workflow! Another value populated with a token: {{second_token}}  . See—contracts can be fun.

Multiple Values Using Tokens
Below, you'll see an example of receiving multiple related values and presenting each one as they were passed as part of loading or showing the Group.
Separate Items Generated On-demand: {{#each additional_items}}
Item Name: {{this.item}}
Item Value: ${{this.itemValue}}
{{/each}}

Dynamic Content Section
Depending on whether we pass a token property name "shouldShow", we can render content within the contract dynamically.
{{#if shouldShow}}This is my content that should show when I pass a true value to "shouldShow".  Otherwise, this content is shown when "shouldShow" is not true.{{/if}}
```

## JavaScript Implementation

> 🚧 Example Code Only
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

### Add the Ironclad Clickwrap JavaScript Library and set up your Site and Group Objects.

```javascript
// Minified Clickwrap Snippet
(function(w,d,s,c,f,n,t,g,a,b,l){w['PactSafeObject']=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement('img');e.src='https://d3r8bdci515tjv.cloudfront.net/error.gif?t='+w[n].t+'&u='+encodeURIComponent(u);d.getElementsByTagName('body')[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&'function'==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,'script','https://vault.pactsafe.io/ps.min.js','https://d3l1mqnl5xpsuc.cloudfront.net/ps.min.js','_ps',4000);

// We'll need a couple of things to get started from Ironclad Clickwrap.
var siteAccessId = "1e8ddd9d-f32c-4dc7-9c13-62095e6d4317"; // A Clickwrap Site Access ID
var groupKey = "full-advanced-dynamic"; // A Clickwrap Group Key.

// Creates a Site object with the a Clickwrap Site Access ID.
_ps("create", siteAccessId, {
  dynamic: true, // Please ensure this is true when using dynamic contracts.
  test_mode: true, // Allows you to clear test data from the Ironclad Clickwrap web app.
});

// Since we're testing, we can enable debugging
// which will log events to console. You'll want to
// set this to false in a production environment.
_ps.debug = true;

// Options set on the CLickwrap Group.
var groupOptions = {
  container_selector: "clickwrapContainer", // ID of where we want the clickwrap to load in the page.
  display_all: false, // Prevents the group from showing the contract immediately.
  auto_run: false
};

// Load a Clickwrap group into the page
_ps("load", groupKey, groupOptions);
```

> 📘 Dynamic Property Needs to be True
>
> It's important to note that you need to set the `dynamic` property to `true` when creating the Site.

### Adding Clickwrap Triggered Events and Helpers

The following is to help to easily grab page elements for validation. Additionally, Ironclad Clickwrap triggered events are set up to handle acceptance, setting the signer id, and if the user unchecks the box.

```javascript
// Return the form element in the page when called.
function pageFormElement() {
  return document.getElementById("myPageForm");
}

// Return the show contract button when called.
function showContractButton() {
  return document.getElementById("showContractButton");
}

// Return the submit button in the page when called.
function pageSubmitButton() {
  return document.getElementById("formSubmitButton");
}

// Check if values exist within the form fields.
function simpleValidationFormValues() {
  var firstNameField = document.getElementById("firstNameInput1");
  var lastNameField = document.getElementById("lastNameInput1");
  return firstNameField !== "" && lastNameField !== "";
}

// Call when the group is ready and loaded.
_ps.on("initialized", function () {
  // Setting a fake unique ID as the signer id on the Site Object.
  var fakeUniqueId = Math.random().toString(36).substring(7);
  _ps.site.set("signer_id", fakeUniqueId);
});

// If there's an error from the Clickwrap snippet,
// you may want to prevent submission if needed.
_ps.on("error", function (message, event_type, context) {
  // Handle any errors.
  console.log(message);
});

/**
 * _ps.on('valid') gets triggered when all contracts within a group
 * have been accepted.
 *
 * Since the user has agreed, we can enable the submit button
 * if basic form validation also passes.
 *
 * Note: if more than one Clickwrap group exists on the page,
 * you'll want to add additional validation to ensure both groups
 * are valid if required.
 */
_ps.on("valid", function (params, context) {
  console.log("Valid event fired!");
  if (simpleValidationFormValues()) {
    var submitButton = pageSubmitButton();
    if (submitButton) submitButton.disabled = false; // Only enable the submit button if found.
  }
});

// Triggered when a user unchecks a checkbox in a Group.
_ps.on("invalid", function (params, context) {
  console.log("Invalid event fired!");
  // If a user has disagreed to a contract,
  // you may want to ensure the submit button is disabled.
  var submitButton = pageSubmitButton();
  if (!submitButton.disabled) submitButton.disabled = true;
});
```

### Setting Render Data

Here, we set render data with values populated by users on the page and data stored in the JavaScript itself. The important piece of getting the contract to retrieve the HTML is the `_ps(groupKey + ":retrieveHTML", renderData)` function which retrieves the HTML but populated with the data.

```javascript
/**
 * When we're ready to retrieve the populated contract,
 * we can set the render data on the Group Object and
 * then retrieve the HTML.
 * 
 * The Object keys are the token names inside the contract
 * and will be populated with the values we pass.
 */
function setRenderData() {
  var firstNameVal = document.getElementById("firstNameInput1").value;
  var lastNameVal = document.getElementById("lastNameInput1").value;

  // Render data that we want in the contract but doesn't require
  // a user to input.
  var staticRenderData = {
    first_token: "my first value",
    second_token: "my second value",
    shouldShow: true,
    additional_items: [
      {
        item: "My first item",
        itemValue: 0.99,
      },
      {
        item: "My second item",
        itemValue: 1.99,
      }
    ]
  };

  var renderData = {
    first_name: firstNameVal,
    last_name: lastNameVal,
    ...staticRenderData,
  };

  _ps(groupKey + ":retrieveHTML", renderData);
}

// Here, we'll listen for when the contract HTML is received
// before we display the contract.
_ps.on("set:contract_html", function (html, group) {
  // Retrieved was called from retrieving HTML.
  group.set('display_all', true);
  group.displayRequired();
});

// Return whether to block the submission or not.
function blockSubmission() {
  // Check to ensure we're able to get the Group successfully.
  if (_ps.getByKey(groupKey)) {
    // Return if we should block the submission using the .block() method.
    return _ps.getByKey(groupKey).block();
  } else {
    // We weren't able to get the group, so blocking form submission may be needed.
    return true;
  }
}

/**
 * Here, we add some basic form validation and then manually
 * send acceptance using the JavaScript snippet. We utilize a
 * callback to wait and ensure acceptance has been sent to Ironclad Clickwrap
 * before allowing the form to submit.
 */
function handleFormSubmit(event) {
  // Prevent the form from automatically submitting without checking Clickwrap acceptance first.
  event.preventDefault();

  // Simple validation to ensure form fields have values.
  var formFieldsHaveValues = simpleValidationFormValues();
  if (!formFieldsHaveValues) {
    alert("Please ensure all fields are filled out!");
    return false;
  }

  // Check to ensure that the acceptance is still valid on the
  // Clickwrap group as a precaution.
  var shouldBlockSubmission = blockSubmission();
  if (shouldBlockSubmission) {
    // We can get the alert message if set on the group or define our own if it's not.
    var acceptanceAlertLanguage =
      _ps.getByKey(groupKey) && _ps.getByKey(groupKey).get("alert_message")
        ? _ps.getByKey(groupKey).get("alert_message")
        : "Please accept our Terms and Conditions.";

    alert(acceptanceAlertLanguage); // Alert the user that the Terms need to be accepted before continuing.
    return false; // Prevent submission
  }

  // We don't need to block the form submission at this point.
  // Manually send acceptance with the Clickwrap Group.
  _ps(groupKey + ":send", "agreed", {
    disable_sending: false, // We have to revert to allow sending with the snippet here.
    event_callback: function (err, eventType, group, request) {
      if (err) {
        // Something went wrong with sending the agreed event.
        alert("Uh oh, something went wrong. Please try submitting again."); // Alert the user
        return false; // Prevent form submission due to error.
      }

      // Since we had no errors, go ahead and submit the form.
      var form = pageFormElement();
      if (form) form.submit(); // Check we're able to retrieve the form.
      return true;
    },
  });
}

// Handler for when the Show Contract button is clicked.
function handleShowContractButton() {
  var fieldsExist = simpleValidationFormValues();
  if (!fieldsExist) alert("Please fill out the required form fields!");
  setRenderData();
}

// We want to add listeners for validation and handling of render data.
function addListeners() {
  var form = pageFormElement(); // Get the form element.
  var showContractBtn = showContractButton();
  var lastNameInputField = document.getElementById("lastNameInput1");

  if (form) {
    // Add listener for form submissions.
    form.addEventListener("submit", function (event) {
      handleFormSubmit(event);
    });
  }

  if (showContractBtn) {
    // Handle when show contract button is clicked.
    showContractBtn.addEventListener("click", function () {
      handleShowContractButton();
    });
  }

  if (lastNameInputField) {
    // Allow show contract button if second input field changes
    // and has text in it.
    lastNameInputField.addEventListener("change", function () {
      if (lastNameInputField.val != "") showContractBtn.disabled = false;
    });
  }
}

// Set up validation of Terms before allowing form submission.
if (document.readyState === "loading") {
  // Loading hasn't finished yet
  document.addEventListener("DOMContentLoaded", addListeners);
} else {
  // `DOMContentLoaded` has already fired
  addListeners();
}
```