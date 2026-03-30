# Source: https://docs.socket.dev/docs/socket-threat-feed.md

# socket threat-feed

Look up the Socket threat feed

This opens an interactive Socket Threat Feed in your terminal.

You can also generate a `--json` dump for the current request, or format it nicely with `--markdown`.

**Note: Access to this feature requires a special Thread Feed license.**

```
$ socket threat-feed --help

  [beta] View the threat feed

  Usage
    $ socket threat-feed [options] [ECOSYSTEM] [TYPE_FILTER]

  API Token Requirements
    - Quota: 1 unit
    - Permissions: threat-feed:list
    - Special access

  This feature requires a Threat Feed license. Please contact
  sales@socket.dev if you are interested in purchasing this access.

  Options
    --direction       Order asc or desc by the createdAt attribute
    --eco             Only show threats for a particular ecosystem
    --filter          Filter what type of threats to return
    --interactive     Allow for interactive elements, asking for input. Use 
                      --no-interactive to prevent any input questions, defaulting 
                      them to cancel/no.
    --json            Output result as json
    --markdown        Output result as markdown
    --org             Force override the organization slug, overrides the default
                      org from config
    --page            Page token
    --perPage         Number of items per page
    --pkg             Filter by this package name
    --version         Filter by this package version

  Valid ecosystems:

    - gem
    - golang
    - maven
    - npm
    - nuget
    - pypi

  Valid type filters:

    - anom    Anomaly
    - c       Do not filter
    - fp      False Positives
    - joke    Joke / Fake
    - mal     Malware and Possible Malware [default]
    - spy     Telemetry
    - tp      False Positives and Unreviewed
    - typo    Typo-squat
    - u       Unreviewed

  Note: if you filter by package name or version, it will do so for anything
        unless you also filter by that ecosystem and/or package name. When in
        doubt, look at the threat-feed and see the names in the name/version
        column. That's what you want to search for.

  You can put filters as args instead, we'll try to match the strings with the
  correct filter type but since this would not allow you to search for a package
  called "mal", you can also specify the filters through flags.

  First arg that matches a typo, eco, or version enum is used as such. First arg
  that matches none of them becomes the package name filter. Rest is ignored.

  Note: The version filter is a prefix search, pkg name is a substring search.

  Examples
    $ socket threat-feed
    $ socket threat-feed maven --json
    $ socket threat-feed typo
    $ socket threat-feed npm joke 1.0.0 --perPage=5 --page=2 --direction=asc
```