# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/mixin/PrintMixin.md

# [PrintMixin](https://bryntum.com/docs/gantt/api/Grid/feature/export/mixin/PrintMixin)

Mixin implementing print functionality to PdfExport feature.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPrintMixin](https://bryntum.com/docs/gantt/api/Grid/feature/export/mixin/PrintMixin#property-isPrintMixin)
Identifies an object as an instance of [PrintMixin](https://bryntum.com/docs/gantt/api/#Grid/feature/export/mixin/PrintMixin) class, or subclass thereof.

[isPrintMixin](https://bryntum.com/docs/gantt/api/Grid/feature/export/mixin/PrintMixin#property-isPrintMixin-static)
Identifies an object as an instance of [PrintMixin](https://bryntum.com/docs/gantt/api/#Grid/feature/export/mixin/PrintMixin) class, or subclass thereof.

## Functions

Functions are methods available for calling on the class

[showPrintDialog](https://bryntum.com/docs/gantt/api/Grid/feature/export/mixin/PrintMixin#function-showPrintDialog)
Shows the [print dialog](https://bryntum.com/docs/gantt/api/#Grid/view/export/ExportDialog)

[print](https://bryntum.com/docs/gantt/api/Grid/feature/export/mixin/PrintMixin#function-print)
Starts the print process. Accepts a config object which overrides any default configs. **NOTE** Component should not be interacted with when print is in progress

[onPrintIFrameLoad](https://bryntum.com/docs/gantt/api/Grid/feature/export/mixin/PrintMixin#function-onPrintIFrameLoad)
This method is called when IFrame is loaded with all the HTML/CSS and is about to be printed. Use it to take control over the page contents.
