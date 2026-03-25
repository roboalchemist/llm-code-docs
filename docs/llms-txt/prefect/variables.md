# Source: https://docs.prefect.io/v3/how-to-guides/configuration/variables.md

# Source: https://docs.prefect.io/v3/concepts/variables.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Variables

> Variables are dynamically-named, mutable string values that can be used to store and reuse non-sensitive bits of data.

export const TF = ({name, href}) => <p>You can manage {name} with the <a href={href}>Terraform provider for Prefect</a>.</p>;

export const CLI = ({name, href}) => <p>You can manage {name} with the <a href={href}>Prefect CLI</a>.</p>;

export const variables = {
  cli: "https://docs.prefect.io/v3/api-ref/cli/variable",
  api: "https://app.prefect.cloud/api/docs#tag/Variables",
  tf: "https://registry.terraform.io/providers/PrefectHQ/prefect/latest/docs/resources/variable"
};

export const API = ({name, href}) => <p>You can manage {name} with the <a href={href}>Prefect API</a>.</p>;

Variables enable you to store and reuse non-sensitive bits of data, such as configuration information.
They are:

* named, mutable values of any JSON type
* scoped to a self-hosted Prefect server instance or a single workspace in a Prefect Cloud account
* meant for values with infrequent writes and frequent reads (but you can create or
  modify variables at any time)
* cacheable for quicker retrieval
* most commonly loaded during flow runtime (but you can load them in other contexts to pass
  configuration information to Prefect configuration files, such as deployment steps)

<Warning>
  **Variables are not Encrypted**

  We do not recommend using variables to store sensitive information. Instead, use
  [Secret blocks](https://docs.prefect.io/develop/blocks/#prefect-built-in-blocks) to store and access
  sensitive information.
</Warning>

## Manage variables

Create, read, edit, and delete variables through the Prefect UI, Python SDK, API, CLI or Terraform.
Names must adhere to these traditional variable naming conventions:

* Have no more than 255 characters
* Only contain lowercase alphanumeric characters (\[a-z], \[0-9]) or underscores (\_). Spaces are not allowed.
* Be unique

Values must have less than or equal to 5000 characters.

Optionally, you can add tags to a variable.

### Through the Prefect UI

View all the variables in your self-hosted Prefect server instance or Prefect Cloud account workspace
in the **Variables** page of the Prefect UI. Both the name and value of all variables
are visible to anyone with access to the server or workspace.

To create a new variable:

1. Select the **+** button next to the header of the **Variables** page.
2. Enter the name and value of the variable.

### Through the Python SDK

You can access variables at runtime using the `prefect.variables` module in the Python SDK.

```python  theme={null}
from prefect.variables import Variable

# Set a variable

Variable.set("my_variable", "my_value")

# Get a variable

my_var = Variable.get("my_variable")

# Update a variable by passing the `overwrite` parameter
# If the variable does not exist, it will be created

Variable.set("my_variable", "my_new_value", overwrite=True)

# Delete a variable
Variable.unset("my_variable")
```

### Through the REST API

<API name="variables" href={variables.api} />

### Through the CLI

<CLI name="variables" href={variables.cli} />

* `prefect variable set` creates or updates a variable.
* `prefect variable get` retrieves a variable's value.
* `prefect variable unset` deletes a variable.
* `prefect variable ls` lists all variables.
* `prefect variable inspect` shows a variable's details.

### Through Terraform

<TF name="variables" href={variables.tf} />


Built with [Mintlify](https://mintlify.com).