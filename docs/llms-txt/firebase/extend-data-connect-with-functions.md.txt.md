# Source: https://firebase.google.com/docs/data-connect/extend-data-connect-with-functions.md.txt

With Cloud Functions for Firebase, you can handle events in
Firebase Data Connect. Cloud Functions lets you run server-side code in
response to events, such as the execution of a mutation in your
Data Connect service. This lets you add custom logic without
deploying your own servers.

## Common use cases

- **Data Synchronization:** Replicate or synchronize data with other systems
  (like Cloud Firestore, BigQuery, or external APIs) after a mutation
  occurs.

- **Asynchronous Workflows:** Kick off long-running processes, such as image
  processing or data aggregation, after a database change.

- **User engagement:** Send emails or Cloud Messaging notifications to
  users after a specific mutation event in your application, such as account
  creation.

## Trigger a function on a Data Connect mutation

You can trigger a function whenever a Data Connect mutation is executed
using the `onMutationExecuted` event handler. This trigger occurs upon execution
of a [mutation](https://firebase.google.com/docs/data-connect/mutations-guide).

### A basic mutation event function

The following basic example is a function that logs the details of
any mutation executed in your Data Connect service:

### Node.js

    import { onMutationExecuted } from "firebase-functions/dataconnect";
    import { logger } from "firebase-functions";

    export const logMutation = onMutationExecuted(
      {
        /* Trigger on all mutations, spanning all services and connectors
           in us-central1 */
      },
      (event) => {
        logger.info("A mutation was executed!", {
          data: event.data,
        });
      }
    );

### Python

    from firebase_functions import dataconnect_fn, logger

    @dataconnect_fn.on_mutation_executed()
    def log_mutation(event: dataconnect_fn.Event):
      logger.info("A mutation was executed!", event.data)

When triggering off of all mutations in your project, you must not perform any
mutations in the trigger handler or you will cause an infinite loop. If you want
to perform mutations in an event trigger, use the filtering options described
below, and take care that the mutation does not trigger itself.

### Set the function location

The [function location](https://firebase.google.com/docs/functions/locations) must match the
[Data Connect service location](https://firebase.google.com/docs/data-connect/manage-services-and-databases)
for events to trigger the function. By default, the function region is
`us-central1`.

### Node.js

    import { onMutationExecuted } from "firebase-functions/dataconnect";

    export const onMutationRegionOption = onMutationExecuted(
      {
        region: "europe-west1"  // Set if Data Connect service location is not us-central1
      },
      (event) => { /* ... */ }
    );

### Python

    @dataconnect_fn.on_mutation_executed(
      region="europe-west1"  # Set if Data Connect service location is not us-central1
    )
    def mutation_executed_handler_region_option(event: dataconnect_fn.Event):
      pass

### Filter events

The `onMutationExecuted` handler can be configured with options to filter events
based on specific attributes. This is useful when you only want to trigger your
function for certain mutations.

You can filter by `service`, `connector`, and `operation`:

### Node.js

    import { onMutationExecuted } from "firebase-functions/dataconnect";
    import { logger } from "firebase-functions";

    // Trigger this function only for the CreateUser mutation
    // in the users connector of the myAppService service.
    export const onUserCreate = onMutationExecuted(
      {
        service: "myAppService",
        connector: "users",
        operation: "CreateUser",
      },
      (event) => {
        logger.info("A new user was created!", event.data);
        // Add logic here: for example, sending a welcome email.
      }
    );

### Python

    from firebase_functions import dataconnect_fn, logger

    @dataconnect_fn.on_mutation_executed(
      service="myAppService",
      connector="users",
      operation="CreateUser"
    ):
    def on_user_create(event: dataconnect_fn.Event):
      logger.info("A new user was created!", event.data)

### Wildcards and capture groups

You can use wildcards and capture groups to filter your triggers on multiple
values. Any groups captured are available
in `event.params` to use. See [Understand path patterns](https://cloud.google.com/eventarc/docs/path-patterns#apply_a_path_pattern)
for more information.

Examples:

### Node.js

    import { onMutationExecuted } from "firebase-functions/dataconnect";

    // Trigger on all operations that match the pattern `User*`, on any service and
    // connector.
    export const onMutationWildcards = onMutationExecuted(
      {
        operation: "User*",
      },
      (event) => {}
    );

    // Trigger on all operations that match the pattern `User*`, on any service and
    // connector. Capture the operation name in the variable `op`.
    export const onMutationCaptureWildcards = onMutationExecuted(
      {
        operation: "{op=User*}",
      },
      (event) => {
        // `event.params.op` contains the operation name.
      }
    );

    // Trigger on all operations on the service `myAppService`. Capture the
    // operation name in the variable `operation`.
    export const onMutationCaptures = onMutationExecuted(
      {
        service: "myAppService",
        operation: "{operation}",
      },
      (event) => {
        // `event.params.operation` contains the operation name.
      }
    );

### Python

    from firebase_functions import dataconnect_fn

    # Trigger on all operations that match the pattern `User*`, on any service and
    # connector.
    @dataconnect_fn.on_mutation_executed(
      operation="User*"
    )
    def on_mutation_wildcards(event: dataconnect_fn.Event):
      pass

    # Trigger on all operations that match the pattern `User*`, on any service and
    # connector. Capture the operation name in the variable `op`.
    @dataconnect_fn.on_mutation_executed(
      operation="{op=User*}"
    )
    def on_mutation_capture_wildcards(event: dataconnect_fn.Event):
      # `event.params["op"]` contains the operation name.
      pass

    # Trigger on all operations on the service `myAppService`. Capture the
    # operation name in the variable `operation`.
    @dataconnect_fn.on_mutation_executed(
      service="myAppService",
      operation="{operation}"
    )
    def on_mutation_captures(event: dataconnect_fn.Event):
      # `event.params["operation"]` contains the operation name.
      pass

### Access user authentication information

You can access user authentication information about the principal that
triggered the event. For more information about the data available in the
authentication context, see [Auth Context](https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/authcontext.md).

The following example demonstrates how to retrieve authentication information:

### Node.js

    import { onMutationExecuted } from "firebase-functions/dataconnect";

    export const onMutation = onMutationExecuted(
      { operation: "MyMutation" },
      (event) => {
        // mutationExecuted event provides authType and authId:
        // event.authType
        // event.authId
      }
    );

### Python

    from firebase_functions import dataconnect_fn

    @dataconnect_fn.on_mutation_executed(operation="MyMutation")
    def mutation_executed_handler(event: dataconnect_fn.Event):
      # mutationExecuted event provides auth_type and auth_id, which are accessed as follows
      # event.auth_type
      # event.auth_id
      pass

The auth type and auth ID will be populated as such:

| **Mutation initiated by** | **authtype** | **authid** |
|---|---|---|
| Authenticated end user | `app_user` | Firebase Auth token UID |
| Unauthenticated end user | `unauthenticated` | empty |
| Admin SDK impersonating an end user | `app_user` | Firebase Auth token UID of the impersonated user |
| Admin SDK impersonating an unauthenticated request | `unauthenticated` | empty |
| Admin SDK with full permissions | `admin` | empty |

### Access event data

The `CloudEvent` object passed to your function contains information about the
event that triggered it.

#### Event attributes

| Attribute | Type | Description |
|---|---|---|
| `id` | `string` | A unique identifier for the event. |
| `source` | `string` | The connector resource that produced the event (for example, `//firebasedataconnect.googleapis.com/projects/*/locations/*/services/*/connectors/*`). |
| `specversion` | `string` | The `CloudEvents` specification version (e.g., "1.0"). |
| `type` | `string` | The type of the event: `google.firebase.dataconnect.connector.v1.mutationExecuted`. |
| `time` | `string` | The timestamp (ISO 8601 format) for when the event was produced. |
| `subject` | `string` | Optional. Extra information about the event context, like the operation name. |
| `params` | `object` | A map of captured path patterns. |
| `authType` | `string` | An enum representing the type of principal that triggered the event. |
| `authId` | `string` | A unique identifier of the principal that triggered the event. |
| `data` | `MutationEventData` | The payload of the Data Connect event. See the next section. |

#### Data payload

The `MutationEventData` object contains the payload of the
Data Connect event:

    {
      // ...
      "authType": // ...
      "data": {
        "payload": {
          "variables": {
            "userId": "user123",
            "updateData": {
              "displayName": "New Name"
            }
          },
          "data": {
            "updateUser": {
              "id": "user123",
              "displayName": "New Name",
              "email": "user@example.com"
            }
          },
          "errors": []
        }
      }
    }

- **`payload.variables`**: An object containing the variables that were passed to the mutation.
- **`payload.data`**: An object containing the data that was returned by the mutation.
- **`payload.errors`**: An array of any errors that occurred during the mutation's execution. If the mutation was successful, this array will be empty.

#### Example

Here's how you can access the mutation variables and the returned data:

### Node.js

    import { onMutationExecuted } from "firebase-functions/dataconnect";
    import { logger } from "firebase-functions";

    export const processNewUserData = onMutationExecuted(
      {
        "service": "myAppService",
        "connector": "users",
        "operation": "CreateUser",
      },
      (event) => {
        // The variables passed to the mutation
        const mutationVariables = event.data.payload.variables;

        // The data returned by the mutation
        const returnedData = event.data.payload.data;

        logger.info("Processing mutation with variables:", mutationVariables);
        logger.info("Mutation returned:", returnedData);

        // ... your custom logic here
      }
    );

### Python

    from firebase_functions import dataconnect_fn, logger

    @dataconnect_fn.on_mutation_executed(
      service="myAppService",
      connector="users",
      operation="CreateUser"
    ):
    def process_new_user_data(event: dataconnect_fn.Event):
      # The variables passed to the mutation
      mutation_vars = event.data.payload.variables
      # The data returned by the mutation
      returned_data = event.data.payload.data

      logger.info("Processing mutation with variables:", mutationVariables)
      logger.info("Mutation returned", returnedData)

      # ... your custom logic here

Note that unlike some other database triggers, such as Cloud Firestore or
Realtime Database, the Data Connect event does not provide a "before"
snapshot of the data. Because Data Connect proxies requests to the
underlying database, the "before" snapshot of the data cannot be obtained
transactionally. Instead, you have access to the arguments sent to the mutation
and the data that was returned by it.

One consequence of this is that you cannot use the strategy of comparing
"before" and "after" snapshots to avoid infinite loops, in which an event
trigger triggers the same event. If you must perform a mutation from a function
triggered by a mutation event, make use of event filters and take care to ensure
that no mutation can ever trigger itself, even indirectly.