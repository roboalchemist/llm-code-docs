# Source: https://zokrates.github.io/language/assembly.html

Title: Assembly - ZoKrates

URL Source: https://zokrates.github.io/language/assembly.html

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

[Assembly --------](https://zokrates.github.io/language/assembly.html#assembly)
ZoKrates allows developers to define constraints through assembly blocks. Assembly blocks are considered **unsafe**, as safety and correctness of the resulting arithmetic circuit is in the hands of the developer. Usage of assembly is recommended only in optimization efforts for experienced developers to minimize constraint count of an arithmetic circuit.

> The usage of assembly blocks in ZoKrates is experimental. In particular, while assembly blocks help minimise constraint count in some cases, they currently can at the same time lead to larger compiler output and slower witness generation.

[Writing assembly ----------------](https://zokrates.github.io/language/assembly.html#writing-assembly)
All constraints must be enclosed within an `asm` block. In an assembly block we can do the following:

1.   Assign to a witness variable using `<--`
2.   Define a constraint using `===`

Assigning a value, in general, should be combined with adding a constraint:

```
def main(field a, field b) -> field {
    field mut c = 0;
    field mut invb = 0;
    asm {
        invb <-- b == 0 ? 0 : 1 / b;
        invb * b === 1;
        c <-- invb * a;
        a === b * c;
    }
    return c;
}
```

> Note that operator `<--` is used for unconstrained assignment and can be easily misused. This operator does not generate constraints, which could result in unconstrained variables in the constraint system.

Unconstrained assignment `<--` allows assignment to variables with complex types. The type must consist of field elements only (eg. `field[3]`):

```
field[3] mut c = [0; 3];
asm {
    c <-- [2, 2, 4];
    c[0] * c[1] === c[2];
}
```

In some cases we can combine the witness assignment and constraint generation with the `<==` operator (constrained assignment):

```
asm {
    c <== 1 - a*b;
}
```

which is equivalent to:

```
asm {
    c <-- 1 - a*b;
    c === 1 - a*b;
}
```

In the case of constrained assignment `<==`, both sides of the statement have to be of type `field`.

A constraint can contain arithmetic expressions that are built using multiplication, addition, and other variables or `field` values. Only quadratic expressions are allowed to be included in constraints. Non-quadratic expressions or usage of other arithmetic operators like division or power are not allowed as constraints, but can be used in the witness assignment expression.

The following code is not allowed:

```
asm {
    d === a*b*c;
}
```

as the constraint `d === a*b*c` is not quadratic.

In some cases, ZoKrates will apply minor transformations on the defined constraints in order to meet the correct format:

```
asm {
    x * (x - 1) === 0;
}
```

will be transformed to:

```
asm {
    x === x * x;
}
```
[Type casting ------------](https://zokrates.github.io/language/assembly.html#type-casting)
Assembly is a low-level part of the compiler which does not have type safety. In some cases we might want to do zero-cost conversions between `field` and `bool` type.

[### field_to_bool_unsafe](https://zokrates.github.io/language/assembly.html#field_to_bool_unsafe)
This call is unsafe because it is the responsibility of the user to constrain the field input:

```
from "EMBED" import field_to_bool_unsafe;

def main(field x) -> bool {
    // we constrain `x` to be 0 or 1
    asm {
        x * (x - 1) === 0;
    }
    // we can convert `x` to `bool` afterwards, as we constrained it properly
    // if we failed to constrain `x` to `0` or `1`, the call to `field_to_bool_unsafe` introduces undefined behavior
    // `field_to_bool_unsafe` call does not produce any extra constraints
    bool out = field_to_bool_unsafe(x);
    return out;
}
```
[](https://zokrates.github.io/language/logging.html "Previous chapter")[](https://zokrates.github.io/toolbox/index.html "Next chapter")

[](https://zokrates.github.io/language/logging.html "Previous chapter")[](https://zokrates.github.io/toolbox/index.html "Next chapter")
