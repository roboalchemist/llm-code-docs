# vscode-languageserver-protocol

Source: https://github.com/microsoft/vscode-languageserver-node/tree/main/protocol

NPM Package: `vscode-languageserver-protocol`

Tool-independent implementation of the Language Server Protocol definition in TypeScript. This module can be used in any type of Node.js application.

## Overview

This npm module provides type-safe definitions for all LSP protocol messages, making it suitable for building language server protocol implementations in various contexts beyond just VSCode.

## Installation

```bash
npm install vscode-languageserver-protocol
```

## Protocol Definition Structure

The protocol module defines three categories of messages:

1. **Requests** - Messages expecting a response
2. **Notifications** - One-way messages without response
3. **Server Capabilities** - What features the server supports

## Request Types

### Defining Custom Requests

```typescript
import { RequestType, RequestType0, RequestType1, RequestType2 } from 'vscode-languageserver-protocol';

// No parameters
export const MyRequest0 = new RequestType0<string, void>('my/request0');

// One parameter
export const MyRequest1 = new RequestType1<string, string, void>('my/request1');

// Two parameters
export const MyRequest2 = new RequestType2<string, number, string, void>(
  'my/request2'
);

// Multiple parameters (as single object)
export interface MyParams {
  param1: string;
  param2: number;
}

export interface MyResult {
  result: string;
}

export const MyRequest = new RequestType<MyParams, MyResult, void>(
  'my/customRequest'
);
```

### Using Request Types

On the server:

```typescript
connection.onRequest(MyRequest, async (params: MyParams) => {
  // Process request
  return { result: 'response value' };
});
```

On the client:

```typescript
const result = await client.sendRequest(MyRequest, {
  param1: 'value',
  param2: 42
});
```

## Notification Types

### Defining Custom Notifications

```typescript
import { NotificationType, NotificationType0 } from 'vscode-languageserver-protocol';

// No parameters
export const MyNotification0 = new NotificationType0('my/notification0');

// With parameters
export interface MyNotificationParams {
  message: string;
}

export const MyNotification = new NotificationType<MyNotificationParams>(
  'my/notification'
);
```

### Using Notification Types

On the server:

```typescript
connection.onNotification(MyNotification, (params: MyNotificationParams) => {
  console.log(params.message);
});
```

On the client:

```typescript
client.sendNotification(MyNotification, {
  message: 'Notification message'
});
```

## Core Protocol Messages

### Text Synchronization

```typescript
import {
  DidOpenTextDocumentNotification,
  DidChangeTextDocumentNotification,
  DidCloseTextDocumentNotification,
  DidSaveTextDocumentNotification,
  TextDocumentSyncKind,
  TextDocumentSyncOptions
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  textDocumentSync: TextDocumentSyncKind.Incremental,
  // or with options
  textDocumentSync: {
    openClose: true,
    change: TextDocumentSyncKind.Incremental,
    save: { includeText: true }
  }
}
```

### Hover

```typescript
import {
  HoverRequest,
  HoverParams,
  Hover,
  MarkupKind
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  hoverProvider: true
}

// Handler
connection.onHover((params: HoverParams) => {
  return {
    contents: {
      kind: MarkupKind.Markdown,
      value: 'Hover information'
    }
  } as Hover;
});
```

### Completion

```typescript
import {
  CompletionRequest,
  CompletionParams,
  CompletionList,
  CompletionItem,
  CompletionItemKind,
  InsertTextFormat
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  completionProvider: {
    resolveProvider: true,
    triggerCharacters: ['.', ':'],
    allCommitCharacters: [';', ',']
  }
}

// Handler
connection.onCompletion((params: CompletionParams) => {
  return {
    isIncomplete: false,
    items: [
      {
        label: 'keyword',
        kind: CompletionItemKind.Keyword,
        detail: 'A keyword',
        documentation: 'Keyword documentation',
        insertText: 'keyword',
        insertTextFormat: InsertTextFormat.PlainText,
        sortText: '1'
      }
    ]
  } as CompletionList;
});

// Resolve completion
connection.onCompletionResolve((item: CompletionItem) => {
  item.data = { /* custom data */ };
  return item;
});
```

### Go to Definition

```typescript
import {
  DefinitionRequest,
  DefinitionParams,
  Location,
  LocationLink
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  definitionProvider: true
}

// Handler
connection.onDefinition((params: DefinitionParams) => {
  return Location.create(uri, range);
  // or
  return [
    LocationLink.create(originUri, originRange, targetUri, targetRange)
  ];
});
```

### Find References

```typescript
import {
  ReferencesRequest,
  ReferencesParams
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  referencesProvider: true
}

// Handler
connection.onReferences((params: ReferencesParams) => {
  return [
    Location.create(uri1, range1),
    Location.create(uri2, range2)
  ];
});
```

### Document Symbols

```typescript
import {
  DocumentSymbolRequest,
  DocumentSymbolParams,
  SymbolInformation,
  DocumentSymbol,
  SymbolKind
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  documentSymbolProvider: true
}

// Handler (returning SymbolInformation)
connection.onDocumentSymbol((params: DocumentSymbolParams) => {
  return [
    SymbolInformation.create(
      'className',
      SymbolKind.Class,
      range,
      params.textDocument.uri
    )
  ];
});

// Or using hierarchical DocumentSymbol
connection.onDocumentSymbol((params: DocumentSymbolParams) => {
  return [
    DocumentSymbol.create(
      'className',
      'class details',
      SymbolKind.Class,
      range,
      range,
      [
        DocumentSymbol.create(
          'methodName',
          undefined,
          SymbolKind.Method,
          methodRange,
          methodRange
        )
      ]
    )
  ];
});
```

### Workspace Symbols

```typescript
import {
  WorkspaceSymbolRequest,
  WorkspaceSymbolParams
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  workspaceSymbolProvider: true
}

// Handler
connection.onWorkspaceSymbol((params: WorkspaceSymbolParams) => {
  return [
    SymbolInformation.create(
      'globalSymbol',
      SymbolKind.Function,
      range,
      uri
    )
  ];
});
```

### Code Actions

```typescript
import {
  CodeActionRequest,
  CodeActionParams,
  CodeAction,
  CodeActionKind,
  Command
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  codeActionProvider: true
  // or with options
  codeActionProvider: {
    codeActionKinds: [CodeActionKind.QuickFix],
    resolveProvider: true
  }
}

// Handler
connection.onCodeAction((params: CodeActionParams) => {
  const fixes: CodeAction[] = [];

  for (const diagnostic of params.context.diagnostics) {
    fixes.push(
      CodeAction.create(
        'Fix issue',
        {
          changes: {
            [params.textDocument.uri]: [
              TextEdit.replace(diagnostic.range, 'fixed text')
            ]
          }
        },
        CodeActionKind.QuickFix
      )
    );
  }

  return fixes;
});
```

### Code Lens

```typescript
import {
  CodeLensRequest,
  CodeLensParams,
  CodeLens,
  Command
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  codeLensProvider: {
    resolveProvider: true
  }
}

// Handler
connection.onCodeLens((params: CodeLensParams) => {
  return [
    CodeLens.create(range, {
      title: 'Run Test',
      command: 'extension.runTest',
      arguments: [testName]
    } as Command)
  ];
});

// Resolve code lens
connection.onCodeLensResolve((lens: CodeLens) => {
  return lens;
});
```

### Document Formatting

```typescript
import {
  DocumentFormattingRequest,
  DocumentFormattingParams,
  DocumentRangeFormattingRequest,
  DocumentRangeFormattingParams,
  DocumentOnTypeFormattingRequest,
  DocumentOnTypeFormattingParams,
  TextEdit,
  FormattingOptions
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  documentFormattingProvider: true,
  documentRangeFormattingProvider: true,
  documentOnTypeFormattingProvider: {
    firstTriggerCharacter: '}',
    moreTriggerCharacter: [';', ',']
  }
}

// Document formatting handler
connection.onDocumentFormatting((params: DocumentFormattingParams) => {
  return [
    TextEdit.replace(wholeDocumentRange, formattedText)
  ];
});

// Range formatting handler
connection.onDocumentRangeFormatting(
  (params: DocumentRangeFormattingParams) => {
    return [
      TextEdit.replace(params.range, formattedRangeText)
    ];
  }
);

// On type formatting handler
connection.onDocumentOnTypeFormatting(
  (params: DocumentOnTypeFormattingParams) => {
    return [
      TextEdit.insert(params.position, additionalText)
    ];
  }
);
```

### Rename

```typescript
import {
  RenameRequest,
  RenameParams,
  WorkspaceEdit
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  renameProvider: true
  // or with options
  renameProvider: {
    prepareProvider: true
  }
}

// Handler
connection.onRename((params: RenameParams) => {
  return WorkspaceEdit.create({
    changes: {
      [uri]: [
        TextEdit.replace(range1, params.newName),
        TextEdit.replace(range2, params.newName)
      ]
    }
  });
});

// Prepare rename
connection.onPrepareRename((params) => {
  return range;
});
```

### Diagnostics

```typescript
import {
  PublishDiagnosticsNotification,
  Diagnostic,
  DiagnosticSeverity,
  DiagnosticTag,
  CodeDescription
} from 'vscode-languageserver-protocol';

// Send diagnostics
connection.sendDiagnostics({
  uri: documentUri,
  diagnostics: [
    {
      severity: DiagnosticSeverity.Error,
      range: {
        start: { line: 0, character: 0 },
        end: { line: 0, character: 5 }
      },
      message: 'Error message',
      code: 'ERR001',
      source: 'myLanguage',
      tags: [DiagnosticTag.Unnecessary],
      codeDescription: {
        href: 'https://example.com/error-docs'
      },
      relatedInformation: [
        {
          location: {
            uri: otherUri,
            range: otherRange
          },
          message: 'Related issue'
        }
      ]
    }
  ]
});
```

### Signature Help

```typescript
import {
  SignatureHelpRequest,
  SignatureHelpParams,
  SignatureInformation,
  ParameterInformation,
  MarkupContent,
  MarkupKind
} from 'vscode-languageserver-protocol';

// Server capability
capabilities: {
  signatureHelpProvider: {
    triggerCharacters: ['(', ','],
    retriggerCharacters: [',']
  }
}

// Handler
connection.onSignatureHelp((params: SignatureHelpParams) => {
  return {
    signatures: [
      SignatureInformation.create(
        'function(arg1: string, arg2: number): void',
        {
          kind: MarkupKind.Markdown,
          value: 'Function documentation'
        } as MarkupContent,
        ParameterInformation.create(
          'arg1',
          'Argument 1'
        ),
        ParameterInformation.create(
          'arg2',
          'Argument 2'
        )
      )
    ],
    activeSignature: 0,
    activeParameter: 0
  };
});
```

## Configuration Management

```typescript
import {
  DidChangeConfigurationNotification,
  ConfigurationRequest,
  ConfigurationParams
} from 'vscode-languageserver-protocol';

// Register for configuration change notifications
connection.client.register(
  DidChangeConfigurationNotification.type,
  undefined
);

// Handle configuration change
connection.onDidChangeConfiguration((change) => {
  // Configuration changed
});

// Request configuration from client
const config = await connection.sendRequest(
  ConfigurationRequest.type,
  {
    items: [
      { section: 'myLanguage' },
      { section: 'myLanguage.diagnostics', scopeUri: documentUri }
    ]
  } as ConfigurationParams
);
```

## Workspace Features

```typescript
import {
  DidChangeWorkspaceFoldersNotification,
  WorkspaceFoldersRequest
} from 'vscode-languageserver-protocol';

// Register for workspace folder changes
connection.client.register(
  DidChangeWorkspaceFoldersNotification.type,
  undefined
);

// Handle workspace folder changes
connection.onDidChangeWorkspaceFolders((event) => {
  // Event contains added and removed folders
});

// Request workspace folders
const folders = await connection.sendRequest(
  WorkspaceFoldersRequest.type
);
```

## File Events

```typescript
import {
  DidChangeWatchedFilesNotification,
  FileChangeType
} from 'vscode-languageserver-protocol';

// Handle watched file changes
connection.onDidChangeWatchedFiles((change) => {
  for (const event of change.changes) {
    if (event.type === FileChangeType.Created) {
      // File created
    } else if (event.type === FileChangeType.Changed) {
      // File changed
    } else if (event.type === FileChangeType.Deleted) {
      // File deleted
    }
  }
});
```

## Parameter Structures

Control how parameters are sent in requests/notifications:

```typescript
import { ParameterStructures } from 'vscode-languageserver-protocol';

// Auto-detect best structure (default)
const request = new RequestType<Params, Result, void>('my/request');

// Force by-position parameters
const request = new RequestType<Params, Result, void>(
  'my/request',
  ParameterStructures.byPosition
);

// Force by-name parameters
const request = new RequestType<Params, Result, void>(
  'my/request',
  ParameterStructures.byName
);
```

## Error Codes

Standard LSP error codes:

```typescript
import { ErrorCodes, LSPErrorCodes } from 'vscode-languageserver-protocol';

// JSON-RPC error codes
ErrorCodes.ParseError = -32700;
ErrorCodes.InvalidRequest = -32600;
ErrorCodes.MethodNotFound = -32601;
ErrorCodes.InvalidParams = -32602;
ErrorCodes.InternalError = -32603;

// LSP-specific error codes
LSPErrorCodes.ServerNotInitialized = -32002;
LSPErrorCodes.UnknownErrorCode = -32001;
LSPErrorCodes.RequestCancelled = -32800;
LSPErrorCodes.ContentModified = -32801;
LSPErrorCodes.ServerCancelled = -32802;
```

## Implementation Notes

- This module is version-aligned with the LSP specification version number
- It provides a tool-independent implementation suitable for various environments
- Type-safe definitions prevent runtime errors
- Can be used alongside other protocol implementations
- Supports proposed protocol features for early adoption

## Usage Scenarios

1. **Building custom protocol implementations** - Use type definitions as reference
2. **Creating protocol adapters** - Transform messages between different protocols
3. **Protocol validation tools** - Validate messages against LSP definitions
4. **Cross-platform language servers** - Use in Node.js, Deno, or other runtimes
5. **Language protocol research** - Study the protocol specification through code

## Related Resources

- [Language Server Protocol Specification](https://microsoft.github.io/language-server-protocol/)
- [vscode-languageserver-types](../types.md) - Data types
- [vscode-languageserver](../server.md) - Server implementation
- [vscode-languageclient](../client.md) - Client implementation
