# Source: https://docs.redwoodjs.com/docs/data-migrations

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Data Migrations]

[Version: 8.8]

On this page

<div>

# Data Migrations

</div>

> Data Migrations are available as of RedwoodJS v0.15

There are two kinds of changes you can make to your database:

-   Changes to structure
-   Changes to content

In Redwood, [Prisma Migrate](https://www.prisma.io/docs/reference/tools-and-interfaces/prisma-migrate) takes care of codifying changes to your database *structure* in code by creating a snapshot of changes to your database that can be reliably repeated to end up in some known state.

To track changes to your database *content*, Redwood includes a feature we call **Data Migration**. As your app evolves and you move data around, you need a way to consistently declare how that data should move.

Imagine a `User` model that contains several columns for user preferences. Over time, you may end up with more and more preferences to the point that you have more preference-related columns in the table than you do data unique to the user! This is a common occurrence as applications grow. You decide that the app should have a new model, `Preference`, to keep track of them all (and `Preference` will have a foreign key `userId` to reference it back to its `User`). You\'ll use Prisma Migrate to create the new `Preference` model, but how do you copy the preference data to the new table? Data migrations to the rescue!

## Installing[​](#installing "Direct link to Installing") 

Just like Prisma, we will store which data migrations have run in the database itself. We\'ll create a new database table `DataMigration` to keep track of which ones have run already.

Rather than create this model by hand, Redwood includes a CLI tool to add the model to `schema.prisma` and create the DB migration that adds the table to the database:

``` 
yarn rw data-migrate install
```

You\'ll see a new directory created at `api/db/dataMigrations` which will store our individual migration tasks.

Take a look at `schema.prisma` to see the new model definition:

api/db/schema.prisma

``` 
model RW_DataMigration 
```

The install script also ran `yarn rw prisma migrate dev --create-only` automatically so you have a DB migration ready to go. You just need to run the `prisma migrate dev` command to apply it:

``` 
yarn rw prisma migrate dev
```

## Creating a New Data Migration[​](#creating-a-new-data-migration "Direct link to Creating a New Data Migration") 

Data migrations are just plain Typescript or Javascript files which export a single anonymous function that is given a single argument---an instance of `PrismaClient` called `db` that you can use to access your database. The files have a simple naming convention:

``` 
-.js
```

Where `version` is a timestamp, like `20200721123456` (an ISO8601 datetime without any special characters or zone identifier), and `name` is a param-case human readable name for the migration, like `copy-preferences`.

To create a data migration we have a generator:

``` 
yarn rw generate dataMigration copyPreferences
```

This will create `api/db/dataMigrations/20200721123456-copy-preferences.js`:

api/db/dataMigrations/20200721123456-copy-preferences.js

``` 
export default async () => 
```

> **Why such a long name?**
>
> So that if multiple developers are creating data migrations, the chances of them creating one with the exact same filename is essentially zero, and they will all run in a predictable order---oldest to newest.

Now it\'s up to you to define your data migration. In our user/preference example, it may look something like:

api/db/dataMigrations/20200721123456-copy-preferences.js

``` 
const asyncForEach = async (array, callback) => 
}

export default async () =>  },
      },
    })
  })
}
```

This loops through each existing `User` and creates a new `Preference` record containing each of the preference-related fields from `User`.

> Note that in a case like this where you\'re copying data to a new table, you would probably delete the columns from `User` afterwards. This needs to be a two step process!
>
> 1.  Create the new table (db migration) and then move the data over (data migration)
> 2.  Remove the unneeded columns from `User`
>
> When going to production, you would need to run this as two separate deploys to ensure no data is lost.
>
> The reason is that all DB migrations are run and *then* all data migrations. So if you had two DB migrations (one to create `Preference` and one to drop the unneeded columns from `User`) they would both run before the Data Migration, so the columns containing the preferences are gone before the data migration gets a chance to copy them over!
>
> **Remember**: Any destructive action on the database (removing a table or column especially) needs to be a two step process to avoid data loss.

## Running a Data Migration[​](#running-a-data-migration "Direct link to Running a Data Migration") 

When you\'re ready, you can execute your data migration with `data-migrate`\'s `up` command:

``` 
yarn rw data-migrate up
```

This goes through each file in `api/db/dataMigrations`, compares it against the list of migrations that have already run according to the `DataMigration` table in the database, and executes any that aren\'t present in that table, sorted oldest to newest based on the timestamp in the filename.

Any logging statements (like `console.info()`) you include in your data migration script will be output to the console as the script is running.

If the script encounters an error, the process will abort, skipping any following data migrations.

> The example data migration above didn\'t include this for brevity, but you should always run your data migration [inside a transaction](https://www.prisma.io/docs/reference/tools-and-interfaces/prisma-client/transactions#bulk-operations-experimental) so that if any errors occur during execution the database will not be left in an inconsistent state where only *some* of your changes were performed.

## Long-term Maintainability[​](#long-term-maintainability "Direct link to Long-term Maintainability") 

Ideally you can run all database migrations and data migrations from scratch (like when a new developer joins the team) and have them execute correctly. Unfortunately you don\'t get that ideal scenario by default.

Take our example above---what happens when a new developer comes long and attempts to setup their database? All DB migrations will run first (including the one that drops the preference-related columns from `User`) before the data migrations run. They will get an error when they try to read something like `user.newsletter` and that column doesn\'t exist!

One technique to combat this is to check for the existence of these columns before the data migration does anything. If `user.newsletter` doesn\'t exist, then don\'t bother running the data migration at all and assume that your [seed data](/docs/cli-commands#prisma-db-seed) is already in the correct format:

``` 
export default async () =>  },
        },
      })
    })
  }
}
```

## Lifecycle Summary[​](#lifecycle-summary "Direct link to Lifecycle Summary") 

Run once:

``` 
yarn rw data-migrate install
yarn rw prisma migrate dev
```

Run every time you need a new data migration:

``` 
yarn rw generate dataMigration migrationName
yarn rw data-migrate up
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/data-migrations.md)