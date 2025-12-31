# Source: https://flatfile.com/docs/core-concepts/listeners.md

# Events and Listeners

> The anatomy of Events and Listeners - core components of the Flatfile Platform

## Events

Flatfile publishes an [Event](/core-concepts/listeners#events) whenever something happens - editing a Record, uploading a file, clicking an Action button. Events carry structured information about what occurred, including the context and any relevant data.

Each Event includes a domain, topic, context, and optional payload:

| Component          | Description                                       | Example                                                 |
| ------------------ | ------------------------------------------------- | ------------------------------------------------------- |
| Domain             | the jurisdiction of the Event                     | Record, Sheet, Workbook, Space, file, Job, Agent        |
| Topic              | a combination of a domain and an action           | Workbook:created Workbook:updated Workbook:deleted      |
| Context            | detailed information about context of the Event   | `{ spaceId: "us_sp_1234", fileId: "us_fl_1234", ... }`  |
| Payload (optional) | detailed information about execution of the Event | `{ status: "complete", workbookId: "us_wb_1234", ... }` |

For a complete list of Events published by Flatfile, see [Events Reference](/reference/events).

## Listeners

Listeners are functions you write that respond to Events by executing custom code. They enable all the powerful functionality in your Flatfile implementation: data transformations, validations, integrations, and workflows. Listeners define how your [Spaces](/core-concepts/spaces) behave and what happens when users interact with your data.

Listeners can run locally during development or be deployed as [Agents](/core-concepts/listeners#agents) to Flatfile's cloud. Each Listener connects to a specific [Environment](/core-concepts/environments) using that Environment's API keys as environment variables. To switch between different Environments (or promote a development Environment to production), you simply update your environment variables with the corresponding API keys.

By default, Listeners respond to Events from all [Apps](/core-concepts/apps) within an [Environment](/core-concepts/environments). You can use [Namespaces](/guides/namespaces-and-filters#namespaces) to partition your Listeners into isolated functions that only respond to Events from specific Apps.

## How Listeners Work

A Listener receives Events as they occur and executes a callback function in response. For example, when a file is uploaded, a Listener can mount an [Action](/core-concepts/actions) buton to the file for performing data transformations, or when a [Record](/core-concepts/records) is created, a Listener can validate the data.

The callback function can be as simple as logging the Event or as advanced as integrating with external systems. Here is an example that logs the topic of any incoming Event:

<Warning>
  **Note:** The `**` wildcard is a catch-all that will match all Events. This is useful for testing, but should be avoided in production as it can lead to performance issues.
</Warning>

<CodeGroup>
  ```javascript JavaScript
  export default function (listener) {
    listener.on("**", (event) => {
      console.log(`Received event: ${event.topic}`);
    });
  }
  ```

  For a more concrete and practical example, follow along with our [Coding Tutorial](/coding-tutorial).

  ```typescript TypeScript
  import { FlatfileListener, FlatfileEvent } from '@flatfile/listener';

  export default function (listener: FlatfileListener) {
    listener.on("**", (event: FlatfileEvent) => {
      console.log(`Received event: ${event.topic}`);
    });
  }
  ```
</CodeGroup>

## Listener Methods

Flatfile provides two primary methods for configuring listener behavior:

### `listener.on()`

The `listener.on()` method is the fundamental pattern for responding to specific events. This method allows you to provide a callback function that will be executed when the specified event occurs.

For a complete list of Events published by Flatfile, see [Events Reference](/reference/events).

**Type Signature:**

```typescript
listener.on(
  eventPattern: string, 
  callback: (event: FlatfileEvent) => void | Promise<void>
): void

listener.on(
  eventPattern: string, 
  filter: object, 
  callback: (event: FlatfileEvent) => void | Promise<void>
): void
```

**Examples:**

<CodeGroup>
  ```javascript JavaScript
  // Basic Event handling
  listener.on('file:created', async (event) => {
    console.log(`New file uploaded: ${event.context.fileId}`);
  });

  // Event handling with filters
  listener.on('commit:created', { sheet: 'contacts' }, async (event) => {
    console.log('Processing contact data commit...');
    // Process contact data
  });

  // Job handling
  listener.on('job:ready', { job: 'space:configure' }, async (event) => {
    console.log('Configuring Space...');
    // Configure Space
  });
  ```

  ```typescript TypeScript
  import { FlatfileEvent } from '@flatfile/listener';

  // Basic Event handling with proper typing
  listener.on('file:created', async (event: FlatfileEvent) => {
    console.log(`New file uploaded: ${event.context.fileId}`);
  });

  // Event handling with filters
  listener.on('commit:created', { sheet: 'contacts' }, async (event: FlatfileEvent) => {
    console.log('Processing contact data commit...');
    // Process contact data
  });
  ```
</CodeGroup>

### `listener.use()`

The `listener.use()` method is for building and distributing listener functions in a modular manner. It allows you to send your own Listener functions as a callback to the method, each of which receives a `FlatfileListener` instance as their argument.

Inside that callback function, you can use `listener.on()` to register Event handlers or introduce various [Plugins](/core-concepts/plugins) to your listener. The result can be an `index` file with with little more than `listener.use()` calls, each of which distributes your listener function to other places in your codebase:

<CodeGroup>
  ```javascript JavaScript
  // import statements

  export default function (listener) {
    // Distribute listener functions to different modules
    listener.use(validateCustomerData);
    listener.use(processFileUploads);
    listener.use(handleDataTransforms);
    listener.use(setupIntegrations);
  }
  ```

  ```typescript TypeScript
  // import statements

  export default function (listener: FlatfileListener): void {
    // Distribute listener functions to different modules
    listener.use(validateCustomerData);
    listener.use(processFileUploads);
    listener.use(handleDataTransforms);
    listener.use(setupIntegrations);
  }
  ```
</CodeGroup>

This works particularly well for complex listener functions that need to be broken down into smaller, more manageable pieces.

It also works well when combined with [Namespaces](/guides/namespaces-and-filters) to create isolated listener functions that only respond to Events from a specific namespace.

You'll find this pattern often when using [Plugins](/core-concepts/plugins) to extend the functionality of your listener.

**Type Signature:**

```typescript
listener.use(configFunction: (listener: FlatfileListener) => void): void
```

**Examples:**

<CodeGroup>
  ```javascript JavaScript
  // Custom configuration function
  function validateCustomerData(listener) {
    listener.on('commit:created', { sheet: 'customers' }, async (event) => {
      // Validation logic here
      console.log('Validating customer data...');
    });
    
    listener.on('record:updated', { sheet: 'customers' }, async (event) => {
      // Update validation logic here
      console.log('Revalidating updated customer data...');
    });
  }

  // Another configuration function
  function setupDataProcessing(listener) {
    listener.on('file:created', async (event) => {
      console.log('Processing uploaded file...');
    });
  }

  export default function (listener) {
    listener.use(validateCustomerData);
    listener.use(setupDataProcessing);
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener, FlatfileEvent } from '@flatfile/listener';

  // Custom configuration function with proper typing
  function validateCustomerData(listener: FlatfileListener): void {
    listener.on('commit:created', { sheet: 'customers' }, async (event: FlatfileEvent) => {
      // Validation logic here
      console.log('Validating customer data...');
    });
    
    listener.on('record:updated', { sheet: 'customers' }, async (event: FlatfileEvent) => {
      // Update validation logic here
      console.log('Revalidating updated customer data...');
    });
  }

  // Another configuration function
  function setupDataProcessing(listener: FlatfileListener): void {
    listener.on('file:created', async (event: FlatfileEvent) => {
      console.log('Processing uploaded file...');
    });
  }

  export default function (listener: FlatfileListener): void {
    listener.use(validateCustomerData);
    listener.use(setupDataProcessing);
  }
  ```
</CodeGroup>

### When to Use Each Method

| Method           | Use For                                                            |
| ---------------- | ------------------------------------------------------------------ |
| `listener.use()` | Creating reusable functions, organizing complex logic into modules |
| `listener.on()`  | Responding to specific Events, implementing direct Event handlers  |

## Event Routing with Namespaces & Filters

There are two more Listener methods to note, specifically intended for routing events to specific Listener functions: `listener.namespace()` and `listener.filter()`.

**Namespaces** provide architectural boundaries for organizing different parts of your application at the App, Space, and Workbook level:

* `space:customer-portal` - Events from Spaces in the "customer-portal" App
* `workbook:staging` - Events from Workbooks with "staging" namespace

**Event filters** enable granular event targeting based on property values, event types, and conditions:

* `{ sheet: 'contacts' }` - Events from the "contacts" Sheet
* `{ domain: 'job', 'payload.job': 'space:configure' }` - Space configuration Jobs

For comprehensive examples, patterns, and detailed configuration options, see our [Namespaces and Filters guide](/guides/namespaces-and-filters).

**Usage Examples:**

<CodeGroup>
  ```javascript JavaScript
  export default function (listener) {
    // Use namespaces for architectural organization
    listener.namespace('space:customer-portal', (customerListener) => {
      customerListener.on('commit:created', async (event) => {
        console.log('Processing customer portal data...');
      });
    });

    // Use filters for granular targeting
    listener.filter({ sheet: 'contacts' }, (contactsListener) => {
      contactsListener.on('commit:created', async (event) => {
        console.log('Contact data committed');
      });
    });

    // Combine both for maximum precision
    listener.namespace('space:customer-portal', (customerListener) => {
      customerListener.filter({ sheet: 'enterprise-customers' }, (enterpriseListener) => {
        enterpriseListener.on('commit:created', async (event) => {
          console.log('Processing enterprise customer data');
        });
      });
    });
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener, FlatfileEvent } from '@flatfile/listener';

  export default function (listener: FlatfileListener): void {
    // Use namespaces for architectural organization
    listener.namespace('space:customer-portal', (customerListener: FlatfileListener) => {
      customerListener.on('commit:created', async (event: FlatfileEvent) => {
        console.log('Processing customer portal data...');
      });
    });

    // Use filters for granular targeting
    listener.filter({ sheet: 'contacts' }, (contactsListener: FlatfileListener) => {
      contactsListener.on('commit:created', async (event: FlatfileEvent) => {
        console.log('Contact data committed');
      });
    });

    // Combine both for maximum precision
    listener.namespace('space:customer-portal', (customerListener: FlatfileListener) => {
      customerListener.filter({ sheet: 'enterprise-customers' }, (enterpriseListener: FlatfileListener) => {
        enterpriseListener.on('commit:created', async (event: FlatfileEvent) => {
          console.log('Processing enterprise customer data');
        });
      });
    });
  }
  ```
</CodeGroup>

## Agents

In Flatfile, an **Agent** refers to a server-side listener bundled and deployed to Flatfile to be hosted in our secure cloud. You may deploy multiple Agents to a single Environment, each with its own configurations and codebase. But be careful, as multiple Agents can interfere with each other if not properly managed.

<Note>
  Terminology note: **Agents** in Flatfile should not be confused with **AI Agents**. Flatfile Agents are Event Listeners running in Flatfile's cloud infrastructure, whereas AI Agents refer to a semi-autonomous Artificial Intelligence system.
</Note>

### Agent Deployment

To deploy an Agent, run the following command in your terminal from the root directory containing your listener file:

```bash
npx flatfile@latest deploy
```

The CLI will automatically examine your listener code and register itself to listen to only the Events your listener is configured to handle.

#### Deployment Options

**Unique Slug**: Use the `-s` flag to give your Agent a unique slug. This is useful when managing multiple Agents in the same Environment.

```bash
npx flatfile@latest deploy -s my-custom-agent
```

**Multiple Agents**: You may deploy multiple Agents to a single Environment, each with its own configurations and codebase. However, be careful as multiple Agents can interfere with each other if not properly managed (see the next section).

If no slug is provided:

* **Single Agent**: Your Agent will be updated and given a slug of `default`
* **Multiple Agents**: The CLI will prompt you to select which Agent to update

### Managing Multiple Agents

When deploying multiple Agents to the same Environment, careful management is essential to prevent race conditions and conflicts. Multiple Agents listening to the same Event topics can interfere with each other and cause unpredictable behavior.

We recommend combining your code into a single codebase and using [Namespaces and Filters](/guides/namespaces-and-filters) to route events to scoped listeners, ideally organized into separate subdirectories. However, if you need multiple Agents, follow these strategies to avoid conflicts:

#### Conflict Prevention Strategies

1. **Use Namespaces and Filters**: Ensure each Agent listens to distinct Event patterns
2. **Segment by Domain**: Separate Agents by functional areas (e.g., data processing vs. integrations) and separate your accout into different [Apps](/core-concepts/apps)
3. **Avoid Topic Overlap**: Never have multiple Agents handling the same Event topics without proper routing

### Agent Configuration

When deploying an Agent, the CLI will automatically reduce the topic scope your Agent listens to by examining your listener code and registering itself to listen to only the topics your listener is configured to act on.

For example if your listener code only listens to `commit:created` Events, the CLI will automatically configure the Agent to only listen to `commit:created` Events. If your listener has a wildcard listener `**`, the CLI will configure the Agent to listen to all Events.

### Agent Logs

When using Flatfile's secure cloud to host your listener, you can view the executions of your Agent in the "Event Logs" tab of your dashboard.

Event logs are useful in monitoring and troubleshooting your listener. Each execution of your agent is recorded here, including any custom console logs you have configured in your listener code.

<Info>If you are running your Agent locally using the `develop` command to test, these logs will not be recorded in your dashboard. You can still view them in your terminal.</Info>

#### Failures

Failures occur when an Agent fails to execute properly. That means either an uncaught error is thrown, or the execution times out.

If you are catching and handling errors within your code, those executions will not be marked as failures. If you would prefer to see them marked this way, re-throw your error after handling to bubble it up to the execution handler.

<CodeGroup>
  ```javascript JavaScript
  export default function (listener) {
    //note: listening to all Events with a wildcard can be used while testing but is not
    //recommended for production, as it will capture all Events and may cause performance issues
    listener.on("**", (event) => {
      try {
        // do something
      } catch (error) {
        // handle error
        throw error; // re-throw error to mark execution as failure
      }
    });
  }
  ```

  ```typescript TypeScript
  import { FlatfileListener, FlatfileEvent } from '@flatfile/listener';

  export default function (listener: FlatfileListener) {
    //note: listening to all Events with a wildcard can be used while testing but is not
    //recommended for production, as it will capture all Events and may cause performance issues
    listener.on("**", (event: FlatfileEvent) => {
      try {
        // do something
      } catch (error) {
        // handle error
        throw error; // re-throw error to mark execution as failure
      }
    });
  }
  ```
</CodeGroup>
