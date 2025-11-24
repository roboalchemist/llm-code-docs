# Source: https://flatfile.com/docs/embedding/javascript.md

# JavaScript Embedding

> Embed Flatfile using vanilla JavaScript

Embed Flatfile directly into any web application using our JavaScript SDK. This approach works with any framework or vanilla JavaScript setup.

## Quick Links

* [Advanced Configuration](./advanced-configuration) - Complete configuration options reference
* [Server Setup](./server-setup) - Server-side setup for space reuse

## Installation

Add the Flatfile JavaScript SDK to your page:

```html
<script src="https://unpkg.com/@flatfile/javascript/dist/index.js"></script>
```

Or install via npm:

```bash
npm install @flatfile/javascript
```

## Basic Implementation

### 1. HTML Structure

Create a button to trigger the Flatfile embed:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Data Import</title>
    <script src="https://unpkg.com/@flatfile/javascript/dist/index.js"></script>
  </head>
  <body>
    <button id="import-btn">Import Data</button>

    <script>
      // Implementation goes here
    </script>
  </body>
</html>
```

### 2. Initialize Flatfile

```javascript
document.getElementById("import-btn").addEventListener("click", function () {
  window.FlatFileJavaScript.startFlatfile({});
});
```

### 3. Get Your Credentials

**publishableKey**: Get from [Platform Dashboard](https://platform.flatfile.com) → Developer Settings

```javascript
document.getElementById("import-btn").addEventListener("click", function () {
  window.FlatFileJavaScript.startFlatfile({
    publishableKey: "pk_your_publishable_key",
  });
});
```

For detailed authentication and security guidance, see [Advanced Configuration](./advanced-configuration).

## Complete Example

<Note>
  The example below will open an empty space. To create the sheet your users
  should land on, you'll want to create a workbook as shown further down this
  page.
</Note>

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Data Import</title>
    <script src="https://unpkg.com/@flatfile/javascript/dist/index.js"></script>
  </head>
  <body>
    <h1>Welcome to our app</h1>
    <button id="import-btn">Import Data</button>

    <script>
      document
        .getElementById("import-btn")
        .addEventListener("click", function () {
          window.FlatFileJavaScript.startFlatfile({
            publishableKey: "pk_your_publishable_key",
            displayAsModal: true,
          });
        });
    </script>
  </body>
</html>
```

## Creating New Spaces

To create a new Space each time:

1. Add a `workbook` configuration object. Read more about workbooks [here](../core-concepts/workbooks).
2. Optionally [deploy](../core-concepts/listeners) a `listener` for custom data processing. Your listener will contain your validations and transformations

<Note>
  You can also deploy and create your workbook via a server-side listener as
  shown in the above link, rather than passing it in as a client-side property.
</Note>

```javascript
window.FlatFileJavaScript.startFlatfile({
  publishableKey: "pk_your_publishable_key",
  workbook: {
    name: "My Import",
    sheets: [
      {
        name: "Contacts",
        slug: "contacts",
        fields: [
          { key: "name", type: "string", label: "Name" },
          { key: "email", type: "string", label: "Email" },
        ],
      },
    ],
  },
});
```

For detailed workbook configuration, see the [Workbook API Reference](https://reference.flatfile.com/api-reference/workbooks).

## Configuration Options

For complete configuration options including user identity, theming, and advanced features, see [Advanced Configuration](./advanced-configuration).

## Reusing Existing Spaces

To reuse an existing space, you need to set up a server-side component that retrieves the space access token. The basic client-side approach shown above only works for initial space creation.

For space reuse, you'll need:

1. **Server-side setup**: Use your secret key to retrieve the space and its access token
2. **Client-side update**: Use the access token instead of just the publishable key

```javascript
// Client-side: Get space data from your server
const spaceData = await fetch("/api/spaces/us_sp_your_space_id").then((r) =>
  r.json()
);

// Use the space with access token
window.FlatFileJavaScript.startFlatfile({
  space: {
    id: spaceData.id,
    accessToken: spaceData.accessToken, // Retrieved from server
  },
});
```

For complete server-side implementation, see [Server Setup](./server-setup).

## Next Steps

* **Advanced Configuration**: See [Advanced Configuration](./advanced-configuration) for complete options reference
* **Server Setup**: Set up [Server Setup](./server-setup) for space reuse functionality
* **Styling**: Customize the embedded experience in your Platform Dashboard Space settings
* **Data Processing**: Set up Listeners in your Space for custom data transformations
* **API Integration**: Use [Flatfile API](https://reference.flatfile.com) to retrieve processed data

## Example Projects

<CardGroup cols={2}>
  <Card title="Basic JavaScript Example" icon="js" href="https://github.com/FlatFilers/create-flatfile-javascript">
    Complete working example with HTML and JavaScript
  </Card>
</CardGroup>
