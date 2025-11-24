# Source: https://flatfile.com/docs/core-concepts/jobs.md

# Jobs

> Discrete tasks executed asynchronously in response to events

In Flatfile, a Job represents a large unit of work performed asynchronously on a resource such as a file, [Workbook](/core-concepts/workbooks), or [Sheet](/core-concepts/sheets). The Jobs workflow provides visibility into the status and progress of your Jobs, allowing you to monitor and troubleshoot the data processing pipeline. For handling large datasets, see our [multi-part jobs guide](/guides/multi-part-jobs).

<Note>
  In these examples, we'll show the full Job Listener lifecycle implementation, complete with `ack` to acknowledge the job, `update` to update the job's progress, and `complete` or `fail` to complete or fail the job.

  To make this simpler, we provide a plugin called [Job Handler](/plugins/job-handler) that handles the job lifecycle for you. This plugin works by listening to the `job:ready` event and executing the handler callback. There is also an optional `tick` function which allows you to update the Job's progress.

  For example, this listener implementation contains all the code necessary to handle a job:

  ```typescript
  listener.use(jobHandler("workbook:export", async ({ context: { fileId, jobId } }, tick) => {
    const file = await api.files.get(fileId);
    tick(10, "Getting started.");
    // export logic here
    tick(90, "Exported.");
    return {
      outcome: {
        message: "Exporting file contents is complete.",
      }
    }
  }));
  ```
</Note>

## Job Lifecycle

### Lifecycle Events

Jobs fire the following Events during their lifecycle. In chronological order, the Job Events are:

| Event                           | Description                                                                                                                                                                        |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `job:created`                   | Fires when a Job is created, but before it does anything.                                                                                                                          |
| `job:ready`                     | Fires when a Job is ready to move into the execution stage, but before it does anything.                                                                                           |
| `job:updated`                   | Fires when there is an update to a Job while it is executing.                                                                                                                      |
| `job:completed` OR `job:failed` | `job:completed` fires when a Job is completed successfully, `job:failed` fires if a Job is completed but fails. One of these events will fire upon Job completion, but never both. |
| `job:outcome-acknowledged`      | Fires when a user acknowledges the completion of a Job through a UI popup.                                                                                                         |

You can listen on any of these events in your [Listener](/core-concepts/listeners), but the most common event to listen for is `job:ready`.

## Types of Jobs

Jobs can be triggered in a number of ways, most commonly in response to user activity. Jobs are then managed via [Listeners](/core-concepts/listeners), which receive [Events](/core-concepts/listeners#events) published by Flatfile in response to activity.

There are three types of Jobs on the Flatfile Platform:

### Action-Based Jobs

Actions are developer-defined operations that can be mounted on a number of domains (including Sheets, Workbooks, Documents, and Files). Mounting an Action means attaching a custom operation to that domain. That operation can then be triggered by a user event (clicking a button or selecting a menu item).

<Note>
  When an Action is triggered a `job:ready` Event for a Job named `[domain]:[operation]` is published. Your [Listener](/core-concepts/listeners) can then be configured to respond to that Action via its Event.
</Note>

To run an Action based job, two configurations are necessary.

First, create an [Action](/core-concepts/actions) on a domain. Here's an example of a Workbook containing an Action:

```typescript
api.workbook.create({
  name: "October Report Workbook",
  actions: [
    {
      label: "Export Data",
      description: "Send data to destination system",
      operation: "export",
      type: "file",
    },
  ],
});
```

Then, create a [Listener](/core-concepts/listeners) to respond to the Action. This listener should listen for the `job:ready` event, filtered by the `domain:operation` Job - where, in this case, `workbook` is the domain, `export` is the operation.

```typescript
listener.on(
  "job:ready",
  { job: "workbook:export" },
  async ({ context: { jobId } }) => {
    try {
      await api.jobs.ack(jobId, {
        info: "Starting submit job...",
        progress: 10,
      });

      // Custom code here

      await api.jobs.complete(jobId, {
        outcome: {
          message: "Submit Job was completed successfully.",
        },
      });
    } catch (error) {
      await api.jobs.fail(jobId, {
        outcome: {
          message: "This Job failed.",
        },
      });
    }
  }
);
```

### Custom Jobs

Another trigger option is to create a Custom Job via SDK/API. In the SDK, Jobs are created by calling the `api.jobs.create()` method.

Creating a custom Job in your Listener enables any Event to trigger a Job.

Here's an example of creating a custom Job in a Listener:

```typescript
listener.on(
  "commit:created",
  { sheet: "contacts" },
  async ({ context: { workbookId, sheetId } }) => {

    const { data } = await api.jobs.create({
      type: "workbook",
      operation: "myCustomOperation",
      trigger: "immediate",
      source: workbookId
    });
    
  }
);
```

Note that the trigger for this Listener is set to immediate, which means that the Job will be created and executed immediately upon the Event firing.

Therefore, we should have our Listener ready to respond to this Job:

```typescript
listener.on(
  "job:ready",
  { job: "workbook:myCustomOperation" },
  async ({ context: { jobId, workbookId } }) => {
    try {
      await api.jobs.ack(jobId, {
        info: "Starting my custom operation.",
        progress: 10,
      });

      // Custom code here.

      await api.jobs.complete(jobId, {
        outcome: {
          message: "Successfully completed my custom operation.",
        },
      });
    } catch {
      await api.jobs.fail(jobId, {
        outcome: {
          message: "Custom operation failed.",
        },
      });
    }
  }
);
```

### System Jobs

Internally, Flatfile uses Jobs to power many of the features of the Flatfile Platform, such as extraction, record mutation, and AI Assist. Here are some examples of Jobs that the Flatfile Platform creates and manages on your behalf:

| Job Name        | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| `Extract`       | Extracts data from the specified source.                      |
| `Map`           | Maps data from its ingress format to Blueprint fields.        |
| `DeleteRecords` | Deletes records from a dataset based on specified criteria.   |
| `Export`        | Exports data to a specified format or destination.            |
| `MutateRecords` | Alters records in a dataset according to defined rules.       |
| `Configure`     | Sets up or modifies the configuration of a Space.             |
| `AiAssist`      | Utilizes AI to assist with tasks such as data categorization. |
| `FindReplace`   | Searches for specific values and replaces them.               |

## Job Parameters

### Required Parameters

When creating a job, the following parameters are required:

* **type** (string) - Workbook, File, Sheet, Space
* **operation** (string) - `export`, `extract`, `map`, `delete`, etc
* **source** (string) - The id of the data source (FileId, WorkbookId, or SheetId)

### Optional Parameters

* **trigger** (string) - `manual` or `immediate`
* **destination** (string) - The id of the data target (if any)
* **status** (string) - `created`, `planning`, `scheduled`, `ready`, `executing`, `complete`, `failed`, `cancelled`
* **progress** (number) - A numerical or percentage value indicating the completion status of the Job
* **estimatedCompletionAt** (date) - An estimated completion time. The UI will display the estimated processing time in the foreground Job overlay
* **info** (string) - Additional information regarding the Job's current status
* **managed** (string) - Indicates whether the Job is managed by the Flatfile platform or not
* **mode** (string) - `foreground`, `background`, `toolbarBlocking`
* **metadata** (object) - Additional metadata for the Job. You can store any additional information here, such as the IDs of Documents or Sheets created during the execution of Job

Please see our [API Reference](https://reference.flatfile.com/api-reference/jobs/) for details on all possible values.

## Working with Jobs

Jobs can be managed via SDK/API. Commonly, Jobs are acknowledged, progressed, and then completed or failed. Here's a look at those steps.

### Acknowledging Jobs

First, acknowledge a Job. This will update the Job's status to `executing`.

```typescript
await api.jobs.ack(jobId, {
  info: "Starting submit job...",
  progress: 10,
});
```

### Updating Job Progress

Once a Job is acknowledged, you can begin running your custom operation. Jobs were designed to handle large processing loads, but you can easily update your user by updating the Job with a progress value.

```typescript
await api.jobs.update(jobId, {
  progress: 50,
  estimatedCompletionAt: new Date("Tue Aug 23 2023 16:19:42 GMT-0700"),
});
```

`Progress` is a numerical or percentage value indicating the completion status of the work. You may also provide an `estimatedCompletionAt` value which will display your estimate of the remaining processing time in the foreground Job overlay. Additionally, the Jobs Panel will share visibility into the estimated remaining time for acknowledged jobs.

<Frame caption="Example of estimated time">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/core-concepts/assets/estimatedtime_actions.png" width="610" />
</Frame>

### Completing Jobs

Once a job is complete, you can display an alert to the end user using `outcome`.

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was completed successfully. ${myData.length} records were processed.`,
    acknowledge: true,
  },
});
```

### Job Outcomes

You can enhance job completion with various outcome options to guide users to their next action:

<Frame caption="Example of a 'next' button">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/core-concepts/assets/goto_google.png" width="610" />
</Frame>

#### Internal Navigation

Add a button to the dialog that will redirect the user somewhere within a Space using next > Id.

In this code below, we will create a button that says "See all downloads" with this path: space/us\_sp\_1234/files?mode=export

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was completed successfully. ${myData.length} records were processed.`,
    acknowledge: true,
    next: {
      type: "id",
      id: "dev_sp_1234",
      path: "files",
      query: "mode=export",
      label: "See all downloads",
    },
  },
});
```

#### External Links

Add a button to the dialog that will redirect the user to an external link using next > Url.

In this code below, we will create a button that says "Go to Google". It will open in a new tab.

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was completed successfully. ${myData.length} records were processed.`,
    acknowledge: true,
    next: {
      type: "url",
      url: "http://www.google.com",
      label: "Go to Google",
    },
  },
});
```

#### File Downloads

Add a button to the dialog that will redirect the user to an external link using next > Url.

In this code below, we will create a button that says "Download this file".

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was completed successfully. ${myData.length} records were processed.`,
    acknowledge: true,
    next: {
      type: "download",
      fileName: "DownloadedFromFlatfile.csv",
      url: "source_of_file.csv",
      label: "Download this file",
    },
  },
});
```

#### Multiple File Downloads

Download files hosted on Flatfile by using next > files.

In this code below, we will create a button that says "Download files".

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `The files should download automatically`,
    next: {
      type: "files",
      label: "Download files",
      files: [{fileId: "us_fl_123"}],
    },
  },
});
```

#### Snapshots

Add a button to the dialog that will redirect the user a particular snapshot using next > snapshot.

In this code below, we will create a button that says "Go to Snapshot".

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was completed successfully.`,
    acknowledge: true,
    next: {
      type: "snapshot",
      label: "Go to Snapshot",
      snapshotId: snapshot.id,
      sheetId: sheet.id
    },
  },
});
```

#### View Management

Dynamically update visible columns in a sheet using next > view.

In this code below, we will create a button that says "Hide columns":

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was completed on sheet ${sheet.name}`,
    acknowledge: true,
    next: {
      type: "view",
      label: "Hide columns",
      sheetId: sheet.id,
      hiddenColumns: ['age', 'phone', 'middleName'] // field keys to hide
    },
  },
});
```

#### Retry Actions

Often in the event of a failure, you may want to add a button to the dialog that will retry the Job using next > Retry.

Provide retry functionality for failed jobs:

```typescript
await api.jobs.complete(jobId, {
  outcome: {
    message: `Operation was not completed successfully. No records were processed.`,
    acknowledge: true,
    next: {
      type: "retry",
      label: "Try again",
    },
  },
});
```

### Failing Jobs

When a job encounters an error, use the fail method:

```typescript
await api.jobs.fail(jobId, {
  outcome: {
    message: "This Job failed due to an error.",
    acknowledge: true,
  },
});
```
