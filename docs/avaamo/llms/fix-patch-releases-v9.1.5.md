# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/fix-patch-releases-v9.1.5.md

# Fix patch releases (v9.1.5)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.1.5. The following are some of the key fixes included in this release:

1. [Attribute handler support in datasync](#attribute-handler-support-in-datasync)
2. [Default prompt template for new prompt skills](#default-prompt-template-for-new-prompt-skills)
3. [Selective restore options for version comparison](#selective-restore-options-for-version-comparison)

### Attribute handler support in datasync

In this release, we are introducing `Configure Advanced Attribute Handler` support in `DataSync`, a powerful new capability that lets you dynamically assign custom attributes to documents using JavaScript.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8B2AFNsKL5SHCj2CcR7M%2FScreenshot%202026-01-29%20at%205.06.27%E2%80%AFPM.png?alt=media&#x26;token=2dd9ae7a-524c-49a0-b132-357bcf080dba" alt=""><figcaption></figcaption></figure>

With this enhancement, developers can write JavaScript logic that returns specific attributes during ingestion, allowing metadata such as location, category, or other fields to be calculated and applied automatically. These attributes become part of the document’s metadata and can be used for filtering, authorization, search relevance, and downstream logic in your agents.

This enhancement enhances document ingestion flexibility and provides richer control over how document metadata is created and managed during the DataSync process.

**Key highlights:**

* **Enable attribute handler:** Turn on the attribute handler in the DataSync configuration to use custom JavaScript for attribute assignment.
* **Post-ingestion attribute updates:** If attributes were not configured during ingestion, or if you need to update attributes for already ingested documents or articles, you can use the Advanced Attribute Handler. This feature allows you to apply or modify document attributes using custom JavaScript logic during a sync run.
* **Test attribute logic:** Validate the JavaScript logic and verify the updated attributes before applying them across documents during a sync operation.
* **View and export attributes:** Easily review the attributes applied to documents using the View document attributes option and export them as a `CSV file` to audit changes, troubleshoot issues, and support further analysis.
* **Custom JS for dynamic attributes:** Use JavaScript to evaluate document metadata and return attributes based on your logic (e.g., setting a location based on document number).
* **Debug and logs:** Logs from your JavaScript are visible in debug logs to help with development and troubleshooting.
* **Controlled application:** Attribute logic is executed during sync runs (Sync Now or Auto Sync), and changes take effect only after a sync. This ensures safe, predictable application of attribute logic.
* **Error handling:** If incorrect JavaScript causes an error during execution, documents with missing or invalid critical attributes will be marked in error status to prevent unintended exposure. Detailed error information is available in the JavaScript extension error logs.

### Default prompt template for new prompt skills

When you create a new Prompt Skill, a simple `default prompt` is now automatically available in the prompt editor. The default prompt includes a `sample function` to help you get started faster. The sample function connects the Knowledge Handler with the agentic agent to handle Knowledge Skill–related queries.

This enhancement reduces initial setup effort and provides clear guidance on structuring prompts and defining functions when building or configuring prompt skills.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmaiHAED3kou5w46DZ05d%2FScreenshot%202026-01-28%20at%2012.00.05%E2%80%AFPM.png?alt=media&#x26;token=5a2898d3-ad1e-4dc8-855b-c730526bd353" alt=""><figcaption></figcaption></figure>

This enhancement also creates a sample function, as shown below:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FsXbR4AzTsTEjKS1odIlM%2FScreenshot%202026-01-30%20at%2010.57.26%E2%80%AFAM.png?alt=media&#x26;token=37896f01-eb99-4cb8-a4ef-12452089d9c9" alt=""><figcaption></figcaption></figure>

Refer [Prompt skill](https://docs.avaamo.com/user-guide/skills/prompt-skill/create-prompt-skill), for more information.

### Selective restore options for version comparison

In this release, the `Version Comparison` page has been enhanced to support `selective restoration` of changes. You can now choose which sections of a version you want to restore instead of restoring all changes.

Checkboxes are now available for the following sections if the changes are made:

* Prompt
* Function Calls
* Advanced Settings

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F4LYZlnxVyAjqGQQtkEqN%2FScreenshot%202026-01-30%20at%2010.32.09%E2%80%AFAM.png?alt=media&#x26;token=a061cb96-8e4f-4189-9cc6-f0e1287416b4" alt=""><figcaption></figcaption></figure>

You can select one or more sections, and the restore action applies only to those sections. This enhancement provides better control over version restoration and improves the overall version management experience.

Refer [Restore selected](https://docs.avaamo.com/user-guide/skills/prompt-skill/prompt-versions#restore-selected), for more information.
