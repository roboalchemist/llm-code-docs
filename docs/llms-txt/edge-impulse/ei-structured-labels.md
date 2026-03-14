# Source: https://docs.edgeimpulse.com/tools/specifications/data-annotation/ei-structured-labels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edge Impulse structured labels

The Edge Impulse structured labels acquisition format, `structured_labels.labels`, provides a simple and intuitive way to store files and associated labels when you want to upload [multi-label](/studio/projects/data-acquisition/multi-label) samples using the [Ingestion API](/apis/ingestion). The structure and organization are designed to provide clear, index-based labeling for various segments of a data file.

<Info>
  **Associated tutorial**

  For a better understanding, view the [Ingest structured label data](/tutorials/tools/apis/ingestion/ingest-structured-label-data) tutorial.
</Info>

## File structure

The file follows a JSON format, with the following structure:

* `version`:  Indicates the version of the label format.
* `type`: Specifies the type of labeling method - use `structured-labels`.
* `structuredLabels`: This is an object that maps file names to arrays of labels. Where each key represents the name of a file, and its value is an array of objects, each containing:
  * `startIndex` and `endIndex` (milliseconds): These keys define the start and end of the segment within the file that the label applies to, allowing for precise segmentation of data. Note that no missing values are allowed. e.g. the next segment after `"endIndex": 300` needs to be `"startIndex": 301`
  * `label`: A string that represents the label assigned to the range between `startIndex` and `endIndex`.

## File example

```json  theme={"system"}
{
    "version": 1,
    "type": "structured-labels",
    "structuredLabels": {
        "sample.3.json": [{
            "startIndex": 0,
            "endIndex": 300,
            "label": "first_label"
        }, {
            "startIndex": 301,
            "endIndex": 621,
            "label": "second_label"
        }]
    }
}
```


Built with [Mintlify](https://mintlify.com).