# Source: https://docs.xano.com/the-function-stack/functions/apis-and-lambdas/lambda-functions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lambda Functions

## What are Lambda Functions?

Lambda functions allow you to execute JavaScript or TypeScript inside of your Xano function stacks. You may prefer to do this if you are porting old workflows to Xano and already have the code written, or maybe you just prefer to write code instead of using the function stack.

You can also use Lambda functions to leverage custom NPM packages.

## How do I write Lambda functions in Xano?

#### Special Variables

Lambdas have the ability to reference all the available data just like normal function stack statements. All special variables are prefixed with a `$` symbol.

* Xano variables are accessible through the `$var` special variable. To access a Xano variable named title, you would reference it as `$var.title`.
* Xano inputs are accessible through the `$input` special variable. To access a Xano input named score, you would reference it as `$input.score`.
* Xano environment variables are accessible through the `$env` special variable. To access a Xano environment variable named ip, you would reference it as `$env.ip`.
* The authenticated user details are accessible through the `$auth` special variable. The most common members of this variable include `$auth.id` and `$auth.extras`. If there is no authenticated user, then `$auth.id` will evaluate as 0.

#### Context Variables

Depending on how you use a Lambda, you may have support to access some additional variables, known as context variables. These follow the same naming convention as special variables by using a `$` prefix. The most common context variables will be `$this`, `$index`, `$parent`, and `$result`. The meaning of these variables are best described within the examples of the [higher order filters](/the-function-stack/filters/transform#lambda-filters).

## Using the Lambda AI Assistant

<Steps>
  <Step title="Give the assistant context by running your function stack first.">
    If you don't do this, you can still use the AI assistant, but it will make certain inferences that may not be correct.
  </Step>

  <Step title="Look for the 'AI Assistant' button and click it to enable the assistant.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/bed1b8d3-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=b3af2498047ffe978f4e8fdb5aeae66a" width="106" height="46" data-path="images/bed1b8d3-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Ask the assistant for help as needed.">
    In this example, we're asking the assistant to write a function that imports the Decamelize library and applies it to our 'test' input.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/c8ee9a16-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=fd378dc2c2bd6c1ff84d9001fe5cbb56" width="513" height="741" data-path="images/c8ee9a16-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Choose how to proceed with the assistant's suggestions.">
    You can click <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e4ae8e64-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=c49edbe0f90687010ac68e44ebc1edda" className="inline m-0" width="98" height="35" data-path="images/e4ae8e64-image.jpeg" /> to add the suggestions to the Lambda function code, or you can copy it manually and place it as needed.

    Be sure to **rate the assistant's suggestion(s)** using the 👍 and 👎 buttons. We'll use this information to improve the behavior of the assistant in future iterations.
  </Step>
</Steps>

## Using NPM Packages

<Warning>
  **Before you begin**

  It is **highly recommended** that you include version numbers in your imports to ensure code stability; this will allow you time to verify updates to packages and avoid any potential issues.
</Warning>

If you have an NPM package you'd like to use in your Lambda functions, you can import it using the following format:

```javascript  theme={null}
const { default: Decamelize } = await import ("npm:decamelize");
```

When we want to utilize the functions imported from the package listed, we can do so like this:

```javascript  theme={null}
return Decamelize($input.test);
```

Native Node libraries that are native can be accessed with a `node:` prefix instead of `npm:`

```javascript  theme={null}
const { request } = await import("node:https");
```

<Info>
  Please note that not all NPM packages may function properly inside of Xano. If you encounter an issue importing a specific package, please reach out to our support team for further clarification.
</Info>

Private packages are imported using query parameters on the package name:

```
const pkg = await import(
  `@your-scope/your-package?token=${$env.NPM_REGISTRY_TOKEN}&registry=YOUR_REGISTRY_HOST`
);
```

This is detailed in the example when you open the Lambda editor. The above example assumes you have an environment variable called NPM\_REGISTRY\_TOKEN, although it doesn't have to be an environment variable it's definitely best practice.

If your package is ESM (`"type": "module"` in `package.json`), `require()` will fail.

`await import(...)` works and is the safest default.

So if you’re unsure what your package exports, use `await import()`.

## **Working with Files**

Xano provides a comprehensive set of filesystem functions that allow you to read, write, and manipulate files and directories. These functions are available through the global `Deno` namespace.

### Reading Files

#### Read Text Files

```javascript  theme={null}
// Read entire file as string
const content = await Deno.readTextFile("/path/to/file.txt");
```

#### Read Binary Files

```javascript  theme={null}
// Read entire file as Uint8Array
const data = await Deno.readFile("/path/to/file.bin");
```

#### Read File Stream

```csharp  theme={null}
// Open a file for reading as a stream
const file = await Deno.open("/path/to/large-file.txt");
// Create a reader from the file
const reader = file.readable.getReader();
// Read chunks
const { value, done } = await reader.read();
// Close the file when done
file.close();
```

### Writing Files

#### Write Text Files

```javascript  theme={null}
// Write string to file (creates or overwrites)
await Deno.writeTextFile("/path/to/output.txt", "Hello, world!");
```

#### Write Binary Files

```javascript  theme={null}
// Write binary data to file
const data = new Uint8Array([104, 101, 108, 108, 111]);
await Deno.writeFile("/path/to/output.bin", data);
```

#### Append to Files

```javascript  theme={null}
// Append to an existing file
await Deno.writeTextFile("/path/to/log.txt", "New log entry\n", { append: true });
```

### File Operations

#### Check if File Exists

```javascript  theme={null}
try {
  const fileInfo = await Deno.stat("/path/to/file.txt");
  const exists = fileInfo.isFile; // true if it's a file
} catch (error) {
  if (error instanceof Deno.errors.NotFound) {
    // File does not exist
  } else {
    // Other error
  }
}
```

#### Copy Files

```javascript  theme={null}
await Deno.copyFile("/path/source.txt", "/path/destination.txt");
```

#### Rename/Move Files

```javascript  theme={null}
await Deno.rename("/path/oldname.txt", "/path/newname.txt");
```

#### Delete Files

```javascript  theme={null}
await Deno.remove("/path/to/file.txt");
```

### Directory Operations

#### Create Directory

```javascript  theme={null}
// Create a single directory
await Deno.mkdir("/path/to/dir");

// Create nested directories (like mkdir -p)
await Deno.mkdir("/path/to/nested/dir", { recursive: true });
```

#### Read Directory Contents

```javascript  theme={null}
// List files and directories in a directory
for await (const entry of Deno.readDir("/path/to/dir")) {
  console.log(entry.name, entry.isFile ? "file" : "directory");
}
```

#### Remove Directory

```javascript  theme={null}
// Remove empty directory
await Deno.remove("/path/to/empty-dir");

// Remove directory with contents
await Deno.remove("/path/to/dir", { recursive: true });
```

### File Information

#### Get File Stats

```javascript  theme={null}
const fileInfo = await Deno.stat("/path/to/file.txt");
console.log(fileInfo.size); // Size in bytes
console.log(fileInfo.mtime); // Last modification time
console.log(fileInfo.birthtime); // Creation time
console.log(fileInfo.isFile); // Is it a file
console.log(fileInfo.isDirectory); // Is it a directory
```

#### File Permissions

```javascript  theme={null}
// Check if we have read permission
const canRead = await Deno.permissions.query({ name: "read", path: "/path/to/file.txt" });
```

### Temporary Files and Directories

#### Create Temporary File

```javascript  theme={null}
// Create a temp file and return its path
const tempFile = await Deno.makeTempFile();
```

#### Create Temporary Directory

```javascript  theme={null}
// Create a temp directory and return its path
const tempDir = await Deno.makeTempDir();
```

### Working with Paths

Deno provides a `path` module for working with file paths:

```javascript  theme={null}
import { join, dirname, basename, extname } from "https://deno.land/std/path/mod.ts";

const filePath = join("dir", "subdir", "file.txt"); // OS-appropriate path joining
const dir = dirname("/path/to/file.txt"); // "/path/to"
const base = basename("/path/to/file.txt"); // "file.txt"
const ext = extname("/path/to/file.txt"); // ".txt"
```

### Important Notes for Xano Lambda Environment

1. In Xano's Lambda environment, filesystem operations are primarily useful for temporary file operations
2. Use the `/tmp` directory for temporary file storage
3. Files in the Lambda environment are ephemeral - they will not persist between function calls
4. Filesystem operations are useful for:
   * Processing uploaded files
   * Generating temporary files for processing
   * Creating logs or debug information


Built with [Mintlify](https://mintlify.com).