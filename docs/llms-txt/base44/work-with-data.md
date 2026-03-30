# Source: https://docs.base44.com/developers/references/sdk/getting-started/work-with-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Work with data

> Create, read, update, and delete data in your Base44 app

The [`entities`](/developers/references/sdk/docs/type-aliases/entities) module lets you work with your app's data. Each entity type in your app has methods for creating, reading, updating, and deleting records.

You access entity methods through your entity name: `base44.entities.YourEntityName.methodName()`. For example, if you have a `Task` entity, you use [`base44.entities.Task.list()`](/developers/references/sdk/docs/type-aliases/entities#list) to get a list of tasks.

<Tip>
  Generate TypeScript types from your entities to get autocomplete and type
  safety. Run [`base44 types
    generate`](/developers/references/cli/commands/types-generate) in your
  project, and all entity fields, methods, and return types will be fully typed.
  Learn more about [dynamic
  types](/developers/references/sdk/getting-started/dynamic-types).
</Tip>

## Permissions

Data access is controlled by the client's authentication mode and your app's permission rules. You can configure the permissions for each entity in your app's security settings. Learn more about [changing data permissions](https://docs.base44.com/Building-your-app/Managing-your-app-data#changing-data-permissions).

* **Anonymous users**: Can only access entities marked as public.
* **Authenticated users**: Can access entities and records they have permission to view or modify based on your app's configured access rules.
* **Service role**: Can access all entities and records available to the app's admin.

In backend code, you can use the [service role to access data with admin permissions](#service-role-data-access).

## Create records

Use [`create()`](/developers/references/sdk/docs/type-aliases/entities#create) to add new records to an entity:

<CodeGroup>
  ```typescript Create a record theme={null}
  const newTask = await base44.entities.Task.create({
    title: "Complete documentation",
    status: "pending",
    dueDate: "2024-12-31",
  });
  ```

  ```typescript With generated types theme={null}
  // After running: base44 types generate
  const newTask = await base44.entities.Task.create({
    title: "Complete documentation",
    status: "pending",
    // TypeScript knows which fields exist
    // and validates their types
  });

  // Autocomplete works for fields
  console.log(newTask.id);
  console.log(newTask.created_date);
  ```
</CodeGroup>

## Read records

Retrieve data using [`get()`](/developers/references/sdk/docs/type-aliases/entities#get) for a single record, [`list()`](/developers/references/sdk/docs/type-aliases/entities#list) for all records, or [`filter()`](/developers/references/sdk/docs/type-aliases/entities#filter) for records matching specific criteria.

Use [`get()`](/developers/references/sdk/docs/type-aliases/entities#get) with a record ID to retrieve a specific record:

<CodeGroup>
  ```typescript Get by ID theme={null}
  const task = await base44.entities.Task.get(taskId);
  ```
</CodeGroup>

Use [`list()`](/developers/references/sdk/docs/type-aliases/entities#list) to retrieve all records. The method supports sorting, pagination, and field selection:

<CodeGroup>
  ```typescript List all theme={null}
  const tasks = await base44.entities.Task.list();
  ```

  ```typescript Sort results theme={null}
  const tasks = await base44.entities.Task.list("-created_date");
  ```

  ```typescript Paginate results theme={null}
  const tasks = await base44.entities.Task.list(
    "-created_date",
    10, // limit
    20, // skip
  );
  ```

  ```typescript Select specific fields theme={null}
  const tasks = await base44.entities.Task.list(
    "-created_date",
    10,
    0,
    ["title", "status"], // only return these fields
  );
  ```
</CodeGroup>

Use [`filter()`](/developers/references/sdk/docs/type-aliases/entities#filter) to find records that match specific criteria:

<CodeGroup>
  ```typescript Filter by single field theme={null}
  const pendingTasks = await base44.entities.Task.filter({
    status: "pending",
  });
  ```

  ```typescript Filter by multiple fields theme={null}
  const urgentTasks = await base44.entities.Task.filter({
    status: "pending",
    priority: "high",
  });
  ```

  ```typescript Filter with sorting theme={null}
  const recentTasks = await base44.entities.Task.filter(
    { status: "pending" },
    "-created_date", // Sort by created date, descending
  );
  ```

  ```typescript Filter with pagination theme={null}
  const tasks = await base44.entities.Task.filter(
    { status: "pending" },
    "-created_date",
    10, // limit
    20, // skip
  );
  ```
</CodeGroup>

## Update records

Use [`update()`](/developers/references/sdk/docs/type-aliases/entities#update) to modify an existing record:

<CodeGroup>
  ```typescript Update a record theme={null}
  await base44.entities.Task.update(taskId, {
    status: "completed",
  });
  ```
</CodeGroup>

## Delete records

Use [`delete()`](/developers/references/sdk/docs/type-aliases/entities#delete) to remove a single record:

<CodeGroup>
  ```typescript Delete a record theme={null}
  await base44.entities.Task.delete(taskId);
  ```
</CodeGroup>

Use [`deleteMany()`](/developers/references/sdk/docs/type-aliases/entities#deletemany) to remove multiple records matching specific criteria:

<CodeGroup>
  ```typescript Delete multiple records theme={null}
  const result = await base44.entities.Task.deleteMany({
    status: "completed",
    priority: "low",
  });
  ```
</CodeGroup>

## Bulk operations

Use [`bulkCreate()`](/developers/references/sdk/docs/type-aliases/entities#bulkcreate) to create multiple records in a single request:

<CodeGroup>
  ```typescript Create multiple records theme={null}
  const tasks = await base44.entities.Task.bulkCreate([
    { title: "Task 1", status: "pending" },
    { title: "Task 2", status: "pending" },
    { title: "Task 3", status: "in-progress" },
  ]);
  ```
</CodeGroup>

Use [`importEntities()`](/developers/references/sdk/docs/type-aliases/entities#importentities) to import records from a CSV file. This is useful for migrating data or bulk uploads from user interfaces:

<CodeGroup>
  ```typescript Import from file theme={null}
  const handleFileUpload = async (event) => {
    const file = event.target.files?.[0];
    if (file) {
      const result = await base44.entities.Task.importEntities(file);
      console.log(`Imported ${result.output.length} records`);
    }
  };
  ```
</CodeGroup>

<Note>
  `importEntities()` requires a browser environment and cannot be used in
  backend code.
</Note>

## Realtime subscriptions

Use [`subscribe()`](/developers/references/sdk/docs/type-aliases/entities#subscribe) to receive realtime updates when records are created, updated, or deleted:

<CodeGroup>
  ```typescript Subscribe to changes theme={null}
  const unsubscribe = base44.entities.Task.subscribe((event) => {
    console.log(`Task ${event.id} was ${event.type}d`);
    console.log("Updated data:", event.data);
  });

  // Later, clean up the subscription
  unsubscribe();
  ```
</CodeGroup>

## Service role data access

By default, data access is scoped to the current user's permissions. With service role authentication, you can access data with admin-level permissions. This means you can access data that the admin role in your app has access to.

Use `base44.asServiceRole.entities` to access data with admin permissions:

<CodeGroup>
  ```typescript Service role access theme={null}
  // User-level access (limited to current user's permissions)
  const myTasks = await base44.entities.Task.list();

  // Service role access (admin-level permissions)
  const allTasks = await base44.asServiceRole.entities.Task.list();
  ```
</CodeGroup>

## User entity

Every Base44 app includes a built-in `User` entity that stores user account information. This entity has special security rules:

* Regular users can only read and update their own user record
* With service role authentication, you can read, update, and delete any user
* You cannot create users through the entities module - use the `auth` module instead

You can add fields to the User entity to store additional user data, then use those fields in security rules to control data access or in your app to personalize the experience. See [User Schema](/developers/backend/resources/entities/user-schema) for details.

<CodeGroup>
  ```typescript List all users using the service role theme={null}
  const allUsers = await base44.asServiceRole.entities.User.list();
  ```
</CodeGroup>

## See more

<CardGroup cols={2}>
  <Card title="entities module" icon="database" href="/developers/references/sdk/docs/type-aliases/entities">
    Complete API reference
  </Card>

  <Card title="Base44 client" icon="code" href="/developers/references/sdk/getting-started/client">
    Learn about the client and service role
  </Card>
</CardGroup>


Built with [Mintlify](https://mintlify.com).