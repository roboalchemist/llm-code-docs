# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/options-etl-metadata-injection/inject-metadata-tab/specify-the-source-field.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection/options-etl-metadata-injection/inject-metadata-tab/specify-the-source-field.md

# Specify the source field

To specify the source field as metadata to be injected, perform the following steps:

1. In the **Target injection step key**column, double-click the field for which you want to specify a source field.

   The **Source field**dialog box opens.

   ![PDI ETL Metadata Source field dialog box](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-313b476925043a959368fa1c38fc3ec66de049ea%2FPDI%20ETL%20Metadata%20Source%20field%20dialog%20box.png?alt=media)
2. Select a source field and click **OK**.
3. (Optional) Type a word in the **Filter** field and click the **Search** icon to search for fields with that name. Click the **Regex** icon to search using Java regular expressions.
4. (Optional) Select **Use constant value** to specify a constant value for the injected metadata through one of the following actions:
   * Manually entering a value.
   * Using an internal variable to set the value: *${Internal.Step.Unique.Count}*, for example.
   * Using a combination of manually specified values and parameter values: *${FILE\_PREFIX}\_${FILE\_DATE}.txt*, for example.
