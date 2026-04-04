# Source: https://flatfile.com/docs/reference/events.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Reference

> Complete reference for all Flatfile events, their payloads, and when they are triggered

Flatfile emits events throughout the data import lifecycle, allowing your applications to respond to user actions, system changes, and processing results. This reference documents all available events, their payloads, and when they are triggered.

## Event Structure

All Flatfile events follow a consistent structure. Optional fields may be included depending on the event's Domain ([workbook-level](#workbook-events) events, for instance, won't have a sheetId)

```typescript  theme={null}
interface FlatfileEvent {
  id: string;
  topic: string;
  domain: string;
  context: {
    environmentId: string;
    spaceId?: string;
    workbookId?: string;
    sheetId?: string;
    jobId?: string;
    fileId?: string;
    [key: string]: any;
  };
  payload: any;
  attributes?: any;
  createdAt: string;
}
```

## Listening and Reacting to Events

To respond to these events, you'll need to create a [Listener](/core-concepts/listeners) that subscribes to the specific events your application needs to handle.

## Job Events

Job events are triggered when background tasks and operations change state.

### job:created

<ResponseField name="Description">
  Triggered when a new job is first created. Some jobs will enter an optional
  planning state at this time. A job with 'immediate' set to true will skip the
  planning step and transition directly to 'ready.'
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:ready

<ResponseField name="Description">
  Triggered when a job is ready for execution by your listener. Either the job
  has a complete plan of work or the job is configured to not need a plan. This
  is the only event most job implementations will care about. Once a ready job
  is acknowledged by a listener, it transitions into an executing state.
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

<ResponseField name="Usage Example">
  ```typescript  theme={null}
  listener.filter({ job: "*" }, (configure) => {
    configure.on("job:ready", async (event) => {
      const { jobId } = event.context
      // Handle any job that becomes ready
      await processJob(jobId)
    })
  })
  ```
</ResponseField>

### job:scheduled

<ResponseField name="Description">
  Triggered when a job is scheduled to run at a future time
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status (scheduled)
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:updated

<ResponseField name="Description">
  Triggered when a job is updated. For example, when a listener updates the
  state or progress of the job. The event will emit many times as the listener
  incrementally completes work and updates the job.
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:completed

<ResponseField name="Description">
  Triggered when a job has completed successfully
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:outcome-acknowledged

<ResponseField name="Description">
  Triggered to trigger workflow actions after the user has acknowledged that the
  job has completed or failed. Background jobs will skip this step.
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    workbookId?: string
    sheetId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:parts-completed

<ResponseField name="Description">
  Triggered when all parts of a multi-part job have completed processing
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status (parts-completed)
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
    parts: Array<{       // completed parts information
      partId: string
      status: string
      completedAt: string
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:failed

<ResponseField name="Description">Triggered when a job fails</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    domain: string       // event domain (e.g., "space", "workbook")
    operation: string    // operation name (e.g., "configure")
    job: string          // domain:operation format (e.g., "space:configure")
    status: string       // job status
    info?: string        // optional info message
    isPart: boolean      // whether this is a sub-job
    input?: any          // job input data
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    workbookId?: string
    sheetId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

### job:deleted

<ResponseField name="Description">
  Triggered when a job is deleted
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId?: string
    jobId: string
    actorId: string
  }
  ```
</ResponseField>

## Program Events

Program events are triggered when mapping programs and transformations change state.

### program:created

<ResponseField name="Description">
  Triggered when a new mapping program is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

### program:updated

<ResponseField name="Description">
  Triggered when a mapping program is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

### program:recomputing

<ResponseField name="Description">
  Triggered when a mapping program begins recomputing its transformations
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

### program:recomputed

<ResponseField name="Description">
  Triggered when a mapping program has finished recomputing its transformations
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

## File Events

File events are triggered when files are uploaded, processed, or modified.

### file:created

<ResponseField name="Description">
  Triggered when a file upload begins or a new file is created
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    fileId: string
    actorId: string
  }
  ```
</ResponseField>

### file:updated

<ResponseField name="Description">
  Triggered when a file is updated. For example, when a file has been extracted
  into a workbook
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    fileId: string
    actorId: string
  }
  ```
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    status: string
    workbookId?: string
  }
  ```
</ResponseField>

### file:deleted

<ResponseField name="Description">
  Triggered when a file is deleted
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    fileId: string
    actorId: string
  }
  ```
</ResponseField>

### file:expired

<ResponseField name="Description">
  Triggered when a file is expired
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    fileId: string
  }
  ```
</ResponseField>

## Record Events

Record events are triggered when data records are created, updated, or deleted.

### records:created

<ResponseField name="Description">
  Triggered when new records are added to a sheet
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    recordIds: string[]
    recordCount: number
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
  }
  ```
</ResponseField>

### records:updated

<Info>
  **A note on `commit:created` vs `records:updated`**

  You might think you want to listen to `records:updated` for data processing, but **[`commit:created`](#commit-events) is the recommended choice for most automation**.

  A **commit** is like a "git commit" but for data - a versioned snapshot of all changes that occurred together in a single operation. This provides complete transaction context and better performance when processing multiple record changes.

  Flatfile's own Plugins ([Record Hooks](/plugins/record-hook), [Constraints](/plugins/constraints), [Autocast](/plugins/autocast), etc.) all use `commit:created`. Reserve `records:updated` only for real-time per-record feedback scenarios.
</Info>

<ResponseField name="Description">
  Triggered when existing records are modified
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    recordIds: string[]
    changes: Array<{
      recordId: string
      fieldKey: string
      previousValue: any
      newValue: any
    }>
  }
  ```
</ResponseField>

### records:deleted

<ResponseField name="Description">
  Triggered when records are deleted from a sheet
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    recordIds: string[]
    recordCount: number
  }
  ```
</ResponseField>

## Sheet Events

Sheet events are triggered when sheets are created, modified, or when sheet-level operations occur.

### sheet:calculation-updated

<ResponseField name="Description">
  Triggered when sheet calculations or formulas are updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string  
    calculations: Array<{
      field: string
      formula: string
      updated: boolean
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

### sheet:counts-updated

<ResponseField name="Description">
  Triggered when record counts for a sheet are updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    counts: {
      total: number
      valid: number
      error: number
      updated: number
    }
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

### sheet:created

<ResponseField name="Description">
  Triggered when a new sheet is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    name: string
    slug: string
    fieldCount: number
  }
  ```
</ResponseField>

### sheet:updated

<ResponseField name="Description">
  Triggered when a sheet Blueprint or configuration is modified
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    changes: Array<{
      type: "field_added" | "field_removed" | "field_updated" | "config_updated"
      details: any
    }>
  }
  ```
</ResponseField>

### sheet:deleted

<ResponseField name="Description">
  Triggered when a sheet is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    name: string
    slug: string
  }
  ```
</ResponseField>

## Workbook Events

Workbook events are triggered for workbook-level operations and changes.

### workbook:created

<ResponseField name="Description">
  Triggered when a new workbook is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    workbookId: string
    spaceId: string
    name: string
    namespace?: string
    sheetCount: number
  }
  ```
</ResponseField>

### workbook:updated

<ResponseField name="Description">
  Triggered when a workbook is modified
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    workbookId: string
    spaceId: string
    changes: Array<{
      type: "sheet_added" | "sheet_removed" | "config_updated"
      details: any
    }>
  }
  ```
</ResponseField>

### workbook:deleted

<ResponseField name="Description">
  Triggered when a workbook is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    workbookId: string
    spaceId: string
  }
  ```
</ResponseField>

### workbook:expired

<ResponseField name="Description">
  Triggered when a workbook expires
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    workbookId: string
    spaceId: string
  }
  ```
</ResponseField>

## Space Events

Space (Project) events are triggered for project lifecycle changes.

### space:created

<ResponseField name="Description">
  Triggered when a new project (space) is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    spaceId: string
    environmentId: string
    name: string
    appId?: string
  }
  ```
</ResponseField>

### space:updated

<ResponseField name="Description">
  Triggered when a project is modified
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    spaceId: string
    environmentId: string
    changes: Array<{
      field: string
      previousValue: any
      newValue: any
    }>
  }
  ```
</ResponseField>

### space:deleted

<ResponseField name="Description">
  Triggered when a space is deleted
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    actorId: string
  }
  ```
</ResponseField>

### space:expired

<ResponseField name="Description">
  Triggered when a space is expired
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
  }
  ```
</ResponseField>

### space:archived

<ResponseField name="Description">
  Triggered when a space is archived
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
  }
  ```
</ResponseField>

### space:guestAdded

<ResponseField name="Description">
  Triggered when a guest is added
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    actorId: string
    accountId: string
    environmentId: string
    spaceId: string
  }
  ```
</ResponseField>

### space:guestRemoved

<ResponseField name="Description">
  Triggered when a guest's access is revoked from a space
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    actorId: string
    accountId: string
    environmentId: string
    spaceId: string
  }
  ```
</ResponseField>

### space:unarchived

<ResponseField name="Description">
  Triggered when a space is unarchived and restored to active status
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    actorId: string
    accountId: string
    environmentId: string
    spaceId: string
  }
  ```
</ResponseField>

## Environment Events

Environment events are triggered for organization-level changes.

### environment:autobuild-created

<ResponseField name="Description">
  Triggered when an autobuild configuration is created for an environment
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    environmentId: string
    accountId: string
    appId?: string
    actorId: string
  }
  ```
</ResponseField>

### environment:created

<ResponseField name="Description">
  Triggered when a new environment is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    environmentId: string
    name: string
    slug: string
    isProd: boolean
  }
  ```
</ResponseField>

### environment:updated

<ResponseField name="Description">
  Triggered when an environment is modified
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    environmentId: string
    changes: Array<{
      field: string
      previousValue: any
      newValue: any
    }>
  }
  ```
</ResponseField>

### environment:deleted

<ResponseField name="Description">
  Triggered when an environment is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    environmentId: string
    deletedAt: string
    deletedBy: string
  }
  ```
</ResponseField>

## Action Events

Action events are triggered when custom actions are created, updated, or deleted.

### action:created

<ResponseField name="Description">
  Triggered when a new custom action is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    actionId: string
    name: string
    label: string
    description?: string
    type: string
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId?: string
    sheetId?: string
    actorId: string
  }
  ```
</ResponseField>

### action:updated

<ResponseField name="Description">
  Triggered when a custom action is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    actionId: string
    name: string
    label: string
    description?: string
    type: string
    changes: Array<{
      field: string
      previousValue: any
      newValue: any
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId?: string
    sheetId?: string
    actorId: string
  }
  ```
</ResponseField>

### action:deleted

<ResponseField name="Description">
  Triggered when a custom action is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    actionId: string
    name: string
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId?: string
    sheetId?: string
    actorId: string
  }
  ```
</ResponseField>

## Document Events

Document events are triggered when documents are created, updated, or deleted within workbooks.

### document:created

<ResponseField name="Description">
  Triggered when a document is created on a workbook
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    actorId: string
    spaceId: string
    accountId: string
    documentId: string
    environmentId: string
  }
  ```
</ResponseField>

### document:updated

<ResponseField name="Description">
  Triggered when a document is updated on a workbook
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    actorId: string
    spaceId: string
    accountId: string
    documentId: string
    environmentId: string
  }
  ```
</ResponseField>

### document:deleted

<ResponseField name="Description">
  Triggered when a document is deleted on a workbook
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    actorId: string
    spaceId: string
    accountId: string
    documentId: string
    environmentId: string
  }
  ```
</ResponseField>

## Commit Events

Commit events are triggered when data changes are made to records.

### commit:created

<ResponseField name="Description">
  Triggered when a cell in a record is created or updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    versionId: string
    sheetSlug: string
  }
  ```
</ResponseField>

### commit:updated

<ResponseField name="Description">
  Triggered when commit metadata or details are updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    commitId: string
    versionId: string
    changes: Array<{
      field: string
      previousValue: any
      newValue: any
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    workbookId: string
    sheetId: string
    actorId: string
  }
  ```
</ResponseField>

### commit:completed

<ResponseField name="Description">
  Triggered when a commit has completed (only when trackChanges is enabled)
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    versionId: string
    commitId: string
  }
  ```
</ResponseField>

### layer:created

<ResponseField name="Description">
  Triggered when a new layer is created within a commit
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    sheetId: string
    workbookId: string
    layerId: string
    commitId: string
  }
  ```
</ResponseField>

## Snapshot Events

Snapshot events are triggered when snapshots of sheet data are created.

### snapshot:created

<ResponseField name="Description">
  Triggered when a snapshot is created of a sheet
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    snapshotId: string
    sheetId: string
    workbookId: string
    spaceId: string
  }
  ```
</ResponseField>

## Agent Events

Agent events are triggered when agents are created, updated, or deleted.

### agent:created

<ResponseField name="Description">
  Triggered when a new agent is deployed
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    agentId: string
    environmentId: string
  }
  ```
</ResponseField>

### agent:updated

<ResponseField name="Description">
  Triggered when an agent is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    agentId: string
    environmentId: string
  }
  ```
</ResponseField>

### agent:deleted

<ResponseField name="Description">
  Triggered when an agent is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    agentId: string
    environmentId: string
  }
  ```
</ResponseField>

## Secret Events

Secret events are triggered when secrets are managed.

### secret:created

<ResponseField name="Description">
  Triggered when a new secret is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    secretId: string
    spaceId: string
    environmentId: string
  }
  ```
</ResponseField>

### secret:updated

<ResponseField name="Description">
  Triggered when a secret is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    secretId: string
    spaceId: string
    environmentId: string
  }
  ```
</ResponseField>

### secret:deleted

<ResponseField name="Description">
  Triggered when a secret is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    secretId: string
    spaceId: string
    environmentId: string
  }
  ```
</ResponseField>

## Data Clip Events

Data clip events are triggered when data clips are managed.

### data-clip:collaborator-updated

<ResponseField name="Description">
  Triggered when collaborators are added or removed from a data clip
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    dataClipId: string
    collaborators: string[]
    changes: Array<{
      action: "added" | "removed"
      userId: string
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    dataClipId: string
  }
  ```
</ResponseField>

### data-clip:created

<ResponseField name="Description">
  Triggered when a new data clip is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    dataClipId: string
    accountId: string
    status: string
  }
  ```
</ResponseField>

### data-clip:updated

<ResponseField name="Description">
  Triggered when a data clip's details are updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    dataClipId: string
    accountId: string
    status: string
  }
  ```
</ResponseField>

### data-clip:deleted

<ResponseField name="Description">
  Triggered when a data clip is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    dataClipId: string
    accountId: string
    status: string
  }
  ```
</ResponseField>

### data-clip:resolutions-created

<ResponseField name="Description">
  Triggered when new conflict resolutions are created for a data clip
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    dataClipId: string
    resolutions: Array<{
      conflictId: string
      resolution: any
      resolvedBy: string
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    dataClipId: string
  }
  ```
</ResponseField>

### data-clip:resolutions-refreshed

<ResponseField name="Description">
  Triggered when conflict resolutions are refreshed or recalculated for a data clip
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    dataClipId: string
  }
  ```
</ResponseField>

### data-clip:resolutions-updated

<ResponseField name="Description">
  Triggered when existing conflict resolutions are updated for a data clip
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    dataClipId: string
    resolutions: Array<{
      conflictId: string
      resolution: any
      resolvedBy: string
      updatedAt: string
    }>
    changes: Array<{
      conflictId: string
      previousResolution: any
      newResolution: any
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    dataClipId: string
  }
  ```
</ResponseField>

## Canvas Events

Canvas events are triggered when canvases are created, updated, or deleted.

### canvas:created

<ResponseField name="Description">
  Triggered when a new canvas is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    // Full canvas object with all properties
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    canvasId: string
    spaceId: string
    environmentId: string
    accountId: string
  }
  ```
</ResponseField>

### canvas:updated

<ResponseField name="Description">
  Triggered when a canvas is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    // Full canvas object with all properties
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    canvasId: string
    spaceId: string
    environmentId: string
    accountId: string
  }
  ```
</ResponseField>

### canvas:deleted

<ResponseField name="Description">
  Triggered when a canvas is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    // Full canvas object with all properties
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    canvasId: string
    spaceId: string
    environmentId: string
    accountId: string
  }
  ```
</ResponseField>

## Canvas Area Events

Canvas area events are triggered when canvas areas are created, updated, or deleted.

### canvas-area:created

<ResponseField name="Description">
  Triggered when a new canvas area is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    // Full canvas area object with all properties
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    canvasAreaId: string
    canvasId: string
  }
  ```
</ResponseField>

### canvas-area:updated

<ResponseField name="Description">
  Triggered when a canvas area is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    // Full canvas area object with all properties
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    canvasAreaId: string
    canvasId: string
  }
  ```
</ResponseField>

### canvas-area:deleted

<ResponseField name="Description">
  Triggered when a canvas area is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    // Full canvas area object with all properties
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    canvasAreaId: string
    canvasId: string
  }
  ```
</ResponseField>

## Thread Events

Thread events are triggered when AI conversation threads are created, updated, or deleted.

### thread:created

<ResponseField name="Description">
  Triggered when a new AI conversation thread is created
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    threadId: string
    title?: string
    status: string
    createdAt: string
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    threadId: string
    actorId: string
  }
  ```
</ResponseField>

### thread:updated

<ResponseField name="Description">
  Triggered when an AI conversation thread is updated
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {
    threadId: string
    title?: string
    status: string
    changes: Array<{
      field: string
      previousValue: any
      newValue: any
    }>
  }
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    threadId: string
    actorId: string
  }
  ```
</ResponseField>

### thread:deleted

<ResponseField name="Description">
  Triggered when an AI conversation thread is deleted
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    accountId: string
    environmentId: string
    spaceId: string
    threadId: string
    actorId: string
  }
  ```
</ResponseField>

## Cron Events

<Warning>
  \*\* Deployed Agents Required \*\*

  Cron events are only created for environments that have deployed agents subscribed to the specific cron topics. These events will not fire in localhost development environments unless you have deployed agents running in that environment.
</Warning>

Cron events are system events triggered at scheduled intervals for automated processes.

### cron:5-minutes

<ResponseField name="Description">
  Triggered every 5 minutes for system maintenance and periodic tasks
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    environmentId: string
  }
  ```
</ResponseField>

### cron:hourly

<ResponseField name="Description">
  Triggered every hour for scheduled maintenance and cleanup tasks
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    environmentId: string
  }
  ```
</ResponseField>

### cron:daily

<ResponseField name="Description">
  Triggered once daily for daily maintenance and reporting tasks
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    environmentId: string
  }
  ```
</ResponseField>

### cron:weekly

<ResponseField name="Description">
  Triggered once weekly for weekly cleanup and archival tasks
</ResponseField>

<ResponseField name="Payload">
  ```typescript  theme={null}
  {}
  ```
</ResponseField>

<ResponseField name="Context">
  ```typescript  theme={null}
  {
    environmentId: string
  }
  ```
</ResponseField>
