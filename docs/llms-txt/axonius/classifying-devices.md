# Source: https://docs.axonius.com/docs/classifying-devices.md

# Classifying Devices

Navigate to the **Device Inventory Classification** page from the Devices page:

![DeviceInventoryClassificationNavigation](https://files.readme.io/b5a2d16859052c66520ba11780e8912311efed99a0de6271fdb9ea326044bd38-image.png)

<br />

The left navigation panel in the Device Inventory Classification page details the categories applying to your devices:

* **Device Type** - The general category or function of the device.
* **Device OS Family Details** - The operating system family the device belongs to.
* **Deployment Type** - The execution or hosting environment in which the device runs.
* **Device Ownership** - whether the device is business owned, privately owned, etc.
* **Device Lifecycle Status** - The lifecycle or behavior pattern of the device, based on its presence and activity.
* **Device Criticality** - the level of importance of the device.

Expand each category to view the device classes associated with it. For example, the **Device Type** category includes classes such as laptops, mobile devices, and more.

## Selecting Devices to Classify

Select a device class to do the following:

1. Select a query representing the devices in this class. You can select an Axonius predefined query or create your own [saved query](/docs/saved-queries-devices).
   For example, under **Device Lifecycle Status**, you can define that devices seen in the last 30 days are considered Active:

<Image align="center" alt="DeviceLifecycleStatusQuerySelection" width="700px" src="https://files.readme.io/04908e8385bfe0b959dd55f8115a02b35c2c5da18c7c5aba155b8564edd3c743-image.png" />

<br />

2. Provide a description for this class. This description will be used everywhere this class appears - for example, when it’s selected as a field in the Query Wizard. Axonius provides a custom description text, but you can change it.

<Callout icon="💡" theme="warn">
  Important Note

  The categories and classes of devices represent a field-value relationship. For example, **Device Type** is the name of a field that may contain the following values: Desktops and Workstations, Laptops, Mobile, and more. The description you provide for each class is the **value description** of this class.
</Callout>

3. Select whether to apply this class rule starting from the next discovery cycle (recommended for consistency). To apply this, toggle the **Activate** button on. The rule will be executed and classify the devices matching the query on every discovery cycle.
4. Click **Save**, or **Save and Run** to immediately initiate a classification process with the new rule.

## Working with Classifications in the Devices Page

Using the Query Wizard in the **Devices** page, filter the Devices table by selected categories and classes.

1. In the Query Wizard, from the **Field** drop-down, select **Identifiers**. This displays all device categories (A).
2. Hover over a category (B) to view its description (C) and all device classes in this category (D).
3. Click + to view the full list of values (E).

<Image align="center" alt="QueryWizardIdentifiers" width="700px" src="https://files.readme.io/7c1a4845d0e0e8d10d8bee9123f5b5408cb06ff8eb23f65ad1e0c3bae72db78a-image.png" />

<br />

3. Select an identifier. It appears in the Field drop-down, and then, the **Equal / in Equal operators** appear in the operator drop-down. Select the operator relevant to your needs. See [Using Operators in the Query Wizard](/docs/query-wizard-operators) to learn more.
4. From the **Value** field, select the class to filter results by.
   In the following example, we want to display devices whose **Device Type** is **Servers**:

<Image align="center" alt="FilterDeviceTypeByServers" width="600px" src="https://files.readme.io/96723bc445724d4b86c7f1b06c7c53a63636b4ea8a24cd57a73514dcbca701ea-image.png" />

<br />

<Callout icon="📘" theme="info">
  Reminder

  You can edit the value description at any time from the Device Inventory Classification page.
</Callout>

The Devices table now displays only Servers:

![DevicesTableFiltered](https://files.readme.io/9b9c6979b5713f7bda7c7a62517bde07b04d9e219c2de197846f031e02f75dd2-image.png)

<br />

### Exploring Different Device Contexts

To explore the relations between different device classes, you can build more complex queries with more than one identifier. For example, show devices whose Device Type is Servers **and** whose Device OS Family is Windows:

<Image align="center" alt="ComplexQueryServersAndWindowsOSFamily" width="700px" src="https://files.readme.io/f57f45aab400e44b30248d910498da3e9b98d7c9cac48b3620f84d9993932c2d-image.png" />

<br />

If you save this query, and access it from the Queries page, hovering over the Identifier or Value fields displays their descriptions.

<Image align="center" alt="QueriesPageIdentifierValueDescriptions" width="700px" src="https://files.readme.io/7d24e33b77265bd4fdaaeff2458ba6d4cb6f54d748ed8a8251360aace3faf0ef-image.png" />

<br />

Device Inventory Classification also helps you find very specific contexts between device classes and security issues, leading to a better, more focused risk assessment. For example, you can show only Critical CVEs that exist specifically on Business-Owned (Managed) devices:

<Image align="center" alt="QueryCriticalCVEsOnBusinessOwnedDevicesQuery" width="600px" src="https://files.readme.io/21edf60c7acc4a606de5bca991470cf68154016bd9c0c91da45c23109da7fdc0-image.png" />

<br />