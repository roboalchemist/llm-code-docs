# Source: https://developers.notion.com/page/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

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

  We recommend reconnecting Notion MCP in your third-party AI tools to ensure you have the most up-to-date tools and resources, and as always, familiarizing yourself and your team with [security best practices](https://developers.notion.com/docs/mcp-security-best-practices).
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
  ### 📣 Important API update coming September 3rd

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
  ### What's New?

  * Revised **Section 1.1** to refine the scope of application of the [Developer Terms](https://www.notion.so/Developer-Terms-ba4131408d0844e08330da2cbb225c20).
  * Revised **Section 3.1** to clarify prohibited uses of the API and created a new **Section 3.2** for formatting purposes
</Update>

<Update label="September 11, 2024">
  ### What's New?

  We are excited to announce an update to our Notion Public API token format.

  Starting September 25, 2024, newly generated Public API tokens will automatically use the **`ntn_`** prefix instead of the\*\*`secret_`\*\* prefix.

  ### Why the Change?

  This change is part of our ongoing efforts to improve the security of our API. By introducing the **`ntn_`** prefix, we aim to:

  * Enhance compatibility with secret scanners and other security tools, making it easier to identify and manage Notion API tokens.
  * Provide a clearer distinction between Notion API tokens and other types of secrets, reducing the risk of misconfiguration and improving overall security.

  ### What Do You Need to Do?

  * New Integrations: For any new integrations, the tokens will be automatically generated with the **`ntn_`** prefix. Simply generate your tokens as usual through the Notion API settings page.
  * Existing Tokens: All existing tokens with the secret\_ prefix will continue to work without any changes. There is no immediate need to update your existing integrations.
  * Token Format: We strongly advise against using regular expressions (regex) to identify or validate Notion Public API tokens. The token format may change over time, and relying on regex patterns could lead to false positives or negatives. Instead, treat the token as an opaque string and use it as provided.
  * Best Practices: To handle Notion API tokens securely:
    * Store tokens securely using appropriate encryption methods.
    * Use Notion's official SDKs or libraries when available, as they handle token management correctly.
    * Validate tokens by making authenticated requests to Notion's API rather than parsing the token itself.

  ### Questions or Concerns?

  If you have any questions or need assistance with this transition, please feel free to reach out to our support team or visit our docs.
</Update>

<Update label="September 9, 2024">
  ### What's New?

  Revised **Section 3.1** of the [Developer Terms](https://www.notion.so/Developer-Terms-ba4131408d0844e08330da2cbb225c20) to include additional security and data use restrictions.
</Update>

<Update label="Changes for April 2024">
  ### What's New?

  * Added: New property `in_trash` to indicate whether a page/block/database has been deleted or placed in "Trash".
  * Support: Both `archived` and `in_trash` properties are fully supported. Contact developer support for help during this transition or reach out in our [Notion Devs Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg) group.
</Update>

<Update label="Changes for November 27 - December 10, 2023">
  ### What's New?

  * We added support for reading and writing names to `file` blocks in the public API. Read more here.
  * We fixed the types in the SDK to support appending `table` and `column` blocks as children of `toggle` blocks.
  * We updated the emoji and timezones available in the SDK.
  * We added support for `australian_dollar` in the `format` field of number database properties.
</Update>

<Update label="September 8 - September 21, 2023">
  ### What's New?

  * The [Examples](/page/examples) page was updated with all our most recent demo code. We’ve organized these sample integrations by level of experience with the Public API to help developers who are newer to the Public API find introductory code more easily.
  * A note was added to all API endpoint documentation directing developers to review the [Status codes](/reference/status-codes#error-codes) page for a complete list of error codes that can be returned by API requests.
  * A clarification was added to the [Request limits](/reference/request-limits) page and [Append block children endpoint](/reference/patch-block-children) documentation to indicate the current limit for appending a list of block children per API request. Up to 100 block children can be appended at a time.
</Update>

<Update label="September 6 - September 7, 2023">
  ### What's New?

  * The [updates](/page/changelog#notice-for-an-upcoming-public-api-change) related to the [Formulas 2.0 launch](https://twitter.com/NotionHQ/status/1699828805408550971?s=20) are now live in the Public API. These changes will not impact most developers using the Public API; however, please note that the formatting of [`formula.expression`](/reference/property-object#formula), which is returned when [retrieving a database](/reference/retrieve-a-database) with a [Formula property](/reference/property-object#formula), has changed. See Notion's Help Center articles for more information on the Formula 2.0 changes:
    * [Formulas 2.0: How to use Notion’s new and improved formulas with your existing setups](https://www.notion.so/help/guides/new-formulas-whats-changed)
    * [How to write Notion formulas that extend the capabilities of your databases](https://www.notion.so/help/guides/write-formulas-that-extend-capabilities-of-databases)
  * The example for the [Formula database property](/reference/property-object#formula) was updated to align with the new Formula 2.0 launch.
  * [New sample code](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript/intro-to-notion-api) was added to the [Notion SDK for JavaScript’s `examples`](https://github.com/makenotion/notion-cookbook/tree/main/examples/javascript) directory. This new example demonstrates how to use the Public API with basic and intermediate levels of difficulty.
</Update>

<Note>
  **Looking for older updates?**

  Changelog entries from before September 2023 are now kept in a separate page: [Historical changelog](/guides/resources/historical-changelog).
</Note>
