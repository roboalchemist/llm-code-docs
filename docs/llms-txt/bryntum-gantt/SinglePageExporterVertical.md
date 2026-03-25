# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/verticalexporter/SinglePageExporterVertical.md

# [SinglePageExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageExporterVertical)

A single page exporter for vertical mode. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/PdfExport) feature to export to single page. Content will be scaled in both directions to fit the page.

You do not need to use this class directly.

### Extending exporter

```
class MySinglePageExporter extends SinglePageExporterVertical {
    // type is required for exporter
    static type = 'mysinglepageexporter';

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
scheduler.features.pdfExport.export({ exporter : 'mysinglepageexporter' });
```

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[centerContentHorizontally](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageExporterVertical#config-centerContentHorizontally)
Set to `true` to center content horizontally on the page

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isSinglePageExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageExporterVertical#property-isSinglePageExporterVertical)
Identifies an object as an instance of [SinglePageExporterVertical](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/verticalexporter/SinglePageExporterVertical) class, or subclass thereof.

[isSinglePageExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/SinglePageExporterVertical#property-isSinglePageExporterVertical-static)
Identifies an object as an instance of [SinglePageExporterVertical](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/verticalexporter/SinglePageExporterVertical) class, or subclass thereof.
