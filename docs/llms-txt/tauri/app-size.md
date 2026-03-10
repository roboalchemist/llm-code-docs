# App Size

import { Tabs, TabItem } from '@astrojs/starlight/components';

While Tauri by default provides very small binaries it doesn't hurt to push the limits a bit, so here are some tips and tricks for reaching optimal results.

## Cargo Configuration

One of the simplest frontend agnostic size improvements you can do to your project is adding a Cargo profile to it.

Dependent on whether you use the stable or nightly Rust toolchain the options available to you differ a bit. It's recommended you stick to the stable toolchain unless you're an advanced user.

<Tabs>
<TabItem label="Stable">

```toml