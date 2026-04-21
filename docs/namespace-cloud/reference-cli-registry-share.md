<!-- Source: https://namespace.so/docs/reference/cli/registry-share -->

# nsc registry share

Share a private nscr.io image publicly.

`nsc registry share` makes a private nscr.io container image publicly accessible. It generates a new unique id which can
be used to pull the image from public.nscr.io.

## Usage

```
nsc registry share <image-reference> [--suffix <suffix>] [--expires_at <timestamp>]
```

### Example

```
nsc registry share nscr.io/01gr490qvbntkjn9jwypnd4g04/private@sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e
 
Shared Image ID:  foo0sasl3o8
Repository:       private
Digest:           sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e
Visibility:       PUBLIC
Expires At:       Never
 
Shared Reference: public.nscr.io/foo0sasl3o8/test:latest
```

## Options

### --suffix <suffix>

Adds a suffix to the id part of the public reference which makes it easier to distinguish public images.

### --expires\_at <timestamp>

When the image will no longer be accessible publicly. The private image will still exist after this timestamp.

Last updated December 15, 2025
