# Source: https://docs.socket.dev/docs/socket-organizations.md

# socket organization

List organizations associated with the API key used

At the time of writing this should show you the one organization that's associated with the current API token. *(This may change in the future)*

## socket organization --help

```
$ socket organization --help

  Account details

  Usage
    $ socket organization <command>

  Commands
    dependencies      Search for any dependency that is being used in your organization
    list              List organizations associated with the API key used
    policy            Organization policy details

  Options
    (none)

  Examples
    $ socket organization --help
```

## socket organization list

This fetches your organization "slug", ID, and plan.

```
$ socket organization list

✔ Received organization list response.
List of organizations associated with your API key, ending with: abcde

- Name: BearDev, ID: 123, Plan: enterprise
```

## socket organization dependencies

You can use this to find out which dependencies are used in your org and which repository or repositories and which branch may have used them. This is useful in case a bad package was published and you need to quickly figure out where to scrub them from your organization.

```
$ socket organization dependencies --help

  Search for any dependency that is being used in your organization

  Usage
    socket organization dependencies [options]

  API Token Requirements
    - Quota: 1 unit
    - Permissions: none (does need token with access to target org)

  Options
    --json            Output result as json
    --limit           Maximum number of dependencies returned
    --markdown        Output result as markdown
    --offset          Page number

  Examples
    socket organization dependencies
    socket organization dependencies --limit 20 --offset 10
```

## socket organization policy security

You can pull in the currently configured security policy for your organization.

## socket organization policy license

You can pull in the currently configured license policy for your organization.