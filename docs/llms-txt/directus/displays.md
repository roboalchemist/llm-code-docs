# Source: https://directus.io/docs/raw/guides/extensions/app-extensions/displays.md

# Inline Displays

> Displays are used to display a single value throughout the Data Studio.

Displays are small components that are used to display a single value throughout the Data Studio.

Displays receive a single value and any custom display options that are defined in the display entrypoint. They are then expected to render the value in a user-friendly way.

![A Datetime display in the content module](/img/99a21abb-a866-4766-bbce-0ed13295112b.webp)

<partial content="extensions-app">



</partial>

## Display Entrypoint

The `index.js` or `index.ts` file exports an object that is read by Directus. It contains properties that control how a display is displayed throughout the Data Studio, which options are available, and the actual Vue component that will be loaded.

### Entrypoint Example

```js
import { defineInterface } from '@directus/extensions-sdk'
import DisplayComponent from './display.vue';

export default defineInterface({
    id: 'custom',
    name: 'Custom',
    icon: 'box',
    description: 'This is my custom display!',
    component: DisplayComponent,
    options: null,
    types: ['string'],
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
      The displayed name for this layout in the Data Studio.
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
        description
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      A description of this display shown in the Data Studio. Maximum 80 characters.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        component
      </code>
    </td>
    
    <td>
      component
    </td>
    
    <td>
      A reference to your display component.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        options
      </code>
    </td>
    
    <td>
      object | component
    </td>
    
    <td>
      The options of your display. Can be either an options object or a dedicated Vue component.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        types
      </code>
    </td>
    
    <td>
      array
    </td>
    
    <td>
      All <a href="/guides/data-model/fields">
        types
      </a>
      
       supported by the display.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        localTypes
      </code>
    </td>
    
    <td>
      array
    </td>
    
    <td>
      All local types supported by this display. Accepts <code>
        standard
      </code>
      
      , <code>
        file
      </code>
      
      , <code>
        files
      </code>
      
      , <code>
        m2o
      </code>
      
      , <code>
        o2m
      </code>
      
      , <code>
        m2m
      </code>
      
      , <code>
        m2a
      </code>
      
      , <code>
        presentation
      </code>
      
      , <code>
        translations
      </code>
      
       and <code>
        group
      </code>
      
      . Defaults to <code>
        standard
      </code>
      
      .
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fields
      </code>
    </td>
    
    <td>
      array | function
    </td>
    
    <td>
      If this option is set, the display will fetch relational fields. Can either be an array of fields or a function that returns an array of fields.
    </td>
  </tr>
</tbody>
</table>

<partial content="extensions-uid">



</partial>

## Display Component

The display component is a Vue component that will be rendered in the Data Studio whenever your display is used to show the value of a field. Data from the entrypoint are passed in as props.

### Component Example

This example assumes there is an item in the entrypoint’s `options` array with a `field` value of `url`.

```vue
<template>
    <div>Value: {{ value }}</div>
</template>

<script>
export default {
    props: {
        value: {
            type: String,
            default: null,
        },
    },
};
</script>
```

The current value of the field is provided to the component via the `value` prop. If you use the `fields` option to fetch relational fields, the `value` prop will be an object with the requested fields as keys and their respective values.

### Props

<table>
<thead>
  <tr>
    <th>
      Prop
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
        value
      </code>
    </td>
    
    <td>
      any
    </td>
    
    <td>
      The value of the field.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        interface
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      The interface of the field.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        interfaceOptions
      </code>
    </td>
    
    <td>
      object
    </td>
    
    <td>
      The options for the field's interface.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        type
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      The type of the field.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        collection
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      The collection name of the field.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        field
      </code>
    </td>
    
    <td>
      string
    </td>
    
    <td>
      The key of the field.
    </td>
  </tr>
</tbody>
</table>

### Functional Component

Instead of defining the component inside a separate Vue file, you can use a functional component. This allows you to make small displays that don't need a full component.

```js
import { defineInterface } from '@directus/extensions-sdk'

export default defineInterface({
    id: 'custom',
    name: 'Custom',
    icon: 'box',
    description: 'This is my custom display!',
    component: function ({ value }) {
        return value.toLowerCase();
    },
    options: null,
    types: ['string'],
});
```

<partial content="extensions-app-internals">



</partial>
