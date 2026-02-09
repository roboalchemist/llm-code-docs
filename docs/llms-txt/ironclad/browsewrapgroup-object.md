# Source: https://clickwrap-developer.ironcladapp.com/docs/browsewrapgroup-object.md

# BrowsewrapGroup Object

This reference documents the properties and methods available on the BrowsewrapGroup object.

# Properties

## BrowsewrapGroup.parameters `ParameterStore`

A DataObject used by a BrowsewrapGroup to store its properties and `parameters`. During initialization, the parameters object is populated with all of the Group's configuration and display options, as well as the latest id of each contract and version that are a part of the Group.

## BrowsewrapGroup.rendered `Boolean`

A boolean flag indicating if the render() method has been executed successfully, injecting the Group's HTML content into the page.

## BrowsewrapGroup.eventsAttached `Boolean`

A boolean flag indicating if the `setupEvents()` method has been executed successfully, attaching all of the event listeners used to update the badge's position. If the `removeEvents()` method is executed, this property will be set back to false.

# Methods

## get

Returns the value of a parameter or property stored on the Group.

```javascript
group.get(parameter);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|---|---|---|------------------|
|`parameter`|True|String|The name of the parameter to return.|

### Returns

|||
|----|----|
|`String, Number, Boolean, Object, etc.`|The value of the parameter or property, or undefined if the parameter isn't set.|

### Examples

```javascript
// Returns the "key" property.
var val = group.get('key');  // 'legal-badge'
```

```javascript
// Returns the "contracts" parameter, which contains
// the id of each contract included in this Group.
var contracts = group.get('contracts');  // [ 10, 14 ]
```

## set

Sets the value of one or more parameters on the Group. Accepts either a single parameter name and value, or an object of multiple parameter name and value pairs to set.

**Note**: This method only applies to parameters. All properties must be set when the BrowsewrapGroup object is created.

```javascript
group.set(parameter, value);
```

```javascript
group.set(parameters);
```

### Arguments

|\_|NAME|REQUIRED|TYPE|DESCRIPTION|
|---|---|---|---|------------------|
|Option 1|`parameter`|True|String|The name of the parameter to set.|
||`value`|True|String, Number, Object, Function, etc.|The value of the parameter to set.|
|Option 2|`parameters`|True|Object|An object containing one or more parameter name and value pairs to set.|

### Returns

No Return Value

### Examples

```javascript
// Sets the "position" parameter.
group.set('position', 'right');
```

```javascript
// Sets the "position" to "center", and
// makes the badge visible at all times.
group.set({ position: "center", always_visible: true });
```

## send

Invokes a `send` command on the Site, with the `contracts`, `versions` and `group` parameters automatically populated with the Group's values.

```javascript
group.send(event_type, [parameters]);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|---|---|---|------------------|
|`event_type`|True|String|The type of the action being sent. Supported values include: `'agreed'`, `'disagreed'`, `'displayed'`, `'visited'` and `'updated'`.|
|`parameters`|Conditional|Object|A single object containing parameter name and value pairs to use for this send only. The `contracts`, `versions` and `group` parameters are included by default.|

### Returns

No Return Value

### Examples

```javascript
// Sends a "visited" action for the Group.
group.send('visited');

// Automatically adds the Group's parameters to the command:
// {
//   contracts: [ 10, 14 ],
//   versions: [ '5589bf606e7b9c1b1deef447', '5589bf606e7b9c1b1deef450' ],
//   group: 32
// }
```

## render

Injects the badge HTML into the page and runs `setupEvents()`.

```javascript
group.render([force]);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|---|---|---|------------------|
|`force`|False|Boolean|If true, the Group will be forced to re-render.|

### Returns

No Return Value

### Examples

```javascript
// Renders the browsewrap badge on the page.
group.render();
```

## openLegalCenter

Opens the Group's Legal Center page in a new tab. The URL is stored in the `legal_center_url` parameter.

```javascript
group.openLegalCenter();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Opens the Group's Legal Center page.
group.openLegalCenter();
```

## setupEvents

Attaches the `badge_updater` function to multiple events on the window object, including `'load'`, `'scroll'` and `'resize'`. This function is responsible for updating the badge's position on the page.

**Note**: This method will only run if the Group's `eventsAttached` property is `false`.

```javascript
group.setupEvents();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Attaches badge_updater function to 'load', 'scroll' and 'resize' events.
group.setupEvents();
```

## removeEvents

Clears all of the event listeners that were attached by `setupEvents()`.

**Note**: This method will only run if the Group's `eventsAttached` property is `true`.

```javascript
group.removeEvents();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Clears the 'load', 'scroll' and 'resize'
// listeners from the window object.
group.removeEvents();
```

## forceUpdate

Forces the badge to update its position using the `badge_updater` function. This method can be used as an alternative to the event listeners.

```javascript
group.forceUpdate();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Forces the badge to update its position.
group.forceUpdate();
```