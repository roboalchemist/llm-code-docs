# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/feature/export/Print.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/Print.md

# Source: https://bryntum.com/products/gantt/docs-llm/api/Gantt/feature/export/Print.md

# [Print](https://bryntum.com/docs/gantt/api/Gantt/feature/export/Print)

Allows printing Gantt contents using browser print dialog.

This feature is based on [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) with only difference that instead of sending request to a backend it renders content to an IFrame element and requests print dialog for it. For more details about preparing HTML for printing, please refer to the [PdfExport](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/PdfExport) docs.

Usage
-----

```
const gantt = new Gantt({
    features : {
        print : true
    }
})

// Opens popup allowing to customize print settings
gantt.features.print.showPrintDialog();

// Simple print
gantt.features.print.print({
    columns : scheduler.columns.map(c => c.id)
});
```

This feature is **disabled** by default. For info on enabling it, see [GridFeatures](https://bryntum.com/docs/gantt/api/#Grid/view/mixin/GridFeatures).

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPrint](https://bryntum.com/docs/gantt/api/Gantt/feature/export/Print#property-isPrint)
Identifies an object as an instance of [Print](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/Print) class, or subclass thereof.

[isPrint](https://bryntum.com/docs/gantt/api/Gantt/feature/export/Print#property-isPrint-static)
Identifies an object as an instance of [Print](https://bryntum.com/docs/gantt/api/#Gantt/feature/export/Print) class, or subclass thereof.
