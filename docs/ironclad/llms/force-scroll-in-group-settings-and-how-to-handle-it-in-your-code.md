# Source: https://clickwrap-developer.ironcladapp.com/docs/force-scroll-in-group-settings-and-how-to-handle-it-in-your-code.md

# Using Force Scroll

Inside your [Group settings](https://app.pactsafe.com/groups), you may have noticed the option to "Force Scroll" for a signer. For the "Scroll" and "Embedded" style/layout options, this option will force the user to scroll to the bottom when reviewing a contract before the "I Agree" button or checkbox is enabled:

![](https://cl.ly/2y0f13240r1h/Screen%20Recording%202016-12-12%20at%2003.33%20PM.gif)

This Guide will walk you through what this means, when this will affect how contracts are accepted in your code, and how to handle.

## Things you need for this tutorial

* A published Group that has "Force Scroll" enabled and either "Scroll" or "Embedded" style/layout enabled.
* You need to be up to snuff on the JavaScript library and how it works. [Here's a great guide](https://developer.pactsafe.com/docs/loading-a-clickwrap-101).
* Working knowledge of [Triggered Events](https://developer.pactsafe.com/docs/triggered-events-1). There are two callbacks you can manipulate with this functionality (`_ps.on('scrolled:contract', function(){})` and `_ps.on('scrolled', function(){})`).

## Enabling the "Force Scroll" option in a Group

When enabling "Force Scroll" in a group, your user will need to follow instructions pretty well. In addition to the language provided as part of what is injected into the page by Ironclad Clickwrap, you may want to add an additional callout to just double check the user knows to scroll before being able to accept the contract.

## Special event callbacks

There are two special events/callbacks that are made that you'll want to note in case you want to intercept the scroll to execute some of your own code as part of "Force Scroll": `scrolled:contract` and `scrolled`. We'll explain what each of these do.

### \_ps.on('scrolled:contract')

There are two events you can tap into that will be triggered when "Force Scroll" is enabled on your Group. The first, `scrolled:contract` will fire for *each* contract that has reached the bottom:

```javascript
_ps.on('scrolled:contract', function(contractHTML, group){
  // you can output what is passed in this callback like so
  // this is called for EACH contract that the user reaches 
  // the bottom of...
  console.log(arguments);
  console.log("Bottom of a contract has been reached!");
});
```

`contractHTML` is the HTML of the contract which has been scrolled.

`group` is a ClickwrapGroup object. This object contains all the metadata about the group including contract IDs, version IDs, etc. Example usage: `group.get('versions');`

### \_ps.on('scrolled')

The second event that's fired is `scrolled` and will trigger when *all* contracts have been fully scrolled:

```javascript
_ps.on('scrolled', function(contractsElement, group){
  // you can output what is passed in this callback like so
  console.log(arguments);
  console.log("Every contract has been scrolled! Yewwww!");
});
```

`contractsElement` is the object for `container_selector` for the contracts set either in the Group settings or on the page using `_ps('load')`. Example usage: `contractsElement.innerHTML`

`group` is a ClickwrapGroup object. This object contains all the metadata about the group including contract IDs, version IDs, etc. Example usage: `group.get('versions');`

## Doing something custom once a user has scrolled

Let's run through an example to see how this functionality would look

An example that you might use to keep the user posted of their progress would be to upload a progress bar every time the user completes scrolling on an agreement. Then, when the user completes all the agreements we want to show a disabled "Submit" button. Once all agreements have been accepted, enable the submit button.

```javascript
// add jQuery to get this sample to work

var progressBar = function(addPercentage){
  // add a progress bar and update the progress here
}

// for each contract, update a progress bar 50%
_ps.on('scrolled:contract', function(contractsElement, group){
  updateProgressBar(50);
});

_ps.on('scrolled', function(contractsElement, group){
  $('#submit-btn').show();
  $('#submit-btn').prop('disabled', true);
});

_ps.on('valid', function(){
  // once all contracts in a group have been accepted, the
  // 'valid' event is triggered enabling the submit btn
  $('#submit-btn').prop('disabled', false);
});
```

And just like that, you're integrating scrolling magic into your code. Happy coding!