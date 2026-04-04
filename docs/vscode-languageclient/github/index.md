# vscode-languageclient

Source: https://github.com/microsoft/vscode-languageserver-node/tree/main/client

NPM Package: `vscode-languageclient`

The client library that allows VSCode extensions to easily integrate language servers adhering to the Language Server Protocol.

## Overview

This npm module provides the client-side implementation of the Language Server Protocol for VSCode extensions. It handles the communication between the VSCode editor and the language server running either locally or on a remote machine.

## Installation

```bash
npm install vscode-languageclient
```

## Basic Usage

### Creating a Language Client

```typescript
import * as vscode from 'vscode';
import {
  LanguageClient,
  LanguageClientOptions,
  ServerOptions,
  TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient;

export function activate(context: vscode.ExtensionContext) {
  // Location of the server module that was shipped with the extension
  const serverModule = context.asAbsolutePath(
    join('server', 'out', 'server.js')
  );

  // If the extension is launched in debug mode then the debug server options are used
  // Otherwise the run options are used
  const serverOptions: ServerOptions = {
    run: { module: serverModule, transport: TransportKind.ipc },
    debug: {
      module: serverModule,
      transport: TransportKind.ipc,
      options: { execArgv: ['--nolazy', '--inspect=6009'] }
    }
  };

  // Options to control the language client
  const clientOptions: LanguageClientOptions = {
    // Register the server for specific document types
    documentSelector: [{ scheme: 'file', language: 'mylanguage' }],
    synchronize: {
      // Notify the server about file changes to '.clientrc files'
      fileEvents: vscode.workspace.createFileSystemWatcher('**/.clientrc')
    }
  };

  // Create the language client and start the client.
  client = new LanguageClient(
    'languageServerExample',
    'Language Server Example',
    serverOptions,
    clientOptions
  );

  // Start the client. This will also launch the server
  const disposable = client.start();

  // Push the disposable to the context's subscriptions so that the
  // client can be deactivated on extension deactivation
  context.subscriptions.push(disposable);
}

export function deactivate(): Thenable<void> | undefined {
  if (!client) {
    return undefined;
  }
  return client.stop();
}
```

## Server Options

The `ServerOptions` interface defines how to start the language server:

```typescript
interface ServerOptions {
  run?: Executable | { command: string; args?: string[] };
  debug?: Executable | { command: string; args?: string[] };
}

interface Executable {
  command: string;
  args?: string[];
  options?: ExecOptions;
}
```

### Common Transport Types

- **ipc** - Node.js inter-process communication (default for local servers)
- **stdio** - Standard input/output stream
- **socket** - TCP socket connection
- **pipe** - Named pipe

### Server Startup Options

```typescript
const serverOptions: ServerOptions = {
  // Run locally via IPC
  run: { module: serverModule, transport: TransportKind.ipc },

  // Run with debugging
  debug: {
    module: serverModule,
    transport: TransportKind.ipc,
    options: {
      execArgv: ['--nolazy', '--inspect=6009'],
      cwd: process.cwd()
    }
  }
};
```

## Client Options

The `LanguageClientOptions` interface configures client behavior:

```typescript
interface LanguageClientOptions {
  documentSelector?: DocumentSelector;
  synchronize?: SynchronizeOptions;
  diagnosticCollectionName?: string;
  outputChannelName?: string;
  revealOutputChannelOn?: RevealOutputChannelOn;
  stdioEncoding?: string;
  initializationOptions?: any;
  initializationFailureHandler?: (
    error: ResponseError<InitializeError> | Error,
    client: LanguageClient,
    clientOptions: LanguageClientOptions
  ) => boolean;
  errorHandler?: ErrorHandler;
  middleware?: ProvideCompletionItemsSignature;
  uriConverters?: URIConverter;
  workspaceFolder?: WorkspaceFolder | null;
  progressOnInitialization?: boolean;
}
```

### Document Selector

Specifies which files the language server should handle:

```typescript
const clientOptions: LanguageClientOptions = {
  documentSelector: [
    // Handle all TypeScript and JavaScript files
    { scheme: 'file', language: 'typescript' },
    { scheme: 'file', language: 'javascript' },
    // Handle untitled/unsaved files
    { scheme: 'untitled', language: 'typescript' },
    // Handle custom URI schemes
    { scheme: 'custom', language: 'mylanguage' }
  ]
};
```

### Synchronize Options

Control what file changes are synchronized to the server:

```typescript
const clientOptions: LanguageClientOptions = {
  synchronize: {
    // Synchronize setting sections to the server
    configurationSection: ['myLanguage', 'myLanguage.diagnostics'],
    // Notify the server about file changes to matching patterns
    fileEvents: [
      vscode.workspace.createFileSystemWatcher('**/*.ml'),
      vscode.workspace.createFileSystemWatcher('**/*.mli'),
      vscode.workspace.createFileSystemWatcher('**/.ocamlformat')
    ]
  }
};
```

## Client Lifecycle

### Starting the Client

```typescript
// Start the client and wait for it to be ready
const disposable = client.start();

// Or wait for initialization to complete
await client.onReady();
```

### Stopping the Client

```typescript
// Stop the client (async operation)
await client.stop();
```

### Deactivation

```typescript
export async function deactivate(): Promise<void> {
  if (client) {
    await client.stop();
  }
}
```

## Middleware

Middleware allows you to intercept and modify messages between client and server:

```typescript
const clientOptions: LanguageClientOptions = {
  middleware: {
    // Intercept completion requests
    provideCompletionItem: (
      document,
      position,
      context,
      token,
      next
    ) => {
      // Pre-processing
      console.log('Requesting completions at', position);

      // Call the next handler (could be another middleware or the server)
      const result = next(document, position, context, token);

      // Post-processing
      return result;
    },

    // Intercept hover requests
    provideHover: (document, position, token, next) => {
      return next(document, position, token);
    },

    // Intercept diagnostics
    publishDiagnostics: (uri, diagnostics, next) => {
      // Filter or modify diagnostics
      const filtered = diagnostics.filter(d => d.severity === DiagnosticSeverity.Error);
      return next(uri, filtered);
    }
  }
};
```

### Common Middleware Hooks

- `provideCompletionItem`
- `provideHover`
- `provideSignatureHelp`
- `provideDefinition`
- `provideReferences`
- `provideDocumentHighlights`
- `provideCodeActions`
- `provideCodeLenses`
- `provideDocumentSymbols`
- `provideWorkspaceSymbols`
- `provideDocumentFormattingEdits`
- `provideDocumentRangeFormattingEdits`
- `provideOnTypeFormattingEdits`
- `provideRenameEdits`
- `publishDiagnostics`

## Error Handling

Implement custom error handling:

```typescript
const errorHandler: ErrorHandler = {
  error: (error, message, count) => {
    if (count && count <= 3) {
      return ErrorAction.Continue;
    }
    return ErrorAction.Shutdown;
  },
  closed: () => {
    return CloseAction.DoNotRestart;
  }
};

const clientOptions: LanguageClientOptions = {
  errorHandler: errorHandler
};
```

### Error Action

```typescript
enum ErrorAction {
  Continue = 1,
  Shutdown = 2
}

enum CloseAction {
  DoNotRestart = 1,
  Restart = 2
}
```

## Feature Support

The client automatically provides LSP features once the server advertises support:

### Dynamic Feature Registration

```typescript
// The server can dynamically register handlers
client.onNotification('custom/notification', (params) => {
  // Handle custom notification
});

// The client will unregister handlers when the server requests
client.onRequest('custom/request', async (params) => {
  return { /* response */ };
});
```

## Output Channel

Access the client's output channel for logging:

```typescript
// Get the output channel
const outputChannel = client.outputChannel;

// Messages are automatically logged here
// You can also append your own messages
outputChannel.appendLine('Custom message');
outputChannel.show();
```

## Configuration

Access workspace configuration from your extension:

```typescript
// Get configuration
const config = vscode.workspace.getConfiguration('myLanguage');
const value = config.get('setting');

// Listen to configuration changes
vscode.workspace.onDidChangeConfiguration((event) => {
  if (event.affectsConfiguration('myLanguage')) {
    // Reload configuration
  }
});
```

## File Operations

Watch for file system events:

```typescript
const clientOptions: LanguageClientOptions = {
  synchronize: {
    fileEvents: vscode.workspace.createFileSystemWatcher('**/*.ml')
  }
};

// Also handle didCreate, didChange, didDelete
const watcher = vscode.workspace.createFileSystemWatcher('**/*.json');
watcher.onDidCreate(uri => {
  // File created
});
watcher.onDidChange(uri => {
  // File changed
});
watcher.onDidDelete(uri => {
  // File deleted
});
```

## URI Conversion

Convert between VSCode URIs and server URIs:

```typescript
const clientOptions: LanguageClientOptions = {
  uriConverters: {
    code2Protocol: (uri: vscode.Uri): string => uri.toString(true),
    protocol2Code: (value: string): vscode.Uri => vscode.Uri.parse(value)
  }
};
```

## Advanced Features

### Progress Reporting

```typescript
// Create a progress indicator
vscode.window.withProgress(
  { location: vscode.ProgressLocation.Notification, title: 'Working...' },
  async () => {
    // Long-running operation
    await client.sendRequest('custom/longOperation', {});
  }
);
```

### Workspace Folders

Work with multiple workspace folders:

```typescript
const workspaceFolders = vscode.workspace.workspaceFolders;

// Access workspace folder for a document
const workspaceFolder = vscode.workspace.getWorkspaceFolder(document.uri);
```

### Extension Activation

Control when the extension activates:

```typescript
// package.json
{
  "activationEvents": [
    "onLanguage:typescript",
    "onLanguage:javascript",
    "onCommand:extension.activate"
  ]
}
```

## Best Practices

1. **Always dispose of resources** - Push disposables to context.subscriptions
2. **Handle async operations** - Use `await` with client methods
3. **Implement proper error handling** - Don't let errors go unhandled
4. **Monitor server health** - Implement error and close handlers
5. **Use diagnostics collection** - Manage diagnostic collections properly
6. **Synchronize configuration** - Keep server and client config in sync
7. **Test with debugging** - Use the debug configuration to test server startup

## Version History

For detailed version history and breaking changes, see the main repository README.

The client module is actively maintained and receives regular updates aligned with LSP specification versions.
