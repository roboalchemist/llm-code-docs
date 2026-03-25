# Source: https://docs.edgeimpulse.com/tools/specifications/files/sample-id-details-json.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# sample_id_details.json

The `sample_id_details.json` is a file that lives alongside the training (train) and validation (test) dataset splits that are used for training a learning block. The information contained in this file may be relevant to you when developing [custom learning blocks](/studio/organizations/custom-blocks/custom-learning-blocks).

The file contains a list of samples IDs as integers in row order for each dataset. It allows you to map processed features that are passed to your learning block back to the original sample they came from. Note that the same sample ID may appear several times; sample IDs are repeated when there is more than one window created for the sample.

## Data directory structure

```bash  theme={"system"}
data/
├── X_split_test.npy
├── X_split_train.npy
├── Y_split_test.npy
├── Y_split_train.npy
└── sample_id_details.json
```

## File structure

```json  theme={"system"}
{
    "train": [
        <id>,
        <id>,
        ...
        <id>
    ],
    "validation": [
        <id>,
        <id>,
        ...
        <id>
    ]
}
```

## File example

```json  theme={"system"}
{
    "train": [
        1440653288,
        1440653283,
        ...
        1440653252
    ],
    "validation": [
        1440653307,
        1440653297,
        ...
        1440653285
    ]
}
```


Built with [Mintlify](https://mintlify.com).