# Source: https://github.com/davidhalter/parso/blob/master/docs/docs/parser-tree.rst

# Parser Tree

The parser tree is returned by calling `parso.Grammar.parse()`.

**Note:** Parso positions are always 1-based for lines and 0-based for columns. This means the first position in a file is (1, 0).

## Parser Tree Base Classes

Generally there are two types of classes you will deal with: `parso.tree.Leaf` and `parso.tree.BaseNode`.

### parso.tree.BaseNode

A `BaseNode` is a node that contains other nodes/leaves. It's the parent type for all other node classes.

**Common attributes and methods:**

- `children` (list): List of child nodes and leaves.
- `type` (str): The type of this node (e.g., 'file_input', 'simple_stmt').
- `start_pos` (tuple): A tuple `(line, column)` representing the start position.
- `end_pos` (tuple): A tuple `(line, column)` representing the end position.
- `parent` (BaseNode or None): The parent node, or `None` if this is the root.

**Methods:**

- `children` - List of child nodes/leaves.
- `get_code()` - Returns the code represented by this node as a string.
- `get_first_leaf()` - Returns the first leaf node in this tree.
- `get_last_leaf()` - Returns the last leaf node in this tree.
- `get_next_sibling()` - Returns the next sibling node.
- `get_previous_sibling()` - Returns the previous sibling node.

### parso.tree.Leaf

A `Leaf` is a terminal node in the parse tree that represents a single token (like an identifier, operator, or keyword).

**Common attributes:**

- `value` (str): The string content of this leaf.
- `type` (str): The type of this leaf (e.g., 'NAME', 'OP', 'NUMBER').
- `start_pos` (tuple): A tuple `(line, column)` representing the start position.
- `end_pos` (tuple): A tuple `(line, column)` representing the end position.
- `parent` (BaseNode or None): The parent node.

**Methods:**

- `get_code()` - Returns the code represented by this leaf as a string.
- `get_next_sibling()` - Returns the next sibling node.
- `get_previous_sibling()` - Returns the previous sibling node.

### parso.tree.NodeOrLeaf

All nodes and leaves have these methods/properties (this is the base class for both `BaseNode` and `Leaf`):

**Common methods:**

- `get_root_node()` - Returns the root node of the tree.
- `get_code()` - Returns the code represented by this node/leaf as a string.
- `get_first_leaf()` - Returns the first leaf node in this tree.
- `get_last_leaf()` - Returns the last leaf node in this tree.
- `get_next_sibling()` - Returns the next sibling node, or `None` if this is the last sibling.
- `get_previous_sibling()` - Returns the previous sibling node, or `None` if this is the first sibling.
- `get_next_leaf()` - Returns the next leaf in the entire tree.
- `get_previous_leaf()` - Returns the previous leaf in the entire tree.
- `search_ancestor(*types)` - Returns an ancestor with one of the given types, or `None`.

**Properties:**

- `parent` - The parent node.
- `type` - The type of the node/leaf.
- `start_pos` - A tuple `(line, column)` representing the start position (1-based line, 0-based column).
- `end_pos` - A tuple `(line, column)` representing the end position.

## Python Parser Tree

The Python-specific parser tree extends the base classes with additional node types.

### parso.python.tree

Python-specific tree nodes represent Python language constructs such as:

- `PythonNode` - A node representing a Python grammar rule.
- `PythonLeaf` - A leaf representing a Python token.
- `Name` - Represents a name/identifier.
- `Number` - Represents a numeric literal.
- `String` - Represents a string literal.
- `Operator` - Represents an operator.
- `Keyword` - Represents a keyword.

These classes extend the base `BaseNode` and `Leaf` classes with Python-specific functionality.

## Utility

### parso.tree.search_ancestor()

```python
parso.tree.search_ancestor(node, *types)
```

Returns an ancestor of the given node with one of the given types, or `None` if no such ancestor exists.

**Parameters:**
- `node` (NodeOrLeaf): The node to start searching from.
- `*types` (str): The types to search for.

**Returns:** A `NodeOrLeaf` with one of the given types, or `None`.

**Example:**

```python
>>> import parso
>>> module = parso.parse('x = 1')
>>> leaf = module.get_first_leaf()
>>> parso.tree.search_ancestor(leaf, 'file_input')
<Module: @1-1>
```
