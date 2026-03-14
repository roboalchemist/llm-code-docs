# Source: https://docs.edgeimpulse.com/tools/specifications/data-acquisition/csv.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CSV

You can import data in CSV format using either the upload functionality in the Studio (Go to **Data acquisition**, then press the upload icon) or through the [Edge Impulse CLI](/tools/clis/edge-impulse-cli/uploader).

The format below is the default format used by our [Ingestion API](/apis/ingestion). If you need more flexibility, the [CSV Wizard](/studio/projects/data-acquisition/csv-wizard) feature can help you to set a CSV parser to easily import CSV files formatted differently.

## CSV format

Edge Impulse requires CSV data to be stored in a particular format. You'll need to create one CSV file per sample (e.g. a machine with a fault state). The first row should be a header describing the sensor axes, and each row should be a single reading at a particular time. For multi-axis, time-series data, the first column name **must** be `timestamp` in millisecond format. It should have **constant intervals** between lines (ie: 16 below), the data ingestion service will infer the sampling frequency from the intervals. For example, this is data from an accelerometer:

```text  theme={"system"}
timestamp,accX,accY,accZ
0,4.220828473773600,1.8800472920291100,-16.89228981323240
16,4.471770735278730,2.0017025177553300,-17.887080018505500
32,4.31928972478658,2.4953566802978500,-18.926163539013300
48,4.648792312787470,2.958335718591510,-18.5336641043514
64,4.773739711926880,2.719663740594690,-18.800019623565700
80,4.653879991315310,2.6865938301637800,-19.98305510341230
```

For a single, multi-axis reading (i.e. something that is not time-series data), you can omit the timestamp. Note that you must have 1 header row and only 1 data row. This is an example from a single, triple-axis accelerometer:

```text  theme={"system"}
accX,accY,accZ
4.220828473773600,1.8800472920291100,-16.89228981323240
```

## CSV filename

If you prefix the file name with the name of the label, the uploader will automatically assign the right labels to your data. The prefix should end with a period before the sample name in the following format:

```text  theme={"system"}
<label>.<unique-id>.csv
```

For example, `faultstate1.sample0.csv` will tell the Studio that the containing data should have the label `faultstate1`.

## Example

[This repository](https://github.com/edgeimpulse/example-data-collection-csv) provides examples that show how to save data in CSV format to be uploaded to Edge Impulse.


Built with [Mintlify](https://mintlify.com).