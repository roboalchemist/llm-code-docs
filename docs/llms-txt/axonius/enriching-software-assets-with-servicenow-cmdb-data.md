# Source: https://docs.axonius.com/docs/enriching-software-assets-with-servicenow-cmdb-data.md

# Enriching Software Assets with ServiceNow CMDB Data

You can enrich the Axonius Software table with ServiceNow CMDB data from the CMDB table. To do this, you must first configure the ServiceNow adapter and have access to the CMDB table.

The software hash ID (based on the Software Name and Vendor Name) and the Software Version must be exact matches. Each record in the CMDB is at the version level, so enrichment will happen only when the hash and the version match.

## Configuring the Schema Mapping

To configure the fields you want to enrich, you need to create a custom schema mapping JSON file. For more information, see [Using Custom Schema Entries to Add a JSON File to Fetch Information from One Object to Another](/docs/servicenow#using-custom-schema-entries-to-add-a-json-file-to-fetch-information-from-one-object-to-another).

## Field Mapping

You can map standard ServiceNow fields into Axonius Software fields. In addition, you can map custom ServiceNow fields (identified by “\_” at the beginning of their name) as aggregated fields in Axonius. The fields are displayed in the Software module and on the Devices page as part of the Installed Software complex field.

<Callout icon="📘" theme="info">
  Note

  * When mapping ServiceNow fields, it’s important to map to fields that exist in both modules (Software and Devices). Any field that isn’t under Installed Software will not appear in the Devices module.

  * Mapping to the **Approval Status** field automatically adds the asset to the [Software Registry](/docs/software-approval-list), where it remains visible even if not detected on a device.

  * The following fields are mapped out of the box for ServiceNow enrichment - you don’t need to map them:
    * Installed Software: Name=product (and if it’s missing then) name
    * Installed Software: Name=manufacturer
    * Installed Software: Version=version
    * Installed Software: Description=description
    * Installed Software: Major Version=major version
    * Installed Software: Managed Status=status
</Callout>

1. Make sure that the ServiceNow adapter is connected.

2. In the ServiceNow adapter, enable the **Fetch “cmdb\_software\_product\_model” table for Various Software enrichment** advanced setting.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNow%20Fetch%20CMDB%20table%20Software%20Enrichment%20adv%20setting.png)

3. Then enable [**Custom Parsing**](/docs/adapter-custom-parsing).
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNow%20Software%20Custom%20Parsing%20enabled.png)

4. Click > to open the **Software Custom Parsing** setting.

   1. **Field Title** - Select an existing field or create a new one.
      ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNow%20Software%20Custom%20Parsing%20create%20new%20field.png)

   <Callout icon="📘" theme="info">
     Note

     For a CMDB software enrichment field to be displayed in Devices, it must be inside the Installed Software complex field.
   </Callout>

   2. **Raw Path** - Enter the software raw path + “|value” (Example: owner|value)

   <Callout icon="📘" theme="info">
     Note

     You need to export the ServiceNow CMDB table as XML in order to see its raw path.
   </Callout>

   <Image alt="ServiceNow Export XML.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNow%20Export%20XML.png" />

   3. **Type** - Select the relevant field type.
   4. **Field Structure** - Select the field structure.

5. Click **Add Field** to add another field.

   <Image alt="ServiceNow Software Custom Parsing.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ServiceNow%20Software%20Custom%20Parsing.png" />

6. Click **Save**.

7. The updated values are only displayed after a new global discovery cycle runs. You can run it manually if necessary. For more details, see [Discovery Cycle](/docs/discovery-cycle).

8. When the cycle is complete, the enrichment fields appear in the Installed Software complex field in both Software and Devices. CMDB enrichments are also visible when selecting the specific adapter ([ServiceNow](/docs/servicenow)) in the Query Wizard.