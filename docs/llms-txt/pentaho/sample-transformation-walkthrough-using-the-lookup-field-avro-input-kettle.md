# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/avro-input/using-the-avro-input-step-on-the-pentaho-engine/options-reuse/lookup-fields-tab-reuse/sample-transformation-walkthrough-using-the-lookup-field-avro-input-kettle.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/avro-input/options-reuse/lookup-fields-tab-reuse/sample-transformation-walkthrough-using-the-lookup-field-avro-input-kettle.md

# Sample transformation walkthrough using the Lookup field

The following example transformation demonstrates how to use the **Lookup** field. The transformation processes a CSV file and feeds its data into the Avro Input step. The Avro Input step decodes the Avro structure using a lookup field consisting of an **atm\_id** variable mapped to an *atm* field.

1. Save the following code block in a text file as `atm.schema`.

   ```
   {
     "type": "map",
           "values":{
           "type": "record",
           "name":"ATM",
           "fields": [
                     {"name": "serial_no", "type": "string"},
                     {"name": "location", "type": "string"}
           ]
           }
   }
   ```
2. Save the following code block in a text file as `simpleexample.csv`:

   ```
   atm|atms
   atm1|{"atm1": {"serial_no": "zxy555", "location": "Uptown"}, "atm2": {"serial_no": "vvv242", "location": "Downtown"}, "atm4": {"serial_no": "zzz111", "location": "Central"}, "atm6": {"serial_no": "piu786", "location": "Eastside"}, "atm10": {"serial_no": "hbc999", "location": "Westside"}, "atm20": {"serial_no": "mmm456", "location": "Lunar city"}}
   atm2|{"atm1": {"serial_no": "zxy555", "location": "Uptown"}, "atm2": {"serial_no": "vvv242", "location": "Downtown"}, "atm4": {"serial_no": "zzz111", "location": "Central"}, "atm6": {"serial_no": "piu786", "location": "Eastside"}, "atm10": {"serial_no": "hbc999", "location": "Westside"}, "atm20": {"serial_no": "mmm456", "location": "Lunar city"}}
   atm4|{"atm1": {"serial_no": "zxy555", "location": "Uptown"}, "atm2": {"serial_no": "vvv242", "location": "Downtown"}, "atm4": {"serial_no": "zzz111", "location": "Central"}, "atm6": {"serial_no": "piu786", "location": "Eastside"}, "atm10": {"serial_no": "hbc999", "location": "Westside"}, "atm20": {"serial_no": "mmm456", "location": "Lunar city"}}
   ```
3. Create a transformation with a CSV File Input step and a hop from the CSV Input step to the Avro Input step.

   ![Avro Input Sample CSV Transform](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-0ebd98bcac581ebe4816db2e01a22a4e1b126a55%2FPDI_TransStep_Avro_Input_Sample_CSV_Transform.png?alt=media)
4. Configure the CSV File Input step as shown below, where the file name is the path to the `simpleexample.csv` file on your system:

   ![Avro Input Sample CSV File Input](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-66e785ac510f35b8f16aeded2a386c6c19d7cea1%2FPDI_TransStep_Avro_Input_Sample_CSV_File_Input.png?alt=media)

   **Note:** Make sure that the delimiter is the pipe character.
5. Configure the Avro File Input step tabs as shown below, where the schema is the path to the `atm.schema` file on your system:

   ![Avro Input Sample Source Config](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-26e101d5505b7096adf7ff1f8c92b21a3468b142%2FPDI_AvroInput_SourceTab_PentahoEngine.png?alt=media)
6. Click **Get fields** to populate the **Avro fields** table. Enter the **Indexed values**field as shown below:

   ![Avro Input Sample Avro Fields Config](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-223ae80db6ef71d71b145e9e2dbb4af839acf5e8%2FPDI_TransStep_Avro_Input_Sample_Avro_Fields_Config.png?alt=media)

   **Note:** Make sure to select the **Pass through fields from previous step** option.
7. Enter the following values in the **Lookup fields** tab:

   ![Avro Input Sample Lookup Fields Config](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-2817c439a5b7daba70469369d9868f4209270bcd%2FPDI_TransStep_Avro_Input_Sample_Lookup_Fields_Config.png?alt=media)
8. Click **Preview** to view the data.

   You should see results similar to the results shown below:

   ![Avro Input Sample Preview Data](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-e9e47055da843e6ca4310c7461eee8d647691f14%2FPDI_TransStep_Avro_Input_Sample_Preview_Data.png?alt=media)
9. Save your transformation.
