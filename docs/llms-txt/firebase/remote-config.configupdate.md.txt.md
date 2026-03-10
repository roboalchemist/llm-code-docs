# Source: https://firebase.google.com/docs/reference/js/remote-config.configupdate.md.txt

# ConfigUpdate interface

Contains information about which keys have been updated.

**Signature:**

    export interface ConfigUpdate 

## Methods

| Method | Description |
|---|---|
| [getUpdatedKeys()](https://firebase.google.com/docs/reference/js/remote-config.configupdate.md#configupdategetupdatedkeys) | Parameter keys whose values have been updated from the currently activated values. Includes keys that are added, deleted, or whose value, value source, or metadata has changed. |

## ConfigUpdate.getUpdatedKeys()

Parameter keys whose values have been updated from the currently activated values. Includes keys that are added, deleted, or whose value, value source, or metadata has changed.

**Signature:**

    getUpdatedKeys(): Set<string>;

**Returns:**

Set\<string\>