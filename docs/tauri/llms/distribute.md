# Distribute

import { CardGrid, LinkCard, LinkButton } from '@astrojs/starlight/components';
import CommandTabs from '@components/CommandTabs.astro';

Tauri provides the tooling you need to distribute your application either to the platform app stores or as platform-specific installers.

## Building

Tauri builds your application directly from its CLI via the `build`, `android build` and `ios build` commands.

<CommandTabs
  npm="npm run tauri build"
  yarn="yarn tauri build"
  pnpm="pnpm tauri build"
  deno="deno task tauri build"
  bun="bun tauri build"
  cargo="cargo tauri build"
/>

See the [distributing](#distributing) section to learn more about the configuration options available for each bundle
and how to distribute them to your users.

:::note
Most platforms requires code signing. See the [signing](#signing) section for more information.
:::

### Bundling

By default the `build` command automatically bundles your application for the configured formats.

If you need further customization on how the platform bundles are generated, you can split the build and bundle steps:

<CommandTabs
  npm="npm run tauri build -- --no-bundle