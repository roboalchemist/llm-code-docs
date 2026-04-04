# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/fix-patch-releases-v9.1.2.md

# Fix patch releases (v9.1.2)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.1.2. The following are some of the key fixes included in this release:

1. [Introducing Salesforce as a content source for DataSync (Beta)](#introducing-salesforce-as-a-content-source-for-datasync-beta)
2. [Pull specific LLaMB skill changes](#pull-specific-llamb-skill-changes)

### Introducing Salesforce as a content source for DataSync (Beta)

In this release, DataSync AI now supports `Salesforce` as a content source, allowing you to bring Salesforce records directly into your agent knowledge.&#x20;

{% hint style="info" %}
This feature is currently in beta and intended for testing; feedback is appreciated.
{% endhint %}

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FtUEA2gXCWtPQFGwrh4GM%2FScreenshot%202025-12-04%20at%2012.22.10%E2%80%AFPM.png?alt=media&#x26;token=129044f6-7ca0-4f8e-8f28-d33156e05433" alt=""><figcaption></figcaption></figure>

With this enhancement, DataSync seamlessly processes information from Salesforce, including cases, knowledge articles, and custom objects, alongside other supported content sources. This helps agents provide accurate, context-aware responses based on the latest data available in your Salesforce environment.

This feature extends DataSync's reach, making it easier to unify enterprise knowledge and keep your agents consistently up to date.

### Pull specific LLaMB skill changes

In this release, the LLaMB skill now supports pulling updates for **specific LLaMB skill changes** between stages. This improvement gives users greater control over stage deployments and helps prevent accidental updates to unrelated LLaMB skills.

When you add or modify an LLaMB skill during development and then initiate an update to production, the system will now display all detected changes under `Advanced Options`. You can review the list and selectively choose which updates to apply, ensuring only the intended LLaMB skill changes move to the production agent.

The changes are categorized as follows:

* **To be created**: Newly added LLaMB skills
* **To be updated**: Existing LLaMB skills that have been modified

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FuYpeiwpING6VNejAaFBa%2FScreenshot%202025-12-04%20at%2011.27.55%E2%80%AFAM.png?alt=media&#x26;token=66dac582-7c67-4299-8b4b-9d2f7ebd765d" alt=""><figcaption></figcaption></figure>

This enhancement ensures safer, more predictable deployments and improved version management across stages.

Refer [Promote and pull updates](https://docs.avaamo.com/user-guide/how-to/build-agents/manage-agents/promote-and-pull-updates), for more information.
