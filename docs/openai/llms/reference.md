# Source: https://developers.openai.com/codex/cli/reference.md

# Source: https://developers.openai.com/apps-sdk/reference.md

# Reference

## `window.openai` component bridge

See [build a ChatGPT UI](https://developers.openai.com/apps-sdk/build/chatgpt-ui) for implementation walkthroughs.

### Capabilities

| Capability          | What it does                                                                                                                                                                     | Typical use                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| State & data        | `window.openai.toolInput`                                                                                                                                                        | Arguments supplied when the tool was invoked.                                                        |
| State & data        | `window.openai.toolOutput`                                                                                                                                                       | Your `structuredContent`. Keep fields concise; the model reads them verbatim.                        |
| State & data        | `window.openai.toolResponseMetadata`                                                                                                                                             | The `_meta` payload; only the widget sees it, never the model.                                       |
| State & data        | `window.openai.widgetState`                                                                                                                                                      | Snapshot of UI state persisted between renders.                                                      |
| State & data        | `window.openai.setWidgetState(state)`                                                                                                                                            | Stores a new snapshot synchronously; call it after every meaningful UI interaction.                  |
| Widget runtime APIs | `window.openai.callTool(name, args)`                                                                                                                                             | Invoke another MCP tool from the widget (mirrors model-initiated calls).                             |
| Widget runtime APIs | `window.openai.sendFollowUpMessage({ prompt })`                                                                                                                                  | Ask ChatGPT to post a message authored by the component.                                             |
| Widget runtime APIs | `window.openai.uploadFile(file)`                                                                                                                                                 | Upload a user-selected file and receive a `fileId`.                                                  |
| Widget runtime APIs | `window.openai.getFileDownloadUrl({ fileId })`                                                                                                                                   | Retrieve a temporary download URL for a file uploaded by the widget or provided via file params.     |
| Widget runtime APIs | `window.openai.requestDisplayMode(...)`                                                                                                                                          | Request PiP/fullscreen modes.                                                                        |
| Widget runtime APIs | `window.openai.requestModal({ params, template })`                                                                                                                               | Spawn a modal owned by ChatGPT (optionally targeting another registered template).                   |
| Widget runtime APIs | `window.openai.notifyIntrinsicHeight(...)`                                                                                                                                       | Report dynamic widget heights to avoid scroll clipping.                                              |
| Widget runtime APIs | `window.openai.openExternal({ href })`                                                                                                                                           | Open a vetted external link in the user’s browser.                                                   |
| Widget runtime APIs | `window.openai.setOpenInAppUrl({ href })`                                                                                                                                        | Set the page that a user will open when clicking the "Open in &lt;App&gt;" button in fullscreen mode |
| Context             | `window.openai.theme`, `window.openai.displayMode`, `window.openai.maxHeight`, `window.openai.safeArea`, `window.openai.view`, `window.openai.userAgent`, `window.openai.locale` | Environment signals you can read—or subscribe to via `useOpenAiGlobal`—to adapt visuals and copy.    |

## File APIs

| API                                            | Purpose                                             | Notes                                                                  |
| ---------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------- |
| `window.openai.uploadFile(file)`               | Upload a user-selected file and receive a `fileId`. | Supports `image/png`, `image/jpeg`, `image/webp`.                      |
| `window.openai.getFileDownloadUrl({ fileId })` | Request a temporary download URL for a file.        | Only works for files uploaded by the widget or passed via file params. |

When persisting widget state, use the structured shape (`modelContent`, `privateContent`, `imageIds`) if you want the model to see image IDs during follow-up turns.

## Tool descriptor parameters

Need more background on these fields? Check the [Advanced section of the MCP server guide](https://developers.openai.com/apps-sdk/build/mcp-server#advanced).

By default, a tool description should include the fields listed [here](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool).

### `_meta` fields on tool descriptor

We also require the following `_meta` fields on the tool descriptor:

| Key                                       |    Placement    | Type         | Limits                          | Purpose                                                                                         |
| ----------------------------------------- | :-------------: | ------------ | ------------------------------- | ----------------------------------------------------------------------------------------------- |
| `_meta["securitySchemes"]`                | Tool descriptor | array        | —                               | Back-compat mirror for clients that only read `_meta`.                                          |
| `_meta["openai/outputTemplate"]`          | Tool descriptor | string (URI) | —                               | Resource URI for component HTML template (`text/html+skybridge`).                               |
| `_meta["openai/widgetAccessible"]`        | Tool descriptor | boolean      | default `false`                 | Allow component→tool calls through the client bridge.                                           |
| `_meta["openai/visibility"]`              | Tool descriptor | string       | `public` (default) or `private` | Hide a tool from the model while keeping it callable from the widget.                           |
| `_meta["openai/toolInvocation/invoking"]` | Tool descriptor | string       | ≤ 64 chars                      | Short status text while the tool runs.                                                          |
| `_meta["openai/toolInvocation/invoked"]`  | Tool descriptor | string       | ≤ 64 chars                      | Short status text after the tool completes.                                                     |
| `_meta["openai/fileParams"]`              | Tool descriptor | string[]     | —                               | List of top-level input fields that represent files (object shape `{ download_url, file_id }`). |

Example:

```ts
server.registerTool(
  "search",
  {
    title: "Public Search",
    description: "Search public documents.",
    inputSchema: {
      type: "object",
      properties: { q: { type: "string" } },
      required: ["q"],
    },
    securitySchemes: [
      { type: "noauth" },
      { type: "oauth2", scopes: ["search.read"] },
    ],
    _meta: {
      securitySchemes: [
        { type: "noauth" },
        { type: "oauth2", scopes: ["search.read"] },
      ],
      "openai/outputTemplate": "ui://widget/story.html",
      "openai/toolInvocation/invoking": "Searching…",
      "openai/toolInvocation/invoked": "Results ready",
    },
  },
  async ({ q }) => performSearch(q)
);
```

### Annotations

To label a tool as "read-only," please use the following [annotation](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) on the tool descriptor:

| Key               | Type    | Required | Notes                                                                                                                                                           |
| ----------------- | ------- | :------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `readOnlyHint`    | boolean | Required | Signal that the tool is read-only: it only retrieves or computes information and does not create, update, delete, or send data outside of ChatGPT.              |
| `destructiveHint` | boolean | Required | Declare that the tool may delete or overwrite user data so ChatGPT knows to elicit explicit approval first.                                                     |
| `openWorldHint`   | boolean | Required | Declare that the tool publishes content or reaches outside the current user’s account, prompting the client to summarize the impact before asking for approval. |
| `idempotentHint`  | boolean | Optional | Declare that calling the tool repeatedly with the same arguments will have no additional effect on its environment.                                             |

These hints only influence how ChatGPT frames the tool call to the user; servers must still enforce their own authorization logic.

Example:

```ts
server.registerTool(
  "list_saved_recipes",
  {
    title: "List saved recipes",
    description: "Returns the user’s saved recipes without modifying them.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
  },
  async () => fetchSavedRecipes()
);
```

Need more background on these fields? Check the [Advanced section of the MCP server guide](https://developers.openai.com/apps-sdk/build/mcp-server#advanced).

## Component resource `_meta` fields

Additional detail on these resource settings lives in the [Advanced section of the MCP server guide](https://developers.openai.com/apps-sdk/build/mcp-server#advanced).

Set these keys on the resource template that serves your component (`registerResource`). They help ChatGPT describe and frame the rendered iframe without leaking metadata to other clients.

| Key                                   |     Placement     | Type            | Purpose                                                                                                                                                                                                                          |
| ------------------------------------- | :---------------: | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_meta["openai/widgetDescription"]`   | Resource contents | string          | Human-readable summary surfaced to the model when the component loads, reducing redundant assistant narration.                                                                                                                   |
| `_meta["openai/widgetPrefersBorder"]` | Resource contents | boolean         | Hint that the component should render inside a bordered card when supported.                                                                                                                                                     |
| `_meta["openai/widgetCSP"]`           | Resource contents | object          | Define allowlists for the widget: `connect_domains` (network requests), `resource_domains` (images, fonts, scripts), optional `frame_domains` (iframe sources), and optional `redirect_domains` (openExternal redirect targets). |
| `_meta["openai/widgetDomain"]`        | Resource contents | string (origin) | Dedicated origin for hosted components (required for app submission; must be unique per app). Defaults to `https://web-sandbox.oaiusercontent.com`.                                                                              |

The `openai/widgetCSP` object supports:

- `connect_domains`: `string[]` – domains the widget may contact via fetch/XHR.
- `resource_domains`: `string[]` – domains for static assets (images, fonts, scripts, styles).
- `frame_domains?`: `string[]` – optional list of origins allowed for iframe embeds. By default, widgets cannot render subframes; adding `frame_domains` opts in to iframe usage and triggers stricter app review.
- `redirect_domains?`: `string[]` – optional list of origins that can receive `openExternal` redirects without the safe-link modal. When the destination matches, ChatGPT appends a `redirectUrl` query parameter pointing back to the current conversation.

## Tool results

The [Advanced section of the MCP server guide](https://developers.openai.com/apps-sdk/build/mcp-server#advanced) provides more guidance on shaping these response fields.

Tool results can contain the following [fields](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool-result). Notably:

| Key                 | Type                  | Required | Notes                                                                                           |
| ------------------- | --------------------- | -------- | ----------------------------------------------------------------------------------------------- |
| `structuredContent` | object                | Optional | Surfaced to the model and the component. Must match the declared `outputSchema`, when provided. |
| `content`           | string or `Content[]` | Optional | Surfaced to the model and the component.                                                        |
| `_meta`             | object                | Optional | Delivered only to the component. Hidden from the model.                                         |

Only `structuredContent` and `content` appear in the conversation transcript. `_meta` is forwarded to the component so you can hydrate UI without exposing the data to the model.

Host-provided tool result metadata:

| Key                               |            Placement            | Type   | Purpose                                                                                                                 |
| --------------------------------- | :-----------------------------: | ------ | ----------------------------------------------------------------------------------------------------------------------- |
| `_meta["openai/widgetSessionId"]` | Tool result `_meta` (from host) | string | Stable ID for the currently mounted widget instance; use it to correlate logs and tool calls until the widget unmounts. |

Example:

```ts
server.registerTool(
  "get_zoo_animals",
  {
    title: "get_zoo_animals",
    inputSchema: { count: z.number().int().min(1).max(20).optional() },
    _meta: { "openai/outputTemplate": "ui://widget/widget.html" },
  },
  async ({ count = 10 }) => {
    const animals = generateZooAnimals(count);

    return {
      structuredContent: { animals },
      content: [{ type: "text", text: `Here are ${animals.length} animals.` }],
      _meta: {
        allAnimalsById: Object.fromEntries(
          animals.map((animal) => [animal.id, animal])
        ),
      },
    };
  }
);
```

### Error tool result

To return an error on the tool result, use the following `_meta` key:

| Key                             | Purpose      | Type               | Notes                                                    |
| ------------------------------- | ------------ | ------------------ | -------------------------------------------------------- |
| `_meta["mcp/www_authenticate"]` | Error result | string or string[] | RFC 7235 `WWW-Authenticate` challenges to trigger OAuth. |

## `_meta` fields the client provides

See the [Advanced section of the MCP server guide](https://developers.openai.com/apps-sdk/build/mcp-server#advanced) for broader context on these client-supplied hints.

| Key                            | When provided           | Type            | Purpose                                                                                     |
| ------------------------------ | ----------------------- | --------------- | ------------------------------------------------------------------------------------------- |
| `_meta["openai/locale"]`       | Initialize + tool calls | string (BCP 47) | Requested locale (older clients may send `_meta["webplus/i18n"]`).                          |
| `_meta["openai/userAgent"]`    | Tool calls              | string          | User agent hint for analytics or formatting.                                                |
| `_meta["openai/userLocation"]` | Tool calls              | object          | Coarse location hint (`city`, `region`, `country`, `timezone`, `longitude`, `latitude`).    |
| `_meta["openai/subject"]`      | Tool calls              | string          | Anonymized user id sent to MCP servers for the purposes of rate limiting and identification |
| `_meta["openai/session"]`      | Tool calls              | string          | Anonymized conversation id for correlating tool calls within the same ChatGPT session.      |

Operation-phase `_meta["openai/userAgent"]` and `_meta["openai/userLocation"]` are hints only; servers should never rely on them for authorization decisions and must tolerate their absence.

Example:

```ts
server.registerTool(
  "recommend_cafe",
  {
    title: "Recommend a cafe",
    inputSchema: { type: "object" },
  },
  async (_args, { _meta }) => {
    const locale = _meta?.["openai/locale"] ?? "en";
    const location = _meta?.["openai/userLocation"]?.city;

    return {
      content: [{ type: "text", text: formatIntro(locale, location) }],
      structuredContent: await findNearbyCafes(location),
    };
  }
);
```