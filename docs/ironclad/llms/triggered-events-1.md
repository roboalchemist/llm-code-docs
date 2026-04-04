# Source: https://clickwrap-developer.ironcladapp.com/docs/triggered-events-1.md

# Triggered Events

## Common use cases

Let's say you wanted to enable a button once a checkbox is checked:

````javascript
_ps.on('valid', function(){
  console.log(arguments);
  $('#button').prop('disabled', false);
});




## Real-time events to interact with your own app

This reference documents the events that are triggered on the global `_ps` object. Events are triggered based on interactions with the Ironclad Clickwrap JavaScript library. Examples include when a user clicks all checkboxes (`_ps.on('valid')`), when acceptance is sent to Ironclad Clickwrap (`_ps.on('sent')`), or when an error occurs (`_ps.on('error')`). These callbacks are used to manage interactions so that the experience of plugging Ironclad Clickwrap into your own apps does not disrupt your own flows.

# Events

## all

A special event that is triggered when any other event is triggered. The name of the original event is always the first argument passed to the callback function. The rest of the arguments will match whatever arguments were passed to the original event's callback function.

```javascript
_ps.on('all', callback);
````

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`event`|String|The name of the event that was triggered.|
|`[arguments]`|Any|All of the arguments that were passed to the original event.|

## ready

Triggered once ps.js has been loaded and the \_ps object is setup.

```javascript
_ps.on('ready', callback);
```

### Callback Arguments

No Arguments

## create

Triggered when a Site object is created.

```javascript
_ps.on('create', callback);

```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`context`|Site|The created Site object.|

## sent

Triggered when a `send` command has been completed successfully.

```javascript
_ps.on('sent', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`event_type`|String|The type of action that was sent. Supported values include: `'agreed'`, `'disagreed'`, `'displayed'`, `'visited'` and `'updated'`.|
|`parameters`|Object|An object containing the `contract` and `group` details that were sent. Contains three parameters: `'contracts'`, `'versions'` and `'group'`.|
|`context`|Site, BrowsewrapGroup or ClickwrapGroup|The Site or Group object that initiated the `send` command.|
|`payload`|String|The URL-encoded payload that would have been sent to the Action API. This argument is only present when the Site's disable\_sending property is set to true.|

## retrieved

Triggered when a `retrieve` command has been completed successfully.

```javascript
_ps.on('retrieved', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`responseJSON`|Object|The JSON response body returned by the XMLHttpRequest.|
|`xhr`|XMLHttpRequest|The raw XMLHttpRequest that was sent to the Action API.|
|`context`|Site, BrowsewrapGroup or ClickwrapGroup|The Site or Group object that initiated the `retrieve` command.|

## set

Triggered when a parameter is set.

**Note**: This event will only be triggered for specific parameters. Supported parameters include: `signer_id`, `signer_id_selector`, `form_selector`, `position` and `always_visible`.

```javascript
_ps.on('set', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`parameter`|String|The name of the parameter that was set.|
|`value`|String, Number, Object, Function, etc.|The value that was set.|
|`context`|Site, BrowsewrapGroup or ClickwrapGroup|The Site or Group object on which the parameter was set.|

## set:parameter

Triggered when the named parameter is set.

**Note**: This event will only be triggered for specific parameters. Supported parameters include: `signer_id`, `signer_id_selector`, `form_selector`, `position` and `always_visible`.

```javascript
_ps.on('set:[parameter]', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`value`|String, Number, Object, Function, etc.|The value that was set.|
|`context`|Site, BrowsewrapGroup or ClickwrapGroup|The Site or Group object on which the parameter was set.|

### Examples

```javascript
// Listens for the signer_id parameter to be set.
_ps.on('set:signer_id', function(value, context) {
  console.log(value);
});
```

## initialized

Triggered when a Group object is initialized and ready to use.

```javascript
_ps.on('initialized', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`key`|String|The unique key of the Group object.|
|`context`|BrowsewrapGroup or ClickwrapGroup|The initialized Group object.|

## rendered

Triggered when a Group object has been rendered.

```javascript
_ps.on('rendered', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`context`|BrowsewrapGroup or ClickwrapGroup|The Group object that was rendered.|

## displayed

Triggered when a Group object displays a contract.

```javascript
_ps.on('displayed', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`element`|HTMLElement|The contract's HTMLElement that was displayed.|
|`context`|BrowsewrapGroup or ClickwrapGroup|The Group object that displayed the contract.|

## hidden

Triggered when a Group object hides a contract.

```javascript
_ps.on('hidden', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`element`|HTMLElement|The contract's HTMLElement that was hidden.|
|`context`|BrowsewrapGroup or ClickwrapGroup|The Group object that hid the contract.|

## valid

Triggered when all of the contracts in a Group have been accepted by a signer.

**Note**: If a Group's `display_all` parameter is set to `true`, this event will only be triggered when all contracts have been accepted and checked.

```javascript
_ps.on('valid', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`parameters`|Object|An object containing the contracts and versions that belong to the Group. Contains three parameters: `'contracts'`, `'versions'` and `'group'`.|
|`context`|BrowsewrapGroup or ClickwrapGroup|The Group object that was validated.|

## invalid

Triggered when all of the contracts in a Group are no longer accepted by a signer. This event will be triggered if a signer un-checks a contract on a valid Group.

```javascript
_ps.on('invalid', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`parameters`|Object|An object containing the contracts and versions that belong to the Group. Contains three parameters: `'contracts'`, `'versions'` and `'group'`.|
|`context`|BrowsewrapGroup or ClickwrapGroup|The Group object that was invalidated.|

## scrolled:contract

Triggered when "Force Scroll" has been enabled in your Group Settings and one of the contracts in a Group has been scrolled to the bottom of a "Scroll" or "Embedded" Group style/layout.

```javascript
_ps.on('scrolled:contract', function(contractHTML, group){
  // you can output what is passed in this callback like so
  // this is called for EACH contract that the user reaches 
  // the bottom of...
  console.log(contractHTML);
  console.log(group);
  console.log(group.get("contracts"));
});
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`contractHTML`|Object|An object containing the HTML of the contract that has been scrolled to the bottom.|
|`group`|ClickwrapGroup|The Group object that contains the contract that was scrolled to the bottom.|

## scrolled

Triggered when "Force Scroll" has been enabled in your Group Settings and **all** of the contracts in a Group have been scrolled to the bottom of within a "Scroll" or "Embedded" Group style/layout.

```javascript
_ps.on('scrolled:contract', function(contractsElement, group){
  // you can output what is passed in this callback like so
  // this is called for EACH contract that the user reaches 
  // the bottom of...
  console.log(contractsElement);
  console.log(contractsElement.innerHTML);
  console.log(group);
  console.log(group.get("contracts"));
});
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`contractsElement`|Object|The element containing the entire container selector of the group.|
|`group`|ClickwrapGroup|The Group object that had all contracts scrolled to the bottom.|

## error

Triggered when a `send` or `retrieve` command encounters an error before being sent.

```javascript
_ps.on('error', callback);
```

### Callback Arguments

|NAME|TYPE|DESCRIPTION|
|----|----|--------|
|`message`|String|A message describing why the error occurred.|
|`event_type`|String|The type of action that was being sent.|
|`context`|Site, BrowsewrapGroup or ClickwrapGroup|The Site or Group object that initiated the command.|