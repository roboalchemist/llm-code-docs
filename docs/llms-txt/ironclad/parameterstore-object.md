# Source: https://clickwrap-developer.ironcladapp.com/docs/parameterstore-object.md

# ParameterStore Object

This reference documents the properties and methods available on the ParameterStore object.

# Properties

## ParameterStore.data `DataObject`

A DataObject used to store a set of parameters and their corresponding values.

# Methods

## get

Returns the value of a parameter using the `getter` function defined by the parameter definition.

```javascript
parameters.get(parameter);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`parameter`|True|String|The name of the parameter to return.|

### Returns

|||
|----|--------|
|`String, Number, Boolean, Object, etc.`|The value of the parameter or property, or undefined if the parameter isn't set.|

### Examples

```javascript
// Returns the "signer_id" parameter.
var val = parameters.get('signer_id');  // 'john@ironcladhq.com'
```

## set

Sets the value of one or more parameters, using the `setter` function defined by the parameter definition. Accepts either a single parameter name and value, or an object of multiple parameter name and value pairs to set.

```javascript
parameters.set(parameter, value, override);
```

```javascript
parameters.set(parameters, override);
```

### Arguments

|\_|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|----|--------|
|Option 1|`parameter`|True|String|The name of the parameter to set.|
||`value`|True|String, Number, Object, Function, etc.|The value of the parameter to set.|
|Option 2|`parameters`|True|Object|An object containing one or more parameter name and value pairs to set.|
||`override`|False|Boolean|A flag indicating if the parameters should be set as temporary override values.|

### Returns

No Return Value

### Examples

```javascript
// Sets the "signer_id" parameter.
parameters.set('signer_id', 'john@ironcladhq.com', false);
// Sets the "contracts" parameter as an override value.
parameters.set('contracts', [ 10, 14 ], true);
```