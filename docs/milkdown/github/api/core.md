# Source: https://github.com/Milkdown/milkdown/blob/main/docs/api/core.md

# @milkdown/core

The core module for milkdown.

# Editor

@Editor

@EditorStatus
@OnStatusChange

---

# Internal Plugins

## Config

@config

### Config Timer

@ConfigReady

## Init

@init

### Init Timer

@InitReady

### Init Slice

@initTimerCtx

@editorCtx
@prosePluginsCtx
@inputRulesCtx
@nodeViewCtx
@markViewCtx

@remarkPluginsCtx
@remarkCtx
@remarkStringifyOptionsCtx

## Schema

@schema

### Schema Timer

@SchemaReady

### Schema Slice

@schemaTimerCtx

@nodesCtx
@marksCtx
@schemaCtx

## Parser

@parser

### Parser Timer

@ParserReady

### Parser Slice

@parserTimerCtx

@parserCtx

## Serializer

@serializer

### Serializer Timer

@SerializerReady

### Serializer Slice

@serializerTimerCtx

@serializerCtx

## Commands

@commands
@CommandManager
@createCmdKey

@CommandChain

### Commands Timer

@CommandsReady

### Commands Slice

@commandsTimerCtx

@commandsCtx

## Keymap

@keymap
@KeymapManager

### Keymap Timer

@KeymapReady

### Keymap Slice

@keymapTimerCtx

@keymapCtx

## Paste Rules

@pasteRule

### PasteRules Timer

@PasteRulesReady

### PasteRules Slice

@pasteRulesTimerCtx

@pasteRulesCtx
@PasteRule

## EditorState

@editorState

### EditorState Timer

@EditorStateReady

### EditorState Slice

@editorStateTimerCtx

@editorStateCtx
@editorStateOptionsCtx

## EditorView

@editorView

### EditorView Timer

@EditorViewReady

### EditorView Ctx

@editorViewTimerCtx

@defaultValueCtx
@rootCtx
@rootDOMCtx
@rootAttrsCtx

@editorViewCtx
@editorViewOptionsCtx
