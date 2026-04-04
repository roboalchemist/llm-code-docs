# Source: https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties.md

# Properties

Properties are customizable data fields of [blueprints](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md), used to save and display information from external data sources.

## Configure properties in Port[â](#configure-properties-in-port "Direct link to Configure properties in Port")

You can create, delete, or edit properties via the builder page or directly from the software catalog.

### From the builder page[â](#from-the-builder-page "Direct link to From the builder page")

**To edit an existing property:**

1. Go to your [Builder page](https://app.getport.io/settings).
2. Expand the blueprint you want to edit by double-clicking on it.
3. Under the `Properties` tab, click on the property you want to edit.
4. Make your desired changes to the form, then click `Save`.

**To create a new property:**

1. Go to your [Builder page](https://app.getport.io/settings).
2. Expand the blueprint you want to edit by double-clicking on it.
3. Click on the `+ New property` button:

![](/img/software-catalog/customize-integrations/createNewProperty.png)

<br />

<br />

4. Fill in the form with the desired property details, including the [property type](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/.md#supported-properties), then click `Create`.

### From the software catalog[â](#from-the-software-catalog "Direct link to From the software catalog")

Each catalog page in your software catalog contains a table with all entities created from a certain blueprint. You can modify the properties of the blueprint directly from this table:

1. Go to the desired page of your [software catalog](https://app.getport.io/organization/catalog).

2. In the top-right corner of the table are its filters, click on the `Manage properties` button:

   ![](/img/software-catalog/customize-integrations/managePropertiesFromCatalog.png)

   <br />

3. A dropdown will appear showing all of the properties.<br /><!-- -->To modify or delete a property, hover over the it and click on the `...` icon:

   ![](/img/software-catalog/customize-integrations/managePropertiesDropdown.png)

   <br />

   **Note** that [meta-properties](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md) are not editable, so you will not see a `...` icon next to them.

4. To create a new property in the blueprint, click on the `+ Property` button at the bottom of the dropdown.

Hiding properties

You can also hide properties from the table by clicking on the toggle on the right side of the property name.

## Structure[â](#structure "Direct link to Structure")

Each blueprint has a `properties` section under its `schema`. Each property is defined as an object with the following structure:

```
{
  "myProp": {
    "title": "My property",
    "icon": "My icon",
    "description": "My property",
    "type": "property_type"
  }
}
```

The different components that make up a basic property definition are listed in the following table:

| Field         | Description                                                                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`       | Property title.                                                                                                                                                                   |
| `identifier`  | Property identifer. (Maximum 100 characters)                                                                                                                                      |
| `type`        | **Mandatory field.** The data type of the property.                                                                                                                               |
| `icon`        | Icon for the property.<br /><br />See the [full icon list](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/.md#full-icon-list).          |
| `description` | Description of the property.<br />This value is visible to users when hovering on the info icon in the UI. It provides detailed information about the use of a specific property. |
| `default`     | Default value for this property in case an entity is created without explicitly providing a value.                                                                                |

Property name

The name of the property is the key of the property object. For example, in the code block above, the name of the property is `myProp`.

## Change a property's type[â](#change-a-propertys-type "Direct link to Change a property's type")

The **type** field setting of a property (**number**, **string**, etc.) is permanent and cannot be changed after the property is created. If you create a **number** property, you won't be able to change it later to a **string**.

To change the type configuration after creation:

1. Create a new property with the desired **type**.
2. Use the [migrate blueprint data](/build-your-software-catalog/customize-integrations/configure-data-model/migrate-data/.md) feature to insert the data to the new property. Ensure you apply the correct conversions if needed (for example, converting numbers to strings).
3. Delete the old property.
4. Rename the new property to the old property name (optional).

## Supported properties[â](#supported-properties "Direct link to Supported properties")

## [ðï¸<!-- --> <!-- -->Aggregation Property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/aggregation-property.md)

[Aggregation properties allow you to calculate metrics based on the relations in your catalog.](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/aggregation-property.md)

## [ðï¸<!-- --> <!-- -->Array](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/array.md)

[Array is a data type used to save lists of data](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/array.md)

## [ðï¸<!-- --> <!-- -->Boolean](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/boolean.md)

[Boolean is a primitive data type that has one of two possible values - true and false](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/boolean.md)

## [ðï¸<!-- --> <!-- -->Calculation](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/.md)

[1 item](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/.md)

## [ðï¸<!-- --> <!-- -->Datetime](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/datetime.md)

[Datetime is a data type used to reference a date and time](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/datetime.md)

## [ðï¸<!-- --> <!-- -->Email](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/email.md)

[Email is a data type used to save Email addresses](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/email.md)

## [ðï¸<!-- --> <!-- -->Embedded Url](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/.md)

[1 item](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/embedded-url/.md)

## [ðï¸<!-- --> <!-- -->Markdown](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/markdown.md)

[The Markdown property is used to display Markdown content within an entity in Port.](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/markdown.md)

## [ðï¸<!-- --> <!-- -->Meta](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md)

[A meta-property is a property that exists on every entity in Port by default.](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md)

## [ðï¸<!-- --> <!-- -->Mirror Property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/mirror-property.md)

[Mirror Property allows you to map data from related entities to your entity](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/mirror-property.md)

## [ðï¸<!-- --> <!-- -->Number](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/number.md)

[Number is a primitive data type used to save numeric data](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/number.md)

## [ðï¸<!-- --> <!-- -->Object](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/object.md)

[Object is a data type used to save object definitions in JSON](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/object.md)

## [ðï¸<!-- --> <!-- -->Proto](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/proto.md)

[Proto is a data type used to save proto definitions in Port](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/proto.md)

## [ðï¸<!-- --> <!-- -->String](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/string.md)

[String is a primitive data type used to save text data](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/string.md)

## [ðï¸<!-- --> <!-- -->Swagger UI](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/swagger.md)

[The Swagger UI property is used to import and display OpenAPI and/or AsyncAPI specification files within an entity in Port.](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/swagger.md)

## [ðï¸<!-- --> <!-- -->Team](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/team.md)

[Team is a data type used to reference teams that exist in Port](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/team.md)

## [ðï¸<!-- --> <!-- -->Timer](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/timer.md)

[Timer is a data type used to define an expiration date/lifespan of a specific entity](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/timer.md)

## [ðï¸<!-- --> <!-- -->URL](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/url.md)

[URL is a data type used to save links to websites](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/url.md)

## [ðï¸<!-- --> <!-- -->Enum](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/enum.md)

[Enum is a data type used to define a named set of constant values.](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/enum.md)

## [ðï¸<!-- --> <!-- -->User](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/user.md)

[User is a data type used to reference users that exist in Port](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/user.md)

## [ðï¸<!-- --> <!-- -->Yaml](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/yaml.md)

[Yaml is a data type used to save object definitions in YAML](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/yaml.md)

## [ðï¸<!-- --> <!-- -->Labeled URL](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/labeled-url-object.md)

[Labeled URL is an object type used to store URLs with custom display labels](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/labeled-url-object.md)
