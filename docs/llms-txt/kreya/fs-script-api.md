# Source: https://kreya.app/docs/scripting-and-tests/general/fs-script-api.md

# FileSystem module reference

The `fs/promises` module provides utilities for working with files and can be accessed using an import:

```
import { readFile } from 'fs/promises';

const content = await readFile('./foo.txt', 'utf8');
```

### Path resolution[​](#path-resolution "Direct link to Path resolution")

All `fs/promises` paths are resolved relative to the directory of the running operation or script (equivalent to using `path.resolve` from that directory).

### Project sandbox[​](#project-sandbox "Direct link to Project sandbox")

Kreya scripts can only access files within the Kreya project directory and its subdirectories; access outside this sandbox is blocked.

## Functions[​](#functions "Direct link to Functions")

### appendFile()[​](#appendfile "Direct link to appendFile()")

#### Call Signature[​](#call-signature "Direct link to Call Signature")

```
function appendFile(
   path: string, 
   data: string, 
encodingName?: string): Promise<void>;
```

Appends data to a file, replacing the file if it already exists.

##### Parameters[​](#parameters "Direct link to Parameters")

| Parameter       | Type     | Description                                                                                |
| --------------- | -------- | ------------------------------------------------------------------------------------------ |
| `path`          | `string` | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`          | `string` | The data to append.                                                                        |
| `encodingName?` | `string` | The encoding to use: utf8 (default), utf16le, ascii, hex, base64, or base64url.            |

##### Returns[​](#returns "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-1 "Direct link to Call Signature")

```
function appendFile(
   path: string, 
   data: string, 
options: FileAppendOptions): Promise<void>;
```

Appends data to a file.

##### Parameters[​](#parameters-1 "Direct link to Parameters")

| Parameter | Type                                      | Description                                                                                |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string`                                  | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `string`                                  | The data to append.                                                                        |
| `options` | [`FileAppendOptions`](#fileappendoptions) | The options.                                                                               |

##### Returns[​](#returns-1 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-2 "Direct link to Call Signature")

```
function appendFile(path: string, data: Uint8Array): Promise<void>;
```

Appends data to a file, replacing the file if it already exists.

##### Parameters[​](#parameters-2 "Direct link to Parameters")

| Parameter | Type         | Description                                                                                |
| --------- | ------------ | ------------------------------------------------------------------------------------------ |
| `path`    | `string`     | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `Uint8Array` | The data to append.                                                                        |

##### Returns[​](#returns-2 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-3 "Direct link to Call Signature")

```
function appendFile(
   path: string, 
   data: Uint8Array, 
options: FileAppendOptions): Promise<void>;
```

Appends data to a file, replacing the file if it already exists (depending on `options.flag`).

##### Parameters[​](#parameters-3 "Direct link to Parameters")

| Parameter | Type                                      | Description                                                                                |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string`                                  | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `Uint8Array`                              | The data to append.                                                                        |
| `options` | [`FileAppendOptions`](#fileappendoptions) | The options.                                                                               |

##### Returns[​](#returns-3 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-4 "Direct link to Call Signature")

```
function appendFile(
   path: string, 
   data: Uint8Array, 
options: FileAppendOptions): Promise<void>;
```

Appends data to a file, replacing the file if it already exists (depending on `options.flag`).

##### Parameters[​](#parameters-4 "Direct link to Parameters")

| Parameter | Type                                      | Description                                                                                |
| --------- | ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string`                                  | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `Uint8Array`                              | The data to append.                                                                        |
| `options` | [`FileAppendOptions`](#fileappendoptions) | The options.                                                                               |

##### Returns[​](#returns-4 "Direct link to Returns")

`Promise`<`void`>

***

### readFile()[​](#readfile "Direct link to readFile()")

#### Call Signature[​](#call-signature-5 "Direct link to Call Signature")

```
function readFile(path: string): Promise<Uint8Array<ArrayBufferLike>>;
```

Reads the entire content of a file.

##### Parameters[​](#parameters-5 "Direct link to Parameters")

| Parameter | Type     | Description                                                                                |
| --------- | -------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string` | The path to the file (resolved relative to the directory of the running script/operation). |

##### Returns[​](#returns-5 "Direct link to Returns")

`Promise`<`Uint8Array`<`ArrayBufferLike`>>

The data of the file.

#### Call Signature[​](#call-signature-6 "Direct link to Call Signature")

```
function readFile(path: string, encodingName: string): Promise<string>;
```

Reads the entire content of a file.

##### Parameters[​](#parameters-6 "Direct link to Parameters")

| Parameter      | Type     | Description                                                                                |
| -------------- | -------- | ------------------------------------------------------------------------------------------ |
| `path`         | `string` | The path to the file (resolved relative to the directory of the running script/operation). |
| `encodingName` | `string` | The encoding to use: utf8 (default), utf16le, ascii, hex, base64, or base64url.            |

##### Returns[​](#returns-6 "Direct link to Returns")

`Promise`<`string`>

The contents of the file.

#### Call Signature[​](#call-signature-7 "Direct link to Call Signature")

```
function readFile(path: string, options: FileReadOptions): Promise<Uint8Array<ArrayBufferLike>> | Promise<string>;
```

Reads the entire content of a file.

##### Parameters[​](#parameters-7 "Direct link to Parameters")

| Parameter | Type                                  | Description                                                     |
| --------- | ------------------------------------- | --------------------------------------------------------------- |
| `path`    | `string`                              | The path of the file (resolved relative to the running script). |
| `options` | [`FileReadOptions`](#filereadoptions) | The options to read the file, including `encoding`.             |

##### Returns[​](#returns-7 "Direct link to Returns")

`Promise`<`Uint8Array`<`ArrayBufferLike`>> | `Promise`<`string`>

The file content as string if an encoding is provided, as Uint8Array otherwise.

***

### writeFile()[​](#writefile "Direct link to writeFile()")

#### Call Signature[​](#call-signature-8 "Direct link to Call Signature")

```
function writeFile(
   path: string, 
   data: string, 
encodingName?: string): Promise<void>;
```

Writes data to a file, replacing the file if it already exists.

##### Parameters[​](#parameters-8 "Direct link to Parameters")

| Parameter       | Type     | Description                                                                                |
| --------------- | -------- | ------------------------------------------------------------------------------------------ |
| `path`          | `string` | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`          | `string` | The data to write.                                                                         |
| `encodingName?` | `string` | The encoding to use: utf8 (default), utf16le, ascii, hex, base64, or base64url.            |

##### Returns[​](#returns-8 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-9 "Direct link to Call Signature")

```
function writeFile(
   path: string, 
   data: string, 
options: FileWriteOptions): Promise<void>;
```

Writes data to a file, replacing the file if it already exists (depending on `options.flag`).

##### Parameters[​](#parameters-9 "Direct link to Parameters")

| Parameter | Type                                    | Description                                                                                |
| --------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string`                                | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `string`                                | The data to write.                                                                         |
| `options` | [`FileWriteOptions`](#filewriteoptions) | The options.                                                                               |

##### Returns[​](#returns-9 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-10 "Direct link to Call Signature")

```
function writeFile(path: string, data: Uint8Array): Promise<void>;
```

Writes data to a file, replacing the file if it already exists.

##### Parameters[​](#parameters-10 "Direct link to Parameters")

| Parameter | Type         | Description                                                                                |
| --------- | ------------ | ------------------------------------------------------------------------------------------ |
| `path`    | `string`     | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `Uint8Array` | The data to write.                                                                         |

##### Returns[​](#returns-10 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-11 "Direct link to Call Signature")

```
function writeFile(
   path: string, 
   data: Uint8Array, 
options: FileWriteOptions): Promise<void>;
```

Writes data to a file, replacing the file if it already exists (depending on `options.flag`).

##### Parameters[​](#parameters-11 "Direct link to Parameters")

| Parameter | Type                                    | Description                                                                                |
| --------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string`                                | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `Uint8Array`                            | The data to write.                                                                         |
| `options` | [`FileWriteOptions`](#filewriteoptions) | The options.                                                                               |

##### Returns[​](#returns-11 "Direct link to Returns")

`Promise`<`void`>

#### Call Signature[​](#call-signature-12 "Direct link to Call Signature")

```
function writeFile(
   path: string, 
   data: Uint8Array, 
options: FileWriteOptions): Promise<void>;
```

Writes data to a file, replacing the file if it already exists (depending on `options.flag`).

##### Parameters[​](#parameters-12 "Direct link to Parameters")

| Parameter | Type                                    | Description                                                                                |
| --------- | --------------------------------------- | ------------------------------------------------------------------------------------------ |
| `path`    | `string`                                | The path to the file (resolved relative to the directory of the running script/operation). |
| `data`    | `Uint8Array`                            | The data to write.                                                                         |
| `options` | [`FileWriteOptions`](#filewriteoptions) | The options.                                                                               |

##### Returns[​](#returns-12 "Direct link to Returns")

`Promise`<`void`>

## Type Aliases[​](#type-aliases "Direct link to Type Aliases")

### FileAppendOptions[​](#fileappendoptions "Direct link to FileAppendOptions")

```
type FileAppendOptions = {
  encoding?: string;
  flag?: string;
};
```

Options to append to files.

#### Properties[​](#properties "Direct link to Properties")

##### encoding?[​](#encoding "Direct link to encoding?")

```
optional encoding: string;
```

The encoding to use: utf8 (default), utf16le, ascii, hex, base64, or base64url.

##### flag?[​](#flag "Direct link to flag?")

```
optional flag: string;
```

File system flag (default a). Supported values: a, ax, a+, ax+, as, as+, w, wx, w+, wx+, r, rs, r+, rs+. Use an x suffix to fail if the file exists, + to allow reading, and s to open synchronously. See also <https://nodejs.org/api/fs.html#file-system-flags>.

***

### FileReadOptions[​](#filereadoptions "Direct link to FileReadOptions")

```
type FileReadOptions = {
  encoding?: string;
};
```

Options when reading a file.

#### Properties[​](#properties-1 "Direct link to Properties")

##### encoding?[​](#encoding-1 "Direct link to encoding?")

```
optional encoding: string;
```

The encoding to use: utf8 (default), utf16le, ascii, hex, base64, or base64url.

***

### FileWriteOptions[​](#filewriteoptions "Direct link to FileWriteOptions")

```
type FileWriteOptions = {
  encoding?: string;
  flag?: string;
};
```

Options to write files.

#### Properties[​](#properties-2 "Direct link to Properties")

##### encoding?[​](#encoding-2 "Direct link to encoding?")

```
optional encoding: string;
```

The encoding to use: utf8 (default), utf16le, ascii, hex, base64, or base64url.

##### flag?[​](#flag-1 "Direct link to flag?")

```
optional flag: string;
```

File system flag (default w). Supported values: w, wx, w+, wx+, a, ax, a+, ax+, as, as+, r, rs, r+, rs+. Use an x suffix to fail if the file exists, + to allow reading, and s to open synchronously. See also <https://nodejs.org/api/fs.html#file-system-flags>.
