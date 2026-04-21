<!-- Source: https://namespace.so/docs/reference/cli/registry-default-expiration -->

# nsc registry default-expiration

Manage the default expiration applied to new images uploaded to nscr.io.

Deprecated: use [`nsc registry policy`](/docs/reference/cli/registry-policy) instead.

`nsc registry default-expiration` makes it possible to query and modify the configured default expiration that is applied to new images uploaded to nscr.io.
By default, images stored in nscr.io never expire. The default expiration duration needs to be at least 4 hours.
Once an image expires it can no longer be accessed and the underlying blobs are automatically deleted.

Note: the default expiration only applies to images created after configuring the value.
In case you would like to apply the expiration retroactively, please reach out to [our support](mailto:support@namespace.so).

## Usage

```
nsc registry default-expiration get [-o <format>]
nsc registry default-expiration set [--expiration <duration>] [--no-expiration]
```

### Examples

```
nsc registry default-expiration get
 
Revision:             4
Default Expiration:   5h0m0s
```

```
nsc registry default-expiration set --expiration=6h
 
Default configuration has been updated to expire images after 6h0m0s.
```

```
nsc registry default-expiration set --no-expiration
 
Default configuration has been updated to never expire images.
```

## Options

### get

#### -o <format>

The output format of the current default expiration configuration. Can either be table or json.

### set

#### --expiration <duration>

How long an image should exist after its creation. The duration is specified as a string and valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".
The provided value needs to be at least 4 hours.

#### --no-expiration

If set, new images will never expire.

Last updated February 17, 2026
