# Source: https://zokrates.github.io/language/functions.html

Title: Functions - ZoKrates

URL Source: https://zokrates.github.io/language/functions.html

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

[Functions ---------](https://zokrates.github.io/language/functions.html#functions)
Functions are declared using the `def` keyword. A function's signature has to be explicitly provided. Its arguments are type annotated, just like variables, and, if the function returns a value, the return type must be specified after an arrow `->`.

A function has to be declared at the top level before it is called.

```
def foo(field a, field b) -> field {
    return a + b;
}

def main() -> field {
    return foo(1, 2);
}
```

A function can be generic over any number of values of type `u32`.

```
def foo<N>() -> field[N] {
    return [42; N];
}

def main() -> field[2] {
    field[2] res = foo();
    return res;
}
```

The generic parameters can be provided explicitly, especially when they cannot be inferred.

```
// a function to sum the N first powers of a field element
def sum_powers<N>(field a) -> field {
    field mut res = 0;
    for u32 i in 0..N {
        res = res + a ** i;
    }
    return res;
}

def main(field a) -> field {
    // call `sum_powers` providing the explicit generic parameter `N := 5`
    return sum_powers::<5>(a);
}
```

If the return type of a function is the empty tuple `()`, the return type as well as the return statement can be omitted.

```
def main() {}
```
[](https://zokrates.github.io/language/constants.html "Previous chapter")[](https://zokrates.github.io/language/generics.html "Next chapter")

[](https://zokrates.github.io/language/constants.html "Previous chapter")[](https://zokrates.github.io/language/generics.html "Next chapter")
