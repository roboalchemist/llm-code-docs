# Source: https://docs.base44.com/developers/references/sdk/docs/type-aliases/entities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# entities

***

## Overview

Entities module for managing app data.

This module provides dynamic access to all entities in the app.
Each entity gets a handler with full CRUD operations and additional utility methods.

Entities are accessed dynamically using the pattern:
`base44.entities.EntityName.method()`

This module is available to use with a client in all authentication modes:

* **Anonymous or User authentication** (`base44.entities`): Access is scoped to the current user's permissions. Anonymous users can only access public entities, while authenticated users can access entities they have permission to view or modify.
* **Service role authentication** (`base44.asServiceRole.entities`): Operations have elevated admin-level permissions. Can access all entities that the app's admin role has access to.

### Entity Handlers

An entity handler is the object you get when you access an entity through `base44.entities.EntityName`. Every entity in your app automatically gets a handler with CRUD methods for managing records.

For example, `base44.entities.Task` is an entity handler for Task records, and `base44.entities.User` is an entity handler for User records. Each handler provides methods like `list()`, `create()`, `update()`, and `delete()`.

You don't need to instantiate or import entity handlers. They're automatically available for every entity you create in your app.

### Built-in User Entity

Every app includes a built-in `User` entity that stores user account information. This entity has special security rules that can't be changed.

Regular users can only read and update their own user record. With service role authentication, you can read, update, and delete any user. You can't create users using the entities module. Instead, use the functions of the [auth module](../interfaces/auth) to invite or register new users.

### Generated Types

If you're working in a TypeScript project, you can generate types from your entity schemas to get autocomplete and type checking on all entity methods. See the [Dynamic Types](/developers/references/sdk/getting-started/dynamic-types) guide to get started.

#### Examples

<CodeGroup>
  ```typescript Get all records from the MyEntity entity theme={null}
  // Get all records the current user has permissions to view
  const myRecords = await base44.entities.MyEntity.list();
  ```

  ```typescript List all users (admin only) theme={null}
  const allUsers = await base44.asServiceRole.entities.User.list();
  ```
</CodeGroup>

## Entity Handler Methods

***

Entity handler providing CRUD operations for a specific entity type.

Each entity in the app gets a handler with these methods for managing data.

### list()

> **list**\<`K extends keyof T`>(\
> `sort?`,\
> `limit?`,\
> `skip?`,\
> `fields?`\
> ): `Promise`\<`Pick`\<`T`, `K`>\[]>

Lists records with optional pagination and sorting.

Retrieves all records of this type with support for sorting,
pagination, and field selection.

**Note:** The maximum limit is 5,000 items per request.

#### Parameters

<Accordion title="Properties">
  <ParamField body="sort" type="SortField<T>">
    A [`SortField<T>`](#sortfield) specifying sort order, such as `'-created_date'` for descending. Defaults to `'-created_date'`.
  </ParamField>

  <ParamField body="limit" type="number">
    Maximum number of results to return. Defaults to `50`.
  </ParamField>

  <ParamField body="skip" type="number">
    Number of results to skip for pagination. Defaults to `0`.
  </ParamField>

  <ParamField body="fields" type="(keyof T)[]">
    Array of field names to include in the response. Defaults to all fields.
  </ParamField>
</Accordion>

#### Returns

Promise resolving to an array of records with selected fields.

#### Examples

<CodeGroup>
  ```typescript Get all records theme={null}
  const records = await base44.entities.MyEntity.list();
  ```

  ```typescript Get first 10 records sorted by date theme={null}
  const recentRecords = await base44.entities.MyEntity.list('-created_date', 10);
  ```

  ```typescript Get paginated results theme={null}
  // Skip first 20, get next 10
  const page3 = await base44.entities.MyEntity.list('-created_date', 10, 20);
  ```

  ```typescript Get only specific fields theme={null}
  const fields = await base44.entities.MyEntity.list('-created_date', 10, 0, ['name', 'status']);
  ```
</CodeGroup>

***

### filter()

> **filter**\<`K extends keyof T`>(\
> `query`,\
> `sort?`,\
> `limit?`,\
> `skip?`,\
> `fields?`\
> ): `Promise`\<`Pick`\<`T`, `K`>\[]>

Filters records based on a query.

Retrieves records that match specific criteria with support for
sorting, pagination, and field selection.

**Note:** The maximum limit is 5,000 items per request.

#### Parameters

<Accordion title="Properties">
  <ParamField body="query" type="Partial<T>" required>
    Query object with field-value pairs. Each key should be a field name
    from your entity schema, and each value is the criteria to match. Records matching all
    specified criteria are returned. Field names are case-sensitive.
  </ParamField>

  <ParamField body="sort" type="SortField<T>">
    A [`SortField<T>`](#sortfield) specifying sort order, such as `'-created_date'` for descending. Defaults to `'-created_date'`.
  </ParamField>

  <ParamField body="limit" type="number">
    Maximum number of results to return. Defaults to `50`.
  </ParamField>

  <ParamField body="skip" type="number">
    Number of results to skip for pagination. Defaults to `0`.
  </ParamField>

  <ParamField body="fields" type="(keyof T)[]">
    Array of field names to include in the response. Defaults to all fields.
  </ParamField>
</Accordion>

#### Returns

Promise resolving to an array of filtered records with selected fields.

#### Examples

<CodeGroup>
  ```typescript Filter by single field theme={null}
  const activeRecords = await base44.entities.MyEntity.filter({
    status: 'active'
  });
  ```

  ```typescript Filter by multiple fields theme={null}
  const filteredRecords = await base44.entities.MyEntity.filter({
    priority: 'high',
    status: 'active'
  });
  ```

  ```typescript Filter with sorting and pagination theme={null}
  const results = await base44.entities.MyEntity.filter(
    { status: 'active' },
    '-created_date',
    20,
    0
  );
  ```

  ```typescript Filter with specific fields theme={null}
  const fields = await base44.entities.MyEntity.filter(
    { priority: 'high' },
    '-created_date',
    10,
    0,
    ['name', 'priority']
  );
  ```
</CodeGroup>

***

### get()

> **get**(`id`): `Promise`\<`T`>

Gets a single record by ID.

Retrieves a specific record using its unique identifier.

#### Parameters

<ParamField body="id" type="string" required>
  The unique identifier of the record.
</ParamField>

#### Returns

`Promise<T>`

Promise resolving to the record.

#### Example

<CodeGroup>
  ```typescript Get record by ID theme={null}
  const record = await base44.entities.MyEntity.get('entity-123');
  console.log(record.name);
  ```
</CodeGroup>

***

### create()

> **create**(`data`): `Promise`\<`T`>

Creates a new record.

Creates a new record with the provided data.

#### Parameters

<ParamField body="data" type="Partial<T>" required>
  Object containing the record data.
</ParamField>

#### Returns

`Promise<T>`

Promise resolving to the created record.

#### Example

<CodeGroup>
  ```typescript Create a new record theme={null}
  const newRecord = await base44.entities.MyEntity.create({
    name: 'My Item',
    status: 'active',
    priority: 'high'
  });
  console.log('Created record with ID:', newRecord.id);
  ```
</CodeGroup>

***

### update()

> **update**(`id`, `data`): `Promise`\<`T`>

Updates an existing record.

Updates a record by ID with the provided data. Only the fields
included in the data object will be updated.

#### Parameters

<Accordion title="Properties">
  <ParamField body="id" type="string" required>
    The unique identifier of the record to update.
  </ParamField>

  <ParamField body="data" type="Partial<T>" required>
    Object containing the fields to update.
  </ParamField>
</Accordion>

#### Returns

`Promise<T>`

Promise resolving to the updated record.

#### Examples

<CodeGroup>
  ```typescript Update single field theme={null}
  const updated = await base44.entities.MyEntity.update('entity-123', {
    status: 'completed'
  });
  ```

  ```typescript Update multiple fields theme={null}
  const updated = await base44.entities.MyEntity.update('entity-123', {
    name: 'Updated name',
    priority: 'low',
    status: 'active'
  });
  ```
</CodeGroup>

***

### delete()

> **delete**(`id`): `Promise`\<`DeleteResult`>

Deletes a single record by ID.

Permanently removes a record from the database.

#### Parameters

<ParamField body="id" type="string" required>
  The unique identifier of the record to delete.
</ParamField>

#### Returns

`DeleteResult`

Result returned when deleting a single entity.

<Accordion title="Properties">
  <ResponseField name="success" type="boolean" required>
    Whether the deletion was successful.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Delete a record theme={null}
  const result = await base44.entities.MyEntity.delete('entity-123');
  console.log('Deleted:', result.success);
  ```
</CodeGroup>

***

### deleteMany()

> **deleteMany**(`query`): `Promise`\<`DeleteManyResult`>

Deletes multiple records matching a query.

Permanently removes all records that match the provided query.

#### Parameters

<ParamField body="query" type="Partial<T>" required>
  Query object with field-value pairs. Each key should be a field name
  from your entity schema, and each value is the criteria to match. Records matching all
  specified criteria will be deleted. Field names are case-sensitive.
</ParamField>

#### Returns

`DeleteManyResult`

Result returned when deleting multiple entities.

<Accordion title="Properties">
  <ResponseField name="success" type="boolean" required>
    Whether the deletion was successful.
  </ResponseField>

  <ResponseField name="deleted" type="number" required>
    Number of entities that were deleted.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Delete by multiple criteria theme={null}
  const result = await base44.entities.MyEntity.deleteMany({
    status: 'completed',
    priority: 'low'
  });
  console.log('Deleted:', result.deleted);
  ```
</CodeGroup>

***

### bulkCreate()

> **bulkCreate**(`data`): `Promise`\<`T`\[]>

Creates multiple records in a single request.

Efficiently creates multiple records at once. This is faster
than creating them individually.

#### Parameters

<ParamField body="data" type="Partial<T>[]" required>
  Array of record data objects.
</ParamField>

#### Returns

`Promise<T[]>`

Promise resolving to an array of created records.

#### Example

<CodeGroup>
  ```typescript Create multiple records at once theme={null}
  const result = await base44.entities.MyEntity.bulkCreate([
    { name: 'Item 1', status: 'active' },
    { name: 'Item 2', status: 'active' },
    { name: 'Item 3', status: 'completed' }
  ]);
  ```
</CodeGroup>

***

### importEntities()

> **importEntities**(`file`): `Promise`\<`ImportResult`\<`T`>>

Imports records from a file.

Imports records from a file, typically CSV or similar format.
The file format should match your entity structure. Requires a browser environment and can't be used in the backend.

#### Parameters

<ParamField body="file" type="File" required>
  File object to import.
</ParamField>

#### Returns

`ImportResult<T>`

Result returned when importing entities from a file.

<Accordion title="Properties">
  <ResponseField name="status" type="&#x22;success&#x22; | &#x22;error&#x22;" required>
    Status of the import operation.
  </ResponseField>

  <ResponseField name="details" type="string | null" required>
    Details message, e.g., "Successfully imported 3 entities with RLS enforcement".
  </ResponseField>

  <ResponseField name="output" type="T[] | null" required>
    Array of created entity objects when successful, or null on error.
  </ResponseField>
</Accordion>

#### Example

<CodeGroup>
  ```typescript Import records from file in React theme={null}
  const handleFileImport = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      const result = await base44.entities.MyEntity.importEntities(file);
      if (result.status === 'success' && result.output) {
        console.log(`Imported ${result.output.length} records`);
      }
    }
  };
  ```
</CodeGroup>

***

### subscribe()

> **subscribe**(`callback`): () => `void`

Subscribes to realtime updates for all records of this entity type.

Establishes a WebSocket connection to receive instant updates when any
record is created, updated, or deleted. Returns an unsubscribe function
to clean up the connection.

#### Parameters

<ParamField body="callback" type="RealtimeCallback<T>" required>
  Callback function called when an entity changes. The callback receives an event object with the following properties:

  * `type`: The type of change that occurred - `'create'`, `'update'`, or `'delete'`.
  * `data`: The entity data after the change.
  * `id`: The unique identifier of the affected entity.
  * `timestamp`: ISO 8601 timestamp of when the event occurred.
</ParamField>

#### Returns

Unsubscribe function to stop receiving updates.

#### Example

<CodeGroup>
  ```typescript Subscribe to all Task changes theme={null}
  const unsubscribe = base44.entities.Task.subscribe((event) => {
    console.log(`Task ${event.id} was ${event.type}d:`, event.data);
  });

  // Later, clean up the subscription
  unsubscribe();
  ```
</CodeGroup>

## Type Definitions

### EntityRecord

***

> **EntityRecord** = `{ [K in keyof EntityTypeRegistry]: EntityTypeRegistry[K] & ServerEntityFields }`

Combines the [`EntityTypeRegistry`](#entitytyperegistry) schemas with server fields like `id`, `created_date`, and `updated_date` to give the complete record type for each entity. Use this when you need to type variables holding entity data.

#### Example

<CodeGroup>
  ```typescript Using EntityRecord to get the complete type for an entity theme={null}
  // Combine your schema with server fields (id, created_date, etc.)
  type TaskRecord = EntityRecord['Task'];

  const task: TaskRecord = await base44.entities.Task.create({
    title: 'My task',
    status: 'pending'
  });

  // Task now includes both your fields and server fields:
  console.log(task.id);           // Server field
  console.log(task.created_date); // Server field
  console.log(task.title);        // Your field
  ```
</CodeGroup>

### EntityTypeRegistry

***

Registry mapping entity names to their TypeScript types. The [`types generate`](/developers/references/cli/commands/types-generate) command fills this registry, then [`EntityRecord`](#entityrecord) adds server fields.

### SortField

***

> **SortField**\<`T`> = `keyof T` | `` `+${keyof T}` `` | `` `-${keyof T}` ``

Sort field type for entity queries.

Accepts any field name from the entity type with an optional prefix:

* `'+'` prefix or no prefix: ascending sort
* `'-'` prefix: descending sort

#### Example

<CodeGroup>
  ```typescript Specify sort direction by prefixing field names with + or - theme={null}
  // Ascending sort
  'created_date'
  '+created_date'

  // Descending sort
  '-created_date'
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).