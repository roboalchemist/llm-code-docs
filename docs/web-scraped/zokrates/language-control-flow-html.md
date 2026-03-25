# Source: https://zokrates.github.io/language/control_flow.html

Title: Control flow - ZoKrates

URL Source: https://zokrates.github.io/language/control_flow.html

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

[Control Flow ------------](https://zokrates.github.io/language/control_flow.html#control-flow)
ZoKrates provides a single thread of execution with a few flow constructs.

[### Function calls](https://zokrates.github.io/language/control_flow.html#function-calls)
Function calls help make programs clear and modular.

Arguments are passed by value.

Function parameters can be declared as mutable to allow for mutation within the function's body. However, mutable function arguments are still passed by value, so the original value can never be mutated.

```
def incr(field mut a) -> field {
    a = a + 1;
    return a;
}

def main() {
    field x = 1;
    field res = incr(x);
    assert(x == 1); // x has not changed
    return;
}
```

Generic parameters, if any, must be compile-time constants. They are inferred by the compiler if that is possible, but can also be provided explicitly.

```
def foo<N, P>() -> field[P] {
    return [42; P];
}

def main() -> field[2] {
    // `P` is inferred from the declaration of `res`, while `N` is provided explicitly
    field[2] res = foo::<3, _>();
    return res;
}
```
[### Conditional expressions](https://zokrates.github.io/language/control_flow.html#conditional-expressions)
A conditional expression allows you to branch your code depending on a boolean condition.

```
def main(field x) -> field {
    field y = if x + 2 == 3 { 1 } else { 5 };
    return y;
}
```

The conditional expression can also be written using a ternary operator:

```
def main(field x) -> field {
    field y = x + 2 == 3 ? 1 : 5;
    return y;
}
```

There are two important caveats when it comes to conditional expressions. Before we go into them, let's define two concepts:

*   for an execution of the program, _an executed branch_ is a branch which has to be paid for when executing the program, generating proofs, etc.
*   for an execution of the program, _a logically executed branch_ is a branch which is "chosen" by the condition of an if-expression. This is the more intuitive notion of execution, and there is only one for each if-expression.

Now the two caveats:

*   **Both branches are always executed**. No short-circuiting happens based on the value of the condition. Therefore, the complexity of a program in terms of the number of constraints it compiles down to is the _sum_ of the cost of all branches.

```
def cheap(field x) -> field {
    return x + 1;
}

def expensive(field x) -> field {
    return x**1000;
}

def main(field x) -> field {
    return if x == 1 {
        cheap(x)
    } else {
        expensive(x) // both branches executed
    };
}
```

*   **An unsatisfied constraint inside any branch will make the whole execution fail, even if this branch is not logically executed**. Also, the compiler itself inserts assertions which can fail. This can lead to unexpected results:

```
def main(field x) -> field {
    return if x == 0 {
        0
    } else {
        1 / x // executed even for x := 0, which leads to the execution failing
    };
}
```

> The reason for these caveats is that the program is compiled down to an arithmetic circuit. This construct does not support jumping to a branch depending on a condition as you could do on traditional architectures. Instead, all branches are inlined as if they were printed on a circuit board.

[### For loops](https://zokrates.github.io/language/control_flow.html#for-loops)
For loops are available with the following syntax:

```
def main() -> u32 {
    u32 mut res = 0;
    for u32 i in 0..4 {
        for u32 j in i..5 {
            res = res + i;
        }
    }
    return res;
}
```

The bounds have to be constant at compile-time, therefore they cannot depend on execution inputs. They can depend on generic parameters. The range is half-open, meaning it is bounded inclusively below and exclusively above. The range `start..end` contains all values within `start <= x < end`. The range is empty if `start >= end`.

> For loops are only syntactic sugar for repeating a block of statements many times. No condition of the type `index < max` is being checked at run-time after each iteration. Instead, at compile-time, the index is incremented and the block is executed again. Therefore, assigning to the loop index does not have any influence on the number of iterations performed and is considered bad practice.

[### Assertions](https://zokrates.github.io/language/control_flow.html#assertions)
Any boolean can be asserted to be true using the `assert` function.

```
def main() {
    assert(1f + 1f == 2f);
    return;
}
```

If any assertion fails, execution stops as no valid proof could be generated from it.

[](https://zokrates.github.io/language/operators.html "Previous chapter")[](https://zokrates.github.io/language/constants.html "Next chapter")

[](https://zokrates.github.io/language/operators.html "Previous chapter")[](https://zokrates.github.io/language/constants.html "Next chapter")
