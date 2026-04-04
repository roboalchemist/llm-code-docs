# GLSP - Language Server Protocol SDK for Go

**Source:** https://github.com/tliron/glsp

## Overview

GLSP is a Language Server Protocol (LSP) SDK for Go that simplifies the implementation of language servers. It provides pre-built message structures, handlers, and a ready-to-run JSON-RPC 2.0 server, allowing developers to focus on language-specific features rather than protocol details.

## Key Features

GLSP includes:

1. **All message structures** - Easy serialization of LSP protocol messages
2. **Handler for client methods** - Map your code to LSP specification methods
3. **Ready-to-run JSON-RPC 2.0 server** - Supports multiple communication protocols:
   - stdio (standard input/output)
   - TCP
   - WebSockets
   - Node.js IPC

## Installation

```bash
go get github.com/tliron/glsp
```

## Quick Start

### Minimal Example

```go
package main

import (
	"github.com/tliron/glsp"
	protocol "github.com/tliron/glsp/protocol_3_16"
	"github.com/tliron/glsp/server"
	"github.com/tliron/commonlog"

	// Must include a backend implementation
	// See CommonLog for other options: https://github.com/tliron/commonlog
	_ "github.com/tliron/commonlog/simple"
)

const lsName = "my language"

var (
	version string = "0.0.1"
	handler protocol.Handler
)

func main() {
	// This increases logging verbosity (optional)
	commonlog.Configure(1, nil)

	handler = protocol.Handler{
		Initialize:  initialize,
		Initialized: initialized,
		Shutdown:    shutdown,
		SetTrace:    setTrace,
	}

	server := server.NewServer(&handler, lsName, false)

	server.RunStdio()
}

func initialize(context *glsp.Context, params *protocol.InitializeParams) (any, error) {
	capabilities := handler.CreateServerCapabilities()

	return protocol.InitializeResult{
		Capabilities: capabilities,
		ServerInfo: &protocol.InitializeResultServerInfo{
			Name:    lsName,
			Version: &version,
		},
	}, nil
}

func initialized(context *glsp.Context, params *protocol.InitializedParams) error {
	return nil
}

func shutdown(context *glsp.Context) error {
	protocol.SetTraceValue(protocol.TraceValueOff)
	return nil
}

func setTrace(context *glsp.Context, params *protocol.SetTraceParams) error {
	protocol.SetTraceValue(params.Value)
	return nil
}
```

## Core Concepts

### Context

The `glsp.Context` struct contains:
- `Method` - The LSP method name
- `Params` - Raw message parameters
- `Notify` - Function to send notifications to the client
- `Call` - Function to send requests to the client
- `Context` - Go context for cancellation

### Handler

GLSP uses a `protocol.Handler` struct to map your code to LSP lifecycle methods and feature handlers:

```go
type Handler struct {
	Initialize  func(*glsp.Context, *protocol.InitializeParams) (any, error)
	Initialized func(*glsp.Context, *protocol.InitializedParams) error
	Shutdown    func(*glsp.Context) error
	SetTrace    func(*glsp.Context, *protocol.SetTraceParams) error
	// ... additional handlers for language features
}
```

### Server

The `server.Server` type manages the JSON-RPC communication:

```go
type Server struct {
	Handler              glsp.Handler
	LogBaseName          string
	Debug                bool
	Timeout              time.Duration
	ReadTimeout          time.Duration
	WriteTimeout         time.Duration
	StreamTimeout        time.Duration
	WebSocketTimeout     time.Duration
}

// Create a new server
server := server.NewServer(&handler, "my language", false)

// Run the server with stdio transport
server.RunStdio()

// Or use other transports
server.RunTCP(":8080")
server.RunWebSocket("/ws", ":8080")
```

## Protocol Versions

GLSP supports multiple LSP protocol versions:

- **protocol_3_16** - LSP 3.16.x
- **protocol_3_17** - LSP 3.17.x

Import the appropriate package based on your requirements:

```go
import protocol "github.com/tliron/glsp/protocol_3_16"
// or
import protocol "github.com/tliron/glsp/protocol_3_17"
```

## Transport Methods

### stdio

```go
server.RunStdio()
```

Communicates via standard input/output. Ideal for editor integrations.

### TCP

```go
server.RunTCP(":8080")
```

Communicates over TCP on a specified host:port.

### WebSocket

```go
server.RunWebSocket("/ws", ":8080")
```

Communicates over WebSocket protocol with optional HTTP endpoint.

### Node.js IPC

```go
// Node.js IPC support available
// See source code for implementation details
```

## Implementing Language Features

To implement language-specific features, extend the handler with appropriate callbacks:

```go
handler = protocol.Handler{
	Initialize:  initialize,
	Initialized: initialized,
	Shutdown:    shutdown,
	SetTrace:    setTrace,
	// Add more handlers for:
	// - Text document completion
	// - Hover information
	// - Diagnostic messages
	// - Symbol navigation
	// And more...
}
```

Refer to the LSP specification at https://microsoft.github.io/language-server-protocol/ for available methods.

## Dependencies

GLSP has minimal dependencies:

- `github.com/gorilla/websocket` - WebSocket support
- `github.com/pkg/errors` - Error handling
- `github.com/sourcegraph/jsonrpc2` - JSON-RPC 2.0 protocol
- `github.com/tliron/commonlog` - Logging

## Real-World Examples

Projects using GLSP:

- **[Puccini TOSCA Language Server](https://github.com/tliron/puccini-language-server)** - LSP server for the TOSCA language
- **[zk](https://github.com/mickael-menu/zk)** - A command-line Zettelkasten note-taking app

## Related Projects

- **[go-lsp](https://github.com/sourcegraph/go-lsp)** - Another LSP implementation with reduced protocol coverage

## Important Notes

- This is an early release - some features are not yet fully implemented
- See the LSP specification for complete protocol documentation
- CommonLog provides flexible logging configuration options

## Status & License

- **Status:** Early release
- **License:** Apache 2.0
- **Go Version:** 1.22+

## References

- **Language Server Protocol:** https://microsoft.github.io/language-server-protocol/
- **GitHub Repository:** https://github.com/tliron/glsp
- **Go Package Documentation:** https://pkg.go.dev/github.com/tliron/glsp
