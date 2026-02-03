# Source: https://dev.writer.com/blueprints/parsejson.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Parse JSON

Converts a JSON string into an object, so you can work with it in your logic.

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=998885fd519824d4f30f92198b620453" alt="" data-og-width="2310" width="2310" data-og-height="1490" height="1490" data-path="images/agent-builder/blueprints/parse-json-block.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=2425ca6bac6a1dfe65672addab818ec6 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=94e30f08c1230be8967003faa23b442d 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f2bc6edaabb144a7068060cbb29e4f2a 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ac1b08e420a65cea7f133549ded4fa2b 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=077ce433c6ee92c1b65fca4cd1b910d8 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-block.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=f587f97f4cd5836220fced4477878ced 2500w" />

## Overview

The **Parse JSON** block transforms a JSON-formatted string into a structured object that you can work with programmatically. For example, if you have a string like `'{"name": "John", "age": 30}'`, this block converts it into an object where you can access values like `object.name` or `object.age`.

This block is essential when you need to extract and work with data from:

* API responses that return JSON strings
* Form submissions containing JSON data
* Configuration files stored as JSON
* Any text that follows JSON format

The parsed object lets you:

* Access nested values using dot notation (for example, `user.address.city`)
* Iterate through arrays of data
* Pass structured data to other blocks
* Validate and transform the data structure

## Common use cases

* Parsing API responses
* Converting user input into structured data
* Extracting values from JSON payloads
* Validating JSON format before further processing

## How it works

1. **JSON string**: Enter the JSON string to parse. You can use variables or state values.

The block parses the string and outputs the resulting object. If the string is not valid JSON, the block raises an error.

## Examples

### User order form processing

This example shows why parsing JSON is essential for conditional logic and data extraction.

**Scenario:** A user submits an order form with JSON data that looks like this:

```json  theme={null}
{
  "customer": {
    "name": "Sarah Johnson",
    "email": "sarah@example.com",
    "tier": "premium"
  },
  "items": [
    {"product": "Laptop", "price": 1299.99, "quantity": 1},
    {"product": "Mouse", "price": 29.99, "quantity": 2}
  ],
  "total": 1359.97,
  "shipping_method": "express"
}
```

**Without Parse JSON (problematic):**

* Text generation block sees: `"{"customer": {"name": "Sarah Johnson"...`
* Can't access specific values like customer name or total
* Can't apply conditional logic based on order value
* Can't calculate discounts for premium customers

**With Parse JSON (powerful):**

1. **UI Trigger** → User submits order form
2. **Parse JSON** → Converts form data to structured object
3. **Set state** → Store parsed data in a state variable called `parsed_order`
4. **Classification** → Check if `@{parsed_order.total}` >= 1000 for free shipping
5. **Text generation** → Use `@{parsed_order.customer.name}` and `@{parsed_order.total}` in response

**Block Configuration:**

* **JSON string:** `@{order}` (the name of the state variable that contains the JSON string from the interface)

<img src="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=47b7ab1472b0b8d19a5d23aa49231df2" alt="" data-og-width="2742" width="2742" data-og-height="1520" height="1520" data-path="images/agent-builder/blueprints/parse-json-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?w=280&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=14775b2b16e38a51281cdce4c9be28cf 280w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?w=560&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=aabaa684568fce5895a31bff8635c6a1 560w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?w=840&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1b4364460c8034d92da9f600ed174d3d 840w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?w=1100&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=585522ab4d9551b2ea4f1d3e99654123 1100w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?w=1650&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=ddfad032b8f763098b148d4ca967b45f 1650w, https://mintcdn.com/writer/KruNpIclsgQbhj82/images/agent-builder/blueprints/parse-json-workflow.png?w=2500&fit=max&auto=format&n=KruNpIclsgQbhj82&q=85&s=1bdc7a602c9421a417582e2b96cac879 2500w" />

## Fields

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th>Control</th>
    <th>Default</th>
    <th>Description</th>
    <th>Options</th>
    <th>Validation</th>
  </thead>

  <tbody>
    <tr>
      <td>Plain text</td>
      <td>Text</td>
      <td>Textarea</td>

      <td>
        <span>-</span>
      </td>

      <td>-</td>

      <td>
        <span>-</span>
      </td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>

## End states

Below are the possible end states of the block call.

<table className="blueprintFields">
  <thead>
    <th>Name</th>
    <th>Field</th>
    <th>Type</th>
    <th>Description</th>
  </thead>

  <tbody>
    <tr>
      <td>Success</td>
      <td>-</td>
      <td>success</td>
      <td>The request was successful.</td>
    </tr>

    <tr>
      <td>Error</td>
      <td>-</td>
      <td>error</td>
      <td>The text provided couldn't be parsed.</td>
    </tr>
  </tbody>
</table>

The output of the **Parse JSON** block is a structured object. You can use this object in the following block with the `@{result}` variable.

To access the values of the object in other blueprint blocks, you can use dot notation. For example, if the object looks like this:

```json  theme={null}
{
  "customer": {
    "name": "Sarah Johnson",
    "email": "sarah@example.com",
    "tier": "premium"
  }
}
```

`@{result.customer.name}` will return the value of the `name` property of the `customer` object.
