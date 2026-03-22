# Source: https://docs.roboflow.com/developer/rest-api/export-data.md

# Export Data

You can export a dataset from the Roboflow platform using the web interface and the Python SDK.

{% tabs %}
{% tab title="Python SDK" %}
To create a ZIP file of a dataset for export from the Python SDK, begin by retrieving a specific [version from a project](https://docs.roboflow.com/developer/list-projects-and-versions#get-a-project):

```
version = project.version(version_number)
```

Then download the dataset directly:

```python
version.download(model_format="yolov5", location="./downloads")
```

The download method handles export creation automatically if needed, extracts the ZIP file to your specified location, and returns an object describing the dataset.
{% endtab %}

{% tab title="REST API" %}
`/:workspace/:project/:version/:format` is the route you should use to get the download link for an exported dataset in a specific format. You can use this in the Jupyter notebooks from [our model library](https://models.roboflow.com) or your own custom training scripts.

The following endpoint returns an `export` value that contains a `link` key with a URL from which you can download a dataset:

<pre class="language-bash"><code class="lang-bash"><strong>curl "https://api.roboflow.com/roboflow/chess-sample-4ckfl/1/yolov5pytorch?api_key=$ROBOFLOW_API_KEY"
</strong></code></pre>

Here is an example payload returned by the endpoint:

```bash
{
    "workspace": {
        "name": "Roboflow",
        "url": "roboflow",
        "members": 7
    },
    "project": {
        "id": "roboflow/chess-sample-4ckfl",
        "type": "object-detection",
        "name": "Chess Sample",
        "created": 1630335544.592,
        "updated": 1630335741.988,
        "images": 12,
        "unannotated": 3,
        "annotation": "pieces",
        "public": false,
        "splits": {
            "test": 1,
            "train": 9,
            "valid": 2
        },
        "classes": {
            "white-bishop": 11,
            "black-king": 8,
            "black-knight": 11,
            "white-queen": 7,
            "black-bishop": 8,
            "white-rook": 10,
            "black-rook": 10,
            "white-king": 8,
            "black-queen": 4,
            "black-pawn": 37,
            "white-pawn": 34,
            "white-knight": 10
        }
    },
    "version": {
        "id": "roboflow/chess-sample-4ckfl/1",
        "name": "augmented",
        "created": 1630335698.746,
        "images": 30,
        "splits": {
            "train": 27,
            "test": 1,
            "valid": 2
        },
        "model": {
            "id": "chess-sample-4ckfl/1",
            "endpoint": "https://detect.staging.roboflow.com/chess-sample-4ckfl/1",
            "start": 1630335799.682,
            "end": 1630337523.889,
            "fromScratch": false,
            "tfjs": true,
            "oak": true,
            "map": "62.87",
            "recall": "85.29",
            "precision": "23.44"
        },
        "preprocessing": {
            "grayscale": {
                "enabled": true
            },
            "resize": {
                "width": 416,
                "height": 416,
                "enabled": true,
                "format": "Stretch to"
            },
            "auto-orient": {
                "enabled": true
            }
        },
        "augmentation": {
            "rotate": {
                "enabled": true,
                "degrees": "5"
            },
            "exposure": {
                "enabled": true,
                "percent": "25"
            },
            "noise": {
                "enabled": true,
                "percent": "2"
            },
            "image": {
                "versions": "3",
                "enabled": true
            },
            "flip": {
                "horizontal": true,
                "enabled": true,
                "vertical": false
            },
            "brightness": {
                "enabled": true,
                "brighten": true,
                "percent": "25",
                "darken": true
            },
            "crop": {
                "percent": 30,
                "enabled": true,
                "min": 0
            }
        },
        "exports": [
            "yolov5pytorch"
        ]
    },
    "export": {
        "format": "yolov5pytorch",
        "link": "https://app.staging.roboflow.com/ds/o06EL6FAt7?key=KYtxHKCvaN"
    }
}
```

{% endtab %}

{% tab title="CLI" %}
You can export data through the Roboflow CLI using the following command:

```
roboflow download <datasetUrl>
```

[Find more information about this CLI command in our docs.](https://docs.roboflow.com/developer/rest-api/broken-reference)
{% endtab %}
{% endtabs %}

Here are the settings options available for dataset export:

| Object Detection | Single-Label Classification | Multi-Label Classification | Instance Segmentation | Semantic Segmentation | Keypoint Detection |
| ---------------- | --------------------------- | -------------------------- | --------------------- | --------------------- | ------------------ |
| clip             | folder                      | multiclass                 | coco-segmentation     | coco-segmentation     | coco               |
| coco             | clip                        | folder                     | clip                  | png-mask-semantic     | yolov5pytorch      |
| createml         |                             | clip                       | coco                  |                       |                    |
| darknet          |                             |                            | createml              |                       |                    |
| multiclass       |                             |                            | darknet               |                       |                    |
| tensorflow       |                             |                            | multiclass            |                       |                    |
| tfrecord         |                             |                            | tensorflow            |                       |                    |
| voc              |                             |                            | tfrecord              |                       |                    |
| yolokeras        |                             |                            | voc                   |                       |                    |
| yolov5pytorch    |                             |                            | yolokeras             |                       |                    |
| yolov7pytorch    |                             |                            | yolov4pytorch         |                       |                    |
| mt-yolov6        |                             |                            | yolov4scaled          |                       |                    |
| retinanet        |                             |                            | yolov5-obb            |                       |                    |
| benchmarker      |                             |                            | yolov5pytorch         |                       |                    |
|                  |                             |                            | yolov7pytorch         |                       |                    |
|                  |                             |                            | mt-yolov6             |                       |                    |
|                  |                             |                            | retinanet             |                       |                    |
|                  |                             |                            | benchmarker           |                       |                    |
