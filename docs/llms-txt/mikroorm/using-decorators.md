# Source: https://mikro-orm.io/docs/using-decorators.md

# Using Decorators

This guide covers using class decorators to define entities. While the [Getting Started guide](https://mikro-orm.io/docs/guide/first-entity.md) uses the `defineEntity` helper for its simplicity and full type inference, decorators remain a powerful and popular approach for entity definition.

## Decorator Types[​](#decorator-types "Direct link to Decorator Types")

MikroORM v7 supports two types of decorators:

| Feature             | Legacy (Experimental) Decorators    | ES Spec Decorators         |
| ------------------- | ----------------------------------- | -------------------------- |
| TypeScript config   | `experimentalDecorators: true`      | No special config needed   |
| Package             | `@mikro-orm/decorators/legacy`      | `@mikro-orm/decorators/es` |
| Metadata reflection | Supported (with `reflect-metadata`) | Not supported              |
| ts-morph support    | Yes                                 | Yes                        |
| Transpiler support  | tsc, swc, babel (with plugins)      | tsc, esbuild, swc          |

### Legacy (Experimental) Decorators[​](#legacy-experimental-decorators "Direct link to Legacy (Experimental) Decorators")

Legacy decorators are the traditional TypeScript decorators that have been available for years. They require the `experimentalDecorators` compiler option.

tsconfig.json

```
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true // only needed with reflect-metadata
  }
}
```

./entities/User.ts

```
import { Entity, PrimaryKey, Property } from '@mikro-orm/decorators/legacy';

@Entity()
export class User {

  @PrimaryKey()
  id!: number;

  @Property()
  fullName!: string;

  @Property()
  email!: string;

  @Property({ nullable: true })
  age?: number;

}
```

### ES Spec Decorators (Stage 3)[​](#es-spec-decorators-stage-3 "Direct link to ES Spec Decorators (Stage 3)")

ES spec decorators follow the [TC39 Stage 3 proposal](https://github.com/tc39/proposal-decorators) and are now supported natively by TypeScript 5.0+ without any configuration. They work with modern bundlers like esbuild out of the box.

./entities/User.ts

```
import { Entity, PrimaryKey, Property } from '@mikro-orm/decorators/es';

@Entity()
export class User {

  @PrimaryKey()
  id!: number;

  @Property()
  fullName!: string;

  @Property()
  email!: string;

  @Property()
  age?: number;

}
```

ES Spec Decorator Limitations

ES spec decorators do **not** support metadata reflection. This means:

* You cannot use `reflect-metadata` with ES spec decorators
* You must always provide the target entity type explicitly in relation decorators
* The `TsMorphMetadataProvider` can still infer types from your source code

## Metadata Providers[​](#metadata-providers "Direct link to Metadata Providers")

When using decorators, MikroORM needs a way to understand the types of your entity properties. This is handled by metadata providers.

### ReflectMetadataProvider[​](#reflectmetadataprovider "Direct link to ReflectMetadataProvider")

The `ReflectMetadataProvider` uses the `reflect-metadata` package to read type information emitted by the TypeScript compiler. This approach is fast and lightweight, but has some limitations.

**Installation:**

* npm
* Yarn
* pnpm
* Bun

```
npm install reflect-metadata
```

```
yarn add reflect-metadata
```

```
pnpm add reflect-metadata
```

```
bun add reflect-metadata
```

**Configuration:**

mikro-orm.config.ts

```
import { ReflectMetadataProvider } from '@mikro-orm/decorators/legacy';
import { defineConfig } from '@mikro-orm/sqlite';

export default defineConfig({
  metadataProvider: ReflectMetadataProvider,
  entities: [User, Article], // explicit entity references recommended
  // ...
});
```

**TypeScript Configuration:**

tsconfig.json

```
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "emitDecoratorMetadata": true
  }
}
```

**Bootstrap:**

app.ts

```
import 'reflect-metadata'; // Must be imported before any entity
import { MikroORM } from '@mikro-orm/sqlite';
```

**Limitations:**

When using `reflect-metadata`, you need to be more explicit in your decorators:

```
import { Entity, ManyToOne, PrimaryKey, Property } from '@mikro-orm/decorators/legacy';

@Entity()
export class Article {

  @PrimaryKey()
  id!: number;

  @Property()
  title!: string;

  // Must specify `entity` and `nullable` explicitly
  @ManyToOne(() => User, { nullable: true })
  author?: User;

  // Must specify `entity`, `nullable` and `ref` explicitly
  @ManyToOne(() => Publisher, { ref: true, nullable: true })
  publisher?: Ref<Publisher>;

  // Array types need explicit items
  @Property({ type: 'string[]' })
  tags: string[] = [];

}
```

**Type inference limitations with reflect-metadata:**

| Scenario            | ts-morph             | reflect-metadata                |
| ------------------- | -------------------- | ------------------------------- |
| Scalar types        | Automatic            | Automatic                       |
| Optional properties | Inferred as nullable | Requires `nullable: true`       |
| Relation targets    | Automatic            | Requires `entity: () => Entity` |
| `Ref<T>` wrapper    | Automatic            | Requires `ref: true`            |
| Array element types | Automatic            | Requires explicit `type`        |
| Enums               | Automatic            | Requires `items: () => Enum`    |
| Union types         | Supported            | Not supported                   |

ES Spec Decorators

`ReflectMetadataProvider` only works with legacy decorators. ES spec decorators do not support `emitDecoratorMetadata`, so you cannot use reflect-metadata with them.

### TsMorphMetadataProvider[​](#tsmorphmetadataprovider "Direct link to TsMorphMetadataProvider")

The `TsMorphMetadataProvider` uses the TypeScript Compiler API (via [ts-morph](https://ts-morph.com)) to read type information directly from your source files. This is slower than `ReflectMetadataProvider`, but it supports inferring many options from the TypeScript source code.

**Installation:**

* npm
* Yarn
* pnpm
* Bun

```
npm install @mikro-orm/reflection
```

```
yarn add @mikro-orm/reflection
```

```
pnpm add @mikro-orm/reflection
```

```
bun add @mikro-orm/reflection
```

**Configuration:**

mikro-orm.config.ts

```
import { TsMorphMetadataProvider } from '@mikro-orm/reflection';
import { defineConfig } from '@mikro-orm/sqlite';

export default defineConfig({
  metadataProvider: TsMorphMetadataProvider,
  entities: [User, Article],
  // ...
});
```

**TypeScript Configuration:**

tsconfig.json

```
{
  "compilerOptions": {
    "declaration": true,
    "experimentalDecorators": true
  }
}
```

The `declaration: true` option is required because ts-morph reads `.d.ts` files when running from compiled JavaScript.

**Benefits:**

* Automatically infers property types, including complex types and generics
* Infers nullability from optional properties (`?`)
* Works with both legacy and ES spec decorators
* Allows DRY entity definitions (less decorator options needed)

**Considerations:**

* Slower discovery (mitigated by metadata caching)
* Requires `.d.ts` files to be generated
* Not compatible with some bundlers (e.g., webpack in certain configurations)

**Folder-based discovery and ESM:**

When using folder-based discovery (glob patterns in `entities` option) in an ESM project with test runners like Vitest, you may encounter an error like `TypeError: Unknown file extension ".ts"` (ERR\_UNKNOWN\_FILE\_EXTENSION). This happens because the dynamic import of your entities fails to resolve TypeScript files - MikroORM performs these imports internally, and tools like Vitest cannot automatically transform them.

To work around this, you can override the `dynamicImportProvider` option in your ORM config. This allows you to use an `import` call defined inside the context of your ESM application:

mikro-orm.config.ts

```
export default defineConfig({
  // ...
  // for vitest to get around `TypeError: Unknown file extension ".ts"` (ERR_UNKNOWN_FILE_EXTENSION)
  dynamicImportProvider: id => import(id),
});
```

This tells MikroORM to use your application's import context instead of its own, allowing proper TypeScript file resolution.

**Example - DRY entity definition with ts-morph:**

```
import { Entity, ManyToOne, PrimaryKey, Property } from '@mikro-orm/decorators/legacy';

@Entity()
export class Article {

  @PrimaryKey()
  id!: number;

  @Property()
  title!: string;

  // ts-morph infers: type is User, nullable is true
  @ManyToOne()
  author?: User;

  // ts-morph infers the Ref wrapper and target entity
  @ManyToOne()
  publisher?: Ref<Publisher>;

}
```

### Metadata Caching[​](#metadata-caching "Direct link to Metadata Caching")

When using `TsMorphMetadataProvider`, the discovery process can be slow due to TypeScript parsing. MikroORM caches the metadata to speed up subsequent startups.

mikro-orm.config.ts

```
import { defineConfig } from '@mikro-orm/sqlite';
import { TsMorphMetadataProvider } from '@mikro-orm/reflection';

export default defineConfig({
  metadataProvider: TsMorphMetadataProvider,
  metadataCache: {
    enabled: true, // enabled by default for TsMorphMetadataProvider
    // Cache is stored in `temp` folder by default
    // Add this folder to .gitignore
  },
});
```

For production deployments, you can generate the cache at build time:

```
npx mikro-orm cache:generate
```

This creates a production-ready cache that eliminates the need for ts-morph at runtime.

See [Metadata Cache](https://mikro-orm.io/docs/metadata-cache.md) for more details.

### Comparison of Approaches[​](#comparison-of-approaches "Direct link to Comparison of Approaches")

| Approach                             | Pros                                                 | Cons                                   |
| ------------------------------------ | ---------------------------------------------------- | -------------------------------------- |
| `defineEntity`                       | Full type inference, no decorators, works everywhere | Different syntax than traditional ORMs |
| ES decorators + ts-morph             | Modern standard, DRY definitions                     | Slower startup, requires `.d.ts` files |
| Legacy decorators + ts-morph         | DRY definitions, familiar syntax                     | Slower startup, requires config        |
| Legacy decorators + reflect-metadata | Fast startup, lightweight                            | Verbose, limited type inference        |

## Migration from v6[​](#migration-from-v6 "Direct link to Migration from v6")

In MikroORM v7, decorators were moved to a separate package:

```
- import { Entity, PrimaryKey, Property } from '@mikro-orm/core';
+ import { Entity, PrimaryKey, Property } from '@mikro-orm/decorators/legacy';
```

For ES spec decorators:

```
import { Entity, PrimaryKey, Property } from '@mikro-orm/decorators/es';
```

The `ReflectMetadataProvider` is also moved:

```
- import { ReflectMetadataProvider } from '@mikro-orm/core';
+ import { ReflectMetadataProvider } from '@mikro-orm/decorators/legacy';
```

See [Upgrading from v6 to v7](https://mikro-orm.io/docs/upgrading-v6-to-v7.md) for the complete migration guide.
