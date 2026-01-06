# Getting Started

Source: https://knip.dev/overview/getting-started

## Requirements

Knip v5 requires at least Node.js v18.18.0. Or Bun.

Want to try Knip without installation? Visitthe playground.

## Installation

This is the easiest and recommended way to install Knip:

- npm
- pnpm
- bun
- yarn

```typescript
npminit@knip/config
```

```typescript
pnpmcreate@knip/config
```

```typescript
buncreate@knip/config
```

```typescript
yarncreate@knip/config
```

Now you can run Knip to lint your project:

- npm
- pnpm
- bun
- yarn

```typescript
npmrunknip
```

```typescript
pnpmknip
```

```typescript
bunknip
```

```typescript
yarnknip
```

Knip will lint your project and report unused dependencies, exports and files.

If the output makes sense to you, feel free to go to the next page:configuration.

## Too Much?

In large or complex codebases the output might be overwhelming. Start by
limiting the number of shown issues per type:

- npm
- pnpm
- bun
- yarn

```typescript
npmrunknip----max-show-issues5
```

```typescript
pnpmknip--max-show-issues5
```

```typescript
bunknip--max-show-issues5
```

```typescript
yarnknip--max-show-issues5
```

The output is easier to digest and may include some configuration hints to get
an idea of what’s left to configure. Many unused files? Go toconfigurationand follow up withtroubleshootingif needed.

Do not use theignoreoption just to get rid of unwanted output. ReadConfiguring Project Filesto get the most out of Knip.

## Manual

Alternatively, manually install Knip using your package manager:

- npm
- pnpm
- bun
- yarn

```typescript
npminstall-Dkniptypescript@types/node
```

```typescript
pnpmadd-Dkniptypescript@types/node
```

```typescript
bunadd-Dkniptypescript@types/node
```

```typescript
yarnadd-Dkniptypescript@types/node
```

Knip usestypescriptand@types/nodeas peer dependencies to increase
compatibility with your project. No worries, they’re probably in yournode_modulesalready.

Then add aknipscript to yourpackage.json:

```typescript
{"name":"my-project","scripts":{"knip":"knip"}}
```

## Without installation

To run Knip without adding it to your project:

- npm
- pnpm
- bun

```typescript
npxknip
```

```typescript
pnpmdlxknip
```

```typescript
bunxknip
```

In this scenariotypescriptand@types/nodeare expected to be installed
already.

ISC License© 2024Lars Kappert

