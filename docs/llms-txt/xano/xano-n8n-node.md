# Source: https://docs.xano.com/xano-n8n-node.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano n8n Node

> Use the n8n community node to run Xano Metadata API operations from any workflow.

The **n8n-nodes-xano** community node lets you call your Xano workspace directly from an n8n workflow. It covers the core content endpoints, so you can create automations that read, write, search, and synchronize data without writing glue code.

<Card title="View the node on GitHub" icon="github" href="https://github.com/n8n-io/n8n-nodes-xano">
  Browse the source, open issues, or contribute improvements to the community node.
</Card>

***

## Installation

Follow the official n8n community-node install flow so the Xano node appears inside your editor.

<Steps>
  <Step title="Enable community nodes">
    In your n8n instance, open <strong>Settings → Community Nodes</strong> and confirm community packages are allowed.
  </Step>

  <Step title="Add the package name">
    Click <strong>Install</strong> and provide <code>n8n-nodes-xano</code>. n8n downloads the package and restarts if required.
  </Step>

  <Step title="Validate availability">
    Create or open a workflow, drag a new node, and search for <strong>Xano</strong>. You should see the node plus its credential type.
  </Step>
</Steps>

Need more detail? See the <a href="https://docs.n8n.io/integrations/community-nodes/installation/">community-node installation guide</a>.

***

## Operations

| Action        | Operation value       | What it does                                 |
| ------------- | --------------------- | -------------------------------------------- |
| Create Row    | `createRow`           | Insert a single record into a selected table |
| Update Row    | `updateRow`           | Patch a row based on its ID                  |
| Delete Row    | `deleteSingleContent` | Delete one row by ID                         |
| Get Row       | `getSingleContent`    | Retrieve one record by ID                    |
| Get Many Rows | `getTableContent`     | Paginate through table rows                  |
| Bulk Create   | `bulkCreateContent`   | Insert multiple rows at once                 |
| Bulk Update   | `bulkUpdateContent`   | Send batched updates                         |
| Search Rows   | `searchRow`           | Run Metadata API search filters              |

***

## Credentials

Authenticate once with a Xano Metadata API token, then reuse those credentials across workflows.

<Steps>
  <Step title="Generate a Metadata API access token">
    <ol>
      <li>Log into Xano and click <strong>Instances</strong> in the lower-left navigation.</li>
      <li>Select the instance you want n8n to control, then click the gear icon.</li>
      <li>Open <strong>Metadata API</strong> and choose <strong>Create Token</strong>.</li>
      <li>Name the token (for example, <code>n8n automation</code>), set the expiration, and choose the scopes listed below.</li>
    </ol>
  </Step>

  <Step title="Assign the right scopes">
    <ul>
      <li><strong>Database</strong> — CRUD access for tables.</li>
      <li><strong>Content</strong> — Needed for `/content` endpoints.</li>
      <li>Optional: <strong>API Groups</strong> or other scopes if you plan to expand the node.</li>
    </ul>
  </Step>

  <Step title="Store the token in n8n">
    <ol>
      <li>In n8n, open <strong>Credentials</strong> → <strong>New</strong>.</li>
      <li>Search for <strong>Xano API</strong>, paste the token into the <strong>Access Token</strong> field, and save.</li>
      <li>Use the credential inside the Xano node; n8n confirms connectivity when you execute the workflow.</li>
    </ol>
  </Step>
</Steps>

<Info>
  For CRUD-only automation, `Read` and `Update` scope levels are the minimum. Add `Create` or `Delete` privileges only if your workflow needs them.
</Info>

<Warning>
  Invalid or expired tokens return a 401 error in n8n. Regenerate the token in Xano and update the stored credential if that happens.
</Warning>

***

## Compatibility

The node is tested with n8n v1.100.0 and later. Earlier versions should work if they support community nodes, but upgrade if you see dependency errors.

***

## Usage Recipes

Each recipe assumes you already selected the credential plus the target workspace and table.

### Get many rows (`getTableContent`)

1. Choose **Get Many Rows** as the operation.
2. Configure **Page** and **Items per Page** (defaults: `1` and `10`).
3. Add optional query-string parameters under **Additional Fields → Query Params**.
4. Run the node to mirror the response from `/content` including pagination metadata.

### Create a row (`createRow`)

1. Select **Create Row**.
2. Add fields for every column you want to populate; required fields are marked in the dropdown.
3. JSON strings are parsed automatically, so objects stay structured.
4. Execute to POST to `/content`; the response includes the new `id`.

### Update a row (`updateRow`)

1. Pick **Update Row** and supply the row `id` plus any fields that need to change.
2. The node validates field names before calling Xano; incorrect names fail fast.
3. Runs a PUT `/content/{id}` and returns the updated record.

### Get a single row (`getSingleContent`)

1. Choose **Get a Row**.
2. Provide the row ID in **Field Value** (the selector is fixed to `id`).
3. Executes a GET `/content/{id}` and emits the record.

### Delete a row (`deleteSingleContent`)

1. Choose **Delete a Row**.
2. Enter the row ID.
3. Sends DELETE `/content/{id}`. Empty responses are normalized to `{ success: true }`.

### Bulk create rows (`bulkCreateContent`)

1. Select **Create Row Bulk**.
2. Choose **Field Builder** to add items visually or **JSON Input** to paste an array.
3. Toggle **Allow ID Field** if you must seed primary keys.
4. The node posts `{ items, allow_id_field }` to `/content/bulk`.

### Bulk update rows (`bulkUpdateContent`)

1. Choose **Update Rows Bulk**.
2. Provide each row’s `id` (or `row_id`) plus the fields to patch via Field Builder or JSON Input.
3. The node converts entries into `{ row_id, updates }` and POSTs to `/content/bulk/patch`.

### Search rows (`searchRow`)

1. Select **Search Row** and configure **Sort By**, **Sort Order**, **Page**, and **Items per Page**.
2. In **Items (JSON Array)**, enter Metadata API search objects.
3. The node POSTs `/content/search` with `{ page, per_page, sort, search }`.

#### Search syntax cheat sheet

| Goal                             | JSON snippet                                                                                                                   | Notes                                         |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| `id = 2`                         | <pre><code>{`[{"id&#124;=":"2"}]`}</code></pre>                                                                                | <code>\|=</code> compares stringified values  |
| `status IN ('active','pending')` | <pre><code>{`[{"status&#124;in":["active","pending"]}]`}</code></pre>                                                          | <code>\|in</code> accepts arrays              |
| `first_name ILIKE 'jo%'`         | <pre><code>{`[{"first_name&#124;ilike":"jo%"}]`}</code></pre>                                                                  | `%` / `_` follow SQL wildcard rules           |
| `created_at between two dates`   | <pre><code>{`[{"created_at&#124;between":["2024-01-01","2024-01-31"]}]`}</code></pre>                                          | Works for numbers too                         |
| `price > 100`                    | <pre><code>{`[{"price&#124;>":100}]`}</code></pre>                                                                             | Support for `>=`, `<`, `<=`                   |
| Compound AND                     | <pre><code>{`["and", {"archived&#124;=":false}, {"score&#124;>=":10}]`}</code></pre>                                           | Prefix array with `"and"`                     |
| Nested OR                        | <pre><code>{`["and", {"workspace_id&#124;=":1}, ["or", {"status&#124;=":"pending"}, {"status&#124;=":"draft"}]]`}</code></pre> | Mirrors Metadata API syntax                   |
| Null check                       | <pre><code>{`[{"deleted_at&#124;is":null}]`}</code></pre>                                                                      | Use `null` or `not null`                      |
| Contains                         | <pre><code>{`[{"name&#124;like":"%corp%"}]`}</code></pre>                                                                      | Use <code>\|ilike</code> for case-insensitive |

<Info>
  Build filters inside the Xano UI, inspect the network request for `/content/search`, and copy the `search` payload directly into the node for complex queries.
</Info>

***

## Resources

* <a href="https://docs.n8n.io/integrations/#community-nodes">n8n community node docs</a>
* <a href="https://docs.xano.com/">Xano documentation</a>
* <a href="https://docs.xano.com/xano-features/metadata-api">Xano Metadata API guide</a>

***

## Version history

| Version | Notes           |
| ------- | --------------- |
| 1.0.6   | Minor updates   |
| 1.0.5   | Minor updates   |
| 1.0.4   | Minor updates   |
| 1.0.3   | Minor updates   |
| 1.0.2   | Minor updates   |
| 1.0.1   | Initial release |


Built with [Mintlify](https://mintlify.com).