# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/verticalexporter/SinglePageUnscaledExporterVertical.md

# [SinglePageUnscaledExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageUnscaledExporterVertical)

A single page exporter for vertical mode. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/PdfExport) feature to export to single page. Content is exported with dimensions required to fit all requested rows and columns. This allows generating PDF page not constrained by the standard paper formats.

You do not need to use this class directly.

### Extending exporter

```
class MySinglePageExporter extends SinglePageUnscaledExporterVertical {
    // type is required for exporter
    static type = 'mysinglepageunscaledexporter';

    get stylesheets() {
        const stylesheets = super.stylesheets;

        stylesheets.forEach(styleNodeOrLinkTag => doSmth(styleNodeOrLinkTag))

        return stylesheets;
    }
}

const scheduler = new Scheduler({
    mode     : 'vertical',
    features : {
        pdfExport : {
            // this export feature is configured with only one exporter
            exporters : [MySinglePageExporter]
        }
    }
});

// run export with the new exporter
scheduler.features.pdfExport.export({ exporter : 'mysinglepageunscaledexporter' });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSinglePageUnscaledExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageUnscaledExporterVertical#property-isSinglePageUnscaledExporterVertical)
Identifies an object as an instance of [SinglePageUnscaledExporterVertical](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/verticalexporter/SinglePageUnscaledExporterVertical) class, or subclass thereof.

[isSinglePageUnscaledExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageUnscaledExporterVertical#property-isSinglePageUnscaledExporterVertical-static)
Identifies an object as an instance of [SinglePageUnscaledExporterVertical](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/verticalexporter/SinglePageUnscaledExporterVertical) class, or subclass thereof.
