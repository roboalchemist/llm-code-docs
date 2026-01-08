# Source: https://swc.rs/docs/usage/swc-loader

# swc-loader
This module allows you to use SWC with webpack.
For Rspack users, you can use Rspack’s [builtin:swc-loader ], without the need to install the swc-loader package.
## Installation []
### pnpm npm yarn pnpm
```pnpm i -D @swc/core swc-loader ```
### npm
```npm i -D @swc/core swc-loader ```
### yarn
```yarn add -D @swc/core swc-loader ```
## Usage []
webpack.config.js ```module : { rules : [ { test: / \. m ? js $ / , exclude: / (node_modules) / , use: { // `.swcrc` can be used to configure swc loader: "swc-loader" } } ] } ```
### Options []
Loader options are passed through to SWC as if they were part of your `.swcrc `.
For instance, [to configure `browserslist `-based `targets `for compilation ]and see the effect:
```{ use : { loader : "swc-loader" , options : { env : { targets : "defaults" , debug : true } } } } ```
### React Development []
The [`jsc.transform.react.development `]option is automatically set based on the [webpack `mode `].
### With babel-loader []
When used with babel-loader, the parseMap option must be set to true.
webpack.config.js ```module : { rules : [ { test: / \. m ? js $ / , exclude: / (node_modules) / , use: { loader: "swc-loader" , options: { parseMap: true } } } ] } ```