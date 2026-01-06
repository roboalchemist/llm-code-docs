# GLSP API Reference

## Package Structure

GLSP is organized into several packages:

### glsp

The core package containing the foundational types and interfaces.

#### Context

```go
type Context struct {
	Method  string                    // The LSP method name
	Params  json.RawMessage           // Raw message parameters
	Notify  func(string, any)         // Send notification to client
	Call    func(string, any, any)    // Send request to client
	Context context.Context           // Go context for cancellation
}
```

Used to represent the execution context for each LSP method call.

#### NotifyFunc

```go
type NotifyFunc func(method string, params any)
```

Function signature for sending notifications to the client.

#### CallFunc

```go
type CallFunc func(method string, params any, result any)
```

Function signature for sending requests to the client.

#### Handler Interface

```go
type Handler interface {
	Handle(context *Context) (result any, validMethod bool, validParams bool, err error)
}
```

Core interface that all handlers must implement.

### server

Package for running the LSP server with various transports.

#### Server

```go
type Server struct {
	Handler              glsp.Handler
	LogBaseName          string
	Debug                bool
	Log                  commonlog.Logger
	Timeout              time.Duration
	ReadTimeout          time.Duration
	WriteTimeout         time.Duration
	StreamTimeout        time.Duration
	WebSocketTimeout     time.Duration
}
```

Main server struct managing JSON-RPC communication.

##### Constructor

```go
func NewServer(handler glsp.Handler, logName string, debug bool) *Server
```

Creates a new server with the specified handler, log name, and debug mode.

##### Methods

```go
// Run server on stdio
func (s *Server) RunStdio() error

// Run server on TCP
func (s *Server) RunTCP(address string) error

// Run server on WebSocket
func (s *Server) RunWebSocket(path string, address string) error
```

#### DefaultTimeout

```go
var DefaultTimeout = time.Minute
```

Default timeout for server operations (1 minute).

### protocol_3_16 / protocol_3_17

Protocol-specific packages containing LSP message structures and handler types.

#### Handler Type

```go
type Handler struct {
	// Lifecycle methods
	Initialize  func(*glsp.Context, *InitializeParams) (any, error)
	Initialized func(*glsp.Context, *InitializedParams) error
	Shutdown    func(*glsp.Context) error
	SetTrace    func(*glsp.Context, *SetTraceParams) error

	// Feature handlers (text document synchronization)
	DidOpen    func(*glsp.Context, *DidOpenTextDocumentParams) error
	DidChange  func(*glsp.Context, *DidChangeTextDocumentParams) error
	DidClose   func(*glsp.Context, *DidCloseTextDocumentParams) error
	WillSave   func(*glsp.Context, *WillSaveTextDocumentParams) error
	DidSave    func(*glsp.Context, *DidSaveTextDocumentParams) error

	// Language feature handlers
	Completion          func(*glsp.Context, *CompletionParams) (*CompletionList, error)
	CompletionItemResolve func(*glsp.Context, *CompletionItem) (*CompletionItem, error)
	Hover               func(*glsp.Context, *HoverParams) (*Hover, error)
	SignatureHelp       func(*glsp.Context, *SignatureHelpParams) (*SignatureHelp, error)
	Definition          func(*glsp.Context, *DefinitionParams) ([]Location, error)
	References          func(*glsp.Context, *ReferenceParams) ([]Location, error)
	DocumentSymbol      func(*glsp.Context, *DocumentSymbolParams) ([]DocumentSymbol, error)
	WorkspaceSymbol     func(*glsp.Context, *WorkspaceSymbolParams) ([]SymbolInformation, error)
	CodeAction          func(*glsp.Context, *CodeActionParams) ([]CodeAction, error)
	Diagnostic          func(*glsp.Context, *TextDocumentItem) ([]Diagnostic, error)

	// Additional handlers...
}
```

#### Key Message Types

**InitializeParams**
- Sent by client to initialize the server
- Contains client capabilities and workspace information

**InitializeResult**
- Response from server
- Contains server capabilities
- Includes optional server info (name, version)

**InitializedParams**
- Sent by client after receiving initialize result
- Signals that client has processed initialization

**DidOpenTextDocumentParams**
- Sent when client opens a text document
- Contains document URI and initial content

**DidChangeTextDocumentParams**
- Sent when client modifies a text document
- Contains change events with ranges and new text

**DidCloseTextDocumentParams**
- Sent when client closes a text document

**CompletionParams**
- Sent when requesting code completion
- Contains position in document

**HoverParams**
- Sent when requesting hover information
- Contains position in document

**Hover**
- Response containing hover information
- Includes markup content

## Common Patterns

### Creating a Basic Server

```go
package main

import (
	"github.com/tliron/glsp"
	protocol "github.com/tliron/glsp/protocol_3_16"
	"github.com/tliron/glsp/server"
)

func main() {
	handler := protocol.Handler{
		Initialize: handleInitialize,
	}

	server := server.NewServer(&handler, "my-language-server", false)
	server.RunStdio()
}

func handleInitialize(ctx *glsp.Context, params *protocol.InitializeParams) (any, error) {
	// Return server capabilities
	return protocol.InitializeResult{
		Capabilities: protocol.ServerCapabilities{
			// Define what features your server supports
		},
	}, nil
}
```

### Adding Text Document Synchronization

```go
handler := protocol.Handler{
	Initialize:  handleInitialize,
	DidOpen:     handleDidOpen,
	DidChange:   handleDidChange,
	DidClose:    handleDidClose,
}

func handleDidOpen(ctx *glsp.Context, params *protocol.DidOpenTextDocumentParams) error {
	// Process document open event
	return nil
}

func handleDidChange(ctx *glsp.Context, params *protocol.DidChangeTextDocumentParams) error {
	// Process document changes
	return nil
}

func handleDidClose(ctx *glsp.Context, params *protocol.DidCloseTextDocumentParams) error {
	// Process document close event
	return nil
}
```

### Implementing Code Completion

```go
handler := protocol.Handler{
	Completion: handleCompletion,
}

func handleCompletion(ctx *glsp.Context, params *protocol.CompletionParams) (*protocol.CompletionList, error) {
	return &protocol.CompletionList{
		IsIncomplete: false,
		Items: []protocol.CompletionItem{
			{
				Label: "example",
				Kind:  protocol.CompletionItemKindKeyword,
			},
		},
	}, nil
}
```

### Sending Diagnostics

```go
func publishDiagnostics(ctx *glsp.Context, uri string, diagnostics []protocol.Diagnostic) {
	ctx.Notify("textDocument/publishDiagnostics", protocol.PublishDiagnosticsParams{
		URI:         uri,
		Diagnostics: diagnostics,
	})
}
```

## Error Handling

When implementing handlers, return errors that will be sent back to the client:

```go
func handleInitialize(ctx *glsp.Context, params *protocol.InitializeParams) (any, error) {
	if params == nil {
		return nil, errors.New("initialize params cannot be nil")
	}
	// Process initialization
	return result, nil
}
```

## Logging

GLSP uses the `github.com/tliron/commonlog` package for logging. Configure it in your server:

```go
import "github.com/tliron/commonlog"

// Set verbosity (0 = errors only, 1 = info, 2 = debug)
commonlog.Configure(1, nil)
```

## Transport Configuration

### Timeout Configuration

```go
server := server.NewServer(&handler, "my-ls", false)
server.Timeout = 2 * time.Minute
server.ReadTimeout = 30 * time.Second
server.WriteTimeout = 30 * time.Second
server.RunStdio()
```

### Running on TCP

```go
server := server.NewServer(&handler, "my-ls", false)
server.RunTCP("localhost:8080")
```

### Running on WebSocket

```go
server := server.NewServer(&handler, "my-ls", false)
server.RunWebSocket("/lsp", "localhost:8080")
```

## Server Capabilities

Define your server's capabilities in the Initialize response:

```go
capabilities := protocol.ServerCapabilities{
	TextDocumentSync: protocol.TextDocumentSyncOptionsOrKind{
		Kind: protocol.TextDocumentSyncKindFull,
	},
	CompletionProvider: &protocol.CompletionOptions{
		ResolveProvider: true,
	},
	HoverProvider: true,
	DefinitionProvider: true,
}
```

See the LSP specification for all available capabilities.
