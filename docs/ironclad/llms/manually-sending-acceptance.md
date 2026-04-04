# Source: https://clickwrap-developer.ironcladapp.com/docs/manually-sending-acceptance.md

# Manually Sending Acceptance

## Overview

The default behaviour for Embedded Clickwraps is to send acceptance as soon as the user checks the checkbox. When using our JavaScript Library, there may be some scenarios where you need to send acceptance manually rather than when the user checks the box since an acceptance event will be sent automatically by default.

## Example Scenarios

Some common use cases as to why you may need to send acceptance manually:

* You may want to confirm a form is fully validated before sending any data to Ironclad Clickwrap. This is especially true if you send additional data about the event (more on that later).
* You may want to ensure acceptance has been submitted successfully before allowing a form submission to occur.
* Your flow consists of multiple steps or is a multi-step form with the need for greater control.
* Your overall implementation might only use pieces of the Ironclad Clickwrap JavaScript Library or might be more custom.

## How to Use

When sending acceptance manually, there are two pieces to focus on: disabling default sending behavior upon load and enabling when you're ready to send acceptance. See below:

### Disable Automatic Sending

This part is crucial to ensuring the acceptance isn't automatically sent. You can adjust this setting when configuring the JavaScript snippet with the property `disable_sending`. The example below shows when creating and configuring your Clickwrap Site object.

```javascript
var siteAccessId = 'YOUR_SITE_ACCESS_ID';
_ps('create', siteAccessId, {
  disable_sending: true // Disable automatic sending with the JavaScript snippet.
});
```

### Enable Sending and Send Agreed

When you're ready to send acceptance to Ironclad Clickwrap, you can easily Send using the `_ps` function and your group key. The following example uses a callback to handle any additional logic like checking for an error when the sending happens or submitting a form.

```javascript
var groupKey = 'my-clickwrap-group-key';

// Manually send acceptance with the Clickwrap Group.
_ps(groupKey + ':send', 'agreed', {
  disable_sending: false, // We have to revert to allow sending with the snippet here.
  event_callback: function(err, eventType, group, request) {
    if (err) {
      // Something went wrong with sending the event.
      alert('Uh oh, something went wrong. Please try submitting again.'); // Alert the user
      return;
    }

    // Since we had no errors, go ahead and submit the form.
    form.submit();
  }
});
```

> 🚧 Example Only Code
>
> Please note that the example code is for demonstration purposes only. Your implementation will most likely be different than what is shown here.

### Full Example Code

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
      <h1>Ironclad Clickwrap Example with a Form</h1>
    
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
    
      <!-- By default, the submit button is disabled for validation with JavaScript -->
  	  <button id="formSubmitButton" type="submit" class="btn btn-primary" disabled>Submit</button>
      </form>
    </div>

    <!-- Optional JavaScript -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/js/bootstrap.bundle.min.js" integrity="sha512-kBFfSXuTKZcABVouRYGnUo35KKa1FBrYgwG4PAx7Z2Heroknm0ca2Fm2TosdrrI356EDHMW383S3ISrwKcVPUw==" crossorigin="anonymous"></script>
    
    <!-- Ironclad Clickwrap Implementation -->
    <script>
    // Minified Clickwrap Snippet
    (function(w,d,s,c,f,n,t,g,a,b,l){w['PactSafeObject']=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement('img');e.src='https://d3r8bdci515tjv.cloudfront.net/error.gif?t='+w[n].t+'&u='+encodeURIComponent(u);d.getElementsByTagName('body')[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&'function'==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,'script','https://vault.pactsafe.io/ps.min.js','https://d3l1mqnl5xpsuc.cloudfront.net/ps.min.js','_ps',4000);
  
    // We'll need a couple of things to get started from Clickwrap.
    var siteAccessId = '1e8ddd9d-f32c-4dc7-9c13-62095e6d4317'; // A Clickwrap Site Access ID
    var groupKey = "clickwrap-example"; // A Clickwrap Group Key.
  
    // Creates a Site object with the a Clickwrap Site Access ID.
    _ps('create', siteAccessId, {
      disable_sending: true, // Disable automatic sending with the JavaScript snippet.
      test_mode: true // Allows you to clear test data from the Ironclad Clickwrap web app.
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
  
    // If there's an error from the Clickwrap snippet,
    // you may want to prevent submission if needed.
    _ps.on('error', function(message, event_type, context) {
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
     * are valid.
     */
    _ps.on('valid', function(params, context) {
      console.log('Valid event fired!');
      if (simpleValidationFormValues()) {
        var submitButton = pageSubmitButton();
        if (submitButton) submitButton.disabled = false; // Only enable the submit button if found.
      }
    });
    
    // Check if values exist within the form fields.
    function simpleValidationFormValues() {
      var emailField = document.getElementById('exampleInputEmail1');
      var passwordField = document.getElementById('exampleInputPassword1');
      return (emailField !== "" && passwordField !== "");
    }
  
    // Return the form element in the page when called.
    function pageFormElement() {
      return document.getElementById('myPageForm');
    }
      
    // Return the submit button in the page when called.
    function pageSubmitButton() {
      return document.getElementById('formSubmitButton');
    }
  
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
      // Prevent the form from automatically submitting without checking Ironclad Clickwrap acceptance first.
      event.preventDefault();
      
      // Simple validation to ensure form fields have values.
      var formFieldsHaveValues = simpleValidationFormValues();
      if (!formFieldsHaveValues) {
        alert('Please ensure all fields are filled out!');
        return false;
      }
      
      // Check to ensure that the acceptance is still valid on the
      // Clickwrap group as a precaution.
      var shouldBlockSubmission = blockSubmission();
      if (shouldBlockSubmission) {
        // We can get the alert message if set on the group or define our own if it's not.
        var acceptanceAlertLanguage = (_ps.getByKey(groupKey) && _ps.getByKey(groupKey).get('alert_message')) ?  _ps.getByKey(groupKey).get('alert_message') :  'Please accept our Terms and Conditions.'
  
        alert(acceptanceAlertLanguage); // Alert the user that the Terms need to be accepted before continuing.
        return false; // Prevent submission
      }
      
      // We don't need to block the form submission at this point.
      // Manually send acceptance with the Clickwrap Group.
      _ps(groupKey + ':send', 'agreed', {
        disable_sending: false, // We have to revert to allow sending with the snippet here.
        event_callback: function(err, eventType, group, request) {
          if (err) {
            // Something went wrong with sending the agreed event.
            alert('Uh oh, something went wrong. Please try submitting again.'); // Alert the user
            return false; // Prevent form submission due to error.
          }
          
          // Since we had no errors, go ahead and submit the form.
          var form = pageFormElement();
          if (form) form.submit(); // Check we're able to retrieve the form.
          return true;
        }
      });
    }
  
    // We want to prevent the form submission
    // unless acceptance has gone through.
    function addFormAcceptanceValidation() {
      var form = pageFormElement(); // Get the form element.
      if (!form) return; // Return if no form is found in the page.
      
      // Add listener for form submissions.
      form.addEventListener('submit', function(event) {
        handleFormSubmit(event);
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