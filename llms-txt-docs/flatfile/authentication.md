# Source: https://flatfile.com/docs/guides/authentication.md

# Authentication and Authorization

> Complete guide to authenticating with Flatfile using API keys, Personal Access Tokens, and managing roles and permissions

This guide covers all aspects of authentication with Flatfile, including API keys, Personal Access Tokens, and role-based access control for your team and customers.

## API Keys

Flatfile provides two different kinds of environment-specific API keys you can use to interact with the API. In addition, you can work with a development key or a production environment.

<Info>
  API keys are created automatically. Use the [API Keys and Secrets](https://platform.flatfile.com/dashboard/keys-and-secrets) page to see your API keys for
  any given Environment.
</Info>

### Testing and Development

[Environments](/core-concepts/environments) are isolated entities and are intended to be a safe place to create and test different configurations. A `development` and `production` environment are created by default.

| isProd  | Name          | Description                                                                                 |
| ------- | ------------- | ------------------------------------------------------------------------------------------- |
| *false* | `development` | Use this default environment, and its associated test API keys, as you build with Flatfile. |
| *true*  | `production`  | When you're ready to launch, create a new environment and swap out your keys.               |

<Note>
  The development environment does not count towards your paid credits.
</Note>

### Secret and Publishable Keys

All Accounts have two key types for each environment. Learn when to use each type of key:

| Type            | Id                     | Description                                                                                                             |
| --------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Secret key      | `sk_23ghsyuyshs7dcrty` | **On the server-side:** Store this securely in your server-side code. Don't expose this key in an application.          |
| Publishable key | `pk_23ghsyuyshs7dcert` | **On the client-side:** Can be publicly-accessible in your application's client-side code. Use when embedding Flatfile. |

<Note>
  The `accessToken` provided from `publishableKey` will remain valid for a
  duration of 24 hours.
</Note>

## Personal Access Tokens

Personal Access Tokens (PATs) provide a secure way to authenticate with the Flatfile API. Unlike environment-specific API keys, PATs are user-scoped tokens that inherit the permissions of the user who created them.

Personal Access Tokens:

* Are user-scoped authentication tokens
* Have the same auth scope as the user who created them
* Can be used in place of a JWT for API authentication
* Are ideal for scripts, automation, and integrations that need to act on behalf of a user

This opens up possibilities for various use cases, including building audit logs, managing Spaces, and monitoring agents across environments.

### Creating a Token

1. Log in to your Flatfile account
2. Click on your user profile dropdown in the top-right corner
3. Select "Personal Access Tokens"
4. Click "Create Token"
5. Enter a descriptive name for your token
6. Copy the generated token immediately - it will only be shown once

<Note>
  Make sure to copy your token when it's first created. For security reasons,
  you won't be able to view the token again after leaving the page.
</Note>

### Exchanging Credentials for an Access Token

You can exchange your email and password credentials for an access token using the auth endpoint. See the [Authentication Examples](/guides/deeper/auth-examples#creating-a-pat-via-api) for the complete API call.

The response will include an access token that you can use for API authentication.

### Retrieving a Personal Access Token (Legacy Method)

Your `publishableKey` and `secretKey` are specific to an environment. Therefore, to interact at a higher level, you can use a personal access token.

1. From the dashboard, open **Settings**

2. Click to **Personal Tokens**

3. Retrieve your `clientId` and `secret`.

4. Using the key pair, call the auth endpoint. See the [Authentication Examples](/guides/deeper/auth-examples#legacy-client-credentials-flow) for the complete API call.

5. The response will include an `accessToken`. Present that as your **Bearer `token`** in place of the `secretKey`.

### Using a Token

Use your Personal Access Token in API requests by including it in the Authorization header as documented in the [API Reference](https://reference.flatfile.com).

### Managing Tokens

You can view all your active tokens in the Personal Access Tokens page. For each token, you can see:

* Name
* Creation date
* Last used date (if applicable)

To delete a token:

1. Navigate to the Personal Access Tokens page
2. Find the token you want to delete
3. Click the menu icon (three dots) next to the token
4. Select "Delete"
5. Confirm the deletion

<Warning>
  Deleting a token immediately revokes access for any applications or scripts
  using it. Make sure you update any dependent systems before deleting a token.
</Warning>

### Best Practices

* Create separate tokens for different applications or use cases
* Use descriptive names that identify where the token will be used
* Regularly review and delete unused tokens
* Rotate tokens periodically for enhanced security
* Never share your tokens with others - each user should create their own tokens

### Example Use Cases

#### Building an Audit Log

Query for all events across all environments and combine them with user and guest data to create a comprehensive audit log, providing a detailed history of actions within the application.

#### Managing Spaces Across Environments

Determine the number of Spaces available and identify which Spaces exist in different environments, allowing you to efficiently manage and organize your data.

#### Monitoring Agents Across Environments

Keep track of agents deployed to various environments by retrieving information about their presence, ensuring smooth and efficient data import processes.

## Roles & Permissions

Grant your team and customers access with role-based permissions.

### Administrator Roles

Administrator roles have full access to your accounts, including inviting additional admins and seeing developer keys.

<Note>
  The `accessToken` provided will remain valid for a duration of 24 hours.
</Note>

| Role          | Details                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator | This role is meant for any member of your team who requires full access to the Account.<br /> <br />✓ Can add other administrators <br />✓ Can view secret keys <br />✓ Can view logs |

### Guest Roles

Guest roles receive access via a magic link or a shared link depending on the [Environment](https://platform.flatfile.com/dashboard) `guestAuthentication` type. Guests roles can invite other Guests unless you turn off this setting in the [Guest Sidebar](/guides/customize-guest-sidebar).

<Note>
  The `accessToken` provided will remain valid for a duration of 1 hour.
</Note>

Data Clips can provide granular guest access to a specific [sheet](/core-concepts/sheets) by sharing only selected records from that sheet within a [workbook](/core-concepts/workbooks). However, if the clipped sheet includes [reference fields](/core-concepts/fields#reference) that point to other sheets in the same workbook, guests will also receive read access to those referenced records to support lookups and validation. Learn more in the [Data Clips guide](/legacy-docs/advanced-guides/dataclips).

#### Space Grant

| Role               | Details                                                                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single-Space Guest | This role is meant for a guest who has access to only one Space. Such guests can be invited to additional Spaces at any time.                                  |
| Multi-Space Guest  | This role is meant for a guest who has access to multiple Spaces. They will see a drop-down next to the Space name that enables them to switch between Spaces. |

#### Workbook Grant

| Role                  | Details                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Single-Workbook Guest | This role is meant for a guest who should have access to only one Workbook within a Space. |
| Multi-Workbook Guest  | This role is intended for a guest who has access to multiple Workbooks within a Space.     |

<Info>This role can only be configured using code. See code example.</Info>

```js
const createGuest = await api.guests.create({
  environmentId: "us_env_hVXkXs0b",
  email: "guest@example.com",
  name: "Mr. Guest",
  spaces: [
    {
      id: "us_sp_DrdXetPN",
      workbooks: [
        {
          id: "us_wb_qGZbKwDW",
        },
      ],
    },
  ],
});
```

#### Guest Lifecycle

When a guest user is deleted, all their space connections are automatically removed to ensure security. This means:

* The guest loses access to all previously connected spaces
* They cannot regain access to these spaces without being explicitly re-invited

This automatic cleanup ensures that deleted guests cannot retain any access to spaces, even if they are later recreated with the same email address.

## API Reference

For detailed API documentation on authentication endpoints, see the [Authentication API Reference](https://reference.flatfile.com/api-reference/auth).

For programmatic management of Personal Access Tokens, see the [Personal Access Tokens API Reference](https://reference.flatfile.com/api-reference/auth/personal-access-tokens).
