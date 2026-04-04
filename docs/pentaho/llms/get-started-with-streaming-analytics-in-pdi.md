# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/streaming-analytics/get-started-with-streaming-analytics-in-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/streaming-analytics/get-started-with-streaming-analytics-in-pdi.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/streaming-analytics/get-started-with-streaming-analytics-in-pdi.md

# Get started with streaming analytics in PDI

Pentaho Data Integration (PDI) products are designed to work as if data flows like running water. You can think of PDI as a series of pipes through which water flows and is joined and mixed with other flows. No matter how big the source, the water keeps flowing, such that all the data will be processed if the data keeps flowing. The size of the “pipe” in PDI is directly linked to the number of data records and to the amount of memory needed to hold all those records. The key to successfully transforming your data with high performance is to understand which PDI steps may increase and speed up the flow.

You can develop a PDI transformation that is always waiting for new data. All the steps continue running, awaiting new data. In this transformation, the input steps ingest data records in PDI from the stream. Once ingested, you can process the data to refine it. After processing, you can push it back into the stream or retain it for analysis.
