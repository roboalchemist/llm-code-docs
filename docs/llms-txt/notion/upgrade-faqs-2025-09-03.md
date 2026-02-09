# Source: https://developers.notion.com/guides/get-started/upgrade-faqs-2025-09-03.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQs: Version 2025-09-03

> Commonly asked questions about data sources and how to migrate to Notion's API version 2025-09-03

<AccordionGroup>
  <Accordion title="What is a datasource and how does it relate to a database?">
    In September 2025, Notion is launching several features to improve what you can do with databases. This includes support for multiple **data sources** under a single **database**, each of which can have a different set of properties (schemas). The **database** becomes a *container* for one or more **data sources**.

    <Frame caption="Diagram of the new Notion API data model. A database is a parent of one or more data sources, each of which parents zero or more pages. Previously, databases could only have one data source, so the concepts were combined in the API until 2025">
      <img src="https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=8d4f9e6731559c09bf0f0aadec57d404" data-og-width="3840" width="3840" data-og-height="2765" height="2765" data-path="images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?w=280&fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=d3e13fd08c6883c7f45f303199ac2033 280w, https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?w=560&fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=fcd2beb45162561d1c127793d7c34445 560w, https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?w=840&fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=5fe2512e4398c4a24266ffdb1f0365ab 840w, https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?w=1100&fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=8ea3c62aba5144a110b827538d94ee65 1100w, https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?w=1650&fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=715ea4b01fd3b9ea8f2e8ee9f10cae80 1650w, https://mintcdn.com/notion-demo/kjidwljTiCgFD8sF/images/docs/acf8104f9bb0b15e37e8f03cef3699eb19cf43c608fa4769ea04fc00468bb069-image.png?w=2500&fit=max&auto=format&n=kjidwljTiCgFD8sF&q=85&s=2825854ce63b215add9aaebd1507fb06 2500w" />
    </Frame>

    To learn more about data sources in the Notion app and related features, visit our [help center page](https://www.notion.com/help/data-sources-and-linked-databases).
  </Accordion>

  <Accordion title="Is a datasource a new concept?">
    Prior to this release, **databases** were limited to one **data source**, so the **data source ID** was hidden. Now that multiple data sources are supported, we need a way to identify the specific data source for a request. Starting from the `2025-09-03` API version, Notion is providing a new set of APIs under `/v1/data_sources` for managing each **data source**. Most of your integration's existing database operations should move to this set of APIs.

    The `/v1/databases` family of endpoints now refers to the **database** (container) as of `2025-09-03`. To discover the data sources available for a database, the database object includes a `data_sources` array, each having an `id` and a `name`. The data source ID can then by used with the `/v1/data_sources` APIs.
  </Accordion>

  <Accordion title="How does this impact database URLs?">
    The concept of a database ID in the Notion app stays the same, and continues to be shown in the URL for a database followed by the ID of the specific view you're looking at. For example, in a link like `https://notion.so/workspace/248104cd477e80fdb757e945d38000bd?v=148104cd477e80bb928f000ce197ddf2`:

    * `248104cd-477e-80fd-b757-e945d38000bd` is the **database** (container) ID.
    * `148104cd477e80bb928f000ce197ddf2` is the database view (managing views is not currently supported in the API).

    <Note>
      **Note**:

      The ID of the specific **data source** you're looking at isn't embedded in the URL, but will be listed in a separate dropdown menu.
    </Note>
  </Accordion>

  <Accordion title="Can I see an example of how parent & child relationships work?">
    Here's a diagram of a scenario where a workspace has a top-level page that has a database with two data sources:

    <Frame caption="Diagram showing a page in a workspace with a database child. The database has two data sources, each of which have two rows (child pages).">
      <img src="https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=84dc88593a360a864b658849c8a4cd6c" data-og-width="464" width="464" data-og-height="537" height="537" data-path="images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?w=280&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=14e52d5e197d8bf8992345abfed30a24 280w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?w=560&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=7caf7738d58965a44ddc6d683044ee98 560w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?w=840&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=5756e99f75d47c899c2fb10242bf7738 840w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?w=1100&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=c51b611c9c4210ea866a187da6db4264 1100w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?w=1650&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=3cb6a55fd9a6ad274abee75edbcfa4de 1650w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/16252219aa29c1b45f8db4a8a0ecffb7455954075ce15ffd1407388de62a3d1f-image.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=e59f752c4bf847e3b1d71edd79ad75d3 2500w" />
    </Frame>

    Going from top to bottom, here's a simplified run-through of how the API objects connect to one another:

    * **Parent Page**:

      * `parent` is `{"type": "workspace", "workspace": "true"}`
      * No changes to how the page's Block children work.

    * **Database**:

      * `parent` is `{"type": "page_id", "page_id": "<id of Parent Page>"}`
      * `data_sources` is `[{"id": "...", "name": "Data Source"}, {"id": "...", "name": "Data Source"}]`

    * **Data Source**:

      * `parent` is `{"type": "database_id", "database_id": "<id of Database>"}`
      * `database_parent` is `{"type": "page_id", "page_id": "<id of Parent Page>"}`

    * **Page**:

      * `parent` is `{"type": "data_source_id", "data_source_id": "<id of Data Source>"}`
      * No changes to how the page's Block children work.
  </Accordion>

  <Accordion title="How do permissions work for data sources?">
    User and bot permissions are managed at the **database** level, not per data source. This means that the level of access a Notion user or integration has (or doesn't have) is the same across all data sources in a database.
  </Accordion>

  <Accordion title="How do these changes work with wikis?">
    Unlike other databases, wikis won't support multiple data sources as part of the September 2025 launch. For this reason, and due to limited support in Notion's API, we recommend using alternative ways to structure your knowledge in Notion that don't involve wikis.

    However, for completeness, here's a diagram of how parent/child relationships work in an example wiki scenario:

    <Frame caption="Diagram showing single-source databases nested under one another as part of a wiki structure.">
      <img src="https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=be6ff0852c38631907b4dff7a5ffb02c" data-og-width="359" width="359" data-og-height="504" height="504" data-path="images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?w=280&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=b69031317d694776c660c9b0872a9589 280w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?w=560&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=c218d7c7d491b5a042b81a97f80c3aad 560w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?w=840&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=66f3a71c9ec9900c75dfffcd37a9d69b 840w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?w=1100&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=96d5279147e8b20879b188ed15b49cc3 1100w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?w=1650&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=ad7354f4c218691ee230172c55f3423f 1650w, https://mintcdn.com/notion-demo/9OFhQspLr8njnajd/images/docs/41afb783e9b0060cf2bba81da964c08359100231e43f54fa3a38e98d69c4ce4f-image.png?w=2500&fit=max&auto=format&n=9OFhQspLr8njnajd&q=85&s=eaa6a3305fb9c4a239d6183366fc71d9 2500w" />
    </Frame>
  </Accordion>

  <Accordion title="Which APIs are & aren't affected?">
    * Each family of APIs is summarized in the table below.
    * Ones that are affected are marked in **bold** in the first column, and the `2025-09-03` changes are outlined in the second column.
    * Ones that aren't affected are listed as "None" (some of which have explanatory comments as to why they aren't affected.)

    | Endpoints        | Changes                                                                                                                                                                                                                                                                                                           |
    | :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Authentication   | None                                                                                                                                                                                                                                                                                                              |
    | Blocks           | None                                                                                                                                                                                                                                                                                                              |
    | **Pages**        | `parent` is a `data_source_id` instead of a `database_id`                                                                                                                                                                                                                                                         |
    | **Databases**    | Modified to act on the entire database (container) instead of its data sources via Create, Retrieve, or Update; see migration guide details above <br /> <br />Creating a database and its initial data source works the same way, but `properties` must be nested under `initial_data_source` as of `2025-09-03` |
    | **Data Sources** | New set of APIs for operating on individual data sources under a database via Create, Update, Query, or Retrieve                                                                                                                                                                                                  |
    | Comments         | None (comments can only have blocks or pages as parents, not databases or data sources, so they aren't affected)                                                                                                                                                                                                  |
    | File Uploads     | None                                                                                                                                                                                                                                                                                                              |
    | **Search**       | Filter value parameter refers to `"data_source"` instead of `"database"`; response results include each `"data_source"` object instead of `"database"` objects                                                                                                                                                    |
    | Users            | None                                                                                                                                                                                                                                                                                                              |
  </Accordion>

  <Accordion title="When can I start using the `2025-09-03` version?">
    The API version is already available to use for Notion API requests as of late August. We recommend starting the upgrade process detailed above at your earliest convenience if your integration is affected by the changes.

    If your workspace is connected to any public integrations (rather than an internal bot owned by you or your business), they may not have upgraded yet. If you rely on important workflows or automations, contact the third-party for any questions or issues regarding their timeline & support for databases with multiple sources.

    ### Notes on API versions

    As a reminder, [API versioning](/reference/versioning) is determined by providing a mandatory `Notion-Version` HTTP header with each API request. If you're using the [TypeScript SDK](https://github.com/makenotion/notion-sdk-js), you might be configuring the version in one place where the Notion client is instantiated, or passing it explicitly for each request. You can follow the rest of this guide incrementally, upgrading each use of the API at a time at your convenience.

    We're also extending the concept of API versioning to [integration webhooks](/reference/webhooks) to allow Notion to introduce backwards-incompatible changes without affecting your endpoint until you upgrade the API version in the integration settings. Ensure your webhook URL can handle events of both the old and new shape for a short period of time before making the upgrade.
  </Accordion>

  <Accordion title="How long will the `2022-06-28` version continue to work?">
    We don't currently have any process for halting support of old Notion API versions. If we introduce a "minimum versioning" program in the future, we'll communicate this with all affected users with ample notice period (e.g. 6 months) and start with versions that came before `2022-06-28`.

    However, even though API integrations continue to work, we recommend upgrading to `2025-09-03` as soon as possible. That way, your system is ready for in-app creation of data sources, gains new functionality when working with databases, and you can help Notion's support teams better handle any questions or requests you have by making sure you're up-to-date.

    ### Behavior for existing integrations

    Integrations using the `2022-06-28` API version (or older) will **continue to work with existing databases in Notion that have a single data source**. Webhooks will also generally continue to be delivered without any changes to the format.

    However, if any Notion users create a second data source for a database in a workspace that's connected to your integration (starting on September 3, 2025), your database IDs are no longer precise enough for Notion to process the request.

    Until you follow this guide to upgrade, Notion responds to requests involving a database ID with multiple data sources with validation errors that look like:

    <CodeGroup>
      ```json JSON Response theme={null}
      {
        "code": "validation_error",
        "status": 400,
        "message": "Databases with multiple data sources are not supported in this API version.",
        "object": "error",
        "additional_data": {
          "error_type": "multiple_data_sources_for_database",
          "database_id": "27a5d30a-1728-4a1e-a788-71341f22fb97",
          "child_data_source_ids": [
            "164b19c5-58e5-4a47-a3a9-c905d9519c65",
            "25c104cd-477e-8047-836b-000b4aa4bc94"
          ],
          "minimum_api_version": "2025-09-03"
        }
      }
      ```
    </CodeGroup>

    The `additional_data` in the response can help you identify the relevant data source IDs to use instead, as you upgrade your integration.
  </Accordion>

  <Accordion title="Why is this the first version upgrade since 2022?">
    We aim to improve functionality in our API through backwards-compatible features first and foremost. We've shipped several changes since 2022, including the [File Upload](/reference/file-upload) API, but generally aim to avoid having large sets of users have to go through a detailed upgrade progress when possible.

    With these new changes to the Notion app, we want our integration partners, developer community, ambassadors, champions, and everyone else making great tools to unlock the power of multiple-source database containers. This involves rethinking what a "database ID" in the API can do and repurposing API endpoints, necessitating the `2025-09-03` version release.
  </Accordion>
</AccordionGroup>

## What’s Next

Upgrade your integrations, learn more about integration webhooks, and stay tuned for any future updates to Notion's API:

<CardGroup>
  <Card title="Changes by version" icon="angles-right" href="/reference/changes-by-version" horizontal color="#0076d7" />

  <Card title="Webhooks" icon="angles-right" href="/reference/webhooks" horizontal color="#0076d7" />

  <Card title="Typed API SDK for JS" icon="angles-right" href="/api-sdk-for-typescript-and-javascript" horizontal color="#0076d7" />

  <Card title="Upgrading to Version 2025-09-03" icon="angles-right" href="/guides/get-started/upgrade-guide-2025-09-03" horizontal color="#0076d7" />
</CardGroup>
