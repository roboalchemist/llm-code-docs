# Source: https://developers.kit.com/plugins/component-library/dependencies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dependencies

Many Kit components support **dependencies** — a feature that conditionally displays customization options based on user interactions with other fields. This creates a more intuitive and contextual user experience by showing relevant options only when needed.

## Configuration

To implement dependencies, add a `dependencies` property to your component's JSON configuration. This property accepts an array of objects that specify which fields must be interacted with before the current field becomes visible.

In order for a field to show when any value is selected:

```json  theme={null}
{
  "name": "advancedOption",
  "type": "text",
  "dependencies": [
      {
        "field": "basicOption"
      },
      {
        "field": "secondDependency"
      }
    ]
  // ...additional component-specific settings
}
```

## Value-Specific Dependencies

For more granular control, you can require specific values using a dependency object, with an additional specified value property. The dependent field will only appear when the specified field contains the exact value.

```json  theme={null}
{
  "name": "colorPicker",
  "type": "color",
  "dependencies": [
    {
      "field": "customColor",
      "value": "custom"
    }
  ]
  // ...additional component-specific settings
}
```

If you only want to show a component when a field has no value, you can specify the value as `null`:

```json  theme={null}
{
  "name": "colorPicker",
  "type": "color",
  "dependencies": [
    {
      "field": "customColor",
      "value": null
    }
  ]
  // ...additional component-specific settings
}
```

## Component-Specific Behaviors

While dependencies are widely supported, certain components have unique behaviors or limitations, examples can be found below:

* **Toggle components**: Only trigger dependencies when set to `true` (on state)
* **Some components**: May not support dependencies due to their functional design

For detailed information about dependency support and special behaviors for each component type, refer to the individual component documentation pages.

## Best Practices

* Use dependencies to progressively reveal complex options
* Keep dependency chains simple and logical
* Test all dependency scenarios to ensure expected behavior
* Document any custom dependency logic for team members and add to your app's help centre article


Built with [Mintlify](https://mintlify.com).