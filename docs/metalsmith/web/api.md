# Source: https://metalsmith.io/api

Title: API reference

URL Source: https://metalsmith.io/api

Markdown Content:
[](https://metalsmith.io/api#typedefs)Typedefs
----------------------------------------------

[Metalsmith](https://metalsmith.io/api#Metalsmith) ⇒ `Metalsmith`
Initialize a new `Metalsmith` builder with a working `directory`.

[Files](https://metalsmith.io/api#Files) : `Object.<string, File>`
Metalsmith representation of the files in `metalsmith.source()`. The keys represent the file paths and the values are [File](https://metalsmith.io/api#File) objects

[File](https://metalsmith.io/api#File) : `Object`
Metalsmith file. Defines `mode`, `stats` and `contents` properties by default, but may be altered by plugins

[BuildCallback](https://metalsmith.io/api#BuildCallback) : `function`
A callback to run when the Metalsmith build is done

[DoneCallback](https://metalsmith.io/api#DoneCallback) : `function`
A callback to indicate that a plugin's work is done

[Plugin](https://metalsmith.io/api#Plugin) : `function`
A Metalsmith plugin is a function that is passed the file list, the metalsmith instance, and a `done` callback. Calling the callback is required for asynchronous plugins, and optional for synchronous plugins.

[Debugger](https://metalsmith.io/api#Debugger) : `function`
A [debug](https://github.com/debug-js/debug#readme)-based plugin debugger

[MatterOptions](https://metalsmith.io/api#MatterOptions) : `Object`
Options for parsing/stringifying front-and other matter

Initialize a new `Metalsmith` builder with a working `directory`.

**Kind**: global typedef

| Param | Type |
| --- | --- |
| directory | `string` |

**Properties**

| Name | Type |
| --- | --- |
| [plugins] | [`Array<Plugin>`](https://metalsmith.io/api#Plugin) |
| [ignores] | `Array<string>` |

*   [Metalsmith](https://metalsmith.io/api#Metalsmith) ⇒ [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.use(plugin)](https://metalsmith.io/api#Metalsmith+use) ⇒ [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.directory([directory])](https://metalsmith.io/api#Metalsmith+directory) ⇒ `string` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.metadata([metadata])](https://metalsmith.io/api#Metalsmith+metadata) ⇒ `Object` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.source([path])](https://metalsmith.io/api#Metalsmith+source) ⇒ `string` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.destination([path])](https://metalsmith.io/api#Metalsmith+destination) ⇒ `string` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.concurrency([max])](https://metalsmith.io/api#Metalsmith+concurrency) ⇒ `number` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.clean([clean])](https://metalsmith.io/api#Metalsmith+clean) ⇒ `boolean` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.frontmatter([frontmatter])](https://metalsmith.io/api#Metalsmith+frontmatter) ⇒ `boolean` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.watch([options])](https://metalsmith.io/api#Metalsmith+watch) ⇒ `boolean` | [`Chokidar.WatchOptions`](https://github.com/paulmillr/chokidar/blob/3.5.3/types/index.d.ts#L68) | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.ignore([files])](https://metalsmith.io/api#Metalsmith+ignore) ⇒ [`Metalsmith`](https://metalsmith.io/api#Metalsmith) | `Array.<string>`
    *   [.statik([paths])](https://metalsmith.io/api#Metalsmith+statik) ⇒ [`Files`](https://metalsmith.io/api#Files) | `void`
    *   [.path(...paths)](https://metalsmith.io/api#Metalsmith+path) ⇒ `string`
    *   [.match(patterns [, input [, options]])](https://metalsmith.io/api#Metalsmith+match) ⇒ `Array.<string>`
    *   [.imports(specifier [, namedExport])](https://metalsmith.io/api#Metalsmith+imports) ⇒ `Promise<*>`
    *   [.debug(namespace)](https://metalsmith.io/api#Metalsmith+debug) ⇒ [`Debugger`](https://metalsmith.io/api#Debugger)
    *   [.env([ vars [, value]])](https://metalsmith.io/api#Metalsmith+env) ⇒ `string` | `number` | `boolean` | `Object` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)
    *   [.build([callback])](https://metalsmith.io/api#Metalsmith+build) ⇒ [`Promise.<Files>`](https://metalsmith.io/api#Files) | `void`
    *   [.process([callback])](https://metalsmith.io/api#Metalsmith+process) ⇒ [`Promise.<Files>`](https://metalsmith.io/api#Files) | `void`
    *   [.run(files, plugins)](https://metalsmith.io/api#Metalsmith+run) ⇒ [`Promise.<Files>`](https://metalsmith.io/api#Files) | `void`
    *   [.matter](https://metalsmith.io/api#Metalsmith+matter)
        *   [.parse(contents)](https://metalsmith.io/api#Metalsmith+matter+parse) ⇒ [`File`](https://metalsmith.io/api#File) | `void`
        *   [.stringify(file)](https://metalsmith.io/api#Metalsmith+matter+stringify) ⇒ `string`
        *   [.wrap(stringifiedData)](https://metalsmith.io/api#Metalsmith+matter+wrap) ⇒ `string`

### [](https://metalsmith.io/api#Metalsmith+use)metalsmith.use(plugin) ⇒ [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Add a `plugin` function to the stack.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [plugin] | [`plugin`](https://metalsmith.io/api#Plugin) |

**Example**

```
metalsmith
 .use(drafts())   // use the drafts plugin
 .use(markdown()) // use the markdown plugin
```

### [](https://metalsmith.io/api#Metalsmith+directory)metalsmith.directory([directory]) ⇒ `string` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set the working `directory`.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [directory] | `string` |

**Example**

```
new Metalsmith('.')                   // set the path of the working directory through the constructor
metalsmith.directory()                // returns '.'
metalsmith.directory('./other/path')  // set the path of the working directory
```

### [](https://metalsmith.io/api#Metalsmith+metadata)metalsmith.metadata([metadata]) ⇒ `Object` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set the global `metadata`.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [metadata] | `Object` |

**Example**

```
metalsmith.metadata({ sitename: 'My blog' });  // set metadata
metalsmith.metadata()                          // returns { sitename: 'My blog' }
```

### [](https://metalsmith.io/api#Metalsmith+source)metalsmith.source([path]) ⇒ `string` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set the source directory.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [path] | `string` |

**Example**

```
metalsmith.source('./src');    // set source directory
metalsmith.source()            // returns './src'
```

### [](https://metalsmith.io/api#Metalsmith+destination)metalsmith.destination([path]) ⇒ `string` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set the destination directory.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [path] | `string` |

**Example**

```
metalsmith.destination('build'); // set destination
metalsmith.destination()         // returns 'build'
```

### [](https://metalsmith.io/api#Metalsmith+concurrency)metalsmith.concurrency([max]) ⇒ `number` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set the maximum number of files to open at once.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [max] | `number` |

**Example**

```
metalsmith.concurrency(20)   // set concurrency to max 20
metalsmith.concurrency()     // returns 20
```

### [](https://metalsmith.io/api#Metalsmith+clean)metalsmith.clean([clean]) ⇒ `boolean` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set whether the destination directory will be removed before writing.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [clean] | `boolean` |

**Example**

```
metalsmith.clean(true)  // clean the destination directory
metalsmith.clean()      // returns true
```

### [](https://metalsmith.io/api#Metalsmith+frontmatter)metalsmith.frontmatter([frontmatter]) ⇒ `boolean` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Optionally turn off frontmatter parsing or pass a [gray-matter options object](https://github.com/jonschlinkert/gray-matter/tree/4.0.2#option)

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [frontmatter] | `boolean` | [`GrayMatterOptions`](https://github.com/jonschlinkert/gray-matter/tree/4.0.2#option) |

**Example**

```
metalsmith.frontmatter(false)  // turn off front-matter parsing
metalsmith.frontmatter()       // returns false
metalsmith.frontmatter({ excerpt: true })
```

### [](https://metalsmith.io/api#Metalsmith+watch)metalsmith.watch([options]) ⇒ `boolean` | [`Chokidar.WatchOptions`](https://github.com/paulmillr/chokidar/blob/3.5.3/types/index.d.ts#L68) | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Partial rebuilding (=using `metalsmith.watch` with `metalsmith.clean(false)`) is still experimental and combined with `@metalsmith/metadata`<= 0.2.0 a bug may trigger an infinite loop. metalsmith.watch is incompatible with existing watch plugin. In watch mode, metalsmith.process/build are **not awaitable**. Callbacks passed to these methods will run on every rebuild instead of running once at the build's end.

Set the list of paths to watch and trigger rebuilds on. The watch method will skip files ignored with `metalsmith.ignore()` and will do partial (true) or full (false) rebuilds depending on the `metalsmith.clean()` setting. It can be used both for rebuilding in-memory with `metalsmith.process` or writing to file system with `metalsmith.build`.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type | Description |
| --- | --- | --- |
| [options] | `boolean` | `string` | `Array.<string>` | `Chokidar.WatchOptions` | If string or array of strings, the directory path(s) to watch. If `true` or `false`, will (not) watch [Metalsmith.source()](https://metalsmith.io/api#Metalsmith+source). Alternatively an object of Chokidar watchOptions, except `cwd`, `ignored`, `alwaysStat`, `ignoreInitial`, and `awaitWriteFinish`. These options are controlled by Metalsmith. |

**Example**

```
metalsmith
  .ignore(['wont-be-watched'])  // ignored
  .clean(false)                 // do partial rebuilds
  .watch(true)                  // watch all files in metalsmith.source()
  .watch(['lib','src'])         // or watch files in directories 'lib' and 'src'

if (process.argv[2] === '--dry-run') {
  metalsmith.process(onRebuild) // reprocess in memory without writing to disk
} else {
  metalsmith.build(onRebuild)   // rewrite to disk
}

function onRebuild(err, files) {
  if (err) {
    metalsmith.watch(false)            // stop watching
     .finally(() => console.log(err))  // and log build error
  }
  console.log('reprocessed files', Object.keys(files).join(', '))
}
```

### [](https://metalsmith.io/api#Metalsmith+ignore)metalsmith.ignore([files]) ⇒ [`Metalsmith`](https://metalsmith.io/api#Metalsmith) | `Array.<string>`

Get or set the list of filepaths or glob patterns to ignore

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type | Description |
| --- | --- | --- |
| [files] | `string` | `Array.<string>` | The names or glob patterns of files or directories to ignore. |

**Example**

```
metalsmith.ignore()                      // return a list of ignored file paths
metalsmith.ignore('layouts')             // ignore the layouts directory
metalsmith.ignore(['.*', 'data.json'])   // ignore dot files & a data file
```

### [](https://metalsmith.io/api#Metalsmith+statik)metalsmith.statik([paths]) ⇒ [`Files`](https://metalsmith.io/api#Files) | `void`

Get or set files to consider static, i.e. that should be copied to `metalsmith.destination()` without being processed by plugins.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

**Returns**: a regular Metalsmith [Files](https://metalsmith.io/api#Files) object, with the difference that the files' `stats`,`mode` and `contents` are read-only and `contents.toString()` contains the original file path of the file relative to [Metalsmith.source](https://metalsmith.io/api#Metalsmith+source)

| Param | Type | Description |
| --- | --- | --- |
| [paths] | `string` | `Array.<string>` | The names or glob patterns of files or directories to consider static. |

**Example**

```
metalsmith.statik(["assets","CNAME","api/static"]);
const statik = metalsmith.statik()
statik['library.css'].contents.toString() // 'library.css'
```

### [](https://metalsmith.io/api#Metalsmith+path)metalsmith.path(...paths) ⇒ `string`

Resolve `paths` relative to the metalsmith `directory`.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| ...paths | `string` |

**Example**

```
metalsmith.path('./path','to/file.ext')
```

### [](https://metalsmith.io/api#Metalsmith+match)metalsmith.match(patterns [, input [,options]]) ⇒ `Array.<string>`

Match filepaths in the source directory by [glob](https://en.wikipedia.org/wiki/Glob_(programming)) pattern. If `input` is not specified, patterns are matched against `Object.keys(files)`

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

**Returns**: `Array.<string>` - An array of matching file paths

| Param | Type | Description |
| --- | --- | --- |
| patterns | `string` | `Array.<string>` | One or more [glob](https://en.wikipedia.org/wiki/Glob_(programming) patterns |
| [input] | `Array.<string>` | Array of paths to match patterns to |
| [options] | [`micromatch.Options`](https://github.com/micromatch/micromatch#options) | [Micromatch options](https://github.com/micromatch/micromatch#options) |

### [](https://metalsmith.io/api#Metalsmith+imports)metalsmith.imports(specifier[, namedExport]) ⇒ `Promise<*>`

Like Javascript's dynamic `import()`, with CJS/ESM support for loading default exports, all or a single named export, and JSON files.

Relative paths are resolved against `metalsmith.directory()`.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

**Returns**: `Promise.<*>` - a JS/JSON module

| Param | Type | Description |
| --- | --- | --- |
| specifier | `string` | Any specifier you would pass to import/require* |
| [namedExport] | `string` | Return only a single named export |

**Example**

```
* await metalsmith.imports('metalsmith') // Metalsmith
 * await metalsmith.imports('./data.json')  // object
 * await metalsmith.imports('./helpers/index.js', 'formatDate')  // function
```

### [](https://metalsmith.io/api#Metalsmith+env)metalsmith.env([vars [, value]]) ⇒ `string` | `number` | `boolean` | `Object` | [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

Get or set one or multiple metalsmith environment variables. Metalsmith env vars are case-insensitive.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type | Description |
| --- | --- | --- |
| [vars] | `string` | `Object` | Name of the environment variable, or an object with `{ name: <value> }` pairs |
| [value] | `string` | `number` | `boolean` | Value of the environment variable |

**Example**

```
// pass all Node env variables
metalsmith.env(process.env)
// get all env variables
metalsmith.env()
// get DEBUG env variable
metalsmith.env('DEBUG')
// set DEBUG env variable (chainable)
metalsmith.env('DEBUG', '*')
// set multiple env variables at once (chainable)
// this does not clear previously set variables
metalsmith.env({
  DEBUG: false,
  NODE_ENV: 'development'
})
```

### [](https://metalsmith.io/api#Metalsmith+debug)metalsmith.debug(namespace) ⇒ [`Debugger`](https://metalsmith.io/api#Debugger)

Create a new [debug](https://github.com/debug-js/debug#readme) debugger

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type | Description |
| --- | --- | --- |
| namespace | `string` | Debugger namespace |

**Example**

```
function plugin(files, metalsmith) {
  const debug = metalsmith.debug('metalsmith-myplugin')
  debug('a debug log')    // logs 'metalsmith-myplugin a debug log'
  debug.warn('A warning') // logs 'metalsmith-myplugin:warn A warning'
}
```

### [](https://metalsmith.io/api#Metalsmith+build)metalsmith.build([callback]) ⇒ [`Promise.<Files>`](https://metalsmith.io/api#Files) | `void`

Build with the current settings to the destination directory.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

**Fulfills**: [`Files`](https://metalsmith.io/api#Files)

**Rejects**: `Error`

| Param | Type |
| --- | --- |
| [callback] | [`BuildCallback`](https://metalsmith.io/api#BuildCallback) |

**Example**

```
// callback variant
metalsmith.build(function(error, files) {
  if (error) throw error
  console.log('Build success!')
})

// promise variant
try {
  const files = await metalsmith.build()
  console.log('Build success')
} catch (error) {
  throw error
}
```

### [](https://metalsmith.io/api#Metalsmith+process)metalsmith.process([callback]) ⇒ [`Promise.<Files>`](https://metalsmith.io/api#Files) | `void`

Process files through plugins without writing out files.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

**Fulfills**: [`Files`](https://metalsmith.io/api#Files)

**Rejects**: `Error`

| Param | Type |
| --- | --- |
| [callback] | [`BuildCallback`](https://metalsmith.io/api#BuildCallback) |

**Example**

```
// callback variant
metalsmith.process(err => {
  if (err) throw err
  console.log('Success')
})

// promise variant
try {
  await metalsmith.process()
  console.log('Success')
} catch (err) {
  throw err
}
```

### [](https://metalsmith.io/api#Metalsmith+run)metalsmith.run(files, plugins) ⇒ `Object`

Run a set of `files` through the plugins stack.

**Kind**: instance method of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

**Access**: package

| Param | Type |
| --- | --- |
| files | [`files`](https://metalsmith.io/api#Files) |
| plugins | [`Array<Plugin>`](https://metalsmith.io/api#Plugin) |

**Kind**: instance member of [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

### [](https://metalsmith.io/api#Metalsmith+matter+parse)metalsmith.matter.options([options]) ⇒ `void` | [`MatterOptions`](https://metalsmith.io/api#MatterOptions)

Get or set options for parsing & stringifying matter

**Kind**: instance method of [`Metalsmith.matter`](https://metalsmith.io/api#Metalsmith+matter)

| Param | Type |
| --- | --- |
| [options] | [`MatterOptions`](https://metalsmith.io/api#MatterOptions) |

**Example**

```
metalsmith.matter.parse(Buffer.from('---\ntitle: Hello World\n---\nIntro\n---')) === {
  contents: Buffer<'Hello world'>,
  title: 'Hello World',
  excerpt: 'Intro'
}
```

### [](https://metalsmith.io/api#metalsmithmatterparsefile-%E2%87%92--file)metalsmith.matter.parse(file) ⇒ [`File`](https://metalsmith.io/api#File)

Parse a string for front matter and return it as a [`File`](https://metalsmith.io/api#File) object.

**Kind**: instance method of [`Metalsmith.matter`](https://metalsmith.io/api#Metalsmith+matter)

| Param | Type |
| --- | --- |
| file | [`Buffer`](https://nodejs.org/api/buffer.html) | `string` |

**Example**

```
metalsmith.matter.parse(Buffer.from('---\ntitle: Hello World\n---\nIntro\n---')) === {
  contents: Buffer<'Hello world'>,
  title: 'Hello World',
  excerpt: 'Intro'
}
```

### [](https://metalsmith.io/api#Metalsmith+matter+stringify)metalsmith.matter.stringify(file) ⇒ `string`

Stringify a [`File`](https://metalsmith.io/api#File) object to a string with frontmatter and contents

**Kind**: instance method of [`Metalsmith.matter`](https://metalsmith.io/api#Metalsmith+matter)

| Param | Type |
| --- | --- |
| contents | [`File`](https://metalsmith.io/api#File) |

**Example**

```
metalsmith.matter.stringify({
  contents: Buffer.from('body'),
  title: 'Hello World',
  excerpt: 'Intro'
}) === [
  'title: Hello World',
  'excerpt: Intro',
  '---',
  'body'
].join('\n')
```

### [](https://metalsmith.io/api#Metalsmith+matter+wrap)metalsmith.matter.wrap(stringifiedData) ⇒ `string`

Wrap stringified front-matter-compatible data with the matter delimiters

**Kind**: instance method of [`Metalsmith.matter`](https://metalsmith.io/api#Metalsmith+matter)

| Param | Type |
| --- | --- |
| stringifiedData | [`Buffer`](https://nodejs.org/api/buffer.html) |`string` |

**Example**

```
metalsmith.matter.wrap(Buffer.from('{"hello": "world"}')) === '---\n{"hello": "world"}\n---'
```

[](https://metalsmith.io/api#Files)Files : `Object.<string, File>`
------------------------------------------------------------------

Metalsmith representation of the files in `metalsmith.source()`. The keys represent the file paths and the values are [File](https://metalsmith.io/api#File) objects

**Kind**: global typedef

[](https://metalsmith.io/api)

[](https://metalsmith.io/api#File)File
--------------------------------------

Metalsmith file. Defines `mode`, `stats` and `contents` properties by default, but may be altered by plugins

**Kind**: global typedef

**Properties**

| Name | Type | Description |
| --- | --- | --- |
| contents | [`Buffer`](https://nodejs.org/api/buffer.html) | A NodeJS [Buffer](https://nodejs.org/api/buffer.html) that can be `.toString`'ed to obtain its human-readable contents |
| stats | [`fs.Stats`](https://nodejs.org/api/fs.html#fs_class_fs_stats) | A NodeJS [fs.Stats object](https://nodejs.org/api/fs.html#fs_class_fs_stats) with extra filesystem metadata and methods |
| mode | `string` | [Octal permission mode](https://en.wikipedia.org/wiki/File-system_permissions#Numeric_notation) |

[](https://metalsmith.io/api#BuildCallback)BuildCallback : `function`
---------------------------------------------------------------------

A callback to run when the Metalsmith build is done

**Kind**: global typedef

**this**: [`Metalsmith`](https://metalsmith.io/api#Metalsmith)

| Param | Type |
| --- | --- |
| [error] | [`Error`](https://nodejs.org/api/errors.html#class-error) |
| files | [`Files`](https://metalsmith.io/api#Files) |

**Example**

```
function onBuildEnd(error, files) {
  if (error) throw error
  console.log('Build success')
}
```

[](https://metalsmith.io/api#DoneCallback)DoneCallback : `function`
-------------------------------------------------------------------

A callback to indicate that a plugin's work is done

**Kind**: global typedef

| Param | Type |
| --- | --- |
| [error] | [`Error`](https://nodejs.org/api/errors.html#class-error) |

**Example**

```
function plugin(files, metalsmith, done) {
  // ..do stuff
  done()
}
```

[](https://metalsmith.io/api#Plugin)Plugin : `function`
-------------------------------------------------------

A Metalsmith plugin is a function that is passed the file list, the metalsmith instance, and a `done` callback. Calling the callback is required for asynchronous plugins, and optional for synchronous plugins.

**Kind**: global typedef

| Param | Type |
| --- | --- |
| files | [`Files`](https://metalsmith.io/api#Files) |
| metalsmith | [`Metalsmith`](https://metalsmith.io/api#Metalsmith) |
| done | [`DoneCallback`](https://metalsmith.io/api#DoneCallback) |

**Example**

```
function drafts(files, metalsmith) {
  Object.keys(files).forEach(path => {
    if (files[path].draft) {
      delete files[path]
    }
  })
}

metalsmith.use(drafts)
```

[](https://metalsmith.io/api#Debugger)Debugger : `function`
-----------------------------------------------------------

A [debug](https://github.com/debug-js/debug#readme)-based plugin debugger with `warn`, `info` and `error` channels.

**Kind**: global typedef

| Param | Type | Description |
| --- | --- | --- |
| message | `string` | Debug message, including [formatter placeholders](https://github.com/debug-js/debug#formatters) and an additional `%b` (buffer) formatter |
| ...args | `any` | Arguments to fill the formatter placeholders with |

**Example**

```
const createDebugger = require('metalsmith/lib/debug')
const debugger = createDebugger('metalsmith-myplugin')
debugger('A message')
```

**Methods**

| Name | Type | Description |
| --- | --- | --- |
| warn | `function` | Log a warning. Same signature as main debug function |
| error | `function` | Log an error. Same signature as main debug function |
| info | `function` | Log an informational message. Same signature as main debug function |

**Example**

```
const createDebugger = require('metalsmith/lib/debug')
const debugger = createDebugger('metalsmith-myplugin')
debugger.error('An error')
debugger.warn('A warning')
debugger.info('File contents: %b', Buffer.from('custom'))
```

[](https://metalsmith.io/api#matteroptions-object)MatterOptions: `Object`
-------------------------------------------------------------------------

[Gray matter options](https://github.com/jonschlinkert/gray-matter#options)

**Kind**: global typedef

| Param | Type |
| --- | --- |
| language | `string` |
| excerpt | `boolean` | `function` |
| excerpt_separator | `string` |
| delimiters | `string` | `string[]` |
| engines | `Object<string, { parse: Function[, stringify: Function] }>` |
