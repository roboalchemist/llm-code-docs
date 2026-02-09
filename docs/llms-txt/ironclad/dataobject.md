# Source: https://clickwrap-developer.ironcladapp.com/docs/dataobject.md

# DataObject

This reference documents the properties and methods available on the DataObject.

# Properties

## DataObject.keys `Array<String>`

An array of all the parameter names stored in the object.

## DataObject.values `Object`

An object that holds the persistent name-value pairs stored in the object.

## DataObject.overrides `Object`

An object that holds the temporary name-value pairs stored in the object.

# Methods

## get

Returns the value stored in the object at the given parameter name.
data.get(parameter);

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`parameter`|True|String|The name of the parameter to return. If an override value exists, that value will be returned.|

### Returns

|||
|----|--------|
|`String, Number, Boolean, Object, etc.`|The value of the parameter or property, or `undefined` if the parameter isn't set.|

### Examples

```javascript
// Returns the "key" parameter.
var val = data.get('key');  // 'login-contracts'
```

## set

Sets the value of a parameter by name.

```javascript
data.set(parameter, value, override);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`parameter`|True|String|The name of the parameter to set.|
|`value`|True|String, Number, Object, Function, etc.|The value of the parameter to set.|
|`override`|False|Boolean|A flag indicating if the parameter should be set as a temporary override value. Defaults to `false`.|

### Returns

No Return Value

### Examples

```javascript
// Sets the "signer_id" parameter.
data.set('signer_id', 'john@ironcladhq.com', false);
```

```javascript
// Sets the "contracts" parameter as an override value.
data.set('contracts', [ 10, 14 ], true);
```

## map

Invokes a callback function for each name and value pair stored in the object.

```javascript
data.map(callback);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`callback`|True|Function|The callback function to execute for each name and value pair. The function receives two arguments: `name` and `value`.|

### Returns

No Return Value

### Examples

```javascript
// Logs each name and value pair to the console.
data.map(function(name, value) {
  console.log(name + ': ' + value);
});
```