# Source: https://flatfile.com/docs/core-concepts/sheets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sheets

> Individual data tables within Workbooks that organize and structure imported data

## What are Sheets?

Sheets are individual data tables within [Workbooks](/core-concepts/workbooks) that organize and structure imported data. Each Sheet represents a distinct data type or entity, similar to tables in a database or tabs in a spreadsheet.

Sheets serve as containers for [Records](/core-concepts/records) and are defined by [Blueprints](/core-concepts/blueprints) that specify their structure, validation rules, and data types. They provide the fundamental building blocks for organizing data within the Flatfile platform.

## Basic Blueprint Structure

* A [Blueprint](/core-concepts/blueprints) defines the data structure for any number of [Spaces](/core-concepts/spaces)
* A [Space](/core-concepts/blueprints) may contain many [Workbooks](/core-concepts/workbooks) and many [Documents](/core-concepts/documents)
* A [Document](/core-concepts/documents) contains static documentation and may contain many [Document-level Actions](/guides/using-actions#document-actions)
* A [Workbook](/core-concepts/workbooks) may contain many [Sheets](/core-concepts/sheets) and many [Workbook-level Actions](/guides/using-actions#workbook-actions)
* A [Sheet](/core-concepts/sheets) may contain many [Fields](/core-concepts/fields) and many [Sheet-level Actions](/guides/using-actions#sheet-actions)
* A [Field](/core-concepts/fields) defines a single column of data, and may contain many [Field-level Actions](/guides/using-actions#field-actions)

## Basic Sheet Definition

The following examples demonstrate the configuration of isolated Sheets, which are intended to be used in the context of a [Workbook](/core-concepts/workbooks) configuration.

### Single-Sheet Sheet Configuration

This example configures a single [Sheet](/core-concepts/sheets) containing three [Fields](/core-concepts/fields) and one [Action](/core-concepts/actions) and defining [access controls](#sheet-level-access).

```javascript  theme={null}
const customerSheet = {
  name: "Customers",
  slug: "customers",
  fields: [
    {
      key: "firstName",
      type: "string",
      label: "First Name",
      constraints: [{ type: "required" }],
    },
    {
      key: "email",
      type: "string",
      label: "Email Address",
      constraints: [{ type: "required" }, { type: "unique" }],
    },
    {
      key: "company",
      type: "string",
      label: "Company Name",
    },
  ],
  access: ["add", "edit", "delete"],
  actions: [
    {
      operation: "validate-inventory",
      mode: "background",
      label: "Validate Inventory",
      description: "Check product availability against inventory system",
    },
  ],
};
```

## Sheet level access

With `access` you can control Sheet-level access for users.

| Access Level      | Description                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| `"*"` *(default)* | A user can use all access actions to this Sheet                                                 |
| `"add"`           | A user can add a record(s) to the Sheet                                                         |
| `"delete"`        | A user can delete record(s) from the Sheet                                                      |
| `"edit"`          | A user can edit records (field values) in the Sheet                                             |
| `"import"`        | A user can import CSVs to this Sheet                                                            |
| `<empty>`         | If no parameters are specified in the access array, sheet-level readOnly access will be applied |

<Warning>
  {" "}

  If you use `"*"` access control, users will gain new functionalities as we expand
  access controls. Use an exhaustive list today to block future functionality from
  being added automatically.
</Warning>

```javascript  theme={null}
{
  "sheets": [
    {
      "name": "Contacts",
      "slug": "contacts",
      "access": ["add", "edit"]
      // Define fields
    }
  ]
}
```

## Sheet Constraints

Sheet constraints apply validation rules across multiple fields or entire sheets. These constraints ensure data integrity at the sheet level and work in conjunction with field-level constraints.

### Composite Uniqueness

Ensures that combinations of multiple field values are unique across all records in the sheet. This is useful when individual fields can have duplicate values, but their combination should be unique.

```javascript  theme={null}
{
  name: "Customers",
  slug: "customers",
  constraints: [
    {
      name: "unique-customer-location",
      type: "unique",
      fields: ["customerId", "locationId"],
      requiredFields: ["customerId"], // Only enforce when customerId has a value
      strategy: "concat",
      config: {
        message: "Customers must be unique per location",
        level: "error"
      }
    }
  ],
  fields: [
    // field definitions
  ]
}
```

#### Configuration Properties

| Property         | Type      | Required | Description                                                                          |
| ---------------- | --------- | -------- | ------------------------------------------------------------------------------------ |
| `name`           | string    | ✓        | Unique identifier for the constraint                                                 |
| `type`           | string    | ✓        | Must be `"unique"` for composite uniqueness constraints                              |
| `fields`         | string\[] | ✓        | Array of field names that must be unique together                                    |
| `requiredFields` | string\[] |          | Subset of `fields` that when empty, disables constraint validation                   |
| `strategy`       | string    | ✓        | Either `"concat"` or `"hash"` - determines how uniqueness is calculated              |
| `config`         | object    |          | Configuration options for the validation message and level when the constraint fails |

**Strategy Options:**

| Strategy | Description                                            | Best Used When                                             |
| -------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| `concat` | Concatenates field values to determine uniqueness      | Simple field types, debugging needed, performance critical |
| `hash`   | Uses SHA1 hash of combined field values for uniqueness | Complex values, collision avoidance, data privacy          |

**Config Options:**

| Key       | Type   | Description                                                                                                           |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| `message` | string | The message shown to the user if this constraint is violated. Defaults to "Composite \<constraint name> is not unique |
| `level`   | string | The error level when this constraint is violated. Must be one of `"error"` (default), `"warn"` or `"info`".           |

#### Choosing the Right Strategy

The `strategy` property determines how uniqueness is calculated. You can choose to simply concatenate the field values as a single string or use a SHA1 hash function to create a unique identifier. Consider the following when choosing a strategy:

**Use `concat` when:**

* You aren't concerned about concatenation collisions (see example below)
* Performance is critical (string concatenation is faster than SHA1)
* You have short/consistent value sizes

**Use `hash` when:**

* You want to avoid concatenation collisions
* You aren't concerned about the performance cost (SHA1 calculation is slower than string concatenation)
* You have long/inconsistent value sizes (SHA1 hashes are always 20 bytes)

**Concatenation Collision Example:**

In this example, the `concat` strategy would consider the following records to be duplicates:

<CardGroup cols={2}>
  <Card>
    ```json  theme={null}
      {
        "firstName": "John",
        "lastName": "Smith"
      }
    ```
  </Card>

  <Card>
    ```json  theme={null}
      {
        "firstName": "JohnS",
        "lastName": "mith"
      }
    ```
  </Card>
</CardGroup>

Constraint configuration with `concat` strategy:

```javascript  theme={null}
{
  // sheet configuration
  constraints: [
    {
      name: "unique-name-combination",
      type: "unique",
      fields: ["firstName", "lastName"],
      strategy: "concat"
    }
  ]
}
```

This is because both records have the same concatenated value:

```javascript  theme={null}
"John" + "Smith" = "JohnSmith"
"JohnS" + "mith" = "JohnSmith"
```

But the `hash` strategy would prevent this, because the hash function creates a unique identifier based on each field's invividual value rather than a simple concatenation.

```javascript  theme={null}
hash(["John", "Smith"]) = "9e03c21f9beff9d943843c1b0623848fe63e2beb"
hash(["JohnS", "mith"]) = "2fd09d2f5e62d980988094b43640966a3bffbde9"
```

Constraint configuration with `hash` strategy:

```javascript  theme={null}
{
  // sheet configuration
  constraints: [
    {
      name: "unique-name-combination",
      type: "unique",
      fields: ["firstName", "lastName"],
      strategy: "hash" // Prevents collision
    }
  ]
}
```

#### Conditional Validation with Required Fields

The `requiredFields` property enables conditional uniqueness validation. When any field specified in `requiredFields` is empty (null, undefined, or empty string), the entire constraint is ignored for that record.

**Use Cases:**

* **Partial data imports** - Allow incomplete records during staged import processes
* **Optional relationships** - Handle cases where some composite key fields are optional
* **Data migration** - Gradually enforce constraints as required fields get populated
* **Conditional business rules** - Only enforce uniqueness when critical fields have values

**Important Notes:**

* `requiredFields` should contain only fields that exist in the `fields` array
* If ANY required field is empty, the constraint is completely ignored
* Empty fields are: `null`, `undefined`, or empty strings (`""`)
* If `requiredFields` is omitted, the constraint always applies

#### Example: Customer Registration System

Consider a customer registration system where you want unique combinations of email and company, but only when `email` is provided:

```javascript  theme={null}
{
  name: "unique-customer-profile",
  type: "unique",
  fields: ["email", "company"],
  requiredFields: ["email"], // Only enforce when email exists
  strategy: "hash"
}
```

**Data Behavior:**

| Email             | Company       | Validation Result | Reason                               |
| ----------------- | ------------- | ----------------- | ------------------------------------ |
| `"john@acme.com"` | `"Acme Corp"` | ✅ Enforced        | Email provided                       |
| `"jane@acme.com"` | `"Acme Corp"` | ❌ Duplicate       | Same email+company combination       |
| `""`              | `"Acme Corp"` | ⏭️ Ignored        | Email empty (required field)         |
| `null`            | `"Beta Inc"`  | ⏭️ Ignored        | Email null (required field)          |
| `"bob@beta.com"`  | `""`          | ✅ Enforced        | Email provided, company can be empty |

**Without `requiredFields`:**
All records would be validated, potentially causing errors during partial data imports.

#### Example: Multiple Required Fields

For more complex scenarios, you can specify multiple required fields:

```javascript  theme={null}
{
  name: "unique-order-item",
  type: "unique",
  fields: ["orderId", "productId", "customerId"],
  requiredFields: ["orderId", "productId"], // Both must have values
  strategy: "hash"
}
```

In this case, the constraint only applies when **both** `orderId` and `productId` have non-empty values. If either is empty, the entire constraint is ignored.

<Info>
  Individual field constraints like required and unique are covered in [Field Constraints](/core-concepts/fields#field-constraints).
</Info>

## Collections

Collections provide a way to organize Sheets within a Workbook into named groupings in the Flatfile UI. This helps to visually organize complex Workbooks with many Sheets, making it easier to navigate and understand the data structure. Collections have no functional impact on the data itself; their only purpose is to help you organize your Sheets visually.

### Configuring Sheets with Collections

Assigning a Collection to a Sheet is as simple as adding a `collection` property to your Sheet [Blueprint](/core-concepts/blueprints) when [configuring your Space](/core-concepts/spaces#space-configuration) (or otherwise creating or updating a Sheet via the API). If you add the same Collection to multiple Sheets, they will be grouped together in the UI.

The following example depicts a Blueprint defining a single Workbook with three Sheets organized into two Collections: **Source Data** with one Sheet, and **Processed** with two Sheets.

<Info>
  Workbooks also have a similar feature called [Folders](/core-concepts/workbooks#folders), which you can use to group associated Workbooks.

  You can think of **Folders** and **Collections** like a filing system:

  * [Folders](/core-concepts/workbooks#folders) help you organize your Workbooks within a Space (like organizing binders on a shelf)
  * **Collections** help you organize Sheets within each Workbook (like organizing tabs within a binder).
</Info>

<Tabs>
  <Tab title="Screenshot">
    <Frame caption="An example of Sheets grouped by Collection">
      <img src="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=2ac77c2216674308523e84c57f8f1c90" data-og-width="1690" width="1690" data-og-height="1420" height="1420" data-path="core-concepts/assets/sheet-collections.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?w=280&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c532c9f5cbf99203a2afe73ec8fd5d05 280w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?w=560&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=c5df586d515299a86f1a2769bfc3b87c 560w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?w=840&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=e69d56e86669ee973afc5379ec062a04 840w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?w=1100&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=2e7d5fd0bd00aa7884dd7d9d93b2d925 1100w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?w=1650&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=73ecf5d9c5fd1603c930cb4c960f1bff 1650w, https://mintcdn.com/flatfileinc/JzFdJ3ksHuS-ooTQ/core-concepts/assets/sheet-collections.png?w=2500&fit=max&auto=format&n=JzFdJ3ksHuS-ooTQ&q=85&s=4bf5dfa56e4c8c96dad30cfcb7db3a80 2500w" />
    </Frame>
  </Tab>

  <Tab title="Blueprints">
    ```javascript  theme={null}
    const workbook = {
      name: "Data Processing Pipeline",
      sheets: [
        {
          name: "Raw Customer Data",
          collection: "Source Data", // Assign to "Source Data" collection (only Sheet)
          slug: "raw_customers",
          fields: [
            { key: "name", type: "string", label: "Customer Name" },
            { key: "email", type: "string", label: "Email Address" }
          ]
        },
        {
          name: "Processed Customers",
          collection: "Processed", // Assign to "Processed" collection (first Sheet)
          slug: "clean_customers", 
          fields: [
            { key: "name", type: "string", label: "Full Name" },
            { key: "email", type: "string", label: "Email" },
            { key: "validation_status", type: "string", label: "Status" }
          ]
        },
        {
          name: "Customer Reports", 
          collection: "Processed", // Assign to "Processed" collection (second Sheet)
          slug: "customer_reports",
          fields: [
            { key: "metric", type: "string", label: "Metric Name" },
            { key: "value", type: "number", label: "Value" }
          ]
        }
      ]
    };
    ```
  </Tab>
</Tabs>

## Sheet Treatments

Sheets have an optional `treatments` parameter which takes an array of treatments for your Sheet. Treatments can be used to categorize your Sheet and control its behavior. Certain treatments will cause your Sheet to look or behave differently.

### Reference sheets

Giving your Sheet a treatment of `"ENUM_REFERENCE"` will mark it as reference data for other sheets. Reference sheets are currently hidden from view, allowing you to generate a number of reference values without adding visual distraction for the user.

<Note>
  **Dynamic Enums**

  This feature, along with the [Reference Field Filtering](/core-concepts/fields#reference-field-filtering) feature, may be collectively referred to as **Dynamic Enums**. By combining these two features, you can create a drop-down list for any cell in your sheet that's dynamically controlled by the value of another field in the same record – and to the end-user, it will just work like a dynamically-configured `enum` field.
</Note>

<Warning>
  Please note that this feature is not intended for situations where PII or other sensitive data must be hidden from view of the user - for situations like that, reach out to support or your CSM for best practices.
</Warning>

```javascript  theme={null}
const referenceSheet = {
  name: "Countries",
  slug: "countries",
  treatments: ["ENUM_REFERENCE"],
  fields: [
    {
      key: "code",
      type: "string",
      label: "Country Code"
    },
    {
      key: "name",
      type: "string",
      label: "Country Name"
    }
  ]
};
```

Currently, `"ENUM_REFERENCE"` is the only treatment that changes the behavior of your Sheet.

## Sheet Options

Configurable properties for a Sheet that control its behavior and appearance:

| Option                         | Type    | Required | Description                                                                                                                                                                                             |
| ------------------------------ | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **name**                       | string  | ✓        | The name of your Sheet as it will appear to your end users                                                                                                                                              |
| **description**                | string  |          | A sentence or two describing the purpose of your Sheet                                                                                                                                                  |
| **slug**                       | string  |          | A unique identifier for your Sheet. Used to reference your Sheet in code, for example in a Record Hook                                                                                                  |
| **readonly**                   | boolean |          | A boolean specifying whether or not this sheet is read only. Read only sheets are not editable by end users                                                                                             |
| **allowAdditionalFields**      | boolean |          | When set to `true`, your Sheet will accept additional fields beyond what you specify in its configuration. These additional fields can be added via API, or by end users during the file import process |
| **access**                     | array   |          | An array specifying the access controls for this Sheet. Valid values: `"*"`, `"add"`, `"edit"`, `"delete"`, `"import"`. [Read more about access controls](#sheet-level-access)                          |
| **fields**                     | array   | ✓        | This is where you define your Sheet's data schema. The collection of fields in your Sheet determines the shape of data you wish to accept (minimum: 1, maximum: 1000)                                   |
| **actions**                    | array   |          | An array of actions that end users can perform on this Sheet. [Read more about actions](/core-concepts/actions)                                                                                         |
| **constraints**                | array   |          | An array of sheet-level validation constraints that apply across multiple fields or entire sheets. [Read more about sheet constraints](#sheet-constraints)                                              |
| **metadata**                   | object  |          | Use `metadata` to store any extra contextual information about your Sheet. Must be valid JSON                                                                                                           |
| **mappingConfidenceThreshold** | number  |          | Configure the minimum required confidence for mapping jobs targeting that Sheet (default: 0.5, range: 0-1)                                                                                              |
