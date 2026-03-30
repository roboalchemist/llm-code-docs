# Source: https://firebase.google.com/docs/reference/security/storage.md.txt

# Firebase Security Rules for Cloud Storage Reference

Firebase Security Rules for Cloud Storage are used to determine who has read and write access
to files stored in Cloud Storage, as well as how files are structured
and what metadata they contain. Cloud Storage Security Rules are composed of rules that
consider the `request` and `resource` to allow or deny a desired action, such
as uploading a file or retrieving file metadata. These reference docs cover
the types of rules, the properties of a `request` and a `resource`, the data
types used by Cloud Storage Security Rules, and how errors occur.

## Rule

A `rule` is an expression that is evaluated to determine if a `request` is
allowed to perform a desired action.

### Types

#### Allow

`allow` rules consist of a method, such as `read` or `write`, as well as
an optional condition. When a rule is executed, the condition is evaluated, and
if the condition evaluates to `true`, the desired method is allowed; otherwise,
the method is denied. An `allow` rule with no condition always allows the
desired method.

```
// Always allow method
allow <method>;

// Allow method if condition is true
allow <method>: if <condition>;
```

Currently, `allow` is the only supported type of rule.

### Request Methods

#### Read

The `read` method covers all requests where file data or metadata is read,
including file downloads and file metadata reads.

```
// Always allow reads
allow read;

// Allow reads if condition evaluates to true
allow read: if <condition>;
```

#### Write

The `write` method covers all requests where file data or metadata is written,
including file uploads, file deletes, and file metadata updates.

```
// Always allow writes
allow write;

// Allow writes if condition evaluates to true
allow write: if <condition>;
```

## Match

Rules are executed when a user `request` (such as a file upload or download)
matches a file path covered by a rule. A `match` consists of a path and a body,
which must contain at least one `allow` rule. If no path is matched, the request
is rejected.

You can `match` a fully named path, or you can insert wildcards to match all
paths that fit a certain pattern.

### Path Segments

#### `single_segment`

You can use single path segments to create a rule that matches a file stored
in Cloud Storage.

```
// Allow read at "path" if condition evaluates to true
match /path {
  allow read: if <condition>;
}
```

Multiple path segments and nested paths are also allowed:

```
// Allow read at "path/to/object" if condition evaluates to true
match /path {
  match /to {
    match /object {
      allow read: if <condition>;
    }
  }
}
```

#### `{single_segment_wildcard}`

If you want to apply a rule to multiple files at the same path, you can use a
wildcard path segment to match all files at a certain path. A wildcard variable
is declared in a path by wrapping a variable in curly braces: `{variable}`.
This variable is accessible within the match statement as a `string`.

```
// Allow read at any path "/*", if condition evaluates to true
match /{single_path} {
  // Matches "path", "to", or "object" but not "path/to/object"
  allow read: if <condition>;
}
```

Multiple path segments and nested paths may also have wildcards:

```
// Allow read at any path "/path/*/newPath/*", if condition evaluates to true
match /path/{first_wildcard} {
  match /newPath/{second_wildcard} {
    // Matches "path/to/newPath/newObject" or "path/from/newPath/oldObject"
    allow read: if <condition>;
  }
}
```

#### `{multi_segment_wildcard=**}`

If you want to match any number of path segments at or below a path, you can use
a multi segment wildcard, which will match all requests to and below the
location. This can be useful for providing a user their own free form
storage space, or creating rules that match many different path segments (such
as creating a publicly readable set of files, or requiring authentication for
all writes).

A multi segment wildcard path is declared similarly to a single segment
wildcard, with the addition of the `=**` at the end of the variable:
`{variable=**}`. A multi-segment wildcard variable is available within the match
statement as a `path` object.

```
// Allow read at any path "/**", if condition evaluates to true
match /{multi_path=**} {
  // Matches anything at or below this, from "path", "path/to", "path/to/object", ...
  allow read: if <condition>;
}
```

## Request

The `request` variable is provided within a condition to represent the
request being made at that path. The `request` variable has a number of
properties which can be used to decide whether to allow the incoming request.

### Properties

#### `auth`

When an authenticated user performs a request against Cloud Storage,
the `auth` variable is populated with the user's `uid` (`request.auth.uid`) as
well as the claims of the Firebase Authentication JWT (`request.auth.token`).

`request.auth.token` contains some or all of the following keys:

| Field | Description |
|---|---|
| `email` | The email address associated with the account, if present. |
| `email_verified` | `true` if the user has verified they have access to the `email` address. Some providers automatically verify email addresses they own. |
| `phone_number` | The phone number associated with the account, if present. |
| `name` | The user's display name, if set. |
| `sub` | The user's Firebase UID. This is unique within a project. |
| `firebase.identities` | Dictionary of all the identities that are associated with this user's account. The keys of the dictionary can be any of the following: `email`, `phone`, `google.com`, `facebook.com`, `github.com`, `twitter.com`. The values of the dictionary are arrays of unique identifiers for each identity provider associated with the account. For example, `auth.token.firebase.identities["google.com"][0]` contains the first Google user ID associated with the account. |
| `firebase.sign_in_provider` | The sign-in provider used to obtain this token. Can be one of the following strings: `custom`, `password`, `phone`, `anonymous`, `google.com`, `facebook.com`, `github.com`, `twitter.com`. |
| `firebase.tenant` | The tenantId associated with the account, if present. e.g. `tenant2-m6tyz` |

If using custom authentication, `request.auth.token` also contains any custom
claims specified by the developer.

When an unauthenticated user performs a request, `request.auth` is `null`.

```
// Allow requests from authenticated users
allow read, write: if request.auth != null;
```

#### `path`

The `path` variable contains the path that a `request` is being performed
against.

```
// Allow a request if the first path segment equals "images"
allow read, write: if request.path[0] == 'images';
```

#### `resource`

The `resource` variable contains the metadata of a file being uploaded or the
updated metadata for an existing file. This is related to the
[`resource`](https://firebase.google.com/docs/reference/security/storage#resource_1) variable, which contains the current file metadata at
the requested path, as opposed to the new metadata.

```
// Allow a request if the new value is smaller than 5MB
allow read, write: if request.resource.size < 5 * 1024 * 1024;
```

`request.resource` contains the following properties from `resource`:

| Property |
|---|
| `name` |
| `bucket` |
| `metadata` |
| `size` |
| `contentType` |

#### `time`

The `time` variable contains a timestamp representing the current server time
a request is being evaluated at. You can use this to provide time-based access
to files, such as: only allowing files to be uploaded until a certain date,
or only allowing files to be read up to an hour after they were uploaded.

```
// Allow a read if the file was created less than one hour ago
allow read: if request.time < resource.timeCreated + duration.value(1, 'h');
```

Many functions are provided to write rules using [timestamps](https://firebase.google.com/docs/reference/security/storage#timestamp) and
[durations](https://firebase.google.com/docs/reference/security/storage#duration).

## Resource

The `resource` variable contains file metadata for files in
Cloud Storage, such as the file name, size, creation time, and
custom metadata.

### Properties

#### `name`

A string containing the full name of the file, including the path to the file.

```
// Allow reads if the resource name is "path/to/object"
allow read: if resource.name == 'path/to/object'
```

#### `bucket`

A string containing the [Google Cloud Storage](https://cloud.google.com/storage)
bucket this file is stored in.

```
// Allow reads of all resources in your bucket
allow read: if resource.bucket == '<your-cloud-storage-bucket>'
```

#### `generation`

A int containing the Google Cloud Storage
[object generation](https://cloud.google.com/storage/docs/object-versioning) of
the file. Used for object versioning.

```
// Allow reads if the resource matches a known object version
allow read: if resource.generation == <known-generation>
```

#### `metageneration`

A int containing the Google Cloud Storage
[object metageneration](https://cloud.google.com/storage/docs/object-versioning)
of the file. Used for object versioning.

```
// Allow reads if the resource matches a known object metadata version
allow read: if resource.metageneration == <known-generation>
```

#### `size`

An int containing the file size in bytes.

```
// Allow reads if the resource is less than 10 MB
allow read: if resource.size < 10 * 1024 * 1024;
```

#### `timeCreated`

A timestamp representing when the file was created.

```
// Allow reads if the resource was created less than an hour ago
allow read: if resource.timeCreated < request.time + duration.value(60, "m")
```

#### `updated`

A timestamp representing when the file was last updated.

```
// Allow reads if the resource was updated less than an hour ago
allow read: if resource.updated < request.time + duration.value(60, "m")
```

#### `md5Hash`

A string containing the [MD5 hash](https://en.wikipedia.org/wiki/MD5) of the
file.

```
// Allow writes if the hash of the uploaded file is the same as the existing file
allow write: if request.resource.md5Hash == resource.md5Hash;
```

> [!NOTE]
> **Note:** MD5 hash collisions are possible and could allow someone to overwrite a file, even if a rule like the above exists. Consider additional file validation or other rules to enforce immutability (e.g. `allow write: if resource ==
> null;`)

#### `crc32c`

A string containing the
[crc32c hash](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) of the
file.

```
// Allow writes if the hash of the uploaded file is the same as the existing file
allow write: if request.resource.crc32c == resource.crc32c;
```

> [!NOTE]
> **Note:** crc32c hash collisions are possible and could allow for someone to overwrite a file, even if a rule like the above exists. Consider additional file validation or other rules to enforce immutability (e.g. `allow write: if
> resource == null;`).

#### `etag`

A string containing the [etag](https://en.wikipedia.org/wiki/HTTP_ETag) of the
file.

```
// Allow writes if the etag matches a known object etag
allow write: if resource.etag == <known-generation>
```

#### `contentDisposition`

A string containing the content disposition of the file.

```
// Allow reads if the content disposition matches a certain value
allow read: if resource.contentDisposition == 'inlined';
```

#### `contentEncoding`

A string containing the content encoding of the file.

```
// Allow reads if the content is encoded with gzip
allow read: if resource.contentEncoding == 'gzip';
```

#### `contentLanguage`

A string containing the content language of the file.

```
// Allow reads if the content language is Japanese
allow read: if resource.contentLanguage == 'ja';
```

#### `contentType`

A string containing the content type of the file.

```
// Allow reads if the content type is PNG.
allow read: if resource.contentType == 'image/png';
```

#### `metadata`

A `Map<String, String>` containing additional developer provided metadata
fields.

```
// Allow reads if a certain metadata field matches a desired value
allow read: if resource.metadata.customProperty == 'customValue';
```

## firestore.get and firestore.exists

The `firestore.get()` and `firestore.exists()` functions allow you to access
documents in Cloud Firestore to evaluate complex authorization criteria.

The `firestore.get()` and `firestore.exists()` functions both expect
fully-specified document paths. When using variables to construct paths for
`firestore.get()` and `firestore.exists()`, you need to explicitly escape
variables using the `$(variable)` syntax.

### firestore.get

Get the contents of a Cloud Firestore document.

```
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{club}/files/{fileId} {
      allow read: if club in
        firestore.get(/databases/(default)/documents/users/$(request.auth.uid)).data.memberships
    }
  }
}
```

### firestore.exists

Check if a Cloud Firestore document exists.

```
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/photos/{fileId} {
      allow read: if
        firestore.exists(/databases/(default)/documents/users/$(userId)/friends/$(request.auth.uid))
    }
  }
}
```

## Service

The `service` is the first declaration in a Cloud Storage Security Rules file, and
specifies which service these rules will apply to.

### Name

#### `name`

The name of the service rules will be apply to. The only current value is
`firebase.storage`.

```
// Specify the service name
service firebase.storage {
  match /b/{bucket}/o {
    ...
  }
}
```

## Data Types

The Security Rules language allows you to check type using the `is` operator.

    // For example
    a is null
    a is string

### `null`

The `null` data type represents a value not existing.

```
allow read: if request.auth != null;
```

### `bool`

The `bool` type represents a boolean `true` or `false` value.

```
allow read: if true;   // always succeeds
allow write: if false; // always fails
```

#### Comparison

Boolean values can be compared using the `==` operators `!=`.

#### Boolean Operations

| Operation | Expression |
|---|---|
| `AND` | `x && y` |
| `OR` | `x || y` |
| `NOT` | `!x` |

Operations short circuit, and can return either `true`, `false`, or an
[Error](https://firebase.google.com/docs/reference/security/storage#errors).

```
allow read: if true || false;   // always succeeds, short circuits at true
allow write: if false && true; // always fails, short circuits at false
```

### `int` and `float`

The `int` and `float` types represent numbers. Ints are: `0`, `1`, `-2`, etc.
, while floats are: `1.0`, `-2.0`, `3.33`, etc.

Ints are signed 64-bit values, and floats are 64-bit IEEE 754 compliant values.
Values of type `int` will be coerced to `float` when used in comparisons and
arithmetic operations with a `float` value.

#### Comparison

Ints and floats can be compared and ordered using the `==`, `!=`, `>`, `<`,
`>=`, and `<=` operators.

#### Arithmetic

Ints and floats can be added, subtracted, multiplied, divided, moduloed, and
negated:

| Operation | Expression |
|---|---|
| Addition | `x + y` |
| Subtraction | `x - y` |
| Multiplication | `x * y` |
| Division | `x / y` |
| Modulo | `x % y` |
| Negation | `-x` |

#### Mathematical functions

Firebase Security Rules for Cloud Storage also provides a number of mathematics helper
functions to simplify expressions:

| Function | Description |
|---|---|
| `math.ceil(x)` | Ceiling of the numeric value |
| `math.floor(x)` | Floor of the numeric value |
| `math.round(x)` | Round the input value to the nearest int |
| `math.abs(x)` | Absolute value of the input |
| `math.isInfinite(x)` | Test whether the value is `±∞`, returns a `bool` |
| `math.isNaN(x)` | Test whether the value is not a number `NaN`, returns a `bool` |

### `string`

#### Comparison

Strings can be lexographically compared and ordered using the `==`, `!=`, `>`, `<`, `>=`, and
`<=` operators.

#### Concatenation

Strings can be concatenated using the `+` operator.

```
// Concatenate a file name and extension
'file' + '.txt'
```

#### Index and Range

The `index` operator, `string[]`, returns a string that contains the character
at the provided index in the string.

```
// Allow reads of files that begin with 'a'
match /{fileName} {
  allow read: if fileName[0] == 'a';
}
```

The `range` operator, `string[i:j]`, returns a string that contains the
characters between the specified indices, from `i` (inclusive) until `j`
(exclusive). If `i` or `j` are not specified, they default to 0 and the size of
the string, respectively, but at least `i` or `j` must be specified
for the range to be valid.

```
// Allow reads of files that begin with 'abcdef'
match /{fileName} {
  allow read: if fileName[0:6] == 'abcdef';
}
```

The `index` and `range` operators will yield an error if the indices provided
exceed the string bounds.

#### `size`

Returns the number of characters in the string.

```
// Allow files with names less than 10 characters
match /{fileName} {
  allow write: if fileName.size() < 10;
}
```

#### `matches`

Performs a regular expression match, returns `true` if the string matches the
given regular expression. Uses
[Google RE2 syntax](https://github.com/google/re2/wiki/Syntax).

```
// Allow writes to files which end in ".txt"
match /{fileName} {
  allow write: if fileName.matches('.*\\.txt')
}
```

#### `split`

Splits a string according to a provided regular expression and returns a `list`
of strings. Uses [Google RE2 syntax](https://github.com/google/re2/wiki/Syntax).

```
// Allow files named "file.*" to be uploaded
match /{fileName} {
  allow write: if fileName.split('.*\\..*')[0] == 'file'
}
```

### `path`

Paths are directory-like names with optional pattern matching. The
presence of a forward slash `/` denotes the start of a path segment.

#### `path`

Converts a `string` argument to a `path`.

```
// Allow reads on a specific file path
match /{allFiles=**} {
  allow read: if allFiles == path('/path/to/file');
}
```

### `timestamp`

Timestamps are in UTC, with possible values beginning at 0001-01-01T00.00.00Z
and ending at 9999-12-31T23.59.59Z.

#### Comparison

Timestamps can be compared and ordered using the `==`, `!=`, `>`, `<`, `>=`, and
`<=` operators.

#### Arithmetic

Timestamps support addition and subtraction between timestamps and durations as
follows:

| Expression | Result |
|---|---|
| `timestamp + duration` | `timestamp` |
| `duration + timestamp` | `timestamp` |
| `timestamp - duration` | `timestamp` |
| `timestamp - timestamp` | `duration` |
| `duration + duration` | `duration` |
| `duration - duration` | `duration` |

#### `date`

A `timestamp` value containing the `year`, `month`, and `day` only.

```
// Allow reads on the same day that the resource was created.
allow read: if request.time.date() == resource.timeCreated.date()
```

#### `year`

The year value as an int, from 1 to 9999.

```
// Allow reads on all requests made before 2017
allow read: if request.time.year() < 2017
```

#### `month`

The month value as an int, from 1 to 12.

```
// Allow reads on all requests made during the month of January
allow read: if request.time.month() == 1;
```

#### `day`

The current day of the month as an int, from 1 to 31.

```
// Allow reads on all requests made during the first day of each month
allow read: if request.time.day() == 1;
```

#### `time`

A `duration` value containing the current time.

```
// Allow reads on all requests made before 12PM
allow read: if request.time.time() < duration.time(12, 0, 0, 0);
```

#### `hours`

The hours value as an int, from 0 to 23.

```
// Allow reads on all requests made before 12PM
allow read: if request.time.hours() < 12;
```

#### `minutes`

The minutes value as an int, from 0 to 59.

```
// Allow reads during even minutes of every hour
allow read: if request.time.minutes() % 2 == 0;
```

#### `seconds`

The seconds value as an int, from 0 to 59.

```
// Allow reads during the second half of each minute
allow read: if request.time.seconds() > 29;
```

#### `nanos`

The fractional seconds in nanos as an int.

```
// Allow reads during the first 0.1 seconds of each second
allow read: if request.time.nanos() < 100000000;
```

#### `dayOfWeek`

The day of the week, from 1 (Monday) to 7 (Sunday).

```
// Allow reads on weekdays (Monday to Friday)
allow read: if request.time.dayOfWeek() < 6;
```

#### `dayOfYear`

The day of the current year, from 1 to 366.

```
// Allow reads every fourth day
allow read: if request.time.dayOfYear() % 4 == 0;
```

#### `toMillis`

Returns the current number of milliseconds since the Unix epoch.

```
// Allow reads if the request is made before a specified time
allow read: if request.time.toMillis() < <milliseconds>;
```

### `duration`

Duration values are represented as seconds plus fractional seconds in
nanoseconds.

#### Comparison

Durations can be compared and ordered using the `==`, `!=`, `>`, `<`, `>=`, and
`<=` operators.

#### Arithmetic

Durations support addition and subtraction between timestamps and durations as
follows:

| Expression | Result |
|---|---|
| `timestamp + duration` | `timestamp` |
| `duration + timestamp` | `timestamp` |
| `timestamp - duration` | `timestamp` |
| `timestamp - timestamp` | `duration` |
| `duration + duration` | `duration` |
| `duration - duration` | `duration` |

#### `seconds`

The number of seconds in the current duration. Must be between -315,576,000,000
and +315,576,000,000 inclusive.

#### `nanos`

The number of fractional seconds (in nanoseconds) of the current duration. Must
be beween -999,999,999 and +999,999,999 inclusive. For non-zero seconds and
non-zero nanonseconds, the signs of both must be in agreement.

#### `duration.value`

Durations can be created using the `duration.value(int magnitude, string units)`
function, which creates a time duration from the given magnitude and unit.

```
// All of these durations represent one hour:
duration.value(1, "h")
duration.value(60, "m")
duration.value(3600, "s")
```

Possible `unit`s are:

| Duration | `unit` |
|---|---|
| Weeks | `w` |
| Days | `d` |
| Hours | `h` |
| Minutes | `m` |
| Seconds | `s` |
| Milliseconds | `ms` |
| Nanoseconds | `ns` |

#### `duration.time`

Durations can be created using the
`duration.time(int hours, int minutes, int seconds, int nanoseconds)` function,
which creates a time duration of the given hours, minutes, seconds, and
nanoseconds.

```
// Create a four hour, three minute, two second, one nanosecond duration
duration.time(4, 3, 2, 1)
```

### `list`

A list contains an ordered array of values, which can of type: `null`, `bool`,
`int`, `float`, `string`, `path`, `list`, `map`, `timestamp`, or `duration`.

Given *`x`* and *`y`* of type `list` and `i` and `j` of type `int`

#### Creation

To create a list, add values between brackets:

```
// Create a list of strings
['apples', 'grapes', 'bananas', 'cheese', 'goats']
```

#### Comparison

Lists can be compared using the `==` operators `!=`. Equality of two lists
requires all values to be equal.

#### Index and Range

The `index` operator, `list[]`, returns the item at the provided index in the
list.

```
// Allow reads of all files that begin with 'a'
match /{fileName} {
  allow read: if fileName[0] == 'a';
}
```

The `range` operator, `list[i:j]`, returns all items in a list between the
specified indices, from `i` (inclusive) until `j` (exclusive). If `i` or `j` are
not specified, they default to 0 and the size of the list, respectively, but
at least `i` or `j` must be specified for the range to be valid.

```
// Allow reads of all files that begin with 'abcdef'
match /{fileName} {
  allow read: if fileName[0:6] == 'abcdef';
}
```

#### `in`

Returns `true` if the desired value is present in the list or `false` if not
present.

```
// Allow read if a filename has the string 'txt' in it
match /{fileName} {
  allow read: if 'txt' in fileName.split('\\.');
}
```

#### `join`

Combines a list of strings into a single string, separated by the given string.

```
// Allow reads if the joined array is 'file.txt'
allow read: if ['file', 'txt'].join('.') == 'file.txt';
```

#### `size`

The number of items in the list.

```
// Allow read if there are three items in our list
allow read: if ['foo', 'bar', 'baz'].size() == 3;
```

#### `hasAll`

Returns `true` if all values are present in the list.

```
// Allow read if one list has all items in the other list
allow read: if ['file', 'txt'].hasAll(['file', 'txt']);
```

### `map`

A map contains key/value pairs, where keys are strings and values can be any
of: `null`, `bool`, `int`, `float`, `string`, `path`, `list`, `map`,
`timestamp`, or `duration`.

#### Creation

To create a map, add key/value pairs between braces:

```
// Create a map of strings to strings
{
  'mercury': 'mars',
  'rain': 'cloud',
  'cats': 'dogs',
}
```

#### Comparison

Maps can be compared using the `==` operators `!=`. Equality of two maps
requires all keys are present in both maps and all values are equal.

#### Index

Values in a map are accessed by using either bracket or dot notation:

```
// Access custom metadata properties
allow read: if resource.metadata.property == 'property'
allow write: if resource.metadata['otherProperty'] == 'otherProperty'
```

If a key is not present, an `error` will be returned.

#### `in`

Returns `true` if the desired key is present in the map or `false` if not
present.

```
// Allow reads if a property is present in the custom metadata
allow read: if property in resource.metadata;
```

#### `size`

The number of keys in the map.

```
// Allow reads if there's exactly one custom metadata key
allow read: if resource.metadata.size() == 1;
```

#### `keys`

A list of all keys in the map.

```
// Allow reads if the first metadata key is 'myKey'
allow read: if resource.metadata.keys()[0] == 'myKey';
```

#### `values`

A list of all values in the map, in key order.

```
// Allow reads if the first metadata value is 'myValue'
allow read: if resource.metadata.values()[0] == 'myValue';
```

## Errors

### Error Evaluation

Firebase Security Rules for Cloud Storage continue evaluation when errors are encountered.
This is useful because conditional `&&` and `||` expressions may absorb an error
if the conditional would otherwise short-circuit to `false` or `true`
respectively. For instance:

| Expression | Result |
|---|---|
| `error && true` | `error` |
| `error && false` | `false` |
| `error || true` | `true` |
| `error || false` | `error` |

Common places where errors are raised are: division by zero, accessing values
in a list or map that don't exist, and passing values of the incorrect type
to a function.

```
// Error if resource.size is zero
allow read: if 1000000 / resource.size;

// Error, key doesn't exist
allow read: if resource.metadata.nonExistentKey == 'value';

// Error, no unit 'y' exists
allow read: if request.time < resource.timeCreated + duration.value(1, 'y');
```