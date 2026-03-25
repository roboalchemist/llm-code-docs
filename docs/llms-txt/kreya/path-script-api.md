# Source: https://kreya.app/docs/scripting-and-tests/general/path-script-api.md

# Path module reference

The `path` module provides utilities for working with file and directory paths and can be accessed using an import:

```
import { join } from "path";`

const grpcOperationPath = join("../", "gRPC", "my-operation");
```

### Path resolution[​](#path-resolution "Direct link to Path resolution")

When used in Kreya scripts and operations, all paths are resolved relative to the directory of the running operation or script This mirrors `path.resolve` starting from that directory.

## Variables[​](#variables "Direct link to Variables")

### delimiter[​](#delimiter "Direct link to delimiter")

```
const delimiter: ";" | ":";
```

Provides the platform-specific path delimiter.

***

### sep[​](#sep "Direct link to sep")

```
const sep: "\" | "/";
```

Provides the platform-specific path segment separator.

## Functions[​](#functions "Direct link to Functions")

### basename()[​](#basename "Direct link to basename()")

#### Call Signature[​](#call-signature "Direct link to Call Signature")

```
function basename(path: string): string;
```

Returns the last portion of a path, similar to the Unix basename command. Trailing directory separators are ignored.

##### Parameters[​](#parameters "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `path`    | `string` |             |

##### Returns[​](#returns "Direct link to Returns")

`string`

#### Call Signature[​](#call-signature-1 "Direct link to Call Signature")

```
function basename(path: string, suffix: string): string;
```

Returns the last portion of a path, similar to the Unix basename command. Trailing directory separators are ignored.

##### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `path`    | `string` |             |
| `suffix`  | `string` |             |

##### Returns[​](#returns-1 "Direct link to Returns")

`string`

***

### dirname()[​](#dirname "Direct link to dirname()")

```
function dirname(path: string): string;
```

Returns the directory name of a path, similar to the Unix dirname command. Trailing directory separators are ignored.

#### Parameters[​](#parameters-2 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `path`    | `string` |             |

#### Returns[​](#returns-2 "Direct link to Returns")

`string`

***

### extname()[​](#extname "Direct link to extname()")

```
function extname(path: string): string;
```

Returns the extension of the path, from the last occurrence of the . (period) character to end of string in the last portion of the path. If there is no . in the last portion of the path, or if there are no . characters other than the first character of the basename of path, an empty string is returned.

#### Parameters[​](#parameters-3 "Direct link to Parameters")

| Parameter | Type     | Description |
| --------- | -------- | ----------- |
| `path`    | `string` |             |

#### Returns[​](#returns-3 "Direct link to Returns")

`string`

***

### format()[​](#format "Direct link to format()")

```
function format(pathObject: FormatInputPathObject): string;
```

Formats a file path from a PathObject.

#### Parameters[​](#parameters-4 "Direct link to Parameters")

| Parameter    | Type                                              | Description                                    |
| ------------ | ------------------------------------------------- | ---------------------------------------------- |
| `pathObject` | [`FormatInputPathObject`](#formatinputpathobject) | The PathObject containing the path components. |

#### Returns[​](#returns-4 "Direct link to Returns")

`string`

A formatted file path string.

***

### isAbsolute()[​](#isabsolute "Direct link to isAbsolute()")

```
function isAbsolute(path: string): boolean;
```

Determines if the literal path is absolute. Therefore, it’s not safe for mitigating path traversals. If the given path is a zero-length string, false will be returned.

#### Parameters[​](#parameters-5 "Direct link to Parameters")

| Parameter | Type     | Description   |
| --------- | -------- | ------------- |
| `path`    | `string` | path to test. |

#### Returns[​](#returns-5 "Direct link to Returns")

`boolean`

***

### join()[​](#join "Direct link to join()")

```
function join(...paths: string[]): string;
```

Join all arguments together and normalize the resulting path.

#### Parameters[​](#parameters-6 "Direct link to Parameters")

| Parameter  | Type        | Description    |
| ---------- | ----------- | -------------- |
| ...`paths` | `string`\[] | paths to join. |

#### Returns[​](#returns-6 "Direct link to Returns")

`string`

***

### normalize()[​](#normalize "Direct link to normalize()")

```
function normalize(path: string): string;
```

Normalize a string path, reducing '..' and '.' parts. When multiple slashes are found, they're replaced by a single one; when the path contains a trailing slash, it is preserved. On Windows backslashes are used.

#### Parameters[​](#parameters-7 "Direct link to Parameters")

| Parameter | Type     | Description              |
| --------- | -------- | ------------------------ |
| `path`    | `string` | string path to normalize |

#### Returns[​](#returns-7 "Direct link to Returns")

`string`

***

### parse()[​](#parse "Direct link to parse()")

```
function parse(path: string): ParsedPath;
```

See [ParsedPath](#parsedpath).<br /><!-- -->Parses a file path into its constituent components.

#### Parameters[​](#parameters-8 "Direct link to Parameters")

| Parameter | Type     | Description             |
| --------- | -------- | ----------------------- |
| `path`    | `string` | The file path to parse. |

#### Returns[​](#returns-8 "Direct link to Returns")

[`ParsedPath`](#parsedpath)

A ParsedPath record containing the parsed components.

***

### relative()[​](#relative "Direct link to relative()")

```
function relative(from: string, to: string): string;
```

Returns the relative path from from to to based on the current working directory. If from and to each resolve to the same path (after calling path.resolve() on each), a zero-length string is returned. If a zero-length string is passed as from or to, the current working directory will be used instead of the zero-length strings.

#### Parameters[​](#parameters-9 "Direct link to Parameters")

| Parameter | Type     | Description      |
| --------- | -------- | ---------------- |
| `from`    | `string` | The source path. |
| `to`      | `string` | The target path. |

#### Returns[​](#returns-9 "Direct link to Returns")

`string`

***

### resolve()[​](#resolve "Direct link to resolve()")

```
function resolve(...paths: string[]): string;
```

Resolves a sequence of paths or path segments into an absolute path. The given sequence of paths is processed from right to left, with each subsequent path prepended until an absolute path is constructed. For instance, given the sequence of path segments: `/foo`, `/bar`, `baz`, calling `resolve('/foo', '/bar', 'baz')` would return `/bar/baz` because `'baz'` is not an absolute path but `'/bar' + '/' + 'baz'` is. If, after processing all given path segments, an absolute path has not yet been generated, the current working directory is used. The resulting path is normalized and trailing slashes are removed unless the path is resolved to the root directory. Zero-length path segments are ignored. If no path segments are passed, path.resolve() will return the absolute path of the current working directory.

#### Parameters[​](#parameters-10 "Direct link to Parameters")

| Parameter  | Type        | Description                          |
| ---------- | ----------- | ------------------------------------ |
| ...`paths` | `string`\[] | A sequence of paths or path segments |

#### Returns[​](#returns-10 "Direct link to Returns")

`string`

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### FormatInputPathObject[​](#formatinputpathobject "Direct link to FormatInputPathObject")

```
type FormatInputPathObject = {
  base?: string;
  dir?: string;
  ext?: string;
  name?: string;
  root?: string;
};
```

Represents the parsed components of a file path.

#### Properties[​](#properties "Direct link to Properties")

##### base?[​](#base "Direct link to base?")

```
optional base: string;
```

The base name of the file (including the extension).

##### dir?[​](#dir "Direct link to dir?")

```
optional dir: string;
```

The directory path from the root to the base name.

##### ext?[​](#ext "Direct link to ext?")

```
optional ext: string;
```

The file extension (including the leading period). If there is no extension, it will be an empty string.

##### name?[​](#name "Direct link to name?")

```
optional name: string;
```

The file name without the extension.

##### root?[​](#root "Direct link to root?")

```
optional root: string;
```

The root of the path such as '/' or 'c:'.

***

### ParsedPath[​](#parsedpath "Direct link to ParsedPath")

```
type ParsedPath = {
  base: string;
  dir: string;
  ext: string;
  name: string;
  root: string;
};
```

Represents the parsed components of a file path.

#### Properties[​](#properties-1 "Direct link to Properties")

##### base[​](#base-1 "Direct link to base")

```
base: string;
```

The base name of the file (including the extension).

##### dir[​](#dir-1 "Direct link to dir")

```
dir: string;
```

The directory path from the root to the base name.

##### ext[​](#ext-1 "Direct link to ext")

```
ext: string;
```

The file extension (including the leading period). If there is no extension, it will be an empty string.

##### name[​](#name-1 "Direct link to name")

```
name: string;
```

The file name without the extension.

##### root[​](#root-1 "Direct link to root")

```
root: string;
```

The root of the path such as '/' or 'c:'.
