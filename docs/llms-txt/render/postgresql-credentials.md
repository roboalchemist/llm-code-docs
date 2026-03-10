# Source: https://render.com/docs/postgresql-credentials.md

# Database Credentials for Render Postgres — Add database users and perform zero-downtime rotations.

You can add and delete PostgreSQL users from your Render Postgres database. This is most commonly helpful for performing a [credential rotation](#rotating-credentials).

Any users you [create](#adding-a-user) via the Render Dashboard or API are listed in the *Credentials* section of your database's *Info* page:

[image: PostgreSQL users in the Render Dashboard]

Render provides enhanced management of these users, including automatic updates to [Blueprint](infrastructure-as-code)-managed environment variables that [reference the database's connection string](blueprint-spec#referencing-values-from-other-services).

> *Users created directly with the [`CREATE USER`](https://www.postgresql.org/docs/8.0/sql-createuser.html) command are _not_ managed by Render.*
>
> - These users are not displayed in the Render Dashboard or API.
> - These users do not replace your database's [default user](#the-default-user) on creation.

## Managing PostgreSQL users

### The default user

Whenever you [add a PostgreSQL user](#adding-a-user) to your database, that user becomes the database's new "default" user:

- The default user's credentials appear in your database's [connection URLs](postgresql-creating-connecting#connect-to-your-database) shown in the Render Dashboard.
- Default user credentials are also used by environment variables that [reference connection strings](blueprint-spec#referencing-values-from-other-services) in a Render [Blueprint](infrastructure-as-code).
    - Whenever the default user changes, these environment variables update their value on the next Blueprint sync.
- All other existing PostgreSQL users remain valid. However, you can no longer view credentials for the previous default user.

### Adding a user

Add a new Render-managed PostgreSQL user to your database with any of the following methods:

> *Users created directly with the [`CREATE USER`](https://www.postgresql.org/docs/8.0/sql-createuser.html) command are _not_ managed by Render.*
>
> - These users are not displayed in the Render Dashboard or API.
> - These users do not replace your database's [default user](#the-default-user) on creation.

**Dashboard**

#### Dashboard

1. From your database's *Info* page in the [Render Dashboard](https://dashboard.render.com), scroll down to the *Credentials* section:

    [image: Creating a PostgreSQL user in the Render Dashboard]

2. Click *+ New default credential*.

    The creation dialog appears.

3. Optionally provide a username for the new credential. If you don't, Render generates one for you.

4. Click *Create Credential*.

That's it! Your newly created user appears in the table as the new default user for your database.

**API**

#### API

Using the [Render API](api), you can create a new credential with the [Create PostgreSQL User](https://api-docs.render.com/reference/create-postgres-user) endpoint.

Provide a `username` in your request body:

```json
{
  "username": "my_new_user"
}
```

### Viewing users

You can view the active PostgreSQL users for your database. Note that these methods only show users that you added with one of the methods [above](#adding-a-user), not built-in PostgreSQL roles or users created via `CREATE USER`.

**Dashboard**

#### Dashboard

From your database's *Info* page in the [Render Dashboard](https://dashboard.render.com), scroll down to the *Credentials* section. This section displays all active users, with the default user indicated by a label:

[image: Postgres credentials in the Render Dashboard]

**API**

#### API

Using the [Render API](api), you can list all PostgreSQL users with the [List PostgreSQL Users](https://api-docs.render.com/reference/list-postgres-users) endpoint.

Each object in the response array includes `username`, `createdAt`, and `default` properties. The `default` property is `true` for the default user.

### Deleting a user

You can delete PostgreSQL users if they have compromised credentials or are no longer needed.

> *You can't delete your database's current default user.*
>
> To perform a credential rotation involving the default user, first [create a new user](#adding-a-user) to make it the new default. You can then delete the previous default user.

**Dashboard**

#### Dashboard

1. From your database's *Info* page in the [Render Dashboard](https://dashboard.render.com), scroll down to the *Credentials* section:

    [image: Postgres credentials in the Render Dashboard]

2. Click the trashcan icon next to the user you want to delete.

3. Confirm the deletion.

That's it! The user and its credentials are removed immediately.

**API**

#### API

Using the [Render API](api), you can delete a credential with the [Delete PostgreSQL User](https://api-docs.render.com/reference/delete-postgres-user) endpoint.

> *Render never fully deletes your database's _original_ user.*
>
> If you "delete" the original user, Render actually deactivates it by revoking its login privileges. This is a safeguard to preserve database objects owned by the original user.

## Rotating credentials

The following diagram illustrates performing a zero-downtime credential rotation for your database (steps described below):

[diagram]

1. [Add a new PostgreSQL user](#adding-a-user) to your database.
2. Update the configuration of all apps and services that connect to your database to use the new user's credentials.
    - For [Blueprint](infrastructure-as-code)-managed services that [dynamically reference the database's connection string](blueprint-spec#referencing-values-from-other-services), perform a manual Blueprint sync to update the environment variable.
3. Redeploy all of your connected apps and services with the updated credentials.
4. Monitor your database to confirm when no connections are using the original user's credentials.

    You can help confirm this with a query like the following (substitute the original user's name where indicated):

    ```sql
    SELECT COUNT(*) FROM pg_stat_activity WHERE usename = 'ORIGINAL_USER_NAME_HERE';
    ```

5. [Delete the original user.](#deleting-a-user)

## Webhook support

Credential management actions trigger the following [webhook](webhooks) events:

| Event | Description |
| --- | --- |
| `PostgresCredentialsCreated` | Triggers when a PostgreSQL user is created. |
| `PostgresCredentialsDeleted` | Triggers when a PostgreSQL user is deleted. |
