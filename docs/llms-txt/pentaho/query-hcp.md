# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/query-hcp.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/query-hcp.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/query-hcp.md

# Query HCP

The Query HCP step uses the [Metadata Query Engine (MQE)](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/Developer_documentation/Searching_Namespaces/01_Introduction_to_searching_in_HCP#Search_facilities) to query your [Hitachi Content Platform (HCP)](https://knowledge.hitachivantara.com/Documents/Storage/Content_Platform/8.1.2/System_administration/Introduction_to_Hitachi_Content_Platform/01_About_Hitachi_Content_Platform) repository for objects, their URLs, and system metadata properties. You can use the resulting object URL to define [HCP object and custom metadata](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Advanced%20Pentaho%20Data%20Integration%20topics/Advanced%20topics%20\(Pentaho%20Data%20Integration%20overview\)/PDI%20and%20Hitachi%20Content%20Platform%20\(HCP\)=GUID-F4977458-2FA6-4D2C-8991-1391D0849655=6=en=.md) locations for the PDI [Read metadata from HCP](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/PDI/Transformation%20steps/PDI%20transformation%20steps%20reference%20\(overview\)/Read%20metadata%20from%20HCP=GUID-8452E7E6-3B0E-4DCC-A8CF-468DD73A0A6B=2=en=.md) and [Write metadata to HCP](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/write-metadata-to-hcp) steps.

**Note:** After modifying an HCP object, your change may not be immediately reflected in your query results of the HCP repository until the search index has been updated.
