# Source: https://docs.redwoodjs.com/docs/database-seeds

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Database Seeds]

[Version: 8.8]

On this page

<div>

# Database Seeds

</div>

Seeds are data that are required in order for your app to function. Think of the data a new developer would need to get up and running with your codebase, or data that needs to exist when a new instance of your application is deployed to a new environment.

Seed data are things like:

-   An admin user so that you can log in to your new instance
-   A list of categories that can be assigned to a Product
-   Lists of roles and permissions

Seed data is not meant for:

-   Sample data to be used in development
-   Data to run tests against
-   Randomized data

## Best Practices[​](#best-practices "Direct link to Best Practices") 

Ideally seed data should be idempotent: you can execute the seed script against your database at any time and end up with the seed data properly populated in the database. It should not result in wiping out existing records or creating duplicates of any seeded data that is already present.

Making your seeds idempotent requires more code than just a straight `createMany()`. The code examples below use the safest idempotent strategy by having an `upsert` check if a record with the same unique identifier already exists, and if so just update it, if not then create it. But, this technique requires a separate SQL statement for each member of your data array and is less performant than `createMany()`.

You could also do a check if *any* data exists in the database first, and if not, create the records with `createMany()`. However, this means that any existing seed data that may have been modified will remain, and would not be updated to match what you expect in your seed.

When in doubt, `upsert`!

## When seeds run[​](#when-seeds-run "Direct link to When seeds run") 

Seeds are automatically run the first time you migrate your database:

``` 
yarn rw prisma migrate dev
```

They are run *every* time you reset your database:

``` 
yarn rw prisma migrate reset
```

You can manually run seeds at any time with the following command:

``` 
yarn rw prisma db seed
```

You generally don\'t need to keep invoking your seeds over and over again, so it makes sense that Prisma only does it on a complete database reset, or when the database is created with the first `prisma migrate dev` execution. But as your schema evolves you may add a new model that requires some seeded data and so you can add it to your seed file and then manually run it to create those records.

### Performance[​](#performance "Direct link to Performance") 

Prisma is faster at execting a `createMany()` instead of many `create` or `upsert` functions. Unfortunately, you lose the ability to easily make your seed idempotent with a single function call.

One solution to simulate an `upsert` will still using `createMany()` could be to start with the full array of data and first check to see whether each of those records already exist in the database. If they do, create two arrays: one for records that don\'t exist and run `createMany()` with them, and the second list for records that do exist, and run `updateMany()` on those.

Unfortunately this relies on a select query for each record, which may negate the performance benefits of `createMany()`. Since you are running seeds realitively rarely, it\'s our recommendation that you focus less on absolute performance and worry more about making them easy to maintain.

## Types[​](#types "Direct link to Types") 

If you\'re using Typescript you\'ll probably want to type your seeds as well. Getting the right types for Prisma models can be tricky, but here\'s the formula:

scripts/seed.ts

``` 
import  from 'api/src/lib/db'
import type  from '@prisma/client'

export default async () => ,
      ,
    ]

    await db.user.createMany()
  } catch (error) 
}
```

## Creating seed data[​](#creating-seed-data "Direct link to Creating seed data") 

Take a look at `scripts/seed.js` (or `.ts` if you\'re working on a Typescript project):

scripts/seed.js

``` 
import  from 'api/src/lib/db'

export default async () => ,
    //   ,
    // ]
    //
    // await db.user.createMany()

    console.info(
      '\n  No seed data, skipping. See scripts/seed.ts to start seeding your database!\n'
    )
  } catch (error) 
}
```

Let\'s create some categories for a bookstore. For this example, assume the `Category` model has a unique constraint on the `name` field. Remove the commented example and add your code:

scripts/seed.js

``` 
export default async () => ,
      ,
      ,
      ,
      ,
      ,
    ]

    for (const item of data) ,
        update: ,
        create: ,
      })
    }
  } catch (error) 
}
```

You can now execute this seed as many times as you want and you\'ll end up with that exact list in the database each time. And, any additional categories you\'ve created in the meantime will remain. Remember: seeds are meant to be the *minimum* amount of data you need for your app to run, not necessarily *all* the data that will ever be present in those tables.

# Seeding users for dbAuth

If using dbAuth and seeding users, you\'ll need to add a `hashedPassword` and `salt` using the same algorithm that dbAuth uses internally. Here\'s an easy way do that:

scripts/seed.js

``` 
import  from '@redwoodjs/auth-dbauth-api'

export default async () => ,
    ,
  ]

  for (const user of users) ,
      create: ,
      update: ,
    })
  }
}
```

## What if I don\'t need seeds?[​](#what-if-i-dont-need-seeds "Direct link to What if I don't need seeds?") 

In order to stop automatically executing seeds with the `prisma migrate` commands you can remove the following lines from `package.json` in the root of your app:

``` 
"prisma": ,
```

You can then delete the `scripts/seed.js` file.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/database-seeds.md)