# Source: https://ast-grep.github.io/catalog/python.md

---
url: /catalog/python.md
---
# Python

This page curates a list of example ast-grep rules to check and to rewrite Python code.

## Migrate OpenAI SDK&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiZGVmICRGVU5DKCQkJEFSR1MpOiAkJCRCT0RZIiwicmV3cml0ZSI6IiIsImNvbmZpZyI6InJ1bGU6XG4gIHBhdHRlcm46IGltcG9ydCBvcGVuYWlcbmZpeDogZnJvbSBvcGVuYWkgaW1wb3J0IENsaWVudFxuLS0tXG5ydWxlOlxuICBwYXR0ZXJuOiBvcGVuYWkuYXBpX2tleSA9ICRLRVlcbmZpeDogY2xpZW50ID0gQ2xpZW50KCRLRVkpXG4tLS1cbnJ1bGU6XG4gIHBhdHRlcm46IG9wZW5haS5Db21wbGV0aW9uLmNyZWF0ZSgkJCRBUkdTKVxuZml4OiB8LVxuICBjbGllbnQuY29tcGxldGlvbnMuY3JlYXRlKFxuICAgICQkJEFSR1NcbiAgKSIsInNvdXJjZSI6ImltcG9ydCBvc1xuaW1wb3J0IG9wZW5haVxuZnJvbSBmbGFzayBpbXBvcnQgRmxhc2ssIGpzb25pZnlcblxuYXBwID0gRmxhc2soX19uYW1lX18pXG5vcGVuYWkuYXBpX2tleSA9IG9zLmdldGVudihcIk9QRU5BSV9BUElfS0VZXCIpXG5cblxuQGFwcC5yb3V0ZShcIi9jaGF0XCIsIG1ldGhvZHM9KFwiUE9TVFwiKSlcbmRlZiBpbmRleCgpOlxuICAgIGFuaW1hbCA9IHJlcXVlc3QuZm9ybVtcImFuaW1hbFwiXVxuICAgIHJlc3BvbnNlID0gb3BlbmFpLkNvbXBsZXRpb24uY3JlYXRlKFxuICAgICAgICBtb2RlbD1cInRleHQtZGF2aW5jaS0wMDNcIixcbiAgICAgICAgcHJvbXB0PWdlbmVyYXRlX3Byb21wdChhbmltYWwpLFxuICAgICAgICB0ZW1wZXJhdHVyZT0wLjYsXG4gICAgKVxuICAgIHJldHVybiBqc29uaWZ5KHJlc3BvbnNlLmNob2ljZXMpIn0=)

### Description

OpenAI has introduced some breaking changes in their API, such as using `Client` to initialize the service and renaming the `Completion` method to `completions` . This example shows how to use ast-grep to automatically update your code to the new API.

API migration requires multiple related rules to work together.
The example shows how to write [multiple rules](/reference/playground.html#test-multiple-rules) in a [single YAML](/guide/rewrite-code.html#using-fix-in-yaml-rule) file.
The rules and patterns in the example are simple and self-explanatory, so we will not explain them further.

### YAML

```yaml
id: import-openai
language: python
rule:
  pattern: import openai
fix: from openai import Client
---
id: rewrite-client
language: python
rule:
  pattern: openai.api_key = $KEY
fix: client = Client($KEY)
---
id: rewrite-chat-completion
language: python
rule:
  pattern: openai.Completion.create($$$ARGS)
fix: |-
  client.completions.create(
    $$$ARGS
  )
```

### Example

```python {2,6,11-15}
import os
import openai
from flask import Flask, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=("POST"))
def index():
    animal = request.form["animal"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(animal),
        temperature=0.6,
    )
    return jsonify(response.choices)
```

### Diff

```python
import os
import openai # [!code --]
from openai import Client # [!code ++]
from flask import Flask, jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY") # [!code --]
client = Client(os.getenv("OPENAI_API_KEY")) # [!code ++]

@app.route("/chat", methods=("POST"))
def index():
    animal = request.form["animal"]
    response = openai.Completion.create( # [!code --]
    response = client.completions.create( # [!code ++]
      model="text-davinci-003",
      prompt=generate_prompt(animal),
      temperature=0.6,
    )
    return jsonify(response.choices)
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim), inspired by [Morgante](https://twitter.com/morgantepell/status/1721668781246750952) from [grit.io](https://www.grit.io/)

## Prefer Generator Expressions&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiWyQkJEFdIiwicmV3cml0ZSI6IiRBPy4oKSIsImNvbmZpZyI6InJ1bGU6XG4gIHBhdHRlcm46ICRGVU5DKCRMSVNUKVxuY29uc3RyYWludHM6XG4gIExJU1Q6IHsga2luZDogbGlzdF9jb21wcmVoZW5zaW9uIH1cbiAgRlVOQzpcbiAgICBhbnk6XG4gICAgICAtIHBhdHRlcm46IGFueVxuICAgICAgLSBwYXR0ZXJuOiBhbGxcbiAgICAgIC0gcGF0dGVybjogc3VtXG4gICAgICAjIC4uLlxudHJhbnNmb3JtOlxuICBJTk5FUjpcbiAgICBzdWJzdHJpbmc6IHtzb3VyY2U6ICRMSVNULCBzdGFydENoYXI6IDEsIGVuZENoYXI6IC0xIH1cbmZpeDogJEZVTkMoJElOTkVSKSIsInNvdXJjZSI6ImFsbChbeCBmb3IgeCBpbiB5XSlcblt4IGZvciB4IGluIHldIn0=)

### Description

List comprehensions like `[x for x in range(10)]` are a concise way to create lists in Python. However, we can achieve better memory efficiency by using generator expressions like `(x for x in range(10))` instead. List comprehensions create the entire list in memory, while generator expressions generate each element one at a time. We can make the change by replacing the square brackets with parentheses.

### YAML

```yaml
id: prefer-generator-expressions
language: python
rule:
  pattern: $LIST
  kind: list_comprehension
transform:
  INNER:
    substring: {source: $LIST, startChar: 1, endChar: -1 }
fix: ($INNER)
```

This rule converts every list comprehension to a generator expression. However, **not every list comprehension can be replaced with a generator expression.** If the list is used multiple times, is modified, is sliced, or is indexed, a generator is not a suitable replacement.

Some common functions like `any`, `all`, and `sum` take an `iterable` as an argument. A generator function counts as an `iterable`, so it is safe to change a list comprehension to a generator expression in this context.

```yaml
id: prefer-generator-expressions
language: python
rule:
  pattern: $FUNC($LIST)
constraints:
  LIST: { kind: list_comprehension }
  FUNC:
    any:
      - pattern: any
      - pattern: all
      - pattern: sum
      # ...
transform:
  INNER:
    substring: {source: $LIST, startChar: 1, endChar: -1 }
fix: $FUNC($INNER)
```

### Example

```python
any([x for x in range(10)])
```

### Diff

```python
any([x for x in range(10)]) # [!code --]
any(x for x in range(10)) # [!code ++]
```

### Contributed by

[Steven Love](https://github.com/StevenLove)

## Use Walrus Operator in `if` statement

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiZm4gbWFpbigpIHsgXG4gICAgJCQkO1xuICAgIGlmKCRBKXskJCRCfSBcbiAgICBpZigkQSl7JCQkQ30gXG4gICAgJCQkRlxufSIsInJld3JpdGUiOiJmbiBtYWluKCkgeyAkJCRFOyBpZigkQSl7JCQkQiAkJCRDfSAkJCRGfSIsImNvbmZpZyI6ImlkOiB1c2Utd2FscnVzLW9wZXJhdG9yXG5ydWxlOlxuICBmb2xsb3dzOlxuICAgIHBhdHRlcm46XG4gICAgICBjb250ZXh0OiAkVkFSID0gJCQkRVhQUlxuICAgICAgc2VsZWN0b3I6IGV4cHJlc3Npb25fc3RhdGVtZW50XG4gIHBhdHRlcm46IFwiaWYgJFZBUjogJCQkQlwiXG5maXg6IHwtXG4gIGlmICRWQVIgOj0gJCQkRVhQUjpcbiAgICAkJCRCXG4tLS1cbmlkOiByZW1vdmUtZGVjbGFyYXRpb25cbnJ1bGU6XG4gIHBhdHRlcm46XG4gICAgY29udGV4dDogJFZBUiA9ICQkJEVYUFJcbiAgICBzZWxlY3RvcjogZXhwcmVzc2lvbl9zdGF0ZW1lbnRcbiAgcHJlY2VkZXM6XG4gICAgcGF0dGVybjogXCJpZiAkVkFSOiAkJCRCXCJcbmZpeDogJyciLCJzb3VyY2UiOiJhID0gZm9vKClcblxuaWYgYTpcbiAgICBkb19iYXIoKSJ9)

### Description

The walrus operator (`:=`) introduced in Python 3.8 allows you to assign values to variables as part of an expression. This rule aims to simplify code by using the walrus operator in `if` statements.

This first part of the rule identifies cases where a variable is assigned a value and then immediately used in an `if` statement to control flow.

```yaml
id: use-walrus-operator
language: python
rule:
  pattern: "if $VAR: $$$B"
  follows:
    pattern:
      context: $VAR = $$$EXPR
      selector: expression_statement
fix: |-
  if $VAR := $$$EXPR:
    $$$B
```

The `pattern` clause finds an `if` statement that checks the truthiness of `$VAR`.
If this pattern `follows` an expression statement where `$VAR` is assigned `$$$EXPR`, the `fix` clause changes the `if` statements to use the walrus operator.

The second part of the rule:

```yaml
id: remove-declaration
rule:
  pattern:
    context: $VAR = $$$EXPR
    selector: expression_statement
  precedes:
    pattern: "if $VAR: $$$B"
fix: ''
```

This rule removes the standalone variable assignment when it directly precedes an `if` statement that uses the walrus operator. Since the assignment is now part of the `if` statement, the separate declaration is no longer needed.

By applying these rules, you can refactor your Python code to be more concise and readable, taking advantage of the walrus operator's ability to combine an assignment with an expression.

### YAML

```yaml
id: use-walrus-operator
language: python
rule:
  follows:
    pattern:
      context: $VAR = $$$EXPR
      selector: expression_statement
  pattern: "if $VAR: $$$B"
fix: |-
  if $VAR := $$$EXPR:
    $$$B
---
id: remove-declaration
language: python
rule:
  pattern:
    context: $VAR = $$$EXPR
    selector: expression_statement
  precedes:
    pattern: "if $VAR: $$$B"
fix: ''
```

### Example

```python
a = foo()

if a:
    do_bar()
```

### Diff

```python
a = foo() # [!code --]

if a: # [!code --]
if a := foo(): # [!code ++]
    do_bar()
```

### Contributed by

Inspired by reddit user [/u/jackerhack](https://www.reddit.com/r/rust/comments/13eg738/comment/kagdklw/?)

## Remove `async` function&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiYXdhaXQgJCQkQ0FMTCIsInJld3JpdGUiOiIkJCRDQUxMICIsImNvbmZpZyI6ImlkOiByZW1vdmUtYXN5bmMtZGVmXG5sYW5ndWFnZTogcHl0aG9uXG5ydWxlOlxuICBwYXR0ZXJuOlxuICAgIGNvbnRleHQ6ICdhc3luYyBkZWYgJEZVTkMoJCQkQVJHUyk6ICQkJEJPRFknXG4gICAgc2VsZWN0b3I6IGZ1bmN0aW9uX2RlZmluaXRpb25cbnRyYW5zZm9ybTpcbiAgUkVNT1ZFRF9CT0RZOlxuICAgIHJld3JpdGU6XG4gICAgICByZXdyaXRlcnM6IFtyZW1vdmUtYXdhaXQtY2FsbF1cbiAgICAgIHNvdXJjZTogJCQkQk9EWVxuZml4OiB8LVxuICBkZWYgJEZVTkMoJCQkQVJHUyk6XG4gICAgJFJFTU9WRURfQk9EWVxucmV3cml0ZXJzOlxuLSBpZDogcmVtb3ZlLWF3YWl0LWNhbGxcbiAgcnVsZTpcbiAgICBwYXR0ZXJuOiAnYXdhaXQgJCQkQ0FMTCdcbiAgZml4OiAkJCRDQUxMXG4iLCJzb3VyY2UiOiJhc3luYyBkZWYgbWFpbjMoKTpcbiAgYXdhaXQgc29tZWNhbGwoMSwgNSkifQ==)

### Description

The `async` keyword in Python is used to define asynchronous functions that can be `await`ed.

In this example, we want to remove the `async` keyword from a function definition and replace it with a synchronous version of the function. We also need to remove the `await` keyword from the function body.

By default, ast-grep will not apply overlapping replacements. This means `await` keywords will not be modified because they are inside the async function body.

However, we can use the [`rewriter`](https://ast-grep.github.io/reference/yaml/rewriter.html) to apply changes inside the matched function body.

### YAML

```yaml
id: remove-async-def
language: python
rule:
  # match async function definition
  pattern:
    context: 'async def $FUNC($$$ARGS): $$$BODY'
    selector: function_definition
rewriters:
# define a rewriter to remove the await keyword
  remove-await-call:
    pattern: 'await $$$CALL'
    fix: $$$CALL # remove await keyword
# apply the rewriter to the function body
transform:
  REMOVED_BODY:
    rewrite:
      rewriters: [remove-await-call]
      source: $$$BODY
fix: |-
  def $FUNC($$$ARGS):
    $REMOVED_BODY
```

### Example

```python
async def main3():
  await somecall(1, 5)
```

### Diff

```python
async def main3(): # [!code --]
  await somecall(1, 5) # [!code --]
def main3(): # [!code ++]
  somecall(1, 5) # [!code ++]
```

### Contributed by

Inspired by the ast-grep issue [#1185](https://github.com/ast-grep/ast-grep/issues/1185)

## Refactor pytest fixtures

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiZGVmIGZvbygkWCk6XG4gICRTIiwicmV3cml0ZSI6ImxvZ2dlci5sb2coJE1BVENIKSIsImNvbmZpZyI6ImlkOiBweXRlc3QtdHlwZS1oaW50LWZpeHR1cmVcbmxhbmd1YWdlOiBQeXRob25cbnV0aWxzOlxuICBpcy1maXh0dXJlLWZ1bmN0aW9uOlxuICAgIGtpbmQ6IGZ1bmN0aW9uX2RlZmluaXRpb25cbiAgICBmb2xsb3dzOlxuICAgICAga2luZDogZGVjb3JhdG9yXG4gICAgICBoYXM6XG4gICAgICAgIGtpbmQ6IGlkZW50aWZpZXJcbiAgICAgICAgcmVnZXg6IF5maXh0dXJlJFxuICAgICAgICBzdG9wQnk6IGVuZFxuICBpcy10ZXN0LWZ1bmN0aW9uOlxuICAgIGtpbmQ6IGZ1bmN0aW9uX2RlZmluaXRpb25cbiAgICBoYXM6XG4gICAgICBmaWVsZDogbmFtZVxuICAgICAgcmVnZXg6IF50ZXN0X1xuICBpcy1weXRlc3QtY29udGV4dDpcbiAgICAjIFB5dGVzdCBjb250ZXh0IGlzIGEgbm9kZSBpbnNpZGUgYSBweXRlc3RcbiAgICAjIHRlc3QvZml4dHVyZVxuICAgIGluc2lkZTpcbiAgICAgIHN0b3BCeTogZW5kXG4gICAgICBhbnk6XG4gICAgICAgIC0gbWF0Y2hlczogaXMtZml4dHVyZS1mdW5jdGlvblxuICAgICAgICAtIG1hdGNoZXM6IGlzLXRlc3QtZnVuY3Rpb25cbiAgaXMtZml4dHVyZS1hcmc6XG4gICAgIyBGaXh0dXJlIGFyZ3VtZW50cyBhcmUgaWRlbnRpZmllcnMgaW5zaWRlIHRoZSBcbiAgICAjIHBhcmFtZXRlcnMgb2YgYSB0ZXN0L2ZpeHR1cmUgZnVuY3Rpb25cbiAgICBhbGw6XG4gICAgICAtIGtpbmQ6IGlkZW50aWZpZXJcbiAgICAgIC0gbWF0Y2hlczogaXMtcHl0ZXN0LWNvbnRleHRcbiAgICAgIC0gaW5zaWRlOlxuICAgICAgICAgIGtpbmQ6IHBhcmFtZXRlcnNcbnJ1bGU6XG4gIG1hdGNoZXM6IGlzLWZpeHR1cmUtYXJnXG4gIHJlZ2V4OiBeZm9vJFxuZml4OiAnZm9vOiBpbnQnXG4iLCJzb3VyY2UiOiJmcm9tIGNvbGxlY3Rpb25zLmFiYyBpbXBvcnQgSXRlcmFibGVcbmZyb20gdHlwaW5nIGltcG9ydCBBbnlcblxuaW1wb3J0IHB5dGVzdFxuZnJvbSBweXRlc3QgaW1wb3J0IGZpeHR1cmVcblxuQHB5dGVzdC5maXh0dXJlKHNjb3BlPVwic2Vzc2lvblwiKVxuZGVmIGZvbygpIC0+IEl0ZXJhYmxlW2ludF06XG4gICAgeWllbGQgNVxuXG5AZml4dHVyZVxuZGVmIGJhcihmb28pIC0+IHN0cjpcbiAgICByZXR1cm4gc3RyKGZvbylcblxuZGVmIHJlZ3VsYXJfZnVuY3Rpb24oZm9vKSAtPiBOb25lOlxuICAgICMgVGhpcyBmdW5jdGlvbiBkb2Vzbid0IHVzZSB0aGUgJ2ZvbycgZml4dHVyZVxuICAgIHByaW50KGZvbylcblxuZGVmIHRlc3RfMShmb28sIGJhcik6XG4gICAgcHJpbnQoZm9vLCBiYXIpXG5cbmRlZiB0ZXN0XzIoYmFyKTpcbiAgICAuLi4ifQ==)

### Description

One of the most commonly used testing framework in Python is [pytest](https://docs.pytest.org/en/8.2.x/). Among other things, it allows the use of [fixtures](https://docs.pytest.org/en/6.2.x/fixture.html).

Fixtures are defined as functions that can be required in test code, or in other fixtures, as an argument. This means that all functions arguments with a given name in a pytest context (test function or fixture) are essentially the same entity. However, not every editor's LSP is able to keep track of this, making refactoring challenging.

Using ast-grep, we can define some rules to match fixture definition and usage without catching similarly named entities in a non-test context.

First, we define utils to select pytest test/fixture functions.

```yaml
utils:
  is-fixture-function:
    kind: function_definition
    follows:
      kind: decorator
      has:
        kind: identifier
        regex: ^fixture$
        stopBy: end
  is-test-function:
    kind: function_definition
    has:
      field: name
      regex: ^test_
```

Pytest fixtures are declared with a decorator `@pytest.fixture`. We match the `function_definition` node that directly follows a `decorator` node. That decorator node must have a `fixture` identifier somewhere. This accounts for different location of the `fixture` node depending on the type of imports and whether the decorator is used as is or called with parameters.

Pytest functions are fairly straightforward to detect, as they always start with `test_` by convention.

The next utils builds onto those two to incrementally:

* Find if a node is inside a pytest context (test/fixture)
* Find if a node is an argument in such a context

```yaml
utils:
  is-pytest-context:
    # Pytest context is a node inside a pytest
    # test/fixture
    inside:
      stopBy: end
      any:
        - matches: is-fixture-function
        - matches: is-test-function
  is-fixture-arg:
    # Fixture arguments are identifiers inside the 
    # parameters of a test/fixture function
    all:
      - kind: identifier
      - inside:
          kind: parameters
      - matches: is-pytest-context
```

Once those utils are declared, you can perform various refactoring on a specific fixture.

The following rule adds a type-hint to a fixture.

```yaml
rule:
  matches: is-fixture-arg
  regex: ^foo$
fix: 'foo: int'
```

This one renames a fixture and all its references.

```yaml
rule:
  kind: identifier
  matches: is-fixture-context
  regex: ^foo$
fix: 'five'
```

### Example

#### Renaming Fixtures

```python {2,6,7,12,13}
@pytest.fixture
def foo() -> int:
    return 5

@pytest.fixture(scope="function")
def some_fixture(foo: int) -> str:
    return str(foo)

def regular_function(foo) -> None:
    ...

def test_code(foo: int) -> None:
    assert foo == 5
```

#### Diff

```python {2,6,7,12}
@pytest.fixture
def foo() -> int: # [!code --]
def five() -> int: # [!code ++]
    return 5

@pytest.fixture(scope="function")
def some_fixture(foo: int) -> str: # [!code --]
def some_fixture(five: int) -> str: # [!code ++]
    return str(foo)

def regular_function(foo) -> None:
    ...

def test_code(foo: int) -> None: # [!code --]
def test_code(five: int) -> None: # [!code ++]
    assert foo == 5 # [!code --]
    assert five == 5 # [!code ++]
```

#### Type Hinting Fixtures

```python {6,12}
@pytest.fixture
def foo() -> int:
    return 5

@pytest.fixture(scope="function")
def some_fixture(foo) -> str:
    return str(foo)

def regular_function(foo) -> None:
    ...

def test_code(foo) -> None:
    assert foo == 5
```

#### Diff

```python {2,6,7,12}
@pytest.fixture
def foo() -> int:
    return 5

@pytest.fixture(scope="function")
def some_fixture(foo) -> str: # [!code --]
def some_fixture(foo: int) -> str: # [!code ++]
    return str(foo)

def regular_function(foo) -> None:
    ...

def test_code(foo) -> None: # [!code --]
def test_code(foo: int) -> None: # [!code ++]
    assert foo == 5
```

## Rewrite `Optional[Type]` to `Type | None`&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiIiwicmV3cml0ZSI6IiIsInN0cmljdG5lc3MiOiJzaWduYXR1cmUiLCJzZWxlY3RvciI6IiIsImNvbmZpZyI6InJ1bGU6XG4gIHBhdHRlcm46IFxuICAgIGNvbnRleHQ6ICdhOiBPcHRpb25hbFskVF0nXG4gICAgc2VsZWN0b3I6IGdlbmVyaWNfdHlwZVxuZml4OiAkVCB8IE5vbmUiLCJzb3VyY2UiOiJkZWYgYShhcmc6IE9wdGlvbmFsW0ludF0pOiBwYXNzIn0=)

### Description

[PEP 604](https://peps.python.org/pep-0604/) recommends that `Type | None` is preferred over `Optional[Type]` for Python 3.10+.

This rule performs such rewriting. Note `Optional[$T]` alone is interpreted as subscripting expression instead of generic type, we need to use [pattern object](/guide/rule-config/atomic-rule.html#pattern-object) to disambiguate it with more context code.

### YAML

```yaml
id: optional-to-none-union
language: python
rule:
  pattern:
    context: 'a: Optional[$T]'
    selector: generic_type
fix: $T | None
```

### Example

```py {1}
def a(arg: Optional[int]): pass
```

### Diff

```py
def a(arg: Optional[int]): pass # [!code --]
def a(arg: int | None): pass # [!code ++]
```

### Contributed by

[Bede Carroll](https://github.com/ast-grep/ast-grep/discussions/1492)

## Recursive Rewrite Type&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiIiwicmV3cml0ZSI6IiIsInN0cmljdG5lc3MiOiJzbWFydCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoicmV3cml0ZXJzOlxyXG4tIGlkOiBvcHRpb25hbFxyXG4gIGxhbmd1YWdlOiBQeXRob25cclxuICBydWxlOlxyXG4gICAgYW55OlxyXG4gICAgLSBwYXR0ZXJuOlxyXG4gICAgICAgIGNvbnRleHQ6ICdhcmc6IE9wdGlvbmFsWyRUWVBFXSdcclxuICAgICAgICBzZWxlY3RvcjogZ2VuZXJpY190eXBlXHJcbiAgICAtIHBhdHRlcm46IE9wdGlvbmFsWyRUWVBFXVxyXG4gIHRyYW5zZm9ybTpcclxuICAgIE5UOlxyXG4gICAgICByZXdyaXRlOiBcclxuICAgICAgICByZXdyaXRlcnM6IFtvcHRpb25hbCwgdW5pb25zXVxyXG4gICAgICAgIHNvdXJjZTogJFRZUEVcclxuICBmaXg6ICROVCB8IE5vbmVcclxuLSBpZDogdW5pb25zXHJcbiAgbGFuZ3VhZ2U6IFB5dGhvblxyXG4gIHJ1bGU6XHJcbiAgICBwYXR0ZXJuOlxyXG4gICAgICBjb250ZXh0OiAnYTogVW5pb25bJCQkVFlQRVNdJ1xyXG4gICAgICBzZWxlY3RvcjogZ2VuZXJpY190eXBlXHJcbiAgdHJhbnNmb3JtOlxyXG4gICAgVU5JT05TOlxyXG4gICAgICByZXdyaXRlOlxyXG4gICAgICAgIHJld3JpdGVyczpcclxuICAgICAgICAgIC0gcmV3cml0ZS11bmlvbnNcclxuICAgICAgICBzb3VyY2U6ICQkJFRZUEVTXHJcbiAgICAgICAgam9pbkJ5OiBcIiB8IFwiXHJcbiAgZml4OiAkVU5JT05TXHJcbi0gaWQ6IHJld3JpdGUtdW5pb25zXHJcbiAgcnVsZTpcclxuICAgIHBhdHRlcm46ICRUWVBFXHJcbiAgICBraW5kOiB0eXBlXHJcbiAgdHJhbnNmb3JtOlxyXG4gICAgTlQ6XHJcbiAgICAgIHJld3JpdGU6IFxyXG4gICAgICAgIHJld3JpdGVyczogW29wdGlvbmFsLCB1bmlvbnNdXHJcbiAgICAgICAgc291cmNlOiAkVFlQRVxyXG4gIGZpeDogJE5UXHJcbnJ1bGU6XHJcbiAga2luZDogdHlwZVxyXG4gIHBhdHRlcm46ICRUUEVcclxudHJhbnNmb3JtOlxyXG4gIE5FV19UWVBFOlxyXG4gICAgcmV3cml0ZTogXHJcbiAgICAgIHJld3JpdGVyczogW29wdGlvbmFsLCB1bmlvbnNdXHJcbiAgICAgIHNvdXJjZTogJFRQRVxyXG5maXg6ICRORVdfVFlQRSIsInNvdXJjZSI6InJlc3VsdHM6ICBPcHRpb25hbFtVbmlvbltMaXN0W1VuaW9uW3N0ciwgZGljdF1dLCBzdHJdXVxuIn0=)

### Description

Suppose we want to transform Python's `Union[T1, T2]` to `T1 | T2` and `Optional[T]` to `T | None`.

By default, ast-grep will only fix the outermost node that matches a pattern and will not rewrite the inner AST nodes inside a match. This avoids unexpected rewriting or infinite rewriting loop.

So if you are using non-recursive rewriter like [this](https://github.com/ast-grep/ast-grep/discussions/1566#discussion-7401382), `Optional[Union[int, str]]` will only be converted to `Union[int, str] | None`. Note the inner `Union[int, str]` is not enabled. This is because the rewriter `optional` matches `Optional[$TYPE]` and rewrite it to `$TYPE | None`. The inner `$TYPE` is not processed.

However, we can apply `rewriters` to inner types recursively. Take the `optional` rewriter as an example, we need to apply rewriters, `optional` and `unions`, **recursively** to `$TYPE` and get a new variable `$NT`.

### YAML

```yml
id: recursive-rewrite-types
language: python
rewriters:
# rewrite Optional[T] to T | None
- id: optional
  rule:
    any:
    - pattern:
        context: 'arg: Optional[$TYPE]'
        selector: generic_type
    - pattern: Optional[$TYPE]
  # recursively apply rewriters to $TYPE
  transform:
    NT:
      rewrite:
        rewriters: [optional, unions]
        source: $TYPE
  # use the new variable $NT
  fix: $NT | None

# similar to Optional, rewrite Union[T1, T2] to T1 | T2
- id: unions
  language: Python
  rule:
    pattern:
      context: 'a: Union[$$$TYPES]'
      selector: generic_type
  transform:
    UNIONS:
      # rewrite all types inside $$$TYPES
      rewrite:
        rewriters: [ rewrite-unions ]
        source: $$$TYPES
        joinBy: " | "
  fix: $UNIONS
- id: rewrite-unions
  rule:
    pattern: $TYPE
    kind: type
  # recursive part
  transform:
    NT:
      rewrite:
        rewriters: [optional, unions]
        source: $TYPE
  fix: $NT

# find all types
rule:
  kind: type
  pattern: $TPE
# apply the recursive rewriters
transform:
  NEW_TYPE:
    rewrite:
      rewriters: [optional, unions]
      source: $TPE
# output
fix: $NEW_TYPE
```

### Example

```python
results:  Optional[Union[List[Union[str, dict]], str]]
```

### Diff

```python
results:  Optional[Union[List[Union[str, dict]], str]] # [!code --]
results:  List[str | dict] | str | None #[!code ++]
```

### Contributed by

Inspired by [steinuil](https://github.com/ast-grep/ast-grep/discussions/1566)

## Rewrite SQLAlchemy with Type Annotations&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiYShudWxsYWJsZT1UcnVlKSIsInJld3JpdGUiOiIxMjMiLCJzdHJpY3RuZXNzIjoic21hcnQiLCJzZWxlY3RvciI6ImtleXdvcmRfYXJndW1lbnQiLCJjb25maWciOiJpZDogcmVtb3ZlLW51bGxhYmxlLWFyZ1xubGFuZ3VhZ2U6IHB5dGhvblxucnVsZTpcbiAgcGF0dGVybjogJFggPSBtYXBwZWRfY29sdW1uKCQkJEFSR1MpXG4gIGFueTpcbiAgICAtIHBhdHRlcm46ICRYID0gbWFwcGVkX2NvbHVtbigkJCRCRUZPUkUsIFN0cmluZywgJCQkTUlELCBudWxsYWJsZT1UcnVlLCAkJCRBRlRFUilcbiAgICAtIHBhdHRlcm46ICRYID0gbWFwcGVkX2NvbHVtbigkJCRCRUZPUkUsIFN0cmluZywgJCQkTUlELCBudWxsYWJsZT1UcnVlKVxucmV3cml0ZXJzOlxuLSBpZDogZmlsdGVyLXN0cmluZy1udWxsYWJsZVxuICBydWxlOlxuICAgIHBhdHRlcm46ICRBUkdcbiAgICBpbnNpZGU6XG4gICAgICBraW5kOiBhcmd1bWVudF9saXN0XG4gICAgYWxsOlxuICAgIC0gbm90OiBcbiAgICAgICAgcGF0dGVybjogU3RyaW5nXG4gICAgLSBub3Q6XG4gICAgICAgIHBhdHRlcm46XG4gICAgICAgICAgY29udGV4dDogYShudWxsYWJsZT1UcnVlKVxuICAgICAgICAgIHNlbGVjdG9yOiBrZXl3b3JkX2FyZ3VtZW50XG4gIGZpeDogJEFSR1xuXG50cmFuc2Zvcm06XG4gIE5FV0FSR1M6XG4gICAgcmV3cml0ZTpcbiAgICAgIHJld3JpdGVyczogW2ZpbHRlci1zdHJpbmctbnVsbGFibGVdXG4gICAgICBzb3VyY2U6ICQkJEFSR1NcbiAgICAgIGpvaW5CeTogJywgJ1xuZml4OiB8LVxuICAkWDogTWFwcGVkW3N0ciB8IE5vbmVdID0gbWFwcGVkX2NvbHVtbigkTkVXQVJHUykiLCJzb3VyY2UiOiJtZXNzYWdlID0gbWFwcGVkX2NvbHVtbihTdHJpbmcsIGRlZmF1bHQ9XCJoZWxsb1wiLCBudWxsYWJsZT1UcnVlKVxuXG5tZXNzYWdlID0gbWFwcGVkX2NvbHVtbihTdHJpbmcsIG51bGxhYmxlPVRydWUpXG5cbl9tZXNzYWdlID0gbWFwcGVkX2NvbHVtbihcIm1lc3NhZ2VcIiwgU3RyaW5nLCBudWxsYWJsZT1UcnVlKVxuXG5tZXNzYWdlID0gbWFwcGVkX2NvbHVtbihTdHJpbmcsIG51bGxhYmxlPVRydWUsIHVuaXF1ZT1UcnVlKVxuXG5tZXNzYWdlID0gbWFwcGVkX2NvbHVtbihcbiAgU3RyaW5nLCBpbmRleD1UcnVlLCBudWxsYWJsZT1UcnVlLCB1bmlxdWU9VHJ1ZSlcblxuIyBTaG91bGQgbm90IGJlIHRyYW5zZm9ybWVkXG5tZXNzYWdlID0gbWFwcGVkX2NvbHVtbihTdHJpbmcsIGRlZmF1bHQ9XCJoZWxsb1wiKVxuXG5tZXNzYWdlID0gbWFwcGVkX2NvbHVtbihTdHJpbmcsIGRlZmF1bHQ9XCJoZWxsb1wiLCBudWxsYWJsZT1GYWxzZSlcblxubWVzc2FnZSA9IG1hcHBlZF9jb2x1bW4oSW50ZWdlciwgZGVmYXVsdD1cImhlbGxvXCIpIn0=)

### Description

[SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html) recommends using type annotations with `Mapped` type for modern declarative mapping. The `mapped_column()` construct can derive its configuration from [PEP 484](https://peps.python.org/pep-0484/) type annotations.

This rule helps migrate legacy SQLAlchemy code that explicitly uses `String` type and `nullable=True` to the modern type annotation approach using `Mapped[str | None]`.

The key technique demonstrated here is using **rewriters** to selectively filter arguments. The rewriter:

1. Matches each argument inside the `argument_list`
2. Excludes the `String` type argument
3. Excludes the `nullable=True` keyword argument
4. Keeps all other arguments

### YAML

```yaml
id: remove-nullable-arg
language: python
rule:
  pattern: $X = mapped_column($$$ARGS)
  any:
    - pattern: $X = mapped_column($$$BEFORE, String, $$$MID, nullable=True, $$$AFTER)
    - pattern: $X = mapped_column($$$BEFORE, String, $$$MID, nullable=True)
rewriters:
- id: filter-string-nullable
  rule:
    pattern: $ARG
    inside:
      kind: argument_list
    all:
    - not:
        pattern: String
    - not:
        pattern:
          context: a(nullable=True)
          selector: keyword_argument
  fix: $ARG

transform:
  NEWARGS:
    rewrite:
      rewriters: [filter-string-nullable]
      source: $$$ARGS
      joinBy: ', '
fix: |-
  $X: Mapped[str | None] = mapped_column($NEWARGS)
```

### Example

```python {1,3,5,7-8}
message = mapped_column(String, default="hello", nullable=True)

message = mapped_column(String, nullable=True)

_message = mapped_column("message", String, nullable=True)

message = mapped_column(String, nullable=True, unique=True)

message = mapped_column(
  String, index=True, nullable=True, unique=True)

# Should not be transformed
message = mapped_column(String, default="hello")

message = mapped_column(String, default="hello", nullable=False)

message = mapped_column(Integer, default="hello")
```

### Diff

```python
message = mapped_column(String, default="hello", nullable=True) # [!code --]
message: Mapped[str | None] = mapped_column(default="hello") # [!code ++]

message = mapped_column(String, nullable=True) # [!code --]
message: Mapped[str | None] = mapped_column() # [!code ++]

_message = mapped_column("message", String, nullable=True) # [!code --]
_message: Mapped[str | None] = mapped_column("message") # [!code ++]

message = mapped_column(String, nullable=True, unique=True) # [!code --]
message: Mapped[str | None] = mapped_column(unique=True) # [!code ++]

message = mapped_column( # [!code --]
  String, index=True, nullable=True, unique=True) # [!code --]
message: Mapped[str | None] = mapped_column( # [!code ++]
  index=True, unique=True) # [!code ++]
```

### Contributed by

Inspired by [discussion #2319](https://github.com/ast-grep/ast-grep/discussions/2319)
