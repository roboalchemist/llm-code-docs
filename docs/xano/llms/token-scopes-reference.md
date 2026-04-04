# Source: https://docs.xano.com/xano-features/metadata-api/token-scopes-reference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Token Scopes Reference

This page is designed to give you a clear reference of what all of the scopes mean when generating Metadata API access tokens.

It is imperative that you ensure only the scopes necessary for your use case are selected to avoid potential security risks.

## Before you proceed

Please note that a Metadata API access token grants access to **all workspaces** in the instance the token was created.

Each scope offers four different permission settings, as follows.

* **C (Create)**

  * Create new data defined within this scope

* **R (Read)**

  * Read data defined within this scope

* **U (Update)**

  * Update existing data defined within this scope

* **D (Delete)**

  * Delete data defined within this scope

You can quickly add or remove all permission settings by hovering over them and clicking + or -

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e7bea723-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=8b1a67a1aa181b0877b04cec296b9dd5" width="437" height="59" data-path="images/e7bea723-image.jpeg" />
</Frame>

| Scope                      | Description                                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Workspace Database         | Allows access to the database including table data and schema across all data sources                                                 |
| Workspace Content          | Allows access to workspace-wide information such as datasources, branches, basic workspace information and exporting / importing data |
| Workspace Live Data Source | Allows specific access to the live (production) data source                                                                           |
| Workspace API Groups       | Allows access to APIs and API groups                                                                                                  |
| Workspace Functions        | Allows access to [custom functions](/the-function-stack/building-with-visual-development/custom-functions)                            |
| Workspace Addons           | Allows access to [addons](/the-function-stack/functions/database-requests/query-all-records#using-addons)                             |
| Workspace Tasks            | Allows access to [tasks](/the-function-stack/building-with-visual-development/background-tasks)                                       |
| Workspace Files            | Allows access to public and private [file storage](/file-storage/file-storage-in-xano)                                                |
| Workspace Request History  | Allows access to your [request history](/maintenance-monitoring-and-logging/request-history)                                          |

### What scopes should I use?

While it's hard to answer this question without specific knowledge of your use case, here are some examples of proper scoping that might make sense.

#### **WeWeb**

To use WeWeb's Xano plugin(s), you'll need the following scopes.

| Scope                | C | R  | U | D | Why?                                                                                 |
| -------------------- | - | -- | - | - | ------------------------------------------------------------------------------------ |
| Workspace API Groups |   | ✅️ |   |   | WeWeb needs to be able to read information about your API groups and available APIs. |
| Workspace Content    |   | ✅️ |   |   | WeWeb needs to know about your available workspaces.                                 |

#### **Monitoring and Logging**

For monitoring and logging tools, you might need the following scopes.

| Scope                     | C | R  | U | D | Why?                                                         |
| ------------------------- | - | -- | - | - | ------------------------------------------------------------ |
| Workspace API Groups      |   | ✅️ |   |   | For getting specific information about APIs it is monitoring |
| Workspace Content         |   | ✅️ |   |   | General information about your available workspaces.         |
| Workspace Request History |   | ✅️ |   |   | Specific request history data for parsing and logging        |


Built with [Mintlify](https://mintlify.com).