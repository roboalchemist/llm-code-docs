<!-- Source: https://namespace.so/docs/reference/cli/volume-release -->

# nsc volume release

Releases all volumes for a provided tag.

`volume release` destroys all volumes backing the provided volume tag.

## Usage

```
nsc volume release <volume-tag>
```

### Example

First, let's check which tags are in use.

```
% nsc volume list
┌───────────────────────────────────────────────────────────────────────┐
│ Tag                            Size (Used / Total)   Last Used        │
│───────────────────────────────────────────────────────────────────────│
│ build-cluster-arm64            12 GiB / 64 GiB       22 hours ago     │
│ build-cluster-amd64            8.0 GiB / 64 GiB      22 hours ago     │
│ my-private-docker-image-cache  5.0 GiB / 20 GiB      1 month ago      │
│ my-private-preview-cache       1.2 GiB / 20 GiB      1 month ago      │
└───────────────────────────────────────────────────────────────────────┘
```

We decide that we want to drop `my-private-preview-cache`.

```
% nsc volume release my-private-preview-cache
 
Released volumes with tag my-private-preview-cache.
```

Finally, we can see the updated list of volumes.

```
% nsc volume list
┌───────────────────────────────────────────────────────────────────────┐
│ Tag                            Size (Used / Total)   Last Used        │
│───────────────────────────────────────────────────────────────────────│
│ build-cluster-arm64            12 GiB / 64 GiB       22 hours ago     │
│ build-cluster-amd64            8.0 GiB / 64 GiB      22 hours ago     │
│ my-private-docker-image-cache  5.0 GiB / 20 GiB      1 month ago      │
└───────────────────────────────────────────────────────────────────────┘
```

Last updated April 16, 2026
