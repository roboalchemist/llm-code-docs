<!-- Source: https://namespace.so/docs/reference/cli/volume-list -->

# nsc volume list

Lists the volumes for this workspace.

`volume list` lists the [volumes](/docs/architecture/storage/cache-volumes) for this workspace.
For each volume tag, you can observe the used and total size, and when the volume was last used.

## Usage

```
nsc volume list [-o <plain|json>]
```

### Example

```
% nsc volume list
┌───────────────────────────────────────────────────────────────────────┐
│ Tag                            Size (Used / Total)   Last Used        │
│───────────────────────────────────────────────────────────────────────│
│ build-cluster-arm64            12 GiB / 64 GiB       22 hours ago     │
│ build-cluster-amd64            8.0 GiB / 64 GiB      22 hours ago     │
│ my-private-docker-image-cache  5.0 GiB / 20 GiB      In use           │
│ my-private-preview-cache       1.2 GiB / 20 GiB      1 month ago      │
└───────────────────────────────────────────────────────────────────────┘
```

To print the list in a machine-friendly format, use `-o json`:

```
$ nsc volume list -o json
[
  {
    "tag": "build-cluster-arm64",
    "used_mb": 12288,
    "size_mb": 65536,
    "in_use": false,
    "last_attached_at": "2025-11-14T10:30:00Z"
  },
  {
    "tag": "my-private-docker-image-cache",
    "used_mb": 5120,
    "size_mb": 20480,
    "in_use": true,
    "last_attached_at": "2025-11-15T08:15:00Z"
  }
]
```

## Options

### -o <type>

Specifies the output format. Supported options are `json` and
`plain`. By default `plain` output format is used.

Last updated April 16, 2026
