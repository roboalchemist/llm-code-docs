# Source: https://github.com/davidhalter/parso/blob/master/docs/docs/usage.rst

# Usage

Parso works around grammars. You can simply create Python grammars by calling `parso.load_grammar()`. Grammars (with a custom tokenizer and custom parser trees) can also be created by directly instantiating `parso.Grammar`. More information about the resulting objects can be found in the [parser tree documentation](./parser-tree.md).

The simplest way of using parso is without even loading a grammar (`parso.parse()`):

```python
>>> import parso
>>> parso.parse('foo + bar')
<Module: @1-1>
```

## Loading a Grammar

Typically if you want to work with one specific Python version, use:

```python
parso.load_grammar(version=None, path=None)
```

Loads and returns a grammar. The default version is the current Python version.

**Parameters:**
- `version` (str): A string in the format `'3.9'` or `'3.10'` that specifies the Python version for which you want to parse.
- `path` (str): If you have a custom grammar file, you can also supply it here.

## Grammar Methods

You will get back a grammar object that you can use to parse code and find issues in it:

### Grammar.parse()

```python
Grammar.parse(code, *, error_recovery=True, start_symbol=None, cache=True, diff_cache=True)
```

Parses the given code and returns the parse tree.

**Parameters:**
- `code` (str or bytes): The code you want to parse.
- `error_recovery` (bool): If `True` (default), returns error nodes for invalid syntax. If `False`, raises `ParseError` for invalid syntax.
- `start_symbol` (str): Specifies which grammar rule to parse. The default is to parse a module.
- `cache` (bool): Store the parse tree in RAM for this code.
- `diff_cache` (bool): Store the parse tree on disk for incremental parsing.

**Returns:** A `parso.tree.NodeOrLeaf` object representing the parse tree.

### Grammar.iter_errors()

```python
Grammar.iter_errors(node)
```

Given a `parso.tree.NodeOrLeaf`, returns a generator of `parso.normalizer.Issue` objects.

## Error Retrieval

Parso is able to find multiple errors in your source code. Iterating through those errors yields the following instances:

### parso.normalizer.Issue

**Attributes:**
- `code` (int): An integer that represents the error type.
- `message` (str): A string representation of the error message.
- `start_pos` (tuple): A tuple `(line, column)` representing where the error starts.

## Utility Functions

Parso also offers some utility functions that can be really useful:

### parso.parse()

```python
parso.parse(code, *, version=None, error_recovery=True, start_symbol=None, cache=True, diff_cache=True)
```

A shortcut for loading a grammar and parsing code in one call. Internally does `parso.load_grammar(version).parse(code, ...)`.

### parso.split_lines()

```python
parso.split_lines(code, keepends=False)
```

Splits strings on `\n` and `\r\n` only (not on `\r`).

### parso.python_bytes_to_unicode()

```python
parso.python_bytes_to_unicode(source)
```

Converts Python source code to unicode, handling encoding declarations and BOMs (Byte Order Marks) correctly.

## Used By

- [jedi](https://github.com/davidhalter/jedi) - Used by IPython and a lot of editor plugins.
- [mutmut](https://github.com/boxed/mutmut) - Mutation testing framework.
