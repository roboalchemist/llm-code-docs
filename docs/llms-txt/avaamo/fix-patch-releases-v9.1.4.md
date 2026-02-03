# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/fix-patch-releases-v9.1.4.md

# Fix patch releases (v9.1.4)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.1.4. The following are some of the key fixes included in this release:

1. [Introducing Conversational Intelligence (CI)](#introducing-conversational-intelligence-ci)
2. [Introducing Confluence as a content source for DataSync](#introducing-confluence-as-a-content-source-for-datasync)
3. [Citation links in regression test files](#citation-links-in-regression-test-files)
4. [Citation links in query insights](#citation-links-in-query-insights)

### **Introducing Conversational Intelligence (CI)**

In this release, we introduce `Conversational Intelligence (CI),` a powerful, AI-driven analytics layer that provides deep insights across digital and voice interactions. CI works seamlessly across `classic agents, AI agents, and Agent Copilot,` providing a unified, centralized way to analyze conversations at scale.

**Key points:**

* **AI-driven conversation analysis:** CI analyzes the entire conversatio&#x6E;*,* including transcripts and call metadata, to understand context, intent, and sentiment, rather than relying on rigid conversation trees.
* **Built for modern AI conversations:** Unlike legacy tag-based systems, CI adapts naturally to fluid, non-linear AI agent conversations, making it the most effective way to analyze AI-driven interactions.
* **Centralized analytics platform:** Eliminates the need for custom tagging logic or external dashboards by providing a single analytics layer for all bots and channels.
* **Chat with your data:** Users can interact with insights using a conversational interface to ask questions and explore trends.
* **Rich insights and reporting:** Includes charts, date-based filtering, and automated weekly summary emails.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fo4dqeKIPNTPvZgmBmDGL%2FScreenshot%202026-01-16%20at%202.51.07%E2%80%AFPM.png?alt=media&#x26;token=b4db9103-37e4-4fd8-b771-52f095fc2f80" alt=""><figcaption></figcaption></figure>

Conversational Intelligence replaces legacy tagging approaches with a smarter, scalable, AI-first analytics solution, helping teams gain accurate, actionable insights from every customer interaction.

### **Introducing Confluence as a content source for DataSync**

In this release, DataSync adds support for `Confluence` as a content source, enabling you to ingest Confluence pages and spaces directly into your knowledge base. This integration keeps agent knowledge aligned with the latest documentation, runbooks, and team updates maintained in Confluence.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3x6v1ETqljWz2QyOAuvl%2FScreenshot%202026-01-12%20at%2011.48.53%E2%80%AFAM.png?alt=media&#x26;token=c45411d1-116d-4d73-a93c-0607d54da033" alt=""><figcaption></figcaption></figure>

By automatically syncing Confluence content, agents can deliver more accurate, up-to-date responses without manual uploads, reducing maintenance effort and improving response quality.

Refer [Confluence](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/confluence), for more information.

### **Citation links in regression test files**

In this release, we introduce **citation links in regression result files**, making it easier to trace and verify the sources used during regression testing. Each test result can now include direct citation links, allowing reviewers to quickly validate responses against their original knowledge sources.

This enhancement improves transparency, simplifies result verification, and helps teams confidently assess response accuracy during regression testing.

{% hint style="info" %}
**Note:** To enable citation links in the regression test result file, please reach out to **Avaamo Support**.
{% endhint %}

### **Citation links in query insights**

In this release, citation links are now displayed in query insights across both the `Web channel` and the `Conversation History` pages. This enhancement makes it easier to trace responses back to their original knowledge sources directly from insights, improving transparency and simplifying verification during analysis and troubleshooting.

* This is especially useful for **voice channels**, where responses are not visually inspectable during live interactions.
* Citation links help **bot developers debug and validate responses** by clearly identifying which knowledge sources were used.
* You can use citation visibility during testing and analysis, and disable it later if required for production environments.

Citation link in Web Channel:

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtI01AZQJVjJ6TG6km1mG%2FScreenshot%202026-01-16%20at%2012.07.58%E2%80%AFPM.png?alt=media&#x26;token=339bb303-1161-4f7f-b622-a701e6250d2c" alt="" width="375"><figcaption></figcaption></figure></div>

Citation link in Conversation history:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fb7yAhqY6bKe51WEAHbP6%2FScreenshot%202026-01-16%20at%202.24.56%E2%80%AFPM.png?alt=media&#x26;token=c9324ccf-9fe5-403d-8225-be3662976d82" alt=""><figcaption></figcaption></figure>
