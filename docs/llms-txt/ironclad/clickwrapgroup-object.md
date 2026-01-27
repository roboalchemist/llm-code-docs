# Source: https://clickwrap-developer.ironcladapp.com/docs/clickwrapgroup-object.md

# ClickwrapGroup Object

This reference documents the properties and methods available on the ClickwrapGroup object.

# Properties

## ClickwrapGroup.parameters `ParameterStore`

A DataObject used by a ClickwrapGroup to store its properties and parameters. During initialization, the `parameters` object is populated with all of the Group's configuration and display options, as well as the latest id of each contract and version that are a part of the Group.

## ClickwrapGroup.agreed `ParameterStore`

A DataObject that stores which contracts in the Group have been accepted by the signer, either previously or during this session.

## ClickwrapGroup.checked `ParameterStore`

A DataObject that stores which contracts in the Group have had their checkbox manually checked by the signer.

## ClickwrapGroup.rendered `Boolean`

A boolean flag indicating if the `render()` method has been executed successfully, injecting the Group's HTML content into the page.

## ClickwrapGroup.inputInjected `Boolean`

A boolean flag indicating if the `<input type="hidden" name="__ps-contracts" class="__ps-contracts">` element has been injected into the form. The value of this input element specifies whether all contracts in the Group have been accepted.

## ClickwrapGroup.signerIdListening `Boolean`

A boolean flag indicating if the Group is listening for `'blur'` and `'change'` events on an input element, which contains the value for the `signer_id` parameter.

# Methods

## get

Returns the value of a parameter or property stored on the Group.

```javascript
group.get(parameter);
```

### Arguments

| NAME        | REQUIRED | TYPE   | DESCRIPTION                          |
| ----------- | -------- | ------ | ------------------------------------ |
| `parameter` | True     | String | The name of the parameter to return. |

### Returns

|                                         |                                                                                  |
| --------------------------------------- | -------------------------------------------------------------------------------- |
| `String, Number, Boolean, Object, etc.` | The value of the parameter or property, or undefined if the parameter isn't set. |

### Examples

```javascript
// Returns the "key" property.
var val = group.get('key');  // 'login-contracts'
```

```javascript
// Returns the "contracts" parameter, which contains
// the id of each contract included in this Group.
var contracts = group.get('contracts');  // [ 10, 14 ]
```

## set

Sets the value of one or more parameters on the Group. Accepts either a single parameter name and value, or an object of multiple parameter name and value pairs to set.

**Note**: This method only applies to *parameters*. All properties must be set when the ClickwrapGroup object is created.

```javascript
group.set(parameter, value);
```

```javascript
group.set(parameters);
```

### Arguments

| \_       | NAME         | REQUIRED | TYPE                                     | DESCRIPTION                                                             |
| -------- | ------------ | -------- | ---------------------------------------- | ----------------------------------------------------------------------- |
| Option 1 | `parameter`  | True     | String                                   | The name of the parameter to set.                                       |
|          | `value`      | True     | `String, Number, Object, Function, etc.` | The value of the parameter to set.                                      |
| Option 2 | `parameters` | True     | Object                                   | An object containing one or more parameter name and value pairs to set. |

### Returns

No Return Value

### Examples

```javascript
// Sets the "alert_message" parameter.
group.set('alert_message', 'Please accept all legal contracts.');
```

## getAgreed

Returns the Group's `contracts`, `versions` and `group` parameters, filtered for accepted contracts only.

```javascript
group.getAgreed();
```

### Arguments

No Arguments

### Returns

|          |                                                                                  |
| -------- | -------------------------------------------------------------------------------- |
| `Object` | An object containing the Group's `contracts`, `versions` and `group` parameters. |

### Examples

```javascript
// Returns "contracts", "versions" and "group".
var params = group.getAgreed();

// Only returns contracts that have been accepted:
// {
//   contracts: [ 10 ],
//   versions: [ '5589bf606e7b9c1b1deef447' ],
//   group: 33
// }
```

## getChecked

Returns the Group's `contracts`, `versions` and `group` parameters, filtered to include checked contracts only.

```javascript
group.getChecked(filter);
```

### Arguments

| NAME     | REQUIRED | TYPE    | DESCRIPTION                                                                    |
| -------- | -------- | ------- | ------------------------------------------------------------------------------ |
| `filter` | False    | Boolean | If `true`, only checked contracts that haven't been accepted will be returned. |

### Returns

|          |                                                                                  |
| -------- | -------------------------------------------------------------------------------- |
| `Object` | An object containing the Group's `contracts`, `versions` and `group` parameters. |

### Examples

```javascript
// Returns "contracts", "versions" and "group".
var params = group.getChecked();

// Only returns contracts that have been checked by the signer:
// {
//   contracts: [ 10 ],
//   versions: [ '5589bf606e7b9c1b1deef447' ],
//   group: 33
// }
```

## send

Invokes a `send` command on the Site, with the `contracts`, `versions` and `group` parameters automatically populated with the Group's values.

```javascript
group.send(event_type, [parameters]);
```

### Arguments

| NAME         | REQUIRED    | TYPE   | DESCRIPTION                                                                                                                                                      |
| ------------ | ----------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_type` | True        | String | The type of the action being sent. Supported values include: `'agreed'`, `'disagreed'`, `'displayed'`, `'visited'` and `'updated'`.                              |
| `parameters` | Conditional | Object | A single object containing parameter name and value pairs to use for this send only. The `contracts`, `versions` and `group` parameters are included by default. |

### Returns

No Return Value

### Examples

```javascript
// Sends an "agreed" action for the Group.
group.send('agreed');

// Automatically adds the Group's parameters to the command:
// {
//   contracts: [ 10, 14 ],
//   versions: [ '5589bf606e7b9c1b1deef447', '5589bf606e7b9c1b1deef450' ],
//   group: 33
// }
```

## sendChecked

Sends an `'agreed'` action for the Group's contracts that have been checked.

```javascript
group.sendChecked();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Sends an "agreed" action for the Group.
group.sendChecked();

// Automatically adds the Group's checked contracts to the command:
// {
//   contracts: [ 10 ],
//   versions: [ '5589bf606e7b9c1b1deef447' ],
//   group: 33
// }
```

## render

Injects the contract HTML into the page and sends a `retrieve` command if the `signer_id` parameter is set. Once rendered, either `display()` or `displayAll()` is called to show the contracts on the page.

```javascript
group.render([force]);
```

### Arguments

| NAME    | REQUIRED | TYPE    | DESCRIPTION                                     |
| ------- | -------- | ------- | ----------------------------------------------- |
| `force` | False    | Boolean | If true, the Group will be forced to re-render. |

### Returns

No Return Value

### Examples

```javascript
// Injects the Group's contract HTML into the DOM.
group.render();
```

## displayRequired

Displays only the contracts that haven't been accepted by the signer.

```javascript
group.displayRequired();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Displays the rendered contracts that need
// to be accepted by the signer.
group.displayRequired();
```

## displayAll

Displays all contracts in the Group, even those that have previously been accepted by the signer.

**Note**: To invoke this method after `render()`, set the Group's `display_all` property to true.

```javascript
group.displayAll();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Displays all of the rendered contracts.
group.displayAll();
```

## hide

Hides one or more contracts on the page.

```javascript
group.hide(contracts);
```

### Arguments

| NAME        | REQUIRED | TYPE          | DESCRIPTION                        |
| ----------- | -------- | ------------- | ---------------------------------- |
| `contracts` | True     | Array`<Number>` | The `id` of each contract to hide. |

### Returns

No Return Value

### Examples

```javascript
// Hides contracts 10 and 14 on the page.
group.hide([ 10, 14 ]);
```

## hideAll

Hides all contracts in the Group.

```javascript
group.hideAll();
```

### Arguments

No Arguments

### Returns

No Return Value

### Examples

```javascript
// Hides all of the Group's contracts on the page.
group.hideAll();
```

## allChecked

Returns a boolean flag indicating if all contracts in the Group have been checked.

**Note**: This only factors in the state of the HTML checkbox, and does not consider whether or not `'agreed'` actions have actually been sent to the Activity API.

```javascript
group.allChecked();
```

### Arguments

No Arguments

### Returns

|           |                                                            |
| --------- | ---------------------------------------------------------- |
| `Boolean` | A flag indicating if every contract's checkbox is checked. |

### Examples

```javascript
// Blocks form submission if any contracts are unchecked.
$('#submit-button').on('click', function(evt) {
  if (!group.allChecked()) {
    alert(group.get('alert_message'));
    return false;
  }
  else {
    group.send('agreed', {
      disable_sending: false,
      function(err) {
        if (err) handleError();
        else form.submit();
      }
    });
  }
});
```

## block

Returns a boolean flag indicating if any contracts in the Group still need to be accepted.

**Note**: If the Group's `display_all` property is set to `true`, this method will determine if every contract is both accepted *and* checked.

```javascript
group.block();
```

### Arguments

No Arguments

### Returns

|           |                                                                        |
| --------- | ---------------------------------------------------------------------- |
| `Boolean` | A flag indicating if at least one contract still needs to be accepted. |

### Examples

```javascript
// Blocks form submission if any contracts
// still need to be accepted.
$('#submit-button').on('click', function(evt) {
  if (group.block()) {
    alert(group.get('alert_message'));
    return false;
  }
  else form.submit();
});
```

## getPayload

Returns the URL-encoded payload that will be sent to [the Ironclad Clickwrap API](https://clickwrap-developer.ironcladapp.com/reference/send-contracts-signedaccepted-by-signer) upon acceptance, not including the `event_type`. This is especially useful to pass frontend details to the backend for server-side implementations.

**Note**: Even if the Group's `disable_sending` property is set to `true`, this method will return the payload that would be sent if automatic sending was allowed.

```javascript
group.getPayload();
```

### Arguments

No Arguments

### Returns

|          |                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------- |
| `String` | A URL-encoded payload including key metadata of the presented contract. Formatted for Ironclad's `/send` API endpoint. |

### Examples

```javascript
if(g = _ps.getByKey(groupKey)) {
  const payload = g.getPayload(); 
}
```