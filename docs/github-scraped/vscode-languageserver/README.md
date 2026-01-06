# vscode-languageserver

Source: https://github.com/microsoft/vscode-languageserver-node/tree/main/server

NPM Package: `vscode-languageserver`

Npm module to implement a VSCode language server using Node.js as a runtime.

## Overview

This module provides the server-side implementation of the Language Server Protocol for Node.js. It handles incoming LSP requests and notifications from a VSCode client extension.

## Installation

```bash
npm install vscode-languageserver
```

## Quick Start

### Basic Language Server

```typescript
import {
  createConnection,
  TextDocuments,
  Diagnostic,
  DiagnosticSeverity,
  ProposedFeatures,
  TextDocumentSyncKind,
  InitializeParams,
  DidChangeConfigurationNotification,
  CompletionItem,
  CompletionItemKind,
  TextDocumentPositionParams,
  TextDocumentItem,
  Connection
} from 'vscode-languageserver/node';

import { TextDocument } from 'vscode-languageserver-textdocument';

// Create a connection for the server. The connection uses Node's IPC as a transport.
// Also include all preview / proposed LSP features.
const connection = createConnection(ProposedFeatures.all);

// Create a simple text document manager.
const documents: TextDocuments<TextDocument> = new TextDocuments(TextDocument);

let hasConfigurationCapability: boolean = false;
let hasWorkspaceFolderCapability: boolean = false;
let hasDiagnosticRelatedInformationCapability: boolean = false;

connection.onInitialize((params: InitializeParams) => {
  const capabilities = params.capabilities;

  // Does the client support the `workspace/configuration` request?
  hasConfigurationCapability = !!(
    capabilities.workspace && !!capabilities.workspace.configuration
  );
  hasWorkspaceFolderCapability = !!(
    capabilities.workspace && !!capabilities.workspace.workspaceFolders
  );
  hasDiagnosticRelatedInformationCapability = !!(
    capabilities.textDocument &&
    capabilities.textDocument.publishDiagnostics &&
    capabilities.textDocument.publishDiagnostics.relatedInformation
  );

  const result: InitializeResult = {
    capabilities: {
      textDocumentSync: TextDocumentSyncKind.Incremental,
      completionProvider: {
        resolveProvider: true
      }
    }
  };
  if (hasWorkspaceFolderCapability) {
    result.capabilities.workspace = {
      workspaceFolders: {
        supported: true,
        changeNotifications: true
      }
    };
  }
  return result;
});

connection.onInitialized(() => {
  if (hasConfigurationCapability) {
    // Register for all configuration changes.
    connection.client.register(
      DidChangeConfigurationNotification.type,
      undefined
    );
  }
  if (hasWorkspaceFolderCapability) {
    connection.workspace.onDidChangeWorkspaceFolders(_event => {
      connection.console.log('Workspace folder change event received.');
    });
  }
});

// The example settings
interface ExampleSettings {
  maxNumberOfProblems: number;
}

// The global settings, used when the `workspace/configuration` request is not supported by the client.
const defaultSettings: ExampleSettings = { maxNumberOfProblems: 1000 };
let globalSettings: ExampleSettings = defaultSettings;

// Cache the settings of all open documents
const documentSettings: Map<string, Thenable<ExampleSettings>> = new Map();

connection.onDidChangeConfiguration(change => {
  if (hasConfigurationCapability) {
    // Reset all cached document settings
    documentSettings.clear();
  } else {
    globalSettings = <ExampleSettings>(
      (change.settings.languageServerExample || defaultSettings)
    );
  }

  // Revalidate all open text documents
  documents.all().forEach(validateTextDocument);
});

function getDocumentSettings(resource: string): Thenable<ExampleSettings> {
  if (!hasConfigurationCapability) {
    return Promise.resolve(globalSettings);
  }
  let result = documentSettings.get(resource);
  if (!result) {
    result = connection.workspace.getConfiguration(
      { scopeUri: resource, section: 'languageServerExample' }
    );
    documentSettings.set(resource, result);
  }
  return result;
}

// Only keep settings for open documents
documents.onDidClose(e => {
  documentSettings.delete(e.document.uri);
});

// The content of a text document has changed. This event is emitted
// when the text document first opened or when its content has changed.
documents.onDidChangeContent(change => {
  validateTextDocument(change.document);
});

async function validateTextDocument(textDocument: TextDocument): Promise<void> {
  // In this simple example we get the settings for every validate run.
  const settings = await getDocumentSettings(textDocument.uri);

  // The validator creates diagnostics for all uppercase words length 2 and more
  const text = textDocument.getText();
  const pattern = /\b[A-Z]{2,}\b/g;
  let m: RegExpExecArray | null;

  let problems = 0;
  const diagnostics: Diagnostic[] = [];
  while ((m = pattern.exec(text)) && problems < settings.maxNumberOfProblems) {
    problems++;
    const diagnostic: Diagnostic = {
      severity: DiagnosticSeverity.Warning,
      range: {
        start: textDocument.positionAt(m.index),
        end: textDocument.positionAt(m.index + m[0].length)
      },
      message: `${m[0]} is all uppercase.`,
      source: 'ex'
    };
    if (hasDiagnosticRelatedInformationCapability) {
      diagnostic.relatedInformation = [
        {
          location: {
            uri: textDocument.uri,
            range: Object.assign({}, diagnostic.range)
          },
          message: 'Spelling matters'
        },
        {
          location: {
            uri: textDocument.uri,
            range: Object.assign({}, diagnostic.range)
          },
          message: 'Especially for function/class names'
        }
      ];
    }
    diagnostics.push(diagnostic);
  }

  // Send the computed diagnostics to the client
  connection.sendDiagnostics({ uri: textDocument.uri, diagnostics });
}

connection.onDidChangeWatchedFiles(_change => {
  // Monitored files have change in VSCode
  connection.console.log('We received a file change event');
});

// This handler provides the initial list of the completion items.
connection.onCompletion(
  (_textDocumentPosition: TextDocumentPositionParams): CompletionItem[] => {
    // The pass parameter contains the position of the text document in
    // which code complete got requested. For the example we ignore this
    // information and always provide the same completion items.
    return [
      {
        label: 'TypeScript',
        kind: CompletionItemKind.Text,
        data: 1
      },
      {
        label: 'JavaScript',
        kind: CompletionItemKind.Text,
        data: 2
      }
    ];
  }
);

// This handler resolves additional information for the item selected in
// the completion list.
connection.onCompletionResolve(
  (item: CompletionItem): CompletionItem => {
    if (item.data === 1) {
      item.detail = 'TypeScript details';
      item.documentation = 'TypeScript documentation';
    } else if (item.data === 2) {
      item.detail = 'JavaScript details';
      item.documentation = 'JavaScript documentation';
    }
    return item;
  }
);

// Make the text document manager listen on the connection
// for open, change and close text document synchronization events
documents.listen(connection);

// Listen on the connection
connection.listen();
```

## Server Creation

### Creating a Connection

The `createConnection()` function establishes the server-client connection:

```typescript
import { createConnection, ProposedFeatures } from 'vscode-languageserver/node';

// Create connection over stdin/stdout
const connection = createConnection();

// Or with specific features
const connection = createConnection(ProposedFeatures.all);
```

### Transport Options

```typescript
// Default: stdio transport
const connection = createConnection();

// IPC transport
const connection = createConnection(
  new IPCMessageReader(process.stdin),
  new IPCMessageWriter(process.stdout)
);

// Socket transport
const connection = createConnection(
  new SocketMessageReader(socket),
  new SocketMessageWriter(socket)
);
```

## Document Management

### TextDocuments

Manage open text documents and their changes:

```typescript
import { TextDocuments } from 'vscode-languageserver/node';
import { TextDocument } from 'vscode-languageserver-textdocument';

// Create a documents manager
const documents = new TextDocuments(TextDocument);

// Listen to document events
documents.onDidOpen(event => {
  console.log('Document opened:', event.document.uri);
});

documents.onDidChange(event => {
  console.log('Document changed:', event.document.uri);
});

documents.onDidClose(event => {
  console.log('Document closed:', event.document.uri);
});

documents.onDidSave(event => {
  console.log('Document saved:', event.document.uri);
});

// Get a document
const document = documents.get(uri);

// Access document content
const text = document.getText();
const line = document.getText({ start: { line: 0, character: 0 }, end: { line: 1, character: 0 } });

// Calculate positions
const offset = document.offsetAt({ line: 5, character: 10 });
const position = document.positionAt(100);

// Make changes to documents
documents.listen(connection);
```

## Initialization

### onInitialize Handler

```typescript
import { InitializeParams, InitializeResult } from 'vscode-languageserver/node';

connection.onInitialize((params: InitializeParams) => {
  // Get client capabilities
  const capabilities = params.capabilities;

  // Check for specific capabilities
  const hasHover = capabilities.textDocument?.hoverProvider;
  const hasCompletion = capabilities.textDocument?.completionProvider;

  // Return server capabilities
  const result: InitializeResult = {
    capabilities: {
      textDocumentSync: TextDocumentSyncKind.Incremental,
      hoverProvider: true,
      completionProvider: {
        resolveProvider: true,
        triggerCharacters: ['.', ':', '<']
      },
      definitionProvider: true,
      referencesProvider: true,
      documentSymbolProvider: true,
      workspaceSymbolProvider: true,
      codeActionProvider: true,
      codeLensProvider: {
        resolveProvider: true
      },
      documentFormattingProvider: true,
      documentRangeFormattingProvider: true,
      renameProvider: true
    }
  };

  return result;
});

connection.onInitialized(() => {
  // Server is fully initialized
  // Can now send requests to client
});
```

## Request Handlers

### Generic Request Handler

```typescript
connection.onRequest(method, async (params) => {
  // Handle custom request
  return result;
});
```

### Standard LSP Requests

```typescript
// Hover
connection.onHover((params: HoverParams) => {
  return {
    contents: 'Hover information'
  };
});

// Completion
connection.onCompletion((params: CompletionParams) => {
  return [
    { label: 'item1', kind: CompletionItemKind.Text },
    { label: 'item2', kind: CompletionItemKind.Function }
  ];
});

connection.onCompletionResolve((item: CompletionItem) => {
  item.detail = 'Detailed information';
  return item;
});

// Go to Definition
connection.onDefinition((params: DefinitionParams) => {
  return Location.create(uri, range);
});

// Find References
connection.onReferences((params: ReferencesParams) => {
  return [
    Location.create(uri1, range1),
    Location.create(uri2, range2)
  ];
});

// Document Symbols
connection.onDocumentSymbol((params: DocumentSymbolParams) => {
  return [
    DocumentSymbol.create('symbolName', SymbolKind.Class, range)
  ];
});

// Workspace Symbols
connection.onWorkspaceSymbol((params: WorkspaceSymbolParams) => {
  return [
    SymbolInformation.create('symbolName', SymbolKind.Class, range, uri)
  ];
});

// Code Actions
connection.onCodeAction((params: CodeActionParams) => {
  return [
    CodeAction.create('Fix issue', {
      changes: { [uri]: [TextEdit.replace(range, 'replacement')] }
    })
  ];
});

// Code Lens
connection.onCodeLens((params: CodeLensParams) => {
  return [
    CodeLens.create(range, { title: 'Lens', command: 'command' })
  ];
});

connection.onCodeLensResolve((lens: CodeLens) => {
  return lens;
});

// Document Formatting
connection.onDocumentFormatting((params: DocumentFormattingParams) => {
  return [
    TextEdit.replace(wholeDocRange, formattedText)
  ];
});

// Document Range Formatting
connection.onDocumentRangeFormatting((params: DocumentRangeFormattingParams) => {
  return [
    TextEdit.replace(params.range, formattedText)
  ];
});

// Format on Type
connection.onDocumentOnTypeFormatting((params: DocumentOnTypeFormattingParams) => {
  return [
    TextEdit.insert(params.position, ' ')
  ];
});

// Rename
connection.onRename((params: RenameParams) => {
  return WorkspaceEdit.create({
    changes: {
      [uri]: [TextEdit.replace(range1, newName), TextEdit.replace(range2, newName)]
    }
  });
});

// Signature Help
connection.onSignatureHelp((params: SignatureHelpParams) => {
  return {
    signatures: [
      SignatureInformation.create(
        'function(arg1: string, arg2: number): void',
        'Function documentation',
        [
          ParameterInformation.create('arg1', 'Argument 1'),
          ParameterInformation.create('arg2', 'Argument 2')
        ]
      )
    ],
    activeSignature: 0,
    activeParameter: 0
  };
});
```

## Notification Handlers

### Generic Notification Handler

```typescript
connection.onNotification(method, (params) => {
  // Handle custom notification
});
```

### Standard LSP Notifications

```typescript
// Text Document Changes
documents.onDidChange(event => {
  // Document content changed
});

// Text Document Opened
documents.onDidOpen(event => {
  // Document opened
});

// Text Document Closed
documents.onDidClose(event => {
  // Document closed
});

// Configuration Changed
connection.onDidChangeConfiguration((change) => {
  // Configuration changed on client side
});

// Watched Files Changed
connection.onDidChangeWatchedFiles((change) => {
  for (const event of change.changes) {
    console.log(event.uri, event.type);
  }
});

// Workspace Folders Changed
connection.onDidChangeWorkspaceFolders((event) => {
  for (const folder of event.added) {
    console.log('Added:', folder.uri);
  }
  for (const folder of event.removed) {
    console.log('Removed:', folder.uri);
  }
});
```

## Sending Messages to Client

### Sending Diagnostics

```typescript
connection.sendDiagnostics({
  uri: documentUri,
  diagnostics: [
    {
      severity: DiagnosticSeverity.Error,
      range: range,
      message: 'Error message',
      code: 'ERROR001'
    }
  ]
});
```

### Sending Notifications

```typescript
// Show message to user
connection.sendNotification('window/showMessage', {
  type: MessageType.Warning,
  message: 'Warning message'
});

// Log to output
connection.console.log('Log message');
connection.console.error('Error message');
```

### Sending Requests

```typescript
// Request configuration from client
const config = await connection.sendRequest('workspace/configuration', {
  items: [{ section: 'myLanguage' }]
});

// Request workspace folders
const folders = await connection.sendRequest('workspace/workspaceFolders', null);

// Show input dialog
const result = await connection.sendRequest('window/showInputBox', {
  prompt: 'Enter value:',
  value: 'default'
});
```

## Configuration Management

### Getting Configuration

```typescript
connection.onDidChangeConfiguration((change) => {
  if (hasConfigurationCapability) {
    // Reset cached configuration
    documentSettings.clear();
  } else {
    // Use global settings
    globalSettings = change.settings.myLanguage || defaultSettings;
  }
});

async function getSettings(resource: string) {
  if (!hasConfigurationCapability) {
    return globalSettings;
  }

  const settings = await connection.workspace.getConfiguration({
    scopeUri: resource,
    section: 'myLanguage'
  });

  return settings;
}
```

## Logging

### Console Logging

```typescript
connection.console.log('Log message');
connection.console.warn('Warning message');
connection.console.error('Error message');
```

### Trace Logging

```typescript
connection.tracer.log('Trace message');
```

## Error Handling

### Request Error Responses

```typescript
connection.onRequest('myRequest', async (params) => {
  try {
    // Implementation
    return result;
  } catch (error) {
    // Return error response
    return new ResponseError(
      -32603,
      'Internal error: ' + error.message
    );
  }
});
```

## Workspace Features

### Workspace Folders

```typescript
connection.onInitialize((params) => {
  const workspaceFolders = params.workspaceFolders;

  for (const folder of workspaceFolders || []) {
    console.log('Workspace folder:', folder.uri);
  }

  return {
    capabilities: {
      workspace: {
        workspaceFolders: {
          supported: true,
          changeNotifications: true
        }
      }
    }
  };
});

connection.onDidChangeWorkspaceFolders((event) => {
  // Handle workspace folder changes
});

// Get workspace folders at runtime
const folders = await connection.workspace.getWorkspaceFolders();
```

## Advanced Features

### Dynamic Capability Registration

```typescript
connection.onInitialize((params) => {
  // Return capabilities with version info for dynamic updates
  return {
    capabilities: {
      textDocumentSync: TextDocumentSyncKind.Incremental
    }
  };
});

connection.onInitialized(() => {
  // Dynamically register a capability
  connection.client.register(
    DidChangeConfigurationNotification.type,
    undefined
  );
});
```

## Lifecycle

```typescript
// Startup
connection.listen();

// While running
// ... handle requests and notifications

// Shutdown
connection.onShutdown(() => {
  // Perform cleanup
  connection.dispose();
});

connection.onExit(() => {
  // Server is exiting
  process.exit(0);
});
```

## Best Practices

1. **Always validate input** - Check parameters before processing
2. **Handle errors gracefully** - Use try-catch and return proper errors
3. **Cancel long operations** - Respect cancellation tokens
4. **Cache appropriately** - Cache settings and computed results
5. **Use typed parameters** - Use LSP type definitions from the protocol module
6. **Log adequately** - Use connection.console for debugging
7. **Performance matters** - Optimize for incremental updates and partial results

## Testing

Test your language server with sample files and validate:

1. Proper initialization with capability reporting
2. Correct response to all implemented requests
3. Proper error handling for invalid input
4. Memory usage under load
5. CPU usage during large file processing

## Deployment

Package your server as a Node.js module:

```bash
npm install vscode-languageserver
npm run build
npm publish
```

The server can be deployed as:
- Built into a VSCode extension
- Shipped separately as an npm module
- Deployed on a remote server
