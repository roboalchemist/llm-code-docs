# Source: https://dev.writer.com/blueprints/key-valuestorage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Key-Value Storage

Stores data between sessions. Uses unique keys (names) to identify the data. Keys can only contain alphanumeric characters, underscores, and hyphens.

<img src="https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=af1402f1adb8c8274aec5f658c4d2301" alt="" data-og-width="1331" width="1331" data-og-height="796" height="796" data-path="images/agent-builder/blueprints/key-value-storage-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?w=280&fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=66093a65e05a903ba1f252780db7f953 280w, https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?w=560&fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=f28bfd455f15c7e7cd945864fd71a974 560w, https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?w=840&fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=56fab7e28db796ebdf981ba3d3f0f6a3 840w, https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?w=1100&fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=2a70e19f2a3c08b077f83af37ce99172 1100w, https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?w=1650&fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=b91baf32f696982cd43333a6bbe1ebf5 1650w, https://mintcdn.com/writer/dStw8zI8X1OyAw6r/images/agent-builder/blueprints/key-value-storage-block.png?w=2500&fit=max&auto=format&n=dStw8zI8X1OyAw6r&q=85&s=f52b725de78e59ad3c851f91161fc140 2500w" />

## Overview

The **Key-Value Storage** block allows you to save data in the cloud between browser sessions and agent redeploys. Unlike [agent state](/agent-builder/state), which is session-based and temporary, Key-Value Storage provides persistent storage through browser refreshes, new sessions, and agent updates.

This block works with individual items or JSON-serializable objects such as lists, dictionaries, and other nested structures.

<Note>
  **Storage scope:** Key-Value Storage is **per agent**, not per user. All users of the same agent share the same storage namespace. If you need user-specific data, include a user identifier in your key names (for example, `user_preferences_{user_id}`) to ensure data isolation between users.
</Note>

## Common use cases

* Storing user preferences or settings that should persist across sessions
* Maintaining application data that needs to survive agent redeploys
* Storing configuration data or feature flags
* Persisting user progress or state in multi-step workflows

<Warning>
  Key-value storage is not a secure way to store sensitive data. If you need to store sensitive data, use [Vault](/agent-builder/secrets).
</Warning>

## How it works

The Key-Value Storage block provides four actions: [save](#save), [get](#get), [delete](#delete), and [list keys](#list-keys).

### Save

Specify a key (name) and a value you want to associate with it. If this key already exists, the existing value is updated. If it doesn't exist, it is created.

* **Key**: A unique identifier for your data. Keys can only contain alphanumeric characters, underscores, and hyphens.
* **Value type**: Choose how to interpret the value:
  * **Plain text**: Stores the value as a string.
  * **JSON**: Parses the value as JSON, allowing you to store objects, lists, and nested structures directly.
* **Value**: The data you want to store. You can enter plain text, use expressions like `@{state.username}`, or enter JSON directly when using JSON value type.

When you save a value, it's stored in the cloud and associated with your agent. The data persists even if the user closes their browser or you redeploy the agent.

<Note>
  To store structured data (objects, lists, nested structures), set Value type to **JSON** and enter your data directly in the Value field, or reference a state variable using `@{state.variable_name}`.
</Note>

### Get

Specify a key name to retrieve the data you've stored under that key. If the key exists, the block returns the stored value. If the key doesn't exist, the block raises an error that you can handle with error routing.

The retrieved value maintains its original structure. If you stored a complex object as JSON, you'll get back the same structure with all nested attributes accessible.

### Delete

Specify a key name to delete the data associated with that key. This permanently removes the key-value pair from storage. If you try to delete a key that doesn't exist, the block raises an error.

### List keys

Retrieve a list of all keys currently stored for your agent. This action doesn't require a key parameter, and returns an array of key names that you can use to iterate over stored data or check what data exists.

## Accessing nested data

When you store structured data (either by setting Value type to JSON or by referencing a state variable like `@{state.user_profile}`), you can access nested attributes directly in subsequent blocks using dot notation, similar to how you access [nested state variables](/agent-builder/state#nested-state-variables).

For example, if `state.user_profile` contains:

```json  theme={null}
{
  "name": "John Doe",
  "preferences": {
    "theme": "dark",
    "language": "en"
  },
  "tasks": [
    {"id": 1, "title": "Task 1"},
    {"id": 2, "title": "Task 2"}
  ]
}
```

After saving this data (either by entering the JSON directly with Value type set to JSON, or by using `@{state.user_profile}` as the Value), you can retrieve it with the **Get** action and access nested values in subsequent blocks using dot notation:

* `@{result.name}` returns "John Doe"
* `@{result.preferences.theme}` returns "dark"
* `@{result.tasks.0.title}` returns "Task 1"

## Examples

### Caching computed results

This example shows how to cache expensive computations for reuse.

**Blueprint Flow:**

1. **UI Trigger** → User requests data analysis
2. **Key-Value Storage (Get)** → Attempts to retrieve cached result with key `analysis_result`
   * **Success path** → Display cached result
   * **Error path** → If cache doesn't exist:
     * **Python code** → Perform expensive computation
     * **Key-Value Storage (Save)** → Store result with key `analysis_result`
     * **Set state** → Display result to user

### Managing application configuration

This example demonstrates storing configuration data that survives agent redeploys.

**Blueprint Flow:**

1. **UI Trigger** → Admin updates configuration
2. **Key-Value Storage (Save)** → Stores configuration with key `app_config`
3. **Set state** → Confirms update

In other parts of the agent:

1. **Key-Value Storage (Get)** → Retrieves configuration with key `app_config`
2. **Python code** → Uses configuration values (accessible via `@{result}`) to control agent behavior

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Action</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <code>Save</code>
      </td>

      <td>-</td>

      <td>
        <ul>
          <li>Save - Save</li>

          <li>Get - Get</li>

          <li>Delete - Delete</li>

          <li>List keys - List keys</li>
        </ul>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Key</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Value type</td>
      <td>Text</td>
      <td>-</td>

      <td>
        <code>text</code>
      </td>

      <td>-</td>

      <td>
        <ul>
          <li>text - Plain text</li>

          <li>JSON - JSON</li>
        </ul>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Value</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The request was successful.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The request wasn't successful.</td>
    </tr>
  </tbody>
</table>
