# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/exporter/MultiPageVerticalExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/exporter/MultiPageVerticalExporter.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/exporter/MultiPageVerticalExporter.md

# [MultiPageVerticalExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/MultiPageVerticalExporter)

A vertical multiple page exporter. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) feature to export to multiple pages. Content will be scaled in a horizontal direction to fit the page.

You do not need to use this class directly.

### Extending exporter

```
class MyMultiPageVerticalExporter extends MultiPageVerticalExporter {
    // type is required for exporter
    static get type() {
        return 'mymultipageverticalexporter';
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
            exporters : [MyMultiPageVerticalExporter]
        }
    }
});

// run export with the new exporter
gantt.features.pdfExport.export({ exporter : 'mymultipageverticalexporter' });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMultiPageVerticalExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/MultiPageVerticalExporter#property-isMultiPageVerticalExporter)
Identifies an object as an instance of [MultiPageVerticalExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/MultiPageVerticalExporter) class, or subclass thereof.

[isMultiPageVerticalExporter](https://bryntum.com/docs/gantt/api/Gantt/feature/export/exporter/MultiPageVerticalExporter#property-isMultiPageVerticalExporter-static)
Identifies an object as an instance of [MultiPageVerticalExporter](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/exporter/MultiPageVerticalExporter) class, or subclass thereof.
