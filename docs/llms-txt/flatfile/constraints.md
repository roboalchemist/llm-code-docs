# Source: https://flatfile.com/docs/plugins/constraints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Constraints Plugin

> Extend Flatfile validation capabilities with custom validation logic for complex field and sheet-level constraints

The Constraints plugin extends Flatfile's validation capabilities by allowing developers to define custom validation logic, called "external constraints," within a listener. These custom rules can then be applied to specific fields or to the entire sheet through the blueprint configuration.

The main purpose is to handle complex validation scenarios that are not covered by Flatfile's standard built-in constraints. Use cases include:

* Field-level validation based on complex logic (e.g., checking a value's format against a specific regular expression not available by default)
* Cross-field validation where the validity of one field depends on the value of another (e.g., ensuring 'endDate' is after 'startDate')
* Validating data against an external system or API (e.g., checking if a product SKU exists in an external database)
* Applying a single validation rule to multiple fields simultaneously

The plugin works by matching a `validator` key in the blueprint with a corresponding handler registered in the listener.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-constraints
```

## Configuration & Parameters

Configuration for this plugin is not set on the plugin itself, but within the Sheet's blueprint configuration. The plugin reads this blueprint to apply the correct logic.

### Field-Level Constraints

For field-level constraints (used with `externalConstraint`), add a constraint object to a field's `constraints` array:

| Parameter   | Type   | Required | Description                                                                              |
| ----------- | ------ | -------- | ---------------------------------------------------------------------------------------- |
| `type`      | string | Yes      | Must be set to 'external' to indicate it's a custom validation rule                      |
| `validator` | string | Yes      | A unique name for your validator used to link the blueprint rule to the validation logic |
| `config`    | object | No       | An arbitrary object containing any parameters or settings your validation logic needs    |

### Sheet-Level Constraints

For sheet-level constraints (used with `externalSheetConstraint`), add a constraint object to the sheet's top-level `constraints` array:

| Parameter   | Type      | Required | Description                                                 |
| ----------- | --------- | -------- | ----------------------------------------------------------- |
| `type`      | string    | Yes      | Must be set to 'external'                                   |
| `validator` | string    | Yes      | A unique name for your sheet-level validator                |
| `fields`    | string\[] | Yes      | An array of field keys that this constraint applies to      |
| `config`    | object    | No       | An arbitrary object with settings for your validation logic |

### Default Behavior

If no `external` type constraints are defined in the blueprint, the plugin will have no effect. The validation logic only runs when a matching `validator` is found in the blueprint for the current sheet.

## Usage Examples

### Basic Field-Level Constraint

<CodeGroup>
  ```javascript JavaScript theme={null}
  // In your listener file (e.g., index.js)
  import { listener } from '@flatfile/listener'
  import { externalConstraint } from '@flatfile/plugin-constraints'

  listener.use(
    externalConstraint('minLength', (value, key, { config, record }) => {
      if (typeof value === 'string' && value.length < config.len) {
        record.addError(key, `Must be at least ${config.len} characters.`)
      }
    })
  )

  // In your blueprint file (e.g., workbook.js)
  const blueprint = {
    sheets: [
      {
        name: 'Promotions',
        slug: 'promos',
        fields: [
          {
            key: 'promo_code',
            type: 'string',
            label: 'Promo Code',
            constraints: [
              { type: 'external', validator: 'minLength', config: { len: 8 } },
            ],
          },
        ],
      },
    ],
  }
  ```

  ```typescript TypeScript theme={null}
  // In your listener file (e.g., index.ts)
  import { listener } from '@flatfile/listener'
  import { externalConstraint } from '@flatfile/plugin-constraints'

  listener.use(
    externalConstraint('minLength', (value, key, { config, record }) => {
      if (typeof value === 'string' && value.length < config.len) {
        record.addError(key, `Must be at least ${config.len} characters.`)
      }
    })
  )

  // In your blueprint file (e.g., workbook.ts)
  const blueprint = {
    sheets: [
      {
        name: 'Promotions',
        slug: 'promos',
        fields: [
          {
            key: 'promo_code',
            type: 'string',
            label: 'Promo Code',
            constraints: [
              { type: 'external', validator: 'minLength', config: { len: 8 } },
            ],
          },
        ],
      },
    ],
  }
  ```
</CodeGroup>

### Configurable Constraint

<CodeGroup>
  ```javascript JavaScript theme={null}
  // In your listener file (e.g., index.js)
  import { listener } from '@flatfile/listener'
  import { externalConstraint } from '@flatfile/plugin-constraints'

  // This 'length' validator can be used for min or max length checks
  listener.use(
    externalConstraint('length', (value, key, { config, record }) => {
      if (typeof value !== 'string') return

      if (config.max && value.length > config.max) {
        record.addError(key, `Text must be under ${config.max} characters.`)
      }
      if (config.min && value.length < config.min) {
        record.addError(key, `Text must be over ${config.min} characters.`)
      }
    })
  )

  // In your blueprint file (e.g., workbook.js)
  const blueprint = {
    sheets: [
      {
        name: 'Content',
        slug: 'content',
        fields: [
          {
            key: 'title',
            type: 'string',
            label: 'Title',
            constraints: [
              { type: 'external', validator: 'length', config: { max: 50 } },
            ],
          },
          {
            key: 'description',
            type: 'string',
            label: 'Description',
            constraints: [
              { type: 'external', validator: 'length', config: { min: 10 } },
            ],
          },
        ],
      },
    ],
  }
  ```

  ```typescript TypeScript theme={null}
  // In your listener file (e.g., index.ts)
  import { listener } from '@flatfile/listener'
  import { externalConstraint } from '@flatfile/plugin-constraints'

  // This 'length' validator can be used for min or max length checks
  listener.use(
    externalConstraint('length', (value, key, { config, record }) => {
      if (typeof value !== 'string') return

      if (config.max && value.length > config.max) {
        record.addError(key, `Text must be under ${config.max} characters.`)
      }
      if (config.min && value.length < config.min) {
        record.addError(key, `Text must be over ${config.min} characters.`)
      }
    })
  )

  // In your blueprint file (e.g., workbook.ts)
  const blueprint = {
    sheets: [
      {
        name: 'Content',
        slug: 'content',
        fields: [
          {
            key: 'title',
            type: 'string',
            label: 'Title',
            constraints: [
              { type: 'external', validator: 'length', config: { max: 50 } },
            ],
          },
          {
            key: 'description',
            type: 'string',
            label: 'Description',
            constraints: [
              { type: 'external', validator: 'length', config: { min: 10 } },
            ],
          },
        ],
      },
    ],
  }
  ```
</CodeGroup>

### Sheet-Level Constraint

<CodeGroup>
  ```javascript JavaScript theme={null}
  // In your listener file (e.g., index.js)
  import { listener } from '@flatfile/listener'
  import { externalSheetConstraint } from '@flatfile/plugin-constraints'

  listener.use(
    externalSheetConstraint('contact-required', (values, keys, { record }) => {
      if (!values.email && !values.phone) {
        const message = 'Either Email or Phone must be provided.'
        // Add the error to both fields
        keys.forEach((key) => record.addError(key, message))
      }
    })
  )

  // In your blueprint file (e.g., workbook.js)
  const blueprint = {
    sheets: [
      {
        name: 'Contacts',
        slug: 'contacts',
        fields: [
          { key: 'email', type: 'string', label: 'Email' },
          { key: 'phone', type: 'string', label: 'Phone' },
        ],
        constraints: [
          {
            type: 'external',
            validator: 'contact-required',
            fields: ['email', 'phone'],
          },
        ],
      },
    ],
  }
  ```

  ```typescript TypeScript theme={null}
  // In your listener file (e.g., index.ts)
  import { listener } from '@flatfile/listener'
  import { externalSheetConstraint } from '@flatfile/plugin-constraints'

  listener.use(
    externalSheetConstraint('contact-required', (values, keys, { record }) => {
      if (!values.email && !values.phone) {
        const message = 'Either Email or Phone must be provided.'
        // Add the error to both fields
        keys.forEach((key) => record.addError(key, message))
      }
    })
  )

  // In your blueprint file (e.g., workbook.ts)
  const blueprint = {
    sheets: [
      {
        name: 'Contacts',
        slug: 'contacts',
        fields: [
          { key: 'email', type: 'string', label: 'Email' },
          { key: 'phone', type: 'string', label: 'Phone' },
        ],
        constraints: [
          {
            type: 'external',
            validator: 'contact-required',
            fields: ['email', 'phone'],
          },
        ],
      },
    ],
  }
  ```
</CodeGroup>

## API Reference

### externalConstraint

Registers a listener for a field-level custom validation rule. The provided callback function will be executed for every record on each field that has a matching `external` constraint in the blueprint.

**Signature:**

```typescript  theme={null}
externalConstraint(
  validator: string, 
  cb: (
    value: any, 
    key: string, 
    support: { 
      config: any, 
      record: FlatfileRecord, 
      property: Flatfile.Property, 
      event: FlatfileEvent 
    }
  ) => any | Promise<any>
)
```

**Parameters:**

* `validator` (string): The name of the validator. This must match the `validator` property in the field's constraint configuration in the blueprint.
* `cb` (function): A callback function that contains the validation logic. It receives:
  * `value` (any): The value of the cell being validated
  * `key` (string): The key of the field being validated
  * `support` (object): An object containing helpful context:
    * `config` (any): The `config` object from the blueprint constraint
    * `record` (FlatfileRecord): The full record object, which can be used to get other values or add errors
    * `property` (Flatfile.Property): The full property (field) definition from the sheet schema
    * `event` (FlatfileEvent): The raw event that triggered the validation

**Error Handling Examples:**

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Using record.addError() (Recommended)
  listener.use(
    externalConstraint('must-be-positive', (value, key, { record }) => {
      if (typeof value === 'number' && value <= 0) {
        record.addError(key, 'Value must be a positive number.')
      }
    })
  )

  // Throwing an Error
  listener.use(
    externalConstraint('must-be-positive', (value) => {
      if (typeof value === 'number' && value <= 0) {
        throw 'Value must be a positive number.'
      }
    })
  )
  ```

  ```typescript TypeScript theme={null}
  // Using record.addError() (Recommended)
  listener.use(
    externalConstraint('must-be-positive', (value, key, { record }) => {
      if (typeof value === 'number' && value <= 0) {
        record.addError(key, 'Value must be a positive number.')
      }
    })
  )

  // Throwing an Error
  listener.use(
    externalConstraint('must-be-positive', (value) => {
      if (typeof value === 'number' && value <= 0) {
        throw 'Value must be a positive number.'
      }
    })
  )
  ```
</CodeGroup>

### externalSheetConstraint

Registers a listener for a sheet-level custom validation rule that involves multiple fields. The callback is executed once per record for each matching `external` constraint in the sheet's top-level `constraints` array.

**Signature:**

```typescript  theme={null}
externalSheetConstraint(
  validator: string, 
  cb: (
    values: Record<string, TRecordValue>, 
    keys: string[], 
    support: { 
      config: any, 
      record: FlatfileRecord, 
      properties: Flatfile.Property[], 
      event: FlatfileEvent 
    }
  ) => any | Promise<any>
)
```

**Parameters:**

* `validator` (string): The name of the validator. This must match the `validator` property in the sheet's constraint configuration.
* `cb` (function): A callback function that contains the validation logic. It receives:
  * `values` (Record\<string, TRecordValue>): An object where keys are the field keys from the constraint's `fields` array and values are the corresponding cell values for the current record
  * `keys` (string\[]): An array of the field keys this constraint applies to (from the `fields` property in the blueprint)
  * `support` (object): An object containing helpful context:
    * `config` (any): The `config` object from the blueprint constraint
    * `record` (FlatfileRecord): The full record object
    * `properties` (Flatfile.Property\[]): An array of the full property (field) definitions for the fields involved in this constraint
    * `event` (FlatfileEvent): The raw event that triggered the validation

**Error Handling Examples:**

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Using record.addError() - allows different error messages for different fields
  listener.use(
    externalSheetConstraint('date-range', (values, keys, { record }) => {
      if (values.startDate && values.endDate && values.startDate > values.endDate) {
        record.addError('startDate', 'Start date must be before end date.')
        record.addError('endDate', 'End date must be after start date.')
      }
    })
  )

  // Throwing an Error - applies same error message to ALL fields
  listener.use(
    externalSheetConstraint('date-range', (values) => {
      if (values.startDate && values.endDate && values.startDate > values.endDate) {
        throw 'Start date must be before end date.'
      }
    })
  )
  ```

  ```typescript TypeScript theme={null}
  // Using record.addError() - allows different error messages for different fields
  listener.use(
    externalSheetConstraint('date-range', (values, keys, { record }) => {
      if (values.startDate && values.endDate && values.startDate > values.endDate) {
        record.addError('startDate', 'Start date must be before end date.')
        record.addError('endDate', 'End date must be after start date.')
      }
    })
  )

  // Throwing an Error - applies same error message to ALL fields
  listener.use(
    externalSheetConstraint('date-range', (values) => {
      if (values.startDate && values.endDate && values.startDate > values.endDate) {
        throw 'Start date must be before end date.'
      }
    })
  )
  ```
</CodeGroup>

## Troubleshooting

* **Validator Not Firing:** Ensure the `validator` string in your blueprint constraint exactly matches the string you passed to `externalConstraint` or `externalSheetConstraint` in your listener.
* **Constraint Not Recognized:** Double-check that the constraint object in your blueprint has `type: 'external'`.
* **Sheet Constraint Issues:** For `externalSheetConstraint`, make sure the sheet-level constraint in the blueprint includes the `fields` array, listing the keys of all fields involved in the validation.

## Notes

### Special Considerations

* The plugin fetches and caches the sheet schema (blueprint) once per data submission (`commit:created` event). For very high-frequency operations, this could be a performance consideration, but for most use cases, it is not an issue.
* The plugin relies on `@flatfile/plugin-record-hook` to process records in bulk.

### Error Handling Patterns

The plugin supports two primary error handling patterns within the validation callback:

1. **Imperative:** Call `record.addError(key, message)` to add an error to a specific field. This is useful for sheet-level constraints where you might want to flag only one of the involved fields.
2. **Declarative:** `throw new Error(message)` or `throw "message"`. The plugin will catch the thrown error. For `externalConstraint`, the error is added to the field being validated. For `externalSheetConstraint`, the same error message is added to *all* fields listed in the constraint's `fields` array.
