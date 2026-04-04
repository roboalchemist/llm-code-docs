# Source: https://flatfile.com/docs/guides/using-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Actions

> Trigger custom operations based on user input

An Action is a code-based operation that runs where that Action is mounted. Actions run when a user clicks the corresponding user prompt in Flatfile.

## Overview

When an Action is triggered, it creates a [Job](/core-concepts/jobs) that your application can listen for and respond to.

Given that Actions are powered by Jobs, the [Jobs Lifecycle](/core-concepts/jobs#jobs-lifecycle) pertains to Actions as well. This means that you can [update progress values/messages](/core-concepts/jobs#updating-job-progress) while an Action is processing, and when it's done you can provide an [Outcome](/core-concepts/jobs#job-outcomes), which allows you to show a success message, automatically [download a generated file](/core-concepts/jobs#file-downloads), or [forward the user](/core-concepts/jobs#internal-navigation) to a generated Document.

[Actions](/core-concepts/actions) are mounted on resources like **Workbooks**, **Sheets**, **Fields**, **Documents**, and **Files**.

Generally, [Workbook](#workbook-actions), [Sheet](#sheet-actions), [Field](#field-actions), and [Document](#document-actions) Actions are configured within a Blueprint object, while [File](#file-actions) Actions are appended to the file during the upload process. Alternatively, Actions can be mounted to any of these resources via API in a [Listener](/core-concepts/listeners).

[Sheet](#sheet-actions) Actions can be executed on the entire Sheet, for a filtered view of the Sheet, or selectively for the chosen records. See [Sheet Action Execution Modes](#sheet-action-execution-modes) for details on how actions handle different data selections.

<Note>
  In these examples, we'll show the full Job Listener lifecycle implementation, complete with `ack` to acknowledge the job, `update` to update the job's progress, and `complete` or `fail` to complete or fail the job.

  To make this simpler in practice, we provide a plugin called [Job Handler](/plugins/job-handler) that handles the job lifecycle for you. This plugin works by listening to the `job:ready` event and executing the handler callback, even catching errors to fail the job. There is also an optional `tick` function which allows you to update the Job's progress.

  For example: With the [Job Handler](/plugins/job-handler) plugin, the 35-line [File Action Listener](#listener-implementation-4) defined below would be implemented simply as:

  ```typescript  theme={null}
  listener.use(jobHandler("file:logFileContents", async ({ context: { fileId, jobId } }, tick) => {
    const file = await api.files.get(fileId);
    tick(10, "Getting started.");
    console.log({ file });
    tick(90, "Logged.");
    return {
      outcome: {
        message: "Logging file contents is complete.",
      }
    }
  }));
  ```
</Note>

## Workbook Actions

<Frame caption="Two Workbook Actions: A primary action (Submit to API) and a secondary action (Download XML)">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c18065d33049e87c68609265d6bb4d5a" width="610" data-og-width="2108" data-og-height="1054" data-path="guides/assets/workbook-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ffb1e05162f48c85c312f253f0e711c7 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=998a004f172bca7d941f323a19edba8f 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=0f7fb545bcfee06fb17d5b8b21e6b8ee 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=6b03b918e5d3e93b0f3a8ac3d98468c2 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=3ad7999bf436dfce83a272842167fff2 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/workbook-actions.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=f5b0bdb5978115d3bd01af9d9e27d34a 2500w" />
</Frame>

Once a user has extracted and mapped data into a Workbook, it may be more efficient to run an operation on the entire dataset rather than making atomic transformations at the record- or field-level.

For example:

* Sending a webhook that notifies your API of the data's readiness
* Populating a Sheet with data from another source
* Adding two different fields together after a user review's initial validation checks
* Moving valid data from an editable Sheet to a read-only Sheet

Workbook-mounted actions are represented as buttons in the top right of the Workbook.

### Usage

If you configure `primary: true` on an Action, its button will be highlighted in the Workbook.

If you configure `trackChanges: true`, it will disable your actions until all commits are complete (usually data hooks).

#### Blueprint Configuration

First, configure your action in your Blueprint:

```javascript  theme={null}
// Add this to your workbook configuration
actions: [
  {
    operation: "downloadXML",
    mode: "background",
    label: "Download XML",
    type: "string",
    description: "Generates and downloads an XML file with all the users in the workbook",
    primary: false,
  },
  {
    operation: "submitToAPI",
    mode: "background",
    label: "Submit to API",
    type: "string",
    description: "Submits the users to our API",
    primary: true,
  },
],
settings: {
  trackChanges: true,
}
```

#### Listener Implementation

Next, create a listener to handle the `job:ready` event for your action.

```typescript  theme={null}
listener.on(
  "job:ready",
  { job: "workbook:submitToAPI" },
  async (event) => {
    const { jobId, workbookId } = event.context;
    const { data: workbook } = await api.workbooks.get(workbookId);
    const { data: workbookSheets } = await api.sheets.list({ workbookId });
    
    // Collect all sheet data
    const sheets = [];
    for (const [_, element] of workbookSheets.entries()) {
      const { data: records } = await api.records.get(element.id);
      sheets.push({
        ...element,
        ...records,
      });
    }
    
    try {
      // Acknowledge the job start
      await api.jobs.ack(jobId, {
        info: "Starting job to submit action to webhook",
        progress: 10,
      });
      
      // Replace with your actual webhook URL
      const webhookReceiver = "https://your-app.com/webhook/flatfile";
      
      // Submit data to external system
      const response = await fetch(webhookReceiver, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          workbook: {
            ...workbook,
            sheets,
          },
        }),
      });
      
      if (response.status === 200) {
        await api.jobs.complete(jobId, {
          outcome: {
            message: `Data was successfully submitted to ${webhookReceiver}.`,
          },
        });
      } else {
        throw new Error("Failed to submit data to webhook");
      }
    } catch (error) {
      console.error(error);
      await api.jobs.fail(jobId, {
        outcome: {
          message: "This job failed. Check your webhook URL and try again.",
        },
      });
    }
  }
);
```

## Sheet Actions

<Frame caption="Two Sheet Actions: A primary action (Populate...) and a secondary action (Validate...)">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=5675d4fcdc21753bc8aec0419f322b5b" width="610" data-og-width="2112" data-og-height="1056" data-path="guides/assets/sheet-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=42047c37a4be2cce25560774055926cd 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=bbdd78cf502b06169cfc0a7f866a17bd 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=08f9c4b38d863512e2445aae6b816a60 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c35579fe871b8c89cc429a5d348ee852 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=fe0284b2cc739fac865ef69b22b0566d 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/sheet-actions.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a744fd95ec947d681451b3f9819e0ffc 2500w" />
</Frame>

Each Sheet has built-in Actions like download.

Sheet-mounted actions are represented as a dropdown in the toolbar of the Sheet.

### Usage

If you configure `primary: true` on an Action, it creates a top-level button as well as placing it in the dropdown menu.

#### Blueprint Configuration

First, configure your action on your Blueprint. Add the action configuration to your sheet definition:

```javascript  theme={null}
sheets : [
  {
    name: "Users",
    actions: [
      {
        operation: "populateHealthScores",
        mode: "background",
        label: "Populate Health Scores",
        type: "string",
        description: "Populate health scores for all users",
        primary: true,
      },
      {
        operation: "validateHealthScores",
        mode: "background",
        label: "Validate Health Scores",
        type: "string",
        description: "Validate health scores for all users",
        primary: false,
      },
    ]
  }
]
```

#### Listener Implementation

Next, listen for a `job:ready` and filter on the `domain` (sheet) and the `operation` of where the action was placed. Be sure to complete the job when it's done.

```typescript  theme={null}
listener.on(
  "job:ready",
  { job: "sheet:populateHealthScores" },
  async ({ context: { jobId } }) => {
    try {
      await api.jobs.ack(jobId, {
        info: "Populating health scores...",
        progress: 10,
        estimatedCompletionAt: new Date("Tue Aug 23 2023 16:19:42 GMT-0700"),
      });

      // Populate health scores for all users
      // Implementation logic here

      await api.jobs.complete(jobId, {
        info: "Health scores populated successfully.",
      });
    } catch (error) {
      console.error("Error:", error.stack);

      await api.jobs.fail(jobId, {
        info: "Failed to populate health scores.",
      });
    }
  }
);
```

### Sheet Action Execution Modes

Sheet Actions are powerful because they can operate on different subsets of data within a sheet. When a Sheet Action is triggered, it automatically receives context about what data should be processed based on the user's current view and selections.

#### How Sheet Actions Handle Data Context

When a Sheet Action job is created, it receives a `query` object in the job's subject that specifies which records to process:

```javascript  theme={null}
// Job subject structure for Sheet Actions
{
  type: "collection", 
  resource: string,              // Usually sheetId or "records" 
  query: {
    filter: "valid" | "error" | "all" | "none",  // Filter type
    filterField: string,         // Field to filter on (optional)
    searchField: string,         // Field to search in (optional)  
    searchValue: string,         // Search term (optional)
    q: string,                   // FFQL (Flatfile Query Language) query (optional)
    ids: string[]               // Record IDs - INCLUDE when no filter, EXCLUDE when filter applied
  },
  params: {
    sheetId: string,            // Always present for sheet actions
    // Additional params depending on action type
  }
}
```

#### Three Execution Contexts

**1. Entire Sheet (No Filter, No Selection)**

* Processes all records in the sheet
* `query.filter` is `"all"` or undefined
* No `ids` or `exceptions` arrays

**2. Filtered View**

* Processes only records matching the current filter
* `query.filter` indicates the filter type:
  * `"valid"` - Only valid records (no errors)
  * `"error"` - Only records with validation errors
  * Custom filters if applied
* May include search parameters if user has searched
* May include [FFQL queries](/reference/ffql) via the `q` parameter for advanced filtering

**3. Selected Records**

* Processes only user-selected records
* **When no other filters applied**: `query.ids` contains specific record IDs to INCLUDE
* **When filters are applied**: `query.ids` contains record IDs to EXCLUDE from the filtered results

#### Implementation Example

```typescript  theme={null}
listener.on(
  "job:ready", 
  { job: "sheet:processData" },
  async (event) => {
    const { jobId, sheetId } = event.context;
    
    // Get the job to access the query context
    const { data: job } = await api.jobs.get(jobId);
    const query = job.subject?.query || {};
    
    // Pass the query directly to the records API
    // The API handles the inclusion/exclusion logic for ids based on filters
    const { data: records } = await api.records.get(sheetId, {
      ...query  // Includes filter, ids, searchField, searchValue, etc.
    });
    
    console.log(`Processing ${records.length} records`);
    console.log(`Query context:`, query);
    
    // Process the records
    for (const record of records) {
      // Your processing logic here...
    }
    
    await api.jobs.complete(jobId, {
      outcome: {
        message: `Successfully processed ${records.length} records`,
      },
    });
  }
);
```

#### Built-in Action Examples

Built-in actions like Delete and Download demonstrate these execution modes:

* **Delete All** - Removes all records when no selection/filter
* **Delete Selected** - Removes only selected records
* **Delete Valid/Invalid** - Removes records matching the current filter
* **Download Filtered** - Exports only records matching current view

Your custom Sheet Actions automatically inherit this same context-aware behavior.

## Field Actions

<Frame caption="Example Field Action dropdown in column header (Capitalize All Values)">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=d47f0d582aac6342d83901fe12047f05" width="610" data-og-width="1448" data-og-height="838" data-path="guides/assets/field-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a0a677d4a4f4adb27f0fc38a5b553930 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ad6a5f4c81c1a41ac70cb2c5f00385d9 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=5c000d3285292113dfd56615eacf6356 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=57364c7f0b738d5ca8a35a957b1fdb7a 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=d201a86cac558102b80d3a552c09a7b5 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/field-action.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=f2495595a29bdb75bb03c7d234343de9 2500w" />
</Frame>

Field-mounted actions are operations that can be performed on individual columns/fields within a Sheet. They appear as options in the dropdown menu when you click on a column header.

Field actions are particularly useful for:

* Column-specific data transformations (e.g., capitalizing all values in a name field)
* Field-level validation operations
* Data formatting specific to a column type
* Column-specific cleanup operations

### Usage

The `primary` property does not affect the UI for Field actions.

<Note>
  Note: Field Actions are essentially an extension of Sheet actions - therefore their operation names are prefixed with `sheet:`, and the column key is available in the job data.
</Note>

#### Blueprint Configuration

First, configure your field action in your Blueprint by adding it to the field definition:

```javascript  theme={null}
// Add this to your field configuration within a sheet
{
  key: "firstName",
  type: "string",
  label: "First Name",
  description: "Customer's first name",
  actions: [
    {
      operation: "capitalize",
      mode: "foreground",
      label: "Capitalize All Values",
      description: "Capitalizes the values of the selected column",
    }
  ]
}
```

#### Listener Implementation

Next, create a listener to handle the `job:ready` event for your field action. Field actions use the `sheet:operationName` job pattern and provide field context through the job's subject parameters.

```typescript  theme={null}
listener.on(
  "job:ready",
  { job: "sheet:capitalize" },
  async (event) => {
    const { jobId, sheetId } = event.context;
    
    try {
      // Acknowledge the job start
      await api.jobs.ack(jobId, {
        info: "Starting job to capitalize all values",
        progress: 10,
      });

      // Get the field key from the job subject
      const { data: { subject } } = await api.jobs.get(jobId);
      const fieldKey = subject.params.columnKey;

      // Get all records from the sheet
      const { data: { records } } = await api.records.get(sheetId);

      await api.jobs.update(jobId, {
        info: "Capitalizing all values",
        progress: 20,
      });

      // Process records for the specific field
      const updatedRecords = [];
      records.forEach(record => {
        const value = record.values[fieldKey].value as string;
        if (value && value.length > 0) {
          const capitalizedValue = value.toUpperCase();
          if (value !== capitalizedValue) {
            record.values[fieldKey].value = capitalizedValue;
            updatedRecords.push(record);
          }
        }
      });

      await api.jobs.update(jobId, {
        info: "Updating records",
        progress: 60,
      });

      // Update only the modified records
      if (updatedRecords.length > 0) {
        await api.records.update(sheetId, updatedRecords);
      }
      
      await api.jobs.complete(jobId, {
        outcome: {
          message: `Successfully capitalized ${updatedRecords.length} values in the ${fieldKey} column.`,
        },
      });
    } catch (error) {
      console.error(error);
      await api.jobs.fail(jobId, {
        outcome: {
          message: "Failed to capitalize field values: " + error.message,
        },
      });
    }
  }
);
```

### Key Differences from Other Action Types

Field actions have several unique characteristics:

* **Job Pattern**: Use `sheet:operationName`
* **Context Access**: Field key is available via `job.subject.params.columnKey`
* **UI Location**: Appear in column header dropdown menus
* **Configuration**: Defined within individual field objects in the Blueprint

## Document Actions

<Frame caption="Example Document Action">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=8d3a39c31360ace5cd05d126d649935a" width="610" data-og-width="1478" data-og-height="628" data-path="guides/assets/document-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e7f7e428d260c458651a9ef3b5352cd2 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=498e61a0b644eb4c069904ff7b698073 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a8bcec46029fd0f73e96e0051aff3813 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=8b9e3ed0f6344e614be489de20f8a172 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ecce004f145d059f3cd4486281ce70aa 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/document-action.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=b0577962c8ec9580a76c0b73dbc7b3e1 2500w" />
</Frame>

Document-mounted actions are similar to Workbook-mounted actions. They appear in the top right corner of your Document.

### Usage

If you configure `primary: true` on an Action, it will be highlighted in the Document.

#### Document Configuration

Define Document-mounted Actions using the `actions` parameter when you create a Document.

```typescript  theme={null}
import api from "@flatfile/api";

export default function flatfileEventListener(listener) {
  listener.on("file:created", async ({ context: { spaceId, fileId } }) => {
    const fileName = (await api.files.get(fileId)).data.name;
    const bodyText =
      "# Welcome\n" +
      "### Say hello to your first customer Space in the new Flatfile!\n" +
      "Let's begin by first getting acquainted with what you're seeing in your Space initially.\n" +
      "---\n" +
      `Your uploaded file, ${fileName}, is located in the Files area.`;

    const doc = await api.documents.create(spaceId, {
      title: "Getting Started",
      body: bodyText,
      actions: [
        {
          label: "Submit",
          operation: "contacts:submit",
          description: "Would you like to submit the contact data?",
          tooltip: "Submit the contact data",
          mode: "foreground",
          primary: true,
          confirm: true,
        },
      ],
    });
  });
}
```

#### Listener Implementation

In your listener, listen for the job's event and perform your desired operations.

```typescript  theme={null}
export default function flatfileEventListener(listener) {
  listener.on(
    "job:ready",
    { job: "document:contacts:submit" },
    async (event) => {
      const { context, payload } = event;
      const { jobId, workbookId } = context;

      try {
        await api.jobs.ack(jobId, {
          info: "Starting submit job...",
          progress: 10,
          estimatedCompletionAt: new Date("Tue Aug 23 2023 16:19:42 GMT-0700"),
        });

        // Do your work here

        await api.jobs.complete(jobId, {
          outcome: {
            message: `Submit job was completed succesfully.`,
          },
        });
      } catch (error) {
        console.log(`There was an error: ${JSON.stringify(error)}`);
        await api.jobs.fail(jobId, {
          outcome: {
            message: `This job failed.`,
          },
        });
      }
    }
  );
}
```

## File Actions

<Frame caption="Example File Action (Log File Metadata)">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a19153d16a11cacc4a2ad2cda72bb653" width="610" data-og-width="2338" data-og-height="804" data-path="guides/assets/file-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=7d2a3db78b7873b8fd665358d75ccf76 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=4c39a9b440e0ee57546b65619c8bfeb6 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ea9db5dd6b027d4664c0a709f554112f 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=d91373134f3f7b417ec7329e760e83bf 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=188f6d0c0c13f1b2112cd90a01dcda9a 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/file-action.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=a84566de04d7e52869634dd330660921 2500w" />
</Frame>

Each file has built-in actions like Delete and Download.

File-mounted actions are represented as a dropdown menu for each file in the Files list. You can attach additional actions to a File.

### Usage

You can attach additional actions to a File by listening for file events and updating the file's actions array.

#### File Configuration

First, listen for a `file:ready` event and add one or more actions to the file.

```typescript  theme={null}
listener.on("file:created", async ({ context: { fileId } }) => {
  const file = await api.files.get(fileId);
  const actions = file.data?.actions || [];
  const newActions = [
    ...actions,
    {
      operation: "logFileContents",
      label: "Log File Metadata",
      description: "This will log the file metadata.",
      primaty: true,
    }
  ];
  await api.files.update(fileId, {
    actions: newActions,
  });
});
```

#### Listener Implementation

Next, listen for `job:ready` and filter on the `domain` (file) and the `operation` of where the Action was placed. Be sure to complete the job when it's done.

```typescript  theme={null}
listener.on(
  "job:ready",
  { job: "file:logFileContents" },
  async ({ context: { fileId, jobId } }) => {
    try {
      await api.jobs.ack(jobId, {
        info: "Getting started.",
        progress: 10,
        estimatedCompletionAt: new Date(Date.now() + 10000),
      });

      const file = await api.files.get(fileId);
      console.log({ file });

      await api.jobs.update(jobId, {
        info: "Logged.",
        progress: 90,
        estimatedCompletionAt: new Date(Date.now() + 10000),
      });

      
      await api.jobs.complete(jobId, {
        outcome: {
          message: "Logging file contents is complete.",
        },
      });
    } catch (error) {
      await api.jobs.fail(jobId, {
        outcome: {
          message: "Logging file contents failed: " + error.message,
        },
      });
    }

  }
);
```

## Action Parameters

### Required Parameters

| Parameter   | Type     | Description                                                                                                                |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| `operation` | `string` | A unique identifier for the Action that is used by the listener to determine what work to do as part of the resulting Job. |
| `label`     | `string` | The text that will be displayed to the user in the UI as a button or menu item.                                            |

### Optional Parameters

| Parameter     | Type        | Default        | Description                                                                                                            |
| ------------- | ----------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `primary`     | `boolean`   | `false`        | Whether the Action is a primary Action for the resource. Primary Actions are displayed more prominently in the UI.     |
| `confirm`     | `boolean`   | `true`         | When set to true, a modal is shown to confirm the Action.                                                              |
| `description` | `string`    | -              | The text displayed to the user when a confirmation modal is used. Phrase this as a question.                           |
| `icon`        | `string`    | lightning bolt | The icon to be displayed. Use `'none'` to omit the icon. See [Flatfile icons](/reference/icons) for available options. |
| `tooltip`     | `string`    | -              | Text displayed as a tooltip when hovering over the action button or menu item.                                         |
| `messages`    | `array[{}]` | -              | Custom messages displayed as tooltips based on action state. Supports `[{ type: 'error' }]` and `[{ type: 'info' }]`.  |
| `constraints` | `array[{}]` | -              | Conditions that disable the action. Options: `hasAllValid`, `hasSelection`, `hasData`.                                 |
| `mode`        | `string`    | `background`   | Execution mode: `foreground`, `background`, or `toolbarBlocking`.                                                      |

#### Constraint Types

* `hasAllValid`: Disables action when there are invalid records
* `hasSelection`: Disables action when no records are selected (Sheet actions only)
* `hasData`: Disables action when there are no records

#### Mode Types

* `foreground`: Prevents interacting with the entire resource until complete
* `background`: Runs in the background without blocking the UI
* `toolbarBlocking`: Disables sheet-level toolbar and column header menus while allowing manual record entry

### Usage

An Action with all of the above properties would look like this:

```javascript  theme={null}
{
  operation: 'my-action',
  label: 'My Action',
  primary: true,
  confirm: true,
  description: 'Are you sure you want to run this action?',
  constraints: [{ type: 'hasAllValid' }, { type: 'hasSelection' }],
  mode: 'foreground'
  tooltip: 'Click to run action'
}
```

## Input Forms

<Frame caption="Example Input Form">
  <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=6ae2e24a2ea4a307412fcdb84fa16069" width="610" data-og-width="1302" data-og-height="780" data-path="guides/assets/input-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=24254faed402326a94e8847c551eb3ae 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=77c3850908418868bae8c144380cdabe 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=51ab07d7ac88343755d697e67614dc8c 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=ac73917701f3ae1557801111b0f5bf09 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=453f93439f3919adf6fb3d1d6128b933 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/guides/assets/input-form.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=bce41b6e14934f3df7fb2e1c68f9ab6a 2500w" />
</Frame>

When initiating an action, there may be instances where additional information is required from the end user to successfully complete the intended task. For example, you might want to enable users to specify the name of the file they intend to export.

In such cases, if you configure input fields for your action, a secondary dialog will be presented to the end user, prompting them to provide the necessary information. Once the user has entered the required details, they can proceed with the action seamlessly.

### Configuration

| Parameter | Type            | Required | Description                                                  |
| --------- | --------------- | -------- | ------------------------------------------------------------ |
| `type`    | `string`        | ✓        | The type of the input form. Currently accepts: `simple`      |
| `fields`  | `array[object]` | ✓        | An array of field objects representing the input form fields |

### Fields

| Parameter      | Type            | Required | Description                                                      |
| -------------- | --------------- | -------- | ---------------------------------------------------------------- |
| `key`          | `string`        | ✓        | The key for the field                                            |
| `label`        | `string`        | ✓        | The label for the field                                          |
| `type`         | `string`        | ✓        | Field type: `string`, `textarea`, `number`, `boolean`, or `enum` |
| `defaultValue` | `string`        | -        | The default value for the field                                  |
| `description`  | `string`        | -        | A description of the field                                       |
| `config`       | `object`        | -        | Configuration options for the field (required for `enum` type)   |
| `constraints`  | `array[object]` | -        | An array of constraints for the field                            |

### Config (for enum fields)

| Parameter | Type            | Required | Description                       |
| --------- | --------------- | -------- | --------------------------------- |
| `options` | `array[object]` | ✓        | An array of options for the field |

### Options

| Parameter     | Type     | Required | Description                                         |
| ------------- | -------- | -------- | --------------------------------------------------- |
| `value`       | `string` | ✓        | The value or ID of the option                       |
| `label`       | `string` | -        | A visual label for the option                       |
| `description` | `string` | -        | A short description of the option                   |
| `meta`        | `object` | -        | An arbitrary JSON object associated with the option |

### Field Constraints

| Parameter | Type     | Required | Description                                           |
| --------- | -------- | -------- | ----------------------------------------------------- |
| `type`    | `string` | ✓        | The type of constraint. Currently accepts: `required` |

### Usage

First, configure your action to have an inputForm on your Blueprint. These will appear once the action button is clicked.

```javascript  theme={null}
actions: [
  {
    operation: "submitActionFg",
    mode: "foreground",
    label: "Submit data elsewhere",
    type: "string",
    description: "Submit this data to a webhook.",
    primary: true,
    inputForm: {
      type: "simple",
      fields: [
        {
          key: "priority",
          label: "Priority level",
          description: "Set the priority level.",
          type: "enum",
          defaultValue: "80ce8718a21c",
          config: {
            options: [
              {
                value: "80ce8718a21c",
                label: "High Priority",
                description:
                  "Setting a value to High Priority means it will be prioritized over other values",
              },
            ],
          },
          constraints: [
            {
              type: "required",
            },
          ],
        },
      ],
    },
  },
];
```

Next, listen for a `job:ready` and filter on the `job` you'd like to process. Grab the data entered in the form from the job itself and leverage it as required for your use case.

```typescript  theme={null}
import api from "@flatfile/api";

export default async function (listener) {
  listener.on(
    "job:ready",
    { job: "workbook:actionWithInput" },
    async (event) => {
      const { jobId } = event.context;

      try {
        await api.jobs.ack(jobId, {
          info: "Acknowledging job",
          progress: 1,
        });

        // retrieve input
        const { data: job } = await api.jobs.get(jobId);
        const input = job.input;
        console.log({ input });

        // do something with input...

        await api.jobs.complete(jobId, {
          outcome: {
            message: "Action was successful",
          },
        });
        return;
      } catch (error) {
        console.error(error);
        await api.jobs.fail(jobId, {
          outcome: {
            message: "Action failed",
          },
        });
        return;
      }
    }
  );
}
```

## Constraints

### Usage

#### Workbook & Sheet Actions

1. Adding a `hasAllValid` constraint on an Action will disable a Workbook Action when there are invalid records.
2. Adding a `hasData` on an Action will disable a Workbook Action when there are no records.

```javascript  theme={null}
actions: [
  {
    operation: 'submitActionFg',
    mode: 'foreground',
    label: 'Submit data elsewhere',
    description: 'Submit this data to a webhook.',
    primary: true,
    constraints: [{ type: 'hasAllValid'},{ type: 'hasData' }]
  },
  {...}
],
```

#### Sheet Actions Only

Adding a constraint of `hasSelection` on an Action will disable a Sheet Action when no records in the Sheet are selected.

```javascript  theme={null}
sheets : [
  {
    name: "Sheet Name",
    actions: [
      {
        operation: 'duplicate',
        mode: 'background',
        label: 'Duplicate selected names',
        description: 'Duplicate names for selected rows',
        constraints: [{ type: 'hasSelection' }],
        primary: true,
      },
      {...}
    ]
  }
]
```

## Messages

Add custom messages to actions, tailored according to their state:

* Error
* Info

These messages will be displayed as tooltips when users hover over an action, providing context-specific text that corresponds to the action's current state. When an error message is present on an action, the action will be disabled.

### Usage

Simply add a messages property to your action configuration. This property should be an array of objects, each specifying a message type and its content.

```javascript  theme={null}
  actions: [
    {
      operation: 'duplicate',
      mode: 'background',
      label: 'Duplicate selected names',
      description: 'Duplicate names for selected rows',
      messages: [
        { type: 'error', content: 'This is an error message' },
      ],
      primary: true,
    },
    {...}
  ]
```
