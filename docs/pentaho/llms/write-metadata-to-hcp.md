# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/write-metadata-to-hcp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/write-metadata-to-hcp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/write-metadata-to-hcp.md

# Write metadata to HCP

Use the Write metadata to HCP step to write custom metadata fields to a Hitachi Content Platform (HCP) object. Within the step, you can select an HCP object by its URL and then write custom metadata annotations to the object associated with the object URL, enriching and validating the data stored in your HCP repository.

[Hitachi Content Platform](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-hitachi-content-platform-hcp) (HCP) is an object-based storage repository designed for unstructured data. An HCP object consists of a read-only file, a unique URL, system metadata properties, and custom metadata annotations. Each custom metadata annotation for an HCP object must have its own unique annotation name (for example: `myannotation0515202`). HCP uses the annotations associated with each object to add structure and control to the data it stores.

**Note:** For this step to access HCP through the Virtual File System (VFS), you must configure object versioning in HCP Namespaces. See [Access to HCP REST](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/virtual-file-system-browser/before-you-begin-vfs-connections/access-to-hcp-rest).
