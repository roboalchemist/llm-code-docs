# Source: https://clickwrap-developer.ironcladapp.com/docs/using-embedded-forms-in-groups.md

# Using Embedded Forms

Embedded forms give you the user experience of Ironclad Clickwrap's platform with the flexibility of our integration libraries. It's incredibly easy to add contract acceptance to your own application flows.

This article will touch on how to start integrating an Ironclad Clickwrap embedded form group on your page.

### What you'll learn

* What an embedded form is and does
* How to embed an Ironclad Clickwrap embedded form on your page
* What to do after an embedded form is accepted
* How to hide fields in an embedded form
* Where does the data go after a user clicks "I Agree"?

### What is an embedded form?

An embedded form is a group configuration that allows you to not only embed an agreement/contract on your page, but also the necessary form fields you need to populate it.

![](https://cl.ly/1o063U1Q2N1g/Image%202018-01-03%20at%2011.57.49%20PM.png)

### How to embed an embedded form on your page

First you'll need to [create a Clickwrap Group](https://app.pactsafe.com/groups) inside of Ironclad Clickwrap and add a **published** contract to that Group. Make sure "Embedded" is selected as the style/configuration for your Clickwrap before publishing the group.

You'll load an embedded form in exactly the same way you'd load a normal clickwrap or browsewrap group using the Javascript Library.

```html
<script>
_ps('load', 'embedded-test', { container_selector: "embedded-form" });
</script>
<div id="embedded-form"></div>
```

The Signer ID Selector is the ID of the page element where Ironclad Clickwrap will listen to in order to identify the person accepting the contracts. By default, the "Signer ID Selector" of an embedded form is `input-signer_id` (as defined by the form loaded on the page).

### What to do after an embedded form is accepted

Once the embedded form is accepted, Ironclad Clickwrap fires a `valid` event that you can attach a callback to like so:

```javascript
_ps.on('valid', function(){
  console.log(arguments);
  // DO SOMETHING
});
```

Here are some typical use cases that you'd use when embedding a Ironclad Clickwrap form:

* Redirecting to another page to complete a purchase or pay
* Hide the embedded form and show Stripe Checkout
* Send the user to a confirmation page

### How to hide fields in an embedded form

Sometimes, fields like email address may be populated by your own system so you'll want to hide it in the embedded form. Super easy to do—you'll need to do two things:

1. Hide the email field & label on the embedded form.
2. Set the `signer_id_selector` property on your group when you load it.

**Hiding the email field & label on the embedded form.** Through some simple JavaScript, you can hide any field in the Ironclad Clickwrap embedded form. Here's an example of hiding the email field & label:

```javascript
_ps.on('rendered', function(){
  document.getElementById( 'ps-inputs' ).getElementsByTagName( 'label' )[0].style.display = "none";
  document.getElementById( 'input-signer_id' ).style.display = "none";
});
```

**Setting the`signer_id_selector` property when you load.** When you load a group, you can easily overwrite the `signer_id_selector` to tell Ironclad Clickwrap what to listen to:

```html
<script>
_ps('load', 'embedded-test', { 
  container_selector: "embedded-form",
  signer_id_selector: "user-id"
});
</script>
<input id="user-id" type="hidden" value="1235324" name="user_id" />
<div id="embedded-form"></div>
```

### Where does the data go after the user clicks "I Agree"?

In real-time, when your user clicks "I Agree", a call is made to Ironclad Clickwrap asynchronously to capture that acceptance and store it. Inside of Ironclad Clickwrap, you'll automatically see all the versions accepted by your user in the Legal Profile:

![](https://cl.ly/253N1j2Z3b35/Image%202018-01-03%20at%2011.59.10%20PM.png)