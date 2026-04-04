# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/exporter/SinglePageUnscaledExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/exporter/SinglePageUnscaledExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/exporter/SinglePageUnscaledExporter.md

# [SinglePageUnscaledExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/SinglePageUnscaledExporter)

A single page exporter. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) feature to export to single page. Content is exported with dimensions required to fit all requested rows and columns. This allows generating PDF page not constrained by the standard paper formats.

You do not need to use this class directly.

### Extending exporter

```
class MySinglePageExporter extends SinglePageUnscaledExporter {
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

[isSinglePageUnscaledExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/SinglePageUnscaledExporter#property-isSinglePageUnscaledExporter)
Identifies an object as an instance of [SinglePageUnscaledExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/SinglePageUnscaledExporter) class, or subclass thereof.

[isSinglePageUnscaledExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/SinglePageUnscaledExporter#property-isSinglePageUnscaledExporter-static)
Identifies an object as an instance of [SinglePageUnscaledExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/SinglePageUnscaledExporter) class, or subclass thereof.
