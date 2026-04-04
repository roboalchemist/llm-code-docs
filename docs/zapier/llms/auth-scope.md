# Source: https://docs.zapier.com/platform/manage/auth-scope.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.zapier.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Change OAuth scope

> How to add or remove OAuth scopes.

## Impact to users

When an action in a new version of your integration requires additional OAuth scopes, there is no way around asking users to reconnect existing connected accounts before they can use the new action.

You can remove scopes only if no actions need it anymore. Note that existing connected accounts may still have been granted the scopes, and will only lose them when they get reconnected.

## Best practices

Follow these steps to provide the best user experience when adding new scopes.

1. In the new version where you need the additional scopes, try using the action with a existing connected account, and use [error handling](/platform/build/errors) to ensure that the error message instructs users to reconnect the account.

2. In the new version, add the required scopes to the *Scope* field [in the UI](/platform/build/oauth#add-oauth-endpoint-configuration) or `scope` [in the CLI](https://github.com/zapier/zapier-platform/blob/main/packages/schema/docs/build/schema.md#authenticationoauth2configschema).

   <Warning>
     You may need to select the scopes for the OAuth client used by the
     integration as well, in order for us to be able to request them.
   </Warning>

3. Verify that the action now works by connecting an account using the new version.

4. [Promote](/platform/manage/promote) the new version.

5. [Migrate](/platform/manage/migrate) 100% of users to the new version.

<Warning>
  The last two steps are critical to enable users to adopt the new scopes by
  reconnecting existing connected accounts.
</Warning>
