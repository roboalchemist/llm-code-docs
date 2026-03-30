# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/adding-data/image-metadata.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/adding-data/image-metadata.md

# Source: https://docs.roboflow.com/datasets/adding-data/image-metadata.md

# Image Metadata

Metadata lets you attach custom key-value pairs to images in your Roboflow workspace. Use metadata to store structured information alongside your images — such as capture conditions, device identifiers, quality scores, or any domain-specific attributes — and then search, filter, and organize your data around those attributes.

## Overview

Each image can hold any number of metadata entries. An entry is a **key** (a name like `camera_id`) paired with a **value** (a string, number, or boolean).

| Value type | Examples                                    |
| ---------- | ------------------------------------------- |
| String     | `location: "warehouse-3"`, `shift: "night"` |
| Number     | `temperature: 72.5`, `quality_score: 95`    |
| Boolean    | `reviewed: true`, `is_night: false`         |

### Use cases

* **Capture context** — record camera ID, GPS coordinates, weather, lighting conditions
* **Quality tracking** — attach confidence scores, review status, annotator IDs
* **Data slicing** — filter your dataset by any attribute to build targeted training sets
* **External system linking** — store identifiers that connect images back to your internal tools

## Adding Metadata

You can add metadata to images through the web UI, the Python SDK, the REST API, or automatically via S3 Bucket Mirror.

### Web Application

{% stepper %}
{% step %}

### Open an image

Open any image in your project.
{% endstep %}

{% step %}

### Enter key and value

In the metadata section, enter a **key** in the first input and a **value** in the second input.
{% endstep %}

{% step %}

### Add

Press **Enter** to save or click on Add
{% endstep %}
{% endstepper %}

Values are automatically parsed by type:

| Value entered    | Stored as                  |
| ---------------- | -------------------------- |
| `front`          | `"front"` (string)         |
| `95`             | `95` (number)              |
| `3.14`           | `3.14` (number)            |
| `true` / `false` | `true` / `false` (boolean) |

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fh7L2L0c22TIzCxjxuiU1%2Fimage.png?alt=media&#x26;token=3f3eba92-e194-43b4-bd98-801a038836ff" alt=""><figcaption><p>Annotation Tool's metadata editor</p></figcaption></figure>

### Python SDK

Pass a `metadata` dictionary when uploading an image:

```python
import roboflow

rf = roboflow.Roboflow(api_key="YOUR_API_KEY")
project = rf.workspace("your-workspace").project("your-project")

project.upload(
    image_path="image.jpg",
    metadata={
        "camera_id": "cam001",
        "location": "warehouse-3",
        "temperature": 72.5,
        "is_night": False
    }
)
```

### REST API

#### Add metadata during upload

Include a `metadata` field (JSON-stringified) in the multipart form data when uploading an image:

```bash
curl -X POST "https://api.roboflow.com/dataset/your-dataset/upload?api_key=YOUR_API_KEY" \
  -F "name=image.jpg" \
  -F "split=train" \
  -F "file=@image.jpg" \
  -F 'metadata={"camera_id":"cam001","temperature":72.5}'
```

### S3 Bucket Mirror

When using [Bucket Mirror](https://docs.roboflow.com/datasets/adding-data/broken-reference) to sync images from an S3 bucket, you can attach metadata by placing a `.json` file alongside each image with the same base name:

```
my-bucket/
  images/
    photo_001.jpg
    photo_001.json      # metadata for photo_001.jpg
    photo_002.jpg
    photo_002.json      # metadata for photo_002.jpg
```

The JSON file contains your metadata as key-value pairs:

```json
{
    "camera_id": "cam001",
    "location": "warehouse-3",
    "capture": { "temperature": 72.5, "humidity": 45 }
}
```

**Nested objects are automatically flattened** using dot notation. The example above produces:

| Key                   | Value           |
| --------------------- | --------------- |
| `camera_id`           | `"cam001"`      |
| `location`            | `"warehouse-3"` |
| `capture.temperature` | `72.5`          |
| `capture.humidity`    | `45`            |

#### Metadata file constraints

* Maximum file size: **256 KB**
* Must be valid JSON
* `null` and `undefined` values are filtered out

#### Update strategies

Bucket Mirror supports different strategies for how synced metadata interacts with metadata you've set manually in the UI or via API:

| Strategy                        | Behavior                                                                     |
| ------------------------------- | ---------------------------------------------------------------------------- |
| **`mergeBucketWins`** (default) | Merges both sources. On key conflicts, the bucket value wins.                |
| **`mergeUserWins`**             | Merges both sources. On key conflicts, the user-set value wins.              |
| **`overwrite`**                 | Bucket metadata completely replaces all existing metadata.                   |
| **`untilFirstChange`**          | Syncs from bucket until a user manually edits metadata, then stops updating. |
| **`append`**                    | Only adds new keys from the bucket. Never overwrites existing keys.          |

## Searching by Metadata

Metadata is indexed and searchable in the [Asset Library](https://docs.roboflow.com/datasets/adding-data/broken-reference). Use the search bar to filter images by metadata values:

```
metadata.camera_id:"cam001"
metadata.quality_score>80
metadata.reviewed:true
```

You can combine metadata filters with other search filters:

```
metadata.location:"warehouse-3" AND class:forklift
```

The Asset Library also provides autocomplete for metadata keys and values based on what exists in your workspace.

## Key Naming Rules

Metadata keys must follow these rules:

| Rule                 | Detail                                                                 |
| -------------------- | ---------------------------------------------------------------------- |
| Allowed characters   | Letters (`a-z`, `A-Z`), numbers (`0-9`), underscores (`_`), dots (`.`) |
| First character      | Must be a letter, number, or underscore                                |
| Forbidden characters | Forward slashes (`/`) are not allowed                                  |

Valid keys: `camera_id`, `capture.temperature`, `_internal_ref`, `v2_score`

Invalid keys: `camera/id` (contains `/`), `.starts_with_dot` (starts with `.`), `has spaces` (contains spaces)

## Metadata vs. Tags

Both metadata and [tags](https://docs.roboflow.com/datasets/adding-data/broken-reference) help you organize images, but they serve different purposes:

|               | Tags                                 | Metadata                                   |
| ------------- | ------------------------------------ | ------------------------------------------ |
| **Structure** | Simple labels                        | Key-value pairs                            |
| **Values**    | No value, just a name                | String, number, or boolean                 |
| **Best for**  | Categorization, workflow status      | Structured attributes, measurements        |
| **Example**   | `reviewed`, `v2`, `needs-annotation` | `temperature: 72.5`, `camera_id: "cam001"` |

You can use both on the same image. For example, tag an image as `reviewed` and also store `reviewer: "alice"` and `confidence: 0.95` as metadata.
