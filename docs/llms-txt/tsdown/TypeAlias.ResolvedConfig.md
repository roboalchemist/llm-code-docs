# Source: https://tsdown.dev/reference/api/TypeAlias.ResolvedConfig.md

---
url: /reference/api/TypeAlias.ResolvedConfig.md
---
# Type Alias: ResolvedConfig

```ts
type ResolvedConfig = Overwrite<
  MarkPartial<
    Omit<
      UserConfig,
      | 'workspace'
      | 'fromVite'
      | 'publicDir'
      | 'bundle'
      | 'injectStyle'
      | 'removeNodeProtocol'
      | 'external'
      | 'noExternal'
      | 'inlineOnly'
      | 'skipNodeModulesBundle'
      | 'logLevel'
      | 'failOnWarn'
      | 'customLogger'
      | 'envFile'
      | 'envPrefix'
    >,
    | 'globalName'
    | 'inputOptions'
    | 'outputOptions'
    | 'minify'
    | 'define'
    | 'alias'
    | 'onSuccess'
    | 'outExtensions'
    | 'hooks'
    | 'copy'
    | 'loader'
    | 'name'
    | 'banner'
    | 'footer'
    | 'checks'
    | 'css'
  >,
  {
    attw: false | AttwOptions
    clean: string[]
    deps: ResolvedDepsConfig
    devtools: false | DevtoolsOptions
    dts: false | DtsOptions
    entry: Record<string, string>
    exe: false | ExeOptions
    exports: false | ExportsOptions
    format: NormalizedFormat
    ignoreWatch: (string | RegExp)[]
    logger: Logger
    nameLabel: string | undefined
    nodeProtocol: 'strip' | boolean
    pkg?: PackageJsonWithPath
    publint: false | PublintOptions
    rawEntry?: TsdownInputOption
    report: false | ReportOptions
    root: string
    target?: string[]
    tsconfig: false | string
    unused: false | UnusedOptions
  }
>
```

Defined in: [src/config/types.ts:627](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/config/types.ts#L627)
