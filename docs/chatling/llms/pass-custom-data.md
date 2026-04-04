# Source: https://docs.chatling.ai/web-widget/pass-custom-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to pass custom data to your chatbot

> Learn how to send any data, such as customer information, to the chatbot widget.

With the widget's code snippet, you can pass any data to the chatbot. This is useful if you want to send customer information, such as name and email, or any other data to the chatbot and use them in your flow.

## Before you begin

* You must know how to use [variables](/chatbot/builder/variables) in the builder.
* You have to [create variables](/chatbot/builder/variables/how-to-create-variables) in the builder for the data you want to pass to the chatbot. If the variables already exist, you can skip this step.

## Pass custom data during launch

When you [install the chatbot](/web-widget/installation/overview) on your website, you get a code snippet similar to this:

```html  theme={null}
<script> 
window.chtlConfig = { 
    chatbotId: "<WIDGET_ID>" 
} 
</script>

<script async data-id="<WIDGET_ID>" id="chatling-embed-script" type="text/javascript" src="https://chatling.ai/js/embed.js"></script>
```

You can pass custom data during launch by adding the `variables` property to the `chtlConfig` object, and listing the variable names and their values.

```javascript  theme={null}
window.chtlConfig = { 
    chatbotId: "<WIDGET_ID>",
    variables: {
        "variable_name_1": "<VALUE>",
        "variable_name_2": "<VALUE>",
        "variable_name_3": "<VALUE>"
    }
}
```

### Example

Let's say you want to pass the user's name, email and age to the chatbot. First, you need to [create variables](/chatbot/builder/variables/how-to-create-variables) for them in the builder.

<img src="https://chatling-assets.b-cdn.net/variables-for-storing-custom-data-from-widget.jpg" width="350" />

Next, add the variable values to your widget's code snippet. You must make sure that the variable names match exactly as they are in the builder.

```javascript  theme={null}
window.chtlConfig = { 
    chatbotId: "<WIDGET_ID>",
    variables: {
        "contact_name": "John Doe",
        "contact_email": "john.doe@example.com",
        "age": 25
    }
} 
```

Now if you use the variables in your chatbot's flow, they will have the values you passed during launch.

<img src="https://chatling-assets.b-cdn.net/pass-custom-data-during-launch-example-3.jpg" width="400" />

## Pass custom data after launch

If at any point after launching the chatbot, you want to pass some data to it, you can do so by calling the `window.Chatling.setVariables` function.

```javascript  theme={null}
window.Chatling.setVariables({
    "contact_name": "Rick Astley",
    "contact_email": "rick.astley@example.com",
    "age": 30
}, function(success, errorMessage) {
    if (!success) {
        // handle error
    }
});
```

**Note:**

* The `setVariables` function must be called after the chatbot widget has loaded.

- Variables must be present in the builder and the names must match exactly.
- This will overwrite any existing values for the variables.
