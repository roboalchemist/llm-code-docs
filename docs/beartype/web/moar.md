# Source: https://beartype.readthedocs.io/en/latest/moar/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# See Also[¶](#see-also)

External beartype resources include:

[This list of all open-source PyPI-hosted dependents of this package](https://github.com/beartype/beartype/network/dependents) (i.e., third-party packages requiring beartype
as a runtime dependency), kindly furnished by the Libraries.io package
registry.

Related type-checking resources include:

## Runtime Type Checkers[¶](#runtime-type-checkers)

**Runtime type checkers** (i.e., third-party Python packages dynamically
validating callables annotated by type hints at runtime, typically via
decorators, function calls, and import hooks) include:

package

active

PEP-compliant

time multiplier [[1]](#speed)

beartype

**yes**

**yes**

1 ✕ beartype

[enforce](https://github.com/RussBaz/enforce)

no

**yes**

*unknown*

[enforce_typing](https://github.com/matchawine/python-enforce-typing)

no

**yes**

*unknown*

[pydantic](https://docs.pydantic.dev)

**yes**

no

*unknown*

[pytypes](https://github.com/Stewori/pytypes)

no

**yes**

*unknown*

[typeen](https://github.com/k2bd/typen)

no

no

*unknown*

[typical](https://github.com/seandstewart/typical)

**yes**

**yes**

*unknown*

[typeguard](https://github.com/agronholm/typeguard)

no

**yes**

20 ✕ beartype

[[1](#id1)]
The *time multliplier* column approximates how much slower on average
than beartype **that checker is** as [timed by our profile suite](../math/#math-time). A time multiplier of:

“1” means that checker is approximately as fast as beartype, which means
that checker is probably beartype itself.
“20” means that checker is approximately twenty times slower than beartype
on average.

Like [static type checkers](#static-type-checkers), runtime type checkers
*always* require callables to be annotated by type hints. Unlike static type
checkers, runtime type checkers do *not* necessarily
comply with community standards; although some do require callers to annotate
callables with strictly PEP-compliant type hints, others permit or even require
callers to annotate callables with PEP-noncompliant type hints. Runtime type
checkers that do so violate:

[PEP 561 – Distributing and Packaging Type Information](https://peps.python.org/pep-0561), which
requires callables to be annotated with strictly PEP-compliant type hints.
Packages violating [PEP 561](https://peps.python.org/pep-0561) even once cannot be type-checked with static
type checkers (e.g., [mypy](http://mypy-lang.org)), unless each such
violation is explicitly ignored with a checker-specific filter (e.g., with a
[mypy](http://mypy-lang.org)-specific inline type comment).
[PEP 563 – Postponed Evaluation of Annotations](https://peps.python.org/pep-0563), which
explicitly deprecates PEP-noncompliant type hints:

With this in mind, uses for annotations incompatible with the
aforementioned PEPs *[i.e., PEPs 484, 544, 557, and 560]* should be
considered deprecated.

## Runtime Data Validators[¶](#runtime-data-validators)

**Runtime data validators** (i.e., third-party Python packages dynamically
validating callables decorated by caller-defined contracts, constraints, and
validation routines at runtime) include:

- [PyContracts](https://github.com/AlexandruBurlacu/pycontracts).

- [contracts](https://pypi.org/project/contracts).

- [covenant](https://github.com/kisielk/covenant).

- [dpcontracts](https://pypi.org/project/dpcontracts).

- [icontract](https://github.com/Parquery/icontract).

- [pcd](https://pypi.org/project/pcd).

- [pyadbc](https://pypi.org/project/pyadbc).

Unlike both [runtime type checkers](#runtime-type-checkers) and static type
checkers, most runtime data validators do *not*
require callables to be annotated by type hints. Like some runtime type
checkers, most runtime data validators do *not*
comply with community standards but instead require callers to either:

- Decorate callables with package-specific decorators.

Annotate callables with package-specific and thus PEP-noncompliant type
hints.

## Static Type Checkers[¶](#static-type-checkers)

**Static type checkers** (i.e., third-party tooling validating Python callable
and/or variable types across an application stack at static analysis time
rather than Python runtime) include:

- [mypy](http://mypy-lang.org), Python’s official static type checker.

- [Pyre](https://pyre-check.org), published by Meta. …yah.

- [pyright](https://github.com/Microsoft/pyright), published by Microsoft.

- [pytype](https://github.com/google/pytype), published by Google.

 
 
 
 
 
 
 **
 
 previous

 Maths: It’s Plural, Apparently