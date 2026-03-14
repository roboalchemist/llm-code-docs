# Source: https://tsdown.dev/reference/api/Interface.PackageJsonWithPath.md

---
url: /reference/api/Interface.PackageJsonWithPath.md
---
# Interface: PackageJsonWithPath

Defined in: [src/utils/package.ts:9](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/package.ts#L9)

## Extends

* `PackageJson`

## Indexable

```ts
[key: string]: any
```

## Properties

### author?

```ts
optional author: PackageJsonPerson;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:175

The “author” is one person.

#### Inherited from

```ts
PackageJson.author
```

***

### bin?

```ts
optional bin: string | Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:207

A map of command name to local file name. On install, npm will symlink that file into `prefix/bin` for global installs, or `./node_modules/.bin/` for local installs.

#### Inherited from

```ts
PackageJson.bin
```

***

### browser?

```ts
optional browser: string | Record<string, string | false>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:199

If your module is meant to be used client-side the browser field should be used instead of the main field. This is helpful to hint users that it might rely on primitives that aren’t available in Node.js modules. (e.g. window)

#### Inherited from

```ts
PackageJson.browser
```

***

### bugs?

```ts
optional bugs:
  | string
  | {
  email?: string;
  url?: string;
};
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:144

The url to your project’s issue tracker and / or the email address to which issues should be reported. These are helpful for people who encounter issues with your package.

#### Inherited from

```ts
PackageJson.bugs
```

***

### contributors?

```ts
optional contributors: PackageJsonPerson[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:179

“contributors” is an array of people.

#### Inherited from

```ts
PackageJson.contributors
```

***

### cpu?

```ts
optional cpu: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:325

If your code only runs on certain cpu architectures, you can specify which ones.

```json
{
  "cpu": ["x64", "ia32"]
}
```

Like the `os` option, you can also block architectures:

```json
{
  "cpu": ["!arm", "!mips"]
}
```

The host architecture is determined by `process.arch`

#### Inherited from

```ts
PackageJson.cpu
```

***

### dependencies?

```ts
optional dependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:215

Dependencies are specified in a simple object that maps a package name to a version range. The version range is a string which has one or more space-separated descriptors. Dependencies can also be identified with a tarball or git URL.

#### Inherited from

```ts
PackageJson.dependencies
```

***

### description?

```ts
optional description: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:132

Put a description in it. It’s a string. This helps people discover your package, as it’s listed in `npm search`.

#### Inherited from

```ts
PackageJson.description
```

***

### devDependencies?

```ts
optional devDependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:220

If someone is planning on downloading and using your module in their program, then they probably don’t want or need to download and build the external test or documentation framework that you use.
In this case, it’s best to map these additional items in a `devDependencies` object.

#### Inherited from

```ts
PackageJson.devDependencies
```

***

### exports?

```ts
optional exports: PackageJsonExports;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:262

Alternate and extensible alternative to "main" entry point.

When using `{type: "module"}`, any ESM module file MUST end with `.mjs` extension.

Docs:

* https://nodejs.org/docs/latest-v14.x/api/esm.html#esm\_exports\_sugar

#### Since

Node.js v12.7

#### Inherited from

```ts
PackageJson.exports
```

***

### files?

```ts
optional files: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:189

The optional `files` field is an array of file patterns that describes the entries to be included when your package is installed as a dependency. File patterns follow a similar syntax to `.gitignore`, but reversed: including a file, directory, or glob pattern (`*`, `**/*`, and such) will make it so that file is included in the tarball when it’s packed. Omitting the field will make it default to `["*"]`, which means it will include all files.

#### Inherited from

```ts
PackageJson.files
```

***

### funding?

```ts
optional funding: PackageJsonFunding | PackageJsonFunding[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:185

An object containing a URL that provides up-to-date information
about ways to help fund development of your package,
a string URL, or an array of objects and string URLs

#### Inherited from

```ts
PackageJson.funding
```

***

### homepage?

```ts
optional homepage: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:140

The url to the project homepage.

#### Inherited from

```ts
PackageJson.homepage
```

***

### imports?

```ts
optional imports: Record<string, string | Record<string, string>>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:267

Docs:

* https://nodejs.org/api/packages.html#imports

#### Inherited from

```ts
PackageJson.imports
```

***

### keywords?

```ts
optional keywords: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:136

Put keywords in it. It’s an array of strings. This helps people discover your package as it’s listed in `npm search`.

#### Inherited from

```ts
PackageJson.keywords
```

***

### license?

```ts
optional license: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:151

You should specify a license for your package so that people know how they are permitted to use it, and any restrictions you’re placing on it.

#### Inherited from

```ts
PackageJson.license
```

***

### main?

```ts
optional main: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:195

The main field is a module ID that is the primary entry point to your program. That is, if your package is named `foo`, and a user installs it, and then does `require("foo")`, then your main module’s exports object will be returned.
This should be a module ID relative to the root of your package folder.
For most modules, it makes the most sense to have a main script and often not much else.

#### Inherited from

```ts
PackageJson.main
```

***

### man?

```ts
optional man: string | string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:211

Specify either a single file or an array of filenames to put in place for the `man` program to find.

#### Inherited from

```ts
PackageJson.man
```

***

### module?

```ts
optional module: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:241

Non-Standard Node.js alternate entry-point to main.
An initial implementation for supporting CJS packages (from main), and use module for ESM modules.

#### Inherited from

```ts
PackageJson.module
```

***

### name?

```ts
optional name: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:124

The name is what your thing is called.
Some rules:

* The name must be less than or equal to 214 characters. This includes the scope for scoped packages.
* The name can’t start with a dot or an underscore.
* New packages must not have uppercase letters in the name.
* The name ends up being part of a URL, an argument on the command line, and a folder name. Therefore, the name can’t contain any non-URL-safe characters.

#### Inherited from

```ts
PackageJson.name
```

***

### optionalDependencies?

```ts
optional optionalDependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:224

If a dependency can be used, but you would like npm to proceed if it cannot be found or fails to install, then you may put it in the `optionalDependencies` object. This is a map of package name to version or url, just like the `dependencies` object. The difference is that build failures do not cause installation to fail.

#### Inherited from

```ts
PackageJson.optionalDependencies
```

***

### os?

```ts
optional os: string[];
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:309

You can specify which operating systems your module will run on:

```json
{
  "os": ["darwin", "linux"]
}
```

You can also block instead of allowing operating systems, just prepend the blocked os with a '!':

```json
{
  "os": ["!win32"]
}
```

The host operating system is determined by `process.platform`
It is allowed to both block and allow an item, although there isn't any good reason to do this.

#### Inherited from

```ts
PackageJson.os
```

***

### packageJsonPath

```ts
packageJsonPath: string
```

Defined in: [src/utils/package.ts:10](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/package.ts#L10)

***

### packageManager?

```ts
optional packageManager: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:376

See: https://nodejs.org/api/packages.html#packagemanager
This field defines which package manager is expected to be used when working on the current project.
Should be of the format: `<name>@<version>[#hash]`

#### Inherited from

```ts
PackageJson.packageManager
```

***

### peerDependencies?

```ts
optional peerDependencies: Record<string, string>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:228

In some cases, you want to express the compatibility of your package with a host tool or library, while not necessarily doing a `require` of this host. This is usually referred to as a plugin. Notably, your module may be exposing a specific interface, expected and specified by the host documentation.

#### Inherited from

```ts
PackageJson.peerDependencies
```

***

### private?

```ts
optional private: boolean;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:171

If you set `"private": true` in your package.json, then npm will refuse to publish it.

#### Inherited from

```ts
PackageJson.private
```

***

### publishConfig?

```ts
optional publishConfig: object & Pick<PackageJson,
  | "exports"
  | "browser"
  | "main"
  | "module"
  | "unpkg"
  | "bin"
  | "types"
  | "typings"
  | "typesVersions"
  | "os"
| "cpu">;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:329

This is a set of config values that will be used at publish-time.

#### Type Declaration

##### access?

```ts
optional access: "public" | "restricted";
```

The access level that will be used if the package is published.

##### directory?

```ts
optional directory: string;
```

**pnpm-only**

You also can use the field `publishConfig.directory` to customize
the published subdirectory relative to the current `package.json`.

It is expected to have a modified version of the current package in
the specified directory (usually using third party build tools).

##### executableFiles?

```ts
optional executableFiles: string[];
```

**pnpm-only**

By default, for portability reasons, no files except those listed in
the bin field will be marked as executable in the resulting package
archive. The executableFiles field lets you declare additional fields
that must have the executable flag (+x) set even if
they aren't directly accessible through the bin field.

##### linkDirectory?

```ts
optional linkDirectory: boolean;
```

**pnpm-only**

When set to `true`, the project will be symlinked from the
`publishConfig.directory` location during local development.

###### Default

```ts
true
```

##### registry?

```ts
optional registry: string;
```

The registry that will be used if the package is published.

##### tag?

```ts
optional tag: string;
```

The tag that will be used if the package is published.

#### Inherited from

```ts
PackageJson.publishConfig
```

***

### repository?

```ts
optional repository:
  | string
  | {
  directory?: string;
  type: string;
  url: string;
};
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:156

Specify the place where your code lives. This is helpful for people who want to contribute. If the git repo is on GitHub, then the `npm docs` command will be able to find you.
For GitHub, GitHub gist, Bitbucket, or GitLab repositories you can use the same shortcut syntax you use for npm install:

#### Type Declaration

`string`

```ts
{
  directory?: string;
  type: string;
  url: string;
}
```

#### directory?

```ts
optional directory: string;
```

If the `package.json` for your package is not in the root directory (for example if it is part of a monorepo), you can specify the directory in which it lives:

#### type

```ts
type: string
```

#### url

```ts
url: string
```

#### Inherited from

```ts
PackageJson.repository
```

***

### scripts?

```ts
optional scripts: PackageJsonScripts;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:167

The `scripts` field is a dictionary containing script commands that are run at various times in the lifecycle of your package.

#### Inherited from

```ts
PackageJson.scripts
```

***

### type?

```ts
optional type: "commonjs" | "module";
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:251

Make main entry-point be loaded as an ESM module, support "export" syntax instead of "require"

Docs:

* https://nodejs.org/docs/latest-v14.x/api/esm.html#esm\_package\_json\_type\_field

#### Default

```ts
'commonjs'
```

#### Since

Node.js v14

#### Inherited from

```ts
PackageJson.type
```

***

### types?

```ts
optional types: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:232

TypeScript typings, typically ending by `.d.ts`.

#### Inherited from

```ts
PackageJson.types
```

***

### typesVersions?

```ts
optional typesVersions: Record<string, Record<string, string[]>>;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:292

The field is used to specify different TypeScript declaration files for
different versions of TypeScript, allowing for version-specific type definitions.

#### Inherited from

```ts
PackageJson.typesVersions
```

***

### typings?

```ts
optional typings: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:236

This field is synonymous with `types`.

#### Inherited from

```ts
PackageJson.typings
```

***

### unpkg?

```ts
optional unpkg: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:203

The `unpkg` field is used to specify the URL to a UMD module for your package. This is used by default in the unpkg.com CDN service.

#### Inherited from

```ts
PackageJson.unpkg
```

***

### version?

```ts
optional version: string;
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:128

Version must be parseable by `node-semver`, which is bundled with npm as a dependency. (`npm install semver` to use it yourself.)

#### Inherited from

```ts
PackageJson.version
```

***

### workspaces?

```ts
optional workspaces:
  | string[]
  | {
  nohoist?: string[];
  packages?: string[];
};
```

Defined in: node\_modules/.pnpm/pkg-types@2.3.0/node\_modules/pkg-types/dist/index.d.mts:274

The field is used to define a set of sub-packages (or workspaces) within a monorepo.

This field is an array of glob patterns or an object with specific configurations for managing
multiple packages in a single repository.

#### Type Declaration

`string`\[]

```ts
{
  nohoist?: string[];
  packages?: string[];
}
```

#### nohoist?

```ts
optional nohoist: string[];
```

Packages to block from hoisting to the workspace root.
Uses glob patterns to match module paths in the dependency tree.

Docs:

* https://classic.yarnpkg.com/blog/2018/02/15/nohoist/

#### packages?

```ts
optional packages: string[];
```

Workspace package paths. Glob patterns are supported.

#### Inherited from

```ts
PackageJson.workspaces
```
