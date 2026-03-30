# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/split-fields/general-split-fields.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/split-fields/general-split-fields.md

# General

![Split Fields step](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3f39a545a89a948927948c27fdc83be3f3847c18%2FPDI_Split_Fields_dlg.png?alt=media)

The following fields are general to this transformation step:

| Field              | Description                                                                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Step Name**      | Specify the unique name of the step on the canvas. You can customize the name or leave it as the default.                                                                                 |
| **Field to split** | Specify the name of the field you want to split.                                                                                                                                          |
| **Delimiter**      | Specify the delimiter character that separates the fields. Special characters can be set with the format `$[value]`. For example `$[01]`, or `CHAR HEX01` can be set as `$[6F,FF,00,1F]`. |
| **Enclosure**      | Enclose a field with a pair of specified strings. Use this option if you want separator characters in the fields.                                                                         |
