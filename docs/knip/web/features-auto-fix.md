# Auto-fix

Source: https://knip.dev/features/auto-fix

Run Knip as you normally would, and if the report looks good then run it again
with the--fixflag to let Knip automatically apply fixes. It fixes the
followingissue types:

- Removeexportkeyword for unused exports and exported types
- Removeexport defaultkeywords for unused default exports
- Remove exports, re-exports and exported types
- Remove unused enum members
- Remove unused class members (disabled by default)
- Remove unuseddependenciesanddevDependenciesfrompackage.json
- Remove unused files

Use a VCS (version control system) like Git to review and undo changes as
necessary.

## Flags

### Fix

Add the--fixflag to remove unused exports and dependencies:

```typescript
knip--fix
```

Add--allow-remove-filesto allow Knip to remove unused files:

```typescript
knip--fix--allow-remove-files
```

Use--fix-typeto fix only specific issue types:

- files
- exports
- types
- dependencies
- catalog

```typescript
knip--fix-typeexports,typesknip--fix-typeexports--fix-typetypes# same as above
```

### Format

Add--formatto format the modified files using the formatter and
configuration in your project. Supports Biome, deno fmt, dprint and Prettier
(usingFormatly):

```typescript
knip--fix--format
```

## Demo

## Post-fix

After Knip has fixed issues, there are four things to consider:

### 1. Use a formatter

Use a tool like Prettier or Biome if the code needs formatting. Knip removes the
minimum amount of code while leaving it in a working state.

Add the--formatflag to format the modified files using the formatter and
configuration in your project.

### 2. Unused variables

Use a tool like ESLint or Biome to find and remove unused variables inside
files. Even better, tryremove-unused-varsto remove unused variables
within files.

This may result in more deleted code, and Knip may then find more unused code.
Rinse and repeat!

### 3. Unused dependencies

Verify changes inpackage.jsonand update dependencies using your package
manager.

- npm
- pnpm
- bun
- yarn

```typescript
npminstall
```

```typescript
pnpminstall
```

```typescript
buninstall
```

```typescript
yarn
```

### 4. Install unlisted dependencies

If Knip reports unlisted dependencies or binaries, they should be installed
using the package manager in the project, for example:

- npm
- pnpm
- bun
- yarn

```typescript
npminstallunlisted-package
```

```typescript
pnpmaddunlisted-package
```

```typescript
bunaddunlisted-package
```

```typescript
yarnaddunlisted-package
```

## Example results

### Exports

Theexportkeyword for unused exports is removed:

```typescript
export const unused = 1;export default class MyClass {}const unused = 1;class MyClass {}
```

Thedefaultkeyword was also removed here.

Knip removes the whole or part of export declarations:

```typescript
type Snake = 'python' | 'anaconda';const Owl = 'Hedwig';const Hawk = 'Tony';export type { Snake };export { Owl, Hawk };;;
```

### Re-exports

Knip removes the whole or part of re-exports:

```typescript
export { Cat, Dog } from './pets';export { Lion, Elephant } from './jungle';export { Elephant } from './jungle'
```

Also across any chain of re-exports:

- module.ts
- barrel.ts
- index.ts

```typescript
export const Hawk = 'Tony';export const Owl = 'Hedwig';const Owl = 'Hedwig';
```

```typescript
export * from './module.js';
```

```typescript
export { Hawk, Owl } from './barrel.js';export { Hawk } from './barrel.js'
```

### Export assignments

Knip removes individual exported items in “export assignments”, but does not
remove the entire export declaration if it’s empty:

```typescript
export const { a, b  } = fn();export const {   } = fn();export const [c, d] = [c, d];export const [, ] = [c, d];
```

Reason: the right-hand side of the assignment might have side-effects. It’s not
safe to always remove the whole declaration. This could be improved in the
future (feel free to open an issue/RFC).

### Enum members

Unused members of enums are removed:

```typescript
export enum Directions {North = 1,East = 2,South = 3,West = 4,}
```

### CommonJS

Knip supports CommonJS and removes unused exports:

```typescript
module.exports = { identifier, unused };module.exports = { identifier,  };module.exports.UNUSED = 1;module.exports['ACCESS'] = 1;
```

Warning: the right-hand side of such an assignment might have side-effects. Knip
currently removes the whole declaration (feel free to open an issue/RFC).

### Dependencies

Unused dependencies are removed frompackage.json:

```typescript
{"name": "my-package","dependencies": {"rimraf": "*","unused-dependency": "*""rimraf": "*"},"devDependencies": {"unreferenced-package": "5.3.3"}"devDependencies": {}}
```

### Class membersexperimental

Unused members of classes can be removed:

```typescript
export class Rectangle {constructor(public width: number, public height: number) {}static Key = 1;area() {return this.width * this.height;}public get unusedGetter(): string {return 'unusedGetter';}}
```

Currently Knip might be too eager removing class members when they’re not
referenced internally but meant to be called by an external library. For
instance, Knip might thinkcomponentDidMountandrenderin React class
component are unused and will remove those.

Note thatclassMembersaren’t included by default.

## What’s not included

Operations that auto-fix does not (yet) perform and why:

- Add unlisted (dev) dependencies topackage.json(should it go intodependenciesordevDependencies? For monorepos in current workspace or
root?)
- Add unlisted binaries (which package and package version contains the used
binary?)
- Fix duplicate exports (which one should be removed?)

ISC License© 2024Lars Kappert

