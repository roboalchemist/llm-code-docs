# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/setup-ui-for-action/advanced-form-configurations.md

# Advanced input configurations

Advanced input settings allow you to create more customizable experiences for users who perform self-service actions. This is done by creating adaptive inputs that change according to data about the entity, the user, and other inputs.

## Common use-cases[â](#common-use-cases "Direct link to Common use-cases")

* Filter the available options in a dropdown input.
* Create a dependency between inputs to allow the user to select a value based on the value of another input.
* Define dynamic default values based on the logged-in user properties(such as teams, email, role) or the entity that the action is being executed on (for day-2 or delete actions only).

Pulumi Examples' Language

Unless otherwise specified, all **Pulumi** configuration examples are provided in Python. For usage in other languages, please see the Pulumi provider documentation [here](https://www.pulumi.com/registry/packages/port/api-docs/action/).

## Usage[â](#usage "Direct link to Usage")

Defining advanced inputs is currently supported in JSON-mode only.

When creating an action, the second step is defining its inputs. After defining at least one input, an `Advanced configuration` section will appear in the bottom of the form. Click on `Edit JSON`, then add your configuration in JSON format.

![](/img/self-service-actions/advancedInputsFormExample.png)

### Writing your configuration schema[â](#writing-your-configuration-schema "Direct link to Writing your configuration schema")

Port provides a `jqQuery` property that can be used to extract data from the entity, the logged-in user, or the current action's form inputs. It can also be used to perform data manipulations.

For example, the following `jqQuery` checks the value of another property (`language`) and determines the possible values of the `SDK` property accordingly:

```
{
  "properties": {
    "language": {
      "type": "string",
      "enum": ["javascript", "python"]
    },
    "SDK": {
      "type": "string",
      "enum": {
        "jqQuery": "if .form.language == \"javascript\" then [\"Node 16\", \"Node 18\"] else [\"Python 3.8\"] end"
      }
    }
  }
}
```

#### The properties you can access using the "jqQuery" object[â](#the-properties-you-can-access-using-the-jqquery-object "Direct link to The properties you can access using the \"jqQuery\" object")

* form
* entity
* user

The values of the inputs in the current action form.

Usage:

```
{
  "jqQuery": ".form.input1"
}
```

The available `form` object(each input is a key in the action's [`userInputs`](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/.md) object):

```
{
  "input1": "...",
  "input2": "...",
  "input3": "..."
}
```

The properties of the `entity` on which the action is performed. Entity data is only available in "day-2" and "delete" actions.

Usage:

```
{
  "jqQuery": ".entity.properties.property1"
}
```

The available `entity` object:

```
{
  "identifier": "...",
  "title": "...",
  "blueprint": "...",
  "team": ["..."],
  "properties": {
    "property1": "...",
    "property2": "...",
    "property3": "..."
  },
  "relations": {
    "relation1": "...",
    "relation2": "...",
    "relationMany": ["...", "..."]
  },
  "createdAt": "...",
  "createdBy": "...",
  "updatedAt": "...",
  "updatedBy": "...",
  "scorecards": {
    "ResourceQuota": {
      "rules": [
        {
          "identifier": "...",
          "status": "...",
          "level": "..."
        },
        {
          "identifier": "...",
          "status": "...",
          "level": "..."
        }
      ],
      "level": "..."
    },
    "Ownership": {
      "rules": [
        {
          "identifier": "...",
          "status": "...",
          "level": "..."
        },
        {
          "identifier": "...",
          "status": "...",
          "level": "..."
        }
      ],
      "level": "..."
    }
  }
}
```

The properties of the user that executed the action.

Usage examples:

```
{
  // Access the user's email
  "jqQuery": ".user.email"
}
```

```
{
  // Access the user's team-identifiers
  "jqQuery": "[.user.teamsIdentifiers[]]"
}
```

The available logged-in user object:

```
{
  "picture": "...",
  "userId": "...",
  "email": "...",
  "name": "...",
  "mainRole": "...",
  "roles": [
    {
      "name": "..."
    }
  ],
  "teams": [
    {
      "name": "...",
      "provider": "..."
    },
    {
      "name": "...",
      "provider": "..."
    }
  ]
}
```

Keys that are supported with jqQuery expressions:

| Key      | Description                                       |
| -------- | ------------------------------------------------- |
| enum     | any enum of a property                            |
| default  | the default value of any property                 |
| required | the properties which will be required in the form |
| value    | the value inside a "dataset" rule                 |
| visible  | the condition to display any property in the form |
| disabled | the condition to disable any property in the form |

Check if string is empty

To check if a string input is empty, compare it to an empty string, like this:

```
{
  "jqQuery": ".form.version == \"\""
}
```

***

#### Additional available properties[â](#additional-available-properties "Direct link to Additional available properties")

You can use these additional properties to create more complex inputs:

* visible
* dependsOn
* dataset
* disabled

The `visible` property is used to dynamically hide/show elements in the form. The `visible` value could be set to either a boolean (`true` value is always shown, `false` value is always hidden), or to a `jqQuery` which evaluates to a boolean.

#### Input-level visibility

You can apply `visible` to individual inputs to control their display:

In this example, the `runArguments` properties are configured with `visible` so that they only show up in the form when the matching value is selected in the `language` input:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "language": {
      "type": "string",
      "enum": ["javascript", "python"]
    },
    "pythonRunArguments": {
      "type": "string",
      "visible": {
        "jqQuery": ".form.language == \"python\""
      }
    },
    "nodeRunArguments": {
      "type": "string",
      "visible": {
        "jqQuery": ".form.language == \"javascript\""
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        language = {
          enum = ["javascript", "python"]
        }
        pythonRunArguments = {
          visible_jq_query = ".form.language == \"python\""
        }
        nodeRunArguments = {
          visible_jq_query = ".form.language == \"javascript\""
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "language": {
        "enums": ["python", "javascript"],
      },
      "pythonRunArguments": {"visible_jq_query": '.form.language == "python"'},
      "nodeRunArguments": {"visible_jq_query": '.form.language == "javascript"'},
    },
  }
)
```

#### Step-level visibility

You can also apply `visible` to entire steps to control their display:

In this example, the `AWS Configuration` and `Azure Configuration` steps are conditionally shown based on the values selected in the first step's cloud provider input:

* API

```
  {
    "userInputs": {
      "properties": {
        "enum": {
          "icon": "DefaultProperty",
          "title": "Cloud provider",
          "type": "array",
          "items": {
            "enum": [ "aws", "azure" ],
            "enumColors": { "aws": "red", "azure": "blue" },
            "type": "string"
          }
        }
      },
      "required": [],
      "steps": [
        {
          "title": "Cloud selection",
          "order": [ "enum" ]
        },
        {
          "title": "AWS configuration",
          "order": [],
          "visible": { "jqQuery": ".form.enum | index(\"aws\") != null" }
        },
        {
          "title": "Azure configuration",
          "order": [],
          "visible": { "jqQuery": ".form.enum | index(\"azure\") != null" }
        }
      ]
    }
  }
```

The `dependsOn` property is used to create a dependency between inputs. If input X depends on input Y, input X will be **disabled** until input Y is filled.<br /><!-- -->In the example below, the `SDK` input depends on the `Language` input:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "language": {
      "type": "string",
      "enum": ["javascript", "python"]
    },
    "SDK": {
      "type": "string",
      "dependsOn": ["language"]
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        language = {
          enum = ["javascript", "python"]
        }
        SDK = {
          depends_on: ["language"]
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "language": {
        "enums": ["python", "javascript"],
      },
      "SDK": {
        "depends_ons": ["language"]
      },
    },
  }
)
```

The `dataset` property is used to filter the displayed options in an [entity](/actions-and-automations/create-self-service-experiences/setup-ui-for-action/user-inputs/entity.md) input. It is comprised of two properties:

* `Combinator` - the logical operation to apply between the rules of the dataset. [Read more](/search-and-query/structure-and-syntax.md#combinator).
* `Rules` - an array of [rules](/search-and-query/structure-and-syntax.md#rules), only entities that pass them will be displayed in the form. Note that the `value` key in the dataset can be a constant (string, number, etc) or a "jqQuery" object.

- API
- Terraform
- Pulumi

```
{
  "namespace": {
    "type": "string",
    "format": "entity",
    "blueprint": "namespace",
    "dataset": {
      "combinator": "and",
      "rules": [
        {
          "property": "$team",
          "operator": "containsAny",
          "value": "value here. this can also be a 'jqQuery' object"
        }
      ]
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" "myAction" {
  # ...action properties
  user_properties = {
    string_props = {
      "namespace" = {
        format      = "entity"
        blueprint   = "namespace"
        dataset = {
          combinator = "and"
          rules = [
            {
              property = "$team"
              operator = "containsAny"
              value = "value here. this can also be a 'jqQuery' object"
            }
          ]
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "namespace": {
        "format": "entity",
        "blueprint": "namespace",
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "property": "$team",
              "operator": "containsAny",
              "value": "value here. this can also be a 'jqQuery' object"
            }
          ]
        }
      }
    }
  }
)
```

The `disabled` property is used to dynamically disable/enable inputs in the form. The `disabled` value could be set to either a boolean (`true` value is always disabled, `false` value is always enabled), or to a `jqQuery` which evaluates to a boolean.

In this example, the `runArguments` properties are configured with `disabled` so that they only become disabled in the form when the matching value is selected in the `language` input:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "language": {
      "type": "string",
      "enum": ["javascript", "python"]
    },
    "pythonRunArguments": {
      "type": "string",
      "disabled": {
        "jqQuery": ".form.language == \"python\""
      }
    },
    "nodeRunArguments": {
      "type": "string",
      "disabled": {
        "jqQuery": ".form.language == \"javascript\""
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        language = {
          enum = ["javascript", "python"]
        }
        pythonRunArguments = {
          disabled_jq_query = ".form.language == \"python\""
        }
        nodeRunArguments = {
          disabled_jq_query = ".form.language == \"javascript\""
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "language": {
        "enums": ["python", "javascript"],
      },
      "pythonRunArguments": {"disabled_jq_query": '.form.language == "python"'},
      "nodeRunArguments": {"disabled_jq_query": '.form.language == "javascript"'},
    },
  }
)
```

***

## Schema examples[â](#schema-examples "Direct link to Schema examples")

### Creating a dependency between two form inputs[â](#creating-a-dependency-between-two-form-inputs "Direct link to Creating a dependency between two form inputs")

This example contains a dependency between the `language` input and the `SDK` input. The `SDK` input's available options are defined according to the selected language (see the `jqQuery` key).

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "language": {
      "type": "string",
      "enum": ["javascript", "python"]
    },
    "SDK": {
      "type": "string",
      "enum": {
        "jqQuery": "if .form.language == \"javascript\" then [\"Node 16\", \"Node 18\"] else [\"Python 3.8\"] end"
      },
      "dependsOn": ["language"]
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        language = {
          enum = ["javascript", "python"]
        }
        SDK = {
          enum_jq_query = "if .form.language == \"javascript\" then [\"Node 16\", \"Node 18\"] else [\"Python 3.8\"] end"
          depends_on: ["language"]
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "language": {
        "enums": ["python", "javascript"],
      },
      "SDK": {
        "enum_jq_query": "if .form.language == \"javascript\" then [\"Node 16\", \"Node 18\"] else [\"Python 3.8\"] end"
        "depends_ons": ["language"]
      },
    },
  }
)
```

![Cluster And Namespace Action](/assets/images/javascriptSDK-fe25d7efec2617580a45955fa7e3c639.png)

### Hiding property based on the executing user's roles[â](#hiding-property-based-on-the-executing-users-roles "Direct link to Hiding property based on the executing user's roles")

In this example, the `visible` checks if the executing user has the `"admin"` role, and if they don't have this role then the advanced option will be hidden for them. The default value will still be filled in and sent to the backend:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "simpleOption": {
      "type": "string",
      "enum": ["option1", "option2"]
    },
    "advancedOption": {
      "type": "string",
      "default": "default advanced value",
      "visible": {
        "jqQuery": ".user.roles | any(.name == \"Admin\")"
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        simpleOption = {
          enum = ["option1", "option2"]
        }
        advancedOption = {
          visible_jq_query = ".user.roles | any(.name == \"Admin\")"
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  "pulumi-resource-name",
  identifier="action-identifier",
  title="Action Title",
  blueprint="myBlueprint",
  user_properties={
    "string_props": {
      "simpleOption": {
          "enums": ["option1", "option2"]
      },
      "advancedOption": {"visible_jq_query": ".user.roles | any(.name == \"Admin\")"}
    },
  },
  trigger="DAY-2",
  webhook_method={"url": "https://myserver.com"},
)
```

This is how the run form would show up for non-admin users: ![What Non-Admins See](/assets/images/hiddenPropertyExample-eea64e97475a8752ea2f2a0adf3af1f7.png)

And this is how the form would show up for admin users: ![What Admins See](/assets/images/hiddenPropertyShownExample-75bdc135292376efe4157736134492f3.png)

### Filter the dropdown's available options based on a property[â](#filter-the-dropdowns-available-options-based-on-a-property "Direct link to Filter the dropdown's available options based on a property")

This example contains a filter that will only display environments that are not of type `production`:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "env": {
      "type": "string",
      "format": "entity",
      "blueprint": "environment",
      "dataset": {
        "combinator": "and",
        "rules": [
          {
            "property": "type",
            "operator": "!=",
            "value": "production"
          }
        ]
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        env = {
          format : "entity",
          blueprint : "environment"
          dataset = {
            combinator = "and"
            rules = [
              {
                property = "type"
                operator = "!="
                value = {
                  jq_query = "'production'"
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "env": {
        "format": "entity",
        "blueprint": "environment",
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "property": "type",
              "operator": "!=",
              "value": "production"
            }
          ]
        }
      }
    }
  }
)
```

![Only Production Envs](/assets/images/onlyNotProductionEnvs-7d9efd6a56e0d0a39cf3d2df0bac4c0e.png)

â<!-- --> only the environments whose type is not `production` will appear in the dropdown. <!-- -->â

### Filter the dropdown's available options based on a previous input[â](#filter-the-dropdowns-available-options-based-on-a-previous-input "Direct link to Filter the dropdown's available options based on a previous input")

This example contains a filter that will only display the namespaces that are [related to](/search-and-query/structure-and-syntax.md#operators-1) the cluster that was selected in the `Cluster` input:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "Cluster": {
      "type": "string",
      "format": "entity",
      "blueprint": "Cluster",
      "title": "Cluster",
      "description": "The cluster to create the namespace in"
    },
    "namespace": {
      "type": "string",
      "format": "entity",
      "blueprint": "namespace",
      "dependsOn": ["Cluster"],
      "dataset": {
        "combinator": "and",
        "rules": [
          {
            "operator": "relatedTo",
            "blueprint": "Cluster",
            "value": {
              "jqQuery": ".form.Cluster.identifier"
            }
          }
        ]
      },
      "title": "namespace",
      "description": "The namespace to create the cluster in"
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        cluster = {
          format      = "entity",
          blueprint   = "Cluster",
          title       = "Cluster",
          description = "The cluster to create the namespace in"
        }
        namespace = {
          title : "namespace",
          description : "The namespace to create the cluster in"
          format     = "entity",
          blueprint  = "namespace",
          depends_on = ["Cluster"],
          dataset = {
            combinator = "and"
            rules = [
              {
                blueprint = "Cluster"
                operator  = "relatedTo"
                value = {
                  jq_query = ".form.Cluster.identifier"
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "Cluster": {
        "format": "entity",
        "blueprint": "Cluster",
        "title": "Cluster",
        "description": "The cluster to create the namespace in"
      },
      "namespace": {
        "format": "entity",
        "blueprint": "namespace",
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "operator": "relatedTo",
              "blueprint": "Cluster",
              "value": {
                "jq_query": ".form.Cluster.identifier"
              }
            }
          ]
        }
      }
    }
  }
)
```

![Cluster And Namespace Action](/assets/images/clusterNamespaceActionSmallerExample-b696e04ca97e8cf0b073a55171586950.png)

â<!-- --> The user will be required to choose a cluster, then the `namespace` input list will be populated with namespace entities related to the chosen cluster. <!-- -->â

### Filter the dropdown's available options based on properties of the user that executes the action[â](#filter-the-dropdowns-available-options-based-on-properties-of-the-user-that-executes-the-action "Direct link to Filter the dropdown's available options based on properties of the user that executes the action")

This example contains a filter that will only display the namespaces that belong to the user's teams (note the value key in the rules object):

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "namespace": {
      "type": "string",
      "format": "entity",
      "blueprint": "namespace",
      "dataset": {
        "combinator": "and",
        "rules": [
          {
            "property": "$team",
            "operator": "containsAny",
            "value": {
              "jqQuery": "[.user.team]"
            }
          }
        ]
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        namespace = {
          format : "entity",
          blueprint : "namespace"
          dataset = {
            combinator = "and"
            rules = [
              {
                property = "$team",
                operator = "containsAny",
                value = {
                  jq_query = "[.user.team]"
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "string_props": {
      "namespace": {
        "format": "entity",
        "blueprint": "namespace",
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "property": "$team",
              "operator": "containsAny",
              "value": {
                "jq_query": "[.user.team]"
              }
            }
          ]
        }
      }
    }
  }
)
```

![](/img/software-catalog/blueprint/userPropertiesModal.png)

â<!-- --> These are the only namespaces that are associated with the logged-in user's teams. <!-- -->â

### Filter the dropdown's available options based on the properties of the entity on which the action is performed[â](#filter-the-dropdowns-available-options-based-on-the-properties-of-the-entity-on-which-the-action-is-performed "Direct link to Filter the dropdown's available options based on the properties of the entity on which the action is performed")

This example contains a filter that will only display the namespaces that have similar tags to those of the entity on which the action is performed:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "namespace": {
      "type": "string",
      "format": "entity",
      "blueprint": "namespace",
      "dataset": {
        "combinator": "and",
        "rules": [
          {
            "property": "tags",
            "operator": "containsAny",
            "value": {
              "jqQuery": "[.entity.properties.tags[]]"
            }
          }
        ]
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        namespace = {
          format     = "entity",
          blueprint  = "namespace",
          dataset = {
            combinator = "and"
            rules = [
              {
                property = "tags"
                operator = "containsAny"
                value = {
                  jq_query = "[.entity.properties.tags[]]"
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties = {
    "string_props": {
      "namespace": {
        "format": "entity",
        "blueprint": "namespace",
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "property": "tags",
              "operator": "containsAny",
              "value": {
                "jq_query": "[.entity.properties.tags[]]"
              }
            }
          ]
        }
      }
    }
  }
)
```

### Setting a default value with the jqQuery[â](#setting-a-default-value-with-the-jqquery "Direct link to Setting a default value with the jqQuery")

This example contains an array input with a default value that will be equal to the tags of the entity on which the action is performed:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "some_input": {
      "type": "array",
      "default": {
        "jqQuery": ".entity.properties.tags"
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      array_props = {
        some_input = {
          default_jq_query = ".entity.properties.tags"
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "array_props": {
      "some_input": {
        "default_jq_query": ".entity.properties.tags"
      }
    },
  },
  trigger="DAY-2", # CREATE, DAY-2, DELETE
)
```

![entity tags action](/assets/images/defaultEntityTags-226ee6a0e63f2af804db53b3f2a0ec33.png)

â<!-- --> The namespace tags are already inserted into the form. <!-- -->â

### Setting a disabled dynamic value with jqQuery[â](#setting-a-disabled-dynamic-value-with-jqquery "Direct link to Setting a disabled dynamic value with jqQuery")

This example contains an array input with a value that cannot be changed which is equal to the tags of the entity on which the action is performed:

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "some_input": {
      "type": "array",
      "disabled": true,
      "default": {
        "jqQuery": ".entity.properties.tags"
      }
    }
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      array_props = {
        some_input = {
          disabled         = true
          default_jq_query = ".entity.properties.tags"
        }
      }
    }
  }
}
```

pulumi.py

```
action = Action(
  # ...action properties
  user_properties={
    "array_props": {
      "some_input": {
        "disabled": True,
        "default_jq_query": ".entity.properties.tags"
      }
    },
  },
  trigger="DAY-2", # CREATE, DAY-2, DELETE
)
```

![Dynamic Disabled Entity Tags](/assets/images/dynamicDisabledEntityTags-27f1a447c3826821108962b3cf0c5b33.png)

â<!-- --> The namespace tags inserted into the form based on the selected entity. <!-- -->â

### Setting required inputs with the jqQuery[â](#setting-required-inputs-with-the-jqquery "Direct link to Setting required inputs with the jqQuery")

This example contains two user inputs: one will always be required, and the other will be required based on the entity's properties.

* API
* Terraform
* Pulumi

```
{
  "properties": {
    "alwaysRequiredInput": {
      "type": "string"
    },
    "inputRequiredBasedOnData": {
      "type": "string"
    }
  },
  "required": {
    "jqQuery": "if .entity.properties.conditionBooleanProperty then [\"alwaysRequiredInput\", \"inputRequiredBasedOnData\"] else [\"alwaysRequiredInput\"] end"
  }
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" myAction {
  # ...action configuration
  {
    user_properties = {
      string_props = {
        alwaysRequiredInput = {}
        inputRequiredBasedOnData = {}
      }
    }
    required_jq_query = "if .entity.properties.conditionBooleanProperty then [\"alwaysRequiredInput\", \"inputRequiredBasedOnData\"] else [\"alwaysRequiredInput\"] end"
  }
}
```

pulumi.py

```
action = Action(
  "budding-action",
  identifier="budding-action",
  title="A Budding Act",
  # ...more action properties
  user_properties={
    "string_props": {
      "alwaysRequiredInput": {},
      "inputRequiredBasedOnData": {}
    },
  },
  required_jq_query='if .entity.properties.conditionBooleanProperty then ["alwaysRequiredInput", "inputRequiredBasedOnData"] else ["alwaysRequiredInput"] end',
  trigger="DAY-2", # CREATE, DAY-2, DELETE
)

pulumi.export("name", action.title)
```

## Complete Example[â](#complete-example "Direct link to Complete Example")

In this example, we will create an action that lets the user select a cluster and a namespace in that cluster. The user will also be able to select a service that is already running in the cluster. The action will then deploy the selected service to the selected namespace in the cluster. The user will only be able to select a service that is linked to his team.

#### the existing model in Port:[â](#the-existing-model-in-port "Direct link to the existing model in Port:")

![Developer PortalCreate New Blueprint](/assets/images/clusterNamespaceBlueprint-dfef5e61d429bc67929d2792d0a7269d.png)

#### the action's configuration:[â](#the-actions-configuration "Direct link to the action's configuration:")

* API
* Terraform
* Pulumi

Create in Port

```
{
  "identifier": "createRunningService",
  "title": "Deploy running service to a cluster",
  "icon": "Cluster",
  "trigger": {
    "type": "self-service",
    "operation": "CREATE",
    "userInputs": {
      "properties": {
        "Cluster": {
          "type": "string",
          "format": "entity",
          "blueprint": "Cluster",
          "title": "Cluster",
          "description": "The cluster to create the namespace in"
        },
        "namespace": {
          "type": "string",
          "format": "entity",
          "blueprint": "namespace",
          "dependsOn": ["Cluster"],
          "dataset": {
            "combinator": "and",
            "rules": [
              {
                "operator": "relatedTo",
                "blueprint": "Cluster",
                "value": {
                  "jqQuery": ".form.Cluster.identifier"
                }
              }
            ]
          },
          "title": "namespace",
          "description": "The namespace to create the cluster in"
        },
        "service": {
          "type": "string",
          "format": "entity",
          "blueprint": "Service",
          "dataset": {
            "combinator": "and",
            "rules": [
              {
                "property": "$team",
                "operator": "containsAny",
                "value": {
                  "jqQuery": "[.user.team]"
                }
              }
            ]
          },
          "title": "Service"
        }
      },
      "required": ["Cluster", "namespace", "service"]
    },
  },
  "invocationMethod": {
    "type": "WEBHOOK",
    "url": "https://example.com"
  },
  "description": "This will deploy a running service to a cluster"
}
```

Terraform limitation

When using Terraform to define `dataset` rules that mix static values with `jq_query` values, the provider may not handle them correctly. See the [Terraform limitations](/build-your-software-catalog/custom-integration/iac/terraform/.md#limitations) section for a workaround using `jsonencode()`.

```
resource "port_action" "createRunningService" {
  title       = "Create Running Service"
  identifier  = "createRunningService"
  description = "This will deploy a running service to a cluster"
  webhook_method = {
    url = "https://example.com"
  }
  self_service_trigger = {
    operation = "CREATE"
    blueprint_identifier = "createRunningService"
    user_properties = {
      string_props = {
        cluster = {
          format      = "entity",
          blueprint   = "Cluster",
          title       = "Cluster"
          description = "The cluster to create the namespace in"
          required    = true
        }
        namespace = {
          title       = "Namespace"
          format      = "entity",
          blueprint   = "namespace",
          description = "The namespace to create the cluster in"
          required    = true
          depends_on  = ["cluster"]
          dataset = {
            combinator = "and"
            rules = [
              {
                blueprint = "Cluster"
                operator  = "relatedTo"
                value = {
                  jq_query = ".form.Cluster.identifier"
                }
              }
            ]
          }
        }
        service = {
          title     = "Service"
          blueprint = "Service",
          required  = true
          dataset = {
            combinator = "and"
            rules = [
              {
                blueprint = "$team"
                operator  = "containsAny"
                value = {
                  jq_query = "[.user.team]"
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

* Python
* Javascript

```
action = Action(
  "create-running-service",
  identifier="createRunningService",
  title="Deploy running service to a cluster",
  icon="Cluster",
  self_service_trigger={
    operation="CREATE"
    blueprint_identifier="createRunningService"
    user_properties={
      "string_props": {
        "Cluster": {
          "format": "entity",
          "blueprint": "Cluster",
          "required": True,
          "title": "Cluster",
          "description": "The cluster to create the namespace in"
        },
        "namespace": {
          "format": "entity",
          "blueprint": "namespace",
          "required": True,
          "depends_ons": ["Cluster"],
          "dataset": {
              "combinator": "and",
              "rules": [
                {
                  "operator": "relatedTo",
                  "blueprint": "Cluster",
                  "value": {
                    "jq_query": ".form.Cluster.identifier"
                  }
                }
              ],
          },
          "title": "namespace",
          "description": "The namespace to create the cluster in"
        },
        "service": {
          "format": "entity",
          "blueprint": "Service",
          "required": True,
          "dataset": {
            "combinator": "and",
            "rules": [
              {
                "blueprint": "$team",
                "operator": "containsAny",
                "value": {
                  "jq_query": "[.user.team]"
                }
              }
            ]
          },
          "title": "Service"
        }
      },
    },
  }
  description="This will deploy a running service to a cluster"
  webhook_method={"url": "https://example.com"},
)

pulumi.export("name", action.title)
```

```
"use strict";
const pulumi = require("@pulumi/pulumi");
const port = require("@port-labs/port");

const entity = new Action("create-running-service", {
  identifier: "createRunningService",
  title: "Deploy running service to a cluster",
  icon: "Cluster",
  userProperties: {
    stringProps: {
      "Cluster": {
        "format": "entity",
        "blueprint": "Cluster",
        "required": true,
        "title": "Cluster",
        "description": "The cluster to create the namespace in"
      },
      "namespace": {
        "format": "entity",
        "blueprint": "namespace",
        "required": true,
        "dependsOns": ["Cluster"],
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "operator": "relatedTo",
              "blueprint": "Cluster",
              "value": {
                "jqQuery": ".form.Cluster.identifier"
              }
            }
          ],
        },
      },
      "service": {
        "format": "entity",
        "blueprint": "Service",
        "required": true,
        "dataset": {
          "combinator": "and",
          "rules": [
            {
              "blueprint": "$team",
              "operator": "containsAny",
              "value": {
                "jqQuery": "[.user.team]"
              }
            }
          ]
        },
        "title": "Service"
      }
    }
  },
  trigger: "CREATE",
  description: "This will deploy a running service to a cluster"
  webhookMethod: {
    "url": "https://example.com"
  },
});

exports.title = entity.title;
```

#### The action in the developer portal:[â](#the-action-in-the-developer-portal "Direct link to The action in the developer portal:")

![Cluster And Namespace Action](/assets/images/clusterNamespaceAction-de21587a66edb31ec5cc0ceb377f236d.png)

â<!-- --> The user will be required to choose a cluster, and then the namespace input list will be populated with namespace entities related to the chosen cluster. The user will only be able to deploy services associated with his team.<br /><!-- -->Note the `$` before `team`, this indicates that this is a [metadata property](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/meta-properties.md).
