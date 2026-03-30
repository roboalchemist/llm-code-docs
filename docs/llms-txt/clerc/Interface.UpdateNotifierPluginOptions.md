# Source: https://clerc.so1ve.dev/reference/api/plugin-update-notifier/Interface.UpdateNotifierPluginOptions.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Interface.UpdateNotifierPluginOptions.md

---

url: /reference/api/clerc/Interface.UpdateNotifierPluginOptions.md
---

# Interface: UpdateNotifierPluginOptions

Defined in: [packages/plugin-update-notifier/src/index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L8)

## Extends

* `EnhancedNotifierSettings`

## Properties

&#x20;`distTag?`

`string`

Which dist-tag to use to find the latest version

**Default**

```ts twoslash
// @include: imports
"latest";
```

```ts twoslash
// @include: imports
EnhancedNotifierSettings.distTag;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:24

&#x20;`notify?`

`EnhancedNotifyOptions`

‐

‐

[packages/plugin-update-notifier/src/index.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L9)

&#x20;\~~`packageName?`~~

`string`

**Deprecated**

use `pkg.name`

```ts twoslash
// @include: imports
EnhancedNotifierSettings.packageName;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:29

&#x20;\~~`packageVersion?`~~

`string`

**Deprecated**

use `pkg.version`

```ts twoslash
// @include: imports
EnhancedNotifierSettings.packageVersion;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:33

&#x20;`pkg`

`Package`

‐

```ts twoslash
// @include: imports
EnhancedNotifierSettings.pkg;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:25

&#x20;`shouldNotifyInNpmScript?`

`boolean`

Allows notification to be shown when running as an npm script

```ts twoslash
// @include: imports
EnhancedNotifierSettings.shouldNotifyInNpmScript;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:37

&#x20;`updateCheckInterval?`

`number`

How often to check for updates

```ts twoslash
// @include: imports
EnhancedNotifierSettings.updateCheckInterval;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:35
