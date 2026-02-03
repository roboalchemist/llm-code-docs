# Source: https://docs.zapier.com/platform/build-cli/input-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Input Field Configuration

On each trigger, search, or create in the `operation` directive, you can provide fields as an array of objects under `inputFields`.

Those fields have various options you can provide. Here is a brief example:

```js  theme={null}
const App = {
  // ...
  creates: {
    create_recipe: {
      // ...
      operation: {
        // an array of objects is the simplest way
        inputFields: [
          {
            key: "title",
            required: true,
            label: "Title of Recipe",
            helpText: "Name your recipe!",
          },
          {
            key: "style",
            required: true,
            choices: { mexican: "Mexican", italian: "Italian" },
          },
        ],
        perform: () => {},
      },
    },
  },
};
```

Notably, fields come in different types, which may look and act differently in the Zap editor. The default field display is a single-line input field.

| Type       | Behavior                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `string`   | Accepts text input.                                                                                                                                                                                                |
| `text`     | Displays large, `<textarea>`-style entry box, accepts text input.                                                                                                                                                  |
| `code`     | Displays large, `<textarea>`-style box with a fixed-width font, accepts text input.                                                                                                                                |
| `integer`  | Accepts integer number values.                                                                                                                                                                                     |
| `number`   | Accepts any numeric value, including decimal numbers.                                                                                                                                                              |
| `boolean`  | Displays dropdown menu offering true and false options. Passes along `true` or `false`.                                                                                                                            |
| `datetime` | Accepts both [precise and human-readable date-time values](https://help.zapier.com/hc/en-us/articles/8496259603341-Different-field-types-in-Zaps#date-time-fields-0-0). Passes along an ISO-formatted time string. |
| `file`     | Accepts a file object or a string. If a URL is provided in the string, Zapier will automatically make a GET for that file. Otherwise, a text file will be generated.                                               |
| `password` | Displays entered characters as hidden, accepts text input. Does not accept input from previous steps.                                                                                                              |
| `copy`     | Does not allow users to enter data. Shows the value of the Markdown-formatted Help Text for the field as a rich text note in the Zap editor. Good for important notices to users.                                  |

You can find more details on the different field schema options at [our Field Schema](https://github.com/zapier/zapier-platform/blob/main/packages/schema/docs/build/schema.md#fieldschema).

### Custom/Dynamic Fields

In some cases, you may need to provide dynamically-generated fields - especially for custom ones. This is common functionality for CRMs, form software, databases, and other highly-customizable platforms. Instead of an explicit field definition, you can provide a function we'll evaluate to return a list of fields - merging the dynamic with the static fields.

> You should see `bundle.inputData` partially filled in as users provide data - even in field retrieval. This allows you to build hierarchical relationships into fields (e.g. only show issues from the previously selected project).

> A function that returns a list of dynamic fields cannot include additional functions in that list to call for dynamic fields.

```js  theme={null}
const recipeFields = async (z, bundle) => {
  const response = await z.request("https://example.com/api/v2/fields.json");

  // Call response.throwForStatus() if you're using zapier-platform-core v9 or older

  // Should return an array like [{"key":"field_1"},{"key":"field_2"}]
  return response.data; // response.json if you're using core v9 or older
};

const App = {
  // ...
  creates: {
    create_recipe: {
      // ...
      operation: {
        // an array of objects is the simplest way
        inputFields: [
          {
            key: "title",
            required: true,
            label: "Title of Recipe",
            helpText: "Name your recipe!",
          },
          {
            key: "style",
            required: true,
            choices: { mexican: "Mexican", italian: "Italian" },
          },
          recipeFields, // provide a function inline - we'll merge the results!
        ],
        perform: () => {},
      },
    },
  },
};
```

Additionally, if there is a field that affects the generation of dynamic fields, you can set the property `altersDynamicFields: true`. This informs the Zapier UI whenever the value of that field changes, the input fields need to be recomputed. For example, imagine the selection on a static dropdown called "Dessert Type" determining whether the function generating dynamic fields includes the field "With Sprinkles?" or not. If the value in one input field affects others, this is an important property to set.

```js  theme={null}
module.exports = {
  key: "dessert",
  noun: "Dessert",
  display: {
    label: "Order Dessert",
    description: "Orders a dessert.",
  },
  operation: {
    inputFields: [
      {
        key: "type",
        required: true,
        choices: { 1: "cake", 2: "ice cream", 3: "cookie" },
        altersDynamicFields: true,
      },
      function (z, bundle) {
        if (bundle.inputData.type === "2") {
          return [{ key: "with_sprinkles", type: "boolean" }];
        }
        return [];
      },
    ],
    perform: function (z, bundle) {
      /* ... */
    },
  },
};
```

> Only dropdowns support `altersDynamicFields`.

When using dynamic fields, the fields will be retrieved in three different contexts:

* Whenever the value of a field with `altersDynamicFields` is changed, as described above.

* Whenever the Zap Editor opens the "Set up" section for the trigger or action.

* Whenever the "Refresh fields" button at the bottom of the Editor's "Set up" section is clicked.

Be sure to set up your code accordingly - for example, don't rely on any input fields already having a value, since they won't have one the first time the "Set up" section loads.

### Dynamic Dropdowns

See [Dynamic Dropdowns](/platform/build-cli/dynamic-dropdowns).

### Computed Fields

In OAuth and Session Auth, Zapier automatically stores every value from an integration’s auth API response i.e. that’s `getAccessToken` and `refreshAccessToken` for OAuth and `getSessionKey` for session auth.

You can return additional fields in these responses, on top of the expected `access_token` or `refresh_token` for OAuth and `sessionKey` for Session auth. They will be saved in `bundle.authData`. You can reference these fields in any subsequent API call as needed.

> Note: Only OAuth and Session Auth support computed fields.

If you want Zapier to validate that these additional fields exist, you need to use Computed Fields. If you define computed fields in your integration, Zapier will check to make sure those fields exist when it runs the authentication test API call.

Computed fields work like any other field, though with `computed: true` property, and `required: false` as user can not enter computed fields themselves. Reference computed fields in API calls as `{{bundle.authData.field}}`, replacing `field` with that field's name from your test API call response.

You can see examples of computed fields in the [OAuth2](/platform/build-cli/overview#oauth2) or [Session Auth](/platform/build-cli/overview#session) example sections.

### Nested & Children (Line Item) Fields

When your action needs to accept an array of items, you can include an input field with the `children` attribute. The `children` attribute accepts a list of [fields](https://github.com/zapier/zapier-platform/blob/main/packages/schema/docs/build/schema.md#fieldschema) that can be input for each item in this array.

```js  theme={null}
const App = {
  // ...
  operation: {
    // ...
    inputFields: [
      {
        key: "lineItems",
        children: [
          {
            key: "lineItemId",
            type: "integer",
            label: "Line Item ID",
            required: true,
          },
          {
            key: "name",
            type: "string",
            label: "Name",
            required: true,
          },
          {
            key: "description",
            type: "string",
            label: "Description",
          },
        ],
      },
    ],
    // ...
  },
};
```

### Defining extra input field metadata

Since [version 15.19.0](https://github.com/zapier/zapier-platform/blob/963737b72a81bf7d6e8cbbb8292190268da8f066/changelog/v14-v16.md#15190), input fields may define a `meta` property containing an object with `string` keys and `string`, `integers` or `boolean` values. This `meta` object will then be made available as part of [bundle.meta](https://docs.zapier.com/platform/build-cli/core#bundle-meta), under the `inputFields` key. For example, if an input field with a `create_recipe` key defines a `meta` object, then this object will be available during the `perform` method in: `bundle.meta.inputFields['create_recipe']`.

This context storage is particularly useful when using dynamically-generated fields, as you may want to use this extra data to change certain logic in the `perform` method of your triggers or actions.

```js  theme={null}
const fetchStringOrDatetimeFields = async (z, bundle) => {
  // Should return an array like [{'key':'field_1'},{'key':'field_2_datetime'}]
  const response = await z.request("https://example.com/api/v2/fields.json");

  const resultingFields = [];

  response.data.forEach((field) => {
    if (field.key.endsWith("_datetime")) {
      resultingFields.push({
        key: field.key,

        // Set the meta to be parsed as a datetime
        meta: { internalType: "datetime" },
      });
    } else {
      resultingFields.push({
        key: field.key,

        // Set the meta to string (default)
        meta: { internalType: "string" },
      });
    }
  });

  return resultingFields;
};

const App = {
  // ...
  creates: {
    create_agenda: {
      // ...
      operation: {
        inputFields: [fetchStringOrDatetimeFields],
        perform: async (z, bundle) => {
          for (const [key, value] of Object.entries(bundle.inputData)) {
            const fieldMeta = bundle.meta.inputFields[key] || {};

            if (fieldMeta.internalType === "datetime") {
              // process value as a datetime
            } else {
              // process value as a string
            }
          }
        },
      },
    },
  },
};
```

### Visual Grouping

The input fields visual grouping feature provides the means to configure how input fields are displayed in the Zap editor. It could come in handy when you need certain fields to be displayed together perhaps based on priority and have others collapsed under another group.

To leverage this feature, ensure the integration uses platform-core version `>=17.3.0` and define the groups in `inputFieldGroups` array in an action's operation object.

There are 3 properties to define a group;

* `key`: The unique identifier for the group (`Required`).
* `label`: The human-readable name for the group (`Optional`). It is auto-generated from the key when not provided.
* `emphasize`: A boolean property to identify when the group's fields should be displayed or collapsed in the Zap editor. It defaults to false collapsing the group's input fields (`Optional`).

To group an input field, a property `group` is set in the input field object referencing any of the groups by its key.

Take the following, for example;

```js  theme={null}
const App = {
  // ...
  creates: {
    appointment: {
      // ...
      operation: {
        // an array of groups
        inputFieldGroups: [
          { key: "basic_info", label: "Basic Information", emphasize: true },
          { key: "pet_info", label: "Pet Information", emphasize: true },
          {
            key: "billing_info",
            label: "Billing Information",
            emphasize: false,
          },
          { key: "shipping_info" },
        ],
        // an array of input fields referencing keys of groups defined in inputFieldGroups
        inputFields: [
          { key: "vet_name", type: "string", group: "basic_info" },
          { key: "appointment_date", type: "datetime", group: "basic_info" },
          { key: "billing_address", type: "string", group: "billing_info" },
          { key: "billing_city", type: "string", group: "billing_info" },
          { key: "shipping_address", type: "string", group: "shipping_info" },
          { key: "owner", type: "string", group: "pet_info" },
          {
            // line-items
            key: "dogs",
            group: "pet_info",
            children: [
              { key: "name", type: "string" },
              { key: "breed", type: "string" },
              { key: "age", type: "number" },
            ],
          },
        ],
        perform: () => {},
      },
    },
  },
};
```

Here is the visual outcome of the input fields grouping in the Zap editor for the above example;

<Frame>
  <img src="https://cdn.zappy.app/ad54ae22892557eab7ff84c3b8d279ab.png" />

  {" "}
</Frame>
