# Source: https://swc.rs/docs/configuration/supported-browsers

# Supported Browsers
Starting with `v1.1.10 `, you can now use `browserslist `to automatically configure supported browsers.
## Usage []
.swcrc ```{ "env" : { "targets" : { "chrome" : "79" }, "mode" : "entry" , "coreJs" : "3.22" } } ```
## Options []
### targets []
`string | Array<string> | { [string]: string } `, defaults to `{} `.
Describes the environments you support/target for your project. This can either be a [browserslist-compatible ]query [(with limitations) ]:
.swcrc ```{ "env" : { "targets" : "> 0.25%, not dead" } } ```
Or an object of minimum environment versions to support:
.swcrc ```{ "env" : { "targets" : { "chrome" : "58" , "ie" : "11" } } } ```
Example environments:
- `chrome `
- `opera `
- `edge `
- `firefox `
- `safari `
- `ie `
- `ios `
- `android `
- `node `
- `electron `

If `targets `is not specified, SWC uses `browserslist `to get target information.
### path []
- `string `, defaults to current directory.
- `path `specifies the directory to load the `browserslist `module and any browserslist configuration files. For example, `.browserslistrc `or `browserslist `field in package.json. This can be useful if your build system isn’t in the root of your project.

### mode []
- `string `, defaults to `undefined `.
- Possible values: `usage `, `entry `, `undefined `(this matches [`useBuiltIns `]from Babel)

⚠️ The `usage `mode is currently not as efficient as Babel, iff you have a usage like `"foo"["a" + "t"]() `.
SWC does not evaluate the expression `“a” + “t” `and will not include the `String.prototype.at `polyfill.
### skip []
Define ES features to skip to reduce bundle size. For example, your `.swcrc `could be:
.swcrc ```{ "env" : { "skip" : [ "core-js/modules/foo" ] } } ```
### coreJs []
- `string `, defaults to `undefined `.
- `coreJs `specifies the version of `core-js `to use, can be any core-js versions supported by swc. E.g., `"3.22" `.

The option has an effect when used alongside `mode: "usage" `or `mode: "entry" `. It is recommended to specify the minor version (E.g. `"3.22" `) otherwise `"3" `will be interpreted as `"3.0" `which may not include polyfills for the latest features.
## Additional Options []
- `debug `: ( *boolean *) defaults to `false `.
- `dynamicImport `: ( *boolean *) defaults to `false `.
- `loose `: ( *boolean *) defaults to `false `. Enable [loose transformations ]for any plugins that allow them.
- `include `: ( *string[] *) can be a `core-js `module ( `es.math.sign `) or an SWC pass ( `transform-spread `).
- `exclude `: ( *string[] *) can be a `core-js `module ( `es.math.sign `) or an SWC pass ( `transform-spread `).
- `shippedProposals `: ( *boolean *) defaults to `false `.
- `forceAllTransforms `: ( *boolean *) defaults to `false `. Enable all possible transforms.
