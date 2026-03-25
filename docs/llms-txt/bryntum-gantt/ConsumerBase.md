# Source: https://bryntum.com/products/gantt/docs-llm/api/Grid/feature/export/consumer/ConsumerBase.md

# [ConsumerBase](https://bryntum.com/docs/gantt/api/Grid/feature/export/consumer/ConsumerBase)

Base class for consumers of the output from the exporters.

## Functions

Functions are methods available for calling on the class

[start](https://bryntum.com/docs/gantt/api/Grid/feature/export/consumer/ConsumerBase#function-start)
Initiates consumer operation. Exporter will wait for consumer to be ready.

[consumePage](https://bryntum.com/docs/gantt/api/Grid/feature/export/consumer/ConsumerBase#function-consumePage)
Accepts generated page from the exporter. Although declared async, exporter will not wait for consumer to resolve this promise and will keep generating pages.

[end](https://bryntum.com/docs/gantt/api/Grid/feature/export/consumer/ConsumerBase#function-end)
Called after exporter has finished.

[finalize](https://bryntum.com/docs/gantt/api/Grid/feature/export/consumer/ConsumerBase#function-finalize)
Interface for collecting results in an asynchronous manner.
