# Source: https://rspack.dev/guide/features/plugin.md

# Source: https://rspack.dev/guide/compatibility/plugin.md

# Plugin compatibility

This page lists the compatibility status of common community plugins in Rspack.

For details on Rspack's support for webpack built-in plugins, see [Webpack-aligned built-in plugins](/plugins/webpack/index.md).

The table only covers common community plugins. For others, you can verify their functionality yourself, and you're welcome to add them to this page.

| Plugin | Support status | Notes |
| --- | --- | --- |
| [circular-dependency-plugin](https://github.com/aackerman/circular-dependency-plugin) | 🔵 Included | Use [CircularDependencyRspackPlugin](/plugins/rspack/circular-dependency-rspack-plugin) instead |
| [copy-webpack-plugin](https://www.npmjs.com/package/copy-webpack-plugin) | 🔵 Included | Use [CopyRspackPlugin](/plugins/rspack/copy-rspack-plugin) instead |
| [mini-css-extract-plugin](https://webpack.js.org/plugins/mini-css-extract-plugin) | 🔵 Included | Use [CssExtractRspackPlugin](/plugins/rspack/css-extract-rspack-plugin) instead |
| [pnp-webpack-plugin](https://github.com/arcanis/pnp-webpack-plugin) | 🔵 Included | Use [resolve.pnp](/config/resolve#resolvepnp) instead |
| [tsconfig-paths-webpack-plugin](https://www.npmjs.com/package/tsconfig-paths-webpack-plugin) | 🔵 Included | Use [resolve.tsConfig](/config/resolve#resolvetsconfig) instead |
| [@loadable/webpack-plugin](https://www.npmjs.com/package/@loadable/webpack-plugin) | 🟢 Compatible |  |
| [@sentry/webpack-plugin](https://www.npmjs.com/package/@sentry/webpack-plugin) | 🟢 Compatible | Support for this plugin >= v1.20.1 |
| [@soda/friendly-errors-webpack-plugin](https://github.com/sodatea/friendly-errors-webpack-plugin) | 🟢 Compatible |  |
| [@vanilla-extract/webpack-plugin](https://github.com/vanilla-extract-css/vanilla-extract) | 🟢 Compatible |  |
| [assets-webpack-plugin](https://github.com/ztoben/assets-webpack-plugin) | 🟢 Compatible |  |
| [case-sensitive-paths-webpack-plugin](https://github.com/Urthen/case-sensitive-paths-webpack-plugin) | 🟢 Compatible | `useBeforeEmitHook` option not supported |
| [clean-webpack-plugin](https://github.com/johnagan/clean-webpack-plugin) | 🟢 Compatible |  |
| [compression-webpack-plugin](https://github.com/webpack/compression-webpack-plugin) | 🟢 Compatible |  |
| [css-minimizer-webpack-plugin](https://github.com/webpack/css-minimizer-webpack-plugin) | 🟢 Compatible | Rspack provides [LightningCssMinimizerRspackPlugin](/plugins/rspack/lightning-css-minimizer-rspack-plugin) to deliver better performance |
| [dotenv-webpack](https://www.npmjs.com/package/dotenv-webpack) | 🟢 Compatible |  |
| [error-overlay-webpack-plugin](https://github.com/gregberge/error-overlay-webpack-plugin) | 🟢 Compatible |  |
| [eslint-import-resolver-webpack](https://www.npmjs.com/package/eslint-import-resolver-webpack) | 🟢 Compatible |  |
| [filemanager-webpack-plugin](https://github.com/gregnb/filemanager-webpack-plugin) | 🟢 Compatible |  |
| [friendly-errors-webpack-plugin](https://www.npmjs.com/package/friendly-errors-webpack-plugin) | 🟢 Compatible |  |
| [html-minimizer-webpack-plugin](https://github.com/webpack/html-minimizer-webpack-plugin) | 🟢 Compatible |  |
| [html-webpack-plugin](https://www.npmjs.com/package/html-webpack-plugin) | 🟢 Compatible |  |
| [json-minimizer-webpack-plugin](https://github.com/webpack/json-minimizer-webpack-plugin) | 🟢 Compatible |  |
| [license-webpack-plugin](https://www.npmjs.com/package/license-webpack-plugin) | 🟢 Compatible |  |
| [moment-locales-webpack-plugin](https://www.npmjs.com/package/moment-locales-webpack-plugin) | 🟢 Compatible | Support for this plugin was implemented in v0.7.0, please upgrade the Rspack version to use it |
| [monaco-editor-webpack-plugin](https://www.npmjs.com/package/monaco-editor-webpack-plugin) | 🟢 Compatible |  |
| [node-polyfill-webpack-plugin](https://www.npmjs.com/package/node-polyfill-webpack-plugin) | 🟢 Compatible |  |
| [serwist](https://github.com/serwist/serwist) | 🟢 Compatible |  |
| [stylelint-webpack-plugin](https://github.com/webpack/stylelint-webpack-plugin) | 🟢 Compatible |  |
| [terser-webpack-plugin](https://webpack.js.org/plugins/terser-webpack-plugin) | 🟢 Compatible | Rspack provides [SwcJsMinimizerRspackPlugin](/plugins/rspack/swc-js-minimizer-rspack-plugin) to deliver better performance |
| [webpack-bundle-analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer) | 🟢 Compatible |  |
| [webpack-stats-plugin](https://www.npmjs.com/package/webpack-stats-plugin) | 🟢 Compatible |  |
| [webpackbar](https://www.npmjs.com/package/webpackbar) | 🟢 Compatible |  |
| [@nx/webpack](https://www.npmjs.com/package/@nx/webpack) | 🟢 Alternative | Use [@nx/rspack](https://www.npmjs.com/package/@nx/rspack) instead |
| [@pmmmwh/react-refresh-webpack-plugin](https://www.npmjs.com/package/@pmmmwh/react-refresh-webpack-plugin) | 🟢 Alternative | Use [@rspack/plugin-react-refresh](/guide/tech/react#rspackplugin-react-refresh) instead |
| [eslint-webpack-plugin](https://github.com/webpack-contrib/eslint-webpack-plugin) | 🟢 Alternative | Use [eslint-rspack-plugin](https://github.com/rstackjs/eslint-rspack-plugin) instead |
| [fork-ts-checker-webpack-plugin](https://github.com/TypeStrong/fork-ts-checker-webpack-plugin) | 🟢 Alternative | Use [ts-checker-rspack-plugin](https://github.com/rstackjs/ts-checker-rspack-plugin) instead |
| [html-webpack-tags-plugin](https://github.com/jharris4/html-webpack-tags-plugin) | 🟢 Alternative | Use [html-rspack-tags-plugin](https://github.com/rstackjs/html-rspack-tags-plugin) instead |
| [progress-bar-webpack-plugin](https://www.npmjs.com/package/progress-bar-webpack-plugin) | 🟢 Alternative | Use [webpackbar](https://www.npmjs.com/package/webpackbar) instead |
| [speed-measure-webpack-plugin](https://www.npmjs.com/package/speed-measure-webpack-plugin) | 🟢 Alternative | Use [Rsdoctor](/guide/optimization/use-rsdoctor) instead |
| [webpack-filter-warnings-plugin](https://github.com/mattlewis92/webpack-filter-warnings-plugin) | 🟢 Alternative | Use [ignoreWarnings](/config/other-options#ignorewarnings) instead |
| [webpack-manifest-plugin](https://github.com/shellscape/webpack-manifest-plugin) | 🟢 Alternative | Use [rspack-manifest-plugin](https://github.com/rstackjs/rspack-manifest-plugin) instead |
| [webpack-subresource-integrity](https://github.com/waysact/webpack-subresource-integrity) | 🟢 Alternative | Use [SubresourceIntegrityPlugin](/plugins/rspack/subresource-integrity-plugin) instead |
| [webpack-virtual-modules](https://github.com/sysgears/webpack-virtual-modules) | 🟢 Alternative | Use [VirtualModulesPlugin](/plugins/rspack/virtual-modules-plugin) instead |
| [workbox-webpack-plugin](https://www.npmjs.com/package/workbox-webpack-plugin) | 🟢 Alternative | Use [@aaroon/workbox-rspack-plugin](https://github.com/Clarkkkk/workbox-rspack-plugin) instead |
| [add-asset-html-webpack-plugin](https://github.com/SimenB/add-asset-html-webpack-plugin) | 🟡 Partially compatible | This plugin depends on html-webpack-plugin |
| [html-webpack-harddisk-plugin](https://github.com/jantimon/html-webpack-harddisk-plugin) | 🟡 Partially compatible | This plugin depends on html-webpack-plugin |
| [image-minimizer-webpack-plugin](https://www.npmjs.com/package/image-minimizer-webpack-plugin) | 🟡 Partially compatible | Only supports using [loader](https://www.npmjs.com/package/image-minimizer-webpack-plugin#standalone-loader) standalone |
| [webpack-assets-manifest](https://github.com/webdeveric/webpack-assets-manifest) | 🟡 Partially compatible | Only supports basic usage |
| [@cypress/webpack-preprocessor](https://github.com/cypress-io/cypress) | 🔴 Incompatible | To be implemented |
| [@intlify/unplugin-vue-i18n](https://github.com/intlify/bundle-tools) | 🔴 Incompatible | To be implemented |
| [@ngtools/webpack](https://www.npmjs.com/package/@ngtools/webpack) | 🔴 Incompatible | To be implemented |
| [@storybook/react-docgen-typescript-plugin](https://github.com/hipstersmoothie/react-docgen-typescript-plugin) | 🔴 Incompatible | To be implemented |
| [critters-webpack-plugin](https://github.com/GoogleChromeLabs/critters) | 🔴 Incompatible | To be implemented |
| [git-revision-webpack-plugin](https://www.npmjs.com/package/git-revision-webpack-plugin) | 🔴 Incompatible | To be implemented |
| [last-call-webpack-plugin](https://github.com/NMFR/last-call-webpack-plugin) | 🔴 Incompatible | To be implemented |
| [webpack-remove-empty-scripts](https://github.com/webdiscus/webpack-remove-empty-scripts) | 🔴 Incompatible | To be implemented |


You can view examples of common plugins at [rstack-examples](https://github.com/rstackjs/rstack-examples).

Additionally, you can check out the community Rspack plugins at [awesome-rstack](https://github.com/rstackjs/awesome-rstack).
