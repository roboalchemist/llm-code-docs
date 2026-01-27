# Source: https://clickwrap-developer.ironcladapp.com/docs/actions.md

# Actions

This reference documents each type of Action available to be sent.

# Event Callback Function

## event\_callback

All `send` commands support an optional callback function that will be executed once the command is complete, successful or not.

The function can either be provided to an individual command as an argument, or it can be set as a Site's `event_callback` parameter, which will be used by every `send` command executed by the Site.

```javascript
function(err, event_type, context, [payload]) { ... }
```

### Callback Arguments

| NAME         | TYPE                                    | DESCRIPTION                                                                                                                                                                 |
| ------------ | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `err`        | String                                  | This argument will be null if the command was completed successfully. If the command encountered an error, this argument will contain a message describing the error.       |
| `event_type` | String                                  | The type of action that was sent. Supported values include: `'agreed'`, `'disagreed'`, `'displayed'`, `'visited'` and `'updated'`.                                          |
| `context`    | Site, BrowsewrapGroup or ClickwrapGroup | The Site or Group object that initiated the `send` command.                                                                                                                 |
| `payload`    | String                                  | This argument is only present when the Site's `disable_sending` property is set to `true`. It contains the URL-encoded payload that would have been sent to the Action API. |

# Event Types

## agreed

Indicates that a signer has accepted a specific version of a contract.

**Note**: The `signer_id` must be set for this type.

```javascript
send('agreed', contracts, versions, [group], [event_callback]);
```

### Arguments

| NAME             | REQUIRED | TYPE          | DESCRIPTION                                                                                                                                              |
| ---------------- | -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contracts`      | True     | Array`<Number>` | The `id` of each contract included in the action.                                                                                                        |
| `versions`       | True     | Array`<String>` | The `id` of each version included in the action. Ordering matters, as each `id` will be paired with its corresponding position in the `contracts` array. |
| `group`          | False    | Number        | The numeric `id` of the group containing the contracts.                                                                                                  |
| `event_callback` | False    | Function      | A callback function to execute once the command is complete.                                                                                             |

## disagreed

Indicates that a signer has disagreed to a previously accepted version of a contract.

**Note**: The `signer_id` must be set for this type.

```javascript
send('disagreed', contracts, versions, [group], [event_callback]);
```

### Arguments

| NAME             | REQUIRED | TYPE          | DESCRIPTION                                                                                                                                              |
| ---------------- | -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contracts`      | True     | Array`<Number>` | The `id` of each contract included in the action.                                                                                                        |
| `versions`       | True     | Array`<String>` | The `id` of each version included in the action. Ordering matters, as each `id` will be paired with its corresponding position in the `contracts` array. |
| `group`          | False    | Number        | The numeric `id` of the group containing the contracts.                                                                                                  |
| `event_callback` | False    | Function      | A callback function to execute once the command is complete.                                                                                             |

## displayed

Indicates that a specific version of a contract was displayed on the page.

**Note**: The `signer_id` is not required for this type.

```javascript
send('displayed', contracts, versions, [group], [event_callback]);
```

### Arguments

| NAME             | REQUIRED | TYPE          | DESCRIPTION                                                                                                                                              |
| ---------------- | -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contracts`      | True     | Array`<Number>` | The `id` of each contract included in the action.                                                                                                        |
| `versions`       | True     | Array`<String>` | The `id` of each version included in the action. Ordering matters, as each `id` will be paired with its corresponding position in the `contracts` array. |
| `group`          | False    | Number        | The numeric `id` of the group containing the contracts.                                                                                                  |
| `event_callback` | False    | Function      | A callback function to execute once the command is complete.                                                                                             |

## visited

Indicates that a group's legal center was visited.

**Note**: The `signer_id` is **not** required for this type.

```javascript
send('visited', [contracts], [versions], group, [event_callback]);
```

### Arguments

| NAME             | REQUIRED | TYPE          | DESCRIPTION                                                                                                                                              |
| ---------------- | -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contracts`      | False    | Array`<Number>` | The `id` of each contract included in the action.                                                                                                        |
| `versions`       | False    | Array`<String>` | The `id` of each version included in the action. Ordering matters, as each `id` will be paired with its corresponding position in the `contracts` array. |
| `group`          | True     | Number        | The numeric `id` of the group containing the contracts.                                                                                                  |
| `event_callback` | False    | Function      | A callback function to execute once the command is complete.                                                                                             |

## updated

Saves additional name and value pairs to the signer's record.

**Note**: The `signer_id` and `custom_data` must be set for this type.

```javascript
send('updated', parameters);
```

### Arguments

| NAME         | REQUIRED    | TYPE   | DESCRIPTION                                                                                                                                                                                                  |
| ------------ | ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `parameters` | Conditional | Object | An object containing name and value pairs to send with the action. If the `custom_data` parameter hasn't already been set at the Site level, it should be passed as a property of the `parameters` argument. |