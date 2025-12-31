# Source: https://docs.zapier.com/platform/build-cli/empty-values-in-input-data.md

# Empty values in input data

> Handing empty values in `bundle.inputData` in your `perform*` functions

zapier-platform-core v18 introduced a new flag named `cleanInputData`. This flag allows you to tell Zapier whether it should automatically remove empty values, including `null`, `[]` (empty arrays), and `{}` (empty objects), from `bundle.inputData` before passing it to your `perform*` functions.

By default, the `cleanInputData` flag defaults to true, which matches the behavior of all versions prior to v18. Starting with v18, we encourage you to **explicitly set this flag to false**, either globally in `App.flags` or per trigger/action in the `operation` object. For example:

```javascript  theme={null}
const App = {
  flags: {
    cleanInputData: false, // global flag (defaults to true if not set)
  },
  triggers: {
    recipe: {
      operation: {
        cleanInputData: false, // per-action flag, can be omitted if same as global
      },
    },
  },
  creates: {
    recipe: {
      operation: {
        cleanInputData: true, // only enable for this action, overrides global flag
      },
    },
  },
};
```

## When `cleanInputData` is true

When `cleanInputData` is true, Zapier removes any empty values **recursively** from `bundle.inputData` before passing it to your `perform*` (including `perform`, `performList`, `performGet`, etc) functions. For example, given the following input data:

```json  theme={null}
{
  "name": "Chocolate Cake",
  "description": "",
  "tags": [null, "", "dessert"],
  "metadata": {
    "author": null,
    "ratings": {},
    "comments": []
  }
}
```

The resulting `bundle.inputData` passed to your `perform` function would be:

```json  theme={null}
{
  "name": "Chocolate Cake",
  "tags": ["dessert"]
}
```

## When `cleanInputData` is false

When `cleanInputData` is false, Zapier preserves all empty values in `bundle.inputData`. Using the same example input data above, the resulting `bundle.inputData` would be:

```json  theme={null}
{
  "name": "Chocolate Cake",
  "description": "",
  "tags": [null, "", "dessert"],
  "metadata": {
    "author": null,
    "ratings": {},
    "comments": []
  }
}
```

Your `perform` function would then need to handle these empty values appropriately.

We recommend setting `cleanInputData` to false and handling empty values explicitly in your code. This approach provides greater control for developers and avoids unexpected behavior, especially when dealing with nested input data (e.g., line items).

<Warning>
  If your `perform*` functions didn't previously handle empty values, **setting
  `cleanInputData` to false may break your code!** Make sure to test your
  triggers or actions before rolling out this change to users.
</Warning>
