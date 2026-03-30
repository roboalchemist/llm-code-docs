# Source: https://directus.io/docs/raw/guides/extensions/app-extensions/modules.md

# Custom Modules

> Modules are top-level areas of the Data Studio, navigated to from the left-hand module bar.

Modules are top-level areas of the Data Studio, navigated to from the left-hand module bar. They will load at the specified routes.

![A module in Directus](/img/7db9b50a-d25b-40b1-86dc-3e09dad388bf.webp)

The Data Studio splits up functionality into modules - the content module, the files module, the user module, the insights module, and the settings module. Extensions can add new modules to the Data Studio.

<callout icon="material-symbols:info-outline">

**Enable the Module**<br />


For the module to appear in the module bar, the extension has to be enabled in your main project settings.

</callout>

<partial content="extensions-app">



</partial>

## Module Entrypoint

The `index.js` or `index.ts` file exports an object that is read by Directus. It contains properties that control how a module is displayed in the module bar, the routes that exist within the module, and the actual Vue component that will be loaded.

## Entrypoint Example

```js
import { defineInterface } from '@directus/extensions-sdk'
import ModuleComponent from './module.vue';

export default defineInterface({
    id: 'custom',
    name: 'Custom',
    icon: 'box',
    routes: [
        {
            path: '',
            component: ModuleComponent,
        },
    ],
});
```

### Properties

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Type
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        id
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      A unique identifier for this extension.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        name
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      The displayed name for this panel in the Data Studio.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        icon
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      An icon name from the <a href="https://fonts.google.com/icons" rel="nofollow">
        Google Material Icons set
      </a>
      
      . Supports filled and outlined variants.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        color
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      A color associated with the module.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        routes
      </code>
    </td>
    
    <td>
      array
    </td>
    
    <td>
      List of routes in the module. The routes are registered as nested routes with the module's <code>
        id
      </code>
      
       serving as the base path.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        hidden
      </code>
    </td>
    
    <td>
      boolean
    </td>
    
    <td>
      A boolean that indicates if the module should be hidden from the module bar.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        preRegisterCheck
      </code>
    </td>
    
    <td>
      function
    </td>
    
    <td>
      A function that receives the current user as the first parameter and the permissions of this user as the second parameter. It should return a boolean indicating success.
    </td>
  </tr>
</tbody>
</table>

<partial content="extensions-uid">



</partial>

### Route Object

The route object uses the same syntax as Vue Router, defining each route as an object.

<table>
<thead>
  <tr>
    <th>
      Property
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        path
      </code>
    </td>
    
    <td>
      The route path without the leading slash.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        component
      </code>
    </td>
    
    <td>
      A Vue component to be rendered for this route.
    </td>
  </tr>
</tbody>
</table>

The `routes` array should contain a root route with an empty path, which will load at the module's base route (the value of the module's `id`). Dynamic portions of the path can be defined using the `:param` syntax.

### Route Component

The module route component will be rendered in the Data Studio when the route is accessed.

```vue
<template>
    <private-view title="My Custom Module">Content goes here...</private-view>
</template>

<script>
export default {};
</script>
```

You can use the globally-registered `private-view` component to get access to Directus' page structure consisting of the module bar, navigation,
sidebar, header, and the main content area. Named slots can be used to add additional content to these areas.

<table>
<thead>
  <tr>
    <th>
      Slot
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        navigation
      </code>
    </td>
    
    <td>
      Adds content to the navigation area of the Directus interface.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        title-outer:prepend
      </code>
    </td>
    
    <td>
      Inserts content before the outer title container in the Directus header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        headline
      </code>
    </td>
    
    <td>
      Displays a headline above the main title in the Directus header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        title
      </code>
    </td>
    
    <td>
      Sets the main title in the Directus header. If not used, <code>
        title:prepend
      </code>
      
       and <code>
        title:append
      </code>
      
       can be used instead.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        title-outer:append
      </code>
    </td>
    
    <td>
      Inserts content after the outer title container in the Directus header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        actions:prepend
      </code>
    </td>
    
    <td>
      Adds content before the action buttons in the Directus header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        actions
      </code>
    </td>
    
    <td>
      Defines the main action buttons in the Directus header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        actions:append
      </code>
    </td>
    
    <td>
      Adds content after the action buttons in the Directus header.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        splitView
      </code>
    </td>
    
    <td>
      Renders content in the split view area (only if the private layout has the split-view prop set to true).
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        sidebar
      </code>
    </td>
    
    <td>
      Populates the sidebar area in the Directus interface.
    </td>
  </tr>
</tbody>
</table>

<partial content="extensions-app-internals">



</partial>
