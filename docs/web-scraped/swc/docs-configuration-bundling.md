# Source: https://swc.rs/docs/configuration/bundling

# Bundling Configuration
🚧 This feature will be dropped in v2, in favor of SWC-based bundlers like [Parcel 2 ], [Turbopack ], [Rspack ], [fe-farm ].
Please use one of the bundlers instead.
SWC is able to bundle multiple JavaScript or TypeScript files into one.
This feature is currently named `spack `, but will be renamed to `swcpack `in `v2 `. `spack.config.js `will be deprecated for `swcpack.config.js `.
View a [basic example of bundling ].
## Configuration []
You can configure bundling using `spack.config.js `with similar options to webpack. In the future, we are exploring a webpack compatible plugin system.
spack.config.js ```module . exports = { entry: { web: __dirname + "/src/index.ts" , }, output: { path: __dirname + "/lib" , }, }; ```
> Note: CommonJS is currently required. In the future, ES Modules will be supported.

If you want auto-completion or type checking for configuration, you can wrap the export with a `config `function from `@swc/core/spack `. It’s an identity function with type annotation.
spack.config.js ```const { config } = require ( "@swc/core/spack" ); module . exports = config ({ entry: { web: __dirname + "/src/index.ts" , }, output: { path: __dirname + "/lib" , }, }); ```
### mode []
Possible values: `production `, `debug `, `none `.
Currently this value is not used, but it will behave similarly to webpack.
### entry []
Determines the entry of bundling. You may specify a file or a map of bundle name to file path.
> Note: Currently this should be absolute path. You can use `__dirname `to create one.
In the future, SWC will support using relative paths and will resolve files relative to `spack.config.js `.

### output []
You can change destination directory of the bundler using `output `.
spack.config.js ```const { config } = require ( "@swc/core/spack" ); module . exports = config ({ output: { path: __dirname + "/lib" , // Name is optional. name: "index.js" , }, }); ```
### options []
Used to control the behavior of SWC. This field is optional.