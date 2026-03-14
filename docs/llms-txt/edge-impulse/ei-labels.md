# Source: https://docs.edgeimpulse.com/tools/specifications/data-annotation/ei-labels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Edge Impulse labels

The Edge Impulse Exporter acquisition format, `info.labels` or `bounding_boxes.labels`, provides a simple and intuitive way to store files and associated labels.

## Directory structure

Directories containing data in this format will take the following structure:

```
.
├── info.labels
└── training
│   ├── info.labels
│   ├── file1.wav
│   ├── file2.wav
│   ├── file3.wav
│   ...
│   └── file100.jpg
└── testing
    ├── info.labels
    ├── file101.wav
    ├── file102.wav
    ...
    └── file120.wav

2 directories, 123 files
```

The subdirectories contain files in any Edge Impulse-supported format. Each file represents a sample and is associated with its respective labels in the `info.labels` file.

The `info.labels` file can be located in each subdirectory or at the folder root.

## File structure

The file follows a JSON format, with the following structure:

* `version`: Indicates the version of the label format.
* `files`: A list of objects, where each object represents a supported file format and its associated labels.
  * `path`: The file path.
  * `name`: The sample name (does not have to match the file name).
  * `category`: Indicates whether the image belongs to the training or testing set.
  * `label` (optional): Provides information about the labeled objects.
    * `type`: Specifies the type of label - `unlabeled`, `label`, `multi-label`.
    * `label` (optional): The actual label or class name of the sample.
    * `labels` (optional): The labels in the [multi-label format](/studio/projects/data-acquisition/multi-label):
      * `label`: Label for the given period.
      * `startIndex`: Timestamp in milliseconds.
      * `endIndex`: Timestamp in milliseconds.
  * `metadata` (Optional): Additional metadata associated with the image, such as the site where it was collected, the timestamp or any useful information.
  * `boundingBoxes` (Optional): A list of objects, where each object represents a bounding box for an object within the image.
    * `label`: The label or class name of the object within the bounding box.
    * `x`, `y`: The coordinates of the top-left corner of the bounding box.
    * `width`, `height`: The width and height of the bounding box.

## File example

<CodeGroup>
  ```json Single label theme={"system"}
  {
      "version": 1,
      "files": [
          {
              "path": "testing/sample.3.cbor",
              "name": "sample.3.cbor",
              "category": "testing",
              "label": {
                  "type": "label",
                  "label": "first_label"
              }
          }
      ]
  }
  ```

  ```json Multi-label theme={"system"}
  {
      "version": 1,
      "files": [
          {
              "path": "testing/sample_1.json",
              "name": "sample_1",
              "category": "testing",
              "label": {
                  "type": "multi-label",
                  "labels": [
                      {
                          "label": "first_label",
                          "startIndex": 0,
                          "endIndex": 451
                      },
                      {
                          "label": "second_label",
                          "startIndex": 452,
                          "endIndex": 1847
                      }
                  ]
              },
              "metadata": {}
          }
      ]
  }
  ```

  ```json Bounding boxes theme={"system"}
  {
      "version": 1,
      "files": [
          {
              "path": "testing/image_1.jpg",
              "name": "image_1",
              "category": "testing",
              "label": {
                  "type": "label",
                  "label": "data_123"
              },
              "boundingBoxes": [
                  {
                      "label": "object_1",
                      "x": 606,
                      "y": 103,
                      "width": 32,
                      "height": 17
                  }
              ]
          }
      ]
  }
  ```
</CodeGroup>


Built with [Mintlify](https://mintlify.com).