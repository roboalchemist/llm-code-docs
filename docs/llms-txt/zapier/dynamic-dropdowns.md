# Source: https://docs.zapier.com/platform/build-cli/dynamic-dropdowns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic dropdowns

Sometimes, API endpoints require clients to specify a parent object in order to create or access the child resources. For instance, specifying a spreadsheet id in order to retrieve its worksheets. Since people don't speak in auto-incremented ID's, it is necessary that Zapier offer a simple way to select that parent using human readable handles.

Our solution is to present users a dropdown that is populated by making a live API call to fetch a list of parent objects. We call these special dropdowns "dynamic dropdowns."

## Definition

To define one you include the `dynamic` property on the `inputFields` object. The value for the property is a dot-separated *string* concatenation.

```js  theme={null}
//...
issue: {
  key: 'issue',
  //...
  create: {
    //...
    operation: {
      inputFields: [
        {
          key: 'project_id',
          required: true,
          label: 'This is a dynamic dropdown',
          dynamic: 'project.id.name'
        }, // will call the trigger with a key of project
        {
          key: 'title',
          required: true,
          label: 'Title',
          helpText: 'What is the name of the issue?'
        }
      ]
    }
  }
}

```

The dot-separated string concatenation follows this pattern:

* The key of the trigger you want to use to power the dropdown. *required*
* The value to be made available in bundle.inputData. *required*
* The human friendly value to be shown on the left of the dropdown in bold. *optional*

In the above code example the dynamic property makes reference to a trigger with a key of project. Assuming the project trigger returns an array of objects and each object contains an id and name key, i.e.

```js  theme={null}
[
  { id: "1", name: "First Option", dateCreated: "01/01/2000" },
  { id: "2", name: "Second Option", dateCreated: "01/01/2000" },
  { id: "3", name: "Third Option", dateCreated: "01/01/2000" },
  { id: "4", name: "Fourth Option", dateCreated: "01/01/2000" },
];
```

The dynamic dropdown would look something like this.
![screenshot of dynamic dropdown in Zap Editor](https://cdn.zappy.app/6a90fcc532704f6c14b91586f5cd1d5b.png)

## Use a resource

In the first code example the dynamic dropdown is powered by a trigger. You can also use a resource to power a dynamic dropdown. To do this combine the resource key and the resource method using camel case.

```js index.js theme={null}
const App = {
  // ...
  resources: {
    project: {
      key: "project",
      // ...
      list: {
        // ...
        operation: {
          perform: () => {
            return [{ id: 123, name: "Project 1" }];
          }, // called for project_id dropdown
        },
      },
    },
    issue: {
      key: "issue",
      // ...
      create: {
        // ...
        operation: {
          inputFields: [
            {
              key: "project_id",
              required: true,
              label: "Project",
              dynamic: "projectList.id.name",
            }, // calls project.list
            {
              key: "title",
              required: true,
              label: "Title",
              helpText: "What is the name of the issue?",
            },
          ],
        },
      },
    },
  },
};
```

## Hide the trigger

In some cases you will need to power a dynamic dropdown but do not want to make the Trigger available to the end user. Here it is best practice to create the trigger and set `hidden: true` on it's display object.

```js  theme={null}
const App = {
  // ...
  triggers: {
    new_project: {
      key: "project",
      noun: "Project",
      // `display` controls the presentation in the Zapier Editor
      display: {
        label: "New Project",
        description: "Triggers when a new project is added.",
        hidden: true,
      },
      operation: {
        perform: projectListRequest,
      },
    },
    another_trigger: {
      // Another trigger definition...
    },
  },
};
```

## Dependencies between dropdowns

You can have multiple dynamic dropdowns in a single trigger or action. In some cases, a dynamic dropdown depends on the value chosen in another dynamic dropdown when making its API call. The [Google Sheets](https://zapier.com/apps/google-sheets/integrations#triggers-and-actions) integration displays an example of this pattern.

The example below illustrates a 'New Worksheet' trigger that populates a dynamic dropdown input field to select a worksheet:

```js  theme={null}
{
  key: "worksheet",
  // ...
  operation: {
    // ...
    perform: async (z, bundle) => {
      const response = await z.request("https://example.com/api/v2/projects.json", {
        params: {
          spreadsheet_id: bundle.inputData.spreadsheet_id,
        },
      });

      // response.throwForStatus() if you're using core v9 or older

      return response.data; // or response.json if you're using core v9 or older
    }
  }
}
```

Assume there is another `New Records` trigger with `Spreadsheet` and `Worksheet` dynamic dropdown input fields, which have keys `spreadsheet_id` and `worksheet_id` respectively. The selected spreadsheet value is available via `bundle.inputData.spreadsheet_id` to be used by the `Worksheet` trigger.

```js  theme={null}
const App = {
  // ...
  triggers: {
    // ...
    issue: {
      key: "new_records",
      // ...
      operation: {
        inputFields: [
          {
            key: "spreadsheet_id",
            required: true,
            label: "Spreadsheet",
            dynamic: "spreadsheet.id.name",
            altersDynamicFields: true,
          },
          {
            key: "worksheet_id",
            required: true,
            label: "Worksheet",
            dynamic: "worksheet.id.name",
          },
        ],
      },
    },
  },
};
```

> Note: Be mindful that a dynamic dropdown can depend on the value chosen in another dynamic dropdown. Two types of dependencies can exist between fields:
>
> *Requirement dependency*: Affects how dependent fields are enabled or disabled within the UI
>
> * Setting `required: false` makes a field optional and always enabled in the UI.
> * Having no required value set makes a field optional and disabled until the dependencies are selected.
>
> *Value dependency*: Affects how dynamic dropdown field options are retrieved
>
> * Setting a required value or not does not affect how the options of a dynamic field are retrieved.
>
> So, if you have an optional dynamic dropdown that depends on another dropdown input field, that field should not have `required: false` set. Input fields are optional by default, but setting `required: false` on an optional dynamic dropdown field that depends on another removes the requirement dependency relationship.
> In the example above, the `worksheet_id` input field will be disabled until the `spreadsheet_id` input field has a value in Zapier's products such as the Zap editor. Notice that setting `altersDynamicFields: true` signifies other input fields need to be recomputed whenever the value of that field changes.

## Detect when a trigger is used for a dynamic dropdown

If you want your trigger to perform specific scripting for a dynamic dropdown you will need to make use of `bundle.meta.isFillingDynamicDropdown`. This can be useful if need to make use of [pagination](/platform/build-cli/faqs#whats-the-deal-with-pagination-when-is-it-used-and-how-does-it-work) in the dynamic dropdown to load more options.

```js  theme={null}
const App = {
  // ...
  resources: {
    project: {
      key: "project",
      // ...
      list: {
        // ...
        operation: {
          canPaginate: true,
          perform: () => {
            if (bundle.meta.isFillingDynamicDropdown) {
              // perform pagination request here
            } else {
              return [{ id: 123, name: "Project 1" }];
            }
          },
        },
      },
    },
    issue: {
      key: "issue",
      // ...
      create: {
        // ...
        operation: {
          inputFields: [
            {
              key: "project_id",
              required: true,
              label: "Project",
              dynamic: "projectList.id.name",
            }, // calls project.list
            {
              key: "title",
              required: true,
              label: "Title",
              helpText: "What is the name of the issue?",
            },
          ],
        },
      },
    },
  },
};
```

## Link a search action

This feature makes it easier for users to handle the following scenario in a workflow that has multiple steps:

* The value for the input field depends on an output field from an earlier step.
* The value of that output field cannot be used directly.
* They need an additional search step that takes the output they *cannot* use directly, and translate it into something they *can*.

**Example:** Let's say the input field takes the ID of a lead. The user could select a lead from the dynamic dropdown, but then the workflow would act on the same lead every time it runs. An earlier step returns the email address of the lead, but not their ID. The user will need to prepend a search-step that takes the email address and returns the ID.

Users can do this themselves, but by using this feature, Zapier products can make this task easier.

### How it works for the user

In the Zap editor for example, dynamic dropdowns that use this feature will display a
button next to the dynamic dropdown. When the user clicks the button, the right search step is automatically prepended, and correct output field mapped into the dynamic dropdown.

![](https://cdn.zappy.app/c6bd53c4bf3efe9870493dc7c3c2dafc.gif)

### How to configure it

In the definition of the input field, configure `search` with a value of `<searchActionKey>.<outputFieldKey>`.

* Replace `<searchActionKey>` with the `key` of the search action that should prepeded to the user's workflow.
* Replace `<outputFieldKey>` with the `key` of the output field from that search action that should be mapped as value for the input field.

Here's an example:

```js  theme={null}
{
    key: 'project_id',
    required: true,
    label: 'Project',
    dynamic: 'list_projects.id.name',
    search: 'search_projects.id',
}
```
