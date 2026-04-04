# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/exporter/SinglePageExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/exporter/SinglePageExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/exporter/SinglePageExporter.md

# [SinglePageExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/SinglePageExporter)

A single page exporter. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) feature to export to single page. Content will be scaled in both directions to fit the page.

You do not need to use this class directly.

### Extending exporter

```
class MySinglePageExporter extends SinglePageExporter {
    // type is required for exporter
    static get type() {
        return 'mysinglepageexporter';
    }

    get stylesheets() {
        const stylesheets = super.stylesheets;

        stylesheets.forEach(styleNodeOrLinkTag => doSmth(styleNodeOrLinkTag))

        return stylesheets;
    }
}

const gantt = new Gantt({
    features : {
        pdfExport : {
            // this export feature is configured with only one exporter
            exporters : [MySinglePageExporter]
        }
    }
});

// run export with the new exporter
gantt.features.pdfExport.export({ exporter : 'mysinglepageexporter' });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSinglePageExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/SinglePageExporter#property-isSinglePageExporter)
Identifies an object as an instance of [SinglePageExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/SinglePageExporter) class, or subclass thereof.

[isSinglePageExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/SinglePageExporter#property-isSinglePageExporter-static)
Identifies an object as an instance of [SinglePageExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/SinglePageExporter) class, or subclass thereof.
