# Admin Panel API for plugins

A Strapi plugin can interact with both the [back end](/cms/plugins-development/server-api) and the front end of a Strapi application. The Admin Panel API is about the front end part, i.e. it allows a plugin to customize Strapi's [admin panel](/cms/intro).

The admin panel is a 

</Tabs>

### Settings API

The Settings API allows:

* [creating a new setting section](#createsettingsection)
* adding [a single link](#addsettingslink) or [multiple links at once](#addsettingslinks) to existing settings sections

:::note
Adding a new section happens in the [register](#register) lifecycle while adding links happens during the [bootstrap](#bootstrap) lifecycle.
:::

All functions accept links as objects with the following parameters:

| Parameter     | Type             | Description                                                                                                                                                                                                              |
| ------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`          | String           | React id                                                                                                                                                                                                                 |
| `to`          | String           | Path the link should point to                                                                                                                                                                                            |
| `intlLabel`   | Object           | Label for the link, following the  convention, with:<ul><li>`id`: id used to insert the localized label</li><li>`defaultMessage`: default label for the link</li></ul> |
| `Component`   | Async function   | Returns a dynamic import of the plugin entry point                                                                                                                                                                       |
| `permissions` | Array of Objects | Permissions declared in the `permissions.js` file of the plugin                                                                                                                                                          |
| `licenseOnly` | Boolean | If set to `true`, adds a lightning ⚡️ icon next to the icon or menu entry to indicate that the feature or plugin requires a paid license.<br/>(Defaults to `false`) |

#### createSettingSection()

**Type**: `Function`

Create a new settings section.

The function takes 2 arguments:

| Argument        | Type             | Description                                                                                                                                                                                                                                                                                                                   |
| --------------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| first argument  | Object           | Section label:<ul><li>`id` (String): section id</li><li>`intlLabel` (Object): localized label for the section, following the  convention, with:<ul><li>`id`: id used to insert the localized label</li><li>`defaultMessage`: default label for the section</li></ul></li></ul> |
| second argument | Array of Objects | Links included in the section                                                                                                                                                                                                                                                                                                 |

:::note
`intlLabel.id` are ids used in translation files (`[plugin-name]/admin/src/translations/[language].json`)
:::

**Example:**

```jsx title="my-plugin/admin/src/index.js"

const myComponent = async () => {
  const component = await import(
    /* webpackChunkName: "users-providers-settings-page" */ './pages/Providers'
  );

  return component;
};

  register(app) {
    app.createSettingSection(
      { id: String, intlLabel: { id: String, defaultMessage: String } }, // Section to create
      [
        // links
        {
          intlLabel: { id: String, defaultMessage: String },
          id: String,
          to: String,
          Component: myComponent,
          permissions: Object[],
        },
      ]
    );
  },
};
```

#### addSettingsLink()

**Type**: `Function`

Add a unique link to an existing settings section.

**Example:**

```jsx title="my-plugin/admin/src/index.js"

const myComponent = async () => {
  const component = await import(
    /* webpackChunkName: "users-providers-settings-page" */ './pages/Providers'
  );

  return component;
};

  bootstrap(app) {
		// Adding a single link
		app.addSettingsLink(
		 'global', // id of the section to add the link to
			{
				intlLabel: { id: String, defaultMessage: String },
				id: String,
				to: String,
				Component: myComponent,
				permissions: Object[],
        licenseOnly: true, // mark the feature as a paid one not available in your license
			}
    )
  }
}
```

#### addSettingsLinks()

**Type**: `Function`

Add multiple links to an existing settings section.

**Example:**

```jsx title="my-plugin/admin/src/index.js"

const myComponent = async () => {
  const component = await import(
    /* webpackChunkName: "users-providers-settings-page" */ './pages/Providers'
  );

  return component;
};

  bootstrap(app) {
    // Adding several links at once
    app.addSettingsLinks(
      'global', // id of the section to add the link in
        [{
          intlLabel: { id: String, defaultMessage: String },
          id: String,
          to: String,
          Component: myComponent,
          permissions: Object[],
          licenseOnly: true, // mark the feature as a paid one not available in your license
        }]
    )
  }
}
```

### Injection Zones API

Injection zones refer to areas of a view's layout where a plugin allows another to inject a custom React component (e.g. a UI element like a button).

Plugins can use:

* Strapi's [predefined injection zones](#using-predefined-injection-zones) for the Content Manager,
* or custom injection zones, created by a plugin

:::note
Injection zones are defined in the [register()](#register) lifecycle but components are injected in the [bootstrap()](#bootstrap) lifecycle.
:::

#### Using predefined injection zones

Strapi admin panel comes with predefined injection zones so components can be added to the UI of the [Content Manager](/cms/intro):

<!-- TODO: maybe add screenshots once the design system is ready? -->

| View      | Injection zone name & Location                                                                                                                                            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| List view | `actions`: sits between Filters and the cogs icon
| Edit view | `right-links`: sits between "Configure the view" and "Edit" buttons                       |

#### Creating a custom injection zone

To create a custom injection zone, declare it as a `` React component with an `area` prop that takes a string with the following naming convention: `plugin-name.viewName.injectionZoneName`.

#### Injecting components

A plugin has 2 different ways of injecting a component:

* to inject a component from a plugin into another plugin's injection zones, use the `injectComponent()` function
* to specifically inject a component into one of the Content Manager's [predefined injection zones](#using-predefined-injection-zones), use the `getPlugin('content-manager').injectComponent()` function instead

Both the `injectComponent()` and `getPlugin('content-manager').injectComponent()` methods accept the following arguments:

| Argument        | Type   | Description                                                                                                                                                                   |
| --------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| first argument  | String | The view where the component is injected
| second argument | String | The zone where the component is injected
| third argument  | Object | An object with the following keys:<ul><li>`name` (string): the name of the component</li><li>`Component` (function or class): the React component to be injected</li></ul> |

<details>
<summary>Example: Inject a component in the informations box of the Edit View of the Content Manager:</summary>

```jsx title="my-plugin/admin/src/index.js"

  bootstrap(app) {
    app.getPlugin('content-manager').injectComponent('editView', 'informations', {
      name: 'my-plugin-my-compo',
      Component: () => 'my-compo',
    });
  }
}
```

</details>

<details>
<summary>Example: Creating a new injection zone and injecting it from a plugin to another one:</summary>

```jsx title="my-plugin/admin/src/injectionZones.js"
// Use the injection zone in a view

const HomePage = () => {
  return (
    <main>
      <h1>This is the homepage</h1>
	    
    </main>
  );
};
```

```jsx title="my-plugin/admin/src/index.js"
// Declare this injection zone in the register lifecycle of the plugin

  register() {
    app.registerPlugin({
      // ...
      injectionZones: {
        homePage: {
          right: []
        }
      }
    });
  },
}
```

```jsx title="my-other-plugin/admin/src/index.js"
// Inject the component from a plugin in another plugin

  register() {
    // ...
  },
  bootstrap(app) {
    app.getPlugin('my-plugin').injectComponent('homePage', 'right', {
      name: 'my-other-plugin-component',
      Component: () => 'This component is injected',
    });
  }
};
```

</details>

#### Accessing data with the `useContentManagerContext` React hook

Once an injection zone is defined, the component to be injected in the Content Manager can have access to all the data of the Edit View through the `useContentManagerContext` React hook.

<details>
<summary>Example of a basic component using the 'useContentManagerContext' hook</summary>

```js

  unstable_useContentManagerContext as useContentManagerContext,
} from '@strapi/strapi/admin';

const MyCompo = () => {
  const {
    slug,
    isCreatingEntry,
    isSingleType,
    hasDraftAndPublish,
    layout,
    components,
    contentType,
    form,
    model,
    collectionType,
    id,
  } = useContentManagerContext();

  // Form state and handlers
  const {
    initialValues,
    values,
    onChange,
  } = form;

  /**
   * Layout structure:
   *
   * `layout` is grouped by Content Manager views.
   *
   * - layout.edit.layout     → edit view layout definition
   * - layout.edit.components → component layouts used in the edit view
   * - layout.list.layout     → list view layout definition
   */
  const {
    edit: { layout: editLayout, components: editComponents },
    list: { layout: listLayout },
  } = layout;

  return null;
};

```

</details>

### Reducers API

Reducers are  reducers that can be used to share state between components. Reducers can be useful when:

* Large amounts of application state are needed in many places in the application.
* The application state is updated frequently.
* The logic to update that state may be complex.

Reducers can be added to a plugin interface with the `addReducers()` function during the [`register`](#register) lifecycle.

A reducer is declared as an object with this syntax:

**Example:**

```js title="my-plugin/admin/src/index.js"

const reducers = {
  // Reducer Syntax
  [`${pluginId}_exampleReducer`]: exampleReducer
}

  register(app) {
    app.addReducers(reducers)
  },
  bootstrap() {},
};

```

### Hooks API

The Hooks API allows a plugin to create and register hooks, i.e. places in the application where plugins can add personalized behavior.

Hooks should be registered during the [bootstrap](#bootstrap) lifecycle of a plugin.

Hooks can then be run in series, in waterfall or in parallel:

* `runHookSeries` returns an array corresponding to the result of each function executed, ordered
* `runHookParallel` returns an array corresponding to the result of the promise resolved by the function executed, ordered
* `runHookWaterfall` returns a single value corresponding to all the transformations applied by the different functions starting with the initial value `args`.

<details>
<summary>Example: Create a hook in a plugin and use it in another plugin</summary>

```jsx title="my-plugin/admin/src/index.js"
// Create a hook in a plugin

  register(app) {
    app.createHook('My-PLUGIN/MY_HOOK');
  }
}

```

```jsx title="my-other-plugin/admin/src/index.js"
// Use the hook in another plugin

  bootstrap(app) {
    app.registerHook('My-PLUGIN/MY_HOOK', (...args) => {
      console.log(args)

      // important: return the mutated data
      return args
    });

    app.registerPlugin({...})
  }
}
```

</details>

#### Predefined hooks

Strapi includes a predefined `Admin/CM/pages/ListView/inject-column-in-table` hook that can be used to add or mutate a column of the List View of the [Content Manager](/cms/intro):

```jsx
runHookWaterfall(INJECT_COLUMN_IN_TABLE, {
	displayedHeaders: ListFieldLayout[],
	layout: ListFieldLayout,
});
```

```tsx
interface ListFieldLayout {
  /**
   * The attribute data from the content-type's schema for the field
   */
  attribute: Attribute.Any | { type: 'custom' };
  /**
   * Typically used by plugins to render a custom cell
   */
  cellFormatter?: (
    data: Document,
    header: Omit<ListFieldLayout, 'cellFormatter'>,
    { collectionType, model }: { collectionType: string; model: string }
  ) => React.ReactNode;
  label: string | MessageDescriptor;
  /**
   * the name of the attribute we use to display the actual name e.g. relations
   * are just ids, so we use the mainField to display something meaninginful by
   * looking at the target's schema
   */
  mainField?: string;
  name: string;
  searchable?: boolean;
  sortable?: boolean;
}

interface ListLayout {
  layout: ListFieldLayout[];
  components?: never;
  metadatas: {
    [K in keyof Contracts.ContentTypes.Metadatas]: Contracts.ContentTypes.Metadatas[K]['list'];
  };
  options: LayoutOptions;
  settings: LayoutSettings;
}

type LayoutOptions = Schema['options'] & Schema['pluginOptions'] & object;

interface LayoutSettings extends Contracts.ContentTypes.Settings {
  displayName?: string;
  icon?: never;
}
```

Strapi also includes a `Admin/CM/pages/EditView/mutate-edit-view-layout` hook that can be used to mutate the Edit View  of the [Content Manager](/cms/intro):

```tsx
interface EditLayout {
  layout: Array<Array<EditFieldLayout[]>>;
  components: {
    [uid: string]: {
      layout: Array<EditFieldLayout[]>;
      settings: Contracts.Components.ComponentConfiguration['settings'] & {
        displayName?: string;
        icon?: string;
      };
    };
  };
  metadatas: {
    [K in keyof Contracts.ContentTypes.Metadatas]: Contracts.ContentTypes.Metadatas[K]['edit'];
  };
  options: LayoutOptions;
  settings: LayoutSettings;
}

interface EditFieldSharedProps extends Omit<InputProps, 'hint' | 'type'> {
  hint?: string;
  mainField?: string;
  size: number;
  unique?: boolean;
  visible?: boolean;
}

/**
 * Map over all the types in Attribute Types and use that to create a union of new types where the attribute type
 * is under the property attribute and the type is under the property type.
 */
type EditFieldLayout = {
  [K in Attribute.Kind]: EditFieldSharedProps & {
    attribute: Extract<Attribute.Any, { type: K }>;
    type: K;
  };
}[Attribute.Kind];

type LayoutOptions = Schema['options'] & Schema['pluginOptions'] & object;

interface LayoutSettings extends Contracts.ContentTypes.Settings {
  displayName?: string;
  icon?: never;
}
```

:::note
`EditViewLayout` and `ListViewLayout` are parts of the `useDocumentLayout` hook (see ).
:::