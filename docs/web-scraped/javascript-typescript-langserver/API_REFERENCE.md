# API Reference

Source: https://github.com/sourcegraph/javascript-typescript-langserver

Complete reference for the Language Server Protocol (LSP) methods and extensions supported by this language server.

## Standard LSP Methods

This server implements the core Language Server Protocol specification. For detailed protocol information, see: https://microsoft.github.io/language-server-protocol/

### Text Synchronization

#### `textDocument/didOpen`

Notification sent when a document is opened in the client.

```typescript
interface DidOpenTextDocumentParams {
  textDocument: TextDocumentItem
}

interface TextDocumentItem {
  uri: string
  languageId: string
  version: number
  text: string
}
```

#### `textDocument/didChange`

Notification sent when a document is modified.

```typescript
interface DidChangeTextDocumentParams {
  textDocument: VersionedTextDocumentIdentifier
  contentChanges: TextDocumentContentChangeEvent[]
}
```

#### `textDocument/didClose`

Notification sent when a document is closed.

```typescript
interface DidCloseTextDocumentParams {
  textDocument: TextDocumentIdentifier
}
```

### Language Features

#### `textDocument/hover`

Get hover information for a symbol at a position.

**Request:**
```typescript
interface HoverParams {
  textDocument: TextDocumentIdentifier
  position: Position
}
```

**Response:**
```typescript
interface Hover {
  contents: MarkedString | MarkedString[] | MarkupContent
  range?: Range
}
```

**Example:** Displays type information and JSDoc comments for the symbol at the cursor.

#### `textDocument/definition`

Navigate to the definition of a symbol.

**Request:**
```typescript
interface DefinitionParams {
  textDocument: TextDocumentIdentifier
  position: Position
}
```

**Response:**
```typescript
Location | Location[] | null
```

A `Location` includes the document URI and the range of the symbol definition.

#### `textDocument/typeDefinition`

Navigate to the type definition of a symbol.

**Request:**
```typescript
interface TypeDefinitionParams {
  textDocument: TextDocumentIdentifier
  position: Position
}
```

**Response:**
```typescript
Location | Location[] | null
```

Useful for following type aliases and interfaces.

#### `textDocument/references`

Find all references to a symbol in the workspace.

**Request:**
```typescript
interface ReferenceParams {
  textDocument: TextDocumentIdentifier
  position: Position
  context: ReferenceContext
}

interface ReferenceContext {
  includeDeclaration: boolean
}
```

**Response:**
```typescript
Location[] | null
```

#### `textDocument/documentSymbol`

List all symbols in the current document.

**Request:**
```typescript
interface DocumentSymbolParams {
  textDocument: TextDocumentIdentifier
}
```

**Response:**
```typescript
interface DocumentSymbol {
  name: string
  detail?: string
  kind: SymbolKind
  deprecated?: boolean
  range: Range
  selectionRange: Range
  children?: DocumentSymbol[]
}
```

Symbol kinds include: File, Module, Namespace, Package, Class, Method, Property, Field, Constructor, Enum, Interface, Function, Variable, Constant, String, Number, Boolean, Array, Object, Key, Null, EnumMember, Struct, Event, Operator, TypeParameter.

#### `workspace/symbol`

Search for symbols by name across the workspace.

**Request:**
```typescript
interface WorkspaceSymbolParams {
  query: string
}
```

**Response:**
```typescript
SymbolInformation[] | null
```

#### `textDocument/completion`

Get code completion suggestions at a position.

**Request:**
```typescript
interface CompletionParams {
  textDocument: TextDocumentIdentifier
  position: Position
  context?: CompletionContext
}

interface CompletionContext {
  triggerKind: CompletionTriggerKind
  triggerCharacter?: string
}
```

**Response:**
```typescript
interface CompletionList {
  isIncomplete: boolean
  items: CompletionItem[]
}

interface CompletionItem {
  label: string
  kind?: CompletionItemKind
  detail?: string
  documentation?: string | MarkupContent
  sortText?: string
  filterText?: string
  insertText?: string
  textEdit?: TextEdit
  additionalTextEdits?: TextEdit[]
  command?: Command
}
```

#### `textDocument/signatureHelp`

Get function signature information.

**Request:**
```typescript
interface SignatureHelpParams {
  textDocument: TextDocumentIdentifier
  position: Position
  context?: SignatureHelpContext
}
```

**Response:**
```typescript
interface SignatureHelp {
  signatures: SignatureInformation[]
  activeSignature?: number
  activeParameter?: number
}

interface SignatureInformation {
  label: string
  documentation?: string | MarkupContent
  parameters?: ParameterInformation[]
  activeParameter?: number
}

interface ParameterInformation {
  label: string | [number, number]
  documentation?: string | MarkupContent
}
```

#### `textDocument/rename`

Rename a symbol and get all locations to update.

**Request:**
```typescript
interface RenameParams {
  textDocument: TextDocumentIdentifier
  position: Position
  newName: string
}
```

**Response:**
```typescript
interface WorkspaceEdit {
  changes?: { [uri: string]: TextEdit[] }
  documentChanges?: TextDocumentEdit[]
}

interface TextEdit {
  range: Range
  newText: string
}
```

#### `textDocument/diagnostic`

Get diagnostics (errors, warnings) for a document.

**Request:**
```typescript
interface DocumentDiagnosticParams {
  textDocument: TextDocumentIdentifier
}
```

**Response:**
```typescript
interface Diagnostic {
  range: Range
  severity?: DiagnosticSeverity
  code?: number | string
  source?: string
  message: string
  tags?: DiagnosticTag[]
  relatedInformation?: DiagnosticRelatedInformation[]
}
```

Severity levels: Error (1), Warning (2), Information (3), Hint (4).

### Custom Extensions

#### Files Extension

Request file contents from the client without direct file system access.

**Method:** `x/files`

Useful in cloud environments where files may not be directly accessible.

#### SymbolDescriptor Extension

Get descriptor information for a symbol and find all references.

**Method:** `x/references`

Request:
```typescript
interface SymbolDescriptorRequest {
  textDocument: TextDocumentIdentifier
  position: Position
}
```

Response includes descriptor information and reference locations.

#### Streaming Extension

Receive partial results progressively instead of waiting for complete results.

**Feature:** JSON Patches for progressive result delivery

Example: For large reference searches, results are streamed as they're found rather than batched.

**Method:** Supports `textDocument/references` with streaming

Uses JSON Patch format for incremental updates:
```json
{
  "jsonrpc": "2.0",
  "method": "$/progress",
  "params": {
    "token": "token-value",
    "value": [...]
  }
}
```

#### Packages Extension

Get information about project dependencies.

**Methods:**
- `x/dependencies` - Get all dependencies and their versions
- `x/dependents` - Get packages that depend on a symbol

## Data Types

### Position

```typescript
interface Position {
  line: number      // 0-based line number
  character: number // 0-based character offset
}
```

### Range

```typescript
interface Range {
  start: Position
  end: Position
}
```

### Location

```typescript
interface Location {
  uri: string // Document URI (e.g., "file:///path/to/file.ts")
  range: Range
}
```

### TextDocumentIdentifier

```typescript
interface TextDocumentIdentifier {
  uri: string
}
```

### VersionedTextDocumentIdentifier

```typescript
interface VersionedTextDocumentIdentifier extends TextDocumentIdentifier {
  version: number
}
```

## Error Handling

The server responds to requests with either a result or an error:

```typescript
interface ResponseError {
  code: number
  message: string
  data?: any
}
```

Common error codes:
- `-32700`: Parse error
- `-32600`: Invalid request
- `-32601`: Method not found
- `-32602`: Invalid params
- `-32603`: Internal error
- `-32000 to -32099`: Server error range

## Initialization Parameters

### Initialize Request

**Method:** `initialize`

**Request:**
```typescript
interface InitializeParams {
  processId: number | null
  rootPath?: string | null
  rootUri: string | null
  initializationOptions?: any
  capabilities: ClientCapabilities
  trace?: TraceValue
  workspaceFolders?: WorkspaceFolder[] | null
}
```

**Response:**
```typescript
interface InitializeResult {
  capabilities: ServerCapabilities
  serverInfo?: ServerInfo
}

interface ServerCapabilities {
  textDocumentSync?: TextDocumentSyncOptions | TextDocumentSyncKind
  hoverProvider?: boolean | HoverOptions
  completionProvider?: CompletionOptions
  signatureHelpProvider?: SignatureHelpOptions
  definitionProvider?: boolean | DefinitionOptions
  typeDefinitionProvider?: boolean | TypeDefinitionOptions
  implementationProvider?: boolean | ImplementationOptions
  referencesProvider?: boolean | ReferenceOptions
  documentHighlightProvider?: boolean | DocumentHighlightOptions
  documentSymbolProvider?: boolean | DocumentSymbolOptions
  workspaceSymbolProvider?: boolean | WorkspaceSymbolOptions
  codeActionProvider?: boolean | CodeActionOptions
  codeLensProvider?: CodeLensOptions
  documentFormattingProvider?: boolean | DocumentFormattingOptions
  documentRangeFormattingProvider?: boolean | DocumentRangeFormattingOptions
  documentOnTypeFormattingProvider?: DocumentOnTypeFormattingOptions
  renameProvider?: boolean | RenameOptions
  foldingRangeProvider?: boolean | FoldingRangeOptions
  executeCommandProvider?: ExecuteCommandOptions
  selectionRangeProvider?: boolean | SelectionRangeOptions
  linkedEditingRangeProvider?: boolean | LinkedEditingRangeOptions
  workspace?: WorkspaceServerCapabilities
}
```

## Notifications

### Client-to-Server Notifications

- `textDocument/didOpen` - Document opened
- `textDocument/didChange` - Document changed
- `textDocument/didClose` - Document closed
- `textDocument/didSave` - Document saved (if supported)
- `workspace/didChangeConfiguration` - Configuration changed
- `workspace/didChangeWorkspaceFolders` - Workspace folders changed

### Server-to-Client Notifications

- `textDocument/publishDiagnostics` - Push diagnostics to client
- `$/progress` - Progress updates for long-running operations
- `$/logTrace` - Logging information

## OpenTracing Integration

When Jaeger is enabled, the server creates spans for all major operations:

```typescript
interface SpanContext {
  traceId: string
  spanId: string
  flags: number
  // ... additional fields
}
```

Pass span context through the `meta` field of requests for distributed tracing:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/hover",
  "params": { ... },
  "meta": {
    "traceId": "...",
    "spanId": "..."
  }
}
```

View traces at http://localhost:16686 (when running with `--enable-jaeger`).

## Performance Characteristics

### Typical Response Times

- **Hover**: 0-50ms (local cache) to 100-500ms (new analysis)
- **Definition**: 50-200ms
- **References**: 100-500ms per 100 references
- **Completion**: 50-300ms
- **Rename**: 200-1000ms (depends on number of references)

### Memory Usage

- **Base**: ~100MB
- **Per 10 files**: ~5-10MB
- **Large projects (>1000 files)**: 500MB-1GB+

Adjust with `node --max-old-space-size=4096`.

## Completion Item Kinds

- Text (1)
- Method (2)
- Function (3)
- Constructor (4)
- Field (5)
- Variable (6)
- Class (7)
- Interface (8)
- Module (9)
- Property (10)
- Unit (11)
- Value (12)
- Enum (13)
- Keyword (14)
- Snippet (15)
- Color (16)
- File (17)
- Reference (18)
- Folder (19)
- EnumMember (20)
- Constant (21)
- Struct (22)
- Event (23)
- Operator (24)
- TypeParameter (25)
