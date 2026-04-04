# Source: https://developers.webflow.com/data/docs/working-with-the-cms/publishing.mdx

***

title: Publishing with the CMS API
description: Learn how to publish content with the CMS API
hidden: false
subtitle: Learn how to publish content with the CMS API
-------------------------------------------------------

The CMS API uses a staging system that separates draft from published content. This workflow gives you control over what goes live and when, ensuring content quality before publication.

All CMS content exists in one of two states:

<CardGroup cols={2}>
  <Card title="Staged">
    Draft content that can be previewed but isn't visible on the live site. Use this state to prepare and review changes.
  </Card>

  <Card title="Live">
    Content that's published and visible on your site. A live item can have a staged version for updates that don't affect the original.
  </Card>
</CardGroup>

Each CMS Item has `isDraft` and `lastPublished` properties that indicate its current state. The combination of these properties determines an item's status, which is reflected in the Webflow UI.

| Status                                 | Description                                                                                           | `lastPublished` | `isDraft` |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------- | --------- |
| <StatusBadge status="published" />     | Content is live and visible on your website.                                                          | `exists`        | `false`   |
| <StatusBadge status="draft-changes" /> | Live content with unpublished draft changes.                                                          | `exists`        | `true`    |
| <StatusBadge status="draft" />         | Content is in a draft state and has never been published.                                             | `null`          | `true`    |
| <StatusBadge status="queued" />        | Content will be published on the next site-wide publish.                                              | `null`          | `false`   |
| <StatusBadge status="scheduled" />     | Content is scheduled for future publication. This can not be controlled by the CMS API.               | N/A             | N/A       |
| <StatusBadge status="archived" />      | Content has been archived and removed from the live site. Use the `isArchived` flag to archive items. | N/A             | N/A       |

This mapping helps you understand how API operations affect the content status displayed in the Webflow interface.

## Publishing workflows

The CMS API provides flexible publishing options to fit your workflow. Use the accordions below to learn more about each publishing method and see which endpoints to use.

<AccordionGroup>
  <Accordion title="Individual item publishing">
    Publish, unpublish, or stage a single item without affecting other content. This gives you granular control for targeted updates, such as publishing a single blog post or making a small correction to an existing page.

    **Associated endpoints:**

    <ApiEndpoint method="POST" endpoint="/collections/:collection_id/items/publish" link="/data/reference/cms/collection-items/staged-items/publish-item" />

    <ApiEndpoint method="DELETE" endpoint="/collections/:collection_id/items/live" link="/data/reference/cms/collection-items/live-items/delete-items-live" />

    ```ts title={"publishSingleItem.ts"}
    import { WebflowClient } from "webflow-api";

    const webflow = new WebflowClient({
      accessToken: "YOUR_ACCESS_TOKEN",
    });

    const item = await webflow.collections.items.publishItem("COLLECTION_ID", {
      itemIds: ["ITEM_ID"],
    });

    console.log(item);
    ```
  </Accordion>

  <Accordion title="Site-wide publishing">
    Publish all staged content across your entire site in a single operation. This is ideal for coordinated releases, such as a new marketing campaign, a product launch, or a site redesign where multiple content changes need to go live simultaneously.

    <ApiEndpoint method="POST" endpoint="/sites/:site_id/publish" />

    ```ts title={"publishSite.ts"}
    import { WebflowClient } from "webflow-api";

    const webflow = new WebflowClient({
      accessToken: "YOUR_ACCESS_TOKEN",
    });

    const site = await webflow.sites.publish("SITE_ID", {
      customDomains: ["CUSTOM_DOMAIN_ID_1", "CUSTOM_DOMAIN_ID_2"],
      publishToWebflowSubdomain: true,
    });

    console.log(site);
    ```
  </Accordion>

  <Accordion title="Draft changes on a live item">
    When a live item’s `isDraft` property is set to `true`, it remains published on your site. This allows you to safely update the item in a draft state without changing what's visible to your site visitors. The changes will only go live when the item's `isDraft` property is set to `false` and the item is published again.

    <ApiEndpoint method="PATCH" endpoint="/collections/:collection_id/items" />

    ```ts title={"updateLiveItem.ts"}
    import { WebflowClient } from "webflow-api";

    const webflow = new WebflowClient({
      accessToken: "YOUR_ACCESS_TOKEN",
    });

    const item = await webflow.collections.items.updateItem("COLLECTION_ID", "ITEM_ID", {
      isDraft: true, // Set to true to update the live item in a draft state
      fieldData: {
        name: "Heart of Gold",
        slug: "heart-of-gold",
        description: "The Heart of Gold is a ship that is used to travel through space using the infinite improbability drive.",
        pilots: ["Trisha McMillan", "Zaphod Beeblebrox"],
      },
    });

    console.log(item);
    ```
  </Accordion>

  <Accordion title="Update a live item directly">
    To update an item and publish the changes to your live site in a single action, use the `updateItemLive` endpoint. This is useful for making quick corrections or immediate updates without a review stage.

    <ApiEndpoint method="PATCH" endpoint="/collections/:collection_id/items/live" />

    ```ts title={"updateLiveItemDirectly.ts"}
    import { WebflowClient } from "webflow-api";

    const webflow = new WebflowClient({
      accessToken: "YOUR_ACCESS_TOKEN",
    });

    const item = await webflow.collections.items.updateItemLive(
      "COLLECTION_ID",
      "ITEM_ID",
      {
        fieldData: {
          name: "Heart of Gold",
          slug: "heart-of-gold",
          description: "The Heart of Gold is a ship that is used to travel through space using the infinite improbability drive.",
          pilots: ["Trisha McMillan", "Zaphod Beeblebrox"],
        }
      }
    );

    console.log(item);

    ```
  </Accordion>

  <Accordion title="Unpublish an item">
    To remove an item from the live site, you must explicitly call the `unpublishItem` endpoint. This action doesn't delete the item from the CMS; it unpublishes it and sets its `isDraft` property to `true`, allowing you to continue editing it.

    <ApiEndpoint method="DELETE" endpoint="/collections/:collection_id/items/live" />

    ```ts title={"unpublishItem.ts"}
    import { WebflowClient } from "webflow-api";

    const webflow = new WebflowClient({
      accessToken: "YOUR_ACCESS_TOKEN",
    });

    // Note: This does not delete the item, it just unpublishes it.
    const item = await webflow.collections.items.deleteItemLive(
      "COLLECTION_ID",
      "ITEM_ID"
    );

    console.log(item);

    ```
  </Accordion>

  <Accordion title="Archiving content">
    Archiving unpublishes items from your live site at the next full-site publish, but keeps the items accessible in the CMS. To archive an item, set the `isArchived` property on the item to `true`.

    <ApiEndpoint method="PATCH" endpoint="/collections/:collection_id/items" />

    <ApiEndpoint method="PATCH" endpoint="/collections/:collection_id/items/live" />

    ```ts title={"archiveItem.ts"}
    import { WebflowClient } from "webflow-api";

    const webflow = new WebflowClient({
      accessToken: "YOUR_ACCESS_TOKEN",
    });

    const item = await webflow.collections.items.updateItem("COLLECTION_ID", "ITEM_ID", {
      isArchived: true, // Set to true to archive the item
      fieldData: {
        name: "Heart of Gold",
        slug: "heart-of-gold",
        description: "The Heart of Gold is a ship that is used to travel through space using the infinite improbability drive.",
        pilots: ["Trisha McMillan", "Zaphod Beeblebrox"],
      },
    });

    console.log(item);
    ```
  </Accordion>
</AccordionGroup>

## Next steps

Now that you understand the publishing workflows, here are a few topics you might want to explore next:

<CardGroup cols={2}>
  <Card title="Content Delivery" href="/data/docs/working-with-the-cms/content-delivery">
    Deliver your published content to your live application.
  </Card>

  <Card title="Webhooks" href="/data/reference/webhooks/events/collection-item-created">
    Trigger automated workflows when content is published or unpublished.
  </Card>
</CardGroup>
