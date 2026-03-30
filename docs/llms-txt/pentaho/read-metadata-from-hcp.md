# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-hcp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-hcp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/read-metadata-from-hcp.md

# Read metadata from HCP

You can use the Read metadata from HCP step to identify and select an HCP object by its URL path and then select a specific target annotation name to read. The step returns the requested custom metadata from the annotation back to your PDI transformation for downstream processing. You can use the [Write metadata to HCP](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/write-metadata-to-hcp) step to further refine the metadata within the transformation and write it back to HCP.

[Hitachi Content Platform](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pdi-and-hitachi-content-platform-hcp) (HCP) is an object-based storage repository designed for unstructured data. To add structure and control to the data, HCP creates metadata annotations that are associated with each object. An HCP object consists of a read-only file, a unique URL, system metadata properties, and custom metadata annotations. Each annotation for an HCP object has its own annotation name (for example: `myannotation0515202`).
