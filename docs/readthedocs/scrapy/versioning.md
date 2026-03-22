# Versioning and API stability

## Versioning

There are 3 numbers in a Scrapy version: *A.B.C*

- 

*A* is the major version. This will rarely change and will signify very
large changes.

- 

*B* is the release number. This will include many changes including features
and things that possibly break backward compatibility, although we strive to
keep these cases at a minimum.

- 

*C* is the bugfix release number.

Backward-incompatibilities are explicitly mentioned in the release notes,
and may require special attention before upgrading.

Development releases do not follow 3-numbers version and are generally
released as `dev` suffixed versions, e.g. `1.3dev`.

Note

With Scrapy 0.* series, Scrapy used odd-numbered versions for development releases [https://en.wikipedia.org/wiki/Software_versioning#Odd-numbered_versions_for_development_releases].
This is not the case anymore from Scrapy 1.0 onwards.

Starting with Scrapy 1.0, all releases should be considered production-ready.