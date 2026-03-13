# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/PdfExport.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/PdfExport.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/PdfExport.md

# [PdfExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/PdfExport)

Generates PDF/PNG files from the Gantt component.

![Gantt Export dialog](https://bryntum.com/docs/gantt/api/Gantt/gantt-export-dialog.png)

A server-side service is required to perform the export operation. Check out PDF Export Server documentation and installation steps [here](https://bryntum.com/docs/gantt/api/https://github.com/bryntum/pdf-export-server#pdf-export-server)

When your server is up and running, it listens to requests. The Export feature sends a request to the specified URL with the HTML fragments. The server generates a PDF (or PNG) file and returns a download link (or binary, depending on [sendAsBinary](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport#config-sendAsBinary) config). Then the Export feature opens the link in a new tab and the file is automatically downloaded by your browser. This is configurable, see [openAfterExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport#config-openAfterExport) config.

The [exportServer](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport#config-exportServer) URL must be configured. The URL can be localhost if you start the server locally, or your remote server address.

Usage
-----

```
const gantt = new Gantt({
    features : {
        pdfExport : {
            exportServer : 'http://localhost:8080' // Required
        }
    }
})

// Opens popup allowing to customize export settings
gantt.features.pdfExport.showExportDialog();

// Simple export
gantt.features.pdfExport.export({
    // Required, set list of column ids to export
    columns : gantt.columns.map(c => c.id)
}).then(result => {
    // Response instance and response content in JSON
    let { response, responseJSON } = result;
});
```

Configuring the export dialog
-----------------------------

To learn about how to customize the export dialog and its default widgets, please refer to the [SchedulerExportDialog](https://bryntum.com/docs/gantt/api/#Scheduler/view/export/SchedulerExportDialog) which provides a 'ref' identifier for each child widget so that you can customize them all based on your requirements.

Loading resources
-----------------

If you face a problem with loading resources when exporting, the cause might be that the application and the export server are hosted on different servers. This is due to [Cross-Origin Resource Sharing](https://bryntum.com/docs/gantt/api/https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS). There are 2 options how to handle this:

* Allow cross-origin requests from the server where your export is hosted to the server where your application is hosted;
* Copy all resources keeping the folder hierarchy from the server where your application is hosted to the server where your export is hosted and setup paths using [translateURLsToAbsolute](https://bryntum.com/docs/gantt/api/#Grid/feature/export/PdfExport#config-translateURLsToAbsolute) config and configure the export server to give access to the path:

```
const gantt = new Gantt({
    features : {
        pdfExport : {
            exportServer : 'http://localhost:8080',
            // '/resources' is hardcoded in WebServer implementation
            translateURLsToAbsolute : 'http://localhost:8080/resources'
        }
    }
})
```

```
// Following path would be served by this address: http://localhost:8080/resources/
node ./src/server.js -h 8080 -r web/application/styles
```

where `web/application/styles` is the physical root location of the copied resources, for example:

![Export server structure with copied resources](https://bryntum.com/docs/gantt/api/Grid/export-server-resources.png)

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPdfExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/PdfExport#property-isPdfExport)
Identifies an object as an instance of [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) class, or subclass thereof.

[isPdfExport](https://bryntum.com/docs/gantt/api/Gantt/feature/export/PdfExport#property-isPdfExport-static)
Identifies an object as an instance of [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) class, or subclass thereof.
