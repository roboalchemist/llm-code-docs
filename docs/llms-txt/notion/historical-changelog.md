# Historical Changelog

View an archive of Notion Developers updates prior to September 2023

## 📘

View the current [Changelog](/page/changelog) for the newest updates.

This page is a historical archive of updates older than September 2023. This is kept separate from the current changelog to keep page navigation faster while retaining older updates.

## August 23 - September 5, 2023

- The [Working with databases guide](https://developers.notion.com/docs/working-with-databases) was revised to improve its readability and to make additional resources easier to find.
- Notion's [Postman collection](https://www.postman.com/notionhq/workspace/notion-s-api-workspace/collection/15568543-d990f9b7-98d3-47d3-9131-4866ab9c6df2) for the API was updated. Be sure to pull recent changes into your forked version.
- A reminder was added to the [Comments endpoints](https://developers.notion.com/reference/create-a-comment) to update [integration capabilities](https://developers.notion.com/reference/capabilities) for comments prior to using the endpoints. (Read/write comment capabilities are off by default and can be turned on in the [integration dashboard](https://www.notion.so/my-integrations).)
- General clean-up and improvements, including code formatting.

## August 8 - August 22, 2023

- The [Build your first integration](https://developers.notion.com/docs/create-a-notion-integration) guide was rewritten with new demo code to help developers learn how to use Notion’s API even faster.
  - A new [sample app](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express) was added to the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js/tree/main) directory. This completed sample app is referenced in the new [Build your first integration](https://developers.notion.com/docs/create-a-notion-integration) guide.
- The description for the `block_id` path parameter was updated for the [Append block children](https://developers.notion.com/reference/patch-block-children) endpoint to indicate that a block ID or page ID can be used.
- A clarification was added to [documentation](https://developers.notion.com/reference/retrieve-a-database) for retrieving/updating database properties: If a property is based on a relation to another database, the related database also needs to be shared with the integration.
- A clarification was added to documentation for [querying databases](https://developers.notion.com/reference/post-database-query-filter#multi-select). When filtering a multi-select property, the `contains` field will filter for exact matches for the string provided.
- The [Working with comments](https://developers.notion.com/docs/working-with-comments) guide was updated with additional examples to distinguish between creating page comments and inline discussion comments.
  - The [Create a comment](https://developers.notion.com/reference/create-a-comment) endpoint description now links to the Working with comments guide to help developers find additional resources faster.
- If you haven’t already, join our [Notion Devs Slack group](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg) to learn from other developers building with the public API.

### Notice for an upcoming Public API change

#### We will soon be rolling out changes to the Formulas property (Formulas 2.0), and as such, we will be making a change to the Notion Public API.

This is a non-versioned change and is expected to be in effect in the next couple weeks.

**tl;dr:** As part of the Formulas 2.0 rollout, the Public API’s format of the string value for [`formula.expression`](https://developers.notion.com/reference/property-object#formula) will be changing. Public API calls with formula inputs in the old format will still succeed. On write operations, the old format will be supported indefinitely, but on read, only the new format will be returned. This change is being made to improve the formulas experience and ensure parity with the Notion app.

No action is required for creating or updating database formulas. Reading database [`formula.expression`](https://developers.notion.com/reference/property-object#formula) values may require developer changes.

#### What do you need to know?

**The string value of `formula.expression` is changing; the schema is not.**

- **On write** via the Public API ([create](https://developers.notion.com/reference/create-a-database) or [update](https://developers.notion.com/reference/update-a-database) database endpoints), Notion will support using the old format as a Public API input in the formula property schema indefinitely _and_ will support writing in the **new** format.
- Database objects returned via the Public API will have the new formulas 2.0 format.

```javascript
// Old format
"Updated price": {
  "id": "YU%7C%40",
  "name": "Updated price",
  "type": "formula",
  "formula": {
    "expression": "prop(\"Price\") * 2
```
```

# Why is this happening?

Notion databases allow you to build a fully customizable system for you and your team – they provide a place where you can keep all your information in one place, with the ability to build views, filters, and workflows that can be adapted to your needs.

The formula property helps you take that even further – allowing you to perform calculations, create specialized views, and provide an extra layer of insight based on information in other database properties. It helps expand what you can do in Notion databases.

We are improving the formulas experience so that:

1. It’s easier to write formulas.
2. Formula outputs look and feel more native to Notion.
3. The formula language can fulfill more specific needs.

Changes being made to the API are to ensure parity with the Notion app.

## What do you need to do?

This is a non-versioned change that will not affect most developers. As mentioned, the formula property format will still have the same schema in the Public API; only the value of the `formula.expression` field will change.

Keep an eye on this changelog for when the update becomes available in the Public API.

## July 25 - August 7, 2023

- Notion is excited to announce our [Technology Partnership Program](https://www.notion.so/technology-partner-program). 🎉 This program is open to companies who have built a public integration (including Link Previews) and are interested in improving and scaling their integration with Notion’s support. If you think your integration and company could be a fit, [learn more and apply here](https://www.notion.so/technology-partner-program).
- We’ve updated our API reference docs to include information on Notion’s [wiki databases and verified pages](https://www.notion.so/help/wikis-and-verified-pages). Updates include:
  - An overview on wikis in the guide to [working with databases](https://developers.notion.com/docs/working-with-databases#properties).
  - The [verification](https://developers.notion.com/reference/page-property-values#verification) page property was added to the [Page properties](https://developers.notion.com/reference/page-property-values) documentation.
  - The [Create a database](https://developers.notion.com/reference/create-a-database) and [Query a database](https://developers.notion.com/reference/post-database-query) endpoint documentation was updated to reflect API changes related to wikis. Namely, that querying wiki databases can return both [Page](https://developers.notion.com/reference/page) and [Database](https://developers.notion.com/reference/database) objects.
- The [Error codes](https://developers.notion.com/reference/status-codes#error-codes) section in the [Status code](https://developers.notion.com/reference/status-codes) page was updated to include examples of the `message` returned with each type of API error, as well as descriptions of the issue each error code represents.
- A number of sample cURL commands in our docs were still using an old [Notion Version](https://developers.notion.com/reference/versioning) in their headers. These have all been updated.
- A clarification was added to the [Authorization guide](https://developers.notion.com/docs/authorization#making-api-requests-with-an-internal-integration) that the [Notion Version](https://developers.notion.com/reference/versioning) is always required in public API request headers.

## July 11 - July 24, 2023

- A new integration [example](https://github.com/makenotion/notion-sdk-js/tree/main/examples/parse-text-from-any-block-type) was added to the Notion SDK for JavaScript repo. This example shows how to get the plain text from any block type currently supported by the public API.
- The new unique ID page property was added to the [Page properties](https://developers.notion.com/reference/page-property-values) documentation. When used, the unique ID (`unique_id`) auto-increments for every new page created in a database. An optional prefix can be included that will be applied to the ID values.

![The unique ID in a Notion page's properties](https://files.readme.io/c599280-unique_id.png)

- Workspace Owners can now see _all_ internal integrations created in a workspace via the [integration dashboard](https://www.notion.so/my-integrations). This includes integrations created by themselves and other Workspace Owners. We’ve included this information in our [Getting Started](https://developers.notion.com/docs/getting-started#internal-integrations) guide.
- A [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) code sample was added to the [Create a database](https://developers.notion.com/reference/create-a-database) endpoint documentation.

## June 13 - July 10, 2023

- We updated our [Getting started guide](https://developers.notion.com/docs) to help developers who are new to the public API better understand how the API relates to integrations.
- The [Block object](https://developers.notion.com/reference/block#embed) docs were updated with a tip on how to embed Vimeo links in a Notion page via the API.
- A new `after` parameter has been added to the [Append block children](https://developers.notion.com/reference/patch-block-children) endpoint. Developers can now specify where to append a new block, instead of appending it to the end of a parent block by default.

```cURL
curl -X PATCH https://api.notion.com/v1/blocks/16d8004e-5f6a-42a6-9811-51c22ddada12/children \
  -H 'Authorization: Bearer $NOTION_API_KEY' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
    "children": [
    ...
    ],
    "after": "<block_id_to_append_after>"
}'
```

- The [Authorization guide](https://developers.notion.com/docs/authorization) had a clarification added to help developers find the resources they need for [Link Preview](https://developers.notion.com/docs/link-previews) integrations.
- The new `public_url` property was added to the docs. When a page or database has been shared publicly, the response body will include a `public_url` value.

```json
{
  "object": "page",
  "id": "<id>",
  "created_time": "2023-06-02T19:54:00.000Z",
  "last_edited_time": "2023-06-02T23:04:00.000Z",
  "created_by": { ... },
  "last_edited_by": { ... },
  "cover": null,
  "icon": null,
  "parent": { ... },
  "archived": false,
  "properties": { ... },
  "url": "<url>",
  "public_url": "<public-url>"
}
```

- The [Retrieve block children](https://developers.notion.com/reference/get-block-children) endpoint documentation was updated to help developers who are new to the public API better understand the endpoint’s functionality.
- The [Retrieve a block](https://developers.notion.com/reference/retrieve-a-block) endpoint documentation was updated with some additional information related to working with page content.
- The `invalid_grant` code was added to our [Status codes](https://developers.notion.com/reference/status-codes) documentation. This code is returned when the authorization grant (e.g., token) provided is invalid. For example, a status code `<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>` with an `<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>` code with an `<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>` code will be returned when the token provided has expired.
- The [Rich text](https://developers.notion.com/reference/rich-text) documentation was updated with additional information on what rich text is and how the Notion uses it.

## May 30 - June 12, 2023

- Our guides and docs related to Link Preview integrations have been updated to help developers find the information they need faster.
  - Improvements have been made to the following guides and API reference docs:
    - [Getting started guide](https://developers.notion.com/docs/getting-started)
    - [Introduction to Link Previews guide](https://developers.notion.com/docs/link-previews)
    - [Building a Link Preview integration guide](https://developers.notion.com/docs/build-a-link-preview-integration)
    - [Unfurl attribute object docs](https://developers.notion.com/reference/unfurl-attribute-object)
- We added more information about the `plain_text` property found in the `rich_text` object. Learn more about rich text in our [Rich text object](https://developers.notion.com/reference/rich-text) docs.
- The docs related to [filtering](https://developers.notion.com/reference/post-database-query-filter) and [sorting](https://developers.notion.com/reference/post-database-query-sort) database queries now have more code examples for developers building integrations with the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js).
- We reorganized the REST API reference navigation bar after removing the “Other” section to make its child pages easier to find.

## May 16 - May 29, 2023

- The [Query a database](https://developers.notion.com/reference/post-database-query) and [Filter database entries](https://developers.notion.com/reference/post-database-query-filter) docs were updated with additional code examples of passing single and multiple filters.
- The [Working with comments](https://developers.notion.com/docs/working-with-comments) guide was updated to clarify how to retrieve and add comments using the REST API.
- The references docs for `rollup` [page properties](https://developers.notion.com/reference/page-property-values#rollup), as well as the [Retrieve a page property](https://developers.notion.com/reference/retrieve-a-page-property) and [Retrieve a page](https://developers.notion.com/reference/retrieve-a-page) endpoints were updated with additional information related to limitations. In cases where a page property — like a rollup — has more than 25 references, the [Retrieve a page property](https://developers.notion.com/reference/retrieve-a-page-property) endpoint must be used to receive a complete response.
- An outdated Changelog URL now redirects to this Changelog page to help avoid confusion.

## May 2 - May 15, 2023

- We added a database schema size recommendation of **50KB** to our docs to help developers manage their database query performance. It is strongly recommended that developers keep their schema size under this number.
- The [Update a database](https://developers.notion.com/reference/update-a-database) page was updated to improve readability. Additional information on how this endpoint differs from related endpoints was also added to help developers better navigate the REST API docs.
- The [Query a database](https://developers.notion.com/reference/post-database-query#errors) page was updated with additional information about the `filter_properties` query parameter.
  When used with the REST API, this query parameter is passed as a string, like so:

```cURL
https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]&filter_properties=[property_id_2]
```

When used with the [JavaScript SDK](https://github.com/makenotion/notion-sdk-js), the `filter_properties` option accepts an array of property ID strings:

```javascript
notion.databases.query({
  database_id: 'databaseID',
  filter_properties: ['propertyID1', 'propertyID2']
})
```

- Docs that mention the `redirect_uri` — a value used with [public integrations](https://developers.notion.com/docs/authorization#what-is-a-public-integration) — were updated to clarify when this value is required. Refer to the [authorization guide](https://developers.notion.com/re
```

# Backwards Compatibility

*   The [Create a token](https://developers.notion.com/reference/create-a-token) page for a complete description.
*   The video block-type was updated on the [Block Object](https://developers.notion.com/reference/block#video) page to clarify accepted video types. YouTube URLs that contain `<button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">watch</code>` or `<button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">embed</code>` are supported video types.
*   The [Append a block](https://developers.notion.com/reference/patch-block-children) page content was reorganized to improve readability.

## April 18 - May 1, 2023

*   The [Build a Link Preview integration guide](https://developers.notion.com/docs/build-a-link-preview-integration) was updated to reflect a change regarding how link previews are enabled in the [integration dashboard](https://www.notion.so/my-integrations).
*   The [versioning page](https://developers.notion.com/reference/versioning) was updated to clarify that the `<button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Notion-Version</code>` header is required in Notion REST API requests.
*   The [parent object page](https://developers.notion.com/reference/parent-object) and API reference docs for [database POST requests](https://developers.notion.com/reference/create-a-database) and [blocks PATCH requests](https://developers.notion.com/reference/patch-block-children) were updated to better explain how parenting rules work.
*   The [Integration guide](https://developers.notion.com/docs/create-a-notion-integration) was updated with more links to help developers find resources faster.
*   Number database properties now support the Peruvian sol as a currency format. To use it, set `peruvian_sol` as the value for a number’s `format` field when creating or updating a database property or [schema](https://developers.notion.com/reference/property-schema-object#number-configuration).
*   General docs housekeeping, such reducing the number of callouts in our API reference docs to improve the readability.

## March 14 - April 17, 2023

*   Our developer community Slack invite link was updated. [Join here](https://join.slack.com/t/notiondevs/shared_invite/zt-1tjam81wh-BGaZXHUY83DpLNjZwKEiGg) to connect with other developers building with the Notion API.
*   The [Authorization guide](https://developers.notion.com/docs/authorization) was updated to include more information on creating integrations, adding templates to public integrations, and more code examples to get you started, faster.
*   We’ve added more code examples to our API reference docs, including [Archive a page](https://developers.notion.com/reference/archive-a-page) and [Authentication](https://developers.notion.com/reference/authentication).
*   General docs housekeeping, such reducing the number of callouts in our API reference docs to improve the readability.

## February 28 - March 13, 2023

We don’t have any changes to announce this week! Stay tuned, and in the meantime check out our platform roadmap for a look at what we’re building.

## February 14 - 27, 2023

### Fixes and improvements

*   You can now update [rollup database properties](https://developers.notion.com/reference/property-object#rollup) via the API. To programmatically update a `rollup` property, send a PATCH to [Update a database](https://developers.notion.com/reference/update-a-database) that specifies the change in the `properties` body param.

## January 31 - February 13, 2023

We don’t have any updates to share right now. Stay tuned for the next changelog! To get a sense for what we’re heads down working on, check out the [platform roadmap](https://developers.notion.com/page/notion-platform-roadmap#updated-march-2-2022).

## January 18 - 30, 2023

### Fixes and improvements

*   Happy 2023!

### New things

*   Added a token `Refresh` button to the settings page for internal integrations. Click `Refresh` to generate a new token for your internal integration.

![You can now refresh an internal integration token from the integration settings page.](https://files.readme.io/b1d6c0c-2023-01-13_10.58.16.gif)

## January 3 - 17, 2023

### New things

*   Shipped detailed docs for Link Previews including an [overview](https://developers.notion.com/docs/link-previews), [getting started guide](https://developers.notion.com/docs/build-a-link-preview-integration), and [reference materials](https://developers.notion.com/reference/unfurl-attribute-object).

## December 19, 2022 - January 2, 2023

### Fixes and improvements

*   The [Retrieve a Page endpoint](https://developers.notion.com/reference/retrieve-a-page#errors) can now return specific page property values when you include the `filter_properties` path param.
*   You can now request specific page property values from a database by passing `filter_properties` in the request body to the [Query a database endpoint](https://developers.notion.com/reference/post-database-query).

### New things

*   Happy 2023! For a sneak peek of what we’ll be up to this year, check out our updated [platform roadmap](https://developers.notion.com/page/notion-platform-roadmap).

## December 6 - 18, 2022

### Fixes and improvements

*   Updated the [Append block children](https://developers.notion.com/reference/patch-block-children) and [Retrieve block children](https://developers.notion.com/reference/get-block-children) endpoints to specific supported block types to create a more consistent dev experience. The endpoints now throw an error if the block type in the request does not [support children](https://developers.notion.com/reference/block#block-types-that-support-children).

### New things

*   Built a ✨Glitch ✨ demo that updates Notion tasks when a linked GitHub PR is closed or merged. [Give it a spin!](https://glitch.com/~notion-task-github-pr-sync)

## November 22 - December 5, 2022

We took advantage of the US Thanksgiving holiday to host a mini internal hackathon.

Nothing to share from that, yet! It’s been a quiet few weeks.

If you want something to read while you stay tuned for the next update, check out the revised [Get started](https://developers.notion.com/docs/getting-started) guide.

## November 8 - 21, 2022

*   We added a `this_week` filter for database queries. You can now search for database entries where the `"date"`, `"created_time"`, or `"last_edited_time"` property value falls within the current week. Refer to the [date filter condition](https://developers.notion.com/reference/post-database-query-filter#date-filter-condition) docs for details.

## October 25 - November 7, 2022

*   Number database properties now support the Singapore dollar as a currency format. To use it, set `"singapore_dollar"` as the value for a number’s `format` field when creating or updating a database [property](https://developers.notion.com/reference/property-object#number-configuration) or [schema](https://developers.notion.com/reference/property-schema-object#number-configuration).

## October 11 - 24, 2022

*   You can now add a Notion template option to a public integration from the [integration’s settings page](https://www.notion.so/my-integrations). For details on what the permissions flow looks like for users who opt in to the template, refer to the [Authorization guide](https://developers.notion.com/docs/authorization#permissions-flow-for-integrations-with-a-notion-template-option).

## September 26 - October 10, 2022

*   A [`relation`](https://developers.notion.com/reference/property-value-object#relation-property-values) property value now includes a `has_more` property when returned by the [Retrieve a page endpoint](https://developers.notion.com/reference/retrieve-a-page). `has_more` is `true` if the `relation` has more than 25 page references. Otherwise, `has`
```

# More</code> is <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">false</code>.

- We added a <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">workspace_name</code> property to <a href="https://developers.notion.com/reference/user#bots" target="" title="">bot user objects</a>. If the bot  <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">owner.type</code> is "workspace", then  <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">workspace.name</code> identifies the name of the workspace that owns the bot. If the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">owner.type</code> is "user", then  <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">workspace.name</code> is  <code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">null</code>.

## September 12 - 25, 2022

Started an experiment to improve <a href="https://developers.notion.com/reference/post-search" target="" title="">search endpoint</a> performance by tweaking how we call Elasticsearch under the hood.

## August 29 - September 11, 2022

- Fixed a bug where date mentions ended in a <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">→</code> character even if they only represented a single date, not a date range.
- Added an <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Authorization URL</code> field to the public integration form. You can now click to copy the URL that allows users to authorize your integration (read more in the <a href="https://developers.notion.com/docs/authorization#prompting-users-to-add-an-integration" target="" title="">Authorization guide</a>). 
- Corrected an error that caused the <a href="https://developers.notion.com/reference/retrieve-a-page-property" target="" title=""><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">getProperty</code></a> endpoint to return only one item if the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">property_id</code> belonged to a multi-item <a href="https://developers.notion.com/reference/property-item-object#files-property-values" target="" title=""><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">Files</code></a> page property.

## August 31, 2022

### Version 2022-06-28 includes page property types and values

Responses for page retrievals, database queries, and searches will again include page property types and values. This matches the behavior in version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">2022-02-22</code> and takes effect on August 31, 2022.

## August 15 - 28, 2022

### Features

- The public API now supports the following functionality for <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">status</code> properties:

  - Reading and updating <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">status</code> properties on pages (<a href="https://developers.notion.com/reference/property-value-object#status-property-values" target="" title="">read more</a>)
  - Reading, but not updating, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">status</code> property configuration on databases (<a href="https://developers.notion.com/reference/property-object#status-configuration" target="" title="">read more</a>)
  - Filtering or sorting by <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">status</code> properties when querying databases (<a href="https://developers.notion.com/reference/post-database-query-filter#status-filter-condition" target="" title="">read more</a>)

- <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">header_1</code>, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">header_2</code>, and <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">header_3</code> blocks now have an <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">is_toggleable</code> property, to better indicate whether they are heading toggle blocks. (<a href="https://developers.notion.com/reference/block#heading-one-blocks" target="" title="">read more</a>)

  - Headings can be togglified and un-togglified by setting <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">is_toggleable</code> to true or false, but note that all the children inside the toggle must be removed before it can be untogglified.

## August 1 - 14, 2022

No updates for these past two weeks, but stay tuned for the next changelog!

## July 18 - July 31, 2022

### Features

- Added support for <a href="/reference/retrieve-a-comment" target="" title="">reading</a> and <a href="/reference/create-a-comment" target="" title="">writing</a> page-level comments in the API.

## July 19, 2022

### Comments API

Today we're launching a brand new set of APIs for interacting with Notion comments. This includes the ability to:

- Read comments from a page or block.
- Add a comment to a page.
- Add a comment to an existing discussion thread on a block.

For more information, check out the new <a href="/docs/working-with-comments" target="" title="" class="doc-link" data-sidebar="working-with-comments">guide</a> or dive straight into the <a href="/reference/create-a-comment" target="" title="">API reference</a>.

## July 5 - 17, 2022

### Features

- Released a new version of the API, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">2022-06-28</code>. Previous versions of the API are still supported. Read more about the new version <a href="https://developers.notion.com/changelog/releasing-notion-version-2022-06-28" target="" title="">here</a>.
- Created a new template repository for getting started with the Notion API and the official SDK. <a href="https://github.com/makenotion/notion-sdk-typescript-starter" target="" title="">Find it here.</a>

### Bug fixes and performance improvements

- Exported many more named types for API response objects in the <a href="https://github.com/makenotion/notion-sdk-js" target="" title="">official SDK</a>.
- Fixed a bug in the official SDK where some API requests would not work due a capitalization issue. (This was a community-submitted PR; thank you @dvanoni!)

## July 6, 2022

### Releasing Notion-Version 2022-06-28

**Update from August 31, 2022**: Page properties can now be retrieved using the page, query database, and search endpoints, in addition to the page properties endpoint.

Today we’re releasing Notion-Version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">2022-06-28</code> with the following backwards incompatible changes:

- Page properties must be retrieved using the page properties endpoint.
- Parents are now always direct parents; a parent field has been added to block.
- Database relations have a type of <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">single_property</code> and <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">dual_property</code>.

Read more about each of these changes below.

#### Page properties must be retrieved using the page properties endpoint

Previously, the <a href="/reference/page" target="" title="">page object</a> returned from page endpoints, as well as the query database and search endpoint, returned a <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">properties</code> field that contained all the page’s properties along with its value:

```json
"properties": {
    "Name": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "Avocado",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "Avocado",
          "href": null
        }
      ]
   }
}
```

While convenient, returning accurate results for all properties resulted in bad performance and timeouts for larger databases or pages with lots of mentions. To combat performance, on March 1st, we <a href="/reference/property-value-object" target="" title="">added a disclaimer</a> that page objects stopped returning accurate results for pages with more than 25 mentions to other objects (which affected properties of type <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">title</code>, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">rich_text</code>, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">relation</code>, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">people</code>, <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">rollup</code>, and <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">formula</code>). In October 2021, <a href="https://developers.notion.com/changelog/retrieve-page-property-values" target="" title="">we introduced</a> a way to more accurately retrieve individual page properties via the <a href="/reference/retrieve-a-page-property" target="" title="">retrieve a page property item endpoint</a>. With this endpoint, we’re able to paginate complex properties that involve additional look-ups.

With version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">2022-06-28</code>, the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">type</code> and <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">property</code> value from page objects are removed. Thus moving forward, all property value retrieval must happen through the retrieve a page property item endpoint.

#### New Version Response

```json
"properties"
```
```

# June 20 - July 4, 2022

## Features

- Added limited readonly support for database status properties. Read more about status properties [here](https://www.notion.so/help/guides/status-property-gives-clarity-on-tasks).
  - Status property values are returned in the [Retrieve a page](/reference/retrieve-a-page) endpoint. See [Property values](/reference/property-value-object) for more information.
  - Status property configuration is not supported yet. See [Property object](/reference/property-object) for more information.

## Bug Fixes

- Added a validation for adding new rollup properties that prevents creating a rollup of another rollup.

# June 6 - June 19, 2022

## Features

- Added support for creating inline databases with `is_inline`. Read more [here](https://developers.notion.com/reference/database).
- Added support for reading and writing database descriptions with the `description` field. Read more [here](https://developers.notion.com/reference/database).

# May 23 - June 5, 2022

## Bug fixes and performance improvements

- The public API once again supports inline `mailto` links in rich text.

# May 9 - 22, 2022

## Bug fixes and performance improvements

- We now validate URLs used to create inline text links in the public API. For more details on inline links in rich text, see the [Rich text object](/reference/rich-text) documentation.
- The [Search](/reference/post-search) endpoint now returns fuzzier matches, including plurals and different verb tenses. This corresponds to fuzzier matches while searching in the Notion app and should result in more search results overall for any given query.
- Fixed a bug where the integration page at [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) wouldn't load.

# May 10, 2022

## Link Preview APIs

Today we’re excited to launch a new set of APIs for developers to build on — Link Preview APIs. Over the past six months, we launched link previews with tools like Slack, Trello, Figma, and Asana, allowing users to preview authenticated content in a new structured block. Now, we’re ready for any developer to build integrations that support link previews in Notion.

We built link previews to make it easy for users to easily share information in one place using a link. But with a regular link, the information would become automatically stale, making it difficult to share the latest updates among teams. Now, with the new link previews APIs, Notion will let you know when a user pastes a link to a domain you own, let the user authenticate with Notion and your service, and let you unfurl a new link preview block inside Notion.

Learn more about the new link previews APIs [here](https://developers.notion.com/page/link-previews-api), and apply to get access to and build your integration by filling out [this form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).

# April 25 - May 9, 2022

## Bug fixes and performance improvements

- We've shipped a couple of improvements under the hood to make the search and query database endpoints faster. We're actively looking into 500s and timeouts on the query database endpoint in particular.
- Fixed a bug in the OAuth page picker where Shared pages wouldn't load until the workspace switcher was clicked.

# April 11 - 24, 2022

## Bug fixes and performance improvements

- Fixed a bug where some rollups and relations appeared empty when they shouldn't have.
- Fixed a bug in the query database endpoint where an invalid pagination cursor was being returned.

# March 28 - April 10, 2022

There was a [company-wide product bug bash](https://www.notion.so/releases)! As a result nothing API-specific to share for these 2 weeks, but we've been hard at work improving test coverage and paring down tech debt.

# March 14 - 27, 2022

## Features

- You can now filter databases on the created at and last edited at timestamps, even if they don't have a corresponding property of that type. Read more [here](https://developers.notion.com/reference/post-database-query-filter#timestamp-filter-object).
- A [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) response header is now being sent with rate limited request responses. The value of this field is set as an integer number of seconds (in decimal). Requests made after waiting this minimum amount of time should not be rate limited. Read more about our rate limits [here](https://developers.notion.com/reference/request-limits#rate-limits).

## Bug fixes and performance improvements

- Stopped throwing an error when rendering property formulas that hadn't been set up yet in the [Retrieve a page property item](/reference/retrieve-a-page-property) endpoint. These formulas now return `null` values.

# March 18, 2022

## Query a database endpoint supports filtering by timestamp

When [querying a database](/reference/post-database-query) using filters, you previously were only able to build filters using properties that were explicitly defined in the database schema. We've added a new type of filter for the created timestamp and last edited timestamp of any page within the database. This means you can filter by these attributes, even if the database doesn't have a "Created time" or "Last edited time" _property_.

You can read more about this filter type [here](/reference/post-database-query-filter#timestamp-filter-object), but as a preview here is how you would filter by the created timestamp:

```json
{
    "filter": {
        "timestamp": "created_time",
        "created_time": {
          "past_week": {}
        }
    }
}
```

And here's how you would filter by the last edited time:

```json
{
    "filter": {
        "timestamp": "last_edited_time",
        "last_edited_time": {
          "past_week": {}
        }
    }
}
```
```

## February 28, 2022 - March 13, 2022

### Features

- Block colors are now supported in the API! Read more about it [here](https://developers.notion.com/changelog/block-colors-are-now-supported-in-the-api).

### Bug fixes and performance improvements

- Rich text objects now properly include template mentions. Read more about this type of text object [here](https://developers.notion.com/reference/rich-text#template-mentions).

## March 8, 2022

### Block colors are now supported in the API

We have added support for block colors in the Notion Public API. There is now a `color` keyword for the following block types: `paragraph`, `heading_1`, `heading_2`, `heading_3`, `bulleted_list_item`, `numbered_list_item`, `to_do`, `toggle`, `callout`, `quote`, and `table_of_contents`. For these block types, the block color is returned in the [block object](/reference/block), and you can use the [update block](/reference/update-a-block), [append block children](/reference/append-block-children), and [create page](/reference/post-page) endpoints to update the color of existing blocks and create new blocks with color.

The colors supported are `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `pink`, `red`, `gray_background`, `brown_background`, `orange_background`, `yellow_background`, `green_background`, `blue_background`, `purple_background`, `pink_background`, and `red_background`.

### Example Block

```json
{
    "object": "block",
    "id": "79bc0ae2-b002-4ecd-92db-870354734aaf",
    "created_time": "2022-03-03T22:49:00.000Z",
    "last_edited_time": "2022-03-03T22:49:00.000Z",
    "created_by": {
        "object": "user",
        "id": "914ff1b3-45c7-48dc-b2c2-be37d21e7695"
    },
    "last_edited_by": {
        "object": "user",
        "id": "914ff1b3-45c7-48dc-b2c2-be37d21e7695"
    },
    "has_children": false,
    "archived": false,
    "type": "callout",
    "callout": {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": "This block has color!",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "This block has color!",
                "href": null
            }
        ],
        "icon": {
            "type": "emoji",
            "emoji": "💡"
        },
        "color": "green_background"
    }
}
```

## March 7, 2022

### Updated Developers Terms

With the API officially out of beta, Notion has updated our developer terms of service as of March 1st, 2022. View our updated terms [here](https://www.notion.so/notion/Developer-Terms-ba4131408d0844e08330da2cbb225c20).

## February 14, 2022 - 28, 2022: Block by Block edition!

> 📘The API is officially out of beta!
>
> Read more about it [here](https://www.notion.so/blog/api-ga).

### Features

- We now have a [roadmap](https://developers.notion.com/page/notion-platform-roadmap), so you have a better sense of what we'll be building next.
- We released a new version of the API, `2022-02-22`. This version makes our requests and responses more consistent across properties, blocks, and filters, and officially deprecates the list databases endpoint. Read more [here](https://developers.notion.com/changelog/releasing-notion-version-2022-02-22).
- We now show the public API status independently of Notion's status on [https://status.notion.so/](https://status.notion.so/).
- Added `created_by` and `edited_by` to pages, blocks, and databases, and added `archived` to databases. Read more [here](https://developers.notion.com/changelog/created-by-and-last-edited-by-properties-in-block-page-and-database-objects).
- Added new ways for admins of Enterprise workspaces to view and control the integrations installed in their workspaces. Read more [here](https://www.notion.so/help/add-and-manage-integrations-with-the-api).
- Added more information to paginated responses to make it easier to fetch complete responses for complex property types. Read more [here](https://developers.notion.com/reference/pagination).

### Bug fixes and performance improvements

- Fixed a bug where pages and databases with archived (i.e. trashed) ancestors would show `archived: false`. They now show `archived: true` because they are, in fact, archived.
- Improved API performance when rendering users who are members in the space. This affects all user, block, and page-related endpoints since users can be mentioned in both page properties and rich text.
- Added a message about sharing relevant pages and databases with a bot in the 404 not found error message. We found that this was one of the more common reasons for API users to get a 404 when calling the API.
- Fixed a bug where bots could be given a more restrictive "Can edit content" access on child databases, which prevented some bots with write access from being able to update the database schema.
- Fixed a bug where user mentions failed with "user not found" when creating new blocks, even if those users should have been visible to the bot.
- Fixed a bug where malformed properties in a single page would cause an entire request to the query database endpoint to fail.
- Fixed a bug where it was possible to update a page/database in the trash. Attempting to update a trashed page or database now returns a validation error.
- Fixed a bug in the get page property endpoint where retrieving a rollup property which referenced a relation containing pages the bot did not have access to skipped those pages and returned an incorrect result. We now return a validation error.
- Fixed a bug in the get page property endpoint where retrieving a formula property whose depth exceeds what we can compute in the API simply returned the wrong value. We now return a validation error.

## March 1, 2022

### Created by and last edited by properties in Block, Page and Database objects

We have added `created_by` and `last_edited_by` properties for [block](/reference/block), [page](/reference/page) and [database objects](/reference/database) corresponding to the users who have created or last edited these objects. Both properties are [user objects](/reference/user) which will contain `object` and `id` keys. This is a backwards compatible change that is available in older versions of the API as well.
```

# Tasks

## February 25, 2022

### Releasing Notion-Version 2022-02-22

> **📘**
>
> As a reminder, we only version backwards incompatible changes, so generally, you still get access to new features we release on the API without needing to upgrade. You can use different version headers for each request, so you can upgrade incrementally to get to the latest version.

We're releasing Notion-Version `2022-02-22` with the following _backwards incompatible_ changes:

- `text` in blocks has been renamed to `rich_text`, to be consistent with the database property type.
- Query database filter changes:
  - `phone` and `text` are no longer supported in query database filters when filtering by `phone_number` and `rich_text` properties. Use `phone_number` and `rich_text` instead.
  - `rollup` query database filters no longer accept the `text` keyword. Use `rich_text` instead.
  - `formula` query database filters no longer accept the `text` keyword. Use `string` instead.
- `property_item` objects now return a `type`, `next_url`, and `id`.
- Deprecated the List Databases API endpoint.

#### The `text` property in content blocks has been renamed to `rich_text`

To be consistent with the database property type, we have renamed the `text` property to `rich_text`. This affects the following block types: `paragraph`, `heading_1`, `heading_2`, `heading_3`, `callout`, `quote`, `bulleted_list_item`, `numbered_list_item`, `to_do`, `toggle`, `code`, `template`.

Here is an example of the previous `text` property:

```json
{
  "type": "paragraph",
  //...other keys excluded
  "paragraph": {
    "text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
    }]
  }
}
```

Here is an example of the updated `rich_text` property:

```json
{
  "type": "paragraph",
  //...other keys excluded
  "paragraph": {
    "rich_text": [{
      "type": "text",
      "text": {
        "content": "Lacinato kale",
        "link": null
      }
    }]
  }
}
```

#### Query database filter changes

> **_<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>_**`phone` and `text` no longer supported

Version 2022-02-22 no longer supports `phone` and `text` property filters in the query database endpoint. For consistency with the database property types, use `phone_number` and `rich_text` instead when filtering on `phone_number` and `rich_text` properties.

More concretely, this query database filter will throw a validation error:

```json
{
	"filter": {
		"and": [
			{
				"property": "Phone number",
				"phone": {
					"equals": "1112223333"
				}
			}
		]
	}
}
```

This query database filter will succeed:

```json
{
	"filter": {
		"and": [
			{
				"property": "Phone number",
				"phone_number": {
					"equals": "1112223333"
				}
			}
		]
	}
}
```

> **_<button aria-label="Copy Code" class="rdmd-code-copy fa"></button>_**`rollup` property filters accept `rich_text` instead of `text`

Rollup property filters must now be constructed with the `rich_text` keyword instead of the `text` keyword if the value of the rollup is an array of `rich_text`. Put concretely, if a page's rollup property is rendered like so:

```json
{
	"rollup": [
		"Text value"
	]
}
```

```json
{
	"rollup": [
		"Rich text value"
	]
}
```

# Code

```json
"rollup property": {
	"id": "~",
	"type": "rollup",
	"rollup": {
		"type": "array",
		"array": [
			{
				"type": "rich_text",
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "update text 2",
							"link": null
						},
						"annotations": {
							"bold": true,
							"italic": false,
							"strikethrough": false,
							"underline": false,
							"code": false,
							"color": "red"
						},
						"plain_text": "update text 2",
						"href": null
					}
				]
			},
			{
				"type": "rich_text",
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "another text",
							"link": null
						},
						"annotations": {
							"bold": false,
							"italic": false,
							"strikethrough": false,
							"underline": false,
							"code": false,
							"color": "default"
						},
						"plain_text": "another text",
						"href": null
					}
				]
			}
		],
		"function": "show_original"
	}
}
```

This filter will no longer work in version 2022-02-22:

```json
{
	"filter": {
		"property": "rollup property",
		"rollup": {
			"any": {
				"text": {
					"contains": "update text"
				}
			}
		}
	}
}
```

Instead, write:

```json
{
	"filter": {
		"property": "rollup property",
		"rollup": {
			"any": {
				"rich_text": {
					"contains": "update text"
				}
			}
		}
	}
}
```

* * *

## Property list items now have types

Property item lists now always have type `property_item`. Rollup aggregations are now returned inside that type.

We've also added the property `id` field and the `next_url` to fetch the next set of property items.

Here is an example of a previous `rollup` `property_item` list:

```json
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "type": "relation",
      "relation": {
        "id": "83f92c9d-523d-466e-8c1f-9bc2c25a99fe"
      }
    },
    ...
  ],
  "next_cursor": "some-next-cursor-value",
  "has_more": true,
  "rollup": {
    "type": "date",
    "date": {
      "start": "2021-10-07T14:42:00.000+00:00",
      "end": null
    },
    "function": "latest_date"
  },
  "type": "rollup"
}
```

Here is an example of the updated `rollup` `property_item` list:

```json
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "id": "xYz890",
      "type": "relation",
      "relation": {
        "id": "83f92c9d-523d-466e-8c1f-9bc2c25a99fe"
      }
    },
    ...
  ],
  "next_cursor": "some-next-cursor-value",
  "has_more": true,
  "type": "property_item",
  "property_item": {
    "id": "aBcD123",
    "next_url": "https://api.notion.com/v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75/properties/aBcD123?start_cursor=some-next-cursor-value",
    "type": "rollup",
    "rollup": {
      "type": "date",
      "date": {
        "start": "2021-10-07T14:42:00.000+00:00",
        "end": null
      },
      "function": "latest_date"
    }
  }
}
```

* * *

## Deprecated the List Databases endpoint

List all [Databases](/reference/database) endpoint is removed starting in this version. You can use the [Search API](/reference/post-search) for this functionality instead. The List Databases endpoint only returns explicitly shared databases, while search will also return child pages and databases within explicitly shared pages.

## January 31, 2022 - February 13, 2022

> 📘We're trying something new
>
> We're experimenting with publishing biweekly changelogs in addition to our existing changelogs about new features. The biweekly changelogs will include bug fixes and improvements that are not big enough to justify their own changelog entry.
>
> The timing may be somewhat irregular until we smooth the process out, but we hope to align on a regular schedule soon. This is our first regular changelog entry; we hope you find it useful.

### Bug fixes and performance improvements

- We added an optimization for search when filtering by pages or databases. This should particularly help latency when using search to power a database picker in a large workspace. For more details about search and how to optimize search requests, see the [search documentation](https://developers.notion.com/reference/post-search).
- We fixed an issue where fetching an embed block containing an uploaded file returned the wrong file URL.

## January 25, 2022

### Caption property is now supported for code block type

We have added support for adding, updating, and retrieving the `caption` property for `code` block types.

Below is an example response from [append block children](/reference/patch-block-children) containing a code block, with a caption, uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "code",
            "code": {
                "caption": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Hello Caption!",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Hello Caption!",
                        "href": null
                    }
                ],
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "const foo = \"bar\"",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "const foo = \"bar\"",
                        "href": null
                    }
                ],
                "language": "javascript"
            }
        },
    ],
    "next_cursor": null,
    "has_more": false
}
```

## January 5, 2022

We have added support for simple tables in the API.

### Simple tables and simple table rows

Tables are parent blocks for table row children. They can only contain children of type `table_row`.

When creating a table block via the [Append block children](/reference/patch-block-children) endpoint, the `table` must have at least 1 `table_row` whose `cells` array has the same length as the `table_width`.

To fetch content for a `table`, fetch the the `table`, fetch the `table_row`'s `cell`'s `text` and `annotation` properties.

* * *
```

# Table Row

`table_row` children via [Retrieve block children](/reference/get-block-children). The `table` block itself only contains formatting data, no content.

## Table Block Example

```json
{
	"type": "table",
	"table": {
		"table_width": 3,
		"has_column_header": false,
		"has_row_header": false
	}
}
```

## Table Row Block Example

```json
{
  "type": "table_row",
  "table_row": {
    "cells": [
      [
        {
          "type": "text",
          "text": {
            "content": "column 1 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 1 content",
          "href": null
        }
      ],
      [
        {
          "type": "text",
          "text": {
            "content": "column 2 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 2 content",
          "href": null
        }
      ],
      [
        {
          "type": "text",
          "text": {
            "content": "column 3 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 3 content",
          "href": null
        }
      ]
    ]
  }
}
```

For more details, refer to the [Block object](/reference/block) docs.

## December 15, 2021

Both public and internal integrations now support having more granular capabilities, which enforce what an integration can do and see in a Notion workspace. These capabilities when put together enforce which API endpoints an integration can call, and what content and user related information they are able to see. For further information on capabilities and best practices, see the [capabilities reference](/reference/capabilities).

### Content Capabilities

Integrations can have any combination of read content, insert content, or update content capabilities.

- The **read content** capability gives the integration access to read existing content in a Notion workspace.
- The **insert content** capability gives the integration permission to create new content in a Notion workspace.
- The **update content** capability gives the integration permission to update existing content in a Notion workspace.

### User Capabilities

Integrations have different levels of user capabilities, which affect how [user objects](/reference/user) are returned from the Notion API:

- No user information - the integration will not be able to request any information about users. User objects will not include information about the user, including name, profile images, or their email address.
- User information without email addresses - user objects will include other information about the user, including their name or profile images, but omit the email address.
- User information with email addresses - user objects will include all information about the user, including name, profile images, and their email address.

### Limitations

An installed integration can never supersede the capabilities of the user who owns the integration. For example, an integration cannot insert or update on a page if the owner has read-only access.

### Existing Integrations

All existing integrations will continue to have the same functionality as before. Any integrations created before December 15, 2021 automatically will have all content capabilities, and user capabilities that give access to user information including email addresses.

### Updating Integrations

Update the capabilities on an existing integration through [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations). After updating a public integration's capabilities, users will need to re-authenticate with the integration to apply the new capabilities to their installation. After re-authenticating a public integration with changed capabilities, or updating an internal integration with changed capabilities, the new capabilities will apply to all pages already shared with the integration. For more information on setting capabilities see the [Authorization](/docs/authorization) guide.

## December 14, 2021

### Time Zone Support

We have added an optional `time_zone` field (based on the [IANA database](https://www.iana.org/time-zones) time zone values) to the Date objects. Developers can now explicitly set the time zones of Date property values using the `time_zone` field. Once this property is set explicitly, users will be able to see the same time zone in the app. When time zone information is provided in this method, `start` and `end` cannot contain [UTC offsets](https://en.wikipedia.org/wiki/UTC_offset)s. In addition when time zone information is provided in dates, `start` and `end` cannot be dates without time information (i.e. `"2020-12-08"`).

The public API will always return the `time_zone` field as `null` when rendering dates and time zone will be displayed as a [UTC offset](https://en.wikipedia.org/wiki/UTC_offset) in the `start` and `end` date fields.

## November 17, 2021

### Synced Block, Link to Page and Template Block Types Are Now Supported in the API

We have added support for adding and retrieving `synced_block`, `link_to_page`, and `template` block types.
```

;quot;results&quot;: [
        {
            &quot;object&quot;: &quot;block&quot;,
            &quot;id&quot;: &quot;block_id&quot;,
            &quot;created_time&quot;: &quot;2021-11-17T22:17:00.000Z&quot;,
            &quot;last_edited_time&quot;: &quot;2021-11-17T22:17:00.000Z&quot;,
            &quot;has_children&quot;: true,
            &quot;archived&quot;: false,
            &quot;type&quot;: &quot;synced_block&quot;,
            &quot;synced_block&quot;: {
                &quot;synced_from&quot;: {
                    &quot;type&quot;: &quot;block_id&quot;,
                    &quot;block_id&quot;: &quot;original_synced_block_id&quot;
                }
            }
        }
    ],
    &quot;next_cursor&quot;: null,
    &quot;has_more&quot;: false
]
```

> 🚧Important notes
>
> 1. The bot must have access to both the original and reference synced blocks
> 2. Similar to the UI, we don't support changes to <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">synced_from</code> at this time

#### link_to_page block type

We have added support for adding and retrieving <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">link_to_page</code> block types. Using this block type, developers can now create page links to other pages (using the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">page_id</code> property) and full page databases (using the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">database_id</code> property).

Below is an example request body for the [append block children](https://www.notion.so/reference/patch-block-children) endpoint containing a <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">link_to_page</code> block type.

```json
{
    "children": [
        {
            "type": "link_to_page",
            "link_to_page": {
                "type": "page_id",
                "page_id": "61cca5bd-c8c6-4fcc-b517-514da3b8b1e0"
            }
        }
    ]
}
```

#### template block type

We have added support for adding and retrieving <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">template</code> block types. Using this block type, developers can now create templates that duplicate their children blocks.

Below is an example request body for the [append block children](https://www.notion.so/reference/patch-block-children) endpoint containing a <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">template</code> block type.

```json
{
    "children": [
        {
            "type": "template",
            "template": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Create callout template"
                        }
                    }
                ],
                "children": [
                    {
                        "callout": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": "Placeholder callout text"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```

November 10, 2021

The public API now supports returning <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">link_preview</code> blocks and mentions found in <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">rich_text</code>! Previously these blocks had type <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">unsupported</code> and mentions were skipped in <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">rich_text</code>. Note: <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">link_preview</code>s cannot be created via the API, only returned in responses.

See the documentation in [blocks](https://www.notion.so/reference/block#link-preview-blocks) and [rich_text](https://www.notion.so/reference/rich-text#link-preview-mentions) for more information.

```json
{
  "type": "link_preview",
  //...other keys excluded
  "link_preview": {
    "url": "https://github.com/example/example-repo/pull/1234"
  }
}
```

October 25, 2021

We have added support for <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column_list</code> and <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column</code> block types.

You can now add Column Lists and Columns to pages and other block types.

Column Lists are parent blocks for column children. They can only contain children of type <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column</code>.

Columns are parent blocks for any supported block children, excluding <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column</code>s. They can only be appended to <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column_list</code>s.

When initially creating a column list block via [Append block children](https://www.notion.so/reference/patch-block-children), the column list must have at least 2 columns, and those columns must have at least one child each.

When fetching content for a column_list, first fetch the the column children via [Retrieve block children](https://www.notion.so/reference/get-block-children). Then fetch the children for each column block.

Below is an example request body for appending <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column_list</code> and nested <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column</code> children.

```json
{
  "children": [
    {
      "object": "block",
      "type": "column_list",
      "column_list": {
        "children": [
          {
            "object": "block",
            "type": "column",
            "column": {
              "children": [
                {
                  "object": "block",
                  "type": "paragraph",
                  "paragraph": {
                    "text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "some text here"
                        }
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "object": "block",
            "type": "column",
            "column": {
              "children": [
                {
                  "object": "block",
                  "type": "paragraph",
                  "paragraph": {
                    "text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "some text here"
                        }
                      }
                    ]
                  }
                }
              ]
            }
          ]
        ]
      }
    }
  ]
}
```

Below is an example response of appending <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column_list</code> children.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "ca042aa7-2e23-4541-8059-abff360d6752",
            "created_time": "2021-10-25T17:00:00.000Z",
            "last_edited_time": "2021-10-25T17:00:00.000Z",
            "has_children": true,
            "archived": false,
            "type": "column_list",
            "column_list": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

Below is an example request body for appending <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column</code> children. Note that the parent that is being added to must be a block of type <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column_list</code>.

```json
{
    "children": [
        {
            "object": "block",
            "type": "column",
            "column": {
                "children": [
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": "some text here"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```

Below is an example response of appending <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">column</code> children.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "f40c3a13-30d1-4594-bd6f-cdbc15b2c006",
            "created_time": "2021-10-25T21:25:00.000Z",
            "last_edited_time": "2021-10-25T21:25:00.000Z",
            "has_children": true,
            "archived": false,
            "type": "column",
            "column": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

October 18, 2021

### Validation on embed block URLs

The public API will now return errors on embeds blocks that are not supported by the public API. The supported embed block types (as listed and kept up to date in the [Block Object](https://www.notion.so/reference/block#embed-blocks) documentation):

- Framer
- Twitter (tweets)
- Google Drive documents
- Gist
- Figma
- Invision
- Loom
- Typeform
- Codepen
- PDFs
- Google Maps
- Whimisical
- Miro
- Abstract
- Excalidraw
- Sketch
- Replit 

Previously failed embeds would return a successful request, but produce an error in the Notion Application. Failed embed requests will now return a 400 Client Error.

For non embed URLs, consider using the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">bookmark</code> or <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="" name="" tabindex="0">image</code> block types.

October 17, 2021

### Dates with times and timezones are now supported on Database Date Filters

Dates with times and timezones are now supported on Database Date Filters.
```

# Supported on Database Date Filters

Previously, the date filters `equals`, `after`, `before`, `on_or_after`, and `on_or_before` only supported dates without times or timezones.

```json
{
    "filter": {
        "or": [
            {
                "property": "My Time Property",
                "date": {
                    "before": "2021-10-20"
                }
            }
        ]
    },
    "sorts": []
}
```

Now the database date filters can accept ISO 8601 dates with timestamps and timezones.

```json
{
    "filter": {
        "or": [
            {
                "property": "My Time Property",
                "date": {
                    "before": "2021-10-15T12:00:00-07:00"
                }
            }
        ]
    },
    "sorts": []
}
```

> **How Dates with times are compared**
>
> Date time comparisons are done with millisecond precision. If no timezone is provided, the default is UTC.

> **Equals Date filter**
>
> If a date without a time is provided to the `equals`, the comparison is done against the start and end of the UTC date provided (inclusive). If a date with a time is provided, the comparison is done with millisecond precision. If no timezone is provided, the default timezone is UTC.

## October 15, 2021

### Breadcrumb block types are now supported in the API

We have added support for adding and retrieving `Breadcrumb` block types.

You can now add Breadcrumb blocks to pages and other blocks.

Below is an example response from [Append block children](/reference/patch-block-children) containing a Breadcrumb block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "breadcrumb",
            "breadcrumb": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## October 14, 2021

### Table of contents and divider block types are now supported

We have added support for adding and retrieving `Table of Contents` and `Divider` block types.

#### Table of Contents blocks

You can now add Table of Contents blocks to pages and other blocks.

Below is an example response from [Append block children](/reference/patch-block-children) containing a Table of Contents block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "table_of_contents",
            "table_of_contents": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

#### Divider blocks

You can now add Divider blocks to pages and other blocks.

Below is an example response from [Append block children](/reference/patch-block-children) containing a Divider block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "divider",
            "divider": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## October 11, 2021

### Users can now add Equation Blocks, Embed, Bookmark, and Media Blocks

We have added support for retrieving, adding, and updating Equation Blocks. We have also added support for updating Embed, Bookmark, and Media (including image, video, audio, file, PDF) block types.

#### Equation Blocks

You can now add, retrieve, and update equation blocks when using the [Append block children](/reference/patch-block-children), [Retrieve block children](/reference/get-block-children), and [Update block](/reference/update-a-block) API endpoints.

Below is an example response from [Append block children](/reference/patch-block-children) containing an equation block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "2d97bf53-7e79-4efd-a6b2-53c0026ed1b5",
            "created_time": "2021-10-11T17:56:00.000Z",
            "last_edited_time": "2021-10-11T17:56:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "equation",
            "equation": {
                "expression": "e = mc^2"
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

#### Media Blocks (video, audio, image, file, PDF)

You can now update media blocks when using the [Update block](/reference/update-a-block).

> **Only media blocks of type external are supported**
>
> Updated Media blocks must be of type "external" and must reference an external URL. File upload is not currently supported.

Below is an example response from [Update block](/reference/update-a-block) containing a video block uploaded to Notion.

```json
{
    "object": "block",
    "id": "37af9d6e-290a-488b-9d53-fb4b983f8289",
    "created_time": "2021-10-12T23:11:00.000Z",
    "last_edited_time": "2021-10-12T23:12:00.000Z",
    "has_children": false,
    "archived": false,
    "type": "video",
    "video": {
        "caption": [
            {
                "type": "text",
                "text": {
                    "content": "My caption",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "My caption",
                "href": null
            }
        ],
        "type": "external",
        "external": {
            "url": "https://www.youtube.com/watch?v=aA7si7AmPkY"
        }
    }
}
```

#### Embed and Bookmark Block Types

You can now update embed and bookmark blocks when using the [Update block](/reference/update-a-block).

Below is an example response from [Update block](/reference/update-a-block) containing a bookmark block uploaded to Notion.

```json
{
    "object": "block",
    "id": "050010f8-d164-4f5d-85a0-fc9db4598107",
    "created_time": "2021-10-12T23:05:00.000Z",
    "last_edited_time": "2021-10-12T23:06:00.000Z",
    "has_children": false,
    "archived": false,
    "type": "bookmark",
    "bookmark": {
        "caption": [
            {
                "type": "text",
                "text": {
                    "content": "My caption",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "My caption",
                "href": null
            }
        ],
        "url": "http://www.notion.so"
    }
}
```

## October 7, 2021

### Users can now add and update Callout and Quote block types

> **New API endpoints and block types not supported in older versions of the API as of September 28**
>
> As of September 28, 2021, new block types and API endpoints will _not_ be supported in older versions of the API.
```

# Upgrade Notice

If you're currently on version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>2021-05-11</code> or <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>2021-05-13</code>, upgrade to <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>2021-08-16</code> to take advantage of the new block types in this changelog and any other block types or endpoints introduced after September 28.

API functionality introduced before September 28 will continue to work with older API versions.

We have added support for retrieving, adding and updating quote and callout block types.

## Quote blocks

You can now add and retrieve quote blocks when using [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

Below is an example response from [Append block children](/reference/patch-block-children) containing a quote block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-07T19:21:00.000Z",
            "last_edited_time": "2021-10-07T19:21:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "quote",
            "quote": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "The digital revolution is far more significant than the invention of writing or even of printing.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "The digital revolution is far more significant than the invention of writing or even of printing.",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "\n-Douglas Engelbart",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "\n-Douglas Engelbart",
                        "href": null
                    }
                ]
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## Callout blocks

You can now add and retrieve callout blocks when using [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

Below is an example response from [Retrieve block](/reference/retrieve-a-block) containing a callout block uploaded to Notion.

```json
{
    "object": "block",
    "id": "block-id",
    "created_time": "2021-10-07T19:23:00.000Z",
    "last_edited_time": "2021-10-07T19:24:00.000Z",
    "has_children": false,
    "archived": false,
    "type": "callout",
    "callout": {
        "text": [
            {
                "type": "text",
                "text": {
                    "content": "Note: Something special is happening above",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "Note: Something special is happening above",
                "href": null
            }
        ],
        "icon": {
            "type": "emoji",
            "emoji": "💡"
        }
    }
}
```

## October 5, 2021

### Retrieve page property item

Developers can now individually retrieve the value of their page properties with the [Retrieve a page property](/reference/retrieve-a-page-property) endpoint! This includes pagination through a list of property item objects for properties with long values or lots of page references such as formula, relations and rollups. See the [documentation](/reference/retrieve-a-page-property) for more info.

Use the [Retrieve a database](/reference/retrieve-a-database) endpoint to obtain the `property_id`.

**Simple Property Types**

Most properties will be identified by a `type` with the property value in the object found in key `{type}`.

_Example Request/Response_

```bash
curl --request GET \
  --url http://localhost:3000/v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75/properties/some-property-id \
  --header 'Authorization: Bearer $NOTION_API_KEY' \
  --header 'Notion-Version: 2021-08-16'
```

```json
{
  "object": "property_item",
  "type": "number",
  "number": 2
}
```

**Paginated Property Types**

Properties of type `title`, `rich_text`, `relation` and `people` will return a paginated list of `Property Item Objects`.

_Example List Response_

```json
{
    "object": "list",
    "results": [
        {
            "object": "property_item",
            "type": "rich_text",
            "rich_text": {
                "type": "text",
                "text": {
                    "content": "Avocado",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "Avocado",
                "href": null
            }
        },
        ...
    ],
    "next_cursor": "some-next-cursor-value",
    "has_more": true
}
```

**Rollup Property Types**

Rollups of type `'Show Original'`, `'Show unique'`, `'Count unique'` and `'Median'` return a flattened list of property items. All other rollups are returned a list of relations and (after pagination) a `rollup property value` of type `date` or `number`.

_Example Paginated Property Item Request/Response_

A rollup page property with an aggregation that requires additional pagination.

```bash
curl --request GET \
  --url http://localhost:3000/v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75/properties/some-property-id?page_size=10&amp;start_cursor=some-cursor-value \
  --header 'Authorization: Bearer $NOTION_API_KEY' \
  --header 'Notion-Version: 2021-08-16'
```

```json
{
    "object": "list",
    "results": [
        {
            "object": "property_item",
            "type": "relation",
            "relation": {
                "id": "de5d73e8-3748-40fa-9102-f1290fe2444b"
            }
        },
        {
            "object": "property_item",
            "type": "relation",
            "relation": {
                "id": "164325b0-4c9e-416b-ba9c-037b4c9acdfd"
            }
        },
        {
            "object": "property_item",
            "type": "relation",
            "relation": {
                "id": "456baa98-3239-4c1f-b0ea-bdae945aaf33"
            }
        }
      ...
    ],
    "next_cursor": "some-next-cursor-value",
    "has_more": true,
    "rollup": {
        "type": "date",
        "date": {
            "start": "2021-10-07T14:42:00.000+00:00",
            "end": null
        },
        "function": "latest_date"
    },
    "type": "rollup"
}
```

## October 4, 2021

### Retrieve your token's bot user with GET /v1/users/me

If you're using Notion API version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>2021-08-16</code>, you can now retrieve information about the bot associated with your API token, including its ID and the user who authorized it.

**Example request**

```bash
curl --request GET \
  --url http://localhost:3000/v1/users/me \
  --header 'Authorization: Bearer $NOTION_API_KEY' \
  --header 'Notion-Version: 2021-08-16'
```

**Example response**

```json
{
  "object": "user",
  "id": "16d84278-ab0e-484c-9bdd-b35da3bd8905",
  "name": "pied piper",
  "avatar_url": null,
  "type": "bot",
  "bot": {
    "owner": {
      "type": "user",
      "user": {
        "object": "user",
        "id": "5389a034-eb5c-47b5-8a9e-f79c99ef166c",
        "name": "christine makenotion",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "christine@makenotion.com"
        }
      }
    }
  }
}
```

## October 1, 2021

### New functionality not available to old API versions; code, inline databases, and database page block

> 🚧
> 
> New functionality not available to old API versions; code, inline databases, and database page block
```

# 🚧

**New API endpoints and block types not supported in older versions of the API as of September 28**

As of September 28, 2021, new block types and API endpoints will _not_ be supported in older versions of the API. If you're currently on version `2021-05-11` or `2021-05-13`, upgrade to `2021-08-16` to take advantage of the new block types in this changelog and any other block types or endpoints introduced after September 28.

API functionality introduced before September 28 will continue to work with older API versions.

We have added support for retrieving, adding and updating code blocks, inline databases and database page blocks.

## Code blocks

You can now retrieve and add code blocks when using [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

Below is an example response from [Retrieve block children](/reference/get-block-children) containing a code block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "ee27cd42-eaad-467f-9956-c0aa4efa94b5",
            "created_time": "2021-09-22T20:27:00.000Z",
            "last_edited_time": "2021-09-27T19:25:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "code",
            "code": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "const a = 21\nconst b = a + 5",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "const a = 21\nconst b = a + 5",
                        "href": null
                    }
                ],
                "language": "javascript"
            }
        },
    ],
    "next_cursor": null,
    "has_more": false
}
```

## Inline databases and database page blocks

You can now retrieve child database blocks when using [Retrieve block children](/reference/get-block-children) and [Retrieve block](/reference/retrieve-a-block).

> **📘**
>
> Updating `child_database` blocks
>
> To update `child_database` type blocks, use the [Update database](/reference/update-a-database) endpoint. Updating the block's `title` updates the text displayed in the associated `child_database` block.

Below is an example response from [Retrieve block children](/reference/get-block-children) containing a child database uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "0d6ff4f9-1211-4129-ab4a-19dfc33d4d7a",
            "created_time": "2021-09-27T20:25:00.000Z",
            "last_edited_time": "2021-09-27T20:25:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "child_database",
            "child_database": {
                "title": "My child database"
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## September 21, 2021

### Workspace-level tokens for public integrations will be deprecated soon; migrate your OAuth flows

Starting today, we will be changing who can authorize public integrations in Notion workspaces. The previously released authorization method will be fully deprecated on October 19.

#### About the change

Currently, OAuth tokens function on a workspace level: only admins in a workspace can grant access, and there can only be one token per workspace per integration. After a brief transition period (see "How to prepare for this change" below), we will be switching exclusively to user-level tokens. These can be granted by any admin or member in the workspace, and there can be as many tokens per workspace as there are admins and members in the workspace.

See the table for the differences between these two methods:

|  | Workspace-level tokens (old) | User-level tokens (new) |
| --- | --- | --- |
| Who can go through OAuth and grant access | Admins only | Admins and members |
| Number of access tokens per workspace | 1 | Up to N, where N is the number of admins and members |
| Who can go through OAuth and reauthorize access for a given token | Only the original user who went through OAuth to grant the token | Only the original user who went through OAuth to grant the token |
| OAuth token response | Contains an `owner` field with the value `{ workspace: true }` | Contains an `owner` field with the value `{ user: <API user object > }` |
| What resources an integration has access to | Pages/databases the installing user chooses via the page picker during OAuth; pages/databases the installing user and other users in the workspace share with the integration via the Page menu; children of pages/databases that were shared with the integration | Pages/databases the installing user chooses via the page picker during OAuth; pages/databases the installing user shares with the integration via the Page menu; children of pages/databases that were shared with the integration |
| What an integration can do with resources it has access to | Read and write | Read and write |

#### How to prepare for this change:

This change only affects public integrations; that is, integrations that can be installed across many workspaces via OAuth. It does not affect internal integrations.

1. Ensure that you can store and handle multiple Notion API tokens per workspace where your integration is granted access. You may map tokens directly to the `bot_id` which is returned in the OAuth token response and is guaranteed to be unique per API token.
   - To avoid overwriting tokens, do not map the token to the `workspace_id` returned in the OAuth token response, since a workspace may have multiple tokens. Do not map the token to the `owner.user.id` in the OAuth token response, since a user may install your integration in multiple workspaces.
2. Add `&owner=user` to your OAuth authorization URL (the url starting with `https://api.notion.com/v1/oauth/authorize`) once your application is ready for user-level tokens.

#### What to expect on October 19

On October 19, we will migrate all existing workspace-level tokens to user-level tokens. We will also default to creating user-level tokens when a user goes through OAuth, regardless of the `owner` parameter in the OAuth URL.

## September 17, 2021

### Database objects now contain url

[Database objects](/reference/database) now return the web address of the database in the `url` key.

```curl
{
  "object": "database",
  "id": "668d797c-76fa-4934-9b05-ad288df2d136",
  "created_time": "2020-03-17T19:10:04.968Z",
  "last_edited_time": "2020-03-17T21:49:37.913Z",
  "parent": {
    "type": "page_id",
    "page_id": "48f8fee9-cd79-4180-bc2f-ec0398253067"
  },
  "icon": {
    "type": "emoji",
    "emoji": "🎉"
  },
  "cover": {
    "type": "external",
    "external": {
    	"url": "https://website.domain/images/image.png"
    }
  },
  "url": "https://www.notion.so/668d797c76fa49349b05ad288df2d136",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Grocery List",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Grocery List",
      "href": null
    }
  ],
  "properties": {
    "Name": {
      "id": "title",
      "type": "title",
      "title": {}
    },
    "Description": {
      "id": "J@cS",
      "type": "rich_text",
      "rich_text": {}
    },
    "In stock": {
      "id": "{xY`,
      "type": "checkbox",
      "checkbox": {}
    },
    "Food group": {
      "id": "TJmr",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "96eb622f-4b88-4283-919d-ece2fbed3841",
            "name": "🥦Vegetable",
            "color": "green"
          },
          {
            "id": "bb443819-81dc-46fb-882d-ebee6e22c432",
            "name": "🍎Fruit",
            "color": "red"
          },
          {
            "id": "7da9d1b9-8685-472e-9da3-3af57bdb221e",
            "name": "💪Protein",
            "color": "yellow"
          }
        ]
      }
    },
    "Price": {
      "id": "cU^N",
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Cost of next trip": {
      "id": "p:sC",
      "type": "formula",
      "formula": {
        "value": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
      }
    },
    "Last ordered": {
      "id": "\\R[",
      "type": "date",
      "date": {}
    },
    "Meals": {
      "type": "relation",
      "relation": {
        "database": "668d797c-76fa-4934-9b05-ad288df2d136",
        "synced_property_name": null
      }
    },
    "Number of meals": {
      "id": "Z\\Eh",
      "type": "rollup",
      "rollup": {
        "rollup_property_name": "Name",
        "relation_property_name": "Meals",
        "rollup_property_id": "title",
        "relation_property_id": "mxp^",
        "function": "count"
      }
    },
    "Store availability": {
      "type": "multi_select",
      "multi_select": {
        "options": [
          [
            {
              "id": "d209b920-212c-4040-9d4a-bdf349dd8b2a",
              "name": "Duc Loi Market",
              "color": "blue"
            },
            {
              "id": "70104074-0f91-467b-9787-00d59e6e1e41",
              "name": "Rainbow Grocery",
              "color": "gray"
            },
            {
              "id": "e6fd4f04-894d-4fa7-8d8b-e92d08ebb604",
            
```

## September 10, 2021

### Users can now delete Block objects

The Notion API now supports the [Delete a block](https://developers.notion.com/reference/delete-a-block) endpoint for all supported block types (include pages). The endpoint mirrors the behavior in the Notion application UI where items are added to the "Trash" bucket. In addition, the [Block object](https://developers.notion.com/reference/block) now returns a boolean `archived` field to denote if the block has been deleted.

After deleting (archiving) the block, it can be unarchived using the [Update a block](https://developers.notion.com/reference/update-a-block) or [Update page](https://developers.notion.com/reference/patch-page) endpoint with the body `archived: false`.

#### Example Request

```bash
curl 'https://api.notion.com/v1/blocks/9bc30ad4-9373-46a5-84ab-0a7845ee52e6' \
  -H 'Authorization: Bearer $NOTION_API_KEY' \
  -H 'Notion-Version: 2021-08-16'
  -X DELETE \
```

#### Example Response

```json
{
  "object": "block",
  "id": "9bc30ad4-9373-46a5-84ab-0a7845ee52e6",
  "created_time": "2021-03-16T16:31:00.000Z",
  "last_edited_time": "2021-03-16T16:32:00.000Z",
  "has_children": false,
  "type": "to_do",
  "archived": true
  "to_do": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "Lacinato kale",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "Lacinato kale",
        "href": null
      }
    ],
    "checked": false
  }
}
```

## September 9, 2021

### Relation and rollup properties can now be created in databases

When [creating](https://developers.notion.com/reference/create-a-database) or [updating](https://developers.notion.com/reference/update-a-database) databases, you can now add `relation` and `rollup` property types. Note that the related database must also be shared with the integration.

#### Example Request

```bash
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer $NOTION_API_KEY' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-08-16' \
--data '{ 
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Meals": {
          "relation": {
            "database_id": "668d797c-76fa-4934-9b05-ad288df2d136",
          }
        },
        "Number of meals": {
          "rollup": {
            "rollup_property_name": "Name",
            "relation_property_name": "Meals",
            "function": "count"
          }
        }
    }
}'
```

#### Example Response

```json
{
    "object": "database",
    "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
    "created_time": "2021-07-08T23:50:00.000Z",
    "last_edited_time": "2021-07-08T23:50:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
       "Name": {
            "id": "title",
            "type": "title",
            "title": {}
        },
        "Description": {
            "id": "V}lX",
            "type": "rich_text",
            "rich_text": {}
        },
        "In stock": {
            "id": "V>GQ",
            "type": "checkbox",
            "checkbox": {}
        },
        "Meals": {
          "type": "relation",
          "relation": {
            "database_id": "668d797c-76fa-4934-9b05-ad288df2d136",
            "synced_property_name": "Related to Grocery List (Meals)"
          }
        },
        "Number of meals": {
          "id": "Z\\Eh",
          "type": "rollup",
          "rollup": {
            "rollup_property_name": "Name",
            "relation_property_name": "Meals",
            "rollup_property_id": "title",
            "relation_property_id": "mxp^",
            "function": "count"
          }
        },
        
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

## August 24, 2021

### Page icons, cover images, new block types, and improved page file properties

We have added support for linking to external image and file URLs, and many new block types, including image, embed, and file blocks.

You can now use the Notion API to:

- Retrieve and update [page](https://developers.notion.com/reference/page) and [database](https://developers.notion.com/reference/database) icons and cover images.
- [List](https://developers.notion.com/reference/get-block-children) and [append](https://developers.notion.com/reference/patch-block-children) embed, image, video, file, PDF, and bookmark blocks.
- Retrieve URL for [file page properties](https://developers.notion.com/reference/page#files-property-values).
- Update [file page properties](https://developers.notion.com/reference/page#files-property-values).

We do not yet support uploading files to Notion through the API, however, any files already uploaded to Notion can be retrieved. You can reference the details of what is supported [here](https://developers.notion.com/reference/#externally-hosted-files-vs-files-hosted-by-notion).

#### Page Icons and Cover Images

When fetching a [Page object](https://developers.notion.com/reference/page) or a [Database object](https://developers.notion.com/reference/database), the response will now include an `icon` and `cover` property, as shown below:

```json
{
    "object": "database",
    "id": "96433ad8-3fbe-460f-a007-72311c4aa804",
    "cover": {
        "type": "external",
        "external": {
            "url": "https://website.domain/images/image.png"
        }
    },
    // ... remaining properties
}
```

The [Create a page](https://developers.notion.com/reference/post-page), [Update page](https://developers.notion.com/reference/patch-page), [Create a database](https://developers.notion.com/reference/create-a-database), and [Update database](https://developers.notion.com/reference/update-a-database) API endpoints now support the ability to set the page icon and cover image.

#### New Block Types

You can now retrieve and add embed, image, video, file, pdf, and bookmark blocks when using [Append block children](https://developers.notion.com/reference/patch-block-children) and [Retrieve block children](https://developers.notion.com/reference/get-block-children).

Below is an example response from [Retrieve a page](https://developers.notion.com/reference/retrieve-a-page) containing an image uploaded to Notion:

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "4896a9bf-ada2-4bec-8ea2-97bccf07c4ef",
            "created_time": "2021-08-20T21:12:00.000Z",
            "last_edited_time": "2021-08-20T21:12:00.000Z",
            "has_children": false,
            "type": "image",
            "image": {
                "caption": [],
                "type": "file",
                "file": {
                    "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/64f658a7-eb31-4f98-8bea-0aa2956ec475/brocolli.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAEXAMPLE_REDACTED%2F20210820%2Fus-west-2%2Fs3%2Faws4_request&amp;X-Amz-Date=20210820T211229Z&amp;X-Amz-Expires=3600&amp;X-Amz-Signature=e2adc496254ccc741d7ab4f3bab0de7a51b60e31a49d11fcf8702ead2ec9ec18&amp;X-Amz-SignedHeaders=host",
                    "expiry_time": "2021-08-20T22:12:29.066Z"
                }
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

> **📘** Third-party App Embeds
> 
> Third-party web applications, e.g. Typeform, Figma, etc., are retrieved and added as embed blocks.

#### File Page Properties

When retrieving file page properties, you'll now get a link to the file as well as the name.

```json
```

<button aria-selected="true" class="CodeTabs_active" role="tab" type="button">JSON</button></div><div class="CodeTabs-inner" role="tabpanel"><pre><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang-json theme-light" data-lang="json" name="" tabindex="0">{ 
    "object": "page",
    "properties": {
        "Files": {
            "id": "YP~`",
            "type": "files",
            "files": [
                {
                    "name": "Brocolli",
                    "type": "file",
                    "file": {
                        "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c32db351-d1ea-40c2-9660-820db28c44ad/brocolli.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIAEXAMPLE_REDACTED%2F20210820%2Fus-west-2%2Fs3%2Faws4_request&amp;X-Amz-Date=20210820T211042Z&amp;X-Amz-Expires=3600&amp;X-Amz-Signature=859a24c9b7153860b252fa5955829a97632650dcdc5e91c7a831a48c5efecae4&amp;X-Amz-SignedHeaders=host",
                        "expiry_time": "2021-08-20T22:10:42.022Z"
                    }
                },
                {
                    "name": "Text File",
                    "type": "external",
                    "external": {
                        "url": "https://website.domain/files/doc.txt"
                    }
                }
            ]
        },
    },
    // ... remaining properties
}
</code></pre></div></div>
<p>We also support updating file page properties via <a href="/reference/patch-page" target="" title="">Update page</a>.</p>
<h2 class="heading heading-2 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="august-20-2021"></div><div class="heading-text"><div id="section-august-20-2021" class="heading-anchor_backwardsCompatibility"></div>August 20, 2021</div><a aria-label="Skip link to August 20, 2021" class="heading-anchor-icon fa fa-anchor" href="#august-20-2021"></a></h2>
<h3 class="heading heading-3 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="releasing-notion-version-2021-08-16"></div><div class="heading-text"><div id="section-releasing-notion-version-2021-08-16" class="heading-anchor_backwardsCompatibility"></div>Releasing Notion-Version 2021-08-16</div><a aria-label="Skip link to Releasing Notion-Version 2021-08-16" class="heading-anchor-icon fa fa-anchor" href="#releasing-notion-version-2021-08-16"></a></h3>
<p>We're releasing Notion-Version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">2021-08-16</code> with the following <em>backwards incompatible</em> changes:</p>
<ul>
<li><a href="#unknown-keys-will-fail-validation" target="" title="">Unknown Keys Will Fail Validation</a></li>
<li><a href="#changes-to-array-rollup-property-types" target="" title="">Rollup Property Types</a></li>
<li><a href="#append-block-children-returns-a-list-of-blocks" target="" title="">Append Block Children</a></li>
<li><a href="#property-ids-are-now-url-safe" target="" title="">URL Safe Property IDs</a></li>
<li><a href="#empty-database-properties-are-now-returned-as-null" target="" title="">Empty Properties Are Now Returned</a></li>
</ul>
<h4 class="heading heading-4 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="unknown-keys-will-fail-validation"></div><div class="heading-text"><div id="section-unknown-keys-will-fail-validation" class="heading-anchor_backwardsCompatibility"></div>Unknown Keys Will Fail Validation</div><a aria-label="Skip link to Unknown Keys Will Fail Validation" class="heading-anchor-icon fa fa-anchor" href="#unknown-keys-will-fail-validation"></a></h4>
<p>Previously, our endpoints used to only validate against the expected keys in both request body parameters as well as query parameters resulting in some ambiguity between incorrect behavior and invalid inputs. Going forward, to improve the developer experience we will be raising validation errors if keys that are not supported by our API are passed in to requests.</p>
<blockquote class="callout callout_info" theme="📘">
<h2 class="callout-heading"><span class="callout-icon">📘</span>Migration Tip</h2>
<p>To safely migrate to <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">2021-08-16</code>, we recommend thoroughly testing your API calls against the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">2021-08-16</code> version, to see if you get any validation errors due to this change. If you do, remove any parameters that are rejected due to unknown keys.</p>
</blockquote>
<h4 class="heading heading-4 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="changes-to-array-rollup-property-types"></div><div class="heading-text"><div id="section-changes-to-array-rollup-property-types" class="heading-anchor_backwardsCompatibility"></div>Changes to Array Rollup Property Types</div><a aria-label="Skip link to Changes to Array Rollup Property Types" class="heading-anchor-icon fa fa-anchor" href="#changes-to-array-rollup-property-types"></a></h4>
<p>Starting with the Notion-Version header <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">2021-08-16</code>, we are introducing a change to the response for rollup properties on a page which are arrays. Number and date rollups are unaffected. Specifically, the <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">type</code> of elements within an array rollup has been made consistent with property types across other API endpoints:</p>

<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>type: "file"</code></td>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>type: "files"</code></td>
</tr>
<tr>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>type: "text"</code></td>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>type: "rich_text"</code></td>
</tr>
<tr>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>type: "person"</code></td>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>type: "people"</code></td>
</tr>
</tbody>
</table>

An example rollup property value for an array of rich text values, using Notion-Version <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">2021-08-16</code>:</p>
<div class="CodeTabs CodeTabs_initial theme-light">
<div class="CodeTabs-toolbar" role="tablist">
<button aria-selected="true" class="CodeTabs_active" role="tab" type="button">JSON</button>
</div>
<div class="CodeTabs-inner" role="tabpanel">
<pre><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang-json theme-light" data-lang="json" name="" tabindex="0">{ 
  "properties": {
    "sample text array rollup": {
      "id": "NXTh",
      "type": "rollup",
      "rollup": {
        "type": "array",
        "array": [
          {
            "type": "rich_text",
            "rich_text": [
              {
                "type": "text",
                "text": {
                  "content": "hello world!",
                  "link": null
                },
                "annotations": {
                  "bold": false,
                  "italic": false,
                  "strikethrough": false,
                  "underline": false,
                  "code": false,
                  "color": "default"
                },
                "plain_text": "hello world!",
                "href": null
              }
            ]
          },
          {
            "type": "rich_text",
            "rich_text": [
              {
                "type": "text",
                "text": {
                  "content": "foo bar",
                  "link": null
                },
                "annotations": {
                  "bold": false,
                  "italic": false,
                  "strikethrough": false,
                  "underline": false,
                  "code": false,
                  "color": "default"
                },
                "plain_text": "foo bar",
                "href": null
              }
            ]
          }
        ]
      }
    }, 
  }
}
</code></pre>
</div>
</div>
<h4 class="heading heading-4 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="append-block-children-returns-a-list-of-blocks"></div><div class="heading-text"><div id="section-append-block-children-returns-a-list-of-blocks" class="heading-anchor_backwardsCompatibility"></div>Append Block Children returns a list of blocks</div><a aria-label="Skip link to Append Block Children returns a list of blocks" class="heading-anchor-icon fa fa-anchor" href="#append-block-children-returns-a-list-of-blocks"></a></h4>
<p>The <a href="/reference/patch-block-children" target="" title="">Append Block Children</a> endpoint will now return a list of the newly created <a href="/reference/block" target="" title="">Block object</a> children.</p>
<p>Previously the endpoint returned the block object of the parent block. Developers can instead use the <a href="/reference/retrieve-a-block" target="" title="">Retrieve a block</a> endpoint to get the full block object for a specified <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">block_id</code>.</p>
<p>This change allows developers to get <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang- theme-light" data-lang="">block_id</code>'s and additional information of the new blocks right after they're created. Note: only the first level block children are returned. To get sub-children, use the <a href="/reference/get-block-children" target="" title="">Retrieve block children</a> endpoint.</p>
<div class="CodeTabs CodeTabs_initial theme-light">
<div class="CodeTabs-toolbar" role="tablist">
<button aria-selected="true" class="CodeTabs_active" role="tab" type="button">Example response</button>
</div>
<div class="CodeTabs-inner" role="tabpanel">
<pre><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang-json theme-light" data-lang="json" name="Example response" tabindex="0">{ 
    "object": "list",
    "results": [
       {
            "object": "block",
            "id": "9bc30ad4-9373-46a5-84ab-0a7845ee52e6",
            "created_time": "2021-03-16T16:31:00.000Z",
            "last_edited_time": "2021-03-16T16:32:00.000Z",
            "has_children": false,
            "type": "heading_2",
            "heading_2": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Lacinato kale",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "7face6fd-3ef4-4b38-b1dc-c5044988eec0",
            "created_time": "2021-03-16T16:34:00.000Z",
            "last_edited_time": "2021-03-16T16:36:00.000Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale",
                            "link": {
                                "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Lacinato kale",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": " is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": " is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                        "href": null
                    }
                ]
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
</code></pre>
</div>
</div>
<h4 class="heading heading-4 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="property-ids-are-now-url-safe"></div><div class="heading-text"><div id="section-property-i-ds-are-now-url-safe" class="heading-anchor_backwardsCompatibility"></div>Property IDs are now URL Safe</div><a aria-label="Skip link to Property IDs are now URL Safe" class="heading-anchor-icon fa fa-anchor" href="#property-ids-are-now-url-safe"></a></h4>
<p>Endpoints that return property IDs as part of the response body will now return new URL safe encoded property IDs. Any request that uses property IDs (such as <a href="https://developers.notion.com/reference/update-a-database" target="" title="">Update a database</a> or <a href="https://developers.notion.com/reference/patch-page" target="" title="">Update a page</a>) should use the new URL safe ID.</p>
<p>This ensures all property IDs can be referenced in the URL of any new endpoints moving forward.</p>

<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>DoS</code></td>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>DoS%</code></td>
</tr>
<tr>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>title</code></td>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>title</code></td>
</tr>
<tr>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>vEKn</code></td>
<td><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>vEKn</code></td>
</tr>
</tbody>
</table>
<h4 class="heading heading-4 header-scroll" align=""><div class="heading-anchor anchor waypoint" id="empty-database-properties-are-now-returned-as-null"></div><div class="heading-text"><div id="section-empty-database-properties-are-now-returned-as-null" class="heading-anchor_backwardsCompatibility"></div>Empty database properties are now returned as <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>null</code></div><a aria-label="Skip link to Empty database properties are now returned as " class="heading-anchor-icon fa fa-anchor" href="#empty-database-properties-are-now-returned-as-null"></a></h4>
<p>Previously, empty properties of date, email, number, and rollup types were omitted from the page response. Now, these empty properties are returned with <button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code>null</code> values.</p>
<div class="CodeTabs CodeTabs_initial theme-light">
<div class="CodeTabs-toolbar" role="tablist">
<button aria-selected="true" class="CodeTabs_active" role="tab" type="button">Example page response with empty properties</button>
</div>
<div class="CodeTabs-inner" role="tabpanel">
<pre><button aria-label="Copy Code" class="rdmd-code-copy fa"></button><code class="rdmd-code lang-json theme-light" data-lang="json" name="Example page response with empty properties" tabindex="0">{ 
    "object": "page",
    "id": "a8b7e96d-22ce-44d8-991f-6c4535af6608",
```

## August 20, 2021

### Formula properties can now be created in databases

When [creating](https://developers.notion.com/reference/create-a-database) or [updating](https://developers.notion.com/reference/update-a-database) databases, you can now add `formula` property types.

#### Example request

```curl
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer $NOTION_API_KEY' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-05-13' \
--data '{
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Cost of next trip": {
            "formula": {
                "expression": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
            }
        }
    }
}'
```

#### Example response

```json
{
    "object": "database",
    "id": "c23f0085-a061-41c0-b8a6-cbe14d15a4de",
    "created_time": "2021-08-20T16:08:00.000Z",
    "last_edited_time": "2021-08-20T16:08:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
        "Cost of next trip": {
            "id": "Rbq\\",
            "name": "Cost of next trip",
            "type": "formula",
            "formula": {
                "expression": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
            }
        },
        "In stock": {
            "id": "\\JwC",
            "name": "In stock",
            "type": "checkbox",
            "checkbox": {}
        },
        "Description": {
            "id": "`}HT",
            "name": "Description",
            "type": "rich_text",
            "rich_text": {}
        },
        "Price": {
            "id": "u|<{",
            "name": "Price",
            "type": "number",
            "number": {
                "format": "dollar"
            }
        },
        "Name": {
            "id": "title",
            "name": "Name",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

## August 11, 2021

### OAuth token response now includes workspace ID and owner info

We now return a `workspace_id` field and an `owner` in the [token response](https://developers.notion.com/docs/authorization#exchanging-the-grant-for-an-access-token) at the very end of the OAuth authorization flow.

`workspace_id` is the ID of the workspace where the integration was authorized. As a reminder, this is **not** intended to be unique across tokens; in future iterations of our authorization flow users may be able to authorize your integration multiple times in the same workspace.

`owner` contains information about who can view and share the integration. Because all integrations today can be viewed and shared by all members in the space, `owner` is just an object that looks like `{ "workspace": true }` for now.

To summarize, the OAuth token response now looks like this:

| Field | Type | Description | Not null |
| --- | --- | --- | --- |
| `access_token` | string | An access token used to authorize requests to the Notion API. | ✅ |
| `workspace_id` | string | The ID of the workspace where this authorization took place. | ✅ |
| `workspace_name` | string | A human-readable name which can be used to display this authorization in UI. |  |
| `workspace_icon` | string | A URL to an image which can be used to display this authorization in UI. |  |
| `bot_id` | string | An identifier for this authorization. | ✅ |
| `owner` | object | An object containing information about who can view and share this integration. Always `{ "workspace": true }` for now. | ✅ |

## August 11, 2021

### Update existing databases with PATCH /v1/databases

You can now use the Notion API to [update databases](https://developers.notion.com/reference/update-a-database)! 

Supported updates are:

- renaming the database
- adding and removing properties
- renaming properties
- updating property types.

Note that updating the `name` and `color` select and multi select options is not supported.

#### Example request

```curl
curl --location --request PATCH 'https://api.notion.com/v1/databases/668d797c-76fa-4934-9b05-ad288df2d136' \
--header 'Authorization: Bearer $NOTION_API_KEY' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-07-27' \
--data '{
    "title": [
        {
            "text": {
                "content": "Today's grocery list"
            }
        }
    ],
    "properties": {
        "+1": null,
        "Photo": {},
        "Store availability": {
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market"
                    },
                    {
                        "name": "Rainbow Grocery"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "orange"
                    }
                ]
            }
        }
    }
}'
```

#### Example response

```json
{
  "object": "database",
  "id": "668d797c-76fa-4934-9b05-ad288df2d136",
  "created_time": "2020-03-17T19:10:00.000Z",
  "last_edited_time": "2021-08-11T17:26:00.000Z",
  "parent": {
    "type": "page_id",
    "page_id": "48f8fee9-cd79-4180-bc2f-ec0398253067"
  },
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Today's grocery list",
        "link": null
      },
      "annotations": {
        "bold": false,
        
      },
      "plain_text": "Grocery List",
      "href": null
    }
  ],
  "properties": {
    "Cost of next trip": {
      "id": "Rbq\\",
      "name": "Cost of next trip",
      "type": "formula",
      "formula": {
        "expression": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
      }
    },
    "In stock": {
      "id": "\\JwC",
      "name": "In stock",
      "type": "checkbox",
      "checkbox": {}
    },
    "Description": {
      "id": "`}HT",
      "name": "Description",
      "type": "rich_text",
      "rich_text": {}
    },
    "Price": {
      "id": "u|<{",
      "name": "Price",
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Name": {
      "id": "title",
      "name": "Name",
      "type": "title",
      "title": {}
    }
  },
  "parent": {
    "type": "page_id",
    "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
  }
}
```
```

## August 3, 2021

### Retrieve and update blocks with GET and PATCH /v1/blocks/:id

You can now retrieve and update block objects with the Notion API! The `PATCH` endpoint currently supports updating `paragraph`, `heading_1`, `heading_2`, `heading_3`, `bulleted_list_item`, `numbered_list_item`, `toggle` and `to_do` blocks.

#### Retrieve a Block

The [Retrieve a Block](/reference/retrieve-a-block) endpoint returns a [Block Object](/reference/block).

**Example GET request**

```bash
curl 'https://api.notion.com/v1/blocks/9bc30ad4-9373-46a5-84ab-0a7845ee52e6' \
  -H 'Authorization: Bearer $NOTION_API_KEY' \
  -H 'Notion-Version: 2021-05-13'
```

**Example response**

```json
{
  "object": "block",
  "id": "9bc30ad4-9373-46a5-84ab-0a7845ee52e6",
  "created_time": "2021-03-16T16:31:00.000Z",
  "last_edited_time": "2021-03-16T16:32:00.000Z",
  "has_children": false,
  "type": "to_do",
  "to_do": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "Lacinato kale",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "Lacinato kale",
        "href": null
      }
    ],
    "checked": false
  }
}
```

#### Update a Block

The new `PATCH` `/v1/blocks/:id` endpoint supports updating block content (the properties within the block type object) and returns the updated [Block Object](/reference/block), same as the `GET` endpoint shown above. See the [Update a Block](/reference/update-a-block) documentation for more detail.

**Example PATCH request**

```bash
curl https://api.notion.com/v1/blocks/9bc30ad4-9373-46a5-84ab-0a7845ee52e6 \
  -H 'Authorization: Bearer $NOTION_API_KEY' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2021-05-13' \
  -X PATCH \
  --data '{ 
  "to_do": {
    "text": [{ 
      "text": { "content": "Lacinato kale" } 
      }],
    "checked": false
  }
}'
```

## July 26, 2021

### Number properties now support more currency formats

The number property type in databases now supports additional currency options.

The new options are:

- "hong_kong_dollar"
- "new_zealand_dollar"
- "krona"
- "norwegian_krone"
- "mexican_peso"
- "rand"
- "new_taiwan_dollar"
- "danish_krone"
- "zloty"
- "baht"
- "forint"
- "koruna"
- "shekel"
- "chilean_peso"
- "philippine_peso"
- "dirham"
- "colombian_peso"
- "riyal"
- "ringgit"
- "leu"

This impacts the [number configuration of databases](https://developers.notion.com/reference/database#number-configuration).

## July 22, 2021

### OAuth improvements

We've made improvements to the OAuth flow to make it easier to use.

**We now show the page picker on reauthorization.** Just like before, the user who initially authorized an integration can reauthorize by going through OAuth a second time. The page picker step will remember which pages have already been shared with the integration, if any, and let users share or un-share additional pages.

**Users can search for pages to share with an integration.** Previously, users could only select pages at the top level of the Workspace, Shared section, or Private pages section to share with an integration, but we've added a search bar so users can search for and select any page in their workspace.

We also updated the page picker to only show pages for which the user has Full Access permission. Previously, the page picker showed any pages for which the user had at least Can View permission, but would show an error when they tried to give the permission access to those pages.

![Image 1: 1164](https://files.readme.io/15c452e-oauth_improvements.png)

The search bar now lets you search for and select nested pages to share with an integration.

![Image 2: 1134](https://files.readme.io/63ac8e6-oauth2.png)

Once selected, any nested pages appear in the "Manually Added" section.

## July 21, 2021

### Database property objects now include the property name

[Database property objects](https://developers.notion.com/reference/database#database-property) now include the field `name` with the property name as it appears in Notion.

## July 15, 2021

### Rollup property functions now include show_original

The `function` `show_original` has now been added to [rollup database property objects](https://developers.notion.com/reference/database#rollup-configuration). This fixes a bug where rollup properties were omitted if the calculation was "Show Original".

## July 13, 2021

### Create new databases with POST /v1/databases

You can now use the Notion API to [create a database](https://developers.notion.com/reference/create-a-database) as a subpage of an existing page. Currently supported property types are:

- `text`
- `link`
- `checkbox`
- `number`
- `date`
- `folder`
- `emoji`
- `video`
- `audio`
- `file`
- `form`
- `poll`
- `page_link`
- `page`
- `custom`
- `searchable`
- `hidden`
- `locked`
- `public`
- `private`
- `team_member`
- `project`
- `project_folder`
- `project_memberships`
- `project_tasks`
- `project_task_comments`
- `project_tags`
- `project_tag_groups`
- `project_taggings`
- `project_taggings_history`
- `project_taggings_history_comments`
- `project_taggings_history_tags`
- `project_taggings_history_tags_history`
- `project_taggings_history_tags_history_comments`
- `project_taggings_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_comments`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags`
- `project_taggings_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tags_history_tagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTagsHistoryTags

# Example Request

## cURL

```curl
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer $NOTION_API_KEY' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-05-13' \
--data '{
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {},
        "Description": {},
        "In stock": {},
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {},
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {},
        "Photo": {}
    }
}'
```

## Example Response

### JSON

```json
{
    "object": "database",
    "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
    "created_time": "2021-07-08T23:50:00.000Z",
    "last_edited_time": "2021-07-08T23:50:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
        "+1": {
            "id": "PNEQ",
            "type": "people",
            "people": {}
        },
        "In stock": {
            "id": "V>GQ",
            "type": "checkbox",
            "checkbox": {}
        },
        "Price": {
            "id": "V@]u",
            "type": "number",
            "number": {
                "format": "dollar"
            }
        },
        "Description": {
            "id": "V}lX",
            "type": "rich_text",
            "rich_text": {}
        },
        "Last ordered": {
            "id": "eVnV",
            "type": "date",
            "date": {}
        },
        "Store availability": {
            "id": "s}Kq",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "id": "cb79b393-d1c1-4528-b517-c450859de766",
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "id": "58aae162-75d4-403b-a793-3bc7308e4cd2",
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "id": "22d0f199-babc-44ff-bd80-a9eae3e3fcbf",
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "id": "0d069987-ffb0-4347-bde2-8e4068003dbc",
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Photo": {
            "id": "yfiK",
            "type": "files",
            "files": {}
        },
        "Food group": {
            "id": "|JKd",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "6d4523fa-88cb-4ffd-9364-1e39d0f4e566",
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "id": "268d7e75-de8f-4c4b-8b9d-de0f97021833",
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "id": "1b234a00-dc97-489c-b987-829264cfdfef",
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

## July 7, 2021

### User mentions can only be of people

To be consistent with the Notion application, only users of type "people" can be mentioned in rich text objects or in people properties of databases. Trying to include users of type "bot" will return a validation error. Existing mentions of bot users is unaffected.

## July 1, 2021

### Page objects now contain url

[Page objects](/reference/page#all-pages) now return the web address of the page in the `url` key.

#### JSON

```json
{
  "object": "page",
  "id": "251d2b5f-268c-4de2-afe9-c71ff92ca95c",
  "created_time": "2020-03-17T19:10:04.968Z",
  "last_edited_time": "2020-03-17T21:49:37.913Z",
  "parent": {
    "type": "database_id",
    "database_id": "48f8fee9-cd79-4180-bc2f-ec0398253067"
  },
  "archived": false,
  "url": "https://www.notion.so/Avocado-251d2b5f268c4de2afe9c71ff92ca95c",
  "properties": {
    "Name": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "Avocado",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "Avocado",
          "href": null
        }
      ]
    }
  }
}
```

This impacts endpoints that return page object: the [pages](/reference/page) endpoints and [query database](/reference/post-database-query) endpoint.

## June 28, 2021

### Last edited and created time properties are now rounded to the nearest minute

Starting July 1st, the `last_edited_time` and `created_time` properties will be rounded down to the closest minute for `page`, `database`, and `block` objects. Previously, this behavior was inconsistent with some times being rounded and others not.

## June 23, 2021

### Database objects now return parent

Database objects now return a [parent property](/reference/database#page-parent). Databases can have pages or workspaces as parents.

#### JSON

```json
{
  "parent": {
    "type": "page_id",
    "page_id": "b8595b75-abd1-4cad-8dfe-f935a8ef57cb"
  }
}
```

### Other Improvements and Fixes

- Inline database mentions are now included in `last_edited_time` and `created_time` properties.

## Backwards Compatibility

### Example Request

```curl
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer $NOTION_API_KEY' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-05-13' \
--data '{
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {},
        "Description": {},
        "In stock": {},
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {},
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {},
        "Photo": {}
    }
}'
```

### Example Response

#### JSON

```json
{
    "object": "database",
    "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
    "created_time": "2021-07-08T23:50:00.000Z",
    "last_edited_time": "2021-07-08T23:50:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
        "+1": {
            "id": "PNEQ",
            "type": "people",
            "people": {}
        },
        "In stock": {
            "id": "V>GQ",
            "type": "checkbox",
            "checkbox": {}
        },
        "Price": {
            "id": "V@]u",
            "type": "number",
            "number": {
                "format": "dollar"
            }
        },
        "Description": {
            "id": "V}lX",
            "type": "rich_text",
            "rich_text": {}
        },
        "Last ordered": {
            "id": "eVnV",
            "type": "date",
            "date": {}
        },
        "Store availability": {
            "id": "s}Kq",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Photo": {
            "id": "yfiK",
            "type": "files",
            "files": {}
        },
        "Food group": {
            "id": "|JKd",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "6d4523fa-88cb-4ffd-9364-1e39d0f4e566",
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "id": "268d7e75-de8f-4c4b-8b9d-de0f97021833",
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "id": "1b234a00-dc97-489c-b987-829264cfdfef",
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

## June 15, 2021

### Select values can now be dynamically created via Create and Update Page endpoints + other updates since public beta launch

You can now dynamically create new options for [Select](https://developers.notion.so/reference/database#select-configuration) or [Multi-Select properties](https://developers.notion.so/reference/database#multi-select-configuration) when using the [Create Page](https://developers.notion.so/reference/post-page) and [Update Page](https://developers.notion.so/reference/patch-page) endpoints. When specifying an option that does not exist in the database schema already, the option will now be created and the database schema updated accordingly.

#### JSON Example

```json
{
  "properties": {
    "Food group": {
      "multi_select": [{"name": "Vegetable"},{"name": "Fruit"}]
    }
  }
}
```

In the above [property values](https://developers.notion.so/reference/page-property-value) example: Previously, if either "Vegetable" or "Fruit" did not already exist as an option in the database schema, an error would be returned that these are not valid Select options. Now, these options will be created dynamically.

**Bug Fixes**

- The title property of a page can be set, and a page can be archived or un-archived, even when the page does not belong to a database.
- [Retrieving pages](https://developers.notion.so/reference/get-page) that are shared with an integration, but where the page's parent is not shared, no longer erroneously returns a 404.

**Other Changes**

- [Search endpoint](https://developers.notion.so/reference/post-search) now returns untitled pages.
- Applies to [version 2021-05-13](https://developers.notion.so/reference/versioning#changes-by-version) and later only: The [Query Database](https://developers.notion.so/reference/post-database-query) endpoint no longer accepts query parameters – these should be sent as body parameters.

## May 19, 2021

### Notion-Version header will be required starting June 1, 2021

The Notion API has recommended using an explicit version to every HTTP request, using the `Notion-Version` header.

**For integrations created after June 1, 2021 an explicit version on every request will become required**. After July 1, 2021, integrations created before June 1, 2021 will also have the same requirement. Today, the most recent version is `"2021-05-13"`.

#### Is my integration affected? What should I do to update?

This requirement will not break your existing integration; however, we will start enforcing this requirement for all API requests on July 1st. Starting July 1st, if you don't send the Notion-Version header with your Notion API calls, you will get a `"missing_version"` error. Learn more about how the Notion API [handles versioning](https://developers.notion.so/reference/versioning).

If you've been using examples copied from documentation or example code since the public beta, including using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js), your existing code should continue to work as expected.

Otherwise, please make one of the two following changes before July 1:

1. Add `Notion-Version: 2021-05-11` in the header when making requests (no other code change is needed).
2. **Recommended**: Add `Notion-Version: 2021-05-13` in the header when making requests. Making this change will move you to our newest version which includes the following breaking change.

#### Breaking changes in version 2021-05-13

The `type` of [property value objects](https://developers.notion.so/reference/page-property-value) for rich text properties has changed from `"text"` to `"rich_text"`.

When [creating pages](https://developers.notion.so/reference/post-page) and [updating page properties](https://developers.notion.so/reference/patch-page), update page property values that are rich text to use the key `rich_text` instead of `text`. Similarly when [retrieving a page](https://developers.notion.so/reference/get-page), rich text properties will be returned with the `type` `"rich_text"` instead of `"text"`.

This change helps distinguish between the property type, and the inner text values of [rich text object](https://developers.notion.so/reference/rich-text), which have the key `text`.

To illustrate this change, here is an example of how the [page object](https://developers.notion.so/reference/page)'s `properties` appear before and after:

##### JavaScript Example 1

```javascript
// Before (in unversioned requests and responses)
{
  "object": "page",
  "properties": {
    "Description": {
      "type": "text",
      "text": [
        {
          "type": "text",
          "text": { "content": "Hello World" }
        }
      ]
    }
  }
  /* remaining details omitted */
}
```

##### JavaScript Example 2

```javascript
// After (in requests and responses with version 2021-05-13)
{
  "object": "page",
  "properties": {
    "Description": {
      "type": "rich_text",
      "rich_text": [
        {
          "type": "text",
          "text": { "content": "Hello World" }
        }
      ]
    }
  }
  /* remaining details omitted */
}
```

## May 18, 2021

### Initial users may reauthorize a public integration using OAuth

Public integrations use OAuth to [request authorization from a user](https://developers.notion.com/docs/authorization#prompting-users-to-add-an-integration) before being added to a Notion workspace. Previously, once an integration was added to a workspace, no users were able to reauthorize the same integration in that workspace. This change allows the user who initially added the integration to complete the authorization flow more than once. This improvement helps integrations avoid a potential dead end in user flows.

Integrations do not need to make any updates to take advantage of this new capability. An integration may simply link or redirect a user to the authorization URL, the same as the first authorization. During reauthorization the user will not see the page picker. The access token received at the end of reauthorization will be the same as the initial access token. This capability is available immediately.

Please be aware that other previous limitations still exist. Only users with admin access level in a workspace can add an integration. Integrations can only be added to a workspace by one user.

## May 13, 2021

### Hello world, the Notion API is now in public beta

The Notion API is now available for all developers to explore and build upon. Integrations built on the API are available to all Notion users, on free or paid plans.

In this public beta release, you'll find many of the fundamental parts of Notion: reading and writing to pages, working with users, and the deep and powerful world of Notion databases. The API itself offers foundational features such as authorization, pagination, limits, and more. This is enough to build many interesting integrations we've heard Notion users are excited to use. We're excited to see what you'll build for all of us. [→ Get started](https://developers.notion.com/docs/getting-started)

Our goal is to establish that the Notion API is robust, easy to use, and trustworthy. In public beta, we’ll continue to add new features and making significant changes based on your feedback. Once the most important improvements are included, the API will transition from public beta to general availability. you’ll have everything you need to build integrations teams and businesses can depend on.

A special thanks to the all developers who experimented, explored, and shared their ideas with us - both in the private beta and those following along.

## May 4, 2021

### Public integration type extends access to multiple workspaces using OAuth

The Notion API has added a new integration type: Public OAuth integrations. If you're building a product or service for Notion users outside your own team - public integrations are for developers like you.

In order to create and configure an integration, its type, name, avatar, and other related settings, the [My integrations](https://www.notion.com/my-integrations) page is now available.

Public integrations use OAuth to request permission to access pages and databases in new workspaces. Once the user accepts, the integration can receive a separate access token for resources in the user's workspace.

Existing integrations are now known as internal integrations. We no longer call the bearer token you previously used an API Key. It's now known as an integration token. You can keep your bearer token around - it will continue to work just the same.

Learn how to implement these changes in the [authorization guide](https://developers.notion.com/docs/authorization).

## May 3, 2021

### Search is now available in the API

Using the new [search endpoint](https://developers.notion.com/reference/post-search), you can query all pages and databases users have shared with your integration.

The query you provide filters results by matching against the page title. The results also include matches against subpages of pages users have shared with your integration. This endpoint can be helpful when onboarding a new user and trying to find the page they just shared with your integration.

We recommend transitioning away from using the [list databases endpoint](https://developers.notion.com/reference/get-databases). The search endpoint provides all the same functionality - and more.
```

# August 23 - September 5, 2023

* The [Working with databases guide](/docs/working-with-databases) was revised to improve its readability and to make additional resources easier to find.
* Notion's [Postman collection](https://www.postman.com/notionhq/workspace/notion-s-api-workspace/collection/15568543-d990f9b7-98d3-47d3-9131-4866ab9c6df2) for the API was updated. Be sure to pull recent changes into your forked version.
* A reminder was added to the [Comments endpoints](/reference/create-a-comment) to update [integration capabilities](/reference/capabilities) for comments prior to using the endpoints. (Read/write comment capabilities are off by default and can be turned on in the [integration dashboard](https://www.notion.so/my-integrations).)
* General clean-up and improvements, including code formatting.

# August 8 - August 22, 2023

* The [Build your first integration](/docs/create-a-notion-integration) guide was rewritten with new demo code to help developers learn how to use Notion’s API even faster.
  * A new [sample app](https://github.com/makenotion/notion-sdk-js/tree/main/examples/web-form-with-express) was added to the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js/tree/main) `/examples` directory. This completed sample app is referenced in the new [Build your first integration](/docs/create-a-notion-integration) guide.
* The description for the `block_id` path parameter was updated for the [Append block children](/reference/patch-block-children) endpoint to indicate that a block ID or page ID can be used.
* A clarification was added to [documentation](/reference/retrieve-a-database) for retrieving/updating database properties: If a property is based on a relation to another database, the related database also needs to be shared with the integration.
* A clarification was added to documentation for [querying databases](/reference/post-database-query-filter#multi-select). When filtering a multi-select property, the `contains` field will filter for exact matches for the string provided.
* The [Working with comments](/docs/working-with-comments) guide was updated with additional examples to distinguish between creating page comments and inline discussion comments.
  * The [Create a comment](/reference/create-a-comment) endpoint description now links to the Working with comments guide to help developers find additional resources faster.
* If you haven’t already, join our [Notion Devs Slack group](https://join.slack.com/t/notiondevs/shared_invite/zt-20b5996xv-DzJdLiympy6jP0GGzu3AMg) to learn from other developers building with the public API.

## Notice for an upcoming Public API change

### We will soon be rolling out changes to the Formulas property (Formulas 2.0), and as such, we will be making a change to the Notion Public API.

This is a non-versioned change and is expected to be in effect in the next couple weeks.

**tl;dr:** As part of the Formulas 2.0 rollout, the Public API’s format of the string value for [`formula.expression`](/reference/property-object#formula) will be changing. Public API calls with formula inputs in the old format will still succeed. On write operations, the old format will be supported indefinitely, but on read, only the new format will be returned. This change is being made to improve the formulas experience and ensure parity with the Notion app.

No action is required for creating or updating database formulas. Reading database [`formula.expression`](/reference/property-object#formula) values may require developer changes.

### What do you need to know?

**The string value of `formula.expression` is changing; the schema is not.**

* **On write** via the Public API ([create](/reference/create-a-database) or [update](/reference/update-a-database) database endpoints), Notion will support using the old format as a Public API input in the formula property schema indefinitely _and_ will support writing in the **new** format.
* Database objects returned via the Public API will have the new formulas 2.0 format.

```json
// Old format
"Updated price": {
  "id": "YU%7C%40",
  "name": "Updated price",
  "type": "formula",
  "formula": {
    "expression": "prop(\"Price\") * 2"
  }
}

// New format (upcoming)
"Updated price": {
  "id": "YU%7C%40",
  "name": "Updated price",
  "type": "formula",
  "formula": {
      "expression": "{{notion:block_property:BtVS:00000000-0000-0000-0000-000000000000:8994905a-074a-415f-9bcf-d1f8b4fa38e4}}/2"
  }
}
```

### Why is this happening?

Notion databases allow you to build a fully customizable system for you and your team – they provide a place where you can keep all your information in one place, with the ability to build views, filters, and workflows that can be adapted to your needs.

The formula property helps you take that even further – allowing you to perform calculations, create specialized views, and provide an extra layer of insight based on information in other database properties. It helps expand what you can do in Notion databases.

We are improving the formulas experience so that:

1. It’s easier to write formulas.
2. Formula outputs look and feel more native to Notion.
3. The formula language can fulfill more specific needs.

Changes being made to the API are to ensure parity with the Notion app.

### What do you need to do?

This is a non-versioned change that will not affect most developers. As mentioned, the formula property format will still have the same schema in the Public API; only the value of the `formula.expression` field will change.

Keep an eye on this changelog for when the update becomes available in the Public API.

# July 25 - August 7, 2023

* Notion is excited to announce our [Technology Partnership Program](https://www.notion.so/technology-partner-program). 🎉 This program is open to companies who have built a public integration (including Link Previews) and are interested in improving and scaling their integration with Notion’s support. If you think your integration and company could be a fit, [learn more and apply here](https://www.notion.so/technology-partner-program).
* We’ve updated our API reference docs to include information on Notion’s [wiki databases and verified pages](https://www.notion.so/help/wikis-and-verified-pages). Updates include:
  * An overview on wikis in the guide to [working with databases](/docs/working-with-databases#properties).
  * The [`verification`](/reference/page-property-values#verification) page property was added to the [Page properties](/reference/page-property-values) documentation.
  * The [Create a database](/reference/create-a-database) and [Query a database](/reference/post-database-query) endpoint documentation was updated to reflect API changes related to wikis. Namely, that querying wiki databases can return both [Page](/reference/page) and [Database](/reference/database) objects.
* The [Error codes](/reference/status-codes#error-codes) section in the [Status code](/reference/status-codes) page was updated to include examples of the `"message"` returned with each type of API error, as well as descriptions of the issue each error code represents.
* A number of sample cURL commands in our docs were still using an old [Notion Version](/reference/versioning) in their headers. These have all been updated.
* A clarification was added to the [Authorization guide](/docs/authorization#making-api-requests-with-an-internal-integration) that the [Notion Version](/reference/versioning) is always required in public API request headers.

# July 11 - July 24, 2023

* A new integration [example](https://github.com/makenotion/notion-sdk-js/tree/main/examples/parse-text-from-any-block-type) was added to the Notion SDK for JavaScript repo. This example shows how to get the plain text from any block type currently supported by the public API.
* The new unique ID page property was added to the [Page properties](/reference/page-property-values) documentation. When used, the unique ID (`unique_id`) auto-increments for every new page created in a database. An optional prefix can be included that will be applied to the ID values.
* Workspace Owners can now see _all_ internal integrations created in a workspace via the [integration dashboard](https://www.notion.so/my-integrations). This includes integrations created by themselves and other Workspace Owners. We’ve included this information in our [Getting Started](/docs/getting-started#internal-integrations) guide.
* A [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js) code sample was added to the [Create a database](/reference/create-a-database) endpoint documentation.

# June 13 - July 10, 2023

* We updated our [Getting started guide](/docs) to help developers who are new to the public API better understand how the API relates to integrations.
* The [Block object](/reference/block#embed) docs were updated with a tip on how to embed Vimeo links in a Notion page via the API.
* A new `after` parameter has been added to the [Append block children](/reference/patch-block-children) endpoint. Developers can now specify where to append a new block, instead of appending it to the end of a parent block by default.

```bash
curl -X PATCH https://api.notion.com/v1/blocks/16d8004e-5f6a-42a6-9811-51c22ddada12/children \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  --data '{
    "children": [
    ...
    ]
  }, after: "<block_id_to_append_after>"
}'
```

* The [Authorization guide](/docs/authorization) had a clarification added to help developers find the resources they need for [Link Preview](/docs/link-previews) integrations.
* The new `public_url` property was added to the docs. When a page or database has been shared publicly, the response body will include a `public_url` value.

```json
{
  "object": "page",
  "id": "<id>",
  "created_time": "2023-06-02T19:54:00.000Z",
  "last_edited_time": "2023-06-02T23:04:00.000Z",
  "created_by": { ... },
  "last_edited_by": { ... },
  "cover": null,
  "icon": null,
  "parent": { ... },
  "archived": false,
  "properties": { ... },
  "url": "<url>",
  "public_url": "<public-url>"
}
```

* The [Retrieve block children](/reference/get-block-children) endpoint documentation was updated to help developers who are new to the public API better understand the endpoint’s functionality.
* The [Retrieve a block](/reference/retrieve-a-block) endpoint documentation was updated with some additional information related to working with page content.
* The `invalid_grant` code was added to our [Status codes](/reference/status-codes) documentation. This code is returned when the authorization grant (e.g., token) provided is invalid. For example, a status code `400` with an `invalid_grant` code will be returned when the token provided has expired.
* The [Rich text](/reference/rich-text) documentation was updated with additional information on what rich text is and how the Notion uses it.

# May 30 - June 12, 2023

* Our guides and docs related to Link Preview integrations have been updated to help developers find the information they need faster.
  Improvements have been made to the following guides and API reference docs:
  * [Getting started guide](/docs/getting-started)
  * [Introduction to Link Previews guide](/docs/link-previews)
  * [Building a Link Preview integration guide](/docs/build-a-link-preview-integration)
  * [Unfurl attribute object docs](/reference/unfurl-attribute-object)
* We added more information about the `plain_text` property found in the `rich_text` object. Learn more about rich text in our [Rich text object](/reference/rich-text) docs.
* The docs related to [filtering](/reference/post-database-query-filter) and [sorting](/reference/post-database-query-sort) database queries now have more code examples for developers building integrations with the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js).
* We reorganized the REST API reference navigation bar after removing the “Other” section to make its child pages easier to find.

# May 16 - May 29, 2023

* The guides and docs related to Link Preview integrations have been updated to help developers find the information they need faster.
  Improvements have been made to the following guides and API reference docs:
  * [Getting started guide](/docs/getting-started)
  * [Introduction to Link Previews guide](/docs/link-previews)
  * [Building a Link Preview integration guide](/docs/build-a-link-preview-integration)
  * [Unfurl attribute object docs](/reference/unfurl-attribute-object)
* We added more information about the `plain_text` property found in the `rich_text` object. Learn more about rich text in our [Rich text object](/reference/rich-text) docs.
* The docs related to [filtering](/reference/post-database-query-filter) and [sorting](/reference/post-database-query-sort) database queries now have more code examples for developers building integrations with the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js).
* We reorganized the REST API reference navigation bar after removing the “Other” section to make its child pages easier to find.
```

# Database Schema Size Recommendation

*   The [Query a database](/reference/post-database-query) and [Filter database entries](/reference/post-database-query-filter) docs were updated with additional code examples of passing single and multiple filters.
*   The [Working with comments](/docs/working-with-comments) guide was updated to clarify how to retrieve and add comments using the REST API.
*   The references docs for `rollup` [page properties](/reference/page-property-values#rollup), as well as the [Retrieve a page property](/reference/retrieve-a-page-property) and [Retrieve a page](/reference/retrieve-a-page) endpoints were updated with additional information related to limitations. In cases where a page property — like a rollup — has more than 25 references, the [Retrieve a page property](/reference/retrieve-a-page-property) endpoint must be used to receive a complete response.
*   An outdated Changelog URL now redirects to this Changelog page to help avoid confusion.

## Backwards Compatibility

### May 2 - May 15, 2023

*   We added a database schema size recommendation of **50KB** to our docs to help developers manage their database query performance. It is strongly recommended that developers keep their schema size under this number.
*   The [Update a database](/reference/update-a-database) page was updated to improve readability. Additional information on how this endpoint differs from related endpoints was also added to help developers better navigate the REST API docs.
*   The [Query a database](/reference/post-database-query#errors) page was updated with additional information about the `filter_properties` query parameter.  
    When used with the REST API, this query parameter is passed as a string, like so:
    
    ```http
    https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]&filter_properties=[property_id_2]
    ```
    
    When used with the [JavaScript SDK](https://github.com/makenotion/notion-sdk-js), the `filter_properties` option accepts an array of property ID strings:
    
    ```javascript
    notion.databases.query({
        database_id: 'databaseID',
        filter_properties: ["propertyID1", "propertyID2"]
    })
    ```
    
*   Docs that mention the `redirect_uri` — a value used with [public integrations](/docs/authorization#what-is-a-public-integration) — were updated to clarify when this value is required. Refer to the [Create a token](/reference/create-a-token) page for a complete description.
*   The video block-type was updated on the [Block Object](/reference/block#video) page to clarify accepted video types. YouTube URLs that contain `watch` or `embed` are supported video types.
*   The [Append a block](/reference/patch-block-children) page content was reorganized to improve readability.

## April 18 - May 1, 2023

*   The [Build a Link Preview integration guide](/docs/build-a-link-preview-integration) was updated to reflect a change regarding how link previews are enabled in the [integration dashboard](https://www.notion.so/my-integrations).
*   The [versioning page](/reference/versioning) was updated to clarify that the `Notion-Version` header is required in Notion REST API requests.
*   The [parent object page](/reference/parent-object) and API reference docs for [database POST requests](/reference/create-a-database) and [blocks PATCH requests](/reference/patch-block-children) were updated to better explain how parenting rules work.
*   The [Integration guide](/docs/create-a-notion-integration) was updated with more links to help developers find resources faster.
*   Number database properties now support the Peruvian sol as a currency format. To use it, set `peruvian_sol` as the value for a number’s `format` field when creating or updating a database property or [schema](/reference/property-schema-object#number-configuration).
*   General docs housekeeping, such reducing the number of callouts in our API reference docs to improve the readability.

## March 14 - April 17, 2023

*   Our developer community Slack invite link was updated. [Join here](https://join.slack.com/t/notiondevs/shared_invite/zt-1tjam81wh-BGaZXHUY83DpLNjZwKEiGg) to connect with other developers building with the Notion API.
*   The [Authorization guide](/docs/authorization) was updated to include more information on creating integrations, adding templates to public integrations, and more code examples to get you started, faster.
*   We’ve added more code examples to our API reference docs, including [Archive a page](/reference/archive-a-page) and [Authentication](/reference/authentication).
*   General docs housekeeping, such reducing the number of callouts in our API reference docs to improve the readability.

## February 28 - March 13, 2023

We don’t have any changes to announce this week! Stay tuned, and in the meantime check out our platform roadmap for a look at what we’re building.

## February 14 - 27, 2023

### Fixes and Improvements

*   You can now update [rollup database properties](/reference/property-object#rollup) via the API. To programmatically update a `rollup` property, send a PATCH to [Update a database](/reference/update-a-database) that specifies the change in the `properties` body param.

## January 31 - February 13, 2023

We don’t have any updates to share right now. Stay tuned for the next changelog! To get a sense for what we’re heads down working on, check out the [platform roadmap](/page/notion-platform-roadmap#updated-march-2-2022).

## January 18 - 30, 2023

### Fixes and Improvements

*   Stay tuned!

### New Things

*   Added a token `Refresh` button to the settings page for internal integrations. Click `Refresh` to generate a new token for your internal integration.

![You can now refresh an internal integration token from the integration settings page.](https://files.readme.io/b1d6c0c-2023-01-13_10.58.16.gif)

## January 3 - 17, 2023

### New Things

*   Shipped detailed docs for Link Previews including an [overview](/docs/link-previews), [getting started guide](/docs/build-a-link-preview-integration), and [reference materials](/reference/unfurl-attribute-object).

## December 19, 2022 - January 2, 2023

### Fixes and Improvements

*   The [Retrieve a Page endpoint](/reference/retrieve-a-page#errors) can now return specific page property values when you include the `filter_properties` path param.
*   You can now request specific page property values from a database by passing `filter_properties` in the request body to the [Query a database endpoint](/reference/post-database-query).

### New Things

*   Happy 2023! For a sneak peek of what we’ll be up to this year, check out our updated [platform roadmap](/page/notion-platform-roadmap).

## December 6 - 18, 2022

### Fixes and Improvements

*   Updated the [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children) endpoints to specific supported block types to create a more consistent dev experience. The endpoints now throw an error if the block type in the request does not [support children](/reference/block#block-types-that-support-children).

### New Things

*   Built a ✨Glitch ✨ demo that updates Notion tasks when a linked GitHub PR is closed or merged. [Give it a spin!](https://glitch.com/~notion-task-github-pr-sync)

## November 22 - December 5, 2022

We took advantage of the US Thanksgiving holiday to host a mini internal hackathon.

Nothing to share from that, yet! It’s been a quiet few weeks.

If you want something to read while you stay tuned for the next update, check out the revised [Get started](/docs/getting-started) guide.

## November 8 - 21, 2022

*   We added a `this_week` filter for database queries. You can now search for database entries where the `"date"`, `"created_time"`, or `"last_edited_time"` property value falls within the current week. Refer to the [date filter condition](/reference/post-database-query-filter#date-filter-condition) docs for details.

## October 25 - November 7, 2022

*   Number database properties now support the Singapore dollar as a currency format. To use it, set `singapore_dollar` as the value for a number’s `format` field when creating or updating a database [property](/reference/property-object#number-configuration) or [schema](/reference/property-schema-object#number-configuration).

## October 11 - 24, 2022

*   You can now add a Notion template option to a public integration from the [integration’s settings page](https://www.notion.so/my-integrations). For details on what the permissions flow looks like for users who opt in to the template, refer to the [Authorization guide](/docs/authorization#permissions-flow-for-integrations-with-a-notion-template-option).

## September 26 - October 10, 2022

*   A [`relation`](/reference/property-value-object#relation-property-values) property value now includes a `has_more` property when returned by the [Retrieve a page endpoint](/reference/retrieve-a-page). `has_more` is `true` if the `has_more` property is `true`. If it's `false`, there are no more pages to load.
```

# Code

relation has more than 25 page references. Otherwise, `has_more` is `false`.

We added a `workspace_name` property to [bot user objects](/reference/user#bots). If the bot `owner.type` is `"workspace"`, then `workspace.name` identifies the name of the workspace that owns the bot. If the `owner.type` is `"user"`, then `workspace.name` is `null`.
```

# Single Property vs Dual Property

In Notion, you can define a **single property** or **dual property**. These can be used to create one-way relations between databases as well as two-way relations within a database.

## New version of the JavaScript SDK

Coinciding with all of these changes, we've released a new major version (v2.0.0) of the [Notion JavaScript SDK](https://github.com/makenotion/notion-sdk-js). To upgrade to this new version, run `npm install @notionhq/client@latest` or `yarn upgrade --latest @notionhq/client` from within your repository.

## June 20 - July 4, 2022

### Features

- Added limited readonly support for database status properties. Read more about status properties [here](https://www.notion.so/help/guides/status-property-gives-clarity-on-tasks).
  - Status property values are returned in the [Retrieve a page](/reference/retrieve-a-page) endpoint. See [Property values](/reference/property-value-object) for more information.
  - Status property configuration is not supported yet. See [Property object](/reference/property-object) for more information.

### Bug Fixes

- Added a validation for adding new rollup properties that prevents creating a rollup of another rollup.

## June 6 - June 19, 2022

### Features

- Added support for creating inline databases with `is_inline`. Read more [here](/reference/database).
- Added support for reading and writing database descriptions with the `description` field. Read more [here](/reference/database).

## May 23 - June 5, 2022

### Bug fixes and performance improvements

- The public API once again supports inline `mailto` links in rich text.

## May 9 - 22, 2022

### Bug fixes and performance improvements

- We now validate URLs used to create inline text links in the public API. For more details on inline links in rich text, see the [Rich text object](/reference/rich-text) documentation.
- The [Search](/reference/post-search) endpoint now returns fuzzier matches, including plurals and different verb tenses. This corresponds to fuzzier matches while searching in the Notion app and should result in more search results overall for any given query.
- Fixed a bug where the integration page at [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) wouldn't load.

## May 10, 2022

### Link Preview APIs

Today we’re excited to launch a new set of APIs for developers to build on — Link Preview APIs. Over the past six months, we launched link previews with tools like Slack, Trello, Figma, and Asana, allowing users to preview authenticated content in a new structured block. Now, we’re ready for any developer to build integrations that support link previews in Notion.

We built link previews to make it easy for users to easily share information in one place using a link. But with a regular link, the information would become automatically stale, making it difficult to share the latest updates among teams. Now, with the new link previews APIs, Notion will let you know when a user pastes a link to a domain you own, let the user authenticate with Notion and your service, and let you unfurl a new link preview block inside Notion.

Learn more about the new link previews APIs [here](/page/link-previews-api), and apply to get access to and build your integration by filling out [this form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).

## April 25 - May 9, 2022

### Bug fixes and performance improvements

- We've shipped a couple of improvements under the hood to make the search and query database endpoints faster. We're actively looking into 500s and timeouts on the query database endpoint in particular.
- Fixed a bug in the OAuth page picker where Shared pages wouldn't load until the workspace switcher was clicked.

## April 11 - 24, 2022

### Bug fixes and performance improvements

- Fixed a bug where some rollups and relations appeared empty when they shouldn't have.
- Fixed a bug in the query database endpoint where an invalid pagination cursor was being returned.

## March 28 - April 10, 2022

There was a [company-wide product bug bash](https://www.notion.so/releases)! As a result nothing API-specific to share for these 2 weeks, but we've been hard at work improving test coverage and paring down tech debt.

## March 14 - 27, 2022

### Features

- You can now filter databases on the created at and last edited at timestamps, even if they don't have a corresponding property of that type. Read more [here](/reference/post-database-query-filter#timestamp-filter-object).
- A [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) response header is now being sent with rate limited request responses. The value of this field is set as an integer number of seconds (in decimal). Requests made after waiting this minimum amount of time should not be rate limited. Read more about our rate limits [here](/reference/request-limits#rate-limits).

### Bug fixes and performance improvements

- Stopped throwing an error when rendering property formulas that hadn't been set up yet in the [Retrieve a page property item](/reference/retrieve-a-page-property) endpoint. These formulas now return `null` values.

## March 18, 2022

### Query a database endpoint supports filtering by timestamp

When [querying a database](/reference/post-database-query) using filters, you previously were only able to build filters using properties that were explicitly defined in the database schema. We've added a new type of filter for the created timestamp and last edited timestamp of any page within the database. This means you can filter by these attributes, even if the database doesn't have a "Created time" or "Last edited time" _property_.

You can read more about this filter type [here](/reference/post-database-query-filter#timestamp-filter-object), but as a preview here is how you would filter by the created timestamp:

```json
{
    "filter": {
        "timestamp": "created_time",
        "created_time": {
          "past_week": {}
        }
    }
}
```

And here's how you would filter by the last edited time:

```json
{
    "filter": {
        "timestamp": "last_edited_time",
        "last_edited_time": {
          "after": "2021-05-10"
        }
    }
}
```

Note that you can also use this filter type within a compound filter.

## February 28, 2022 - March 13, 2022

### Features

- Block colors are now supported in the API! Read more about it [here](/changelog/block-colors-are-now-supported-in-the-api).

### Bug fixes and performance improvements

- Rich text objects now properly include template mentions. Read more about this type of text object [here](/reference/rich-text#template-mentions).

## March 8, 2022

### Block colors are now supported in the API

We have added support for block colors in the Notion Public API. There is now a `color` keyword for the following block types: `paragraph`, `heading_1`, `heading_2`, `heading_3`, `bulleted_list_item`, `numbered_list_item`, `to_do`, `toggle`, `callout`, `quote`, and `table_of_contents`. For these block types, the block color is returned in the [block object](/reference/block), and you can use the [update block](/reference/update-a-block), [append block children](/reference/append-block-children), and [create page](/reference/post-page) endpoints to update the color of existing blocks and create new blocks with color.

The colors supported are `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `red`, and `green`.

## Previous Versions

### June 20 - July 4, 2022

#### Features

- Added limited readonly support for database status properties. Read more about status properties [here](https://www.notion.so/help/guides/status-property-gives-clarity-on-tasks).
  - Status property values are returned in the [Retrieve a page](/reference/retrieve-a-page) endpoint. See [Property values](/reference/property-value-object) for more information.
  - Status property configuration is not supported yet. See [Property object](/reference/property-object) for more information.

#### Bug Fixes

- Added a validation for adding new rollup properties that prevents creating a rollup of another rollup.

### June 6 - June 19, 2022

#### Features

- Added support for creating inline databases with `is_inline`. Read more [here](/reference/database).
- Added support for reading and writing database descriptions with the `description` field. Read more [here](/reference/database).

### May 23 - June 5, 2022

#### Bug fixes and performance improvements

- The public API once again supports inline `mailto` links in rich text.

### May 9 - 22, 2022

#### Bug fixes and performance improvements

- We now validate URLs used to create inline text links in the public API. For more details on inline links in rich text, see the [Rich text object](/reference/rich-text) documentation.
- The [Search](/reference/post-search) endpoint now returns fuzzier matches, including plurals and different verb tenses. This corresponds to fuzzier matches while searching in the Notion app and should result in more search results overall for any given query.
- Fixed a bug where the integration page at [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) wouldn't load.

### May 10, 2022

#### Link Preview APIs

Today we’re excited to launch a new set of APIs for developers to build on — Link Preview APIs. Over the past six months, we launched link previews with tools like Slack, Trello, Figma, and Asana, allowing users to preview authenticated content in a new structured block. Now, we’re ready for any developer to build integrations that support link previews in Notion.

We built link previews to make it easy for users to easily share information in one place using a link. But with a regular link, the information would become automatically stale, making it difficult to share the latest updates among teams. Now, with the new link previews APIs, Notion will let you know when a user pastes a link to a domain you own, let the user authenticate with Notion and your service, and let you unfurl a new link preview block inside Notion.

Learn more about the new link previews APIs [here](/page/link-previews-api), and apply to get access to and build your integration by filling out [this form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).

### April 25 - May 9, 2022

#### Bug fixes and performance improvements

- We've shipped a couple of improvements under the hood to make the search and query database endpoints faster. We're actively looking into 500s and timeouts on the query database endpoint in particular.
- Fixed a bug in the OAuth page picker where Shared pages wouldn't load until the workspace switcher was clicked.

### April 11 - 24, 2022

#### Bug fixes and performance improvements

- Fixed a bug where some rollups and relations appeared empty when they shouldn't have.
- Fixed a bug in the query database endpoint where an invalid pagination cursor was being returned.

### March 28 - April 10, 2022

There was a [company-wide product bug bash](https://www.notion.so/releases)! As a result nothing API-specific to share for these 2 weeks, but we've been hard at work improving test coverage and paring down tech debt.

### March 14 - 27, 2022

#### Features

- You can now filter databases on the created at and last edited at timestamps, even if they don't have a corresponding property of that type. Read more [here](/reference/post-database-query-filter#timestamp-filter-object).
- A [`Retry-After`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After) response header is now being sent with rate limited request responses. The value of this field is set as an integer number of seconds (in decimal). Requests made after waiting this minimum amount of time should not be rate limited. Read more about our rate limits [here](/reference/request-limits#rate-limits).

#### Bug fixes and performance improvements

- Stopped throwing an error when rendering property formulas that hadn't been set up yet in the [Retrieve a page property item](/reference/retrieve-a-page-property) endpoint. These formulas now return `null` values.

### March 18, 2022

#### Query a database endpoint supports filtering by timestamp

When [querying a database](/reference/post-database-query) using filters, you previously were only able to build filters using properties that were explicitly defined in the database schema. We've added a new type of filter for the created timestamp and last edited timestamp of any page within the database. This means you can filter by these attributes, even if the database doesn't have a "Created time" or "Last edited time" _property_.

You can read more about this filter type [here](/reference/post-database-query-filter#timestamp-filter-object), but as a preview here is how you would filter by the created timestamp:

```json
{
    "filter": {
        "timestamp": "created_time",
        "created_time": {
          "past_week": {}
        }
    }
}
```

And here's how you would filter by the last edited time:

```json
{
    "filter": {
        "timestamp": "last_edited_time",
        "last_edited_time": {
          "after": "2021-05-10"
        }
    }
}
```

Note that you can also use this filter type within a compound filter.

### February 28, 2022 - March 13, 2022

#### Features

- Block colors are now supported in the API! Read more about it [here](/changelog/block-colors-are-now-supported-in-the-api).

#### Bug fixes and performance improvements

- Rich text objects now properly include template mentions. Read more about this type of text object [here](/reference/rich-text#template-mentions).

### March 8, 2022

#### Block colors are now supported in the API

We have added support for block colors in the Notion Public API. There is now a `color` keyword for the following block types: `paragraph`, `heading_1`, `heading_2`, `heading_3`, `bulleted_list_item`, `numbered_list_item`, `to_do`, `toggle`, `callout`, `quote`, and `table_of_contents`. For these block types, the block color is returned in the [block object](/reference/block), and you can use the [update block](/reference/update-a-block), [append block children](/reference/append-block-children), and [create page](/reference/post-page) endpoints to update the color of existing blocks and create new blocks with color.

The colors supported are `default`, `gray`, `brown`, `orange`, `yellow`, `green`, `blue`, `purple`, `red`, and `green`.
```

# March 7, 2022

## Updated Developers Terms

With the API officially out of beta, Notion has updated our developer terms of service as of March 1st, 2022. View our updated terms [here](https://www.notion.so/notion/Developer-Terms-ba4131408d0844e08330da2cbb225c20).

## February 14, 2022 - 28, 2022: Block by Block edition!

> 📘The API is officially out of beta!
> 
> Read more about it [here](https://www.notion.so/blog/api-ga).

### Features

- We now have a [roadmap](/page/notion-platform-roadmap), so you have a better sense of what we'll be building next.
- We released a new version of the API, `2022-02-22`. This version makes our requests and responses more consistent across properties, blocks, and filters, and officially deprecates the list databases endpoint. Read more [here](/changelog/releasing-notion-version-2022-02-22).
- We now show the public API status independently of Notion's status on [https://status.notion.so/](https://status.notion.so/).
- Added `created_by` and `edited_by` to pages, blocks, and databases, and added `archived` to databases. Read more [here](/changelog/created-by-and-last-edited-by-properties-in-block-page-and-database-objects).
- Added new ways for admins of Enterprise workspaces to view and control the integrations installed in their workspaces. Read more [here](https://www.notion.so/help/add-and-manage-integrations-with-the-api).
- Added more information to paginated responses to make it easier to fetch complete responses for complex property types. Read more [here](/reference/pagination).

### Bug fixes and performance improvements

- Fixed a bug where pages and databases with archived (i.e. trashed) ancestors would show `archived: false`. They now show `archived: true` because they are, in fact, archived.
- Improved API performance when rendering users who are members in the space. This affects all user, block, and page-related endpoints since users can be mentioned in both page properties and rich text.
- Added a message about sharing relevant pages and databases with a bot in the 404 not found error message. We found that this was one of the more common reasons for API users to get a 404 when calling the API.
- Fixed a bug where bots could be given a more restrictive "Can edit content" access on child databases, which prevented some bots with write access from being able to update the database schema.
- Fixed a bug where user mentions failed with "user not found" when creating new blocks, even if those users should have been visible to the bot.
- Fixed a bug where malformed properties in a single page would cause an entire request to the query database endpoint to fail.
- Fixed a bug where it was possible to update a page/database in the trash. Attempting to update a trashed page or database now returns a validation error.
- Fixed a bug in the get page property endpoint where retrieving a rollup property which referenced a relation containing pages the bot did not have access to skipped those pages and returned an incorrect result. We now return a validation error.
- Fixed a bug in the get page property endpoint where retrieving a formula property whose depth exceeds what we can compute in the API simply returned the wrong value. We now return a validation error.

## March 1, 2022

### Created by and last edited by properties in Block, Page and Database objects

We have added `created_by` and `last_edited_by` properties for [block](/reference/block), [page](/reference/page) and [database objects](/reference/database) corresponding to the users who have created or last edited these objects. Both properties are [user objects](/reference/user) which will contain `object` and `id` keys. This is a backwards compatible change that is available in older versions of the API as well.

We have also added a boolean `archived` property for [database objects](/reference/database) to denote if the database has been deleted. You can use the `archived` property to archive or unarchive a database and its descendants when [updating the database](/reference/update-a-database).

## February 25, 2022

### Releasing Notion-Version 2022-02-22

> 📘Notion's API versions
> 
> As a reminder, we only version backwards incompatible changes, so generally, you still get access to new features we release on the API without needing to upgrade. You can use different version headers for each request, so you can upgrade incrementally to get to the latest version.

We're releasing Notion-Version `2022-02-22` with the following _backwards incompatible_ changes:

- `text` in blocks has been renamed to `rich_text`, to be consistent with the database property type.
- Query database filter changes:
  - `phone` and `text` are no longer supported in query database filters when filtering by `phone_number` and `rich_text` properties. Use `phone_number` and `rich_text` instead.
  - `rollup` query database filters no longer accept the `text` keyword. Use `rich_text` instead.
  - `formula` query database filters no longer accept the `text` keyword. Use `string` instead.
- `property_item` objects now return a `type`, `next_url`, and `id`.
- Deprecated the List Databases API endpoint.

#### The `text` property in content blocks has been renamed to `rich_text`

To be consistent with the database property type, we have renamed the `text` property to `rich_text`. This affects the following block types: `paragraph`, `heading_1`, `heading_2`, `heading_3`, `heading_4`, `heading_5`, `heading_6`, `heading_7`, `heading_8`, `heading_9`, `heading_10`, `heading_11`, `heading_12`, `heading_13`, `heading_14`, `heading_15`, `heading_16`, `heading_17`, `heading_18`, `heading_19`, `heading_20`, `heading_21`, `heading_22`, `heading_23`, `heading_24`, `heading_25`, `heading_26`, `heading_27`, `heading_28`, `heading_29`, `heading_30`, `heading_31`, `heading_32`, `heading_33`, `heading_34`, `heading_35`, `heading_36`, `heading_37`, `heading_38`, `heading_39`, `heading_40`, `heading_41`, `heading_42`, `heading_43`, `heading_44`, `heading_45`, `heading_46`, `heading_47`, `heading_48`, `heading_49`, `heading_50`, `heading_51`, `heading_52`, `heading_53`, `heading_54`, `heading_55`, `heading_56`, `heading_57`, `heading_58`, `heading_59`, `heading_60`, `heading_61`, `heading_62`, `heading_63`, `heading_64`, `heading_65`, `heading_66`, `heading_67`, `heading_68`, `heading_69`, `heading_70`, `heading_71`, `heading_72`, `heading_73`, `heading_74`, `heading_75`, `heading_76`, `heading_77`, `heading_78`, `heading_79`, `heading_80`, `heading_81`, `heading_82`, `heading_83`, `heading_84`, `heading_85`, `heading_86`, `heading_87`, `heading_88`, `heading_89`, `heading_90`, `heading_91`, `heading_92`, `heading_93`, `heading_94`, `heading_95`, `heading_96`, `heading_97`, `heading_98`, `heading_99`, `heading_100`, `heading_101`, `heading_102`, `heading_103`, `heading_104`, `heading_105`, `heading_106`, `heading_107`, `heading_108`, `heading_109`, `heading_110`, `heading_111`, `heading_112`, `heading_113`, `heading_114`, `heading_115`, `heading_116`, `heading_117`, `heading_118`, `heading_119`, `heading_120`, `heading_121`, `heading_122`, `heading_123`, `heading_124`, `heading_125`, `heading_126`, `heading_127`, `heading_128`, `heading_129`, `heading_130`, `heading_131`, `heading_132`, `heading_133`, `heading_134`, `heading_135`, `heading_136`, `heading_137`, `heading_138`, `heading_139`, `heading_140`, `heading_141`, `heading_142`, `heading_143`, `heading_144`, `heading_145`, `heading_146`, `heading_147`, `heading_148`, `heading_149`, `heading_150`, `heading_151`, `heading_152`, `heading_153`, `heading_154`, `heading_155`, `heading_156`, `heading_157`, `heading_158`, `heading_159`, `heading_160`, `heading_161`, `heading_162`, `heading_163`, `heading_164`, `heading_165`, `heading_166`, `heading_167`, `heading_168`, `heading_169`, `heading_170`, `heading_171`, `heading_172`, `heading_173`, `heading_174`, `heading_175`, `heading_176`, `heading_177`, `heading_178`, `heading_179`, `heading_180`, `heading_181`, `heading_182`, `heading_183`, `heading_184`, `heading_185`, `heading_186`, `heading_187`, `heading_188`, `heading_189`, `heading_190`, `heading_191`, `heading_192`, `heading_193`, `heading_194`, `heading_195`, `heading_196`, `heading_197`, `heading_198`, `heading_199`, `heading_200`, `heading_201`, `heading_202`, `heading_203`, `heading_204`, `heading_205`, `heading_206`, `heading_207`, `heading_208`, `heading_209`, `heading_210`, `heading_211`, `heading_212`, `heading_213`, `heading_214`, `heading_215`, `heading_216`, `heading_217`, `heading_218`, `heading_219`, `heading_220`, `heading_221`, `heading_222`, `heading_223`, `heading_224`, `heading_225`, `heading_226`, `heading_227`, `heading_228`, `heading_229`, `heading_230`, `heading_231`, `heading_232`, `heading_233`, `heading_234`, `heading_235`, `heading_236`, `heading_237`, `heading_238`, `heading_239`, `heading_240`, `heading_241`, `heading_242`, `heading_243`, `heading_244`, `heading_245`, `heading_246`, `heading_247`, `heading_248`, `heading_249`, `heading_250`, `heading_251`, `heading_252`, `heading_253`, `heading_254`, `heading_255`, `heading_256`, `heading_257`, `heading_258`, `heading_259`, `heading_260`, `heading_261`, `heading_262`, `heading_263`, `heading_264`, `heading_265`, `heading_266`, `heading_267`, `heading_268`, `heading_269`, `heading_270`, `heading_271`, `heading_272`, `heading_273`, `heading_274`, `heading_275`, `heading_276`, `heading_277`, `heading_278`, `heading_279`, `heading_280`, `heading_281`, `heading_282`, `heading_283`, `heading_284`, `heading_285`, `heading_286`, `heading_287`, `heading_288`, `heading_289`, `heading_290`, `heading_291`, `heading_292`, `heading_293`, `heading_294`, `heading_295`, `heading_296`, `heading_297`, `heading_298`, `heading_299`, `heading_300`, `heading_301`, `heading_302`, `heading_303`, `heading_304`, `heading_305`, `heading_306`, `heading_307`, `heading_308`, `heading_309`, `heading_310`, `heading_311`, `heading_312`, `heading_313`, `heading_314`, `heading_315`, `heading_316`, `heading_317`, `heading_318`, `heading_319`, `heading_320`, `heading_321`, `heading_322`, `heading_323`, `heading_324`, `heading_325`, `heading_326`, `heading_327`, `heading_328`, `heading_329`, `heading_330`, `heading_331`, `heading_332`, `heading_333`, `heading_334`, `heading_335`, `heading_336`, `heading_337`, `heading_338`, `heading_339`, `heading_340`, `heading_341`, `heading_342`, `heading_343`, `heading_344`, `heading_345`, `heading_346`, `heading_347`, `heading_348`, `heading_349`, `heading_350`, `heading_351`, `heading_352`, `heading_353`, `heading_354`, `heading_355`, `heading_356`, `heading_357`, `heading_358`, `heading_359`, `heading_360`, `heading_361`, `heading_362`, `heading_363`, `heading_364`, `heading_365`, `heading_366`, `heading_367`, `heading_368`, `heading_369`, `heading_370`, `heading_371`, `heading_372`, `heading_373`, `heading_374`, `heading_375`, `heading_376`, `heading_377`, `heading_378`, `heading_379`, `heading_380`, `heading_381`, `heading_382`, `heading_383`, `heading_384`, `heading_385`, `heading_386`, `heading_387`, `heading_388`, `heading_389`, `heading_390`, `heading_391`, `heading_392`, `heading_393`, `heading_394`, `heading_395`, `heading_396`, `heading_397`, `heading_398`, `heading_399`, `heading_400`, `heading_401`, `heading_402`, `heading_403`, `heading_404`, `heading_405`, `heading_406`, `heading_407`, `heading_408`, `heading_409`, `heading_410`, `heading_411`, `heading_412`, `heading_413`, `heading_414`, `heading_415`, `heading_416`, `heading_417`, `heading_418`, `heading_419`, `heading_420`, `heading_421`, `heading_422`, `heading_423`, `heading_424`, `heading_425`, `heading_426`, `heading_427`, `heading_428`, `heading_429`, `heading_430`, `heading_431`, `heading_432`, `heading_433`, `heading_434`, `heading_435`, `heading_436`, `heading_437`, `heading_438`, `heading_439`, `heading_440`, `heading_441`, `heading_442`, `heading_443`, `heading_444`, `heading_445`, `heading_446`, `heading_447`, `heading_448`, `heading_449`, `heading_450`, `heading_451`, `heading_452`, `heading_453`, `heading_454`, `heading_455`, `heading_456`, `heading_457`, `heading_458`, `heading_459`, `heading_460`, `heading_461`, `heading_462`, `heading_463`, `heading_464`, `heading_465`, `heading_466`, `heading_467`, `heading_468`, `heading_469`, `heading_470`, `heading_471`, `heading_472`, `heading_473`, `heading_474`, `heading_475`, `heading_476`, `heading_477`, `heading_478`, `heading_479`, `heading_480`, `heading_481`, `heading_482`, `heading_483`, `heading_484`, `heading_485`, `heading_486`, `heading_487`, `heading_488`, `heading_489`, `heading_490`, `heading_491`, `heading_492`, `heading_493`, `heading_494`, `heading_495`, `heading_496`, `heading_497`, `heading_498`, `heading_499`, `heading_500`, `heading_501`, `heading_502`, `heading_503`, `heading_504`, `heading_505`, `heading_506`, `heading_507`, `heading_508`, `heading_509`, `heading_510`, `heading_511`, `heading_512`, `heading_513`, `heading_514`, `heading_515`, `heading_516`, `heading_517`, `heading_518`, `heading_519`, `heading_520`, `heading_521`, `heading_522`, `heading_523`, `heading_524`, `heading_525`, `heading_526`, `heading_527`, `heading_528`, `heading_529`, `heading_530`, `heading_531`, `heading_532`, `heading_533`, `heading_534`, `heading_535`, `heading_536`, `heading_537`, `heading_538`, `heading_539`, `heading_540`, `heading_541`, `heading_542`, `heading_543`, `heading_544`, `heading_545`, `heading_546`, `heading_547`, `heading_548`, `heading_549`, `heading_550`, `heading_551`, `heading_552`, `heading_553`, `heading_554`, `heading_555`, `heading_556`, `heading_557`, `heading_558`, `heading_559`, `heading_560`, `heading_561`, `heading_562`, `heading_563`, `heading_564`, `heading_565`, `heading_566`, `heading_567`, `heading_568`, `heading_569`, `heading_570`, `heading_571`, `heading_572`, `heading_573`, `heading_574`, `heading_575`, `heading_576`, `heading_577`, `heading_578`, `heading_579`, `heading_580`, `heading_581`, `heading_582`, `heading_583`, `heading_584`, `heading_585`, `heading_586`, `heading_587`, `heading_588`, `heading_589`, `heading_590`, `heading_591`, `heading_592`, `heading_593`, `heading_594`, `heading_595`, `heading_596`, `heading_597`, `heading_598`, `heading_599`, `heading_600`, `heading_601`, `heading_602`, `heading_603`, `heading_604`, `heading_605`, `heading_606`, `heading_607`, `heading_608`, `heading_609`, `heading_610`, `heading_611`, `heading_612`, `heading_613`, `heading_614`, `heading_615`, `heading_616`, `heading_617`, `heading_618`, `heading_619`, `heading_620`, `heading_621`, `heading_622`, `heading_623`, `heading_624`, `heading_625`, `heading_626`, `heading_627`, `heading_628`, `heading_629`, `heading_630`, `heading_631`, `heading_632`, `heading_633`, `heading_634`, `heading_635`, `heading_636`, `heading_637`, `heading_638`, `heading_639`, `heading_640`, `heading_641`, `heading_642`, `heading_643`, `heading_644`, `heading_645`, `heading_646`, `heading_647`, `heading_648`, `heading_649`, `heading_650`, `heading_651`, `heading_652`, `heading_653`, `heading_654`, `heading_655`, `heading_656`, `heading_657`, `heading_658`, `heading_659`, `heading_660`, `heading_661`, `heading_662`, `heading_663`, `heading_664`, `heading_665`, `heading_666`, `heading_667`, `heading_668`, `heading_669`, `heading_670`, `heading_671`, `heading_672`, `heading_673`, `heading_674`, `heading_675`, `heading_676`, `heading_677`, `heading_678`, `heading_679`, `heading_680`, `heading_681`, `heading_682`, `heading_683`, `heading_684`, `heading_685`, `heading_686`, `heading_687`, `heading_688`, `heading_689`, `heading_690`, `heading_691`, `heading_692`, `heading_693`, `heading_694`, `heading_695`, `heading_696`, `heading_697`, `heading_698`, `heading_699`, `heading_700`, `heading_701`, `heading_702`, `heading_703`, `heading_704`, `heading_705`, `heading_706`, `heading_707`, `heading_708`, `heading_709`, `heading_710`, `heading_711`, `heading_712`, `heading_713`, `heading_714`, `heading_715`, `heading_716`, `heading_717`, `heading_718`, `heading_719`, `heading_720`, `heading_721`, `heading_722`, `heading_723`, `heading_724`, `heading_725`, `heading_726`, `heading_727`, `heading_728`, `heading_729`, `heading_730`, `heading_731`, `heading_732`, `heading_733`, `heading_734`, `heading_735`, `heading_736`, `heading_737`, `heading_738`, `heading_739`, `heading_740`, `heading_741`, `heading_742`, `heading_743`, `heading_744`, `heading_745`, `heading_746`, `heading_747`, `heading_748`, `heading_749`, `heading_750`, `heading_751`, `heading_752`, `heading_753`, `heading_754`, `heading_755`, `heading_756`, `heading_757`, `heading_758`, `heading_759`, `heading_760`, `heading_761`, `heading_762`, `heading_763`, `heading_764`, `heading_765`, `heading_766`, `heading_767`, `heading_768`, `heading_769`, `heading_770`, `heading_771`, `heading_772`, `heading_773`, `heading_774`, `heading_775`, `heading_776`, `heading_777`, `heading_778`, `heading_779`, `heading_780`, `heading_781`, `heading_782`, `heading_783`, `heading_784`, `heading_785`, `heading_786`, `heading_787`, `heading_788`, `heading_789`, `heading_790`, `heading_791`, `heading_792`, `heading_793`, `heading_794`, `heading_795`, `heading_796`, `heading_797`, `heading_798`, `heading_799`, `heading_800`, `heading_801`, `heading_802`, `heading_803`, `heading_804`, `heading_805`, `heading_806`, `heading_807`, `heading_808`, `heading_809`, `heading_810`, `heading_811`, `heading_812`, `heading_813`, `heading_814`, `heading_815`, `heading_816`, `heading_817`, `heading_818`, `heading_819`, `heading_820`, `heading_821`, `heading_822`, `heading_823`, `heading_824`, `heading_825`, `heading_826`, `heading_827`, `heading_828`, `heading_829`, `heading_830`, `heading_831`, `heading_832`, `heading_833`, `heading_834`, `heading_835`, `heading_836`, `heading_837`, `heading_838`, `heading_839`, `heading_840`, `heading_841`, `heading_842`, `heading_843`, `heading_844`, `heading_845`, `heading_846`, `heading_847`, `heading_848`, `heading_849`, `heading_850`, `heading_851`, `heading_852`, `heading_853`, `heading_854`, `heading_855`, `heading_856`, `heading_857`, `heading_858`, `heading_859`, `heading_860`, `heading_861`, `heading_862`, `heading_863`, `heading_864`, `heading_865`, `heading_866`, `heading_867`, `heading_868`, `heading_869`, `heading_870`, `heading_871`, `heading_872`, `heading_873`, `heading_874`, `heading_875`, `heading_876`, `heading_877`, `heading_878`, `heading_879`, `heading_880`, `heading_881`, `heading_882`, `heading_883`, `heading_884`, `heading_885`, `heading_886`, `heading_887`, `heading_888`, `heading_889`, `heading_890`, `heading_891`, `heading_892`, `heading_893`, `heading_894`, `heading_895`, `heading_896`, `heading_897`, `heading_898`, `heading_899`, `heading_900`, `heading_901`, `heading_902`, `heading_903`, `heading_904`, `heading_905`, `heading_906`, `heading_907`, `heading_908`, `heading_909`, `heading_910`, `heading_911`, `heading_912`, `heading_913`, `heading_914`, `heading_915`, `heading_916`, `heading_917`, `heading_918`, `heading_919`, `heading_920`, `heading_921`, `heading_922`, `heading_923`, `heading_924`, `heading_925`, `heading_926`, `heading_927`, `heading_928`, `heading_929`, `heading_930`, `heading_931`, `heading_932`, `heading_933`, `heading_934`, `heading_935`, `heading_936`, `heading_937`, `heading_938`, `heading_939`, `heading_940`, `heading_941`, `heading_942`, `heading_943`, `heading_944`, `heading_945`, `heading_946`, `heading_947`, `heading_948`, `heading_949`, `heading_950`, `heading_951`, `heading_952`, `heading_953`, `heading_954`, `heading_955`, `heading_956`, `heading_957`, `heading_958`, `heading_959`, `heading_960`, `heading_961`, `heading_962`, `heading_963`, `heading_964`, `heading_965`, `heading_966`, `heading_967`, `heading_968`, `heading_969`, `heading_970`, `heading_971`, `heading_972`, `heading_973`, `heading_974`, `heading_975`, `heading_976`, `heading_977`, `heading_978`, `heading_979`, `heading_980`, `heading_981`, `heading_982`, `heading_983`, `heading_984`, `heading_985`, `heading_986`, `heading_987`, `heading_988`, `heading_989`, `heading_990`, `heading_991`, `heading_992`, `heading_993`, `heading_994`, `heading_995`, `heading_996`, `heading_997`, `heading_998`, `heading_999`, `heading_1000`, `heading_1001`, `heading_1002`, `heading

# Query database filter changes

_version 2022-02-22 no longer supports `phone` and `text` property filters in the query database endpoint._ For consistency with the database property types, use `phone_number` and `rich_text` instead when filtering on `phone_number` and `rich_text` properties.

More concretely, this query database filter will throw a validation error:

```json
{
	"filter": {
		"and": [
			{
				"property": "Phone number",
				"phone": {
					"equals": "1112223333"
				}
			}
		]
	}
}
```

This query database filter will succeed:

```json
{
	"filter": {
		"and": [
			{
				"property": "Phone number",
				"phone_number": {
					"equals": "1112223333"
				}
			}
		]
	}
}
```

`_`phone` and `text` no longer supported`_

## Property list items now have types

Property item lists now always have type `property_item`. Rollup aggregations are now returned inside that type.

We've also added the property `id` field and the `next_url` to fetch the next set of property items.

### Example of a previous `rollup` `property_item` list

```json
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "type": "relation",
      "relation": {
        "id": "83f92c9d-523d-466e-8c1f-9bc2c25a99fe"
      }
    },
    ...
  ],
  "next_cursor": "some-next-cursor-value",
  "has_more": true,
  "rollup": {
    "type": "date",
    "date": {
      "start": "2021-10-07T14:42:00.000+00:00",
      "end": null
    },
    "function": "latest_date"
  },
  "type": "rollup"
}
```

### Example of the updated `rollup` `property_item` list

```json
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "id": "xYz890",
      "type": "relation",
      "relation": {
        "id": "83f92c9d-523d-466e-8c1f-9bc2c25a99fe"
      }
    },
    ...
  ],
  "next_cursor": "some-next-cursor-value",
  "has_more": true,
  "type": "property_item",
  "property_item": {
    "id": "aBcD123",
    "next_url": "https://api.notion.com/v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75/properties/aBcD123?start_cursor=some-next-cursor-value",
    "type": "rollup",
    "rollup": {
      "type": "date",
      "date": {
        "start": "2021-10-07T14:42:00.000+00:00",
        "end": null
      },
      "function": "latest_date"
    }
  }
}
```

## Deprecated the List Databases endpoint

List all [Databases](/reference/database) endpoint is removed starting in this version. You can use the [Search API](/reference/post-search) for this functionality instead. The List Databases endpoint only returns explicitly shared databases, while search will also return child pages and databases within explicitly shared pages.

# January 31, 2022 - February 13, 2022

> **📘** We're trying something new
> 
> We're experimenting with publishing biweekly changelogs in addition to our existing changelogs about new features. The biweekly changelogs will include bug fixes and improvements that are not big enough to justify their own changelog entry.
> 
> The timing may be somewhat irregular until we smooth the process out, but we hope to align on a regular schedule soon. This is our first regular changelog entry; we hope you find it useful.

## Bug fixes and performance improvements

* We added an optimization for search when filtering by pages or databases. This should particularly help latency when using search to power a database picker in a large workspace. For more details about search and how to optimize search requests, see the [search documentation](/reference/post-search).
* We fixed an issue where fetching an embed block containing an uploaded file returned the wrong file URL.

# January 25, 2022

## Caption property is now supported for code block type

We have added support for adding, updating, and retrieving the `caption` property for `code` block types.

Below is an example response from [append block children](/reference/patch-block-children) containing a code block, with a caption, uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "code",
            "code": {
                "caption": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Hello Caption!",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Hello Caption!",
                        "href": null
                    }
                ],
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "const foo = \"bar\"",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "const foo = \"bar\"",
                        "href": null
                    }
                ],
                "language": "javascript"
            }
        },
    ],
    "next_cursor": null,
    "has_more": false
}
```

# January 5, 2022

We have added support for simple tables in the API.

## Example of a previous `rollup` `property_item` list

```json
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "type": "relation",
      "relation": {
        "id": "83f92c9d-523d-466e-8c1f-9bc2c25a99fe"
      }
    },
    ...
  ],
  "next_cursor": "some-next-cursor-value",
  "has_more": true,
  "rollup": {
    "type": "date",
    "date": {
      "start": "2021-10-07T14:42:00.000+00:00",
      "end": null
    },
    "function": "latest_date"
  },
  "type": "rollup"
}
```

## Example of the updated `rollup` `property_item` list

```json
{
  "object": "list",
  "results": [
    {
      "object": "property_item",
      "id": "xYz890",
      "type": "relation",
      "relation": {
        "id": "83f92c9d-523d-466e-8c1f-9bc2c25a99fe"
      }
    },
    ...
  ],
  "next_cursor": "some-next-cursor-value",
  "has_more": true,
  "type": "property_item",
  "property_item": {
    "id": "aBcD123",
    "next_url": "https://api.notion.com/v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75/properties/aBcD123?start_cursor=some-next-cursor-value",
    "type": "rollup",
    "rollup": {
      "type": "date",
      "date": {
        "start": "2021-10-07T14:42:00.000+00:00",
        "end": null
      },
      "function": "latest_date"
    }
  }
}
```

# Simple tables and simple table rows

Tables are parent blocks for table row children. They can only contain children of type `table_row`.

When creating a table block via the [Append block children](/reference/patch-block-children) endpoint, the `table` must have at least 1 `table_row` whose `cells` array has the same length as the `table_width`.

To fetch content for a `table`, fetch the the `table_row` children via [Retrieve block children](/reference/get-block-children). The `table` block itself only contains formatting data, no content.

### Table block example:

```json
{
	"type": "table",
	"table": {
		"table_width": 3,
		"has_column_header": false,
		"has_row_header": false
	}
}
```

### Table row block example:

```json
{
  "type": "table_row",
  "table_row": {
    "cells": [
      [
        {
          "type": "text",
          "text": {
            "content": "column 1 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 1 content",
          "href": null
        }
      ],
      [
        {
          "type": "text",
          "text": {
            "content": "column 2 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 2 content",
          "href": null
        }
      ],
      [
        {
          "type": "text",
          "text": {
            "content": "column 3 content",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "column 3 content",
          "href": null
        }
      ]
    ]
  }
}
```

For more details, refer to the [Block object](/reference/block) docs.

## December 15, 2021

Both public and internal integrations now support having more granular capabilities, which enforce what an integration can do and see in a Notion workspace. These capabilities when put together enforce which API endpoints an integration can call, and what content and user related information they are able to see. For further information on capabilities and best practices, see the [capabilities reference](/reference/capabilities).

### Content capabilities

Integrations can have any combination of read content, insert content, or update content capabilities.

- The **read content** capability gives the integration access to read existing content in a Notion workspace.
- The **insert content** capability gives the integration permission to create new content in a Notion workspace.
- The **update content** capability gives the integration permission to update existing content in a Notion workspace.

### User capabilities

Integrations have different levels of user capabilities, which affect how [user objects](/reference/user) are returned from the Notion API:

- No user information - the integration will not be able to request any information about users. User objects will not include information about the user, including name, profile images, or their email address.
- User information without email addresses - user objects will include other information about the user, including their name or profile images, but omit the email address.
- User information with email addresses - user objects will include all information about the user, including name, profile images, and their email address.

### Limitations

An installed integration can never supersede the capabilities of the user who owns the integration. For example, an integration cannot insert or update on a page if the owner has read-only access.

### Existing integrations

All existing integrations will continue to have the same functionality as before. Any integrations created before December 15, 2021 automatically will have all content capabilities, and user capabilities that give access to user information including email addresses.

### Updating integrations

Update the capabilities on an existing integration through [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations). After updating a public integration's capabilities, users will need to re-authenticate with the integration to apply the new capabilities to their installation. After re-authenticating a public integration with changed capabilities, or updating an internal integration with changed capabilities, the new capabilities will apply to all pages already shared with the integration. For more information on setting capabilities see the [Authorization](/docs/authorization) guide.

## December 14, 2021

### Time zone support

We have added an optional `time_zone` field (based on the [IANA database](https://www.iana.org/time-zones) time zone values) to the Date objects. Developers can now explicitly set the time zones of Date property values using the `time_zone` field. Once this property is set explicitly, users will be able to see the same time zone in the app. When time zone information is provided in this method, `start` and `end` cannot contain [UTC offset](https://en.wikipedia.org/wiki/UTC_offset)s. In addition when time zone information is provided in dates, `start` and `end` cannot be dates without time information (i.e. `"2020-12-08"`).

The public API will always return the `time_zone` field as `null` when rendering dates and time zone will be displayed as a [UTC offset](https://en.wikipedia.org/wiki/UTC_offset) in the `start` and `end` date fields.

## November 17, 2021

### Synced Block, Link to Page and Template block types are now supported in the API

We have added support for adding and retrieving `synced_block`, `link_to_page` and `template` block types.

#### Synced Block block type

Similar to the UI, there are two versions of a `synced_block` -- the original block that was created first and doesn't yet sync with anything else, and the reference blocks that are synced to the original synced block.

**Original Synced Block**

To create a `synced_block`, the developer needs to create an original synced block. Developers will be able to identify the original `synced_block` because it does not "sync_from" any other block (i.e. the `synced_from` property is set to `null`).

This is an example of an "original" `synced_block`. Note that all of the blocks available to be synced in another `synced_block` are captured in the `children` property.

```json
{
    "type": "synced_block",
    "synced_block": {
        "synced_from": null,
        "children": [
            {
                "callout": {
                    "text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "Callout in synced block"
                            }
                        }
                    ]
                }
            }
        ]
    }
}
```

**Reference Synced Blocks**

To sync the content of the original `synced_block` with another `synced_block`, the developer simply needs to refer to that `synced_block` using the `synced_from` property.

Below is an example of a `synced_block` referring to another `synced_block`. Note that only "original" synced blocks can be referenced in the `synced_from` property.

```json
{
    "type": "synced_block",
    "synced_block": {
        "synced_from": {
            "block_id": "original_synced_block_id"
        }
    }
}
```

Below is the example response after creating the `synced_block` above. We can tell that the content from the original synced block is synced with this one because this block has children even though we didn't explicitly set the children in the body of our API call above (i.e. `has_children` property on the reference block is `true`).

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block_id",
            "created_time": "2021-11-17T22:17:00.000Z",
            "last_edited_time": "2021-11-17T22:17:00.000Z",
            "has_children": true,
            "archived": false,
            "type": "synced_block",
            "synced_block": {
                "synced_from": {
                    "type": "block_id",
                    "block_id": "original_synced_block_id"
                }
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

> 🚧 Important notes:
> 
> 1. The bot must have access to both the original and reference synced blocks
> 2. Similar to the UI, we don't support changes to `synced_from` at this time

#### Link to Page block type

We have added support for adding and retrieving `link_to_page` block types. Using this block type, developers can now create page links to other pages (using the `page_id` property) and full page databases (using the `database_` property).

##### Example

```json
{
    "type": "link_to_page",
    "link_to_page": {
        "page_id": "page_id"
    }
}
```

##### Response

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block_id",
            "created_time": "2021-11-17T22:17:00.000Z",
            "last_edited_time": "2021-11-17T22:17:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "link_to_page",
            "link_to_page": {
                "page_id": "page_id"
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```
```

# Public API Changes

## November 10, 2021

The public API now supports returning `link_preview` blocks and mentions found in `rich_text`. Previously, these blocks had type `unsupported` and mentions were skipped in `rich_text`. Note: `link_preview`s cannot be created via the API, only returned in responses.

See the documentation in [blocks](/reference/block#link-preview-blocks) and [`rich_text`](/reference/rich-text#link-preview-mentions) for more information.

```json
{
  "type": "link_preview",
  //...other keys excluded
  "link_preview": {
    "url": "https://github.com/example/example-repo/pull/1234"
  }
}
```

## October 25, 2021

We have added support for `column_list` and `column` block types.

You can now add Column Lists and Columns to pages and other block types.

Column Lists are parent blocks for column children. They can only contain children of type `column`.

Columns are parent blocks for any supported block children, excluding `column`s. They can only be appended to `column_list`s.

When initially creating a column list block via [Append block children](/reference/patch-block-children), the column list must have at least 2 columns, and those columns must have at least one child each.

When fetching content for a column_list, first fetch the column children via [Retrieve block children](/reference/get-block-children). Then fetch the children for each column block.

Below is an example request body for appending `column_list` and nested `column` children.

```json
{
  "children": [
    {
      "object": "block",
      "type": "column_list",
      "column_list": {
        "children": [
          {
            "object": "block",
            "type": "column",
            "column": {
              "children": [
                {
                  "object": "block",
                  "type": "paragraph",
                  "paragraph": {
                    "text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "some text here"
                        }
                      }
                    ]
                  }
                }
              ]
            }
          },
          {
            "object": "block",
            "type": "column",
            "column": {
              "children": [
                {
                  "object": "block",
                  "type": "paragraph",
                  "paragraph": {
                    "text": [
                      {
                        "type": "text",
                        "text": {
                          "content": "some text here"
                        }
                      }
                    ]
                  }
                }
              ]
            }
          }
        ]
      }
    }
  ]
}
```

Below is an example response of appending `column_list` children.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "ca042aa7-2e23-4541-8059-abff360d6752",
            "created_time": "2021-10-25T17:00:00.000Z",
            "last_edited_time": "2021-10-25T17:00:00.000Z",
            "has_children": true,
            "archived": false,
            "type": "column_list",
            "column_list": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

Below is an example request body for appending `column` children. Note that the parent that is being added to must be a block of type `column_list`.

```json
{
    "children": [
        {
            "object": "block",
            "type": "column",
            "column": {
                "children": [
                    {
                        "object": "block",
                        "type": "paragraph",
                        "paragraph": {
                            "text": [
                                {
                                    "type": "text",
                                    "text": {
                                        "content": "some text here"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    ]
}
```

Below is an example response of appending `column` children.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "f40c3a13-30d1-4594-bd6f-cdbc15b2c006",
            "created_time": "2021-10-25T21:25:00.000Z",
            "last_edited_time": "2021-10-25T21:25:00.000Z",
            "has_children": true,
            "archived": false,
            "type": "column",
            "column": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## October 18, 2021

### Validation on embed block URLs

The public API will now return errors on embeds blocks that are not supported by the public API. The supported embed block types (as listed and kept up to date in the [Block Object](/reference/block#embed-blocks) documentation):

- Framer
- Twitter (tweets)
- Google Drive documents
- Gist
- Figma
- Invision
- Loom
- Typeform
- Codepen
- PDFs
- Google Maps
- Whimisical
- Miro
- Abstract
- Excalidraw
- Sketch
- Replit

Previously failed embeds would return a successful request, but produce an error in the Notion Application. Failed embed requests will now return a 400 Client Error.

For non embed URLs, consider using the `bookmark` or `image` block types.

## October 17, 2021

### Dates with times and timezones are now supported on Database Date Filters

Previously, the date filters `equals`, `after`, `before`, `on_or_after`, and `on_or_before` only supported dates without times nor timezones.

Now the database date filters can accept ISO 8601 dates with timestamps and timezones.

```json
{
    "filter": {
        "or": [
            {
                "property": "My Time Property",
                "date": {
                    "before": "2021-10-15T12:00:00-07:00"
                }
            }
        ]
    },
    "sorts": []
}
```

## October 15, 2021

### Breadcrumb block types are now supported in the API

We have added support for adding and retrieving `Breadcrumb` block types.

You can now add Breadcrumb blocks to pages and other blocks.

Below is an example response from [Append block children](/reference/patch-block-children) containing a Breadcrumb block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "breadcrumb",
            "breadcrumb": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## October 14, 2021

### Table of contents and divider block types are now supported

We have added support for adding and retrieving `Table of Contents` and `Divider` block types.

#### Table of Contents blocks

We have added support for adding and retrieving `Table of Contents` block types.

You can now add Table of Contents blocks to pages and other blocks.

Below is an example response from [Append block children](/reference/patch-block-children) containing a Table of Contents block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-14T18:10:00.000Z",
            "last_edited_time": "2021-10-14T18:10:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "toc",
            "toc": {}
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

# Icon fa fa-anchor

## October 11, 2021

### Users can now add Equation Blocks, Embed, Bookmark, and Media Blocks

We have added support for retrieving, adding, and updating Equation Blocks. We have also added support for updating Embed, Bookmark, and Media (including image, video, audio, file, PDF) block types.

#### Equation Blocks

You can now add, retrieve, and update equation blocks when using the [Append block children](/reference/patch-block-children), [Retrieve block children](/reference/get-block-children), and [Update block](/reference/update-a-block) API endpoints.

##### Example Response from [Append block children](/reference/patch-block-children)

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "2d97bf53-7e79-4efd-a6b2-53c0026ed1b5",
            "created_time": "2021-10-11T17:56:00.000Z",
            "last_edited_time": "2021-10-11T17:56:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "equation",
            "equation": {
                "expression": "e = mc^2"
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

#### Media Blocks (video, audio, image, file, PDF)

You can now update media blocks when using the [Update block](/reference/update-a-block).

> Only media blocks of type external are supported
>
> Updated Media blocks must be of type "external" and must reference an external URL. File upload is not currently supported.

##### Example Response from [Update block](/reference/update-a-block)

```json
{
    "object": "block",
    "id": "37af9d6e-290a-488b-9d53-fb4b983f8289",
    "created_time": "2021-10-12T23:11:00.000Z",
    "last_edited_time": "2021-10-12T23:12:00.000Z",
    "has_children": false,
    "archived": false,
    "type": "video",
    "video": {
        "caption": [
            {
                "type": "text",
                "text": {
                    "content": "My caption",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "My caption",
                "href": null
            }
        ],
        "type": "external",
        "external": {
            "url": "https://www.youtube.com/watch?v=aA7si7AmPkY"
        }
    }
}
```

#### Embed and Bookmark Block Types

You can now update embed and bookmark blocks when using the [Update block](/reference/update-a-block).

##### Example Response from [Update block](/reference/update-a-block)

```json
{
    "object": "block",
    "id": "050010f8-d164-4f5d-85a0-fc9db4598107",
    "created_time": "2021-10-12T23:05:00.000Z",
    "last_edited_time": "2021-10-12T23:06:00.000Z",
    "has_children": false,
    "archived": false,
    "type": "bookmark",
    "bookmark": {
        "caption": [
            {
                "type": "text",
                "text": {
                    "content": "My caption",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "My caption",
                "href": null
            }
        ],
        "url": "http://www.notion.so"
    }
}
```

### October 7, 2021

#### Users can now add and update Callout and Quote block types

> New API endpoints and block types not supported in older versions of the API as of September 28
>
> As of September 28, 2021, new block types and API endpoints will _not_ be supported in older versions of the API. If you're currently on version `2021-05-11` or `2021-05-13`, upgrade to `2021-08-16` to take advantage of the new block types in this changelog and any other block types or endpoints introduced after September 28.
>
> API functionality introduced before September 28 will continue to work with older API versions.

We have added support for retrieving, adding, and updating quote and callout block types.

##### Quote blocks

You can now add and retrieve quote blocks when using the [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

##### Example Response from [Append block children](/reference/patch-block-children)

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "block-id",
            "created_time": "2021-10-07T19:21:00.000Z",
            "last_edited_time": "2021-10-07T19:21:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "quote",
            "quote": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "The digital revolution is far more significant than the invention of writing or even of printing.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": true,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "The digital revolution is far more significant than the invention of writing or even of printing.",
                        "href": null
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "\n-Douglas Engelbart",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "\n-Douglas Engelbart",
                        "href": null
                    }
                ]
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

##### Callout blocks

You can now add and retrieve callout blocks when using the [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

##### Example Response from [Retrieve block](/reference/retrieve-a-block)

```json
{
    "object": "block",
    "id": "block-id",
    "created_time": "2021-10-07T19:23:00.000Z",
    "last_edited_time": "2021-10-07T19:24:00.000Z",
    "has_children": false,
    "archived": false,
    "type": "callout",
    "callout": {
        "text": [
            {
                "type": "text",
                "text": {
                    "content": "Note: Something special is happening above",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "Note: Something special is happening above",
                "href": null
            }
        ],
        "icon": {
            "type": "emoji",
            "emoji": "💡"
        }
    }
}
```

### October 5, 2021

#### Retrieve page property item

Developers can now individually retrieve the value of their page properties with the [Retrieve a page property](/reference/retrieve-a-page-property) endpoint! This includes pagination through a list of property item objects for properties with long values or lots of page references such as formula, relations, and rollups. See the [documentation](/reference/retrieve-a-page-property) for more info.

Use the [Retrieve a database](/reference/retrieve-a-database) endpoint to obtain the `property_id`.

**Simple Property Types**

Most properties will be identified by a `type` with the property value in the object found in key `{type}`.

*Example Request/Response*

```curl
curl --request GET \
  --url http://localhost:3000/v1/pages/b55c9c91-384d-452b-81db-d1ef79372b75/properties/some-property-id \
  --header 'Authorization: Bearer $NOTION_API_KEY' \
  --header 'Notion-Version: 2021-08-16'
```

```json
{
  "object": "property_item",
  "type": "number",
  "number": 2
}
```

**Paginated Property Types**

Properties of type `title`, `rich_text`, `relation`, and `people` will return a paginated list of [Property Item Objects](/reference/retrieve-a-page-property#property-item-objects).

*Example List Response*

```json
{
    "object": "list",
    "results": [
        {
            "object": "property_item",
            "type": "rich_text",
            "rich_text": {
                "type": "text",
                "text": {
                    "content": "Avocado ",
                    "link": null
                },
                "annotations": {
                    "bold": false,
                    "italic": false,
                    "strikethrough": false,
                    "underline": false,
                    "code": false,
                    "color": "default"
                },
                "plain_text": "Avocado ",
                "href": null
            }
        },
... // additional results omitted. 
    ],
    "next_cursor": "some-next-cursor-value",
    "has_more": true
}
```

**Rollup Property Types**

Rollups of type 'Show Original', 'Show unique', 'Count unique', and 'Median' return a flattened list of property items. All other rollups are returned a list of relations and (after pagination) a [rollup property value](/) of type `date` or `number`.

*Example Paginated Property Item Request/Response*

A rollup page property with an aggregation that requires additional pagination.

```curl
```

# October 4, 2021

## Retrieve your token's bot user with GET /v1/users/me

If you're using Notion API version `2021-08-16`, you can now retrieve information about the bot associated with your API token, including its ID and the user who authorized it.

**Example request**

```bash
curl --request GET \
  --url http://localhost:3000/v1/users/me \
  --header 'Authorization: Bearer $NOTION_API_KEY' \
  --header 'Notion-Version: 2021-08-16'
```

**Example response**

```json
{
  "object": "user",
  "id": "16d84278-ab0e-484c-9bdd-b35da3bd8905",
  "name": "pied piper",
  "avatar_url": null,
  "type": "bot",
  "bot": {
    "owner": {
      "type": "user",
      "user": {
        "object": "user",
        "id": "5389a034-eb5c-47b5-8a9e-f79c99ef166c",
        "name": "christine makenotion",
        "avatar_url": null,
        "type": "person",
        "person": {
          "email": "[email protected]"
        }
      }
    }
  }
}
```

# October 1, 2021

## New functionality not available to old API versions; code, inline databases, and database page block

> 🚧New API endpoints and block types not supported in older versions of the API as of September 28
>
> As of September 28, 2021, new block types and API endpoints will _not_ be supported in older versions of the API. If you're currently on version `2021-05-11` or `2021-05-13`, upgrade to `2021-08-16` to take advantage of the new block types in this changelog and any other block types or endpoints introduced after September 28.
>
> API functionality introduced before September 28 will continue to work with older API versions.

We have added support for retrieving, adding and updating code blocks, inline databases and database page blocks.

### Code blocks

You can now retrieve and add code blocks when using [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

Below is an example response from [Retrieve block children](/reference/get-block-children) containing a code block uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "ee27cd42-eaad-467f-9956-c0aa4efa94b5",
            "created_time": "2021-09-22T20:27:00.000Z",
            "last_edited_time": "2021-09-27T19:25:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "code",
            "code": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "const a = 21\nconst b = a + 5",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "const a = 21\nconst b = a + 5",
                        "href": null
                    }
                ],
                "language": "javascript"
            }
        },
    ],
    "next_cursor": null,
    "has_more": false
}
```

### Inline databases and database page blocks

You can now retrieve and update child database blocks when using [Retrieve block children](/reference/get-block-children) and [Retrieve block](/reference/retrieve-a-block).

> 📘Updating `child_database` blocks
>
> To update `child_database` type blocks, use the [Update database](/reference/update-a-database) endpoint. Updating the block's `title` updates the text displayed in the associated `child_database` block.

Below is an example response from [Retrieve block children](/reference/get-block-children) containing a child database uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "0d6ff4f9-1211-4129-ab4a-19dfc33d4d7a",
            "created_time": "2021-09-27T20:25:00.000Z",
            "last_edited_time": "2021-09-27T20:25:00.000Z",
            "has_children": false,
            "archived": false,
            "type": "child_database",
            "child_database": {
                "title": "My child database"
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

# September 21, 2021

## Workspace-level tokens for public integrations will be deprecated soon; migrate your OAuth flows

Starting today we will be changing who can authorize public integrations in Notion workspaces. The previously released authorization method will be fully deprecated on October 19.

### About the change

Currently OAuth tokens function on a workspace level: only admins in a workspace can grant access and there can only be one token per workspace per integration. After a brief transition period (see "How to prepare for this change" below) we will be switching exclusively to user-level tokens. These can be granted by any admin or member in the workspace, and there can be as many tokens per workspace as there are admins and members in the workspace.

See the table for the differences between these two methods:

|  | Workspace-level tokens (old) | User-level tokens (new) |
| --- | --- | --- |
| Who can go through OAuth and grant access | Admins only | Admins and members |
| Number of access tokens per workspace | 1 | Up to N, where N is the number of admins and members |
| Who can go through OAuth and reauthorize access for a given token | Only the original user who went through OAuth to grant the token | Only the original user who went through OAuth to grant the token |
| OAuth token response | Contains an `owner` field with the value `{ workspace: true }` | Contains an `owner` field with the value `{ user: <API user object> }` |
| What resources an integration has access to | Pages/databases the installing user chooses via the page picker during OAuth; pages/databases the installing user and other users in the workspace share with the integration via the Page menu; children of pages/databases that were shared with the integration | Pages/databases the installing user chooses via the page picker during OAuth; pages/databases the installing user shares with the integration via the Page menu; children of pages/databases that were shared with the integration |
| What an integration can do with resources it has access to | Read and write | Read and write |

### How to prepare for this change

This change only affects public integrations; that is, integrations that can be installed across many workspaces via OAuth. It does not affect internal integrations.

1. Ensure that you can store and handle multiple Notion API tokens per workspace where your integration is granted access. You may map tokens directly to the `bot_id` which is returned in the OAuth token response and is guaranteed to be unique per API token.
   - To avoid overwriting tokens, do not map the token to the `workspace_id` returned in the OAuth token response, since a workspace may have multiple tokens. Do not map the token to the `owner.user.id` in the OAuth token response, since a user may install your integration in multiple workspaces.
2. Add `&owner=user` to your OAuth authorization URL (the url starting with `https://api.notion.com/v1/oauth/authorize`) once your application is ready for user-level tokens.

### What to expect on October 19

On October 19, we will migrate all existing workspace-level tokens to user-level tokens. We will also default to creating user-level tokens when a user goes through OAuth, regardless of the `owner` parameter in the OAuth URL.

# September 17, 2021

## Database objects now contain url

[Database objects](/reference/database) now return the web address of the database in the `url` key.

```bash
{
  "object": "database",
  "id": "668d797c-76fa-4934-9b05-ad288df2d136",
  "created_time": "2020-03-17T19:10:04.968Z",
  "last_edited_time": "2020-03-17T21:49:37.913Z",
  "parent": {
    "type": "page_id",
    "page_id": "48f8fee9-cd79-4180-bc2f-ec0398253067"
  },
  "icon": {
    "type": "emoji",
    "emoji": "🎉"
  },
  "cover": {
    "type": "external",
    "external": {
      	"url": "https://website.domain/images/image.png"
    }
  },
  "url": "https://www.notion.so/668d797c76fa49349b05ad288df2d136",
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Grocery List",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Grocery List",
      "href": null
    }
  ],
  "properties": {
    "Name": {
      "id": "title",
      "type": "title",
      "title": {}
    },
    "Description": {
      "id": "J@cS",
      "type": "rich_text",
      "rich_text": {}
    },
    "In stock": {
      "id": "{xY`",
      "type": "checkbox",
      "checkbox": {}
    },
    "Food group": {
      "id": "TJmr",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "96eb622f-4b88-4283-919d-ece2fbed3841",
            "name": "🥦Vegetable",
            "color": "green"
          },
          {
            "id": "bb443819-81dc-46fb-882d-ebee6e22c432",
            "name": "🍎Fruit",
            "color": "red"
          },
          {
            "id": "7da9d1b9-8685-472e-9da3-3af57bdb221e",
            "name": "💪Protein",
            "color": "yellow"
          }
        ]
      }
    },
    "Price": {
      "id": "cU^N",
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Cost of next trip": {
      "id": "p:sC",
      "type": "formula",
      "formula": {
        "value": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
      }
    },
    "Last ordered": {
      "id": "]\\R[",
      "type": "date",
      "date": {}
    },
    "Meals": {
      "type": "relation",
      "relation": {
        "database": "668d797c-76fa-4934-9b05-ad288df2d136",
        "synced_property_name": null
      }
    },
    "Number of meals": {
      "id": "Z\\Eh",
      "type": "rollup",
      "rollup": {
        "rollup_property_name": "Name",
        "relation_property_name": "Meals",
        "rollup_property_id": "title",
        "relation_property_id": "mxp^",
        "function": "count"
      }
    },
    "Store availability": {
      "type": "multi_select",
      "multi_select": {
        "options": [
          [
            {
              "id": "d209b920-212c-4040-9d4a-bdf349dd8b2a",
              "name": "Duc Loi Market",
              "color": "blue"
            },
            {
              "id": "70104074-0f91-467b-9787-00d59e6e1e41",
              "name": "Rainbow Grocery",
              "color": "gray"
            },
            {
  
```

# September 10, 2021

## Users can now delete Block objects

The Notion API now supports the [Delete a block](/reference/delete-a-block) endpoint for all supported block types (include pages). The endpoint mirrors the behavior in the Notion application UI where items are added to the "Trash" bucket. In addition, the [Block object](/reference/block) now returns a boolean `archived` field to denote if the block has been deleted.

After deleting (archiving) the block, it can be unarchived using the [Update a block](/reference/update-a-block) or [Update page](/reference/patch-page) endpoint with the body 
```
archived: false
```.

### Example Request

```bash
curl 'https://api.notion.com/v1/blocks/9bc30ad4-9373-46a5-84ab-0a7845ee52e6' \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H 'Notion-Version: 2021-08-16' \
  -X DELETE \
```

### Example Response

```json
{
  "object": "block",
  "id": "9bc30ad4-9373-46a5-84ab-0a7845ee52e6",
  "created_time": "2021-03-16T16:31:00.000Z",
  "last_edited_time": "2021-03-16T16:32:00.000Z",
  "has_children": false,
  "type": "to_do",
  "archived": true
  "to_do": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "Lacinato kale",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "Lacinato kale",
        "href": null
      }
    ],
    "checked": false
  }
}
```

# September 9, 2021

## Relation and rollup properties can now be created in databases

When [creating](/reference/create-a-database) or [updating](/reference/update-a-database) databases, you can now add `relation` and `rollup` property types. Note that the related database must also be shared with the integration.

### Example Request

```bash
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer "$NOTION_API_KEY"' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-08-16' \
--data '{
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Meals": {
          "relation": {
            "database_id": "668d797c-76fa-4934-9b05-ad288df2d136",
          }
    		},
        "Number of meals": {
          "rollup": {
            "rollup_property_name": "Name",
            "relation_property_name": "Meals",
            "function": "count"
          }
        }
    }
}'
```

### Example Response

```json
{
    "object": "database",
    "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
    "created_time": "2021-07-08T23:50:00.000Z",
    "last_edited_time": "2021-07-08T23:50:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
       "Name": {
            "id": "title",
            "type": "title",
            "title": {}
        },
        "Description": {
            "id": "V}lX",
            "type": "rich_text",
            "rich_text": {}
        },
        "In stock": {
            "id": "V> GQ",
            "type": "checkbox",
            "checkbox": {}
        },
        "Meals": {
          "type": "relation",
          "relation": {
            "database_id": "668d797c-76fa-4934-9b05-ad288df2d136",
            "synced_property_name": "Related to Grocery List (Meals)"
          }
        },
        "Number of meals": {
          "id": "Z\\Eh",
          "type": "rollup",
          "rollup": {
            "rollup_property_name": "Name",
            "relation_property_name": "Meals",
            "rollup_property_id": "title",
            "relation_property_id": "mxp^",
            "function": "count"
          }
        },
        
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

# August 24, 2021

## Page icons, cover images, new block types, and improved page file properties

We have added support for linking to external image and file URLs, and many new block types, including image, embed, and file blocks.

You can now use the Notion API to:

- Retrieve and update [page](/reference/page) and [database](/reference/database) icons and cover images.
- [List](/reference/get-block-children) and [append](/reference/patch-block-children) embed, image, video, file, PDF, and bookmark blocks
- Retrieve URL for [file page properties](/reference/page#files-property-values)
- Update [file page properties](/reference/page#files-property-values)

We do not yet support uploading files to Notion through the API, however, any files already uploaded to Notion can be retrieved. You can reference the details of what is supported [here](#externally-hosted-files-vs-files-hosted-by-notion).

### Page Icons and Cover Images

When fetching a [Page object](/reference/page) or a [Database object](/reference/database), the response will now include an `icon` and `cover` property, as shown below:

```json
{
    "object": "database",
    "id": "96433ad8-3fbe-460f-a007-72311c4aa804",
    "cover": {
        "type": "external",
        "external": {
            "url": "https://website.domain/images/image.png"
        }
    },
    "icon": {
        "type": "emoji",
        "emoji": "🎉"
    },
    // ... remaining properties
}
```

The [Create a page](/reference/post-page), [Update page](/reference/patch-page), [Create a database](/reference/create-a-database), and [Update database](/reference/update-a-database) API endpoints now support the ability to set the page icon and cover image.

### New Block Types

You can now retrieve and add embed, image, video, file, pdf, and bookmark blocks when using [Append block children](/reference/patch-block-children) and [Retrieve block children](/reference/get-block-children).

Below is an example response from [Retrieve a page](/reference/retrieve-a-page) containing an image uploaded to Notion.

```json
{
    "object": "list",
    "results": [
        {
            "object": "block",
            "id": "4896a9bf-ada2-4bec-8ea2-97bccf07c4ef",
            "created_time": "2021-08-20T21:12:00.000Z",
            "last_edited_time": "2021-08-20T21:12:00.000Z",
            "has_children": false,
            "type": "image",
            "image": {
                "caption": [],
                "type": "file",
                "file": {
                    "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/64f658a7-eb31-4f98-8bea-0aa2956ec475/brocolli.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAEXAMPLE_REDACTED%2F20210820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210820T211229Z&X-Amz-Expires=3600&X-Amz-Signature=e2adc496254ccc741d7ab4f3bab0de7a51b60e31a49d11fcf8702ead2ec9ec18&X-Amz-SignedHeaders=host",
                    "expiry_time": "2021-08-20T22:12:29.066Z"
                }
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

> **Third-party App Embeds**
> Third-party web applications, e.g. Typeform, Figma, etc., are retrieved and added as embed blocks.

### File Page Properties

When retrieving file page properties, you'll now get a link to the file as well as the name.

```json
{
    "object": "page",
    "properties": {
        "Files": {
            "id": "YP~",
            "type": "files",
            "files": [
                {
                    "name": "Brocolli",
                    "type": "file",
                    "file": {
                        "url": "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c32db351-d1ea-40c2-9660-820db28c44ad/brocolli.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAEXAMPLE_REDACTED%2F20210820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210820T211042Z&X-Amz-Expires=3600&X-Amz-Signature=859a24c9b7153860b252fa5955829a97632650dcdc5e91c7a831a48c5efecae4&X-Amz-SignedHeaders=host",
                        "expiry_time": "2021-08-20T22:10:42.022Z"
                    }
                },
                {
                    "name": "Text File",
                    "type": "external",
                    "external": {
                        "url": "https://website.domain/files/doc.txt"
                    }
                }
            ]
        },
    },
    // ... remaining properties
}
```

We also support updating file page properties via [Update page](/reference/patch-page).

# August 20, 2021

## Releasing Notion-Version 2021-08-16

We're releasing Notion-Version `2021-08-16` with the following _backwards incompatible_ changes:

- [Unknown Keys Will Fail Validation](#unknown-keys-will-fail-validation)
- [Rollup Property Types](#changes-to-array-rollup-property-types)
- [Append Block Children](#append-block-children-returns-a-list-of-blocks)
- [URL Safe Property IDs](#property-ids-are-now-url-safe)
- [Empty Properties Are Now Returned](#empty-database-properties-are-now-returned-as-null)

### Unknown Keys Will Fail Validation

Previously, our endpoints used to only validate against the expected keys in both request body parameters as well as query parameters resulting in some ambiguity between incorrect behavior and invalid inputs. Going forward, to improve the developer experience we will be raising validation errors if keys that are not supported by our API are passed in to requests.

> **Migration Tip**
> To safely migrate to `2021-08-16`, we recommend thoroughly testing your API calls against the `2021-08-16` version, to see if you get any validation errors due to this change. If you do, remove any parameters that are rejected due to unknown keys.

### Changes to Array Rollup Property Types

Starting with the Notion-Version header `2021-08-16`, we are introducing a change to the response for rollup properties on a page which are arrays. Number and date rollups are unaffected. Specifically, the `type` of elements within an array rollup has been made consistent with property types across other API endpoints:

```json
{
    "object": "database",
    "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
    "created_time": "2021-07-08T23:50:00.000Z",
    "last_edited_time": "2021-07-08T23:50:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
       "Name": {
            "id": "title",
            "type": "title",
            "title": {}
        },
        "Description": {
            "id": "V}lX",
            "type": "rich_text",
            "rich_text": {}
        },
        "In stock": {
            "id": "V> GQ",
            "type": "checkbox",
            "checkbox": {}
        },
        "Meals": {
          "type": "relation",
          "relation": {
            "database_id": "668d797c-76fa-4934-9b05-ad288df2d136",
            "synced_property_name": "Related to Grocery List (Meals)"
          }
        },
        "Number of meals": {
          "id": "Z\\Eh",
          "type": "rollup",
          "rollup": {
            "rollup_property_name": "Name",
            "relation_property_name": "Meals",
            "function": "count"
          }
        },
        
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

> **Third-party App Embeds**
> Third-party web applications, e.g. Typeform, Figma, etc., are retrieved and added as embed blocks.
```

# Rollup Properties

An example rollup property value for an array of rich text values, using Notion-Version `2021-08-16`:

```json
{
  "properties": {
    "sample text array rollup": {
      "id": "NXTh",
      "type": "rollup",
      "rollup": {
        "type": "array",
        "array": [
          {
            "type": "rich_text",
            "rich_text": [
              {
                "type": "text",
                "text": {
                  "content": "hello world!",
                  "link": null
                },
                "annotations": {
                  "bold": false,
                  "italic": false,
                  "strikethrough": false,
                  "underline": false,
                  "code": false,
                  "color": "default"
                },
                "plain_text": "hello world!",
                "href": null
              }
            ]
          },
          {
            "type": "rich_text",
            "rich_text": [
              {
                "type": "text",
                "text": {
                  "content": "foo bar",
                  "link": null
                },
                "annotations": {
                  "bold": false,
                  "italic": false,
                  "strikethrough": false,
                  "underline": false,
                  "code": false,
                  "color": "default"
                },
                "plain_text": "foo bar",
                "href": null
              }
            ]
          }
        ]
      }
    }, 
  }
}
```

## Append Block Children returns a list of blocks

The [Append Block Children](/reference/patch-block-children) endpoint will now return a list of the newly created [Block object](/reference/block) children.

Previously the endpoint returned the block object of the parent block. Developers can instead use the [Retrieve a block](/reference/retrieve-a-block) endpoint to get the full block object for a specified `block_id`.

This change allows developers to get `block_id`'s and additional information of the new blocks right after they're created. Note: only the first level block children are returned. To get sub-children, use the [Retrieve block children](/reference/get-block-children) endpoint.

### Example response

```json
{
    "object": "list",
    "results": [
       {
            "object": "block",
            "id": "9bc30ad4-9373-46a5-84ab-0a7845ee52e6",
            "created_time": "2021-03-16T16:31:00.000Z",
            "last_edited_time": "2021-03-16T16:32:00.000Z",
            "has_children": false,
            "type": "heading_2",
            "heading_2": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Lacinato kale",
                        "href": null
                    }
                ]
            }
        },
        {
            "object": "block",
            "id": "7face6fd-3ef4-4b38-b1dc-c5044988eec0",
            "created_time": "2021-03-16T16:34:00.000Z",
            "last_edited_time": "2021-03-16T16:36:00.000Z",
            "has_children": false,
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": "Lacinato kale",
                            "link": {
                                "url": "https://en.wikipedia.org/wiki/Lacinato_kale"
                            }
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": "Lacinato kale",
                        "href": "https://en.wikipedia.org/wiki/Lacinato_kale"
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": " is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                            "link": null
                        },
                        "annotations": {
                            "bold": false,
                            "italic": false,
                            "strikethrough": false,
                            "underline": false,
                            "code": false,
                            "color": "default"
                        },
                        "plain_text": " is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                        "href": null
                    }
                ]
            }
        }
    ],
    "next_cursor": null,
    "has_more": false
}
```

## Property IDs are now URL Safe

Endpoints that return property IDs as part of the response body will now return new URL safe encoded property IDs. Any request that uses property IDs (such as [Update a database](/reference/update-a-database) or [Update a page](/reference/patch-page)) should use the new URL safe ID.

This ensures all property IDs can be referenced in the URL of any new endpoints moving forward.

| Before | After |
| --- | --- |
| DoS\\ | DoS%5C |
| title | title |
| vEKn | vEKn |

## Empty database properties are now returned as `null`

Previously, empty properties of date, email, number, and rollup types were omitted from the page response. Now, these empty properties are returned with `null` values.

### Example page response with empty properties

```json
{
    "object": "page",
    "id": "a8b7e96d-22ce-44d8-991f-6c4535af6608",
    "created_time": "2021-05-12T06:16:00.000Z",
    "last_edited_time": "2021-08-12T21:36:00.000Z",
    "cover": null,
    "icon": null,
    "parent": {
        "type": "database_id",
        "database_id": "70ff0393-6b40-4e76-afc4-4a26a9aa1606"
    },
    "archived": false,
    "properties": {
        "MyDate": {
            "id": "GZT~",
            "type": "date",
            "date": null
        },
        "Description": {
            "id": "RPld",
            "type": "rich_text",
            "rich_text": []
        },
        "Food group": {
            "id": "W_iA",
            "type": "select",
            "select": null
        },
        "myRollup": {
            "id": "%5Eu%3EC",
            "type": "rollup",
            "rollup": {
                "type": "array",
                "array": []
            }
        },
        "MyRelation": {
            "id": "_pL%3A",
            "type": "relation",
            "relation": []
        },
        "Price": {
            "id": "dPVb",
            "type": "number",
            "number": null
        },
        "MyMultiSelect": {
            "id": "%7B%40%5Co",
            "type": "multi_select",
            "multi_select": null
        },
    },
    "url": "https://notion.so/a8b7e96d22ce44d8991f6c4535af6608"
}
```

## August 20, 2021

### Formula properties can now be created in databases

When [creating](/reference/create-a-database) or [updating](/reference/update-a-database) databases, you can now add `formula` property types.

#### Example request

```curl
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer "$NOTION_API_KEY"' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-05-13' \
--data '{
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Cost of next trip": {
            "formula": {
                "expression": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
            }
        }
    }
}'
```

#### Example response

```json
{
    "object": "database",
    "id": "c23f0085-a061-41c0-b8a6-cbe14d15a4de",
    "created_time": "2021-08-20T16:08:00.000Z",
    "last_edited_time": "2021-08-20T16:08:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
        "Cost of next trip": {
            "id": "Rbq\\",
            "name": "Cost of next trip",
            "type": "formula",
            "formula": {
                "expression": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
            }
        },
        "In stock": {
            "id": "\\JwC",
            "name": "In stock",
            "type": "checkbox",
            "checkbox": {}
        },
        "Description": {
            "id": "`}HT",
            "name": "Description",
            "type": "rich_text",
            "rich_text": {}
        },
        "Price": {
            "id": "u|<{",
            "name": "Price",
            "type": "number",
            "number": {
                "format": "dollar"
            }
        },
        "Name": {
            "id": "title",
            "name": "Name",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

## August 11, 2021

### OAuth token response now includes workspace ID and owner info

We now return a `workspace_id` field and an `owner` in the [token response](/docs/authorization#exchanging-the-grant-for-an-access-token) at the very end of the OAuth authorization flow.

`workspace_id` is the ID of the workspace where the integration was authorized. As a reminder, this is **not** intended to be unique across tokens; in future iterations of our authorization flow users may be able to authorize your integration multiple times in the same workspace.

`owner` contains information about who can view and share the integration. Because all integrations today can be viewed and shared by all members in the space, `owner` is just an object that looks like `{ "workspace": true }` for now.

To summarize, the OAuth token response now looks like this:

| Field | Type | Description | Not null |
| --- | --- | --- | --- |
| `"access_token"` | `string` | An access token used to authorize requests to the Notion API. | ✅ |
| `"workspace_id"` | `string` | The ID of the workspace where this authorization took place. | ✅ |
| `"workspace_name"` | `string` | A human-readable name which can be used to display this authorization in UI. |  |
| `"owner"` | `object` | Information about the owner of the token. |  |
```

# August 11, 2021

## Update existing databases with PATCH /v1/databases

You can now use the Notion API to [update databases](/reference/update-a-database)! 

Supported updates are:

- renaming the database
- adding and removing properties
- renaming properties
- updating property types.

Note that updating the `name` and `color` select and multi select options is not supported.

### Example request

```bash
curl --location --request PATCH 'https://api.notion.com/v1/databases/668d797c-76fa-4934-9b05-ad288df2d136' \
--header 'Authorization: Bearer "$NOTION_API_KEY"' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-07-27' \
--data '{
    "title": [
        {
            "text": {
                "content": "Today's grocery list"
            }
        }
    ],
    "properties": {
        "+1": null,
        "Photo": {
            "url": {}
        },
        "Store availability": {
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market"
                    },
                    {
                        "name": "Rainbow Grocery"
                    },
                    {
                        "name": "Gus's Community Market"
                    },
                    {
                        "name": "The Good Life Grocery",
                        "color": "orange"
                    }
                ]
            }
        }
    }       
}'
```

### Example response

```json
{
  "object": "database",
  "id": "668d797c-76fa-4934-9b05-ad288df2d136",
  "created_time": "2020-03-17T19:10:00.000Z",
  "last_edited_time": "2021-08-11T17:26:00.000Z",
  "parent": {
    "type": "page_id",
    "page_id": "48f8fee9-cd79-4180-bc2f-ec0398253067"
  },
  "title": [
    {
      "type": "text",
      "text": {
        "content": "Today's grocery list",
        "link": null
      },
      "annotations": {
        "bold": false,
        "italic": false,
        "strikethrough": false,
        "underline": false,
        "code": false,
        "color": "default"
      },
      "plain_text": "Today's grocery list",
      "href": null
    }
  ],
  "properties": {
    "Name": {
      "id": "title",
      "type": "title",
      "title": {}
    },
    "Description": {
      "id": "J@cS",
      "type": "rich_text",
      "rich_text": {}
    },
    "In stock": {
      "id": "{xY`",
      "type": "checkbox",
      "checkbox": {}
    },
    "Food group": {
      "id": "TJmr",
      "type": "select",
      "select": {
        "options": [
          {
            "id": "96eb622f-4b88-4283-919d-ece2fbed3841",
            "name": "🥦Vegetable",
            "color": "green"
          },
          {
            "id": "bb443819-81dc-46fb-882d-ebee6e22c432",
            "name": "🍎Fruit",
            "color": "red"
          },
          {
            "id": "7da9d1b9-8685-472e-9da3-3af57bdb221e",
            "name": "💪Protein",
            "color": "yellow"
          }
        ]
      }
    },
    "Price": {
      "id": "cU^N",
      "type": "number",
      "number": {
        "format": "dollar"
      }
    },
    "Cost of next trip": {
      "id": "p:sC",
      "type": "formula",
      "formula": {
        "value": "if(prop(\"In stock\"), 0, prop(\"Price\"))"
      }
    },
    "Last ordered": {
      "id": "]\\R[",
      "type": "date",
      "date": {}
    },
    "Meals": {
      "type": "relation",
      "relation": {
        "database": "668d797c-76fa-4934-9b05-ad288df2d136",
        "synced_property_name": null
      }
    },
    "Number of meals": {
      "id": "Z\\Eh",
      "type": "rollup",
      "rollup": {
        "rollup_property_name": "Name",
        "relation_property_name": "Meals",
        "rollup_property_id": "title",
        "relation_property_id": "mxp^",
        "function": "count"
      }
    },
    "Store availability": {
      "type": "multi_select",
      "multi_select": {
        "options": [
          [
            {
              "id": "d209b920-212c-4040-9d4a-bdf349dd8b2a",
              "name": "Duc Loi Market",
              "color": "blue"
            },
            {
              "id": "70104074-0f91-467b-9787-00d59e6e1e41",
              "name": "Rainbow Grocery",
              "color": "gray"
            },
            {
              "id": "6c3867c5-d542-4f84-b6e9-a420c43094e7",
              "name": "Gus's Community Market",
              "color": "yellow"
            },
            {
              "id": "a62fbb5f-fed4-44a4-8cac-cba5f518c1a1",
              "name": "Good life grocery",
              "color": "orange"
            }
          ]
        ]
      }
    }
    "Photo": {
      "id": "aTIT",
      "type": "url",
      "url": {}
    }
  }
}
```

## August 3, 2021

### Retrieve and update blocks with GET and PATCH /v1/blocks/:id

You can now retrieve and update block objects with the Notion API! The `PATCH` endpoint currently supports updating `paragraph`, `heading_1`, `heading_2`, `heading_3`, `bulleted_list_item`, `numbered_list_item`, `toggle` and `to_do` blocks.

#### Retrieve a Block

The [Retrieve a Block](/reference/retrieve-a-block) endpoint returns a [Block Object](/reference/block).

```bash
curl 'https://api.notion.com/v1/blocks/9bc30ad4-9373-46a5-84ab-0a7845ee52e6' \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H 'Notion-Version: 2021-05-13'
```

```json
{
  "object": "block",
  "id": "9bc30ad4-9373-46a5-84ab-0a7845ee52e6",
  "created_time": "2021-03-16T16:31:00.000Z",
  "last_edited_time": "2021-03-16T16:32:00.000Z",
  "has_children": false,
  "type": "to_do",
  "to_do": {
    "text": [
      {
        "type": "text",
        "text": {
          "content": "Lacinato kale",
          "link": null
        },
        "annotations": {
          "bold": false,
          "italic": false,
          "strikethrough": false,
          "underline": false,
          "code": false,
          "color": "default"
        },
        "plain_text": "Lacinato kale",
        "href": null
      }
    ],
    "checked": false
  }
}
```

#### Update a Block

The new `PATCH` `/v1/blocks/:id` endpoint supports updating block content (the properties within the block type object) and returns the updated [Block Object](/reference/block), same as the `GET` endpoint shown above. See the [Update a Block](/reference/update-a-block) documentation for more detail.

```bash
curl https://api.notion.com/v1/blocks/9bc30ad4-9373-46a5-84ab-0a7845ee52e6 \
  -H 'Authorization: Bearer "$NOTION_API_KEY"' \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2021-05-13" \
  -X PATCH \
  --data '{
  "to_do": {
    "text": [{
      "text": { "content": "Lacinato kale" }
      }],
    "checked": false
  }
}'
```

## July 26, 2021

### Number properties now support more currency formats

The number property type in databases now supports additional currency options.

The new options are:

- "hong_kong_dollar"
- "new_zealand_dollar"
- "krona"
- "norwegian_krone"
- "mexican_peso"
- "rand"
- "new_taiwan_dollar"
- "danish_krone"
- "zloty"
- "baht"
- "forint"
- "koruna"
- "shekel"
- "chilean_peso"
- "philippine_peso"
- "dirham"
- "colombian_peso"
- "riyal"
- "ringgit"
- "leu"

This impacts the [number configuration of databases](/reference/database#number-configuration).

## July 22, 2021

### OAuth improvements

We've made improvements to the OAuth flow to make it easier to use.

**We now show the page picker on reauthorization.** Just like before, the user who initially authorized an integration can reauthorize by going through OAuth a second time. The page picker step will remember which pages have already been shared with the integration, if any, and let users share or un-share additional pages.

**Users can search for pages to share with an integration.** Previously, users could only select pages at the top level of the Workspace, Shared section, or Private pages section to share with an integration, but we've added a search bar so users can search for and select any page in their workspace.

We also updated the page picker to only show pages for which the user has Full Access permission. Previously, the page picker showed any pages for which the user had at least Can View permission, but would show an error when they tried to give the permission access to those pages.

Other OAuth behavior has not changed: only admins can go through OAuth, and only the original person originally added an integration via OAuth can go through the flow again.

![oauth_improvements.png](https://files.readme.io/15c452e-oauth_improvements.png)

The search bar now lets you search for and select nested pages to share with an integration.

![oauth2.png](https://files.readme.io/63ac8e6-oauth2.png)

Once selected, any nested pages appear in the "Manually Added" section.

## July 21, 2021

### Database property objects now include the property name

[Database property objects](/reference/database#database-property) now include the field `name` with the property name as it appears in Notion.

## July 15, 2021

### Rollup property functions now include show_original

The `function` `show_original` has now been added to [rollup database property objects](/reference/database#rollup-configuration). This fixes a bug where rollup properties were omitted if the calculation was "Show Original".

## July 13, 2021

### Create new databases with POST /v1/databases

You can now use the Notion API to [create a database](/reference/create-a-database) as a subpage of an existing page. Currently supported property types are `paragraph`, `heading_1`, `heading_2`, `heading_3`, `bulleted_list_item`, `numbered_list_item`, `toggle` and `to_do` blocks.

You can create a database as a subpage of an existing page with the following example request:

```bash
curl --location --request POST 'https://api.notion.com/v1/databases/668d797c-76fa-4934-9b05-ad288df2d136' \
--header 'Authorization: Bearer "$NOTION_API_KEY"' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-07-27' \
--data '{
    "title": [
        {
            "text": {
                "content": "Today's grocery list"
            }
        }
    ],
    "properties": {
        "+1": null,
        "Photo": {
            "url": {}
        },
        "Store availability": {
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market"
                    },
                    {
                        "name": "Rainbow Grocery"
                    },
                    {
                        "name": "Gus's Community Market"
                    },
                    {
                        "name": "The Good Life Grocery",
                        "color": "orange"
                    }
                ]
            }
        }
    }       
}'
```

# Notion API

## Introduction

The Notion API provides a set of endpoints for managing and interacting with Notion databases. This guide will help you understand how to use the API effectively.

## Request Method

### GET

To retrieve all databases:

```http
GET https://api.notion.com/v1/databases/
```

### POST

To create a database:

```http
POST https://api.notion.com/v1/databases/
```

### PUT/PATCH

To update a database:

```http
PUT https://api.notion.com/v1/databases/<database_id>
```

### DELETE

To delete a database:

```http
DELETE https://api.notion.com/v1/databases/<database_id>
```

## Response Format

### JSON

#### Example request

```http
curl --location --request POST 'https://api.notion.com/v1/databases/' \
--header 'Authorization: Bearer "$NOTION_API_KEY"' \
--header 'Content-Type: application/json' \
--header 'Notion-Version: 2021-05-13' \
--data '{
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    },
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            }
        }
    ],
    "properties": {
        "Name": {
            "title": {}
        },
        "Description": {
            "rich_text": {}
        },
        "In stock": {
            "checkbox": {}
        },
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {
            "date": {}
        },
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus'\''s Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {
            "people": {}
        },
        "Photo": {
            "files": {}
        }
    }
}'
```

#### Example response

```json
{
    "object": "database",
    "id": "bc1211ca-e3f1-4939-ae34-5260b16f627c",
    "created_time": "2021-07-08T23:50:00.000Z",
    "last_edited_time": "2021-07-08T23:50:00.000Z",
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
                "link": null
            },
            "annotations": {
                "bold": false,
                "italic": false,
                "strikethrough": false,
                "underline": false,
                "code": false,
                "color": "default"
            },
            "plain_text": "Grocery List",
            "href": null
        }
    ],
    "properties": {
        "+1": {
            "id": "PNEQ",
            "type": "people",
            "people": {}
        },
        "In stock": {
            "id": "V&gt;GQ",
            "type": "checkbox",
            "checkbox": {}
        },
        "Price": {
            "id": "V@]u",
            "type": "number",
            "number": {
                "format": "dollar"
            }
        },
        "Description": {
            "id": "V}lX",
            "type": "rich_text",
            "rich_text": {}
        },
        "Last ordered": {
            "id": "eVnV",
            "type": "date",
            "date": {}
        },
        "Store availability": {
            "id": "s}Kq",
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "id": "cb79b393-d1c1-4528-b517-c450859de766",
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "id": "58aae162-75d4-403b-a793-3bc7308e4cd2",
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "id": "22d0f199-babc-44ff-bd80-a9eae3e3fcbf",
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "id": "0d069987-ffb0-4347-bde2-8e4068003dbc",
                        "name": "Gus's Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Photo": {
            "id": "yfiK",
            "type": "files",
            "files": {}
        },
        "Food group": {
            "id": "|JKd",
            "type": "select",
            "select": {
                "options": [
                    {
                        "id": "6d4523fa-88cb-4ffd-9364-1e39d0f4e566",
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "id": "268d7e75-de8f-4c4b-8b9d-de0f97021833",
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "id": "1b234a00-dc97-489c-b987-829264cfdfef",
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Name": {
            "id": "title",
            "type": "title",
            "title": {}
        }
    },
    "parent": {
        "type": "page_id",
        "page_id": "98ad959b-2b6a-4774-80ee-00246fb0ea9b"
    }
}
```

## July 7, 2021

### User mentions can only be of people

To be consistent with the Notion application, only users of type "people" can be mentioned in rich text objects or in people properties of databases. Trying to include users of type "bot" will return a validation error. Existing mentions of bot users is unaffected.

## July 1, 2021

### Page objects now contain url

[Page objects](/reference/page#all-pages) now return the web address of the page in the `url` key.

#### JSON

```json
{
  "object": "page",
  "id": "251d2b5f-268c-4de2-afe9-c71ff92ca95c",
  "created_time": "2020-03-17T19:10:04.968Z",
  "last_edited_time": "2020-03-17T21:49:37.913Z",
  "parent": {
    "type": "database_id",
    "database_id": "48f8fee9-cd79-4180-bc2f-ec0398253067"
  },
  "archived": false,
  "url": "https://www.notion.so/Avocado-251d2b5f268c4de2afe9c71ff92ca95c",
  "properties": {
    "Name": {
      "id": "title",
      "type": "title",
      "title": [
        {
          "type": "text",
          "text": {
            "content": "Avocado",
            "link": null
          },
          "annotations": {
            "bold": false,
            "italic": false,
            "strikethrough": false,
            "underline": false,
            "code": false,
            "color": "default"
          },
          "plain_text": "Avocado",
          "href": null
        }
      ]
    }
  }
}
```

This impacts endpoints that return page object: the [pages](/reference/page) endpoints and [query database](/reference/post-database-query) endpoint.

## June 28, 2021

### Last edited and created time properties are now rounded to the nearest minute

Starting July 1st, the `last_edited_time` and `created_time` properties will be rounded down to the closest minute for `page`, `database`, and `block` objects. Previously, this behavior was inconsistent with some times being rounded and others not.

## June 23, 2021

### Database objects now return parent

Database objects now return a [parent property](/reference/database#page-parent). Databases can have pages or workspaces as parents.

#### JSON

```json
{
  "parent": {
    "type": "page_id",
    "page_id": "b8595b75-abd1-4cad-8dfe-f935a8ef57cb"
  }
}
```

### Other Improvements and Fixes

- Inline database mentions are now included in [rich_text mention](/reference/rich-text#database-mentions) responses.
- When an integration does not have access to a [page or database mention](/reference/rich-text#page-mentions), we will no longer completely omit the mention. The mention will be returned with just the ID but without detailed information (title will appear as "Untitled" and annotations will be default).
- When integrations are added to pages inside collections they can now always update page properties, even when the integration does not have access to the parent database. However, integrations will not be able to add new [select](/reference/page#select-property-values) or [multi-select](/reference/page#multi-select-property-values) properties through the create or update page endpoints without the ability to edit the database parent.

## June 15, 2021

### Select values can now be dynamically created via Create and Update Page endpoints + other updates since public beta launch

You can now dynamically create new options for [Select](/reference/database#select-configuration) or [Multi-Select properties](/reference/database#multi-select-configuration) when using the [Create Page](/reference/post-page) and [Update Page](/reference/patch-page) endpoints. When specifying an option that does not exist in the database schema already, the option will now be created and the database schema updated accordingly.

#### JSON

```json
{
  "properties": {
    "Food group": {
      "multi_select": [{"name": "Vegetable"},{"name": "Fruit"}]
    }
  }
}
```

In the above [property values](/reference/page-property-value) example: Previously, if either "Vegetable" or "Fruit" did not already exist as an option in the database schema, an error would be returned that these are not valid Select options. Now, these options will be created dynamically.

**Bug Fixes**

- The title property of a page can be set, and a page can be archived or un-archived, even when the page does not belong to a database.
- [Retrieving pages](/reference/get-page) that are shared with an integration, but where the page's parent is not shared, no longer erroneously returns a 404.

**Other Changes**

- [Search endpoint](/reference/post-search) now returns untitled pages.
- Applies to [version 2021-05-13](versioning#changes-by-version) and later only: The [Query Database](/reference/post-database-query) endpoint no longer accepts query parameters – these should be sent as body parameters.

## May 19, 2021

### "Notion-Version" header will be required starting June 1, 2021

The Notion API has recommended using an explicit version to every HTTP request, using the `Notion-Version` header. **For integrations created after June 1, 2021 an explicit version on every request will become required**. After July 1, 2021, integrations created before June 1, 2021 will also have the same requirement. Today, the most recent version is `"2021-05-13"`.

#### Is my integration affected? What should I do to update?

The `Notion-Version` header is now required for all requests starting from June 1, 2021. If your integration is created after this date, it will need to reflect this requirement. Integrations created before June 1, 2021 will also need to include the `Notion-Version` header in their requests.

## Additional Information

- For more details about the Notion API, refer to the official documentation at [Notion API Documentation](https://developers.notion.com/reference).
- For specific Notion API endpoints, see the [API Reference](/reference).
- To learn more about Notion, visit the [Notion Website](https://www.notion.so/).

## Disclaimer

This document is provided "as is" and subject to change without prior notice. The Notion API is not guaranteed to be complete or error-free. Users should review and understand the risks associated with using the Notion API before relying upon its functionality.
```

# What should I do to update?

This requirement will not break your existing integration; however, we will start enforcing this requirement for all API requests on July 1st. Starting July 1st, if you don't send the Notion-Version header with your Notion API calls, you will get a [`"missing_version"` error](https://notion.so/reference/errors). Learn more about how the Notion API [handles versioning](https://notion.so/reference/versioning).

If you've been using examples copied from documentation or example code since the public beta, including using the [Notion SDK for JavaScript](https://github.com/makenotion/notion-sdk-js), your existing code should continue to work as expected.

Otherwise, please make one of the two following changes before July 1:

1. Add `Notion-Version: 2021-05-11` in the header when making requests (no other code change is needed).
2. **Recommended**: Add `Notion-Version: 2021-05-13` in the header when making requests. Making this change will move you to our newest version which includes the following breaking change.

## Breaking changes in version `2021-05-13`

The `type` of [property value objects](https://notion.so/reference/page-property-value) for rich text properties has changed from `"text"` to `"rich_text"`.

When [creating pages](https://notion.so/reference/post-page) and [updating page properties](https://notion.so/reference/patch-page), update page property values that are rich text to use the key `rich_text` instead of `text`. Similarly when [retrieving a page](https://notion.so/reference/get-page), rich text properties will be returned with the `type` `"rich_text"` instead of `"text"`.

This change helps distinguish between the property type, and the inner text values of [rich text object](https://notion.so/reference/rich-text), which have the key `text`.

To illustrate this change, here is an example of how the [page object](https://notion.so/reference/page)'s `properties` appear before and after:

### JavaScript

```
// Before (in unversioned requests and responses)
{
  "object": "page",
  "properties": {
    "Description": {
      "type": "text",
      "text": [
        {
          "type": "text",
          "text": { "content": "Hello World" }
        }
      ]
    }
  }
  /* remaining details omitted */
}
```

### JavaScript

```
// After (in requests and responses with version 2021-05-13)
{
  "object": "page",
  "properties": {
    "Description": {
      "type": "rich_text",
      "rich_text": [
        {
          "type": "text",
          "text": { "content": "Hello World" }
        }
      ]
    }
  }
  /* remaining details omitted */
}
```

## May 18, 2021

### Initial users may reauthorize a public integration using OAuth

Public integrations use OAuth to [request authorization from a user](https://notion.so/docs/authorization#prompting-users-to-add-an-integration) before being added to a Notion workspace. Previously, once an integration was added to a workspace, no users were able to reauthorize the same integration in that workspace. This change allows the user who initially added the integration to complete the authorization flow more than once. This improvement helps integrations avoid a potential dead end in user flows.

Integrations do not need to make any updates to take advantage of this new capability. An integration may simply link or redirect a user to the authorization URL, the same as the first authorization. During reauthorization the user will not see the page picker. The access token received at the end of reauthorization will be the same as the initial access token. This capability is available immediately.

Please be aware that other previous limitations still exist. Only users with admin access level in a workspace can add an integration. Integrations can only be added to a workspace by one user.

## May 13, 2021

### Hello world, the Notion API is now in public beta

The Notion API is now available for all developers to explore and build upon. Integrations built on the API are available to all Notion users, on free or paid plans.

In this public beta release, you'll find many of the fundamental parts of Notion: reading and writing to pages, working with users, and the deep and powerful world of Notion databases. The API itself offers foundational features such as authorization, pagination, limits, and more. This is enough to build many interesting integrations we've heard Notion users are excited to use. We're excited to see what you'll build for all of us. [→ Get started](https://notion.so/docs/getting-started)

Our goal is to establish that the Notion API is robust, easy to use, and trustworthy. In public beta, we’ll continue to add new features and making significant changes based on your feedback. Once the most important improvements are included, the API will transition from public beta to general availability. you’ll have everything you need to build integrations teams and businesses can depend on.

A special thanks to the all developers who experimented, explored, and shared their ideas with us - both in the private beta and those following along.

## May 4, 2021

### Public integration type extends access to multiple workspaces using OAuth

The Notion API has added a new integration type: Public OAuth integrations. If you're building a product or service for Notion users outside your own team - public integrations are for developers like you.

In order to create and configure an integration, its type, name, avatar, and other related settings, the [My integrations](https://www.notion.com/my-integrations) page is now available.

Public integrations use OAuth to request permission to access pages and databases in new workspaces. Once the user accepts, the integration can receive a separate access token for resources in the user's workspace.

Existing integrations are now known as internal integrations. We no longer call the bearer token you previously used an API Key. It's now known as an integration token. You can keep your bearer token around - it will continue to work just the same.

Learn how to implement these changes in the [authorization guide](https://notion.so/docs/authorization).

## May 3, 2021

### Search is now available in the API

Using the new [search endpoint](https://notion.so/reference/post-search), you can query all pages and databases users have shared with your integration.

The query you provide filters results by matching against the page title. The results also include matches against subpages of pages users have shared with your integration. This endpoint can be helpful when onboarding a new user and trying to find the page they just shared with your integration.

We recommend transitioning away from using the [list databases endpoint](https://notion.so/reference/get-databases). The search endpoint provides all the same functionality - and more.

---

Updated 3 months ago

* * *

[![Image 1: Ask AI](https://notion.so/images/AI.svg)](https://notion.so/ai)

* * *
```

# Notion API v2021-08-16

## August 16, 2021

### [August 16, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#august-16-2021)

- [Database Date Filters](https://developers.notion.so/blog/notion-api-v2021-08-16#database-date-filters)
- [Dates with times and timezones are now supported on Database Date Filters](https://developers.notion.so/blog/notion-api-v2021-08-16#dates-with-times-and-timezones-are-now-supported-on-database-date-filters)
- [October 15, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-15-2021)
  - [Breadcrumb block types are now supported in the API](https://developers.notion.so/blog/notion-api-v2021-08-16#breadcrumb-block-types-are-now-supported-in-the-api)
- [October 14, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-14-2021)
  - [Table of contents and divider block types are now supported](https://developers.notion.so/blog/notion-api-v2021-08-16#table-of-contents-and-divider-block-types-are-now-supported)
  - [Table of Contents blocks](https://developers.notion.so/blog/notion-api-v2021-08-16#table-of-contents-blocks)
  - [Divider blocks](https://developers.notion.so/blog/notion-api-v2021-08-16#divider-blocks)
- [October 11, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-11-2021)
  - [Users can now add Equation Blocks, Embed, Bookmark, and Media Blocks](https://developers.notion.so/blog/notion-api-v2021-08-16#users-can-now-add-equation-blocks-embed-bookmark-and-media-blocks)
- [October 7, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-7-2021)
  - [Users can now add and update Callout and Quote block types](https://developers.notion.so/blog/notion-api-v2021-08-16#users-can-now-add-and-update-callout-and-quote-block-types)
- [October 5, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-5-2021)
  - [Retrieve page property item](https://developers.notion.so/blog/notion-api-v2021-08-16#retrieve-page-property-item)
- [October 4, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-4-2021)
  - [Retrieve your token's bot user with GET /v1/users/me](https://developers.notion.so/blog/notion-api-v2021-08-16#retrieve-your-tokens-bot-user-with-get-v1usersme)
- [October 1, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#october-1-2021)
  - [New functionality not available to old API versions; code, inline databases, and database page block](https://developers.notion.so/blog/notion-api-v2021-08-16#new-functionality-not-available-to-old-api-versions-code-inline-databases-and-database-page-block)
- [September 21, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#september-21-2021)
  - [Workspace-level tokens for public integrations will be deprecated soon; migrate your OAuth flows](https://developers.notion.so/blog/notion-api-v2021-08-16#workspace-level-tokens-for-public-integrations-will-be-deprecated-soon-migrate-your-oauth-flows)
- [September 17, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#september-17-2021)
  - [Database objects now contain url](https://developers.notion.so/blog/notion-api-v2021-08-16#database-objects-now-contain-url)
- [September 10, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#september-10-2021)
  - [Users can now delete Block objects](https://developers.notion.so/blog/notion-api-v2021-08-16#users-can-now-delete-block-objects)
- [September 9, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#september-9-2021)
  - [Relation and rollup properties can now be created in databases](https://developers.notion.so/blog/notion-api-v2021-08-16#relation-and-rollup-properties-can-now-be-created-in-databases)
- [August 24, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#august-24-2021)
  - [Page icons, cover images, new block types, and improved page file properties](https://developers.notion.so/blog/notion-api-v2021-08-16#page-icons-cover-images-new-block-types-and-improved-page-file-properties)
- [August 20, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#august-20-2021)
  - [Releasing Notion-Version 2021-08-16](https://developers.notion.so/blog/notion-api-v2021-08-16#releasing-notion-version-2021-08-16)
  - [Formula properties can now be created in databases](https://developers.notion.so/blog/notion-api-v2021-08-16#formula-properties-can-now-be-created-in-databases)
- [August 11, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#august-11-2021)
  - [OAuth token response now includes workspace ID and owner info](https://developers.notion.so/blog/notion-api-v2021-08-16#oauth-token-response-now-includes-workspace-id-and-owner-info)
- [August 11, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#august-11-2021-1)
  - [Update existing databases with PATCH /v1/databases](https://developers.notion.so/blog/notion-api-v2021-08-16#update-existing-databases-with-patch-v1databases)
- [August 3, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#august-3-2021)
  - [Retrieve and update blocks with GET and PATCH /v1/blocks/:id](https://developers.notion.so/blog/notion-api-v2021-08-16#retrieve-and-update-blocks-with-get-and-patch-v1blocksid)
- [July 26, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-26-2021)
  - [Number properties now support more currency formats](https://developers.notion.so/blog/notion-api-v2021-08-16#number-properties-now-support-more-currency-formats)
- [July 22, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-22-2021)
  - [OAuth improvements](https://developers.notion.so/blog/notion-api-v2021-08-16#oauth-improvements)
- [July 21, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-21-2021)
  - [Database property objects now include the property name](https://developers.notion.so/blog/notion-api-v2021-08-16#database-property-objects-now-include-the-property-name)
- [July 15, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-15-2021)
  - [Rollup property functions now include show_original](https://developers.notion.so/blog/notion-api-v2021-08-16#rollup-property-functions-now-include-show_original)
- [July 13, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-13-2021)
  - [Create new databases with POST /v1/databases](https://developers.notion.so/blog/notion-api-v2021-08-16#create-new-databases-with-post-v1databases)
- [July 7, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-7-2021)
  - [User mentions can only be of people](https://developers.notion.so/blog/notion-api-v2021-08-16#user-mentions-can-only-be-of-people)
- [July 1, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-1-2021)
  - [Page objects now contain url](https://developers.notion.so/blog/notion-api-v2021-08-16#page-objects-now-contain-url)
- [June 28, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#june-28-2021)
  - [Last edited and created time properties are now rounded to the nearest minute](https://developers.notion.so/blog/notion-api-v2021-08-16#last-edited-and-created-time-properties-are-now-rounded-to-the-nearest-minute)
- [June 23, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#june-23-2021)
  - [Database objects now return parent](https://developers.notion.so/blog/notion-api-v2021-08-16#database-objects-now-return-parent)
  - [Other Improvements and Fixes](https://developers.notion.so/blog/notion-api-v2021-08-16#other-improvements-and-fixes)
- [June 15, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#june-15-2021)
  - [Select values can now be dynamically created via Create and Update Page endpoints + other updates since public beta launch](https://developers.notion.so/blog/notion-api-v2021-08-16#select-values-can-now-be-dynamically-created-via-create-and-update-page-endpoints--other-updates-since-public-beta-launch)
- [May 19, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-19-2021)
  - ["Notion-Version" header will be required starting June 1, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#notion-version-header-will-be-required-starting-june-1-2021)
- [May 18, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-18-2021)
  - [Initial users may reauthorize a public integration using OAuth](https://developers.notion.so/blog/notion-api-v2021-08-16#initial-users-may-reauthorize-a-public-integration-using-oauth)
- [May 13, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-13-2021)
  - [Hello world, the Notion API is now in public beta](https://developers.notion.so/blog/notion-api-v2021-08-16#hello-world-the-notion-api-is-now-in-public-beta)
- [May 4, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-4-2021)
  - [Public integration type extends access to multiple workspaces using OAuth](https://developers.notion.so/blog/notion-api-v2021-08-16#public-integration-type-extends-access-to-multiple-workspaces-using-oauth)
- [May 3, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-3-2021)
  - [Search is now available in the API](https://developers.notion.so/blog/notion-api-v2021-08-16#search-is-now-available-in-the-api)

## July 26, 2021

- [July 26, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-26-2021)
  - [Number properties now support more currency formats](https://developers.notion.so/blog/notion-api-v2021-08-16#number-properties-now-support-more-currency-formats)

## July 22, 2021

- [July 22, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-22-2021)
  - [OAuth improvements](https://developers.notion.so/blog/notion-api-v2021-08-16#oauth-improvements)

## July 21, 2021

- [July 21, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-21-2021)
  - [Database property objects now include the property name](https://developers.notion.so/blog/notion-api-v2021-08-16#database-property-objects-now-include-the-property-name)

## July 15, 2021

- [July 15, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-15-2021)
  - [Rollup property functions now include show\_original](https://developers.notion.so/blog/notion-api-v2021-08-16#rollup-property-functions-now-include-show_original)

## July 13, 2021

- [July 13, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-13-2021)
  - [Create new databases with POST /v1/databases](https://developers.notion.so/blog/notion-api-v2021-08-16#create-new-databases-with-post-v1databases)

## July 7, 2021

- [July 7, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-7-2021)
  - [User mentions can only be of people](https://developers.notion.so/blog/notion-api-v2021-08-16#user-mentions-can-only-be-of-people)

## July 1, 2021

- [July 1, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#july-1-2021)
  - [Page objects now contain url](https://developers.notion.so/blog/notion-api-v2021-08-16#page-objects-now-contain-url)

## June 28, 2021

- [June 28, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#june-28-2021)
  - [Last edited and created time properties are now rounded to the nearest minute](https://developers.notion.so/blog/notion-api-v2021-08-16#last-edited-and-created-time-properties-are-now-rounded-to-the-nearest-minute)

## June 23, 2021

- [June 23, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#june-23-2021)
  - [Database objects now return parent](https://developers.notion.so/blog/notion-api-v2021-08-16#database-objects-now-return-parent)
  - [Other Improvements and Fixes](https://developers.notion.so/blog/notion-api-v2021-08-16#other-improvements-and-fixes)

## June 15, 2021

- [June 15, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#june-15-2021)
  - [Select values can now be dynamically created via Create and Update Page endpoints + other updates since public beta launch](https://developers.notion.so/blog/notion-api-v2021-08-16#select-values-can-now-be-dynamically-created-via-create-and-update-page-endpoints--other-updates-since-public-beta-launch)

## May 19, 2021

- [May 19, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-19-2021)
  - ["Notion-Version" header will be required starting June 1, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#notion-version-header-will-be-required-starting-june-1-2021)

## May 18, 2021

- [May 18, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-18-2021)
  - [Initial users may reauthorize a public integration using OAuth](https://developers.notion.so/blog/notion-api-v2021-08-16#initial-users-may-reauthorize-a-public-integration-using-oauth)

## May 13, 2021

- [May 13, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-13-2021)
  - [Hello world, the Notion API is now in public beta](https://developers.notion.so/blog/notion-api-v2021-08-16#hello-world-the-notion-api-is-now-in-public-beta)

## May 4, 2021

- [May 4, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-4-2021)
  - [Public integration type extends access to multiple workspaces using OAuth](https://developers.notion.so/blog/notion-api-v2021-08-16#public-integration-type-extends-access-to-multiple-workspaces-using-oauth)

## May 3, 2021

- [May 3, 2021](https://developers.notion.so/blog/notion-api-v2021-08-16#may-3-2021)
  - [Search is now available in the API](https://developers.notion.so/blog/notion-api-v2021-08-16#search-is-now-available-in-the-api)
```