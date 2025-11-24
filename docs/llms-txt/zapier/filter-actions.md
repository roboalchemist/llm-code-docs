# Source: https://docs.zapier.com/powered-by-zapier/zap-creation/filter-actions.md

# Filter Actions

> Learn how to configure Filter by Zapier actions to control workflow execution based on conditions.

<Info>
  This guide assumes familiarity with building workflows. For an introduction,
  see [How to Build a
  Workflow](/powered-by-zapier/zap-creation/how-to-build-a-workflow). For
  details on working with input fields, see [Fields and
  Fieldsets](/powered-by-zapier/zap-creation/fields-and-fieldsets).
</Info>

Filter by Zapier is an app that allows you to add conditional logic to your workflows. With it, you can specify conditions that must be met for the workflow to continue. This is particularly useful when you only want certain data to trigger subsequent actions. For example, only continuing if an email is from a specific sender, or if a lead's status meets certain criteria.

Filter actions work within the standard workflow paradigm described in [How to Build a Workflow](/powered-by-zapier/zap-creation/how-to-build-a-workflow). While Filter by Zapier is useful enough to warrant its own example, it doesn't require any special handling compared to other apps and actions.

***

# Example: Adding a Filter Step

Let's walk through an example of adding a filter step to a workflow. We'll assume you've already configured a first step as described in [How to Build a Workflow](/powered-by-zapier/zap-creation/how-to-build-a-workflow). For this example, let's say it's a "New Email in Gmail" trigger.

### Finding the Filter by Zapier App

First, we need to find the Filter by Zapier app. You can search for it using the [GET /v2/apps](/powered-by-zapier/api-reference/apps/get-apps-\[v2]) endpoint:

```js  theme={null}
GET /v2/apps?query=filter
```

<CodeGroup>
  ```js Response theme={null}
  {
    "data": [
      {
        "id": "e85bcf45-505b-4acb-b7e8-4c3a81d49afb",
        "type": "app",
        "image": "https://zapier-images.imgix.net/storage/services/ad3d7962908c17bcbe753928e8786b4a.png",
        "action_types": [],
        "title": "Filter by Zapier",
        "images": {
          "url_16x16": "https://zapier-images.imgix.net/storage/services/ad3d7962908c17bcbe753928e8786b4a.png?auto=format%2Ccompress&fit=crop&h=16&ixlib=python-3.0.0&q=50&w=16",
          "url_32x32": "https://zapier-images.imgix.net/storage/services/ad3d7962908c17bcbe753928e8786b4a.png?auto=format%2Ccompress&fit=crop&h=32&ixlib=python-3.0.0&q=50&w=32",
          "url_64x64": "https://zapier-images.imgix.net/storage/services/ad3d7962908c17bcbe753928e8786b4a.png?auto=format%2Ccompress&fit=crop&h=64&ixlib=python-3.0.0&q=50&w=64",
          "url_128x128": "https://zapier-images.imgix.net/storage/services/ad3d7962908c17bcbe753928e8786b4a.png?auto=format%2Ccompress&fit=crop&h=128&ixlib=python-3.0.0&q=50&w=128"
        },
        "hex_color": "ff4a00",
        "categories": [
          {
            "slug": "developer-tools"
          },
          {
            "slug": "zapier-tools"
          }
        ],
        "description": "Only allow a Zap to proceed when a certain condition is met. For example, if you're sending a text message when you receive a new email, you could use a Filter that only sends a text message when the email received is from a certain address."
      }
    ]
  }
  ```
</CodeGroup>

Take note of the app `id`: `e85bcf45-505b-4acb-b7e8-4c3a81d49afb`. We'll use this in the next step.

### Getting the Filter Action

Now that we have the app ID, we can retrieve the filter action using the [GET /v2/actions](/powered-by-zapier/api-reference/actions/get-actions) endpoint with `action_type=FILTER`:

```js  theme={null}
GET /v2/actions?app=e85bcf45-505b-4acb-b7e8-4c3a81d49afb&action_type=FILTER
```

<CodeGroup>
  ```js Response theme={null}
  {
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "count": 1,
      "limit": null,
      "offset": null
    },
    "data": [
      {
        "id": "core:example_filter_action_id",
        "key": "filter",
        "app": "e85bcf45-505b-4acb-b7e8-4c3a81d49afb",
        "type": "action",
        "action_type": "FILTER",
        "is_instant": false,
        "title": "Only continue if...",
        "description": "Set up rules to specify when this Zap can continue running."
      }
    ]
  }
  ```
</CodeGroup>

The filter action has the `action_type` of `FILTER`, which distinguishes it from standard `READ` and `WRITE` actions.

### Configuring Filter Inputs

To get the available inputs, make a request to the [POST /v2/actions/\{action\_id}/inputs](/powered-by-zapier/api-reference/actions/get-input-fields) endpoint:

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/inputs
  {
    "data": {
      "authentication": null,
      "inputs": {}
    }
  }
  ```

  ```js Response theme={null}
  {
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "count": 2,
      "limit": null,
      "offset": null
    },
    "data": [
      {
        "type": "input_field",
        "id": "filter_criteria_count",
        "default_value": "1",
        "depends_on": [],
        "description": "The number of filter conditions to use",
        "format": "SELECT",
        "invalidates_input_fields": true,
        "is_required": true,
        "placeholder": "",
        "title": "Filter Condition Count",
        "value_type": "INTEGER"
      },
      {
        "type": "fieldset",
        "id": "filter_criteria_1",
        "fields": [
          {
            "type": "input_field",
            "id": "filter_criteria_1_key",
            "default_value": "",
            "depends_on": [],
            "description": "The value to filter on, which must be a single output field from a previous step",
            "invalidates_input_fields": false,
            "is_required": true,
            "placeholder": "",
            "title": "key",
            "value_type": "STRING"
          },
          {
            "type": "input_field",
            "id": "filter_criteria_1_match",
            "default_value": "",
            "depends_on": [],
            "description": "The method of comparison to use for filtering.",
            "format": "SELECT",
            "invalidates_input_fields": true,
            "is_required": true,
            "placeholder": "",
            "title": "Filter mode",
            "value_type": "STRING"
          }
        ],
        "title": "Filter Condition 1"
      }
    ]
  }
  ```
</CodeGroup>

#### Understanding Filter Criteria

Each **fieldset** in the response represents a **filter condition**. A filter condition is a single rule like "email subject contains 'urgent'" or "lead status equals 'qualified'".

By default at least one filter condition must be configured. You can increase the number of filter conditions using the `filter_criteria_count` input.

#### Filter Criteria Count

The `filter_criteria_count` input controls how many filter conditions are available. Since it has `format: "SELECT"`, we need to fetch its available choices from the [POST /v2/actions/\{action\_id}/inputs/\{input\_id}/choices](/powered-by-zapier/api-reference/actions/get-choices) endpoint:

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/inputs/filter_criteria_count/choices
  {
    "data": {
      "authentication": null,
      "inputs": {}
    }
  }
  ```

  ```js Response theme={null}
  {
    "data": [
      {
        "id": "1",
        "type": "choice",
        "label": "1",
        "value": "1"
      },
      {
        "id": "2",
        "type": "choice",
        "label": "2",
        "value": "2"
      },
      {
        "id": "3",
        "type": "choice",
        "label": "3",
        "value": "3"
      },
      {
        "id": "4",
        "type": "choice",
        "label": "4",
        "value": "4"
      },
      {
        "id": "5",
        "type": "choice",
        "label": "5",
        "value": "5"
      }
    ],
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "page": 1
    }
  }
  ```
</CodeGroup>

You can configure between 1 and 5 filter conditions.

#### Configuring Multiple Filter Conditions

When you set `filter_criteria_count` to a value greater than 1, you'll need to refetch the inputs (since `invalidates_input_fields` is `true`). Let's see what happens when we request 2 filter conditions:

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/inputs
  {
    "data": {
      "authentication": null,
      "inputs": {
        "filter_criteria_count": 2
      }
    }
  }
  ```

  ```js Response theme={null}
  {
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "count": 4,
      "limit": null,
      "offset": null
    },
    "data": [
      {
        "type": "input_field",
        "id": "filter_criteria_count",
        "default_value": "1",
        "depends_on": [],
        "description": "The number of filter conditions to use",
        "format": "SELECT",
        "invalidates_input_fields": true,
        "is_required": true,
        "placeholder": "",
        "title": "Filter Condition Count",
        "value_type": "INTEGER"
      },
      {
        "type": "input_field",
        "id": "boolean_operator",
        "default_value": "",
        "depends_on": [],
        "description": "How to combine multiple filter conditions",
        "format": "SELECT",
        "invalidates_input_fields": false,
        "is_required": true,
        "placeholder": "",
        "title": "Match Mode",
        "value_type": "STRING"
      },
      {
        "type": "fieldset",
        "id": "filter_criteria_1",
        "fields": [
          {
            "type": "input_field",
            "id": "filter_criteria_1_key",
            "default_value": "",
            "depends_on": [],
            "description": "The value to filter on, which must be a single output field from a previous step",
            "invalidates_input_fields": false,
            "is_required": true,
            "placeholder": "",
            "title": "key",
            "value_type": "STRING"
          },
          {
            "type": "input_field",
            "id": "filter_criteria_1_match",
            "default_value": "",
            "depends_on": [],
            "description": "The method of comparison to use for filtering.",
            "format": "SELECT",
            "invalidates_input_fields": true,
            "is_required": true,
            "placeholder": "",
            "title": "Filter mode",
            "value_type": "STRING"
          }
        ],
        "title": "Filter Condition 1"
      },
      {
        "type": "fieldset",
        "id": "filter_criteria_2",
        "fields": [
          {
            "type": "input_field",
            "id": "filter_criteria_2_key",
            "default_value": "",
            "depends_on": [],
            "description": "The value to filter on, which must be a single output field from a previous step",
            "invalidates_input_fields": false,
            "is_required": true,
            "placeholder": "",
            "title": "key",
            "value_type": "STRING"
          },
          {
            "type": "input_field",
            "id": "filter_criteria_2_match",
            "default_value": "",
            "depends_on": [],
            "description": "The method of comparison to use for filtering.",
            "format": "SELECT",
            "invalidates_input_fields": true,
            "is_required": true,
            "placeholder": "",
            "title": "Filter mode",
            "value_type": "STRING"
          }
        ],
        "title": "Filter Condition 2"
      }
    ]
  }
  ```
</CodeGroup>

Notice that we now have:

* A second fieldset (`filter_criteria_2`)
* A new `boolean_operator` input field

#### Boolean Operator

The `boolean_operator` input appears whenever `filter_criteria_count` is greater than 1. It determines how multiple filter conditions are combined. Let's fetch its choices:

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/inputs/boolean_operator/choices
  {
    "data": {
      "authentication": null,
      "inputs": {}
    }
  }
  ```

  ```js Response theme={null}
  {
    "data": [
      {
        "id": "and",
        "type": "choice",
        "label": "All conditions must match",
        "value": "and"
      },
      {
        "id": "or",
        "type": "choice",
        "label": "At least one condition must match",
        "value": "or"
      }
    ],
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "page": 1
    }
  }
  ```
</CodeGroup>

The `boolean_operator` allows you to specify whether:

* **All conditions must match** (`and`): The workflow continues only if every filter condition is satisfied
* **At least one condition must match** (`or`): The workflow continues if any filter condition is satisfied

#### Filter Match Rules

Each filter condition has a `filter_criteria_{n}_match` field that determines the comparison method. Since this is a `SELECT` field, we need to fetch its choices:

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/inputs/filter_criteria_1_match/choices
  {
    "data": {
      "authentication": null,
      "inputs": {}
    }
  }
  ```

  ```js Response theme={null}
  {
    "data": [
      {
        "id": "contains",
        "type": "choice",
        "label": "(Text) Contains",
        "value": "contains"
      },
      {
        "id": "does not contain",
        "type": "choice",
        "label": "(Text) Does not contain",
        "value": "does not contain"
      },
      {
        "id": "exactly matches",
        "type": "choice",
        "label": "(Text) Exactly matches",
        "value": "exactly matches"
      },
      {
        "id": "does not exactly match",
        "type": "choice",
        "label": "(Text) Does not exactly match",
        "value": "does not exactly match"
      },
      {
        "id": "is in",
        "type": "choice",
        "label": "(Text) Is in",
        "value": "is in"
      },
      {
        "id": "is not in",
        "type": "choice",
        "label": "(Text) Is not in",
        "value": "is not in"
      },
      {
        "id": "starts with",
        "type": "choice",
        "label": "(Text) Starts with",
        "value": "starts with"
      },
      {
        "id": "does not start with",
        "type": "choice",
        "label": "(Text) Does not start with",
        "value": "does not start with"
      },
      {
        "id": "ends with",
        "type": "choice",
        "label": "(Text) Ends with",
        "value": "ends with"
      },
      {
        "id": "does not end with",
        "type": "choice",
        "label": "(Text) Does not end with",
        "value": "does not end with"
      },
      {
        "id": "is greater than",
        "type": "choice",
        "label": "(Number) Greater than",
        "value": "is greater than"
      },
      {
        "id": "is less than",
        "type": "choice",
        "label": "(Number) Less than",
        "value": "is less than"
      },
      {
        "id": "is after",
        "type": "choice",
        "label": "(Date/time) After",
        "value": "is after"
      },
      {
        "id": "is before",
        "type": "choice",
        "label": "(Date/time) Before",
        "value": "is before"
      },
      {
        "id": "is the same as",
        "type": "choice",
        "label": "(Date/time) Equals",
        "value": "is the same as"
      },
      {
        "id": "is true",
        "type": "choice",
        "label": "(Boolean) Is true",
        "value": "is true"
      },
      {
        "id": "is false",
        "type": "choice",
        "label": "(Boolean) Is false",
        "value": "is false"
      },
      {
        "id": "exists",
        "type": "choice",
        "label": "Exists",
        "value": "exists"
      },
      {
        "id": "does not exist",
        "type": "choice",
        "label": "Does not exist",
        "value": "does not exist"
      }
    ],
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "page": 1
    }
  }
  ```
</CodeGroup>

The available match rules include:

* **Text comparisons**: contains, exactly matches, starts with, ends with, etc.
* **Number comparisons**: greater than, less than
* **Date/time comparisons**: after, before, equals
* **Boolean comparisons**: is true, is false
* **Existence checks**: exists, does not exist

#### The Key Field

<Warning>
  The `filter_criteria_{n}_key` field **must** contain one and only one field reference in the format `{{previous_step_alias.field_id}}` or `{{field_id}}` (for 2-step workflows). It cannot contain any other text or multiple field references.
</Warning>

For example, if your first step has an alias of `gmail_trigger` and outputs a field called `subject`, the key field should be set to:

```js  theme={null}
"filter_criteria_1_key": "{{gmail_trigger.subject}}"
```

In a 2-step workflow (where the alias is optional and implicit), you could use:

```js  theme={null}
"filter_criteria_1_key": "{{subject}}"
```

#### The Value Field

Depending on the match rule selected for `filter_criteria_{n}_match`, a `filter_criteria_{n}_value` field may be returned when you refetch the inputs. This field represents the value to compare against.

For example:

* Match rules like **"contains"**, **"exactly matches"**, or **"is greater than"** require a value to compare against, so `filter_criteria_{n}_value` will appear
* Match rules like **"exists"** or **"does not exist"** don't need a comparison value, so `filter_criteria_{n}_value` will not appear

<Note>
  Since `filter_criteria_{n}_match` has `invalidates_input_fields: true`, you'll
  need to refetch the inputs after selecting a match rule to see if a value
  field is required. For more details on this pattern, see the [invalidation and
  dependency flow
  documentation](/powered-by-zapier/zap-creation/fields-and-fieldsets#invalidation--dependancy-flow).
</Note>

### Testing a Filter Step

Once you've configured the filter inputs, you can test the filter step using the [POST /v2/actions/\{action\_id}/test](/powered-by-zapier/api-reference/actions/step-test) endpoint. Unlike actual use of the Filter, "raw" values are allowed as there is no prior/incoming field to reference.

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/test
  {
    "data": {
      "authentication": null,
      "inputs": {
        "filter_criteria_count": 2,
        "boolean_operator": "and",
        "filter_criteria_1_key": "abc",
        "filter_criteria_1_match": "exactly matches",
        "filter_criteria_1_value": "abc",
        "filter_criteria_2_key": "false",
        "filter_criteria_2_match": "is false"
      }
    }
  }
  ```

  ```js Response theme={null}
  {
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "count": 1,
      "limit": null,
      "offset": null
    },
    "data": [
      {
        "can_continue": "true"
      }
    ]
  }
  ```
</CodeGroup>

The test response includes a `can_continue` field that indicates whether the filter conditions were met. In this example, both conditions were satisfied, so the workflow would continue.

### Getting Filter Outputs

To retrieve the output fields from a filter step, use the [POST /v2/actions/\{action\_id}/outputs](/powered-by-zapier/api-reference/actions/get-output-fields) endpoint:

<CodeGroup>
  ```js Request theme={null}
  // POST /v2/actions/core:example_filter_action_id/outputs
  {
    "data": {
      "authentication": null,
      "inputs": {},
      "fetch_live_samples": true
    }
  }
  ```

  ```js Response theme={null}
  {
    "links": {
      "next": null,
      "prev": null
    },
    "meta": {
      "count": 1,
      "limit": null,
      "offset": null
    },
    "data": [
      {
        "type": "output_field",
        "id": "can_continue",
        "title": "Can Continue",
        "sample": "true"
      }
    ]
  }
  ```
</CodeGroup>

Filter steps output a single field: `can_continue`, which indicates whether the filter conditions were met. While this field can be referenced in subsequent steps, filter steps are typically used for their side effect of halting workflow execution when conditions aren't met, rather than for their output data.

## Complete Example

Here's a complete example of adding a filter step to a workflow. This workflow triggers on new Gmail emails and only continues if the email subject contains "urgent":

<CodeGroup>
  ```js Create Zap Request theme={null}
  // POST /v2/zaps
  {
    "data": {
      "enabled": true,
      "title": "Process urgent emails only",
      "steps": [
        {
          "action": "core:wJ3PxHpNArZ8MqvloW3L1ZyMDQ4nJ",
          "alias": "gmail_trigger",
          "inputs": {
            "label_id": "INBOX"
          },
          "authentication": "49509"
        },
        {
          "action": "core:example_filter_action_id",
          "alias": "filter_step",
          "authentication": null,
          "inputs": {
            "filter_criteria_count": 1,
            "filter_criteria_1_key": "{{gmail_trigger.subject}}",
            "filter_criteria_1_match": "contains",
            "filter_criteria_1_value": "urgent"
          }
        },
        {
          "action": "core:3ZYFzZKkjbDK2AwQopVqrZWL9pK",
          "inputs": {
            "message": "Urgent email received: {{gmail_trigger.subject}}"
          },
          "authentication": "857610"
        }
      ]
    }
  }
  ```
</CodeGroup>

<Info>
  Note that filter steps don't require authentication, so the `authentication`
  field is always set to `null`.
</Info>

When this workflow runs, step 2 will evaluate whether the email subject contains "urgent". If it does, the workflow continues to step 3. If it doesn't, the workflow stops and step 3 never executes.
