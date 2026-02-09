# Source: https://clickwrap-developer.ironcladapp.com/docs/groupstore-object.md

# GroupStore Object

This reference documents the properties and methods available on the GroupStore object.

# Properties

## GroupStore.loaded `DataObject`

A DataObject used to store details about the `load` command.

## GroupStore.initialized `DataObject`

A DataObject used to store the initialized Group object.

# Methods

## get

Returns a Group object by key from the `initialized` property.

```javascript
groups.get(key);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`key`|True|String|The key of the Group to return.|

### Returns

|||
|----|----|
|`GroupObject`|The initialized Group object.|

### Examples

```javascript
// Returns a Group with the key "login-contracts".
var group = groups.get('login-contracts');
```

## add

Initializes a new Group object and stores the object in the `initialized` property.

```javascript
groups.add(site, key, type, options, callback);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`site`|True|Site|The Site object that the Group belongs to.|
|`key`|True|String|The unique key of the Group.|
|`type`|True|String|The type of Group object to initialize, `'group'` or `'badge'`, or a constructor function.|
|`options`|True|Object|The configuration options and parameters to set on the Group object.|
|`callback`|False|Function|A callback function to execute once the Group has been initialized. The function receives two arguments: `error` and `group`.|

### Returns

No Return Value

### Examples

```javascript
// Initializes a ClickwrapGroup with the key "login-contracts".
groups.add(site, 'login-contracts', 'group', config, function(err, group) {
  if (err) console.error(err);
  else console.log('Group ' + group.get('key') + ' initialized.');
});
```

## getLoading

Returns the value stored in the `loaded` property for the given key.

```javascript
groups.getLoading(key);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`key`|True|String|The key of the Group to return.|

### Returns

|||
|----|--------|
|`String, Boolean, Object`|The value stored in the `loaded` property.|

### Examples

```javascript
// Returns the details about the load command for "login-contracts".
var val = groups.getLoading('login-contracts');  // 'true'
```

## setLoading

Sets the value for a given key on the `loaded` property.

```javascript
groups.setLoading(key, value);
```

### Arguments

|NAME|REQUIRED|TYPE|DESCRIPTION|
|----|----|----|--------|
|`key`|True|String|The key of the Group to return.|
|`value`|True|String, Boolean, Object|Details about the `load` command.|

### Returns

No Return Value

### Examples

```javascript
// Sets the details about the load command for "login-contracts".
groups.setLoading('login-contracts', 'contracts-container');
```