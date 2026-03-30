# REST API: `status`

The [REST API](/cms/api/rest) offers the ability to filter results based on their status, draft or published.

:::prerequisites
The [Draft & Publish](/cms/features/draft-and-publish) feature should be enabled.
:::

Queries can accept a `status` parameter to fetch documents based on their status:

- `published`: returns only the published version of documents (default)
- `draft`: returns only the draft version of documents

:::tip
In the response data, the `publishedAt` field is `null` for drafts.
:::

:::note
Since published versions are returned by default, passing no status parameter is equivalent to passing `status=published`.
:::

<br /><br />

<details>
<summary>JavaScript query (built with the qs library):</summary>

</ApiCall>