# Zenoh Key Expressions: Complete Guide

Key Expressions (KEs) are the addressing language of Zenoh. Every publish, subscribe, query, and storage operation is addressed by a key expression. This guide covers the full syntax, matching semantics, APIs, and common pitfalls.

---

## Table of Contents

- [1. Keys vs Key Expressions](#1-keys-vs-key-expressions)
  - [Set Semantics](#set-semantics)
- [2. Syntax Specification](#2-syntax-specification)
  - [EBNF Grammar](#ebnf-grammar)
  - [Forbidden Characters in Chunks](#forbidden-characters-in-chunks)
  - [Structural Rules](#structural-rules)
  - [UTF-8 and Unicode](#utf-8-and-unicode)
- [3. Wildcards](#3-wildcards)
  - [`*` — Single-Chunk Wild](#single-chunk-wild)
  - [`**` — Multi-Chunk Wild](#multi-chunk-wild)
  - [`$*` — Sub-Chunk Wild (DSL)](#sub-chunk-wild-dsl)
- [4. DSL Extensions and Verbatim Chunks](#4-dsl-extensions-and-verbatim-chunks)
  - [Verbatim Chunks](#verbatim-chunks)
- [5. Canon Forms](#5-canon-forms)
  - [Canonicalization Rules](#canonicalization-rules)
  - [What Requires Manual Canonicalization](#what-requires-manual-canonicalization)
  - [Invalid KE Examples (Rejected at Validation)](#invalid-ke-examples-rejected-at-validation)
- [6. Selector Syntax](#6-selector-syntax)
  - [Parameter Encoding](#parameter-encoding)
  - [Parsing a Selector](#parsing-a-selector)
  - [Standardized Parameters](#standardized-parameters)
  - [Custom Parameters](#custom-parameters)
  - [Selectors in Subscriptions](#selectors-in-subscriptions)
- [7. intersect() vs includes()](#7-intersect-vs-includes)
  - [Definitions](#definitions)
  - [When the Router Uses Each](#when-the-router-uses-each)
  - [Code Examples](#code-examples)
  - [Verified Behavioral Examples](#verified-behavioral-examples)
- [8. OwnedKeyExpr vs KeyExpr<'_>](#8-ownedkeyexpr-vs-keyexpr_)
  - [`keyexpr` (lowercase) — Borrowed, Zero-Copy](#keyexpr-lowercase-borrowed-zero-copy)
  - [`OwnedKeyExpr` — Heap-Allocated, `Arc<str>` Backed](#ownedkeyexpr-heap-allocated-arcstr-backed)
  - [`KeyExpr<'a>` — The High-Level API Type](#keyexpra-the-high-level-api-type)
  - [Conversion Summary](#conversion-summary)
  - [Path Concatenation with `/`](#path-concatenation-with)
- [9. Declared vs Inline Key Expressions](#9-declared-vs-inline-key-expressions)
  - [The Difference](#the-difference)
  - [When Declaration Matters](#when-declaration-matters)
  - [Rust API](#rust-api)
  - [Python API](#python-api)
  - [Quantifying the Savings](#quantifying-the-savings)
- [10. Key Formatters](#10-key-formatters)
  - [Format String Syntax](#format-string-syntax)
  - [Examples](#examples)
  - [Compile-Time Formats with `kedefine!`](#compile-time-formats-with-kedefine)
  - [Runtime Formats with `KeFormat::new`](#runtime-formats-with-keformatnew)
  - [Parsing and Field Extraction](#parsing-and-field-extraction)
  - [Greedy Parsing and Ambiguity](#greedy-parsing-and-ambiguity)
  - [Use Cases](#use-cases)
- [11. Router Behavior: When Matching Matters](#11-router-behavior-when-matching-matters)
  - [Publication Routing](#publication-routing)
  - [Queryable and Storage Selection](#queryable-and-storage-selection)
  - [Subscription to Wild Publishers](#subscription-to-wild-publishers)
  - [Admin Space Isolation](#admin-space-isolation)
- [12. Quick Reference Tables](#12-quick-reference-tables)
  - [Wildcard Summary](#wildcard-summary)
  - [Set Relations](#set-relations)
  - [Canon Form Rules](#canon-form-rules)
  - [Selector Parameters](#selector-parameters)
  - [Type Quick Reference (Rust)](#type-quick-reference-rust)
- [13. Common Mistakes](#13-common-mistakes)
  - [Using `*` When `**` Is Needed](#using-when-is-needed)
  - [Using `**` When `*` Is Needed](#using-when-is-needed)
  - [Forgetting Canonicalization Before Validation](#forgetting-canonicalization-before-validation)
  - [Using Selector Syntax in a Subscriber](#using-selector-syntax-in-a-subscriber)
  - [Invalid Characters Causing Panics at Runtime](#invalid-characters-causing-panics-at-runtime)
  - [Ambiguous Multi-`**` Formats](#ambiguous-multi-formats)
  - [Confusing Performance of `*` vs `$*`](#confusing-performance-of-vs)
  - [Assuming `**` Matches Verbatim Chunks](#assuming-matches-verbatim-chunks)
  - [Publishing DELETE on `**`](#publishing-delete-on)


---


## 1. Keys vs Key Expressions

A **key** is a concrete name for a piece of data — a `/`-separated list of UTF-8 string chunks with no wildcards. A **key expression** is a superset of keys that can describe sets of keys using wildcards.

```
key:            demo/robot/arm/joint1
key expression: demo/robot/*/joint*   ← describes many keys at once
```

Keys follow these rules:
- Each chunk is a non-empty UTF-8 string
- Chunks cannot contain: `* $ ? #`
- No leading `/`, no trailing `/`, no `//`

KEs follow the same rules for non-wild portions, plus additional syntax for wildcards and DSL chunks.

### Set Semantics

Every KE is equivalent to the set of keys it matches. This gives four possible relationships between two KEs **A** and **B**:

| Relationship | Meaning |
|---|---|
| **Disjoint** | No key belongs to both A and B |
| **Intersect** | At least one key belongs to both |
| **A includes B** | Every key in B is also in A |
| **Equal** | A includes B and B includes A (implies string equality) |

The **unicity property** — enforced through canon forms — guarantees that equal sets always produce equal strings. You can compare KEs for set equality using `==`.

---

## 2. Syntax Specification

### EBNF Grammar

```ebnf
key-expression   ::= chunk ('/' chunk)*
chunk            ::= verbatim-chunk | wild-chunk | plain-chunk
verbatim-chunk   ::= '@' chunk-chars*
wild-chunk       ::= '*' | '**' | dsl-chunk
dsl-chunk        ::= ('$*' | chunk-chars)* ('$*' ('$*' | chunk-chars)*)*
plain-chunk      ::= chunk-chars+
chunk-chars      ::= any UTF-8 character except '/' '*' '$' '?' '#'
```

### Forbidden Characters in Chunks

The characters `* $ ? #` are reserved for KE syntax. They may appear only in their designated roles (`*` as wildcard, `$*` as DSL sub-chunk wild). Any other use is invalid.

### Structural Rules

| Rule | Valid | Invalid |
|---|---|---|
| No leading slash | `a/b` | `/a/b` |
| No trailing slash | `a/b` | `a/b/` |
| No double slash | `a/b` | `a//b` |
| No empty chunks | `a/b` | `a//b` |
| Wildcards are whole-chunk only | `*/b` | `a*/b` (use `a$*/b` instead) |

### UTF-8 and Unicode

Zenoh accepts any valid UTF-8. However, characters with multiple Unicode representations (accented letters, composed vs decomposed forms) are compared byte-for-byte. Zenoh does **not** normalize Unicode. Stick to ASCII-safe characters or normalize your strings before constructing KEs to avoid mismatches.

---

## 3. Wildcards

All three wildcard forms are whole-chunk constructs — they must be surrounded by `/` separators (or be at the start/end of the KE). You cannot embed them inside a chunk without using the `$*` DSL.

### `*` — Single-Chunk Wild

Matches **exactly one chunk** of any value. Equivalent to the regex `[^/]+`. It cannot match zero chunks or a chunk containing `/`.

```
a/*/b   matches:   a/c/b   a/hi/b   a/xyz/b
        no-match:  a/b           ← zero chunks between a and b
                   a/c/d/b       ← two chunks between a and b
                   b/c           ← wrong prefix
```

More examples:
```
demo/*/data     matches:  demo/robot/data   demo/sensor/data
                no-match: demo/data         demo/robot/arm/data
```

### `**` — Multi-Chunk Wild

Matches **zero or more chunks** (including the separators between them). It is the most permissive wildcard.

```
a/**/b  matches:   a/b              ← zero chunks
                   a/c/b            ← one chunk
                   a/c/d/b          ← two chunks
                   a/x/y/z/b        ← many chunks
        no-match:  a/b/c            ← nothing after b
```

`**` alone matches **every possible key**:
```
**      matches:   a   a/b   a/b/c   demo/robot/arm/joint1
```

Practical implication: publishing a DELETE on `**` is equivalent to `rm -rf /` — it deletes everything in the namespace.

```
robot/**    matches:  robot         ← zero chunks after robot
                      robot/arm
                      robot/arm/joint1
                      robot/arm/joint1/angle

**/status   matches:  status
                      device/status
                      a/b/c/status
```

Mixed wildcards:
```
a/**/c/**/e  matches:  a/c/e          ← both ** are zero-width
                       a/b/c/d/e
                       a/b/b/c/d/d/e
```

### `$*` — Sub-Chunk Wild (DSL)

Matches **zero or more characters within a single chunk**, but never crosses a `/` boundary. Equivalent to `[^/]*` per segment. Unlike `*`, it can appear in the middle or at the end of a chunk.

```
a/c$*/b     matches:  a/cool/b   a/c/b   a/cx/b
            no-match: a/uncool/b         ← doesn't start with 'c'

ab$*        matches:  ab   abc   abxyz
            no-match: x/ab               ← wrong prefix chunk

robot-$*    matches:  robot-arm  robot-base  robot-
```

**Performance warning**: `$*` is significantly slower than `*`. The KE language was deliberately designed to make `$*` syntactically inconvenient (vs the old `*` glob behavior) to discourage its use. Prefer a key space design that doesn't require sub-chunk wildcards. For example:

```
AVOID:  factory-12/room-10/robot-$*    ← requires $* matching
PREFER: factory/12/room/10/robot/*     ← uses fast * matching
```

---

## 4. DSL Extensions and Verbatim Chunks

### Verbatim Chunks

A verbatim chunk starts with `@`. It can only be matched by an **identical** verbatim chunk. No wildcard (`*`, `**`, `$*`) can match across or through a verbatim chunk boundary.

```
my-api/@v1/**   intersects: my-api/@v1/endpoint
                             my-api/@v1/data/x

my-api/@v1/**   does NOT intersect: my-api/@v2/**
                                     my-api/*/**
                                     my-api/@$*/**
                                     my-api/**
```

Key behavior: `**` cannot skip over a verbatim chunk. `my-api/**` does NOT match `my-api/@v1/endpoint` — because `@v1` is verbatim and `**` stops at it.

#### Hermetic Namespaces

A regular namespace like `robots/` is not hermetic — `*/arm` can match both `robots/arm` and `sensors/arm`. A verbatim-based hermetic namespace is sealed:

```
@robots/**      ← hermetic namespace
@sensors/**     ← completely separate hermetic namespace

*/**            ← does NOT match inside @robots or @sensors
```

There is no KE that matches both inside and outside a hermetic namespace. This is useful for:
- API versioning: `@v1/**` and `@v2/**`
- Isolated tenants or devices
- Admin vs data separation

#### Separating Variable-Length Sections

When a KE has two `**`-style segments, use a verbatim chunk to disambiguate:

```
# Ambiguous: which ** ate what?
src/${src_path:**}/dst/${dst_path:**}
parsing src/./dst/dst/. → ambiguous

# Unambiguous: @ acts as a hard separator
src/${src_path:**}/@/dst/${dst_path:**}
parsing src/a/b/@/dst/c → src_path=a/b, dst_path=c
```

#### Admin Space

By convention, Zenoh uses `@` chunks for its own [admin space](admin-space-guide.md) data. From version 0.11.0 onward the admin space is a proper hermetic namespace, so user KEs starting with `@` are cleanly separated from Zenoh internals.

---

## 5. Canon Forms

The KE language guarantees **unicity**: for any set of keys, at most one string is a valid KE for that set. This is enforced through canonicalization.

Non-canonical KEs are **rejected** by Zenoh routers. A router receiving a non-canonical KE will drop the associated message and close the connection to the sender.

### Canonicalization Rules

Canonicalization is a fixed-point transformation. The following replacements are applied until none can be applied:

| Input | Canonical form | Example |
|---|---|---|
| Contiguous `$*$*...` in a chunk | Single `$*` | `a/foo$*$*/b` → `a/foo$*/b` |
| `$*` alone in a chunk | `*` | `a/$*/b` → `a/*/b` |
| Multiple consecutive `**` chunks | Single `**` | `a/**/**/b` → `a/**/b` |
| `**/*` sequence | `*/**` | `a/**/*` → `a/*/**` |

```
hello/foo$*$*/bar  →  hello/foo$*/bar
hello/**/**/bye    →  hello/**/bye
hello/$*/bye       →  hello/*/bye
hello/**/*         →  hello/*/**
$*$*$*/hello/$*$*/bye/$*$*  →  */hello/*/bye/*
```

### What Requires Manual Canonicalization

The safe constructors in Rust (`keyexpr::new`, `OwnedKeyExpr::try_from`) **require** the input to already be canonical. They return an error if it isn't.

To canonize a string before constructing:
```rust
// Rust: autocanonize mutates the string in place, then validates
let ke = keyexpr::autocanonize(&mut my_string)?;

// Or use OwnedKeyExpr::autocanonize for an owned version
let ke = OwnedKeyExpr::autocanonize(my_string.to_string())?;
```

```python
# Python: the API accepts raw strings and handles canonization
session.declare_subscriber("demo/example/**")  # validated at binding level
```

### Invalid KE Examples (Rejected at Validation)

```
/a/b        ← leading slash
a/b/        ← trailing slash
a//b        ← double slash (empty chunk)
a/b/*$*     ← mixing * and $* in same chunk
a/b/$**     ← $* followed by * in same chunk
```

---

## 6. Selector Syntax

A **selector** combines a key expression with an optional parameter string for use in `get()` queries. It follows URL conventions:

```
<key-expression>?<parameters>
```

The `?` introduces the parameter section. If there is no `?`, the entire string is interpreted as a KE with no parameters.

### Parameter Encoding

Parameters follow URL query string conventions with one difference: the separator is `;` not `&`:

```
demo/sensor/**?_time=[now(-1h)..now()];format=json
│            │  ──────────────────────────────────
│            │  parameters (separated by ;)
└────────────┘
key expression
```

Rules:
- Parameters are separated by `;`
- Name and value are separated by the first `=`
- If no `=` is present, the value is the empty string
- Both name and value should use percent-encoding for special characters
- Duplicate parameter names result in undefined behavior (implementations should reject duplicates)

### Parsing a Selector

```rust
use zenoh::query::Selector;
use std::convert::TryFrom;

// From a string
let sel = Selector::try_from("demo/sensor/**?_time=[now(-5m)..now()]").unwrap();
let ke = sel.key_expr();         // the KeyExpr part
let params = sel.parameters();   // the Parameters part

// Split into components
let (ke, params) = sel.split();
```

```python
# Python: pass selector string directly to session.get()
session.get("demo/sensor/**?_time=[now(-5m)..now()]")

# Or build a selector from key + parameters
import zenoh
session.get("demo/sensor/**", parameters="_time=[now(-5m)..now()]")
```

### Standardized Parameters

Zenoh reserves parameter names beginning with non-alphanumeric characters. Current standardized parameters:

#### `_time` — Time Range Filter (unstable)

Filters replies to those with timestamps within the specified range. The value uses the Zenoh Time DSL:

```
_time=[now(-1h)..now()]          last 1 hour
_time=[now(-30m)..now()]         last 30 minutes
_time=[2024-01-01T00:00:00Z..]   since a fixed timestamp
_time=[..now(-1d)]               everything older than 1 day
_time=[1704067200000..1704153600000]   epoch ms range
```

Usage:
```
demo/sensor/**?_time=[now(-1h)..now()]
```

In Rust with the `unstable` feature:
```rust
use zenoh::query::ZenohParameters;

let mut params = zenoh_protocol::core::Parameters::default();
let time_range: zenoh_util::time_range::TimeRange = "[now(-1h)..now()]".parse().unwrap();
params.set_time_range(time_range);
```

#### `_anyke` — Accept Any Reply Key Expression (unstable)

By default, a `get("a/b")` query only accepts replies whose key expression matches `a/b`. With `_anyke`, replies on any key expression are accepted.

This matters when a queryable is declared on `a/*` and contains data for both `a/b` and `a/c`. Without `_anyke`, only the `a/b` reply passes the filter. With `_anyke`, all replies pass.

```
a/b?_anyke
```

In Rust:
```rust
use zenoh::query::ZenohParameters;
let mut params = zenoh_protocol::core::Parameters::default();
params.set_reply_key_expr_any();
```

### Custom Parameters

Any parameter name that begins with an alphanumeric character is yours to use. Prefix with your application/service name to avoid conflicts:

```
demo/sensor/**?myapp_format=json;myapp_limit=100
```

Queryables receive the full parameters string and can parse it:

```rust
// In a queryable handler
async fn handle_query(query: Query) {
    let params = query.parameters();
    if let Some(format) = params.get("myapp_format") {
        println!("Requested format: {format}");
    }
}
```

```python
def handle_query(query):
    params_str = str(query.parameters)
    # parse manually or use urllib.parse.parse_qs
```

### Selectors in Subscriptions

Selectors are only valid in `get()` calls. **Do not use selector syntax in subscriber declarations** — the `?` is not a valid KE character and will cause a validation error.

```rust
// CORRECT: subscriber uses plain KE
session.declare_subscriber("demo/sensor/**").await?;

// WRONG: selector syntax in subscriber — validation error
session.declare_subscriber("demo/sensor/**?_time=[now(-1h)..now()]").await?; // ERROR
```

---

## 7. intersect() vs includes()

These are the two core predicates in the KE system. Understanding the difference is essential for building correct subscriptions, storages, and queryables.

### Definitions

**`A.intersects(B)`** — Returns `true` if there exists at least one concrete key that belongs to both sets A and B.

```
a/* intersects */a   → true   (both match a/a)
a/b intersects a/*   → true   (both match a/b)
a/* intersects b/*   → false  (a/x and b/x are always disjoint)
```

**`A.includes(B)`** — Returns `true` if every key that belongs to B also belongs to A. In other words, A's set is a superset of B's set.

```
a/**  includes  a/b      → true   (every a/b key is also in a/**)
a/**  includes  a/*      → true   (every a/x is also in a/**)
a/*   includes  a/**     → false  (a/b/c is in a/** but not in a/*)
a/*   includes  a/b      → true   (a/b is in a/*)
**    includes  a/b/c    → true   (** includes everything)
```

Includes is NOT commutative:
```
a/**  includes  a/b    → true
a/b   includes  a/**   → false
```

### When the Router Uses Each

**Subscription routing (intersect)**

When a publisher publishes on KE `P`, the router delivers to every subscriber declared on KE `S` where `P.intersects(S)`. See [matching guide](matching-guide.md) for how publishers can query whether matching subscribers exist. Intersection is symmetric, so `P intersects S` is the same check as `S intersects P`.

```
Publisher publishes on:    demo/robot/arm
Subscriber on:             demo/robot/*       → receives (intersects)
Subscriber on:             demo/**/arm        → receives (intersects)
Subscriber on:             demo/sensor/*      → does NOT receive (disjoint)
```

**Storage completeness (includes)**

A Zenoh storage is "complete" for a query KE `Q` if it has declared its storage KE `S` such that `S.includes(Q)`. Only a storage where `S.includes(Q)` is guaranteed to hold all data relevant to Q.

```
Storage declared on:   demo/robot/**   includes   demo/robot/arm   → complete
Storage declared on:   demo/robot/*    does NOT include demo/robot/arm/joint → incomplete
```

### Code Examples

```rust
use zenoh_keyexpr::keyexpr;

let a = keyexpr::new("a/**").unwrap();
let b = keyexpr::new("a/b").unwrap();
let c = keyexpr::new("a/*").unwrap();
let d = keyexpr::new("x/**").unwrap();

// intersect: is there any key in common?
assert!(a.intersects(b));   // true: a/b is in both
assert!(a.intersects(c));   // true: a/x is in both
assert!(!a.intersects(d));  // false: a/... and x/... are disjoint

// includes: is every key of right also in left?
assert!(a.includes(b));    // true: a/b is in a/**
assert!(a.includes(c));    // true: every a/x is in a/**
assert!(!c.includes(a));   // false: a/b/c is in a/** but not in a/*
assert!(!a.includes(d));   // false: x/y is in x/** but not in a/**
```

```python
import zenoh

session = zenoh.open(zenoh.Config())

# Python doesn't expose intersects/includes directly on strings,
# but the router applies intersect() semantics automatically:
sub = session.declare_subscriber("a/**")   # receives from a/b, a/b/c, etc.
pub = session.declare_publisher("a/b")
pub.put("hello")   # sub receives this because a/b intersects a/**
```

### Verified Behavioral Examples

From the test suite — these are authoritative:

```
intersect("a/*/c/*/e", "a/b/c/d/e")        → true
intersect("a/*/c/*/e", "a/c/e")            → false  (* requires exactly 1 chunk)
intersect("**", "a/b/c")                   → true
intersect("ab/**", "ab")                   → true   (** matches zero chunks)
intersect("**/xyz", "a/b/xyz/d/e/f/xyz")   → true
intersect("@a", "@ab")                     → false  (verbatim: exact match only)
intersect("@a/**", "@a")                   → true   (** matches zero after @a)
intersect("@a/*", "@a/@b")                 → false  (* cannot match @b verbatim)

includes("a/**", "ab")                     → false  (a/** and ab share a common prefix "a" but ab is not under a/)
includes("**", "a/b/c")                    → true
includes("a/*", "a/**")                    → false  (a/** includes a/b/c, a/* does not)
includes("ab/**", "ab")                    → true
includes("@a/**", "@a")                    → true
includes("@a/**", "@a/@b")                 → false  (* cannot match @b)
```

---

## 8. OwnedKeyExpr vs KeyExpr<'_>

Zenoh's Rust API provides two key expression types with different ownership models. Understanding when to use each avoids unnecessary clones and lifetime errors.

### `keyexpr` (lowercase) — Borrowed, Zero-Copy

`keyexpr` is a `str` newtype — a borrowed reference into existing string storage. It carries a lifetime and cannot outlive its source. Use it when you have a `&str` or `String` already allocated and want to validate and use it without copying.

```rust
use zenoh_keyexpr::keyexpr;

let s = "demo/robot/**";
let ke: &keyexpr = keyexpr::new(s)?;  // borrows from s
// ke.as_str() == "demo/robot/**"
// ke does not own its memory
```

### `OwnedKeyExpr` — Heap-Allocated, `Arc<str>` Backed

`OwnedKeyExpr` wraps an `Arc<str>`, making it cheaply clonable and `'static`. Use it when the KE must outlive the source string, be stored in a struct, or be passed across async task boundaries.

```rust
use zenoh_keyexpr::OwnedKeyExpr;
use std::str::FromStr;

// From a &str (allocates)
let ke = OwnedKeyExpr::try_from("demo/robot/**")?;

// From a String (no extra alloc if already String)
let ke: OwnedKeyExpr = "demo/robot/**".parse()?;

// Autocanonize before constructing
let ke = OwnedKeyExpr::autocanonize("demo/**/*".to_string())?;
// Results in "demo/*/**" (canonized)

// Cheap clone: Arc clone, not string copy
let ke2 = ke.clone();
```

### `KeyExpr<'a>` — The High-Level API Type

The zenoh crate itself uses `KeyExpr<'a>`, a wrapper around either a `&'a keyexpr` or an `OwnedKeyExpr`. Most user-facing API methods accept `impl Into<KeyExpr<'_>>`, which means you can pass strings, `OwnedKeyExpr`, or `&keyexpr` interchangeably.

```rust
use zenoh::key_expr::KeyExpr;

// From a static string literal (no allocation for 'static lifetime)
let ke: KeyExpr<'static> = KeyExpr::from_str_unchecked("demo/robot/**");

// From a validated string (safe)
let ke = KeyExpr::try_from("demo/robot/**")?;

// In API calls, just pass strings directly:
session.declare_subscriber("demo/robot/**").await?;
session.declare_publisher("demo/robot/arm").await?;
```

### Conversion Summary

| From | To | How |
|---|---|---|
| `&str` | `&keyexpr` | `keyexpr::new(s)?` |
| `String` | `OwnedKeyExpr` | `OwnedKeyExpr::try_from(s)?` |
| `&keyexpr` | `OwnedKeyExpr` | `ke.to_owned()` or `OwnedKeyExpr::from(ke)` |
| `OwnedKeyExpr` | `&keyexpr` | `ke.as_ref()` or deref coercion `&*ke` |
| `OwnedKeyExpr` | `String` | `String::from(ke)` |
| `&str` (autocanon) | `&keyexpr` | `keyexpr::autocanonize(&mut s)?` |
| `String` (autocanon) | `OwnedKeyExpr` | `OwnedKeyExpr::autocanonize(s)?` |

### Path Concatenation with `/`

`OwnedKeyExpr` implements `Div` (the `/` operator) for building KEs by joining segments:

```rust
let prefix = OwnedKeyExpr::try_from("demo/robot").unwrap();
let suffix = keyexpr::new("arm/joint1").unwrap();
let full = prefix / suffix;
// full == "demo/robot/arm/joint1"
```

The `join` method does the same thing but accepts `&str`:

```rust
let ke = keyexpr::new("demo/robot").unwrap();
let full = ke.join("arm/joint1")?;
// full == "demo/robot/arm/joint1" (OwnedKeyExpr)
```

---

## 9. Declared vs Inline Key Expressions

Zenoh supports two ways to use a key expression in publish/subscribe operations: inline (passing the string every time) or declared (registering the KE once and using a wire-efficient integer ID afterward).

### The Difference

**Inline**: Every publish/subscribe message carries the full key expression string on the wire. A KE like `demo/robot/arm/joint1/angle` is 32 bytes that travel with every sample.

**Declared**: The session registers the KE string once, receiving a compact integer ID (wire expression ID). Subsequent messages carry only that integer. The router maps integer → KE string internally.

### When Declaration Matters

Declaration pays off when:
- The same KE is used repeatedly (high-frequency publishing)
- The KE is long
- Network bandwidth is constrained (IoT, lossy links)

For one-shot queries or rare operations, the overhead of declaration may not be worth it.

### Rust API

```rust
use zenoh::key_expr::KeyExpr;

let session = zenoh::open(zenoh::Config::default()).await?;

// Declare a key expression for reuse
let ke = session.declare_keyexpr("demo/robot/arm/joint1").await?;

// Now use it — the wire carries an integer, not the string
session.put(&ke, 42.0f64).await?;
session.put(&ke, 43.5f64).await?;
session.put(&ke, 44.0f64).await?;

// Also works for subscribers
let sub = session.declare_subscriber(&ke).await?;
```

### Python API

```python
import zenoh

with zenoh.open(zenoh.Config()) as session:
    # Declare for reuse
    ke = session.declare_keyexpr("demo/robot/arm/joint1")

    pub = session.declare_publisher(ke)
    pub.put(42.0)
    pub.put(43.5)
    pub.put(44.0)
```

### Quantifying the Savings

For a KE of length N bytes published at rate R messages/second:
- Inline overhead: N bytes per message × R msgs/s = N×R bytes/s on the wire
- Declared overhead: ~4 bytes per message × R msgs/s = 4×R bytes/s on the wire

For `demo/factory/floor3/robot12/arm/joint1/angle` (44 bytes) at 100 Hz:
- Inline: 4,400 bytes/s of KE overhead
- Declared: 400 bytes/s (11× reduction just for the KE portion)

---

## 10. Key Formatters

Key Formatters let you define a **template** for a family of KEs, then use that template to both construct KEs and parse them back into named fields. This is especially useful when a KE embeds structured parameters like device IDs, user IDs, or resource paths.

### Format String Syntax

A format string is a regular KE with **specification** placeholders of the form:

```
${id:pattern}               single-line spec
${id:pattern#default}       spec with default value
$#{id:pattern}#             multi-line spec (when pattern/id contains '}')
$#{id:pattern#default}#     multi-line spec with default
```

Where:
- `id` is the field name (no `:` allowed)
- `pattern` is a valid KE that defines the allowed values for this field
- `default` (optional) is used when the field isn't set during formatting

Spec chunks must occupy whole chunks (preceded and followed by `/` or string boundaries). Wildcards are not allowed in non-spec portions of a format string.

### Examples

```
user_id/${user_id:*}/file/${file:*/**}
│       │             │
│       │             └── field 'file', pattern '*/**' (at least one chunk)
│       └── field 'user_id', pattern '*' (exactly one chunk)
└── literal prefix
```

```
device/${device_id:*}/sensor/${sensor_id:*}/reading
```

### Compile-Time Formats with `kedefine!`

For formats known at compile time, `kedefine!` macro generates a typed API with per-field accessor methods:

```rust
use zenoh::key_expr::format::{kedefine, keformat};

kedefine!(
    pub file_format: "user_id/${user_id:*}/file/${file:*/**}",
    pub settings_format: "user_id/${user_id:*}/settings/${setting:**}"
);

fn main() {
    // Formatting: build a KE from field values
    let mut formatter = file_format::formatter();
    let ke = keformat!(formatter, user_id = 42, file = "docs/readme").unwrap();
    println!("{ke}");  // user_id/42/file/docs/readme

    // Parsing: extract field values from a concrete KE
    let ke = zenoh_keyexpr::keyexpr::new("user_id/30/settings/dark_mode").unwrap();
    let parsed = settings_format::parse(ke).unwrap();
    assert_eq!(parsed.user_id(), zenoh_keyexpr::keyexpr::new("30").unwrap());
    // setting() returns Option<&keyexpr> for ** patterns (may be absent)
    assert_eq!(parsed.setting(), zenoh_keyexpr::keyexpr::new("dark_mode").ok());
}
```

### Runtime Formats with `KeFormat::new`

When the format string isn't known at compile time:

```rust
use zenoh_keyexpr::key_expr::format::KeFormat;

let format = KeFormat::new("a/${a:*}/b/$#{b:**}#/c").unwrap();

// Build a KE
let ke = format.formatter()
    .set("a", 1).unwrap()
    .set("b", "hi/there").unwrap()
    .build().unwrap();
assert_eq!(ke.as_str(), "a/1/b/hi/there/c");

// Build with empty b (** pattern allows empty)
let ke = format.formatter()
    .set("a", 1).unwrap()
    .set("b", "").unwrap()
    .build().unwrap();
assert_eq!(ke.as_str(), "a/1/b/c");  // empty b collapses cleanly
```

### Parsing and Field Extraction

```rust
use zenoh_keyexpr::key_expr::format::KeFormat;
use zenoh_keyexpr::keyexpr;

let format = KeFormat::new("device/${device_id:*}/sensor/${sensor_id:*}").unwrap();

let ke = keyexpr::new("device/robot-1/sensor/temp").unwrap();
let parsed = format.parse(ke).unwrap();

// Access by ID
let device_id = parsed.get("device_id").unwrap();  // "robot-1"
let sensor_id = parsed.get("sensor_id").unwrap();  // "temp"
```

### Greedy Parsing and Ambiguity

Specs are greedy and evaluated left-to-right. If your format has multiple `**` specs separated only by fixed text, the first `**` will consume as much as possible:

```
${a:**}/-/${b:**}  parsing  hey/-/-/there
→ a = "hey/-"    (greedily ate the first - too)
→ b = "there"
```

To avoid this ambiguity, separate `**` specs with verbatim chunks:

```
${src:**}/@/${dst:**}  parsing  hey/there/@/foo/bar
→ src = "hey/there"
→ dst = "foo/bar"
```

The `@` chunk cannot be consumed by `**`, so it acts as a hard boundary.

### Use Cases

1. **Per-device topics**: `device/${device_id:*}/${metric:**}` — subscribe with `device/**`, parse device ID on receipt
2. **Versioned APIs**: `api/@${version:v[0-9]*}/${endpoint:**}` (with verbatim)
3. **User namespaces**: `user/${user_id:*}/data/${path:**}` — multi-tenant data separation
4. **Source-destination routing**: `from/${src:**}/@/to/${dst:**}`

---

## 11. Router Behavior: When Matching Matters

Understanding where intersect and includes are applied in the Zenoh network helps design efficient key spaces.

### Publication Routing

When a session publishes a sample on KE `P`, the Zenoh router delivers it to every subscriber declared on KE `S` where `intersect(P, S) == true`.

```
Published on:          demo/robot/arm
Subscribers notified:  demo/robot/*         ✓ (intersects)
                       demo/**/arm          ✓ (intersects)
                       **                   ✓ (intersects)
                       demo/robot/arm       ✓ (exact match)
                       demo/sensor/*        ✗ (disjoint)
```

The check is performed at the router, not the subscriber. If the router decides a subscriber is not interested, the sample is never sent on that network link.

### Queryable and Storage Selection

When a session issues `get("Q")`, the router looks for:
- All queryables declared on `S` where `intersect(Q, S) == true`
- Among those, "best matching" prefers queryables where `S.includes(Q)` (they can answer completely)

```
Query on:          demo/robot/**
Queryable on demo/robot/**     → intersects AND includes → "complete" match
Queryable on demo/**           → intersects AND includes → "complete" match
Queryable on demo/robot/*      → intersects BUT NOT includes (misses deep paths)
```

### Subscription to Wild Publishers

When you subscribe with `**` or any broad KE, you receive from every publisher whose KE intersects yours. For routing efficiency, make subscriptions as specific as possible.

### Admin Space Isolation

The `@` namespace (adminspace) is a hermetic namespace. Even `**` does not match `@/...` keys. This guarantees Zenoh admin traffic is never accidentally captured by application-level subscriptions.

---

## 12. Quick Reference Tables

### Wildcard Summary

| Wildcard | Scope | Regex equivalent | Crosses `/`? | Example match | Example non-match |
|---|---|---|---|---|---|
| `*` | Whole chunk | `[^/]+` | No | `a/*/b` matches `a/x/b` | `a/x/y/b` |
| `**` | Zero or more chunks | `([^/]+/)*([^/]+)?` | Yes | `a/**/b` matches `a/b`, `a/x/b`, `a/x/y/b` | `a/b/c` |
| `$*` | Within chunk | `[^/]*` | No | `ab$*/b` matches `abxy/b` | `xab/b` |

### Set Relations

| Relation | Definition | Test method |
|---|---|---|
| Disjoint | No key in common | `!a.intersects(b)` |
| Intersect | At least one key in common | `a.intersects(b)` |
| A includes B | All of B's keys are in A | `a.includes(b)` |
| Equal | A includes B and B includes A | `a == b` (string equality) |

### Canon Form Rules

| Non-canonical | Canonical |
|---|---|
| `a/$*/b` | `a/*/b` |
| `a/$*$*/b` | `a/*/b` |
| `a/**/**/b` | `a/**/b` |
| `a/**/*` | `a/*/**` |
| `foo$*$*bar` | `foo$*bar` |

### Selector Parameters

| Parameter | Meaning | Status |
|---|---|---|
| `_time` | Time range filter, format: `[start..end]` | Unstable |
| `_anyke` | Accept replies from any key expression | Unstable |
| Custom (alphanumeric prefix) | Application-defined | Stable |

### Type Quick Reference (Rust)

| Type | Owned? | Thread-safe? | Use when |
|---|---|---|---|
| `&keyexpr` | No | N/A | Borrowing from existing `&str` |
| `OwnedKeyExpr` | Yes (`Arc<str>`) | Yes | Storing, async tasks, structs |
| `KeyExpr<'a>` | Either | Depends | High-level API parameter |

---

## 13. Common Mistakes

### Using `*` When `**` Is Needed

`*` matches exactly one chunk. If your key has variable depth, use `**`.

```rust
// WRONG: won't match robot/arm/joint1 (two chunks after robot/)
session.declare_subscriber("robot/*").await?;

// CORRECT: matches any depth under robot/
session.declare_subscriber("robot/**").await?;
```

### Using `**` When `*` Is Needed

Conversely, `**` is greedy and can match more than intended in intersect/includes checks.

```
a/*  includes  a/b      → true  (one chunk)
a/*  includes  a/b/c    → false (two chunks, * can't match both)
a/** includes  a/b/c    → true  (** matches multi-chunk)
```

If your storage KE is `data/**` and you query `data/sensor`, the storage is considered complete. But if you query `data/*` and your storage is `data/sensor/*`, the storage is NOT complete (it may be missing `data/temperature/*` etc.).

### Forgetting Canonicalization Before Validation

`keyexpr::new` requires the input to already be canonical. Passing a non-canonical string returns an error:

```rust
// WRONG: non-canonical input fails
keyexpr::new("hello/$*/world")?;   // Error: not canonical

// CORRECT option 1: autocanonize the string first
let mut s = "hello/$*/world".to_string();
let ke = keyexpr::autocanonize(&mut s)?;   // produces "hello/*/world"

// CORRECT option 2: use OwnedKeyExpr::autocanonize
let ke = OwnedKeyExpr::autocanonize("hello/$*/world".to_string())?;
```

### Using Selector Syntax in a Subscriber

Subscribers accept only key expressions. The `?` character is not valid in a KE and will cause a validation error.

```python
# WRONG
session.declare_subscriber("sensor/**?_time=[now(-1h)..now()]")  # Error

# CORRECT: subscribers don't time-filter; use a queryable + get for time queries
session.declare_subscriber("sensor/**")  # always receives live data
```

### Invalid Characters Causing Panics at Runtime

The characters `? # $ (outside $*)` are forbidden in KE chunks. Passing user-provided strings directly as KEs without validation can cause panics or errors deep in the network stack.

```rust
// DANGEROUS: user input may contain forbidden characters
let user_input = "sensor/device?type=temperature";  // ? is forbidden
session.put(user_input, data).await?;  // will fail

// SAFE: validate first
let ke = keyexpr::new(&user_input).map_err(|e| format!("Invalid KE: {e}"))?;
session.put(ke, data).await?;
```

```python
# Python: validation happens at bind time, not construction
# Pass through sanitized strings or handle ValueError
try:
    session.put("sensor/device?type=temp", data)
except Exception as e:
    print(f"Invalid key expression: {e}")
```

### Ambiguous Multi-`**` Formats

When using Key Formatters with multiple `**` specs, greedy left-to-right parsing can assign chunks to the wrong field.

```rust
// AMBIGUOUS: first ** greedily consumes everything before 'to'
let fmt = KeFormat::new("from/${src:**}/to/${dst:**}").unwrap();
// parsing "a/b/to/c/to/d" → src="a/b/to/c", dst="d"  (not what you wanted)

// UNAMBIGUOUS: verbatim separator
let fmt = KeFormat::new("from/${src:**}/@to/${dst:**}").unwrap();
// parsing "a/b/@to/c/d" → src="a/b", dst="c/d"  (clear boundary)
```

### Confusing Performance of `*` vs `$*`

Sub-chunk wildcard matching (`$*`) involves a linear scan algorithm. At scale, many subscribers using `$*` patterns slow down the router's routing table lookups compared to whole-chunk `*` patterns.

Design your key space to avoid `$*`:

```
AVOID:  factory-${id}-${zone}    ← requires $* to match
PREFER: factory/${id}/${zone}    ← uses fast * matching
```

### Assuming `**` Matches Verbatim Chunks

`**` cannot skip verbatim chunks (those starting with `@`). This is by design but surprises users coming from glob conventions.

```
my-api/**   does NOT match  my-api/@v2/endpoint
my-api/@v2/**  DOES match  my-api/@v2/endpoint
```

If you intend to match across versioned APIs, do not use verbatim chunks in the path.

### Publishing DELETE on `**`

```
session.delete("**").await?
```

This is semantically equivalent to deleting every key in every storage on the network. Use with extreme caution. Always prefer scoped KEs for delete operations.

---

*Sources: zenoh-keyexpr source (`borrowed.rs`, `owned.rs`, `canon.rs`, `include.rs`, `intersect/`, `format/mod.rs`), Key Expressions RFC, Key Formatters RFC, Zenoh API selector.rs, zenoh/examples/, zenoh-python/examples/*

## See Also

- [Queryable Complete Guide](queryable-complete-guide.md) — how key expressions are used in selectors and query routing
- [Liveliness Complete Guide](liveliness-complete-guide.md) — liveliness tokens are addressed by key expressions using the same syntax
- [Matching Guide](matching-guide.md) — MatchingStatus uses key expression intersection to detect subscribers
- [Programming Model Guide](programming-model-guide.md) — how key expressions fit into the broader pub/sub/query API
