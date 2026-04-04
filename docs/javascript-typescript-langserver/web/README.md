# JavaScript/TypeScript Language Server

Source: https://github.com/sourcegraph/javascript-typescript-langserver

An implementation of the Language Server Protocol (LSP) for JavaScript and TypeScript that uses TypeScript's LanguageService to perform source code analysis.

[![npm](https://img.shields.io/npm/v/javascript-typescript-langserver.svg)](https://www.npmjs.com/package/javascript-typescript-langserver)
[![downloads](https://img.shields.io/npm/dm/javascript-typescript-langserver.svg)](https://www.npmjs.com/package/javascript-typescript-langserver)
[![build](https://travis-ci.org/sourcegraph/javascript-typescript-langserver.svg?branch=master)](https://travis-ci.org/sourcegraph/javascript-typescript-langserver)

## Important Note

This project is **no longer actively maintained** by Sourcegraph. The team recommends using:

- **Theia's TypeScript language server** (https://github.com/theia-ide/typescript-language-server) - A thinner wrapper around `tsserver`
- **Sourcegraph's cloud approach** (https://github.com/sourcegraph/sourcegraph-typescript) - Uses Theia's language server
- **Native LSP support for `tsserver`** - The official TypeScript language server (recommended)

The original approach of building a tight integration with TypeScript's APIs made it difficult to keep up with new TypeScript features and always required a bundled TypeScript version rather than using the local TypeScript in `node_modules`.

## Overview

This language server adheres to the [Language Server Protocol (LSP)](https://github.com/Microsoft/language-server-protocol/blob/master/protocol.md). It implements language intelligence features using TypeScript's LanguageService API.

## Core Features

- **Hovers** - Display type information and documentation on hover
- **Goto definition** - Navigate to symbol definitions
- **Goto type definition** - Jump to type definitions
- **Find all references** - Locate all uses of a symbol
- **Document symbols** - List symbols in the current document
- **Workspace symbol search** - Search for symbols across the workspace
- **Rename** - Rename symbols with refactoring
- **Completion** - Intelligent code completion
- **Signature help** - Display function signatures
- **Diagnostics** - Real-time error and warning reporting
- **Quick fixes** - Automated code fixes for common issues

## Try It Out

This language server has been integrated with:

- **sourcegraph.com** - Code intelligence on Sourcegraph
- **Visual Studio Code** - Via the vscode-javascript-typescript extension
- **Eclipse Che** - Cloud IDE integration
- **NeoVim** - Via LanguageClient-neovim plugin
- **Sublime Text** - Via LSP package

## Installation

Install from npm:

```bash
npm install -g javascript-typescript-langserver
```

Or as a dev dependency in your project:

```bash
npm install --save-dev javascript-typescript-langserver
```

## Running from Source

### Prerequisites

- Node.js >= 6.0.0
- npm or yarn

### Build Steps

```bash
# Install dependencies
npm install

# Compile TypeScript to JavaScript
npm run build
# or compile on file changes
npm run watch

# Run tests
npm test
```

## Running the Server

### Via STDIO

```bash
node lib/language-server-stdio
```

The server will read LSP messages from stdin and write responses to stdout.

### Via TCP

```bash
node lib/language-server
```

By default, the server listens on port 2089.

## Command Line Options

```
Usage: language-server [options]

Options:
  -h, --help            output usage information
  -V, --version         output the version number
  -s, --strict          enable strict mode
  -p, --port [port]     specify LSP port to use (default: 2089)
  -c, --cluster [num]   number of concurrent cluster workers
                        (defaults to number of CPUs)
  -t, --trace           print all requests and responses
  -l, --logfile [file]  log output to this file
  -j, --enable-jaeger   enable OpenTracing through Jaeger
```

### Example: Running on a Specific Port

```bash
node lib/language-server --port 3000
```

### Example: With Logging

```bash
node lib/language-server --logfile /var/log/js-ts-lsp.log
```

## LSP Extensions

This language server implements several custom LSP extensions (prefixed with `x`):

### Files Extension

Allows the server to request file contents without directly accessing the file system. Useful for cloud environments where files may not be available locally.

Reference: [extension-files.md](https://github.com/sourcegraph/language-server-protocol/blob/master/extension-files.md)

### SymbolDescriptor Extension

Get a SymbolDescriptor for a symbol and search the workspace for symbols or references to it.

Reference: [extension-workspace-references.md](https://github.com/sourcegraph/language-server-protocol/blob/master/extension-workspace-references.md)

### Streaming Extension

Supports streaming partial results for all endpoints through JSON Patches. Allows for progressive result delivery without waiting for the complete response.

Reference: [streaming protocol](https://github.com/sourcegraph/language-server-protocol/blob/streaming/protocol.md#partialResult)

### Packages Extension

Methods to get information about project dependencies and package metadata.

### TCP / Multiple Client Support

When running over TCP, the `exit` notification will not kill the process, but instead close the TCP socket. This allows multiple clients to connect to a single server instance.

## Versioning

This project follows [semver](http://semver.org/) with the following policy:

- Changes to command line arguments, Node version requirements, or protocol breaking changes result in a major version increase
- Standard LSP method behavior changes follow semantic versioning

## Performance Debugging with OpenTracing

The language server is fully instrumented with [OpenTracing](http://opentracing.io/), allowing you to debug performance issues and see which operations caused methods to take longer than expected.

### Setting up Jaeger Locally

For local development, the server includes built-in support for [Jaeger](http://jaeger.readthedocs.io/en/latest/), an open source OpenTracing implementation:

```bash
docker run -d -p5775:5775/udp -p6831:6831/udp -p6832:6832/udp \
  -p5778:5778 -p16686:16686 -p14268:14268 jaegertracing/all-in-one:latest
```

### Running with Jaeger

```bash
node lib/language-server --enable-jaeger
```

Then make requests from your client and open http://localhost:16686 in your browser to see method calls broken down into spans.

### Passing Span Context

You can pass a span context through an optional `meta` field on JSON RPC message objects:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/hover",
  "params": { /* ... */ },
  "meta": { /* span context */ }
}
```

## Development

### Running Tests

```bash
npm test
```

The test suite uses:
- Timeout: 7000ms
- Slow threshold: 2000ms

### Code Quality

The project enforces code quality through:

```bash
# Run all linters
npm run lint

# Run TSLint
npm run tslint

# Format code with Prettier
npm run prettier
```

### Watch Mode

For development with automatic recompilation:

```bash
npm run watch
```

## Contributing

This project follows the Sourcegraph contribution guidelines:

1. Fork the repository on GitHub
2. Create a topic branch from master
3. Make commits of logical units with proper formatting
4. Push changes to your fork
5. Submit a pull request to the original repository

### Commit Message Format

Commit messages should follow this format:

```
<subsystem>: <what changed>

<why this change was made>

Fixes #<issue-number>
```

The first line should be no longer than 70 characters.

### Certificate of Origin

By contributing, you agree to the Developer Certificate of Origin (DCO). See the [DCO file](DCO) for details.

## License

This project is licensed under the Apache 2.0 license. See [LICENSE](LICENSE) for details.

## Related Projects

- **TypeScript** - https://www.typescriptlang.org/
- **Language Server Protocol** - https://microsoft.github.io/language-server-protocol/
- **Theia IDE** - https://theia-ide.org/
- **Sourcegraph** - https://sourcegraph.com/

## Support

- **Issues** - Report bugs on GitHub: https://github.com/sourcegraph/javascript-typescript-langserver/issues
- **Chat** - Join the community on Gitter: https://gitter.im/sourcegraph/javascript-typescript-langserver
