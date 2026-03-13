# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/exporter/ExporterBase.md

# [ExporterBase](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase)

Base class for all exporters

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[translateURLsToAbsolute](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#config-translateURLsToAbsolute)
`true` to replace all linked CSS files URLs to absolute before passing HTML to the server. When passing a string the current origin of the CSS files URLS will be replaced by the passed origin.

For example: css files pointing to /app.css will be translated from current origin to {translateURLsToAbsolute}/app.css

[keepPathName](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#config-keepPathName)
When `true` links are converted to absolute by combining current window location (with replaced origin) with resource link. When false links are converted by combining new origin with resource link (for angular)

[rowReadyCondition](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#config-rowReadyCondition)
A function that determines when to capture the HTML for exported rows. When set to null (the default), the export happens immediately without waiting. The function receives the export configuration as a parameter. The rendering process works in chunks, using the same approach as the Grid component - displaying visible rows with an additional buffer.

Examples:

```
// simple timeout
new Grid({
    features : {
        pdfExport : {
            rowReadyCondition : async () => await new Promise(resolve => setTimeout(resolve, 100))
        }
    }
});

// waiting for a condition
new Grid({
    features : {
        pdfExport : {
            rowReadyCondition : async () => await promiseWithCondition
        }
    }
});
```

[webSocketRequestTimeout](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#config-webSocketRequestTimeout)
Maximum time in ms to wait for the response over the websocket connection

## Properties

Properties are getters/setters or publicly accessible variables on this class

[rowReadyCondition](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#property-rowReadyCondition)
A function that determines when to capture the HTML for exported rows. When set to null (the default), the export happens immediately without waiting. The function receives the export configuration as a parameter. The rendering process works in chunks, using the same approach as the Grid component - displaying visible rows with an additional buffer.

Examples:

```
// simple timeout
new Grid({
    features : {
        pdfExport : {
            rowReadyCondition : async () => await new Promise(resolve => setTimeout(resolve, 100))
        }
    }
});

// waiting for a condition
new Grid({
    features : {
        pdfExport : {
            rowReadyCondition : async () => await promiseWithCondition
        }
    }
});
```

[webSocketRequestTimeout](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#property-webSocketRequestTimeout)
Maximum time in ms to wait for the response over the websocket connection

[stylesheets](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#property-stylesheets)
Returns all style-related tags: `<style>` and `<link rel="stylesheet">`

## Functions

Functions are methods available for calling on the class

[filterStyles](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#function-filterStyles)
This method accepts all stylesheets (link and style tags) which are supposed to be put on the page. Use this hook method to filter or modify them.

```
new Grid({
    features: {
        pdfExport: {
            // filter out inline styles and bootstrap.css
            filterStyles: styles => styles.filter(item => !/(link|bootstrap.css)/.test(item))
        }
    }
});
```

[pageTpl](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#function-pageTpl)
Template of an extracted page.

[measureElement](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#function-measureElement)
Appends generated header/footer element to the document body to measure their height

[export](https://bryntum.com/docs/gantt/api/Grid/feature/export/exporter/ExporterBase#function-export)
When using [WebSockets](https://bryntum.com/docs/gantt/api/#Grid/feature/export/PdfExport#property-webSocketAvailable), it will stream pages to the backend and return link to the generated file. When not using WebSockets, it will return array of objects containing pages HTML
