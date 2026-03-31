# Source: https://developers.notion.com/page/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

<Update label="March 30, 2026">
  ### Heading 4 block type

  [`heading_4`](/reference/block#headings) is now a supported block type. You can create, read, and update heading 4 blocks through the [Append block children](/reference/patch-block-children), [Retrieve a block](/reference/retrieve-a-block), and [Update a block](/reference/update-a-block) endpoints, matching the existing `heading_1`, `heading_2`, and `heading_3` block types.

  ### Tab item icons

  [Paragraph blocks](/reference/block#paragraph) that are direct children of [tab blocks](/reference/block#tab) now support an optional [`icon`](/reference/emoji-and-icon) field. You can set icons on tab items when creating tabs via [Append block children](/reference/patch-block-children) or [Create a page](/reference/post-page), and update them via [Update a block](/reference/update-a-block). Icons on paragraphs that are not tab items are rejected with a validation error.

  ### "me" relative filter for people properties

  [People filter conditions](/reference/filter-data-source-entries#people) now accept `"me"` as a value for `contains` and `does_not_contain`, in addition to user UUIDs. For [public integrations](/guides/get-started/getting-started#internal-vs-public-integrations), `"me"` resolves to the user who authorized the connection. For [internal integrations](/guides/get-started/getting-started#internal-vs-public-integrations), `"me"` does not resolve to a user — a `contains: "me"` filter will return no results and a `does_not_contain: "me"` filter will match all entries. Works across [database queries](/reference/post-database-query-filter#people), [data source queries](/reference/filter-data-source-entries#people), [view filters, and quick filters](/guides/data-apis/working-with-views#quick-filters).

  ### Relative date filter values

  Date filter conditions that accept an [ISO 8601 date](https://en.wikipedia.org/wiki/ISO_8601) string (`equals`, `before`, `after`, `on_or_before`, `on_or_after`) now also accept the following relative date values: `"today"`, `"tomorrow"`, `"yesterday"`, `"one_week_ago"`, `"one_week_from_now"`, `"one_month_ago"`, `"one_month_from_now"`. These are resolved at query time relative to the current date. See the [date filter reference](/reference/filter-data-source-entries#date) for details.

  ### View API fixes

  Several fixes to the [views API](/guides/data-apis/working-with-views):

  * **Percent-encoded property IDs**: Property IDs returned by the API (e.g. `%7DUlu`) are now correctly resolved when used in view filters, sorts, group-by, and other property references.
  * **`width: 0` rejected**: Column widths must now be at least `1`. A width of `0` was previously accepted but had no effect.
  * **Partial `properties` list**: Specifying a subset of properties in a view now correctly hides unlisted properties instead of showing all properties.

  **SDK support**: `@notionhq/client` [`v5.16.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.16.0) includes typed support for heading 4, tab item icons, and the `"me"` person filter value.
</Update>

<Update label="March 25, 2026">
  ### Tab block support

  [Tab blocks](/reference/block#tab) are now a supported block type in the API. Use tabs to organize content into labeled sections within a page.

  * **Read**: [Retrieve a block](/reference/retrieve-a-block) and [Retrieve block children](/reference/get-block-children) return tab blocks with `type: "tab"` and an empty `tab: {}` object. Each tab within the container is a [paragraph](/reference/block#paragraph) block — the `rich_text` is the tab label, the `icon` is the tab icon, and the `children` contain the tab's content.
  * **Create**: [Append block children](/reference/patch-block-children) accepts `type: "tab"` blocks. Each tab is a paragraph block with nested children and an optional `icon`. Only paragraph blocks can be direct children of a tab block.

  ### Writable verification property

  The [`verification`](/reference/page-property-values#verification) property on wiki database pages can now be set and updated via the [Create page](/reference/post-page) and [Update page](/reference/patch-page) endpoints. Set `state` to `"verified"` or `"unverified"`, with an optional `date` object for expiration. The `verified_by` field is automatically set to the acting integration and cannot be overridden.

  ### Native icons and custom emoji listing

  Two icon-related improvements:

  * **Native Notion icons**: A new `type: "icon"` variant is available on all [`icon`](/reference/emoji-and-icon#icon) fields (pages, databases, callout blocks). Specify an icon by `name` and optional `color` (defaults to `"gray"`). Previously, native icons were returned as `type: "external"` with SVG URLs — they are now returned in the structured `icon` format.
  * **Custom emoji listing**: A new [List custom emojis](/reference/list-custom-emojis) endpoint (`GET /v1/custom_emojis`) retrieves workspace custom emojis with cursor pagination and an optional `name` filter for exact-match lookups.

  **SDK support**: `@notionhq/client` [`v5.15.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.15.0) adds `notion.customEmojis.list()` and typed support for tab blocks, verification writes, and native icons.
</Update>

<Update label="March 19, 2026">
  ### Views API

  We've launched the [`/v1/views` API](/guides/data-apis/working-with-views). Eight new endpoints let integrations programmatically manage database views — the same view presets that users create in the Notion UI:

  * [Create](/reference/create-view), [retrieve](/reference/retrieve-a-view), [update](/reference/update-a-view), and [delete](/reference/delete-view) views on any database.
  * [List views](/reference/list-views) for a database or across the workspace by data source.
  * [Query a view](/reference/create-view-query) to fetch pages using the view's saved filter and sort configuration, with [pagination](/reference/get-view-query-results) support.

  [Supported view types](/guides/data-apis/working-with-views#view-configuration) include table, board, calendar, timeline, gallery, list, form, chart, map, and dashboard. Views can be configured with filters, sorts, [quick filters](/guides/data-apis/working-with-views#quick-filters), and type-specific layout settings like grouping, cover images, subtasks, and chart options.

  Dashboard views support a full grid layout with [widget placement](/guides/data-apis/working-with-views#widget-placement) — add, position, and remove widget views within rows.

  Three new [webhook events](/reference/webhooks/view-created) (`view.created`, `view.updated`, `view.deleted`) are available on API version `2025-09-03` and later.

  **SDK support**: `@notionhq/client` [`v5.14.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.14.0) adds `notion.views.*` and `notion.views.queries.*` methods.

  ### Status property support

  You can now [create and update status properties](/reference/property-object#status) through the Notion API and [Notion MCP](/guides/mcp/mcp). Previously, status properties were read-only — they could be queried but not created or modified via the API.

  * **Create**: pass `{ status: {} }` in a [Create database](/reference/create-database) or [Create data source](/reference/create-a-data-source) request to add a status property with default options (Not started, In progress, Done). Custom initial options are also supported.
  * **Update**: add new options to an existing status property via [Update data source](/reference/update-a-data-source), following the same pattern as select and multi\_select.
  * **MCP**: the `notion-create-database` and `notion-update-data-source` tools now support the `STATUS` column type in their schema definitions.
</Update>

<Update label="March 11, 2026">
  ### New API version: `2026-03-11`

  We've released **Notion API version `2026-03-11`** with three breaking changes that simplify and modernize the API surface:

  * **`after` replaced by `position`**: The [Append block children](/reference/patch-block-children) endpoint now uses a `position` object instead of a flat `after` string parameter, enabling more flexible block placement (including `start` and `end` positioning).
  * **`archived` replaced by `in_trash`**: All endpoints now use `in_trash` instead of `archived` in both request parameters and response bodies. The `archived` field was [deprecated in April 2024](/page/changelog#changes-for-april-2024) and is now fully removed in this version.
  * **`transcription` renamed to `meeting_notes`**: The `transcription` block type has been renamed to `meeting_notes` across all block endpoints.

  Most integrations only need simple find-and-replace updates. See the [upgrade guide](/guides/get-started/upgrade-guide-2026-03-11) for step-by-step instructions.

  **SDK support**: `@notionhq/client` [`v5.12.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.12.0) adds support for `2026-03-11`. Upgrade the SDK and set `notionVersion: "2026-03-11"` to opt in.

  ### Notion MCP: new view tools

  Two new tools are available in [Notion MCP](/guides/mcp/mcp):

  * **`notion-create-view`** — Create new database views with filters, sorts, grouping, display properties, and layout-specific settings (calendar, timeline, etc.).
  * **`notion-update-view`** — Update an existing view's configuration. Accepts `view://` URIs, Notion URLs with `?v=`, or bare UUIDs.

  See [Supported tools](/guides/mcp/mcp-supported-tools) for details and example prompts.

  ### Markdown content API improvements

  The [Update page markdown](/reference/update-page-markdown) endpoint now supports two additional command types:

  * **`update_content`** — Make targeted edits with an array of search-and-replace operations (`old_str` / `new_str`). Recommended for precise, multi-site edits.
  * **`replace_content`** — Replace the entire page content with new markdown in a single operation.

  We recommend `update_content` and `replace_content` over the older `insert_content` and `replace_content_range` commands. See [Working with markdown content](/guides/data-apis/working-with-markdown-content) for usage examples.

  ### Template timezone parameter

  The [Create page](/reference/post-page) and [Update page](/reference/patch-page) endpoints now accept an optional `timezone` field inside the `template` parameter. This controls how template variables like `@now` and `@today` resolve — for example, `"America/New_York"` ensures dates reflect Eastern Time instead of defaulting to UTC. See the [Creating pages from templates](/guides/data-apis/creating-pages-from-templates) guide for details.
</Update>

<Update label="March 2, 2026">
  * The [`GET /v1/pages/:page_id/markdown`](/reference/retrieve-page-markdown) endpoint is now available to **internal integrations** (workspace-level bots), in addition to public integrations.
  * Released [`v5.11.1`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.11.1) of our TS/JS SDK. `UnsupportedBlockObjectResponse` now includes a `block_type` string field indicating the underlying block type.
</Update>

<Update label="February 26, 2026">
  We released [`v5.10.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.10.0) and [`v5.11.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.11.0) of our SDK for JavaScript and TypeScript. Here's what's new in the Notion API:

  ### Markdown content API

  Three new endpoints let you create, read, and update page content using [enhanced markdown](/guides/data-apis/enhanced-markdown) instead of the block-based API:

  * [`POST /v1/pages`](/reference/post-page) now accepts a `markdown` parameter as an alternative to `children`.
  * [`GET /v1/pages/:page_id/markdown`](/reference/retrieve-page-markdown) retrieves a page's full content as enhanced markdown.
  * [`PATCH /v1/pages/:page_id/markdown`](/reference/update-page-markdown) inserts or replaces content using enhanced markdown with ellipsis-based selections.

  See [Working with markdown content](/guides/data-apis/working-with-markdown-content) and the [Enhanced markdown format reference](/guides/data-apis/enhanced-markdown) for details.

  ### AI meeting notes

  * The `GET /v1/pages/:page_id/markdown` endpoint supports an `include_transcript` query parameter to include full meeting note transcripts in the response.
  * Added support for the [`transcription` block type](/reference/block#transcription), enabling integrations to read AI meeting notes metadata — including title, status, calendar event details, and pointers to summary, notes, and transcript content blocks.

  ### SDK improvements

  * **Automatic retry with exponential backoff** — the SDK now retries failed requests automatically with configurable backoff ([v5.10.0](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.10.0)).
  * **Markdown endpoint methods** — `pages.retrieveMarkdown()` and `pages.updateMarkdown()` ([v5.11.0](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.11.0)).

  ### Notion MCP improvements

  Highlighting recent changes to [Notion MCP](https://developers.notion.com/docs/mcp):

  * Create and fetch **comments on blocks**, not just pages.
  * View **Notion Sites** pages via the fetch tool.
  * Fetch AI **meeting transcripts** and query meeting notes efficiently with the new `notion-query-meeting-notes` tool.
  * Fetch an **individual data source** by ID or URL within a database.
  * **\~91% context token reduction** in `notion-create-database` and `notion-update-data-source` tools by switching to SQL DDL-based schemas.
  * Added `update_verification` command to the `notion-update-page` tool.
  * Flattened `notion-update-page` tool parameters and fixed schema issues for improved compatibility with MCP clients.
  * **Enterprise governance**: audit logging for MCP tool usage and admin tool allowlisting.

  We recommend reconnecting Notion MCP in your third-party AI tools to ensure you have the most up-to-date tools and resources.
</Update>

<Update label="January 15, 2026">
  We [released `v5.7.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.7.0) of our SDK for JavaScript and TypeScript. Since the last changelog entry, we've added the following fixes and improvements to the Notion API:

  * Introduce [Move page](/reference/move-page) API to change the `parent` of an existing page.
  * TS/JS example projects extracted to a new open-source project: [`notion-cookbook`](https://github.com/makenotion/notion-cookbook/tree/main/examples).
  * Add support for [customizing the `position` of a new page](https://developers.notion.com/reference/post-page#choosing-a-parent) within the parent page.
  * New APIs to power the flow described in our [Creating pages from templates](/guides/data-apis/creating-pages-from-templates) guide:
    * Introduce [List data source templates](/reference/list-data-source-templates) endpoint.
    * Introduce [`template` parameter](https://developers.notion.com/reference/post-page#setting-up-page-content) to Create Page API.
    * Introduce [`template`](https://developers.notion.com/reference/patch-page#applying-a-page-template) and [`erase_content` parameters](https://developers.notion.com/reference/patch-page#erasing-content-from-a-page) to Update Page API.

  Highlighting recent LLM-facing changes to [Notion MCP](https://developers.notion.com/docs/mcp), our remote Model Context Protocol (MCP) server for AI tools:

  * Released `notion-query-data-sources` tool to Enterprise Notion workspaces with access to Notion AI.
  * Tool consolidation: `notion-get-user` has been removed & its functionality has been rolled into `notion-get-users`.
  * Fixed a bug causing child content to be deleted by the `notion-update-page` tool when using `replace_content` and `replace_content_range` modes.
  * Removed Notion-flavored Markdown specification from `notion-create-pages` tool to conserve context tokens, since it exists behind a dedicated MCP Resource as well.

  We recommend reconnecting Notion MCP in your third-party AI tools to ensure you have the most up-to-date tools and resources.
</Update>

<Update label="September 13, 2025">
  We [released `v5.1.0`](https://github.com/makenotion/notion-sdk-js/releases/tag/v5.1.0) of `@notionhq/client`, our SDK for JavaScript and TypeScript. This includes the following fixes and improvements:

  * Add support for `is_locked` boolean parameter on update page and database APIs (to update whether a page is locked in the Notion app UI)
  * `dataSource.update`: add support for changing a data source's `parent` database
  * Remove `page_id` as a possible `parent` for `CreateDataSourceBodyParameters`
  * Add `request_id` to Client log lines

  As noted in the [library's README](https://github.com/makenotion/notion-sdk-js?tab=readme-ov-file#requirements-and-compatibility), v5 and above of the SDK isn't compatible with API versions older than `2025-09-03`. See the [upgrade guide](/guides/get-started/upgrade-guide-2025-09-03) to learn more.
</Update>

<Update label="August 26, 2025">
  ### Important API update coming September 3rd

  We're introducing multi-source databases to Notion! Our new API version `2025-09-03` separates "**databases**" (containers) from "**data sources**" (tables), unlocking powerful new organizational capabilities.

  ### What you need to know:

  * Current integrations continue working with single-source databases
  * Update to the new API version to support multi-source databases
  * We're introducing the concept of API versioning to [integration webhooks](/reference/webhooks) as well

  Start upgrading your integrations now to ensure a smooth transition when users begin creating additional data sources starting from September 3rd.

  **Full details and migration guide**: [Upgrading to 2025-09-03](/guides/get-started/upgrade-guide-2025-09-03)

  **General information about API versioning**: [Versioning](/reference/versioning)
</Update>

<Update label="December 20, 2024">
  ### What's new

  * Revised **Section 1.1** to refine the scope of application of the [Developer Terms](https://www.notion.so/Developer-Terms-ba4131408d0844e08330da2cbb225c20).
  * Revised **Section 3.1** to clarify prohibited uses of the API and created a new **Section 3.2** for formatting purposes
</Update>

<Update label="September 11, 2024">
  ### What's new

  We are excited to announce an update to our Notion Public API token format.

  Starting September 25, 2024, newly generated Public API tokens will automatically use the **`ntn_`** prefix instead of the\*\*`secret_`\*\* prefix.

  ### Why the change?

  This change is part of our ongoing efforts to improve the security of our API. By introducing the **`ntn_`** prefix, we aim to:

  * Enhance compatibility with secret scanners and other security tools, making it easier to identify and manage Notion API tokens.
  * Provide a clearer distinction between Notion API tokens and other types of secrets, reducing the risk of misconfiguration and improving overall security.

  ### What do you need to do?

  * New Integrations: For any new integrations, the tokens will be automatically generated with the **`ntn_`** prefix. Simply generate your tokens as usual through the Notion API settings page.
  * Existing Tokens: All existing tokens with the secret\_ prefix will continue to work without any changes. There is no immediate need to update your existing integrations.
  * Token Format: We strongly advise against using regular expressions (regex) to identify or validate Notion Public API tokens. The token format may change over time, and relying on regex patterns could lead to false positives or negatives. Instead, treat the token as an opaque string and use it as provided.
  * Best Practices: To handle Notion API tokens securely:
    * Store tokens securely using appropriate encryption methods.
    * Use Notion's official SDKs or libraries when available, as they handle token management correctly.
    * Validate tokens by making authenticated requests to Notion's API rather than parsing the token itself.

  ### Questions or concerns?

  If you have any questions or need assistance with this transition, please feel free to reach out to our support team or visit our docs.
</Update>

<Update label="September 9, 2024">
  ### What's new

  Revised **Section 3.1** of the [Developer Terms](https://www.notion.so/Developer-Terms-ba4131408d0844e08330da2cbb225c20) to include additional security and data use restrictions.
</Update>

<Update label="Changes for April 2024">
  ### What's new

  * Added: New property `in_trash` to indicate whether a page/block/database has been deleted or placed in "Trash".
  * `in_trash` is the preferred field going forward. The `archived` property is a deprecated alias for `in_trash` and may be removed in a future API version. New integrations should use `in_trash` exclusively.
</Update>

<Update label="Changes for November 27 - December 10, 2023">
  ### What's new

  * We added support for reading and writing names to `file` blocks in the public API. Read more here.
  * We fixed the types in the SDK to support appending `table` and `column` blocks as children of `toggle` blocks.
  * We updated the emoji and timezones available in the SDK.
  * We added support for `australian_dollar` in the `format` field of number database properties.
</Update>

<Update label="September 8 - September 21, 2023">
  ### What's new

  * The [Examples](/page/examples) page was updated with all our most recent demo code. We've organized these sample integrations by level of experience with the Public API to help developers who are newer to the Public API find introductory code more easily.
  * A note was added to all API endpoint documentation directing developers to review the [Status codes](/reference/status-codes#error-codes) page for a complete list of error codes that can be returned by API requests.
  * A clarification was added to the [Request limits](/reference/request-limits) page and [Append block children endpoint](/reference/patch-block-children) documentation to indicate the current limit for appending a list of block children per API request. Up to 100 block children can be appended at a time.
</Update>

<Update label="September 6 - September 7, 2023">
  ### What's new

  * The [updates](/page/changelog#notice-for-an-upcoming-public-api-change) related to the [Formulas 2.0 launch](https://twitter.com/NotionHQ/status/1699828805408550971?s=20) are now live in the Public API. These changes will not impact most developers using the Public API; however, please note that the formatting of [`formula.expression`](/reference/property-object#formula), which is returned when [retrieving a database](/reference/retrieve-a-database) with a [Formula property](/reference/property-object#formula), has changed. See Notion's Help Center articles for more information on the Formula 2.0 changes:
    * [Formulas 2.0: How to use Notion's new and improved formulas with your existing setups](https://www.notion.so/help/guides/new-formulas-whats-changed)
    * [How to write Notion formulas that extend the capabilities of your databases](https://www.notion.so/help/guides/write-formulas-that-extend-capabilities-of-databases)
  * The example for the [Formula database property](/reference/property-object#formula) was updated to align with the new Formula 2.0 launch.
  * [New sample code](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/intro-to-notion-api) was added to the [Notion SDK for JavaScript's `examples`](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript) directory. This new example demonstrates how to use the Public API with basic and intermediate levels of difficulty.
</Update>

<Note>
  **Looking for older updates?**

  Changelog entries from before September 2023 are now kept in a separate page: [Historical changelog](/guides/resources/historical-changelog).
</Note>


Built with [Mintlify](https://mintlify.com).