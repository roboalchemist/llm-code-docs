# Source: https://www.daytona.io/docs/en/language-server-protocol.md

The Daytona SDK provides Language Server Protocol (LSP) support through Sandbox instances. This enables advanced language features like code completion, diagnostics, and more.

## Creating LSP Servers

Daytona SDK provides an option to create LSP servers in Python, TypeScript, and Ruby. The `path_to_project` argument is relative to the current Sandbox working directory when no leading `/` is used. The working directory is specified by WORKDIR when it is present in the Dockerfile, and otherwise falls back to the user's home directory.

```python
from daytona import Daytona, LspLanguageId

# Create Sandbox
daytona = Daytona()
sandbox = daytona.create()

# Create LSP server for Python
lsp_server = sandbox.create_lsp_server(
    language_id=LspLanguageId.PYTHON,
    path_to_project="workspace/project"
)

```
```typescript
import { Daytona, LspLanguageId } from '@daytonaio/sdk'

// Create sandbox
const daytona = new Daytona()
const sandbox = await daytona.create({
    language: 'typescript'
})

// Create LSP server for TypeScript
const lspServer = await sandbox.createLspServer(
    LspLanguageId.TYPESCRIPT,
    "workspace/project"
)
```


```ruby
require 'daytona'

# Create Sandbox
daytona = Daytona::Daytona.new
sandbox = daytona.create

# Create LSP server for Python
lsp_server = sandbox.create_lsp_server(
  language_id: Daytona::LspServer::Language::PYTHON,
  path_to_project: 'workspace/project'
)

# Create LSP server for TypeScript
lsp_server = sandbox.create_lsp_server(
  language_id: Daytona::LspServer::Language::TYPESCRIPT,
  path_to_project: 'workspace/project'
)
```


See: [create_lsp_server (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/sandbox.md#sandboxcreate_lsp_server), [createLspServer (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/sandbox.md#createlspserver), [create_lsp_server (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/sandbox.md#create_lsp_server)

### Supported Languages

The supported languages for creating LSP servers with the Daytona SDK are defined by the `LspLanguageId` enum:

| Enum Value                   | Description                         |
|------------------------------|-------------------------------------|
| `LspLanguageId.PYTHON`       | Python language server.             |
| `LspLanguageId.TYPESCRIPT`   | TypeScript/JavaScript language server. |

See: [LspLanguageId (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/lsp-server.md#lsplanguageid), [LspLanguageId (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/lsp-server.md#lsplanguageid)

## LSP Features

Daytona SDK provides LSP features for code analysis and editing.

### Code Completion

Daytona SDK provides an option to get code completions for a specific position in a file using Python, TypeScript, and Ruby.

```python
completions = lsp_server.completions(
    path="workspace/project/main.py",
    position={"line": 10, "character": 15}
)
print(f"Completions: {completions}")
```
```typescript
const completions = await lspServer.completions(
    "workspace/project/main.ts",
    { line: 10, character: 15 }
)
console.log('Completions:', completions)
```

```ruby
completions = lsp_server.completions(
  path: 'workspace/project/main.py',
  position: Daytona::LspServer::Position.new(line: 10, character: 15)
)
puts "Completions: #{completions}"
```

See: [completions (Python SDK)](https://www.daytona.io/docs/python-sdk/sync/lsp-server.md#lspservercompletions), [completions (TypeScript SDK)](https://www.daytona.io/docs/typescript-sdk/lsp-server.md#completions), [completions (Ruby SDK)](https://www.daytona.io/docs/ruby-sdk/lsp-server.md#completions)