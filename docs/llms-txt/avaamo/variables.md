# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/variables.md

# variables

Context variables are temporary variables that can be used to store information required in an agent flow. The values stored in the context variables are available in that conversation flow unless you switch to another flow.&#x20;

You can use **context.variables** in JavaScript blocks to retain information across multiple conversations. See [how to create context variables](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/create-custom-variables), for a sample scenario.

{% hint style="success" %}
**Key Points**:&#x20;

* It is recommended to use context variables for transactional data that is specific to your agent or users, such as agent configuration parameters, and user attributes. Typically, these are in smaller data sets. For large data sets such as blobs and files, which have thousands or lacs of data records, the recommended approach is to develop external APIs for storing and managing such data. You can then pass parameters to query the API to get only filtered data that is required for your agent. Such large data sets must not be stored in the context variables, as it may impact performance.
* By default, the context is reset at the leaf node of the Dialog skill. You can use the **Reset Context** slider to reset context in a non-leaf node if required. See [Reset Context in Advanced Settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings), for more information. Also, see [When is context reset?](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/..#when-is-the-context-reset) for more information
  {% endhint %}

### Create context variables

Create context variables using the following syntax:

```javascript
context.variables.<<variable_name>> = <<value>>
```

<table><thead><tr><th width="176">Attribute</th><th>Description</th></tr></thead><tbody><tr><td>variable_name</td><td>Indicates the name of the variable. A variable name must be an alphanumeric string and must be unique within the agent flow.</td></tr><tr><td>value</td><td><p>Indicates the value to be assigned to the variable. It can be any of the data types supported in JavaScript, for example, numbers, strings, boolean, arrays and objects:</p><ul><li>context.variables.count =0;</li><li>context.variables.toppings=["pepper", "cheese","olives"];</li></ul></td></tr></tbody></table>

### Get context variables

**Get** the context variable using the key and assign it to another variable.

```javascript
var val = context.variables.<<variable_name>>;
```
