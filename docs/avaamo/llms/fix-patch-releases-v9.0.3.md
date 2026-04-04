# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/fix-patch-releases-v9.0.3.md

# Fix patch releases (v9.0.3)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.0.3. The following are some of the key fixes included in this release:

1. [Support for Microsoft Teams single-tenant bots ](#support-for-microsoft-teams-single-tenant-bots)
2. [Content ingestion improvements](#content-ingestion-improvements)

### **Support for Microsoft Teams single-tenant bots**<img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLomqnXOQWCApNMXraXIY%2FDeveloper.png?alt=media&#x26;token=cc2a370f-d7e4-43ee-93b2-3106fdddaa46" alt="" data-size="line">

With Microsoft deprecating multi-tenant bot creation, the Avaamo platform now supports single-tenant bots for Microsoft Teams.

* All newly created bots default to a single-tenant configuration.
* Existing channels with a multi-tenant configuration continue to function, but multi-tenant Azure bot credentials cannot be used in newly created channels, as Avaamo now supports single-tenant bots by default.
* To migrate, follow the Microsoft Teams documentation or create a new single-tenant Azure app and map it to the Avaamo MS Teams channel.

### Content ingestion improvements<img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLomqnXOQWCApNMXraXIY%2FDeveloper.png?alt=media&#x26;token=cc2a370f-d7e4-43ee-93b2-3106fdddaa46" alt="" data-size="line">

Introducing a new parsing mechanism that enhances content extraction across multiple file types via API. This improvement applies to newly uploaded content or files via API.

* **Markdown parsing for HTML content:** Automatically extracts additional formatting elements, such as italics and list tags, and converts them into markdown. This enhancement is applied by default from this release onward, requiring no additional parameters when you upload using the [Upload document ](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis#upload-document-html-url-to-llamb)API.
* **Section header and hierarchy detection in PDF files:** Allows extraction of section headers, section hierarchies, and tables for better content organization. To use this, pass the parameter `"parsing_lib": "markdown"` in the [Upload file](https://docs.avaamo.com/user-guide/llamb/llamb-rest-apis/content-ingestion-apis#upload-different-types-of-files-pdf-docx-pptx-xlsx-csv-html-to-llamb) API.

### **MS Teams – Control over Markdown format**<img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLomqnXOQWCApNMXraXIY%2FDeveloper.png?alt=media&#x26;token=cc2a370f-d7e4-43ee-93b2-3106fdddaa46" alt="" data-size="line">

An option is now available to enable or disable Markdown formatting for LLaMB responses in the Microsoft Teams channel. You can configure this setting on the MS Teams configuration page to control whether responses are rendered in Markdown format.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FynixR35G4NEeX9mdS7ku%2FScreenshot%202025-09-10%20at%2010.21.48%E2%80%AFAM.png?alt=media&#x26;token=4d860e25-f4f6-4ebb-8493-61064b8f6c2a" alt=""><figcaption></figcaption></figure>

Refer [Microsoft Teams (MS Teams)](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams#deploy-your-agent-to-microsoft-teams-channel), for more information.
