# Source: https://phpunit.de/backward-compatibility.html

Title: Backward Compatibility of PHPUnit

URL Source: https://phpunit.de/backward-compatibility.html

Markdown Content:
Semantic Versioning
-------------------

PHPUnit follows [Semantic Versioning](https://semver.org/). Information about the currently supported versions is available [here](https://phpunit.de/supported-versions.html).

A new **major version** is released each year on the first Friday of February. Major versions make incompatible API changes and remove or hard-deprecate (see below) features.

A new **minor version** is released on the first Friday of April, June, August, October, and December. Minor versions add functionality in a backward compatible manner. Minor versions may soft-deprecate (see below) features.

**Patch versions** are released as needed to address issues in a backward compatible manner.

### Exceptions

The backward compatibility promise for PHPUnit has the following exceptions:

#### Internal Code

PHPUnit's units of code that are annotated with `@internal` are not covered by the backward compatibility promise for PHPUnit.

These units of code are internal to PHPUnit and are subject to change or removal even in minor or patch versions. They must not be used in third-party code: not in test code and not in extensions for PHPUnit or in wrappers around PHPUnit.

#### Named Arguments

PHPUnit's units of code that are not annotated with `@internal` are annotated with `@no-named-arguments` instead. This documents the fact that parameter names are not covered by the backward compatibility promise for PHPUnit.

#### Event System: Value Objects

For value objects that are passed from PHPUnit's event system to subscribers, only the public methods for querying information are covered by the backward compatibility promise for PHPUnit. For instance, the constructor methods of these objects are not covered.

Since there is no point in extending these classes outside of PHPUnit's own code, making an `abstract` class of such a value object `abstract readonly`, for example, is not considered to be a break of backward compatibility.

Feature Sunsetting
------------------

The sunsetting of features follows the following steps:

### Soft Deprecation

If the feature is used through a unit of code, for instance by calling a method, then the `@deprecated` annotation is added to that unit of code. IDEs and static analysis tools can now report that deprecated functionality is used.

Tests that use a soft-deprecated assertion method, for example, will continue to work in exactly the same way.

### Hard Deprecation

The feature is hard-deprecated in the next major version after it was soft-deprecated.

Tests that use a hard-deprecated assertion method, for example, will continue to work in exactly the same way. The only difference is that PHPUnit now reports that a hard-deprecated feature is used.

### Removal

The feature is removed in the next major version after it was hard-deprecated.

Tests that use an assertion method that was removed, for example, will no longer work.

Deprecations
------------

The following pages list the features that are deprecated in each version of PHPUnit:

*   [PHPUnit 9.6](https://github.com/sebastianbergmann/phpunit/blob/9.6/DEPRECATIONS.md)
*   [PHPUnit 10.5](https://github.com/sebastianbergmann/phpunit/blob/10.5/DEPRECATIONS.md)
*   [PHPUnit 11.5](https://github.com/sebastianbergmann/phpunit/blob/11.5/DEPRECATIONS.md)
*   [PHPUnit 12.5](https://github.com/sebastianbergmann/phpunit/blob/12.5/DEPRECATIONS.md)
*   [PHPUnit 13.0](https://github.com/sebastianbergmann/phpunit/blob/13.0/DEPRECATIONS.md)

Version Control
---------------

### Tags

[Tags](https://github.com/sebastianbergmann/phpunit/tags) in PHPUnit's [Git](https://github.com/sebastianbergmann/phpunit/) repository are immutable. We do not change published tags to point to a different revision, for example.

In very rare cases we may delete a tag in order to unpublish a broken release. The new release that fixes what was broken will always have a different tag than the one that was unpublished.

### Branches

[Branches](https://github.com/sebastianbergmann/phpunit/branches) in PHPUnit's [Git](https://github.com/sebastianbergmann/phpunit/) repository are private implementation details. For example, we delete branches for versions of PHPUnit that are no longer supported.
