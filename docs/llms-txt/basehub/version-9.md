# Version 9

> Learn how to upgrade from v8 to v9.

```
pnpm i basehub@latest
```

v9 doesn’t introduce too many new features nor breaking changes, but it does fundamentally change how types are generated. Critically, the `basehub` SDK can now work without a “generation step”, and the generation step now only augments the SDK with type information.

This seems subtle, but fixes many bugs related to `basehub` not being able to resolve. For context, before v9, running `basehub dev` or `basehub build` was required for the runtime to get its graphql client. The generation step created the SDK, plus the types. Now, the client is “static” in the sense that’s ready to use once installed, and the generation step is just there for optional typesafety. Additionally, this typesafety works with [TypeScript’s declaration merging](https://www.typescriptlang.org/docs/handbook/declaration-merging.html), which means no more “Restart TS server” to make types work again.

## New Features and Bug Fixes

*   `basehub` now works without a “generation step”, albeit without types.
    
    *   Running `basehub dev` or `basehub build` is now not required by the runtime. That being said, it’s recommended you keep them as they’re in charge of generating types.
        
*   “Restart TS Server” in your IDE should be much less needed.
    

## SDK Breaking Changes

*   The SDK now exposes an ESM-only bundle and uses `package.json`’s `"exports"` field for subpath exports. As a result, your `tsconfig.json` must set `"moduleResolution"` to `"nodenext"` or `"bundler"` under `compilerOptions` for TypeScript to resolve modules correctly.
    
*   `strictNullChecks: true` is required in order for types to work correctly.
    
*   Deprecation of the `.basehub` directory. Now, the generation creates a `basehub-types.d.ts` file and a `basehub.config.ts`. Both files are optional (the runtime doesn’t depend on them at all).
    
    *   This means that old type imports, like `import { QueryGenqlSelection } from ‘@/.basehub’` or similar, should now be directed to `basehub-types.d.ts`
        
*   `createClient` is no longer exported from `”basehub”`. This function was an alias to `import { basehub } from 'basehub'` and we don’t see a point in having that, so we removed it.
    

## API Breaking Changes

*   None
    

That should be all!