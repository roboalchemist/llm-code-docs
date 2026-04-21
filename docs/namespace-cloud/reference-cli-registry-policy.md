<!-- Source: https://namespace.so/docs/reference/cli/registry-policy -->

# nsc registry policy

Manage registry policies for image expiration.

`nsc registry policy` makes it possible to query and modify the expiration policy applied to new images uploaded to nscr.io.
By default, images stored in nscr.io never expire. The expiration duration needs to be at least 4 hours.
Once an image expires it can no longer be accessed and the underlying blobs are automatically deleted.

Policies can be set at two levels:

- **Default policy**: applies to all repositories that don't have a repository-specific policy.
- **Repository policy**: overrides the default policy for a specific repository.

Note: the expiration policy only applies to images created after configuring the value.
In case you would like to apply the expiration retroactively, please reach out to [our support](mailto:support@namespace.so).

## Usage

```
nsc registry policy get [--repository <repository>] [-o <format>]
nsc registry policy set [--default_expiration <duration>] [--no-expiration] [--repository <repository>]
```

### Examples

Get the current default policy:

```
nsc registry policy get
 
Default Expiration:   5h0m0s
```

Get the policy for a specific repository:

```
nsc registry policy get --repository my-app
 
Default Expiration:   168h0m0s
```

Set a default expiration of 7 days for all new images:

```
nsc registry policy set --default_expiration=168h
 
Default configuration has been updated to expire images after 168h0m0s.
```

Set a repository-specific expiration:

```
nsc registry policy set --repository my-app --default_expiration=24h
 
Policy for repository "my-app" has been updated to expire images after 24h0m0s.
```

Disable expiration:

```
nsc registry policy set --no-expiration
 
Default configuration has been updated to never expire images.
```

## Options

### get

#### --repository <repository>

Get the policy for a specific repository. If not specified, returns the default policy.

#### -o <format>

The output format. Can either be `table` or `json`.

### set

#### --default\_expiration <duration>

How long an image should exist after its creation. The duration is specified as a string (e.g., `168h` for 7 days).
The provided value needs to be at least 4 hours.

#### --no-expiration

If set, new images will never expire.

#### --repository <repository>

Set the policy for a specific repository. If not specified, sets the default policy that applies to all repositories without a repository-specific override.

Last updated February 17, 2026
