# Source: https://docs.readthedocs.com/platform/latest/server-side-search/syntax.html

# Search query syntax[](#search-query-syntax "Link to this heading")

When searching on Read the Docs with [[server side search]](index.html), you can use some parameters in your query in order to search on given projects, versions, or to get more accurate results.

## Parameters[](#parameters "Link to this heading")

Parameters are in the form of [`name:value`], they can appear anywhere in the query, and depending on the parameter, you can use one or more of them.

Any other text that isn't a parameter will be part of the search query. If you don't want your search term to be interpreted as a parameter, you can escape it like [`project\:docs`].

Note

Unknown parameters like [`foo:bar`] don't require escaping.

The available parameters are:

project

:   Indicates the project and version to include results from (this doesn't include subprojects or translations). If the version isn't provided, the default version will be used. More than one parameter can be included.

    Examples:

    -   [`project:docs`]` `[`test`]

    -   [`project:docs/latest`]` `[`test`]

    -   [`project:docs/stable`]` `[`project:dev`]` `[`test`]

subprojects

:   Include results from the given project and its subprojects. If the version isn't provided, the default version of all projects will be used. If a version is provided, all subprojects matching that version will be included, and if they don't have a version with that name, we use their default version. More than one parameter can be included.

    Examples:

    -   [`subprojects:docs`]` `[`test`]

    -   [`subprojects:docs/latest`]` `[`test`]

    -   [`subprojects:docs/stable`]` `[`subprojects:dev`]` `[`test`]

user

:   Include results from projects the given user has access to. The only supported value is [`@me`], which is an alias for the current user. Only one parameter can be included. If duplicated, the last one will override the previous one.

    Examples:

    -   [`user:@me`]` `[`test`]

### Permissions[](#permissions "Link to this heading")

If the user doesn't have permission over one version, or if the version doesn't exist, we don't include results from that version.

The API will return all the projects that were used in the final search, with that information you can check which projects were used in the search.