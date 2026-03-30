# Source: https://zokrates.github.io/language/variables.html

Title: Variables - ZoKrates

URL Source: https://zokrates.github.io/language/variables.html

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

[Variables ---------](https://zokrates.github.io/language/variables.html#variables)
Variables can have any name which does not start with a number. Variables are mutable, and always passed by value to functions.

[### Declaration](https://zokrates.github.io/language/variables.html#declaration)
Variables need to be declared to be used. Declaration and definition are always combined, so that undefined variables do not exist.

```
def main() {
    // declare and define `my_variable`
    field mut my_variable = 2;
    // redefine `my_variable`
    my_variable = 3;
    return;
}
```
[### Mutability](https://zokrates.github.io/language/variables.html#mutability)
Variables are immutable by default. In order to declare a mutable variable, the `mut` keyword is used.

```
def main() {
    field a = 42;
    // a = 43; <- not allowed, as `a` is immutable
    field mut b = 42;
    b = 43; // ok
    return;
}
```
[### Shadowing](https://zokrates.github.io/language/variables.html#shadowing)
Shadowing is allowed.

```
def main() -> field {
    field a = 2;
    field a = 3; // shadowing
    for u32 i in 0..5 {
        bool a = true; // shadowing
    }
    // `a` is the variable declared before the loop
    return a;
}
```
[### Scope](https://zokrates.github.io/language/variables.html#scope)[#### Function](https://zokrates.github.io/language/variables.html#function)
Functions have their own scope

```
def foo() -> field {
    // return myGlobal; <- not allowed
    return 42;
}

def main() -> field {
    field myGlobal = 42;
    return foo();
}
```
[#### For-loop](https://zokrates.github.io/language/variables.html#for-loop)
For-loops have their own scope

```
def main() -> u32 {
    u32 mut a = 0;
    for u32 i in 0..5 {
        a = a + i;
    }
    // return i; <- not allowed
    return a;
}
```
[](https://zokrates.github.io/language/index.html "Previous chapter")[](https://zokrates.github.io/language/types.html "Next chapter")

[](https://zokrates.github.io/language/index.html "Previous chapter")[](https://zokrates.github.io/language/types.html "Next chapter")
