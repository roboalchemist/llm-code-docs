# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v9.1.0/introducing-the-datasync-2.0.md

# Introducing the DataSync 2.0

**DataSync 2.0** is a robust content integration and synchronization capability within the Avaamo Conversational AI Platform, designed to empower agents by seamlessly ingesting, processing, and managing information from multiple content sources. This ensures that agents deliver accurate, context-aware, and up-to-date responses.

## Key Highlights of DataSync 2.0

### Comprehensive life cycle management

DataSync 2.0 now supports the complete agent life cycle, from content ingestion and synchronization to updates and deletion. This enhancement ensures smooth and efficient management of all content sources throughout the agent’s operation.

With this capability, you can:

* **Ingest** content from multiple sources such as files, websites, or enterprise connectors.
* **Synchronize** content automatically or manually to keep your agent’s knowledge up to date.
* **Update** existing content sources without recreating jobs, enabling incremental updates.
* **Delete** outdated or irrelevant content sources when no longer needed.

This end-to-end life-cycle support streamlines content management, reduces manual effort, and ensures your agent always operates with the most up-to-date, accurate data.

### Keep your data updated with scheduled syncs

The scheduler option allows you to set up automatic, recurring synchronization for supported content sources. By defining a preferred schedule, you can ensure that your content is updated regularly without manual intervention. This feature helps maintain data consistency and ensures that all ingested information remains current across the platform.

Refer [Auto Sync](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/auto-sync), for more information.

### Manual synchronization with one click

The manual sync option enables users to initiate synchronization for any content source with a single click. This provides an easy and efficient way to refresh content on demand without waiting for scheduled syncs. It ensures that the latest updates from your connected sources are immediately reflected, keeping your data current and consistent across the platform.

Refer [Sync Now](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/sync-now), for more information.

### Access detailed logs of previous sync executions

DataSync now keeps a detailed record of all synchronization executions, allowing users to view and analyze previous runs. This helps track sync activity, review results, and diagnose issues quickly. Maintaining an execution history provides better visibility, greater accountability, and easier troubleshooting across all supported content sources.

Refer [View job version history](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/view-job-version-history), for more information.

### Efficient navigation for large document collections

Pagination support enhances the user experience when working with large document collections. Instead of loading all documents at once, DataSync now divides them into smaller, manageable pages. This improves navigation, reduces load time, and ensures smoother performance when browsing or managing extensive content sources.

### Effortless content discovery across sources

The dynamic search option allows users to locate specific documents within individual content sources quickly. You can search using document names, partial matches, or even parts of the document URL. This feature streamlines content discovery, helping users efficiently find and manage the information they need within large datasets.

### **View synchronization results by status**

The filter-by-status feature enables users to list documents or articles by ingestion status, such as "Ingested," "Error," or "In Progress." This functionality helps users quickly identify problem areas, track ingestion progress, and manage content more efficiently.

### **Remove outdated or unused content sources**

Users can now delete any outdated or unused content source directly from the DataSync interface. This feature helps maintain a clean and organized workspace by allowing you to remove unnecessary or redundant data sources easily.

Refer [Delete job](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/delete-job), for more information.

### **Enhanced performance for large-scale operations**

This release strengthens the system’s ability to manage large ingestion and synchronization workloads more efficiently. Improved scalability and stability ensure consistent performance, faster processing, and greater reliability even under heavy operational demands.

### Actions available for an ingested document

**Ability to update the preview URL:** Users can now modify a document's preview URL after ingestion, ensuring accurate content verification and updated linking.

**Ability to update attributes after ingestion:** The attributes or metadata of ingested documents can be edited at any time, offering greater flexibility in managing document details.

**Ability to delete a single document:** You can remove individual documents without deleting the entire content source, keeping data organized and precise.

**Ability to re-ingest a single document:** Specific documents can be re-synced independently to refresh content without running a complete synchronization job.

Refer [Actions](https://docs.avaamo.com/user-guide/datasync-ai/content-sources/common-actions/actions), for more information.

### **Easily upload multiple documents at once**

The Files content source now supports bulk uploads, allowing users to add multiple documents in a single action. This enhancement simplifies large-scale ingestion and saves time when managing extensive document collections.

### **Add new files to an existing Files content source**

Users can now upload additional files to an already created Files content source. This capability supports incremental updates, enabling content expansion or modification without recreating jobs.

## Why Use DataSync 2.0?

DataSync 2.0 provides a **production-ready foundation** for creating intelligent, self-sufficient AI agents that:

* Deliver accurate and context-aware responses
* Reduce manual intervention and operational overhead
* Scale knowledge efficiently across multiple content sources, including **web platforms** and **files**
* Ensure secure, reliable, and high-quality knowledge delivery to end users

## Next steps

1. Understand what is required in the [Before you begin](https://docs.avaamo.com/user-guide/datasync-ai/before-you-begin) section.
2. Refer [DataSync AI](https://docs.avaamo.com/user-guide/datasync-ai), for more information.
