# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.0.0/fix-patch-releases-v9.0.5.md

# Fix patch releases (v9.0.5)

This article summarizes a list of fix patch releases made in the Avaamo Conversational AI Platform version 9.0.5. The following are some of the key fixes included in this release:

1. [Default markdown support for new channels](#id-1.-default-markdown-support-for-new-channels)
2. [DataSync enhancements](#id-2.-datasync-enhancements)

### **1. Default markdown support for new channels**

All newly created channels include Markdown rendering enabled by default for LLaMB responses. This enhancement ensures that formatted text elements, such as bold, italics, bullet points, and hyperlinks, are rendered as intended without additional setup.

Channels created before this update remain unchanged and retain their existing Markdown configuration. Markdown settings can be manually adjusted from the channel configuration page if needed.

### 2. DataSync enhancements

This release includes several improvements to the **DataSync 2.0 (Beta)** version, enhancing usability, consistency, and data security.

**Key enhancements:**

* **Unlimited ingestion:** The rate limit has been removed — you can now ingest any number of files without restriction.
* **Improved pull/promote process:** Enhanced reliability and performance for data pull and promote operations within DataSync.
* **Dynamic attributes for ServiceNow:** Added support for dynamically pulling attributes from ServiceNow to streamline data synchronization.
* **Duplicate validation:**
  * Duplicate files are not allowed.
  * Duplicate job names are restricted.
* **Delete confirmation:** A Consent button has been added before deleting any ingested document in DataSync AI to prevent accidental deletions.
* **Preview URL update:** Support added for updating the `preview URL` when editing a document.
* **Improved data security:** The `View Job Details` pop-up no longer displays the user’s access token.
* **Consistent messaging:** Consent and confirmation messages have been updated to align with the platform’s design and style guidelines.
* **Product stability:** Other cosmetic updates and minor bug fixes have been implemented to enhance overall stability and performance.
