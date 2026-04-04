# Source: https://docs.port.io/actions-and-automations/create-self-service-experiences/send-link-to-action.md

# Share a pre-filled action URL

Port allows you to generate links that pre-fill action inputs, making it easy to share action execution URLs with your developers.<br /><!-- -->This is particularly useful when you want to:

1. Create bookmarks for commonly used actions with specific inputs.
2. Share action execution links in documentation.
3. Programmatically generate action links from your systems.

## How it works[â](#how-it-works "Direct link to How it works")

The action execution URL follows this structure:

```
https://app.getport.io/self-serve?action=ACTION_IDENTIFIER&actionInputs=ENCODED_INPUTS
```

* `ACTION_IDENTIFIER` is your action's unique identifier
* `ENCODED_INPUTS` is a minified version of your inputs using JSURL encoding

## Generate action execution URL[â](#generate-action-execution-url "Direct link to Generate action execution URL")

To generate an action execution URL, you will need to use the `JSURL` library to properly encode the action inputs.

**Code example (click to expand)**

```
// Load jsurl2 library
let script = document.createElement('script');
script.src = "https://cdn.jsdelivr.net/npm/jsurl2";
document.head.appendChild(script);

script.onload = function() {
    // Your action inputs
    let actionInputs = {
        input1: "value1",
        input2: "value2"
    };

    // Encode the inputs
    let encodedInputs = JSURL.stringify(actionInputs);
    
    // Generate the full URL
    let actionIdentifier = "your_action_id";
    let url = `https://app.getport.io/self-serve?action=${actionIdentifier}&actionInputs=${encodedInputs}`;
    
    console.log("Action URL:", url);
};
```

Entity input key

When pre-filling the entity to operate on in `DAY-2` or `DELETE` operations, use `$targetEntity` as the input key, and the entity's `identifier` as the value.

## Example[â](#example "Direct link to Example")

Let's say you have a "Report Bug" action with identifier `report_bug` that accepts the following inputs:

* `title`: The bug title
* `severity`: Bug severity level
* `description`: Detailed bug description

The following code will generate a link for it:

```
let actionInputs = {
    title: "UI Performance Issue",
    severity: "High",
    description: "The dashboard is loading slowly when displaying more than 100 items"
};

// Using JSURL to encode
let encodedInputs = JSURL.stringify(actionInputs);
let url = `https://app.port.io/self-serve?action=report_bug&actionInputs=${encodedInputs}`;
```

The generated URL will lead to the action's execution form, pre-filled with the defined input values.

JSURL

For complex inputs with special characters, spaces, or nested objects, using JSURL encoding is essential as it properly handles these cases while keeping the URL compact.

## Interactive URL generator[â](#interactive-url-generator "Direct link to Interactive URL generator")

To simplify the process described in this page, you can use this interactive tool to generate the finalized URL:

Action Identifier:Enter action identifier (e.g. report\_bug)

Action Inputs (JSON):Load Example

Generate URL

## Use action URLs in entity properties[â](#use-action-urls-in-entity-properties "Direct link to Use action URLs in entity properties")

Action URLs can be used within entity URL properties, allowing developers to trigger actions directly from the entity page without navigating to the self-service hub.

When an entity property (including [calculation properties](https://docs.port.io/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/calculation-property/)) contains a valid action URL, clicking on it will open the action execution form in a modal on the current page.

### Example: Dynamic action link in a calculation property[â](#example-dynamic-action-link-in-a-calculation-property "Direct link to Example: Dynamic action link in a calculation property")

You can create a calculation property that generates an action URL. For example, a "Deploy Service" link:

```
{
  "calculationProperties": {
    "deployAction": {
      "title": "Deploy Service",
      "type": "string",
      "format": "url",
      "calculation": "'https://app.port.io/self-serve?action=deploy_service&actionInputs=<encoded_inputs>'"
    }
  }
}
```

Use the [action inputs parameter with JSURL encoding](#generate-action-execution-url) to create personalized action URLs based on the entity's data.

Arrays of action URLs

Action URLs also work within array properties.<br /><!-- -->In an array of URLs, clicking on any of them will open the corresponding action form in a modal.

### Limitations[â](#limitations "Direct link to Limitations")

* **Labeled URLs are not supported**: Action URLs must be plain URL strings. The [labeled-url format](/build-your-software-catalog/customize-integrations/configure-data-model/setup-blueprint/properties/labeled-url-object.md) (containing both a URL and display text) will not trigger the in-page modal behavior.
* **Array consistency**: When using an array of URLs, the modal behavior only works if **all URLs** in the array follow the action URL pattern. Mixed arrays (containing both action URLs and regular URLs) will not trigger the modal.
