# Source: https://clickwrap-developer.ironcladapp.com/docs/loading-a-clickwrap-101.md

# Loading a Clickwrap 101

## Overview

Below, we'll cover a few key topics to getting up and running with the Ironclad Clickwrap JavaScript Library.

## Requirements

To get started, you'll need to ensure that you have the following:

* Ironclad Clickwrap Site Access ID. More info in the [Authentication](https://clickwrap-developer.ironcladapp.com/docs/authentication-2) page.
* Group key from a **published** Ironclad Clickwrap Group that contains published Ironclad Clickwrap contracts.
* Development environment with SSL enabled

## Loading Your First Clickwrap

### Ironclad Clickwrap Snippet

Our JavaScript snippet was designed to load our external JavaScript library and give you an interface to interact with your code.

Load the snippet into your page, preferably in the `<head>` of the page.

```javascript
// Minified Clickwrap Snippet for Production Environment
(function(w,d,s,c,f,n,t,g,a,b,l){w["PactSafeObject"]=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement("img");e.src="https://d3r8bdci515tjv.cloudfront.net/error.gif?t="+w[n].t+"&u="+encodeURIComponent(u);d.getElementsByTagName("body")[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&"function"==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,"script","https://vault.pactsafe.io/ps.min.js","https://d3l1mqnl5xpsuc.cloudfront.net/ps.min.js","_ps",5000,function(){window.console&&console.error&&console.error("Unable to load Ironclad Clickwrap Library.")});
```

> 🚧 For Sandboxes and Trial Accounts on Demo Environment
>
> Use the snippet below for accounts on the Demo Environment. Accounts on the demo environment will have the following URL: [https://clickwrap.demo.pactsafe.com/](https://clickwrap.demo.pactsafe.com/).
>
> The snippet above is for production accounts using [https://clickwrap.pactsafe.com/](https://clickwrap.pactsafe.com/).

```javascript
// Minified Clickwrap Snippet for Demo Environment
(function(w,d,s,c,f,n,t,g,a,b,l){w["PactSafeObject"]=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement("img");e.src="https://d3r8bdci515tjv.cloudfront.net/error.gif?t="+w[n].t+"&u="+encodeURIComponent(u);d.getElementsByTagName("body")[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&"function"==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,"script","https://vault.demo.pactsafe.io/ps.min.js","https://d21iwaz8hush8a.cloudfront.net/ps.min.js","_ps",5000,function(){window.console&&console.error&&console.error("Unable to load Ironclad Clickwrap Library.")});
```

### Loading a Group

In order to get your clickwrap loaded into the page, we need to create the Ironclad Clickwrap Site object with a Clickwrap Site Access ID and then load the Clickwrap group using its group key. Follow along in the code below.

```javascript
// We'll need a couple of things to get started from Ironclad Clickwrap.
var siteAccessId = '1e8ddd9d-f32c-4dc7-9c13-62095e6d4317'; // A Clickwrap Site Access ID
var groupKey = "clickwrap-example"; // A Clickwrap Group Key.

// Creates a Site object with the a Clickwrap Site Access ID.
_ps('create', siteAccessId, {
    test_mode: true, // Allows you to clear test data from the Ironclad Clickwrap web app.
});

// Since we're testing, we can enable debugging
// which will log events to console. You'll want to
// set this to false in a production environment.
_ps.debug = true;

// Options set on the Clickwrap Group.
var groupOptions = {
  container_selector: 'clickwrapContainer', // HTML Element ID of where we want the clickwrap to load in the page.
  display_all: true, // Always display the contracts, even if previously signed by the Signer.
  signer_id_selector: 'exampleInputEmail1', // Uses the email input field value as the Signer ID and listen to the field.
}

// Load a Clickwrap group into the page.
_ps('load', groupKey, groupOptions);
```

## Clickwrap Acceptance

### Adding a Snapshot Location

A snapshot location allows you associate visual evidence (a screenshot) of how agreement was visually presented to your end users. Navigate to the Snapshots tab and create a Snapshot Location. Ensure that this location is published. Then, place the following code after the JS snippet and `_ps('load')`. Replace 'location-key' with your specific Snapshot Location key.

```javascript
_ps('set', 'snapshot_location', 'location-key');
```

### Sending Acceptance with Custom Data

By default, Ironclad Clickwrap will automatically send acceptance when the Group's checkbox is checked and when the signer ID selector (in this case an email address field) contains a value.

Alongside information about what contract version a user has signed, the Acceptance Activity Event will also include parameters such as Page Domain, Origin, Browser Timezone, etc. associated to the record. To associate additional information to the record, you can utilize our `Custom Data` feature.

```javascript
//Send custom data to Ironclad Clickwrap to associate with an Acceptance Record
_ps('set', 'custom_data',
{
    order_number: "17392",
    additional_information: "N/A"
});
```

Additionally, some of this information can be associated with the specific Signer record that is created for each unique user. Some out of the box parameters include Title and Company. Use this following example to update the Signer information.

```javascript
//Define custom_data to be associate with the Acceptance Record
_ps('set', 'custom_data',
{
    first_name: "John",
    last_name: "Walker",
    company_name: "Ironclad",
  	title: "CEO"
});
//Use that custom_data to update the Signer Record
_ps('send', 'updated');
```

### Verifying Acceptance

Pretty often, you'll want to ensure acceptance of the contracts within the group before proceeding. In order to do this, you can add validation that may look like the below.

> 🚧 Example Only Code
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

```javascript
// Get the form element on the page.
var pageFormElement = function() {
  return document.getElementById('myPageForm');
}

// Return whether to block the submission or not.
var blockSubmission = function() {
  // Check to ensure we're able to get the Group successfully.
  if (_ps.getByKey(groupKey)) {

    // Return if we should block the submission using the .block() method
    // provided by the Group object.
    return _ps.getByKey(groupKey).block();
  } else {
    // We weren't able to get the group,
    // so blocking form submission may be needed.
    return true;
  }
}

// We want to prevent the form submission
// unless acceptance has gone through.
function addFormAcceptanceValidation() {
  // Get the form element.
  var form = pageFormElement();

  // Return if no form is found in the page.
  if (!form) return;

  // Add listener for form submissions.
  form.addEventListener('submit', function(event) {
    // Prevent the form from automatically submitting without
    // checking Clickwrap acceptance first.
    event.preventDefault();

    if (!blockSubmission()) {
      // We don't need to block the form submission,
      // so submit the form.
      form.submit();
    } else {
      // We can get the alert message if set on the group
      // or define our own if it's not.
      var acceptanceAlertLanguage = (_ps.getByKey(groupKey) && _ps.getByKey(groupKey).get('alert_message')) ?  _ps.getByKey(groupKey).get('alert_message') :  'Please accept our Terms and Conditions.'

      // Alert the user that the Terms need to be accepted before continuing.
      alert(acceptanceAlertLanguage);
    }
  });
}

// Set up validation of Terms before allowing form submission.
if (document.readyState === 'loading') {  // Loading hasn't finished yet
  document.addEventListener('DOMContentLoaded', addFormAcceptanceValidation);
} else {  // `DOMContentLoaded` has already fired
  addFormAcceptanceValidation();
}
```

## Full Example Code

Below, you'll find the code to a full working example, which includes a sample form validation piece.

> 🚧 Example Only
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha512-MoRNloxbStBcD8z3M/2BmnT+rg4IsMxPkXaGh2zD6LGNNFE80W3onsAhRcMAMrSoyWL9xD7Ert0men7vR8LUZg==" crossorigin="anonymous" />

    <title>Simple Form!</title>
  </head>
  <body>
    <div class="container">
      <h1>Clickwrap Example with a Form</h1>

      <form id="myPageForm">
        <div class="form-group">
          <label for="exampleInputEmail1">Email address</label>
          <input type="email" class="form-control" id="exampleInputEmail1" />
        </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1" />
        </div>

        <!-- Note the div container here! -->
        <div id="clickwrapContainer"></div>

        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>

    <!-- Optional JavaScript -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/js/bootstrap.bundle.min.js" integrity="sha512-kBFfSXuTKZcABVouRYGnUo35KKa1FBrYgwG4PAx7Z2Heroknm0ca2Fm2TosdrrI356EDHMW383S3ISrwKcVPUw==" crossorigin="anonymous"></script>

    <!-- Ironclad Clickwrap Implementation -->
    <script>
      // Minified Clickwrap Snippet
      (function(w,d,s,c,f,n,t,g,a,b,l){w['PactSafeObject']=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement('img');e.src='https://d3r8bdci515tjv.cloudfront.net/error.gif?t='+w[n].t+'&u='+encodeURIComponent(u);d.getElementsByTagName('body')[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&'function'==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,'script','https://vault.pactsafe.io/ps.min.js','https://d3l1mqnl5xpsuc.cloudfront.net/ps.min.js','_ps',4000);

      // We'll need a couple of things to get started from Ironclad Clickwrap.
      var siteAccessId = '1e8ddd9d-f32c-4dc7-9c13-62095e6d4317'; // A Clickwrap Site Access ID
      var groupKey = "clickwrap-example"; // A Clickwrap Group Key.

      // Creates a Site object with the a Clickwrap Site Access ID.
      _ps('create', siteAccessId, {
          test_mode: true, // Allows you to clear test data from the Ironclad Clickwrap web app.
      });

      // Since we're testing, we can enable debugging
      // which will log events to console. You'll want to
      // set this to false in a production environment.
      _ps.debug = true;

      // Options set on the Clickwrap Group.
      var groupOptions = {
        container_selector: 'clickwrapContainer', // ID of where we want the clickwrap to load in the page.
        display_all: true, // Always display the contracts, even if previously signed by the Signer.
        signer_id_selector: 'exampleInputEmail1', // Uses the email input field value as the Signer ID and listen to the field.
      }

      // Load a Clickwrap group into the page.
      _ps('load', groupKey, groupOptions);
			
      // Load a Snapshot Location onto the page.
      _ps('set', 'snapshot_location', 'location-key');

      // If there's an error from the Clickwrap snippet,
      // you may want to prevent submission if needed.
      _ps.on('error', function(message, event_type, context) {
        // Handle any errors.
        console.log(arguments);
      });

      // Get the form element on the page.
      var pageFormElement = function() {
        return document.getElementById('myPageForm');
      }

      // Return whether to block the submission or not.
      function blockSubmission() {
        // Check to ensure we're able to get the Group successfully.
        if (_ps.getByKey(groupKey)) {

          // Return if we should block the submission using the .block() method
          // provided by the Group object.
          return _ps.getByKey(groupKey).block();
        } else {
          // We weren't able to get the group,
          // so blocking form submission may be needed.
          return true;
        }
      }

      // We want to prevent the form submission
      // unless acceptance has gone through.
      function addFormAcceptanceValidation() {
        // Get the form element.
        var form = pageFormElement();

        // Return if no form is found in the page.
        if (!form) return;

        // Add listener for form submissions.
        form.addEventListener('submit', function(event) {
          // Prevent the form from automatically submitting without
          // checking Clickwrap acceptance first.
          event.preventDefault();

          if (!blockSubmission()) {
            // We don't need to block the form submission,
            // so submit the form.
            form.submit();
          } else {
            // We can get the alert message if set on the group
            // or define our own if it's not.
            var acceptanceAlertLanguage = (_ps.getByKey(groupKey) && _ps.getByKey(groupKey).get('alert_message')) ?  _ps.getByKey(groupKey).get('alert_message') :  'Please accept our Terms and Conditions.'

            // Alert the user that the Terms need to be accepted before continuing.
            alert(acceptanceAlertLanguage);
          }
        });
      }

      // Set up validation of Terms before allowing form submission.
      if (document.readyState === 'loading') {  // Loading hasn't finished yet
        document.addEventListener('DOMContentLoaded', addFormAcceptanceValidation);
      } else {  // `DOMContentLoaded` has already fired
        addFormAcceptanceValidation();
      }
    </script>
  </body>
</html>
```