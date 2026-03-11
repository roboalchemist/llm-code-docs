# Source: https://directus.io/docs/raw/guides/content/visual-editor/frontend-library.md

# Frontend Library

> A library that allows your website to communicate with your Directus project and enables Visual Editing.

You will make use of the Visual Editing Frontend Library [available via NPM](https://www.npmjs.com/package/@directus/visual-editing) to ensure communication between your website’s HTML elements and the Directus visual editor module. This is done through data attributes and helper functions built into the library and imported into your website.

```bash
npm install @directus/visual-editing
```

## API

The visual editing library consists of a few imported methods, only one of which is required to make the basic functionality work.

<table>
<thead>
  <tr>
    <th>
      Method
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Options
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        apply()
      </code>
    </td>
    
    <td>
      Connects each <code>
        data-directus
      </code>
      
       attribute to your Directus instance. This is required.
    </td>
    
    <td>
      <code>
        directusUrl
      </code>
      
      , <code>
        elements
      </code>
      
      , <code>
        customClass
      </code>
      
      , <code>
        onSaved
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        setAttr()
      </code>
    </td>
    
    <td>
      Helper function for dynamically generating <code>
        data-directus
      </code>
      
       attributes.
    </td>
    
    <td>
      <code>
        collection
      </code>
      
      , <code>
        item
      </code>
      
      , <code>
        fields
      </code>
      
      , <code>
        mode
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        remove()
      </code>
    </td>
    
    <td>
      Removes all elements.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        disable()
      </code>
    </td>
    
    <td>
      Temporarily disable all elements. Re-enable those elements with returned <code>
        enable()
      </code>
      
       function <code>
        const { enable } = disable();
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:warning-rounded" color="warning">

**Client-side Library**
Since this is a client-side library, be sure to run its methods only in the client environment and not on the server.

</callout>

## Configuring Attributes

The association between individual website elements and Directus collections and items is made through `data-directus` attributes rendered within the HTML of your website.

The preferred method for generating your `data-directus` attributes is by using the included `setAttr` helper method in order to render these attributes dynamically.

For example when using `setAttr` in Vue:

```vue
<template>
    <h1 :data-directus="setAttr({ collection: 'posts', item: post.id, fields: 'title',
    mode: 'popover' })">
        {{ post.title }}
    </h1>
</template>
```

The generated attribute will be:

```html
<h1 data-directus="collection:posts;item:12;fields:title;mode:popover">
  I Love Visual Editing
</h1>
```

<callout icon="material-symbols:info-outline">

The `fields` property in the `setAttr` function can also accept an array of strings, which will render a comma separated list like: `data-directus="collection:posts;item:12;fields:title,subtitle,slug"`

</callout>

<table>
<thead>
  <tr>
    <th>
      Option
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
        collection
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      Name of the relevant collection. This is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        item
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
      
      , <code>
        number
      </code>
    </td>
    
    <td>
      Primary key of the item. This is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        fields
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
      
      , <code>
        string[]
      </code>
    </td>
    
    <td>
      The specific fields to show when editing. Optional, otherwise all fields will be shown.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        mode
      </code>
    </td>
    
    <td>
      <code>
        'drawer'
      </code>
      
      , <code>
        'modal'
      </code>
      
      , <code>
        'popover'
      </code>
    </td>
    
    <td>
      Determines how the edit field(s) should be rendered. Optional, but defaults to <code>
        'drawer'
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:warning-rounded" color="warning">

**Be careful with sensitive data in attributes**
It is recommended that you conditionally render sensitive `data-directus` attributes only when your webpage renders within the Directus visual editor in order to avoid leaking this data publicly. <br />

<br />

 There are a number of ways to achieve this. For example you might develop your website to only render sensitive attributes in the presence of a certain query string included in your visual editor URL settings, for example `?visual-editing=true&token=123`.

</callout>

## Connecting to Directus

Once all your `data-directus` attributes have been configured, you need to call the `apply()` method on the page. This method will establish the connection to Directus and make your editable elements interactive within the visual editor module. This must be done only after all the relevant elements on the page have fully mounted or rendered with their generated attributes.

```js
apply({ directusUrl: 'http://localhost:8000' });
```

<table>
<thead>
  <tr>
    <th>
      Option
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
        directusUrl
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      URL of your Directus instance. This is required.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        elements
      </code>
    </td>
    
    <td>
      <code>
        HTMLElement
      </code>
      
      , <code>
        HTMLElement[]
      </code>
    </td>
    
    <td>
      Could have one or more elements. If the elements themselves don’t contain a <code>
        data-directus
      </code>
      
       attribute, their children will be selected. Optionally, otherwise will be applied to all elements on page.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        customClass
      </code>
    </td>
    
    <td>
      <code>
        string[]
      </code>
    </td>
    
    <td>
      Adds a class to overlay elements to enable custom styles. Optional.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        onSaved
      </code>
    </td>
    
    <td>
      <code>
        (data) => void
      </code>
    </td>
    
    <td>
      Callback function called after the fields are saved in Directus. Optional, otherwise current page will be reloaded using <code>
        window.location.reload()
      </code>
      
      .
    </td>
  </tr>
</tbody>
</table>

The `apply()` method also returns the `remove`, `enable` and `disable` methods. These can then be used on the selected elements in question. Make sure to await them.

```js
const { disable, enable, remove } = await apply({ directusUrl });
```

Once you specify an `elements` property, the `customClass` and `onSaved` options cannot be overridden afterwards. You can use the `elements` property to scope a section of your page and apply different options than you might have applied with a previous `apply` call that already included those elements. The returned object can also be used to disable, enable, or remove these scoped elements separately from the other elements. To customize scoped elements see the [customization](/guides/content/visual-editor/customization) page.

```js
const scopedElements = document.querySelector('.header');
const { disable, enable, remove } = await apply({
  directusUrl,
  elements: scopedElements,
  customClass: 'my-scoped-elements',
  onSaved: ({ collection, item, payload }) => refreshData(),
});
```

The optional `onSaved` callback function of the `apply()` method provides an object as a parameter which properties may be useful.

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
        collection
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
    </td>
    
    <td>
      Name of the relevant collection.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        item
      </code>
    </td>
    
    <td>
      <code>
        string
      </code>
      
      , <code>
        number
      </code>
    </td>
    
    <td>
      Primary key of the item.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        payload
      </code>
    </td>
    
    <td>
      <code>
        Record<string, any>
      </code>
    </td>
    
    <td>
      The changed values.
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:warning-rounded" color="warning">

**Client-side Navigation**
It is recommended to call the global `remove()` method on client-side navigation to avoid unnecessarily bloating the underlying store.

</callout>

<callout icon="material-symbols:warning-rounded" color="warning">

**Content Security Policy**
If you have CSP configured, be sure to make your site available for use inside an iFrame in Directus. If you’re unsure where your CSP is defined, check your web server configuration files, your site’s build configuration, or your hosting platform’s security settings.

</callout>

<callout icon="material-symbols:info">

**Usage with Directus Cloud and local development**
Connecting your local development environment to a Directus Cloud Starter or Professional instance must be done by exposing your localhost to the web through an SSL secured connection. There are multiple ways to achieve this:

- Using a tool like [Ngrok](https://ngrok.com/), [serveo](https://serveo.net/), or [localtunnel](https://theboroer.github.io/localtunnel-www/)
- Creating and using your own SSL certificate. In the case of Vite this can be done with an [SSL plugin](https://github.com/vitejs/vite-plugin-basic-ssl)

</callout>

## Field Access Checks

When used with Directus 11.16.0+, the library validates field-level permissions before activating editable elements. After `apply()` is called, elements go through a two-phase lifecycle:

1. **Construction** — elements are registered based on `data-directus` attributes
2. **Activation** — Directus verifies the current user's permissions and only activates elements for fields the user can edit

Elements that fail the permission check remain inert — no overlay, hover listeners, or click handlers are attached.

<callout icon="material-symbols:warning-rounded" color="warning">

**Minimum Version Requirement**
Field access checks require `@directus/visual-editing` v2.0.0+ and Directus 11.16.0+. Without a compatible Directus instance responding to the permission check, elements will not display edit overlays.

</callout>

## Usage in Non-JS Environments

Given this library is built as a Node package, environments that can’t take advantage of NPM will need to take a slightly different approach to including the functionality in their websites.

```js
<script src="https://unpkg.com/@directus/visual-editing" type="text/javascript"></script>
```

<callout icon="material-symbols:info-outline">

More information can be found at [https://unpkg.com](https://unpkg.com).

</callout>

```js
<script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function () {
        DirectusVisualEditing.apply({ directusUrl: 'http://localhost:8000' });
    });
</script>
```
