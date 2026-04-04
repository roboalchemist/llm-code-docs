# VSCode Language Server - Node

Source: https://github.com/microsoft/vscode-languageserver-node

Microsoft's Node.js-based Language Server Protocol (LSP) implementation framework, containing the core npm modules for building language servers and clients for Visual Studio Code.

## Overview

This repository contains the code for the following npm modules:

- **vscode-languageclient**: npm module to talk to a VSCode language server from a VSCode extension
- **vscode-languageserver**: npm module to implement a VSCode language server using Node.js as a runtime
- **vscode-languageserver-textdocument**: npm module to implement text documents usable in a LSP server using Node.js
- **vscode-languageserver-protocol**: the actual language server protocol definition in TypeScript
- **vscode-languageserver-types**: data types used by the language server client and server
- **vscode-jsonrpc**: the underlying message protocol to communicate between a client and a server

All npm modules are built using one Azure Pipeline and are available on npm registry.

## Getting Started

For a detailed document on how to use these npm modules to implement language servers for VSCode, see the official documentation at https://code.visualstudio.com/docs/extensions/example-language-server

### Setting Up the Repository

After cloning the repository, run the following commands to install dependencies and link packages:

```bash
npm install
npm run symlink
```

The `symlink` command points packages in this repository to each other, allowing for local development and testing across multiple packages.

## Core Packages

### vscode-languageclient

The client-side library that allows VSCode extensions to communicate with language servers adhering to the Language Server Protocol.

**NPM:** `vscode-languageclient`

**Key Features:**
- Easy integration of language servers into VSCode extensions
- Support for request/response and notification messaging patterns
- Middleware system for intercepting and modifying messages
- Error handling and server restart mechanisms
- Support for multiple transport types

### vscode-languageserver

The server-side library that implements the Language Server Protocol for Node.js runtimes.

**NPM:** `vscode-languageserver`

**Key Features:**
- Full LSP 3.x support
- Request and notification handlers
- Document synchronization (incremental and full)
- Configuration management
- Workspace symbols and document symbols
- Code actions, diagnostics, and formatting support

### vscode-languageserver-protocol

Tool-independent implementation of the LSP definition in TypeScript.

**NPM:** `vscode-languageserver-protocol`

**Key Features:**
- Protocol definitions aligned with LSP specification
- Type-safe interfaces for all protocol messages
- Support for proposed protocol features
- Can be used in any Node.js application

### vscode-languageserver-types

Shared data types used by both client and server implementations.

**NPM:** `vscode-languageserver-types`

**Key Types:**
- `Position`, `Range`, `Location`
- `TextDocument`, `TextDocumentIdentifier`
- `Diagnostic`, `DiagnosticSeverity`
- `CompletionItem`, `CompletionList`
- `Hover`, `SymbolInformation`
- `CodeLens`, `CodeAction`
- `DocumentSymbol`, `SymbolKind`

### vscode-languageserver-textdocument

Provides a standard text document implementation with incremental update capabilities.

**NPM:** `vscode-languageserver-textdocument`

**Features:**
- Incremental text document synchronization
- Line and character position tracking
- Full document access with offset calculations
- Used as prerequisite for modern LSP servers

### vscode-jsonrpc

Base messaging protocol for client-server communication using JSON-RPC.

**NPM:** `vscode-jsonrpc`

**Key Features:**
- JSON-RPC 2.0 protocol implementation
- Support for stdio, node IPC, and socket transports
- Request/response with correlation handling
- Notification messaging
- Connection lifecycle management

## Transport Types

The LSP implementation supports multiple transport mechanisms:

- **stdio** (standard input/output)
- **Node IPC** (inter-process communication)
- **Socket files** (named pipes, Unix domain sockets)
- **TCP connections**
- **Web sockets** (for browser-based clients)

## Architecture

The library is structured with three layers:

1. **Common Layer** - Protocol definitions and shared types
2. **Node Layer** - Node.js specific implementations (stdio, IPC, sockets)
3. **Browser Layer** - Browser compatible implementations (web sockets)

This three-tier architecture allows the same code to run in multiple environments:

```typescript
// Common code (protocol definitions)
import { RequestType } from 'vscode-languageserver-protocol';

// Node-specific code
import { createMessageConnection } from 'vscode-jsonrpc/node';

// Browser-specific code
import { createWebSocketMessageReader } from 'vscode-languageserver/browser';
```

## LSP Server Example

Basic structure of a language server:

```typescript
import {
  createConnection,
  TextDocuments,
  ProposedFeatures,
  TextDocumentSyncKind,
  InitializeParams,
  InitializeResult,
  Diagnostic,
  DiagnosticSeverity
} from 'vscode-languageserver/node';
import { TextDocument } from 'vscode-languageserver-textdocument';

// Create connection via stdio
const connection = createConnection(ProposedFeatures.all);

// Create documents manager
const documents = new TextDocuments(TextDocument);

connection.onInitialize((params: InitializeParams) => {
  const result: InitializeResult = {
    capabilities: {
      textDocumentSync: TextDocumentSyncKind.Incremental,
      completionProvider: {
        resolveProvider: false
      }
    }
  };
  return result;
});

// Handle document changes
documents.onDidChangeContent(change => {
  validateDocument(change.document);
});

function validateDocument(textDocument: TextDocument): void {
  // Implementation
}

documents.listen(connection);
connection.listen();
```

## LSP Client Example

Basic structure of a language client extension:

```typescript
import * as vscode from 'vscode';
import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient;

export async function activate(context: vscode.ExtensionContext) {
  const serverModule = context.asAbsolutePath(
    join('server', 'out', 'server.js')
  );

  const serverOptions: ServerOptions = {
    run: { module: serverModule, transport: TransportKind.ipc },
    debug: {
      module: serverModule,
      transport: TransportKind.ipc,
      options: { execArgv: ['--nolazy', '--inspect=6009'] }
    }
  };

  const clientOptions: LanguageClientOptions = {
    documentSelector: [{ scheme: 'file', language: 'myLanguage' }]
  };

  client = new LanguageClient(
    'myLanguageServer',
    'My Language Server',
    serverOptions,
    clientOptions
  );

  await client.start();
}

export async function deactivate() {
  if (client) {
    await client.stop();
  }
}
```

## Middleware System

Both client and server support middleware for intercepting messages:

```typescript
// Client middleware example
const clientOptions: LanguageClientOptions = {
  middleware: {
    provideCompletionItem: async (
      document,
      position,
      context,
      token,
      next
    ) => {
      // Pre-processing
      const items = await next(document, position, context, token);
      // Post-processing
      return items;
    }
  }
};
```

## Message Exchange Patterns

### Requests (Request/Response)

```typescript
// Define custom request
export const CustomRequest = new RequestType<
  CustomParams,
  CustomResult,
  void
>('custom/request');

// Server-side handler
connection.onRequest(CustomRequest, (params) => {
  return { result: 'value' };
});

// Client-side usage
const result = await client.sendRequest(CustomRequest, params);
```

### Notifications (One-way)

```typescript
// Define custom notification
export const CustomNotification = new NotificationType<CustomParams>(
  'custom/notification'
);

// Server-side handler
connection.onNotification(CustomNotification, (params) => {
  // Handle notification
});

// Client-side usage
client.sendNotification(CustomNotification, params);
```

## Document Synchronization

The library supports multiple document synchronization modes:

- **None** - No synchronization
- **Full** - Full document is sent on changes
- **Incremental** - Only changed parts are sent (more efficient)

```typescript
// Server capability declaration
capabilities: {
  textDocumentSync: {
    openClose: true,
    change: TextDocumentSyncKind.Incremental,
    save: {
      includeText: true
    }
  }
}
```

## Configuration Management

Servers can request configuration from the client:

```typescript
// Server requests configuration
const config = await connection.sendRequest(
  ConfigurationRequest.type,
  { items: [{ section: 'myLanguage' }] }
);

// Handle document did change notification
connection.onDidChangeConfiguration((change) => {
  // Configuration changed
});
```

## Workspace Features

### Workspace Symbols

```typescript
connection.onWorkspaceSymbol((params) => {
  return [
    {
      name: 'symbolName',
      kind: SymbolKind.Class,
      location: {
        uri: documentUri,
        range: range
      }
    }
  ];
});
```

### Workspace Edits

```typescript
const workspaceEdit: WorkspaceEdit = {
  changes: {
    [documentUri]: [
      TextEdit.insert(position, 'inserted text')
    ]
  }
};
```

## Diagnostics

Publish diagnostics to the client:

```typescript
connection.sendDiagnostics({
  uri: documentUri,
  diagnostics: [
    {
      severity: DiagnosticSeverity.Error,
      range: range,
      message: 'Error message'
    }
  ]
});
```

## Code Actions

Implement code actions for fixing diagnostics:

```typescript
connection.onCodeAction((params) => {
  const diagnostics = params.context.diagnostics;
  return diagnostics.map(diagnostic => ({
    title: 'Fix',
    kind: CodeActionKind.QuickFix,
    edit: {
      changes: {
        [params.textDocument.uri]: [
          TextEdit.replace(diagnostic.range, 'fixed text')
        ]
      }
    }
  }));
});
```

## Completion

Implement code completion:

```typescript
connection.onCompletion((params) => {
  return [
    {
      label: 'keyword',
      kind: CompletionItemKind.Keyword,
      detail: 'Description',
      insertText: 'keyword'
    }
  ];
});

connection.onCompletionResolve((item) => {
  item.documentation = 'Full documentation';
  return item;
});
```

## Recent Changes and Versions

### Next (10.0.0-next.* Client, 10.0.0-next.* Server, 9.0.0-next.* jsonrpc)

- Upgraded to newer libraries, compilers and package.json exports rules
- Compiler upgraded to TypeScript 5.9.x
- Libraries now depend on NodeJS 22.13.14 and ES2022 target
- Uses `exports` property instead of `main` and `typings` in package.json
- Added proposed `CodeActionKind.RefactorMove`
- Snippet support in Workspace edits
- Parallelism control for dispatch requests and notifications
- Browser implementation consistency with Node implementation

### 3.17.5 Protocol, 9.0.1 Client and 9.0.1 Server

- Fixed ESM bundling

### 3.17.4 Protocol, 8.2.0 JSON-RPC, 9.0.0 Client and 9.0.0 Server

- Added proposed inline completion request
- Added proposed formatting ranges request
- Proposed refresh request for folding ranges
- Custom message handlers support

### 3.17.3 Protocol, 8.1.0 JSON-RPC, 8.1.0 Client and 8.1.0 Server

- Support for custom message handlers
- Bug fixes around request ordering with full document sync

### 3.17.0 Protocol, 8.0.0 JSON-RPC, 8.0.0 Client and 8.0.0 Server

- Breaking change: `client.start()` and `client.stop()` now return promises
- Notification and request handler registration before client start
- All `sendNotification` methods return promises
- Handler registrations return `Disposable` for unregistration
- Support for inline values, inlay hints, type hierarchies, notebook documents

## Feature Support by Version

The library supports a comprehensive set of LSP features:

- **Diagnostics** - Report code issues and errors
- **Hover** - Hover information for symbols
- **Completion** - Code completion with snippets
- **Signature Help** - Function signature assistance
- **Go to Definition** - Symbol definition navigation
- **Find References** - Find all symbol usages
- **Document Highlights** - Highlight matching symbols
- **Code Actions** - Quick fixes and refactorings
- **Code Lens** - Inline code metrics and actions
- **Document Symbols** - Outline of document structure
- **Workspace Symbols** - Global symbol search
- **Format Document** - Document and range formatting
- **Format on Type** - Format as user types
- **Rename** - Symbol rename with workspace refactoring
- **Semantic Tokens** - Syntax highlighting with semantic information
- **Folding Ranges** - Collapsible code regions
- **Selection Ranges** - Smart selection expansion
- **Call Hierarchies** - Call chain navigation
- **Inlay Hints** - Inline type and parameter hints
- **Inline Values** - Runtime variable values display
- **Type Hierarchies** - Class inheritance visualization
- **Linked Editing Range** - Multi-cursor for related identifiers
- **Document Links** - Clickable links in documents
- **Moniker** - Cross-language symbol identification
- **Notebook Document** - Jupyter and similar notebook support

## Browser Support

The library now has browser implementations for client and server, enabling:

- Web-based language servers
- Shared TypeScript instances across browser tabs
- Web-based IDE implementations

## Error Handling

Servers can implement custom error handlers:

```typescript
interface ErrorHandler {
  error(error: Error, message: Message, count: number): ErrorAction;
  closed(): CloseAction;
}

enum ErrorAction {
  Continue = 1,
  Shutdown = 2
}

enum CloseAction {
  DoNotRestart = 1,
  Restart = 2
}
```

## Development

### Running Tests

The repository includes comprehensive tests for all packages:

```bash
npm test
```

### Building

```bash
npm run build
```

### Publishing

All packages are published to npm registry from this monorepo.

## License

MIT - See LICENSE.txt in the repository

## Related Resources

- [Language Server Protocol Specification](https://microsoft.github.io/language-server-protocol/)
- [VSCode Extension Development](https://code.visualstudio.com/api)
- [VSCode Language Server Example](https://code.visualstudio.com/docs/extensions/example-language-server)
- [NPM Package: vscode-languageclient](https://www.npmjs.com/package/vscode-languageclient)
- [NPM Package: vscode-languageserver](https://www.npmjs.com/package/vscode-languageserver)
- [NPM Package: vscode-languageserver-protocol](https://www.npmjs.com/package/vscode-languageserver-protocol)
- [NPM Package: vscode-jsonrpc](https://www.npmjs.com/package/vscode-jsonrpc)
