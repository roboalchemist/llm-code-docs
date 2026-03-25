# Source: https://docs.roboflow.com/developer/rest-api/versions/view-a-version.md

# View a Version

You can retrieve information about a Roboflow version using the Python SDK, REST API, and CLI.

### Version ID

Each version generated in Roboflow has a sequential, numerical ID associated with it. You can see that through the app on your versions page or by listing your project versions in the API.

{% tabs %}
{% tab title="Python" %}
To retrieve information about a project, use this command:

```python
import roboflow

rf = roboflow.Roboflow(api_key=YOUR_API_KEY_HERE)

# get a project
project = rf.workspace().project("PROJECT_ID")

model = project.version("1").model
```

The `model` variable contains the following JSON values:

```json
{
  "id": "mug-detector-eocwp/12",
  "name": "Mug Detector",
  "version": "12",
  "classes": null,
  "overlap": 30,
  "confidence": 40,
  "stroke": 1,
  "labels": false,
  "format": "json",
  "base_url": "https://detect.roboflow.com/"
}
```

{% endtab %}

{% tab title="REST API" %}
If you already know which project and version you want to retrieve information about, you can use the `/:workspace/:project/:version` endpoint. It returns similar information as the project endpoint but does not enumerate all of the project's other versions.

To retrieve information about a project, make a GET request to the following endpoint:

```url
https://api.roboflow.com/roboflow/chess-sample-4ckfl/1?api_key=$ROBOFLOW_API_KEY
```

This endpoint returns the following response:

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
            "valid": 2,
            "train": 9
        },
        "classes": {
            "black-knight": 11,
            "black-queen": 4,
            "black-king": 8,
            "white-king": 8,
            "white-pawn": 34,
            "black-bishop": 8,
            "white-rook": 10,
            "black-pawn": 37,
            "white-knight": 10,
            "white-bishop": 11,
            "black-rook": 10,
            "white-queen": 7
        }
    },
    "version": {
        "id": "roboflow/chess-sample-4ckfl/1",
        "name": "augmented",
        "created": 1630335698.746,
        "images": 30,
        "splits": {
            "valid": 2,
            "test": 1,
            "train": 27
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
            "resize": {
                "height": 416,
                "width": 416,
                "format": "Stretch to",
                "enabled": true
            },
            "auto-orient": {
                "enabled": true
            },
            "grayscale": {
                "enabled": true
            }
        },
        "augmentation": {
            "rotate": {
                "degrees": "5",
                "enabled": true
            },
            "brightness": {
                "darken": true,
                "enabled": true,
                "brighten": true,
                "percent": "25"
            },
            "noise": {
                "percent": "2",
                "enabled": true
            },
            "crop": {
                "enabled": true,
                "min": 0,
                "percent": 30
            },
            "flip": {
                "horizontal": true,
                "vertical": false,
                "enabled": true
            },
            "image": {
                "versions": "3",
                "enabled": true
            },
            "exposure": {
                "enabled": true,
                "percent": "25"
            }
        },
        "exports": [
            "yolov5pytorch"
        ],
        "train": {
            "status": "finished",
            "results": {
                "class_map": {
                    "valid": [
                        {
                            "images": "20",
                            "map95": "0.29",
                            "precision": "0.795",
                            "recall": "0.48",
                            "map50": "0.547",
                            "class": "all",
                            "targets": "82"
                        },
                        ...
                    ],
                    "test": [
                        {
                            "images": "10",
                            "map95": "0.478",
                            "precision": "0.846",
                            "recall": "0.759",
                            "map50": "0.844",
                            "class": "all",
                            "targets": "29"
                        },
                        ...
                    ]
                }
            }
        },
        "models": {
            "roboflow-train": {
                "epochs": [
                    {
                        "mAP": "0.5624740875589795",
                        "epoch": "0",
                        "precision": "0.848007354583702",
                        "recall": "0.4796292117720689",
                        "box_loss": "0.04430354",
                        "obj_loss": "0.023823218",
                        "class_loss": "0.012277425",
                        "mAP_50_95": "0.3004394102727502"
                    },
                    {
                        "mAP": "0.5576528999996365",
                        "epoch": "1",
                        "precision": "0.8477760345230224",
                        "recall": "0.47967238365789094",
                        "box_loss": "0.041422606",
                        "obj_loss": "0.020020777",
                        "class_loss": "0.010422977",
                        "mAP_50_95": "0.2943194093111112"
                    },
                    ...
                ]
            }
        },
        "classes": [
            "black-knight",
            "black-queen",
            "black-king",
            "white-king",
            "white-pawn",
            "black-bishop",
            "white-rook",
            "black-pawn",
            "white-knight",
            "white-bishop",
            "black-rook",
            "white-queen"
        ]
    }
}
```

{% endtab %}

{% tab title="CLI" %}
To retrieve information about a project using the CLI, you can use the following command:

```
roboflow project get <project-id>
```

For more details regarding this CLI command, please refer to the [`roboflow project get`](https://github.com/roboflow/roboflow-python/blob/main/CLI-COMMANDS.md#example-get-workspace-details) section of the CLI docs.
{% endtab %}
{% endtabs %}

### Keypoint Detection Skeletons

Keypoint Detection project versions will contain a `skeletons` field which contains your version skeletons for each class. For example, a project with a class `person` might have the following skeleton:

```json
{
...
"skeletons": {
    "person": {
        "vertices": [
            {
                "color": "#FF8000",
                "id": 0,
                "name": "nose",
                "x": 0.4546,
                "y": 0.18859999999999996
            },
            {
                "color": "#FF00FF",
                "id": 1,
                "name": "left_eye"
                "x": 0.478,
                "y": 0.1606
            },
            ...
        ],
        "edges": [
            {
                "color": "#00FFCE",
                "from": 13,
                "to": 15
            },
            ...
        ],
        "symmetries": [
            {
                "direction": "horizontal",
                "points": [1, 2]
            },
            ...
        ]
    }
}
```

Note, vertices should be accessed by index with inference predictions `class_id`. Then, vertex `id` can be used to reference edge (from/to) and symmetries (points).
