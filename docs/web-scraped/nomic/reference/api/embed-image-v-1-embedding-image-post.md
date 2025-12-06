# Embed Image

Source: https://docs.nomic.ai/reference/api/embed-image-v-1-embedding-image-post

# Embed Image

```
POST /v1/embedding/image
```

## /v1/embedding/image

Generate embeddings from images in .png, .jpeg, or .webp formats.

```
.png
```

```
.jpeg
```

```
.webp
```

Images can be provided either as:

- Files (filepaths or raw image bytes)
Files (filepaths or raw image bytes)

- URLs
URLs

#### curl​

```
curl
```

Embedding image files using curl:

```
curl
```

```
curl -X POST "https://api-atlas.nomic.ai/v1/embedding/image" \-H "Authorization: Bearer $NOMIC_API_KEY" \-H "Content-Type: multipart/form-data" \-F "model=nomic-embed-vision-v1.5" \-F "images=@path/to/image1.jpg" \-F "images=@path/to/image2.jpg"
```

Embedding images via URLs using curl:

```
curl
```

```
curl -X POST "https://api-atlas.nomic.ai/v1/embedding/image" \-H "Authorization: Bearer $NOMIC_API_KEY" \-H "Content-Type: application/x-www-form-urlencoded" \-d "model=nomic-embed-vision-v1.5" \-d "urls=https://static.nomic.ai/secret-model.png" \-d "urls=https://static.nomic.ai/secret-model-2.png"
```

#### nomic Python library​

```
nomic
```

Embeddings image files using the nomic Python library:

```
nomic
```

```
from nomic import embedoutput = embed.image(    images=['path/to/image1.jpg', 'path/to/image2.jpg'],    model='nomic-embed-vision-v1.5',)print(output)
```

Embedding images via URLs using the nomic Python library:

```
nomic
```

```
from nomic import embedoutput = embed.image(    images=[        "https://static.nomic.ai/secret-model.png",         "https://static.nomic.ai/secret-model-2.png"    ],    model="nomic-embed-vision-v1.5")print(output)
```

#### requests Python library​

```
requests
```

Embedding image files using the requests Python library (note that this option requires image bytes rather than image files):

```
requests
```

```
import requestsimport osauth_header = "Bearer " + os.environ["NOMIC_API_KEY"]image_filepaths = ["path/to/image1.jpg", "path/to/image2.jpg"]image_bytes = []for fpath in image_filepaths:    with open(fpath, "rb") as f:        image_bytes.append(("images", f.read()))response = requests.post(    "https://api-atlas.nomic.ai/v1/embedding/image",    headers=dict(Authorization=auth_header),    data=dict(model="nomic-embed-vision-v1.5"),    files=image_bytes)print(response.json())
```

Embedding images via URLs using the requests Python library:

```
requests
```

```
import requestsimport osauth_header = "Bearer " + os.environ["NOMIC_API_KEY"]response = requests.post(    "https://api-atlas.nomic.ai/v1/embedding/image",    headers=dict(Authorization=auth_header),    data=dict(        model="nomic-embed-vision-v1.5",        urls=[            "https://static.nomic.ai/secret-model.png",            "https://static.nomic.ai/secret-model-2.png"        ]    ))print(response.json())
```

## Request​

- multipart/form-data
### Body

Body

Possible values: [nomic-embed-vision-v1, nomic-embed-vision-v1.5]

```
nomic-embed-vision-v1
```

```
nomic-embed-vision-v1.5
```

Default value: nomic-embed-vision-v1.5

```
nomic-embed-vision-v1.5
```

The model to use when embedding.

urls

object

anyOf

- MOD1
- Array [
Array [

string

- ]
]

images

object

A batch of image bytes you want to embed

anyOf

- MOD1
- Array [
Array [

string

- ]
]

## Responses​

- 200
- 422
Successful Response

- application/json
- Schema
- Example (from schema)
Schema

The embeddings

usage

object

required

The embedding usage

The number of non-generated tokens ingested.

The total tokens used.

Possible values: [nomic-embed-vision-v1, nomic-embed-vision-v1.5]

```
nomic-embed-vision-v1
```

```
nomic-embed-vision-v1.5
```

The model used to produce the embeddings.

```
{  "embeddings": [    [      0    ]  ],  "usage": {    "prompt_tokens": 0,    "total_tokens": 0  },  "model": "nomic-embed-vision-v1"}
```

Validation Error

- application/json
- Schema
- Example (from schema)
Schema

detail

object[]

- Array [
Array [

loc

object[]

required

- Array [
Array [

anyOf

- MOD1
- MOD2
string

integer

- ]
]

- ]
]

```
{  "detail": [    {      "loc": [        "string",        0      ],      "msg": "string",      "type": "string"    }  ]}
```

