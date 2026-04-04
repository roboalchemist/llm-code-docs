# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/introducing-knowledge-skill-2.0.md

# Introducing Knowledge skill 2.0

The `Knowledge skill` is a core capability of the Avaamo Conversational AI Platform, designed to empower AI agents to access, process, and deliver information from multiple content sources accurately, efficiently, and at scale.&#x20;

{% hint style="info" %}
**Note:** For organizations with **DataSync enabled**, all newly created Knowledge Skills continue to point to the DataSync UI for streamlined content management.
{% endhint %}

### What is a Knowledge skill?

The Knowledge skill allows AI agents to seamlessly ingest and interact with content from diverse sources, including:

* Product documentation
* User manuals and guides
* FAQs and help articles
* Enterprise knowledge systems

This integration ensures AI agents deliver context-aware, up-to-date, and accurate responses, reducing manual intervention and enhancing the overall quality of user interactions.

### Getting started with Knowledge skill

1. Navigate to the `Agent` page in the Avaamo platform.
2. Select `Skills` from the left navigation menu.
3. Click `Add skill`.
4. On the `Skill Builder` page, choose the `Knowledge skill`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F6KDhRvzsSRDpI9zYOlfh%2Fimage.png?alt=media&#x26;token=87770657-59a9-4087-913c-fd6f0842b4da" alt=""><figcaption></figcaption></figure>

6. Select your `content source` and begin ingesting your documents.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3xHrfeKZcyb975ZmJYft%2Fimage.png?alt=media&#x26;token=d1fc34a2-3d5f-4812-90f6-7c381731f991" alt=""><figcaption></figcaption></figure>

Refer Content sources, for more information.

### Key highlights of Knowledge skill

Building on the foundation of `DataSync`, Knowledge Skill includes robust features for content integration, synchronization, execution history, error handling, and scalability. In addition, it introduces these key differentiators:

#### 1. Flat knowledge structure

Unlike LLaMB, which relied on separate document groups, Knowledge Skill ingests all content into a single unified skill. This simplifies organization, search, and retrieval, making knowledge management straightforward and scalable.

#### **2. Centralized view for content and ingestion management**

The new Knowledge tab provides a unified location within each skill to manage all content-related operations. It consolidates content sources, ingestion history, and synchronization details, providing users with a clear, organized view of the knowledge associated with that specific skill. This improves accessibility, simplifies monitoring, and enhances overall management efficiency.

Refer [View and edit knowledge](https://docs.avaamo.com/user-guide/skills/knowledge-skill/view-and-edit-knowledge), for more information.

#### **3. Monitor synchronization progress instantly**

Knowledge Skill 2.0 offers real-time synchronization status updates from LLaMB, enabling users to track the progress and completion of sync operations without delay. This ensures greater visibility into the synchronization process and helps in promptly identifying any issues.

#### **4. Pull specific knowledge skill changes**

As part of **Knowledge Skill 2.0**, you can now pull updates for particular changes made to knowledge skills between stages. This improvement gives users greater control over stage deployments and prevents unintended updates to unrelated knowledge skills.

For example, when you add or modify a knowledge skill during development and plan to update it in production, the system displays a list of the added or modified skills under `Advanced Options`. From this list, you can select the specific changes to apply, ensuring that only the chosen updates are reflected in the production agent.

#### **5. Ability to view a single document:**

Users can preview or inspect individual records within the Knowledge Skill 2.0 interface for quick review and validation.

### Benefits of using the Knowledge skill

* **Intelligent AI agents:** Deliver accurate, context-aware responses consistently.
* **Simplified knowledge management:** Single, unified structure for all content.
* **Scalable operations:** Efficient handling of large volumes of content with full execution history and error tracking.
* **Enhanced user experience:** Provides reliable, timely information, improving engagement and trust.

### Next steps

* Understand what is required in the [Before you begin](https://docs.avaamo.com/user-guide/ai-agent/before-you-begin) section.
* Start by creating a new [AI agent](https://docs.avaamo.com/user-guide/ai-agent/create-an-ai-agent).
* You are now ready to [get started](https://docs.avaamo.com/user-guide/get-started) by exploring AI agents in the Avaamo Conversational AI Platform.

Refer [Knowledge skill](https://docs.avaamo.com/user-guide/skills/knowledge-skill), for more information.
