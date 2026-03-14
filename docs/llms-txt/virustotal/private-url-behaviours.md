# Source: https://virustotal.readme.io/reference/private-url-behaviours.md

# 🔒 Private URLs Behaviours

Information about private URL behaviours

> 🚧 Special privileges required
>
> Private Scanning endpoints are only available to users with [Private Scanning license](https://www.virustotal.com/gui/private-scanning-overview).

Private URL behaviours are identical to [URL behaviours](https://virustotal.readme.io/reference/url-behaviour-summary), but they summarize the behaviour of a [private URL](https://virustotal.readme.io/reference/private-urls). They can be only seen by the users who uploaded the original URL.

## Additional attributes

* `expiration`: <*integer*> the date when the report will no longer be available.

## Relationships

Additionally, private URL behaviour objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section.

The following table shows a summary of available relationships.

| Relationship | Return object type                               |
| :----------- | :----------------------------------------------- |
| analyses     | List of [Private Analyses](https://virustotal.readme.io/reference/private-analyses) |