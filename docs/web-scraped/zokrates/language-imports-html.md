# Source: https://zokrates.github.io/language/imports.html

Title: Imports - ZoKrates

URL Source: https://zokrates.github.io/language/imports.html

Markdown Content:
1.   [**1.** Introduction](https://zokrates.github.io/introduction.html)
2.   [**2.** Getting Started](https://zokrates.github.io/gettingstarted.html)
3.   [**3.** Language](https://zokrates.github.io/language/index.html)
4.       1.   [**3.1.** Variables](https://zokrates.github.io/language/variables.html)
    2.   [**3.2.** Types](https://zokrates.github.io/language/types.html)
    3.   [**3.3.** Operators](https://zokrates.github.io/language/operators.html)
    4.   [**3.4.** Control flow](https://zokrates.github.io/language/control_flow.html)
    5.   [**3.5.** Constants](https://zokrates.github.io/language/constants.html)
    6.   [**3.6.** Functions](https://zokrates.github.io/language/functions.html)
    7.   [**3.7.** Generics](https://zokrates.github.io/language/generics.html)
    8.   [**3.8.** Imports](https://zokrates.github.io/language/imports.html)
    9.   [**3.9.** Comments](https://zokrates.github.io/language/comments.html)
    10.   [**3.10.** Macros](https://zokrates.github.io/language/macros.html)
    11.   [**3.11.** Logging](https://zokrates.github.io/language/logging.html)
    12.   [**3.12.** Assembly](https://zokrates.github.io/language/assembly.html)

5.   [**4.** Toolbox](https://zokrates.github.io/toolbox/index.html)
6.       1.   [**4.1.** CLI](https://zokrates.github.io/toolbox/cli.html)
    2.   [**4.2.** Trusted Setup](https://zokrates.github.io/toolbox/trusted_setup.html)
    3.   [**4.3.** Standard Library](https://zokrates.github.io/toolbox/stdlib.html)
    4.   [**4.4.** Proving schemes](https://zokrates.github.io/toolbox/proving_schemes.html)
    5.   [**4.5.** Verification](https://zokrates.github.io/toolbox/verification.html)
    6.   [**4.6.** ZIR](https://zokrates.github.io/toolbox/ir.html)
    7.   [**4.7.** JSON ABI](https://zokrates.github.io/toolbox/abi.html)
    8.   [**4.8.** zokrates.js](https://zokrates.github.io/toolbox/zokrates_js.html)
    9.   [**4.9.** Experimental](https://zokrates.github.io/toolbox/experimental.html)

7.   [**5.** Examples](https://zokrates.github.io/examples/index.html)
8.       1.   [**5.1.** A SNARK Powered RNG](https://zokrates.github.io/examples/rng_tutorial.html)
    2.   [**5.2.** Proving knowledge of a hash preimage](https://zokrates.github.io/examples/sha256example.html)
    3.   [**5.3.** A ZK Magic Square in the browser](https://zokrates.github.io/examples/magic_square.html)

9.   [**6.** Testing](https://zokrates.github.io/testing.html)

ZoKrates
--------

[](https://zokrates.github.io/print.html "Print this book")

[Imports -------](https://zokrates.github.io/language/imports.html#imports)
You can separate your code into multiple ZoKrates files using `import` statements to import symbols, ignoring the `.zok` extension of the imported file.

[### Import syntax](https://zokrates.github.io/language/imports.html#import-syntax)[#### Symbol selection](https://zokrates.github.io/language/imports.html#symbol-selection)
The preferred way to import a symbol is by module and name:

```
from "./path/to/my/module" import MySymbol;

// `MySymbol` is now in scope.
```

To import multiple symbols with a single import statement, separate the symbols names with commas:

```
from "./path/to/my/module" import MySymbol, MyOtherSymbol;
```
[#### Aliasing](https://zokrates.github.io/language/imports.html#aliasing)
The `as` keyword enables renaming symbols:

```
from "./path/to/my/module" import MySymbol as MyAlias;

// `MySymbol` is now in scope under the alias MyAlias.
```
[#### Legacy](https://zokrates.github.io/language/imports.html#legacy)
The legacy way to import a symbol is by only specifying a module:

```
import "./path/to/my/module";
```

In this case, the name of the symbol is assumed to be `main` and the alias is assumed to be the module's filename so that the above is equivalent to

```
from "./path/to/my/module" import main as module;

// `main` is now in scope under the alias `module`.
```

Note that this legacy method is likely to become deprecated, so it is recommended to use the preferred way instead.

[### Symbols](https://zokrates.github.io/language/imports.html#symbols)
Three types of symbols can be imported

[#### Functions](https://zokrates.github.io/language/imports.html#functions)
Functions are imported by name. If many functions have the same name but different signatures, all of them get imported, and which one to use in a particular call is inferred.

[#### User-defined types](https://zokrates.github.io/language/imports.html#user-defined-types)
User-defined types declared with the `struct` keyword are imported by name.

[#### Constants](https://zokrates.github.io/language/imports.html#constants)
Constants declared with the `const` keyword are imported by name.

[### Relative Imports](https://zokrates.github.io/language/imports.html#relative-imports)
You can import a resource in the same folder directly, like this:

```
from "./mycode" import foo;
```

Imports up the file-system tree are supported:

```
from "../../../mycode" import foo;
```
[### Absolute Imports](https://zokrates.github.io/language/imports.html#absolute-imports)
Absolute imports don't start with `./` or `../` in the path and are used to import components from the ZoKrates standard library. Please check the according [section](https://zokrates.github.io/toolbox/stdlib.html) for more details.

[](https://zokrates.github.io/language/generics.html "Previous chapter")[](https://zokrates.github.io/language/comments.html "Next chapter")

[](https://zokrates.github.io/language/generics.html "Previous chapter")[](https://zokrates.github.io/language/comments.html "Next chapter")
