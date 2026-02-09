# Source: https://developers.notion.com/guides/link-previews/link-previews.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.notion.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> This guide introduces Link Previews, how they work, and what you need to build them.

export const integrationsDashboardUrl = "https://www.notion.so/profile/integrations";

A Link Preview is a real-time excerpt of authenticated content that unfurls in Notion when an authenticated user shares an enabled link. Instead of logging in to multiple tools at a time, collaborators can use Link Previews to centralize their work in Notion.

<Frame caption="An example Link Preview for a GitHub workflow">
  <video controls className="w-full aspect-video rounded-xl" src="https://mintcdn.com/notion-demo/gQdVRy6l7aPTpzMm/images/docs/link_unfurling.mp4?fit=max&auto=format&n=gQdVRy6l7aPTpzMm&q=85&s=fb32ddf0c1c56950202668cb06b25b45" data-path="images/docs/link_unfurling.mp4" />
</Frame>

With the Link Previews API, you can set up integrations that share a Link Preview for your product. For example:

* **Trello** created a Link Preview that unfurls information about a linked task.
* **Figma** built a Link Preview that shares a linked board’s image preview and corresponding metadata.
* **Amplitude** created a Link Preview that shares a linked graph in an iFrame along with an interface to modify the graph.
* **Slack** built a Link Preview that unfurls a linked message’s content and author.

If your customers use Notion, then building a Link Preview can help them to integrate your product into their existing workflows.

## How Link Previews work

A user shares a Link Preview enabled URL. Notion detects enabled URLs based on the settings that you provide when you create the integration. If it’s the first time that a user has shared an enabled URL, then Notion kicks off an auth flow to authenticate with your service. After the user authenticates, Notion and your service exchange tokens that enable your integration to share a Link Preview in the user’s workspace.

<Frame caption="A diagram of the Link Preview flow">
  <img src="https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=ca57bf5daad1fda57bb7f369a94f7109" data-og-width="1800" width="1800" data-og-height="1200" height="1200" data-path="images/docs/e121163-lp_overview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?w=280&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=e52a1a9daf7d8810cba00fefea82a9c1 280w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?w=560&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=00a64cc58bc52506acf17c20fd0db4c9 560w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?w=840&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=5f94bd473180f30edd9110480acf1f97 840w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?w=1100&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=9f83723b64aa490eb0f526e0c0bcb92b 1100w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?w=1650&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=9ff3ca81b514ca3232740649af9fc4c4 1650w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/e121163-lp_overview.png?w=2500&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=fa37c69b590afdcb471f43d6fd236352 2500w" />
</Frame>

Your integration also detects any changes to the data embedded in the Link Preview, and alerts Notion when the Link Preview needs to be updated.

Notion alerts your integration when a Link Preview is deleted, so that your integration can stop listening for updates.

## Build your own Link Preview integration

Notion offers the tools for developers to build their own Link Preview integration to unfurl links for a specified domain.

<Frame caption="Anatomy of an unfurled link preview">
  <img src="https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=f620c2ae86311158ff4d015d6c281d35" data-og-width="1378" width="1378" data-og-height="818" height="818" data-path="images/docs/57f4b0d-Untitled_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?w=280&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=af4ebc31449461f62ae818b60110f47a 280w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?w=560&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=28066cbd01b5fc5d5d1fdfa9ac316c19 560w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?w=840&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=54ebdf9710df808b081661335ba4969f 840w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?w=1100&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=97f5bcf61130a89fbf074fc65b476e85 1100w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?w=1650&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=5f6c8081195b352daec2f02e391dbec9 1650w, https://mintcdn.com/notion-demo/LHm9qfrJYJOPRxs6/images/docs/57f4b0d-Untitled_1.png?w=2500&fit=max&auto=format&n=LHm9qfrJYJOPRxs6&q=85&s=8ebbf0df3e9aabec5e6ed794a9127c9c 2500w" />
</Frame>

Using the <a href={integrationsDashboardUrl}>Integration dashboard</a> and Notion’s public API, developers can customize each section of a Link Preview to show relevant data to users.

### Link Previews vs. Embed blocks

If you have used [Embed blocks](/reference/block#embed) in Notion’s UI before, you may be wondering how Link Previews differ from them. Embeds allow Notion users to embed online content — such as a webpage, PDF, and more — directly in a Notion page. This allows users to preview the content without leaving Notion.

Link Previews are similar but specifically allow developers to determine and customize the content displayed when an authenticated link is unfurled. Rather than embedding the full content of a webpage or file being shared, Link Previews pull data from a linked page and display it in an unfurled format that has been specified by the developer.

Since Link preview integrations require [OAuth 2.0](https://www.oauth.com/) authentication, unfurled link content will update as the data being shared updates. For example, if a GitHub pull request is shared as a Link Preview, the data displayed in the preview will update as the pull request updates (e.g. when it is merged).

<Info>
  To learn more about Embed blocks, read our [reference docs](/reference/block#embed) and [Help Centre guide](https://www.notion.so/help/embed-and-connect-other-apps).
</Info>

## Requirements for building a Link Preview integration

<Warning>
  To build a Link Preview integration, developers must first apply for access to the feature through the [Notion Link Preview API request form](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).

  Additionally, all Link Preview integrations published for distribution require a review from Notion's platform and security teams.
</Warning>

In order to build Link Preview integrations, you need to meet the following requirements:

* Support OAuth 2.0 in your application, or be ready to implement it.
* Own the domain that you’d like to set up with Link Preview enabled URLs.

If you meet these requirements and you’d like to start building with the Link Previews API, then please [request access](https://notionup.typeform.com/to/BXheLK4Z?typeform-source=developers.notion.com).

## Next steps

To learn how to build your own Link Preview integration, read:

* [Build your own Link Preview integration](/guides/link-previews/build-a-link-preview-integration) guide

## Link Preview integration resources

To learn more about Link Previews, see the following resources:

* [Build your own Link Preview integration](/guides/link-previews/build-a-link-preview-integration) guide
* [API reference docs for the Link Preview unfurl attribute object](/reference/unfurl-attribute-object)
* [Help Centre](https://www.notion.so/help/guides/notion-api-link-previews-feature) guide
