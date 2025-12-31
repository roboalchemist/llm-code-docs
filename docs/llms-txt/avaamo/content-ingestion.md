# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/content-ingestion.md

# Content ingestion

You can create a quick smart conversational knowledge base by importing any PDF document or from any externally accessible URL using Answers skill. However, if you have an enterprise with a huge knowledge base, then uploading the documents or the URL to the Answers skill can be tedious and time-consuming. See [Add Document or URL](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1), for more information on how to ingest content using PDF documents and URLs to the Answers skill knowledge base.

Instead, you can use this new feature to configure webhooks to push content to Avaamo Platform using the API or run document parsing repo on a system to ingest content.&#x20;

### How does this work?

{% hint style="info" %}
**Note**: Contact Avaamo Support to start using this feature and for more information on repo access and API documentation.
{% endhint %}

Based on your requirements, you can ingest content in one of the following ways:

* **Document parsing utility**: Most enterprise content websites have sitemaps with indexes and last modified timestamps. The content ingestion utility crawls through the pages provided in the sitemap to create an Answers skill with the knowledge base. This utility can be configured to be run periodically to keep the Answers skill upto date as and when the content is updated in the indexes. Filters can be added to upload content based on certain criteria - for example, to filter content that is only in the English language.
* **Webhooks**: Answers can be set up as an application that can expose its functions using an API call. Those APIs can be configured with a CMS using Webhooks, such that whenever there is any update to the content, the CMS can call the APIs and update the Answers skill.&#x20;
