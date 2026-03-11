# Source: https://symfony.com/doc/8.0/components/uid.html

Title: The UID Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/uid.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/components/uid.rst)

> The UID component provides utilities to work with [unique identifiers](https://en.wikipedia.org/wiki/UID) (UIDs) such as UUIDs and ULIDs.

[Installation](https://symfony.com/doc/8.0/components/uid.html#installation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/current/components/using_components.html) for more details.

[UUIDs](https://symfony.com/doc/8.0/components/uid.html#uuids "Permalink to this headline")
-------------------------------------------------------------------------------------------

[UUIDs](https://en.wikipedia.org/wiki/Universally_unique_identifier) (_universally unique identifiers_) are one of the most popular UIDs in the software industry. UUIDs are 128-bit numbers usually represented as five groups of hexadecimal characters: `xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx` (the `M` digit is the UUID version and the `N` digit is the UUID variant).

### [Generating UUIDs](https://symfony.com/doc/8.0/components/uid.html#generating-uuids "Permalink to this headline")

Use the named constructors of the `Uuid` class or any of the specific classes to create each type of UUID:

**UUID v1** (time-based)

Generates the UUID using a timestamp and the MAC address of your device ([read the UUIDv1 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-1)). Both are obtained automatically, so you don't have to pass any constructor argument:

Tip

It's recommended to use UUIDv7 instead of UUIDv1 because it provides better entropy.

**UUID v2** (DCE security)

Similar to UUIDv1 but with a very high likelihood of ID collision ([read the UUIDv2 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-2)). It's part of the authentication mechanism of DCE (Distributed Computing Environment) and the UUID includes the POSIX UIDs (user/group ID) of the user who generated it. This UUID variant is **not implemented** by the Uid component.

**UUID v3** (name-based, MD5)

Generates UUIDs from names that belong, and are unique within, some given namespace ([read the UUIDv3 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-3)). This variant is useful to generate deterministic UUIDs from arbitrary strings. It works by populating the UUID contents with the`md5` hash of concatenating the namespace and the name:

These are the default namespaces defined by the standard:

* `Uuid::NAMESPACE_DNS` if you are generating UUIDs for [DNS entries](https://en.wikipedia.org/wiki/Domain_Name_System)
* `Uuid::NAMESPACE_URL` if you are generating UUIDs for [URLs](https://en.wikipedia.org/wiki/URL)
* `Uuid::NAMESPACE_OID` if you are generating UUIDs for [OIDs (object identifiers)](https://en.wikipedia.org/wiki/Object_identifier)
* `Uuid::NAMESPACE_X500` if you are generating UUIDs for [X500 DNs (distinguished names)](https://en.wikipedia.org/wiki/X.500)

**UUID v4** (random)

Generates a random UUID ([read the UUIDv4 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-4)). Because of its randomness, it ensures uniqueness across distributed systems without the need for a central coordinating entity. It's privacy-friendly because it doesn't contain any information about where and when it was generated:

**UUID v5** (name-based, SHA-1)

It's the same as UUIDv3 (explained above) but it uses `sha1` instead of `md5` to hash the given namespace and name ([read the UUIDv5 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-5)). This makes it more secure and less prone to hash collisions.

**UUID v6** (reordered time-based)

It rearranges the time-based fields of the UUIDv1 to make it lexicographically sortable (like [ULIDs](https://symfony.com/doc/current/components/uid.html#ulid)). It's more efficient for database indexing ([read the UUIDv6 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-6)):

Tip

It's recommended to use UUIDv7 instead of UUIDv6 because it provides better entropy.

**UUID v7** (UNIX timestamp)

Generates time-ordered UUIDs based on a high-resolution Unix Epoch timestamp source (the number of microseconds since midnight 1 Jan 1970 UTC, leap seconds excluded) ([read the UUIDv7 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-7)). It's recommended to use this version over UUIDv1 and UUIDv6 because it provides better entropy (and a more strict chronological order of UUID generation):

**UUID v8** (custom)

Provides an RFC-compatible format intended for experimental or vendor-specific use cases ([read the UUIDv8 spec](https://datatracker.ietf.org/doc/html/draft-ietf-uuidrev-rfc4122bis#name-uuid-version-8)). You must generate the UUID value yourself. The only requirement is to set the variant and version bits of the UUID correctly. The rest of the UUID content is implementation-specific, and no particular format should be assumed:

If your UUID value is already generated in another format, use any of the following methods to create a `Uuid` object from it:

You can also use the `UuidFactory` to generate UUIDs. Inject the factory in your services and use it as follows:

By default, this factory generates the folllowing UUIDs:

* Default and time-based UUIDs: UUIDv7
* Name-based UUIDs: UUIDv5
* Random-based UUIDs: UUIDv4
* Time-based node and UUID namespace: `null`

You can configure these default values:

### [Converting UUIDs](https://symfony.com/doc/8.0/components/uid.html#converting-uuids "Permalink to this headline")

Use these methods to transform the UUID object into different bases:

You can also convert some UUID versions to others:

### [Working with UUIDs](https://symfony.com/doc/8.0/components/uid.html#working-with-uuids "Permalink to this headline")

UUID objects created with the `Uuid` class can use the following methods (which are equivalent to the `uuid_*()` method of the PHP extension):

If you're working with different UUIDs format and want to validate them, you can use the `$format` parameter of the [isValid()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Uuid.php#:~:text=function%20isValid "Symfony\Component\Uid\Uuid::isValid()") method to specify the UUID format you're expecting:

The following constants are available:

* `Uuid::FORMAT_BINARY`
* `Uuid::FORMAT_BASE_32`
* `Uuid::FORMAT_BASE_58`
* `Uuid::FORMAT_RFC_4122`
* `Uuid::FORMAT_RFC_9562` (equivalent to `Uuid::FORMAT_RFC_4122`)

You can also use the `Uuid::FORMAT_ALL` constant to accept any UUID format. By default, only the RFC 4122 format is accepted.

### [Storing UUIDs in Databases](https://symfony.com/doc/8.0/components/uid.html#storing-uuids-in-databases "Permalink to this headline")

If you [use Doctrine](https://symfony.com/doc/current/doctrine.html), consider using the `uuid` Doctrine type, which converts to/from UUID objects automatically:

There's also a Doctrine generator to help auto-generate UUID values for the entity primary keys:

Using `UuidGenerator::class` to generate UUID values creates a new generator instance and bypasses Symfony's `doctrine.uuid_generator` service. This means the UUID version configured in FrameworkBundle (for example, UUIDv6 or UUIDv7) is ignored.

Instead, configure the Doctrine entity to use Symfony's generator service:

Warning

Using UUIDs as primary keys is usually not recommended for performance reasons: indexes are slower and take more space (because UUIDs in binary format take 128 bits instead of 32/64 bits for auto-incremental integers) and the non-sequential nature of UUIDs fragments indexes. [UUID v6](https://symfony.com/doc/current/components/uid.html#uid-uuid-v6) and [UUID v7](https://symfony.com/doc/current/components/uid.html#uid-uuid-v7) are the only variants that solve the fragmentation issue (but the index size issue remains).

When using built-in Doctrine repository methods (e.g. `findOneBy()`), Doctrine knows how to convert these UUID types to build the SQL query (e.g. `->findOneBy(['user' => $user->getUuid()])`). However, when using DQL queries or building the query yourself, you'll need to set `uuid` as the type of the UUID parameters:

### [Testing UUIDs](https://symfony.com/doc/8.0/components/uid.html#testing-uuids "Permalink to this headline")

Many UUID versions include random or time-dependent parts, which makes them hard to use in tests. The [MockUuidFactory](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Factory/MockUuidFactory.php "Symfony\Component\Uid\Factory\MockUuidFactory") class allows you to control the UUIDs generated during your tests, making them predictable and reproducible.

First, make sure that your service generates UUID values using the [UuidFactory](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Uid/Factory/UuidFactory.php "Symfony\Component\Uid\Factory\UuidFactory"):

Then, in your tests, you can use `MockUuidFactory` to define a sequence of the UUIDs that will be returned each time you generate one:

In addition to the `create()` method, the `MockUuidFactory` also works for the `randomBased()`, `timeBased()`, and `nameBased()` methods. You can even mix different UUID versions in the same sequence.

Note

`MockUuidFactory` throws an exception if the sequence is exhausted or the available UUID types don't match the requested type.

[ULIDs](https://symfony.com/doc/8.0/components/uid.html#ulids "Permalink to this headline")
-------------------------------------------------------------------------------------------

[ULIDs](https://github.com/ulid/spec) (_Universally Unique Lexicographically Sortable Identifier_) are 128-bit numbers usually represented as a 26-character string: `TTTTTTTTTTRRRRRRRRRRRRRRRR` (where `T` represents a timestamp and `R` represents the random bits).

ULIDs are an alternative to UUIDs when using those is impractical. They provide 128-bit compatibility with UUID, they are lexicographically sortable and they are encoded as 26-character strings (vs 36-character UUIDs).

Note

If you generate more than one ULID during the same millisecond in the same process then the random portion is incremented by one bit in order to provide monotonicity for sorting. The random portion is not random compared to the previous ULID in this case.

### [Generating ULIDs](https://symfony.com/doc/8.0/components/uid.html#generating-ulids "Permalink to this headline")

Instantiate the `Ulid` class to generate a random ULID value:

If your ULID value is already generated in another format, use any of the following methods to create a `Ulid` object from it:

Like UUIDs, ULIDs have their own factory, `UlidFactory`, that can be used to generate them:

There's also a special `NilUlid` class to represent ULID `null` values:

### [Converting ULIDs](https://symfony.com/doc/8.0/components/uid.html#converting-ulids "Permalink to this headline")

Use these methods to transform the ULID object into different bases:

### [Working with ULIDs](https://symfony.com/doc/8.0/components/uid.html#working-with-ulids "Permalink to this headline")

ULID objects created with the `Ulid` class can use the following methods:

### [Storing ULIDs in Databases](https://symfony.com/doc/8.0/components/uid.html#storing-ulids-in-databases "Permalink to this headline")

If you [use Doctrine](https://symfony.com/doc/current/doctrine.html), consider using the `ulid` Doctrine type, which converts to/from ULID objects automatically:

There's also a Doctrine generator to help auto-generate ULID values for the entity primary keys:

Warning

Using ULIDs as primary keys is usually not recommended for performance reasons. Although ULIDs don't suffer from index fragmentation issues (because the values are sequential), their indexes are slower and take more space (because ULIDs in binary format take 128 bits instead of 32/64 bits for auto-incremental integers).

When using built-in Doctrine repository methods (e.g. `findOneBy()`), Doctrine knows how to convert these ULID types to build the SQL query (e.g. `->findOneBy(['user' => $user->getUlid()])`). However, when using DQL queries or building the query yourself, you'll need to set `ulid` as the type of the ULID parameters:

[Generating and Inspecting UUIDs/ULIDs in the Console](https://symfony.com/doc/8.0/components/uid.html#generating-and-inspecting-uuids-ulids-in-the-console "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This component provides several commands to generate and inspect UUIDs/ULIDs in the console. They are not enabled by default, so you must add the following configuration in your application before using these commands:

Now you can generate UUIDs/ULIDs as follows (add the `--help` option to the commands to learn about all their options):

In addition to generating new UIDs, you can also inspect them with the following commands to show all the information for a given UID:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
