# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/exporter/MultiPageExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/exporter/MultiPageExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/exporter/MultiPageExporter.md

# [MultiPageExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/MultiPageExporter)

A multiple page exporter. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) feature to export to multiple pages. You do not need to use this class directly.

### Extending exporter

```
class MyMultiPageExporter extends MultiPageExporter {
    // type is required for exporter
    static get type() {
        return 'mymultipageexporter';
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
            exporters : [MyMultiPageExporter]
        }
    }
});

// run export with the new exporter
gantt.features.pdfExport.export({ exporter : 'mymultipageexporter' });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMultiPageExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/MultiPageExporter#property-isMultiPageExporter)
Identifies an object as an instance of [MultiPageExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/MultiPageExporter) class, or subclass thereof.

[isMultiPageExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/MultiPageExporter#property-isMultiPageExporter-static)
Identifies an object as an instance of [MultiPageExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/MultiPageExporter) class, or subclass thereof.
