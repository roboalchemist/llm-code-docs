# Source: https://docs.together.ai/reference/files.md

# Files

## Upload

To upload a new data file:

```sh Shell theme={null}
together files upload <FILENAME>
```

Here's a sample output:

```sh Shell theme={null}
$ together files upload example.jsonl
Uploading example.jsonl: 100%|██████████████████████████████| 5.18M/5.18M [00:01<00:00, 4.20MB/s]
{
    "filename": "example.jsonl",
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "object": "file"
}
```

The `id` field in the response will be the assigned `file-id` for this file object.

## List

To list previously uploaded files:

```sh Shell theme={null}
together files list
```

## Retrieve

To retrieve the metadata of a previously uploaded file:

```sh Shell theme={null}
together files retrieve <FILE-ID>
```

Here's a sample output:

```sh Shell theme={null}
$ together files retrieve file-d931200a-6b7f-476b-9ae2-8fddd5112308
{
    "filename": "example.jsonl",
    "bytes": 5433223,
    "created_at": 1690432046,
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "purpose": "fine-tune",
    "object": "file",
    "LineCount": 0,
    "Processed": true
}
```

## Retrieve content

To download a previously uploaded file:

```sh Shell theme={null}
together files retrieve-content <FILE-ID>
```

Here's a sample output:

```sh Shell theme={null}
$ together files retrieve-content file-d931200a-6b7f-476b-9ae2-8fddd5112308
Downloading file-d931200a-6b7f-476b-9ae2-8fddd5112308.jsonl: 100%|██████████| 5.43M/5.43M [00:00<00:00, 10.0MiB/s]
file-d931200a-6b7f-476b-9ae2-8fddd5112308.jsonl
```

You can specify the output filename with `--output FILENAME` or `-o FILENAME`. By default, the dataset is saved to `<FILE-ID>.jsonl`.

## Delete

To delete a previously uploaded file:

```sh Shell theme={null}
together files delete <FILE-ID>
```

Here's a sample output:

```sh Shell theme={null}
$ together files delete file-d931200a-6b7f-476b-9ae2-8fddd5112308
{
    "id": "file-d931200a-6b7f-476b-9ae2-8fddd5112308",
    "object": "file",
    "deleted": "true"
}
```

## Check

To check that a file is in the correct format, you can do this:

Python

```
from together.utils import check_file

report = check_file(file)

print(report)

assert report["is_check_passed"] == True
```

## Help

See all commands with:

```sh Shell theme={null}
together files --help
```

***


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt