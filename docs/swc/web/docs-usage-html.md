# Source: https://swc.rs/docs/usage/html

## Installation []
### pnpm npm yarn pnpm
```pnpm i -D @swc/html ```
### npm
```npm i -D @swc/html ```
### yarn
```yarn add -D @swc/html ```
## Usage []
### `minify() `/ `minifySync() `[]
If you are minifying a whole HTML document, you can use the `minify() `function.
```import { minify } from '@swc/html' ; const html = await minify ( '<div>Hello, world!</div>' , { }); ```
### `minifyFragment() `/ `minifyFragmentSync() `[]
If you are minifying a fragment of HTML, you can use the `minifyFragment() `function.
```import { minifyFragment } from '@swc/html' ; const html = await minifyFragment ( '<div>Hello, world!</div>' , { }); ```