# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/fix-patch-releases-v9.0.4.md

# Fix patch releases (v9.0.4)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.0.4. The following are some of the key fixes included in this release:

1. [Introducing the DataSync 2.0 (Beta)](#id-1.-introducing-the-datasync-2.0-beta)
2. [Soft unhandled – multilingual support](#id-2.-soft-unhandled-multilingual-support)

### 1. Introducing the DataSync 2.0 (Beta)<img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLomqnXOQWCApNMXraXIY%2FDeveloper.png?alt=media&#x26;token=cc2a370f-d7e4-43ee-93b2-3106fdddaa46" alt="" data-size="line">

> This feature is currently in beta and intended for testing; feedback is appreciated.

The **DataSync** is designed to empower AI agents by seamlessly integrating and processing information from various content sources, including documentation, product guides, FAQs, and enterprise systems. With this capability, the agent can deliver accurate, context-aware responses grounded in the most up-to-date information.

Navigate to `Configuration>DataSync`  to access.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmVYZFUcHusbSFBvQ2p0Z%2FScreenshot%202025-09-26%20at%2010.37.06%E2%80%AFAM.png?alt=media&#x26;token=9c63b839-6112-4199-86f6-4d3106650c7f" alt=""><figcaption></figcaption></figure>

#### Key highlights

* **Content integration**: Ingest structured and unstructured information from documents, web pages, repositories, and other sources.
* **Real-time status synchronization**: Connect with systems of record such as `SharePoint`, `ServiceNow`, `web platforms`, and `files` to ensure content is always current.
* **Flexible synchronization modes**: Choose between `AutoSync` for continuous updates or `Manual` synchronization, with execution history tracking for visibility and control. This is not applicable to content sources like `Files`.
* **Scalability:** Support a wide range of content formats and sources, enabling AI agents to expand knowledge effortlessly.
* **Scheduler or recurring option for content sources:** Automate ingestion cycles to keep knowledge up-to-date without manual intervention.
* **Execution history maintenance:** Track, review, and audit previous synchronization runs for improved transparency.
* **Pagination, search, and filter options:** Simplify navigation and management of large content repositories.
* **Ability to delete content sources:** Remove redundant or outdated sources to maintain a clean and relevant knowledge base.
* **Real-time status polling from LLaMB:** Monitor ingestion and synchronization processes with live updates.
* **Improved scalability and stability:** Handle growing data volumes efficiently while ensuring robust system performance.

DataSync lays the foundation for creating intelligent, self-sufficient AI agents that scale support, reduce manual intervention, and enhance the quality of information delivered to end-users.

### 2. Soft unhandled – multilingual support <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FXenTTa48f7IueKXbyuzg%2FDevelooper%20(3).png?alt=media&#x26;token=74d895d6-211d-48d4-8cb6-2e518090b9a4" alt="" data-size="line">

Enhanced to ensure soft unhandled messages are returned in the user’s selected language. When a query is related to the document but does not match exact information, the message now prompts the user in the same conversation language to rephrase or ask another document-related query.

<div align="left"><figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F2ODkvwKNXw5pl1PNgou1%2FScreenshot%202025-09-26%20at%2010.55.42%E2%80%AFAM.png?alt=media&#x26;token=4e9e5b3b-7c33-4dc0-b4c5-08906e831a5d" alt="" width="375"><figcaption></figcaption></figure></div>
