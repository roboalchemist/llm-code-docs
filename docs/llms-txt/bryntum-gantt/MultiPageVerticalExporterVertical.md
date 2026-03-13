# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/verticalexporter/MultiPageVerticalExporterVertical.md

# [MultiPageVerticalExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/MultiPageVerticalExporterVertical)

A vertical multiple page exporter for Scheduler's vertical mode. Used by the [PdfExport](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/PdfExport) feature to export to multiple pages. Content will be scaled in a horizontal direction to fit the page.

You do not need to use this class directly.

### Extending exporter

```
class MyMultiPageVerticalExporter extends MultiPageVerticalExporterVertical {
    // type is required for exporter
    static type = 'mymultipageverticalexporter';

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
            exporters : [MyMultiPageVerticalExporter]
        }
    }
});

// run export with the new exporter
scheduler.features.pdfExport.export({ exporter : 'mymultipageverticalexporter' });
```

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isMultiPageVerticalExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/MultiPageVerticalExporterVertical#property-isMultiPageVerticalExporterVertical)
Identifies an object as an instance of [MultiPageVerticalExporterVertical](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/verticalexporter/MultiPageVerticalExporterVertical) class, or subclass thereof.

[isMultiPageVerticalExporterVertical](https://bryntum.com/docs/gantt/api/Scheduler/feature/export/verticalexporter/MultiPageVerticalExporterVertical#property-isMultiPageVerticalExporterVertical-static)
Identifies an object as an instance of [MultiPageVerticalExporterVertical](https://bryntum.com/docs/gantt/api/#Scheduler/feature/export/verticalexporter/MultiPageVerticalExporterVertical) class, or subclass thereof.
