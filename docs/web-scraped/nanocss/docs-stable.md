# nano-css Documentation
# Source: https://raw.githubusercontent.com/streamich/nano-css/master/docs/stable.md
# Path: docs/stable.md

# `stable` Addon

When generating class names, `nano-css` stringifies CSS-like objects to compute a hash and generate a unique class name. By default it uses `JSON.stringify`, which is not stable. This
addon makes `nano-css` use [`fastest-stable-stringify`](https://github.com/streamich/fastest-stable-stringify)
to generate fast predictable hashes across JavaScript runtimes.

## Installation

Simply install `stable` addon. Read more about the [Addon Installation](./Addons.md#addon-installation).
