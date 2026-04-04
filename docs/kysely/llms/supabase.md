# Source: https://kysely.dev/docs/integrations/supabase.md

# Supabase

Supabase is an open-source Firebase alternative that provides a suite of tools for building applications. At the core, it is a managed PostgreSQL database vendor. They provide a CLI library called `supabase` that's at the heart of their ecosystem. It manages your database, migrates it and can generate TypeScript types from it. They also provide a JavaScript client library called `@supabase/supabase-js` that wraps a PostgREST API, and is pretty limited - doesn't even allow raw SQL. This is where Kysely comes in.

We provide a bridge library called `kysely-supabase` that allows you to translate `supabase`'s generated TypeScript types into types compatible with Kysely.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

1. `supabase` CLI installed and a Supabase project set up.

2. `kysely` installed.

3. A PostgreSQL driver installed - e.g. `pg` or `postgres`. The latter requires `kysely-postgres-js` to be installed as well.

## Installation[​](#installation "Direct link to Installation")

```
npm i -D kysely-supabase
```

## Usage[​](#usage "Direct link to Usage")

### Generate TypeScript types using `supabase` CLI[​](#generate-typescript-types-using-supabase-cli "Direct link to generate-typescript-types-using-supabase-cli")

```
npx supabase gen types typescript --local > path/to/supabase/generated/types/file
```

### Translate Supabase types to Kysely types[​](#translate-supabase-types-to-kysely-types "Direct link to Translate Supabase types to Kysely types")

src/types.ts

```
import type { Database as SupabaseDatabase } from 'path/to/supabase/generated/types/file'
import type { KyselifyDatabase } from 'kysely-supabase'

export type Database = KyselifyDatabase<SupabaseDatabase>
```

### Pass translated types to Kysely constructor[​](#pass-translated-types-to-kysely-constructor "Direct link to Pass translated types to Kysely constructor")

src/db.ts

```
import { Kysely, PostgresDialect } from 'kysely'
import { Pool } from 'pg'
import type { Database } from './types'

export const db = new Kysely<Database>({
  //                         ^^^^^^^^
  dialect: new PostgresDialect({
    pool: new Pool({
      connectionString: process.env.DATABASE_URL,
    }),
  }),
})
```
