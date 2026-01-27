# Source: https://clickwrap-developer.ironcladapp.com/docs/global_ps-object.md

# Global_ps Object

This reference documents the properties and methods available on the global \_ps object, and details on using the async queue.

# Properties

## \_ps.Sites `Object <String, Site>`

An object used internally by \_ps to store and reference all of the Site objects. Rather than accessing it directly, you should use one of the methods below, such as `getByName()` or `remove()`.

## \_ps.loaded `Boolean`

A boolean flag indicating if ps.js has finished loading and is ready to use.

# Methods

## create

Creates a new Site object.

```javascript
_ps.create(access_id, [name], [options]);
```

### Arguments

<HTMLBlock>
  {`
  <table style="width: 100%; border-collapse: collapse;">
  <thead>
  <tr>
    <th style="border: 1px solid #ddd; padding: 8px;">Name</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Required</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Type</th>
    <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>access_id</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>True</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>The unique access_id assigned to your Ironclad Clickwrap Site, which can be found on the <a href="https://beta.pactsafe.com/settings/site">Site Settings</a> page within Ironclad Clickwrap.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>name</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>False</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>String</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>A name to assign to the Site object. This property is optional for the initial Site, and will default to &#39;s0&#39;, but a name must be provided for any additional Sites.</p>
  </td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>options</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>False</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>Object</p>
  </td>
    <td style="border: 1px solid #ddd; padding: 8px;"><p>An object containing properties to set on the Site.</p>
  </td>
  </tr>
  </tbody>
  </table>
  `}
</HTMLBlock>

### Returns

|||
|----|-------|
|`Site`|The created Site object.|

### Examples

```javascript
// Creates a Site with the default configuration.
_ps.create('0207a846-d9bf-4b13-8430-1344e86ff7b1');
```

```javascript
// Creates a Site named "pactsafe".
_ps.create('0207a846-d9bf-4b13-8430-1344e86ff7b1', 'pactsafe');
```

```javascript
// Creates a Site named "pactsafe", enables localization
// and sets the signer_id to "john@pactsafe.com".
_ps.create('0207a846-d9bf-4b13-8430-1344e86ff7b1', 'pactsafe', {
    localized: true,
    signer_id: 'john@pactsafe.com'
});
```

```javasript
// Creates a Site with the default name and disables sending.
_ps.create('0207a846-d9bf-4b13-8430-1344e86ff7b1', null, {
  disable_sending: true
});
```

## remove

Removes a site Object by name.

```javascript
// The name of your Ironclad Clickwrap Site object.
const name = 'mySite';

_ps.remove(name);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------------|
|`name`|True|String|The name of the Site to remove.|

### Returns

No Return Value

### Examples

```javascript
// Removes the default Site.
_ps.remove('s0');
```

```javascript
// Removes a Site named "pactsafe".
_ps.remove('pactsafe');
```

## getByName

Returns a Site object by name.

```javascript
_ps.getByName(name);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------------|
|`name`|True|String|The name of the Site to return.|

### Returns

|||
|----|-------|
|`Site`|The Site object.|

### Examples

```javascript
// Returns a Site that was given the default name.
var site = _ps.getByName('s0');
```

## getAll

Returns all of the Site objects that have been created.

```javascript
_ps.getAll();
```

### Arguments

No Arguments

### Returns

|||
|----|-------|
|`Array<Site>`|An array containing all of the Site objects.|

### Examples

```javascript
// Returns all Sites that have been created.
var sites = _ps.getAll();
```

## getByKey

Returns a Group object by key.

```javascript
_ps.getByKey(key);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------------|
|`key`|True|String|The key of the Group to return.|

### Returns

|||
|----|-------|
|`BrowsewrapGroup` or `ClickwrapGroup`|The Group object.|

### Examples

```javascript
// Returns a Group with the key "login-contracts".
var group = _ps.getByKey('login-contracts');
```

## getAllGroups

Returns all of the Group objects that have been loaded.

```javascript
_ps.getAllGroups();
```

### Arguments

No Arguments

### Returns

|||
|----|-------|
|`Array<BrowsewrapGroup or ClickwrapGroup>`|An array containing all of the Group objects.|

### Examples

```javascript
// Returns all Groups that have been loaded in any Site.
var groups = _ps.getAllGroups();
```

# Event Methods

See the Events reference for a list of available events.

## on

Listens for an event to be triggered.

```javascript
_ps.on(event, callback);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------------|
|`event`|True|String|The name of the event to listen for.|
|`callback`|True|Function|The callback function to execute when the event is triggered. The arguments that are passed to the function vary between events.|

### Returns

No Return Value

### Examples

```javascript
// Listens for a Group to be initialized.
_ps.on('initialized', function(key, group) {
  console.log('Group ' + key + ' has been initialized.');
});
```

```javascript
// Toggles a form submit button when a Group
// is either validated or invalidated.
_ps.on('valid', function(parameters, group) {
  $('#submit-button').prop('disabled', false);
});
```

```javascript
_ps.on('invalid', function(parameters, group) {
  $('#submit-button').prop('disabled', true);
});
```

```javascript
// Logs all events to the browser's console.
_ps.on('all', function() {
  console.log(arguments);
});
```

## once

Listens for an event to be triggered once. The event listener is then removed.

```javascript
_ps.once(event, callback);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------------|
|`event`|True|String|The name of the event to listen for.|
|`callback`|True|Function|The callback function to execute once the event is triggered. The arguments that are passed to the function vary between events.|

### Returns

No Return Value

### Examples

```javascript
// Submits the form once the contracts have been accepted.
_ps.once('valid', function(parameters, group) {
  $('#login-form').submit();
});
```

## off

Removes an event listener.

```javascript
_ps.off([event], [callback]);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------------|
|`event`|False|String|The name of the event to remove the listener or listeners from. If blank, all event listeners will be removed from the \_ps object.|
|`callback`|False|Function|The callback function to remove. If blank, all listeners for the provided event will be removed from the \_ps object.|

### Returns

No Return Value

### Examples

```javascript
// Removes a logging handler that was attached to 'error' events.
_ps.off('error', logger);
```

```javascript
// Removes all 'sent' event listeners.
_ps.off('sent');
```

```javascript
// Removes all event listeners.
_ps.off();
```

# The Async Queue

## \_ps()

The async queue is created by the snippet and available for use even before ps.js has finished downloading. The \_ps object itself serves as the async command queue function.

Commands can be used to call any method on a Site or Group object asynchronously, forwarding all arguments directly to the method. The `ps()` function accepts a variety of command formats, which are detailed below.

```javascript
_ps([siteName.][groupKey:]method, [arg1, arg2, ..., argN]);
```

```javascript
_ps([siteName.][groupKey:]method, [parameters]);
```

```javascript
_ps(callback);
```

### Arguments

|---|NAME|REQUIRED|TYPE|DESCRIPTION|
|------|------|------|------|------------|
||`method`|True|String|The name of the method to invoke on a Site or Group object. To target methods on the default Site, just provide the name of the method. If you have multiple Sites, you will need to prepend the Site's name to the method, separated by a `.`. To target a Group method, prepend the Group's key, separated by a `:`.|
|Option 1|`arg1, arg2, ..., argN`|Conditional|Any|The in-line arguments to pass to the method.|
|Option 2|`parameters`|Conditional|Object|A single object containing parameter name and value pairs. This format is supported by set, send and retrieve commands.|
|Option 3|`callback`|True|Function|A callback function to execute. All commands in the queue are executed in order, so a callback function can be used to determine when the \_ps object is ready, or when the previous set of commands have been run.|

### Returns

No Return Value

### Examples

```javascript
// Creates a Site.
_ps('create', '0207a846-d9bf-4b13-8430-1344e86ff7b1');
```

```javascript
// Sends an "agreed" action from the default Site.
_ps('send', 'agreed', [ 10, 14 ], [ '5589bf606e7b9c1b1deef447', '5589bf606e7b9c1b1deef450' ], 33);
```

```javascript
// Sends an "agreed" action from a Site named "pactsafe".
_ps('pactsafe.send', 'agreed', [ 10, 14 ], [ '5589bf606e7b9c1b1deef447', '5589bf606e7b9c1b1deef450' ], 33);
```

```javascript
// Sends an "agreed" action with a parameters
// object and an event callback.
_ps('send', 'agreed', {
  contracts: [ 10, 14 ],
  versions: [ '5589bf606e7b9c1b1deef447', '5589bf606e7b9c1b1deef450' ],
  group: 33
  event_callback: function() {
    alert('Action sent.');
  }
});
```

```javascript
// Sets the "signer_id" parameter to "john@pactsafe.com".
_ps('set', 'signer_id', 'john@pactsafe.com');
```

```javascript
//Sets the properties of the signer
_ps('set', 'custom_data',
{
    first_name: "John",
    last_name: "Walker",
    company_name: "PactSafe",
    title: "Customer Support"
});
```

```javascript
// Loads a Group with the key "login-contracts".
_ps('load', 'login-contracts');
```

```javascript
//Loads a Group with the key "login-contracts" and passes in custom data for the Signer
_ps('load','login-contracts', {
            custom_data: {
                first_name: "John",
                last_name: "Walker",
                company_name: "PactSafe",
                title: "Customer Support"
            }
});
```

```javascript
// Sends an "agreed" action for a Group
// with the key "login-contracts".
_ps('login-contracts:send', 'agreed');
```

```javascript
// Adds a callback function to the queue.
_ps(function() {
  alert('All commands have been executed.');
});
```