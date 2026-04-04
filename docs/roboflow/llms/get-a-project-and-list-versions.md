# Source: https://docs.roboflow.com/developer/rest-api/get-a-project-and-list-versions.md

# Get a Project and List Versions

You can retrieve information about a project using the following REST endpoint:

```bash
curl "https://api.roboflow.com/roboflow/chess-sample-4ckfl?api_key=$ROBOFLOW_API_KEY"
```

This endpoint returns a JSON response with the following structure:

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
            "valid": 2,
            "train": 9,
            "test": 1
        },
        "classes": {
            "white-queen": 7,
            "white-king": 8,
            "black-knight": 11,
            "black-pawn": 37,
            "black-rook": 10,
            "white-pawn": 34,
            "black-bishop": 8,
            "white-knight": 10,
            "black-queen": 4,
            "white-bishop": 11,
            "black-king": 8,
            "white-rook": 10
        },
        "versions": [
            {
                "id": "roboflow/chess-sample-4ckfl/3",
                "name": "raw",
                "created": 1630335741.989,
                "images": 12,
                "splits": {
                    "train": 9,
                    "test": 1,
                    "valid": 2
                },
                "preprocessing": {
                    "auto-orient": {
                        "enabled": true
                    }
                },
                "augmentation": {},
                "exports": [
                    "coco",
                    "voc"
                ]
            },
            {
                "id": "roboflow/chess-sample-4ckfl/2",
                "name": "416x416",
                "created": 1630335730.142,
                "images": 12,
                "splits": {
                    "train": 9,
                    "test": 1,
                    "valid": 2
                },
                "preprocessing": {
                    "resize": {
                        "enabled": true,
                        "format": "Stretch to",
                        "width": 416,
                        "height": 416
                    },
                    "auto-orient": {
                        "enabled": true
                    }
                },
                "augmentation": {},
                "exports": []
            },
            {
                "id": "roboflow/chess-sample-4ckfl/1",
                "name": "augmented",
                "created": 1630335698.746,
                "images": 30,
                "splits": {
                    "valid": 2,
                    "train": 27,
                    "test": 1
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
                        "enabled": true,
                        "width": 416,
                        "format": "Stretch to",
                        "height": 416
                    },
                    "auto-orient": {
                        "enabled": true
                    },
                    "grayscale": {
                        "enabled": true
                    }
                },
                "augmentation": {
                    "exposure": {
                        "percent": "25",
                        "enabled": true
                    },
                    "brightness": {
                        "percent": "25",
                        "enabled": true,
                        "darken": true,
                        "brighten": true
                    },
                    "rotate": {
                        "degrees": "5",
                        "enabled": true
                    },
                    "image": {
                        "enabled": true,
                        "versions": "3"
                    },
                    "flip": {
                        "enabled": true,
                        "horizontal": true,
                        "vertical": false
                    },
                    "crop": {
                        "min": 0,
                        "percent": 30,
                        "enabled": true
                    },
                    "noise": {
                        "percent": "2",
                        "enabled": true
                    }
                },
                "exports": [
                    "yolov5pytorch"
                ],
                "versionNotes": "Fix: rotated box misalignment"
            }
        ]
    }
}
```
