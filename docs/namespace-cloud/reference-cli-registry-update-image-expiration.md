<!-- Source: https://namespace.so/docs/reference/cli/registry-update-image-expiration -->

# nsc registry update-image-expiration

Update the expiration of an nscr.io image.

`nsc registry update-image-expiration` updates the expiration of a single image that is stored in nscr.io. Once an image expires it can no longer be accessed and the underlying blobs are automatically deleted.
It is not possible to change the expiration of an image that already expired.

## Usage

```
nsc registry update-image-expiration <image-reference> [--ensure-minimum <duration>] [--expire-at <timestamp>]
```

### Examples

```
nsc registry update-image-expiration testing/backend@sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e --ensure-minimum=5h
 
Ensuring expiry is at least: 5h0m0s
 
Repository:   testing/backend
Digest:       sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e
New Expiry:   2025-12-15T21:25:10Z
 
Image expiry updated successfully.
```

```
nsc registry update-image-expiration testing/backend@sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e --expire-at=2025-12-16T21:25:10Z
 
Setting expiry to: 2025-12-16T21:25:10Z
 
Repository:   testing/backend
Digest:       sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e
New Expiry:   2025-12-16T21:25:10Z
 
Image expiry updated successfully.
```

## Options

### --ensure-minimum <duration>

How long the image should be available at least. If there's currently an expiration set after the provided duration then the command will not do any change.
The duration is specified as a string and valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".

### --expire-at <timestamp>

When the image should expire. This overwrites any previously configured expiration.

Last updated December 15, 2025
