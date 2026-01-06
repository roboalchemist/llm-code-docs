# Source: https://raw.githubusercontent.com/microsoft/lsprotocol/main/packages/python/lsprotocol/types.py

# LSP Types Reference

# LSP Types Reference

This document provides a reference of the main types and enums available in the lsprotocol package.

## Enums and Classes

### SemanticTokenModifiers

"""A set of predefined token modifiers. This set is not fixed
an clients can specify additional token types via the
corresponding client capabilities.
@since 3.16.0"""
# Since: 3.16.0
Declaration = "declaration"
Definition = "definition"
Readonly = "readonly"
Static = "static"
Deprecated = "deprecated"
Abstract = "abstract"
Async = "async"
Modification = "modification"
Documentation = "documentation"
DefaultLibrary = "defaultLibrary"

### SemanticTokenModifiers

"""A set of predefined token modifiers. This set is not fixed
an clients can specify additional token types via the
corresponding client capabilities.
@since 3.16.0"""
# Since: 3.16.0
Declaration = "declaration"
Definition = "definition"
Readonly = "readonly"
Static = "static"
Deprecated = "deprecated"
Abstract = "abstract"
Async = "async"
Modification = "modification"
Documentation = "documentation"
DefaultLibrary = "defaultLibrary"

### DocumentDiagnosticReportKind

"""The document diagnostic report kinds.
@since 3.17.0"""
# Since: 3.17.0
Full = "full"
"""A diagnostic report with a full
set of problems."""
Unchanged = "unchanged"
"""A report indicating that the last
returned report is still accurate."""

### ErrorCodes

"""Predefined error codes."""
ParseError = -32700
InvalidRequest = -32600
MethodNotFound = -32601
InvalidParams = -32602
InternalError = -32603
ServerNotInitialized = -32002
"""Error code indicating that a server received a notification or
request before the server has received the `initialize` request."""
UnknownErrorCode = -32001

### LSPErrorCodes

RequestFailed = -32803
"""A request failed but it was syntactically correct, e.g the
method name was known and the parameters were valid. The error
message should contain human readable information about why
the request failed.
@since 3.17.0"""
# Since: 3.17.0
ServerCancelled = -32802
"""The server cancelled the request. This error code should
only be used for requests that explicitly support being
server cancellable.
@since 3.17.0"""
# Since: 3.17.0
ContentModified = -32801
"""The server detected that the content of a document got
modified outside normal conditions. A server should
NOT send this error code if it detects a content change
in it unprocessed messages. The result even computed
on an older state might still be useful for the client.
If a client decides that a result is not of any use anymore
the client should cancel the request."""
RequestCancelled = -32800
"""The client has canceled a request and a server has detected
the cancel."""

### LSPErrorCodes

RequestFailed = -32803
"""A request failed but it was syntactically correct, e.g the
method name was known and the parameters were valid. The error
message should contain human readable information about why
the request failed.
@since 3.17.0"""
# Since: 3.17.0
ServerCancelled = -32802
"""The server cancelled the request. This error code should
only be used for requests that explicitly support being
server cancellable.
@since 3.17.0"""
# Since: 3.17.0
ContentModified = -32801
"""The server detected that the content of a document got
modified outside normal conditions. A server should
NOT send this error code if it detects a content change
in it unprocessed messages. The result even computed
on an older state might still be useful for the client.
If a client decides that a result is not of any use anymore
the client should cancel the request."""
RequestCancelled = -32800
"""The client has canceled a request and a server has detected
the cancel."""

### FoldingRangeKind

"""A set of predefined range kinds."""
Comment = "comment"
"""Folding range for a comment"""
Imports = "imports"
"""Folding range for an import or include"""
Region = "region"
"""Folding range for a region (e.g. `#region`)"""

### FoldingRangeKind

"""A set of predefined range kinds."""
Comment = "comment"
"""Folding range for a comment"""
Imports = "imports"
"""Folding range for an import or include"""
Region = "region"
"""Folding range for a region (e.g. `#region`)"""

### SymbolKind

"""A symbol kind."""
File = 1
Module = 2
Namespace = 3
Package = 4
Class = 5
Method = 6
Property = 7
Field = 8
Constructor = 9
Enum = 10
Interface = 11
Function = 12
Variable = 13
Constant = 14
String = 15
Number = 16
Boolean = 17
Array = 18
Object = 19
Key = 20
Null = 21
EnumMember = 22
Struct = 23
Event = 24
Operator = 25
TypeParameter = 26

### SymbolKind

"""A symbol kind."""
File = 1
Module = 2
Namespace = 3
Package = 4
Class = 5
Method = 6
Property = 7
Field = 8
Constructor = 9
Enum = 10
Interface = 11
Function = 12
Variable = 13
Constant = 14
String = 15
Number = 16
Boolean = 17
Array = 18
Object = 19
Key = 20
Null = 21
EnumMember = 22
Struct = 23
Event = 24
Operator = 25
TypeParameter = 26

### SymbolTag

"""Symbol tags are extra annotations that tweak the rendering of a symbol.
@since 3.16"""
# Since: 3.16
Deprecated = 1
"""Render a symbol as obsolete, usually using a strike-out."""

### SymbolTag

"""Symbol tags are extra annotations that tweak the rendering of a symbol.
@since 3.16"""
# Since: 3.16
Deprecated = 1
"""Render a symbol as obsolete, usually using a strike-out."""

### UniquenessLevel

"""Moniker uniqueness level to define scope of the moniker.
@since 3.16.0"""
# Since: 3.16.0
Document = "document"
"""The moniker is only unique inside a document"""
Project = "project"
"""The moniker is unique inside a project for which a dump got created"""
Group = "group"
"""The moniker is unique inside the group to which a project belongs"""
Scheme = "scheme"
"""The moniker is unique inside the moniker scheme."""
Global = "global"
"""The moniker is globally unique"""

### UniquenessLevel

"""Moniker uniqueness level to define scope of the moniker.
@since 3.16.0"""
# Since: 3.16.0
Document = "document"
"""The moniker is only unique inside a document"""
Project = "project"
"""The moniker is unique inside a project for which a dump got created"""
Group = "group"
"""The moniker is unique inside the group to which a project belongs"""
Scheme = "scheme"
"""The moniker is unique inside the moniker scheme."""
Global = "global"
"""The moniker is globally unique"""

### MonikerKind

"""The moniker kind.
@since 3.16.0"""
# Since: 3.16.0
Import = "import"
"""The moniker represent a symbol that is imported into a project"""
Export = "export"
"""The moniker represents a symbol that is exported from a project"""
Local = "local"
"""The moniker represents a symbol that is local to a project (e.g. a local
variable of a function, a class not visible outside the project, ...)"""

### MonikerKind

"""The moniker kind.
@since 3.16.0"""
# Since: 3.16.0
Import = "import"
"""The moniker represent a symbol that is imported into a project"""
Export = "export"
"""The moniker represents a symbol that is exported from a project"""
Local = "local"
"""The moniker represents a symbol that is local to a project (e.g. a local
variable of a function, a class not visible outside the project, ...)"""

### InlayHintKind

"""Inlay hint kinds.
@since 3.17.0"""
# Since: 3.17.0
Type = 1
"""An inlay hint that for a type annotation."""
Parameter = 2
"""An inlay hint that is for a parameter."""

### InlayHintKind

"""Inlay hint kinds.
@since 3.17.0"""
# Since: 3.17.0
Type = 1
"""An inlay hint that for a type annotation."""
Parameter = 2
"""An inlay hint that is for a parameter."""

### MessageType

"""The message type"""
Error = 1
"""An error message."""
Warning = 2
"""A warning message."""
Info = 3
"""An information message."""
Log = 4
"""A log message."""
Debug = 5
"""A debug message.
@since 3.18.0
@proposed"""
# Since: 3.18.0
# Proposed

### MessageType

"""The message type"""
Error = 1
"""An error message."""
Warning = 2
"""A warning message."""
Info = 3
"""An information message."""
Log = 4
"""A log message."""
Debug = 5
"""A debug message.
@since 3.18.0
@proposed"""
# Since: 3.18.0
# Proposed

### TextDocumentSyncKind

"""Defines how the host (editor) should sync
document changes to the language server."""
None_ = 0
"""Documents should not be synced at all."""
Full = 1
"""Documents are synced by always sending the full content
of the document."""
Incremental = 2
"""Documents are synced by sending the full content on open.
After that only incremental updates to the document are
send."""

### TextDocumentSyncKind

"""Defines how the host (editor) should sync
document changes to the language server."""
None_ = 0
"""Documents should not be synced at all."""
Full = 1
"""Documents are synced by always sending the full content
of the document."""
Incremental = 2
"""Documents are synced by sending the full content on open.
After that only incremental updates to the document are
send."""

### TextDocumentSaveReason

"""Represents reasons why a text document is saved."""
Manual = 1
"""Manually triggered, e.g. by the user pressing save, by starting debugging,
or by an API call."""
AfterDelay = 2
"""Automatic after a delay."""
FocusOut = 3
"""When the editor lost focus."""

### TextDocumentSaveReason

"""Represents reasons why a text document is saved."""
Manual = 1
"""Manually triggered, e.g. by the user pressing save, by starting debugging,
or by an API call."""
AfterDelay = 2
"""Automatic after a delay."""
FocusOut = 3
"""When the editor lost focus."""


## Module Information

- **LSP Version:** 3.17.0
- **Generated File:** Yes (do not edit directly)
- **Generation Command:** `python -m nox --session build_lsp`
