# Source: https://parceljs.org/plugin-system/logging/

Title: Diagnostics and Logging

URL Source: https://parceljs.org/plugin-system/logging/

Markdown Content:
Parcel includes support for rich diagnostics that are used to describe errors and warnings in a format-agnostic way. It also includes a built in logging system that allows Reporter plugins to handle all logs and errors and present them to the user.

Diagnostics
-----------

[#](https://parceljs.org/plugin-system/logging/#diagnostics)
A [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) is a JavaScript object with a set of properties that are required to create a useful log message. This can be anything from a verbose message to a warning or error. Diagnostics can include a message, information about the file being processed, a code frame, error information, hints on how to potentially resolve the issue, and a link to documentation to learn more.

The `ThrowableDiagnostic` class in the `@parcel/diagnostic` package extends the JavaScript `Error` object with support for diagnostics. When throwing an error within your plugin, use a `ThrowableDiagnostic` object to attach a diagnostic with context about the error. Parcel will automatically attach your plugin name as the origin of the diagnostic.

`import ThrowableDiagnostic from '@parcel/diagnostic';throw new ThrowableDiagnostic({  diagnostic: {    message: 'An error occurred'  }});`
You can also throw multiple diagnostics at once by passing an array to the `diagnostic` option of a `ThrowableDiagnostic`.

### Formatting messages

[#](https://parceljs.org/plugin-system/logging/#formatting-messages)
To format the messages in a diagnostic, a very minimal version of Markdown is supported. This format has been specifically built to be compatible with terminals and other render targets such as browsers and editors, while also not being too cryptic when displayed without any formatting. `@parcel/reporter-cli` uses the `@parcel/markdown-ansi` library to convert these Markdown strings to ANSI escape sequences for rendering in a terminal.

The supported Markdown features are `**bold**`, `*italic*`/`_italic_`, `__underline__` and `~~strikethrough~~`.

The `@parcel/diagnostic` package includes some utilities for working with Markdown messages. The `md` tagged template literal handles escaping any interpolated expressions within Markdown strings. This ensures that any special Markdown characters within expressions do not affect the formatting.

`import {md} from '@parcel/diagnostic';throw new ThrowableDiagnostic({  diagnostic: {    message: md`**Error**: Could not parse ${filePath}`  }});`
There are also utilities for formatting interpolated expressions, including `md.bold`, `md.italic`, `md.underline`, and `md.strikethrough`.

`import {md} from '@parcel/diagnostic';throw new ThrowableDiagnostic({  diagnostic: {    message: md`**Error**: Could not parse ${md.underline(filePath)}`  }});`
### Code frames

[#](https://parceljs.org/plugin-system/logging/#code-frames)
A [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) can have one or more code frames attached. A code frame includes a file path along with one or more code highlights, which give context about where in a file an error occurred. Code highlights are defined by the line and column position within the file, and may also have a message to be displayed at that position.

Code frames should also include the source code for the file the error occurred in. If omitted, Parcel will read the file from the file system. However, in many cases the input source code may have come from another plugin that ran before, so the code will have been modified in some way. Including the code in the code frame avoids this issue.

`throw new ThrowableDiagnostic({  diagnostic: {    message: md`Could not parse ${asset.filePath}`,    codeFrames: [{      filePath: asset.filePath,      code: await asset.getCode(),      codeHighlights: [        {          start: {            line: 1,            column: 5,          },          end: {            line: 2,            column: 3,          },          message: 'Expected a string but got a number'        }      ]    }]  }});`
### Hints

[#](https://parceljs.org/plugin-system/logging/#hints)
Diagnostics can also include hints about how to fix a problem, and a link to documentation for users to learn more. These are provided via the `hints` and `documentationURL` properties.

`throw new ThrowableDiagnostic({  diagnostic: {    message: 'Could not find a config file',    hints: ['Create a tool.config.json file in the project root.'],    documentationURL: 'http://example.com/'  }});`
Logger
------

[#](https://parceljs.org/plugin-system/logging/#logger)
Parcel's logger can be used to log messages in plugins. Every function of a plugin is passed a [`Logger`](https://parceljs.org/plugin-system/logging/#PluginLogger) instance as a parameter. This instance has all the information Parcel needs to identify your plugin as the origin of the message.

The logger accepts [diagnostics](https://parceljs.org/plugin-system/logging/#diagnostics), which are JavaScript objects with a standardized set of properties that describe the log message, its origin, and context such as a code frame. [Reporter](https://parceljs.org/plugin-system/reporter/) plugins use this information to log your message while having complete freedom over how this data is formatted and displayed.

A [`Logger`](https://parceljs.org/plugin-system/logging/#PluginLogger) has a function for each log level, including `verbose`, `info`, `log`, `warn` and `error`. These log levels specify the severity of log messages, which is useful for formatting and filtering. For example, the [`--log-level`](https://parceljs.org/features/cli/#parameters) CLI option can be used to choose which messages you want to see. Each logging function also has a single parameter, which can either be a single [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) object or an array of diagnostics, depending on how many messages you want to log.

**Note**: The results of Parcel plugins are cached. This means any logs or warnings that a plugin emits will only be shown during a rebuild, and not when cached.

### Log levels

[#](https://parceljs.org/plugin-system/logging/#log-levels)

| Level | When to use | function(s) |
| --- | --- | --- |
| verbose | Use this when you want to log anything that can be used for debugging issues, while not being particularly interesting for normal usage. | `logger.verbose(...)` |
| info | Use this to log any information that is not related to a problem. | `logger.info(...)` or `logger.log(...)` |
| warning | Use this to log anything related to a problem that is not critical. | `logger.warning(...)` |
| error | Use this to log any critical issues. You may want to throw a [`ThrowableDiagnostic`](https://parceljs.org/plugin-system/logging/#ThrowableDiagnostic) instead to cause the build to fail. | `logger.error(...)` or `throw ThrowableDiagnostic(...)` |

### How to log a message

[#](https://parceljs.org/plugin-system/logging/#how-to-log-a-message)
Once you're familiar with the [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) format, you can log anything you want, from verbose messages to errors with code frames and hints. This example shows how to log a warning, complete with a code frame, hints, and a documentation URL.

`import {Transformer} from '@parcel/plugin';export default new Transformer({  async transform({asset, logger}) {    // ...    logger.warn({      message: 'This feature is deprecated.',      codeFrames: [{        filePath: asset.filePath,        code: await asset.getCode(),        codeHighlights: [{          start: {            line: 1,            column: 5          },          end: {            line: 1,            column: 10          }        }]      }],      hints: ['Please use this other feature instead.'],      documentationURL: 'http://example.com/'    });  },});`
Automatically collected logs and errors
---------------------------------------

[#](https://parceljs.org/plugin-system/logging/#automatically-collected-logs-and-errors)
Parcel automatically collects any logs created with `console.log` and other `console` methods. Whenever `console.log` is called, Parcel catches this, converts it to a [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic) object, and sends it to [Reporter](https://parceljs.org/plugin-system/reporter/) plugins just like it does with messages sent to the `logger`. However, this is not recommended since Parcel does not have as much information as when calling the `logger` directly.

Parcel also handles any errors that are thrown within plugins. These are converted into a [`Diagnostic`](https://parceljs.org/plugin-system/logging/#Diagnostic), and information about about the plugin is added to it. Errors that are thrown are sent to [Reporter](https://parceljs.org/plugin-system/reporter/) plugins, and the build is halted.

### API

[#](https://parceljs.org/plugin-system/logging/#api)

#### PluginLogger[_parcel/packages/core/logger/src/Logger.js:90_](https://github.com/parcel-bundler/parcel/blob/0b7187b63729ff1020d0e620967a811c8272ad45/packages/core/logger/src/Logger.js#L90)

`interface PluginLogger {``verbose(diagnostic: DiagnosticWithoutOrigin | Array<DiagnosticWithoutOrigin>): void,``info(diagnostic: DiagnosticWithoutOrigin | Array<DiagnosticWithoutOrigin>): void,``log(diagnostic: DiagnosticWithoutOrigin | Array<DiagnosticWithoutOrigin>): void,``warn(diagnostic: DiagnosticWithoutOrigin | Array<DiagnosticWithoutOrigin>): void,``error(input: Diagnostifiable | DiagnosticWithoutOrigin | Array<DiagnosticWithoutOrigin>): void,``}`
##### Referenced by:

[Bundler](https://parceljs.org/plugin-system/bundler/#Bundler), [Compressor](https://parceljs.org/plugin-system/compressor/#Compressor), [DedicatedThreadValidator](https://parceljs.org/plugin-system/validator/#DedicatedThreadValidator), [MultiThreadValidator](https://parceljs.org/plugin-system/validator/#MultiThreadValidator), [Namer](https://parceljs.org/plugin-system/namer/#Namer), [Optimizer](https://parceljs.org/plugin-system/optimizer/#Optimizer), [Packager](https://parceljs.org/plugin-system/packager/#Packager), [Reporter](https://parceljs.org/plugin-system/reporter/#Reporter), [Resolver](https://parceljs.org/plugin-system/resolver/#Resolver), [Runtime](https://parceljs.org/plugin-system/runtime/#Runtime), [Transformer](https://parceljs.org/plugin-system/transformer/#Transformer)

#### DiagnosticCodeFrame[_parcel/packages/core/diagnostic/src/diagnostic.js:33_](https://github.com/parcel-bundler/parcel/blob/0b7187b63729ff1020d0e620967a811c8272ad45/packages/core/diagnostic/src/diagnostic.js#L33)

Describes how to format a code frame. A code frame is a visualization of a piece of code with a certain amount of code highlights that point to certain chunk(s) inside the code.

`type DiagnosticCodeFrame = {|``code?: string,`
The contents of the source file. 

If no code is passed, it will be read in from filePath, remember that the asset's current code could be different from the input contents.

`filePath?: string,`
Path to the file this code frame is about (optional, absolute or relative to the project root)

`language?: string,`
Language of the file this code frame is about (optional)

`codeHighlights: Array<DiagnosticCodeHighlight>,``|}`
##### Referenced by:

[Diagnostic](https://parceljs.org/plugin-system/logging/#Diagnostic)

#### Diagnostic[_parcel/packages/core/diagnostic/src/diagnostic.js:53_](https://github.com/parcel-bundler/parcel/blob/0b7187b63729ff1020d0e620967a811c8272ad45/packages/core/diagnostic/src/diagnostic.js#L53)

A style agnostic way of emitting errors, warnings and info. Reporters are responsible for rendering the message, codeframes, hints, ...

`type Diagnostic = {|``message: string,`
This is the message you want to log.

`origin?: string,`
Name of plugin or file that threw this error

`stack?: string,`
A stacktrace of the error (optional)

`name?: string,`
Name of the error (optional)

`codeFrames?: ?Array<DiagnosticCodeFrame>,`
A code frame points to a certain location(s) in the file this diagnostic is linked to (optional)

`hints?: Array<string>,`
An optional list of strings that suggest ways to resolve this issue

`documentationURL?: string,`
A URL to documentation to learn more about the diagnostic.

`|}`
##### Referenced by:

[BuildFailureEvent](https://parceljs.org/plugin-system/reporter/#BuildFailureEvent), [DiagnosticLogEvent](https://parceljs.org/plugin-system/reporter/#DiagnosticLogEvent), [DiagnosticWithoutOrigin](https://parceljs.org/plugin-system/logging/#DiagnosticWithoutOrigin), [Diagnostifiable](https://parceljs.org/plugin-system/logging/#Diagnostifiable), [ResolveResult](https://parceljs.org/plugin-system/resolver/#ResolveResult), [ThrowableDiagnostic](https://parceljs.org/plugin-system/logging/#ThrowableDiagnostic), [ThrowableDiagnosticOpts](https://parceljs.org/plugin-system/logging/#ThrowableDiagnosticOpts), [ValidateResult](https://parceljs.org/plugin-system/validator/#ValidateResult), [anyToDiagnostic](https://parceljs.org/plugin-system/logging/#anyToDiagnostic), [errorToDiagnostic](https://parceljs.org/plugin-system/logging/#errorToDiagnostic)
