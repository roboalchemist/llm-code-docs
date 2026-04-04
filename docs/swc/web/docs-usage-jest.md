# Source: https://swc.rs/docs/usage/jest

# @swc/jest
To make your Jest tests run faster, you can swap out the default JavaScript-based runner ( `ts-jest `) for a [drop-in Rust replacement ]using SWC.
## Installation []
### pnpm npm yarn pnpm
```pnpm i -D jest @swc/core @swc/jest ```
### npm
```npm i -D jest @swc/core @swc/jest ```
### yarn
```yarn add -D jest @swc/core @swc/jest ```
## Usage []
Inside `jest.config.js `, configure Jest to use SWC:
jest.config.js ```module . exports = { transform: { '^.+ \\ .(t|j)sx?$' : '@swc/jest' , }, } ```
It will load the SWC configuration from `.swcrc `by default. You also can customize it:
jest.config.js ```const fs = require ( 'fs' ) const config = JSON . parse (fs. readFileSync ( `${ __dirname }/.swcrc` , 'utf-8' )) module . exports = { transform: { '^.+ \\ .(t|j)sx?$' : [ '@swc/jest' , { ... config, /* custom configuration in Jest */ }], }, } ```
## Q & A []
### Q: Jest uses CommonJS by default. But I want to use ESM []
A: Setup Jest following this [Guide ].
For JavaScript, edit `package.json `as follows:
package.json ```{ // ... "type" : "module" } ```
For TypeScript, edit `jest.config.js `as follows:
jest.config.js ```module . exports = { // ... extensionsToTreatAsEsm: [ '.ts' , '.tsx' ], } ```
Run test with `--experimental-vm-modules `:
```cross-env NODE_OPTIONS=--experimental-vm-modules jest # or node --experimental-vm-modules ./node_modules/jest/bin/jest.js ```
### Q: What ECMAScript target is set by `jsc.target `? []
A: By default, the version supported by your Node runtime.

| Node version  || Default `jsc.target ` ||
| 12  || ’es2018’  ||
| 13  || ’es2019’  ||
| 14  || ’es2020’  ||
| 15  || ’es2021’  ||
| 16  || ’es2021’  ||
| 17  || ’es2022’  ||
| 18  || ’es2023’  ||

You can customize this by setting an explicit version in `jest.config.js `:
jest.config.js ```module . exports = { transform: { "^.+ \\ .(t|j)sx?$" : [ "@swc/jest" , { jsc: { target: "es2021" , }, }, ], }, } ```