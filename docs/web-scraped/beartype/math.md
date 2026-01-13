# Source: https://beartype.readthedocs.io/en/latest/math/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# Maths: It’s Plural, Apparently[¶](#maths-it-s-plural-apparently)

Math(s) time, people. it’s happening.

**Bear with Us**

[Beartype Timings](#beartype-timings)

- [Timings Overview](#timings-overview)

[Timings Lower Bound](#timings-lower-bound)

- [Formulaic Formulas: They’re Back in Fashion](#formulaic-formulas-they-re-back-in-fashion)

- [Function Call Overhead: The New Glass Ceiling](#function-call-overhead-the-new-glass-ceiling)

- [Holy Balls of Flaming Dumpster Fires](#holy-balls-of-flaming-dumpster-fires)

- [But, But… That’s Not Good Enough!](#but-but-that-s-not-good-enough)

- [Nobody Expects the Linearithmic Time](#nobody-expects-the-linearithmic-time)

## [Beartype Timings](#id5)[¶](#beartype-timings)

Note

Additional timings performed by an unbiased third party employed by Cisco
Systems support the claims below. Notably,
beartype is substantially faster than [pydantic](https://docs.pydantic.dev) – the most popular competing
runtime type-checker – by **several orders of magnitude.** Yes, [pydantic](https://docs.pydantic.dev) was
Cythonized to native machine code in those timings. Believe!

Let’s profile beartype against other runtime type-checkers with a battery of
surely fair, impartial, and unbiased use cases:
$ bin/profile.bash

beartype profiler [version]: 0.0.2

python [basename]: python3.9
python [version]: Python 3.9.0
beartype [version]: 0.6.0
typeguard [version]: 2.9.1

===================================== str =====================================
profiling regime:
 number of meta-loops: 3
 number of loops: 100
 number of calls each loop: 100
decoration [none ]: 100 loops, best of 3: 359 nsec per loop
decoration [beartype ]: 100 loops, best of 3: 389 usec per loop
decoration [typeguard]: 100 loops, best of 3: 13.5 usec per loop
decoration + calls [none ]: 100 loops, best of 3: 14.8 usec per loop
decoration + calls [beartype ]: 100 loops, best of 3: 514 usec per loop
decoration + calls [typeguard]: 100 loops, best of 3: 6.34 msec per loop

=============================== Union[int, str] ===============================
profiling regime:
 number of meta-loops: 3
 number of loops: 100
 number of calls each loop: 100
decoration [none ]: 100 loops, best of 3: 1.83 usec per loop
decoration [beartype ]: 100 loops, best of 3: 433 usec per loop
decoration [typeguard]: 100 loops, best of 3: 15.6 usec per loop
decoration + calls [none ]: 100 loops, best of 3: 17.7 usec per loop
decoration + calls [beartype ]: 100 loops, best of 3: 572 usec per loop
decoration + calls [typeguard]: 100 loops, best of 3: 10 msec per loop

=========================== List[int] of 1000 items ===========================
profiling regime:
 number of meta-loops: 1
 number of loops: 1
 number of calls each loop: 7485
decoration [none ]: 1 loop, best of 1: 10.1 usec per loop
decoration [beartype ]: 1 loop, best of 1: 1.3 msec per loop
decoration [typeguard]: 1 loop, best of 1: 41.1 usec per loop
decoration + calls [none ]: 1 loop, best of 1: 1.24 msec per loop
decoration + calls [beartype ]: 1 loop, best of 1: 18.3 msec per loop
decoration + calls [typeguard]: 1 loop, best of 1: 104 sec per loop

============ List[Sequence[MutableSequence[int]]] of 10 items each ============
profiling regime:
 number of meta-loops: 1
 number of loops: 1
 number of calls each loop: 7485
decoration [none ]: 1 loop, best of 1: 11.8 usec per loop
decoration [beartype ]: 1 loop, best of 1: 1.77 msec per loop
decoration [typeguard]: 1 loop, best of 1: 48.9 usec per loop
decoration + calls [none ]: 1 loop, best of 1: 1.19 msec per loop
decoration + calls [beartype ]: 1 loop, best of 1: 81.2 msec per loop
decoration + calls [typeguard]: 1 loop, best of 1: 17.3 sec per loop

Note

- `sec` = seconds.

- `msec` = milliseconds = 10-3 seconds.

- `usec` = microseconds = 10-6 seconds.

- `nsec` = nanoseconds = 10-9 seconds.

### [Timings Overview](#id6)[¶](#timings-overview)

Beartype is:

**At least twenty times faster** (i.e., 20,000%) and consumes three orders
of magnitude less time in the worst case than [typeguard](https://github.com/agronholm/typeguard) – the only
comparable runtime type-checker also compatible with most modern Python
versions.
**Asymptotically faster** in the best case than [typeguard](https://github.com/agronholm/typeguard), which scales
linearly (rather than not at all) with the size of checked containers.
Constant across type hints, taking roughly the same time to check parameters
and return values hinted by the builtin type `str` as it does to check
those hinted by the unified type `Union[int, str]` as it does to check
those hinted by the container type `List[object]`. [typeguard](https://github.com/agronholm/typeguard) is
variable across type hints, taking significantly longer to check
`List[object]` as as it does to check `Union[int, str]`, which takes
roughly twice the time as it does to check `str`.

Beartype performs most of its work at *decoration* time. The `&#64;beartype`
decorator consumes most of the time needed to first decorate and then repeatedly
call a decorated function. Beartype is thus front-loaded. After paying the
upfront fixed cost of decoration, each type-checked call thereafter incurs
comparatively little overhead.
Conventional runtime type checkers perform most of their work at *call* time.
`&#64;typeguard.typechecked` and similar decorators consume almost none of the
time needed to first decorate and then repeatedly call a decorated function.
They’re back-loaded. Although the initial cost of decoration is essentially
free, each type-checked call thereafter incurs significant overhead.

### [Timings Lower Bound](#id7)[¶](#timings-lower-bound)

In general, `&#64;beartype` adds anywhere from 1µsec (i.e., \(10^{-6}\)
seconds) in the worst case to 0.01µsec (i.e., \(10^{-8}\) seconds) in the
best case of call-time overhead to each decorated callable. This superficially
seems reasonable – but is it?
Let’s delve deeper.

#### [Formulaic Formulas: They’re Back in Fashion](#id8)[¶](#formulaic-formulas-they-re-back-in-fashion)

Let’s formalize how exactly we arrive at the call-time overheads above.

Given any pair of reasonably fair timings between an undecorated callable and
its equivalent `&#64;beartype`-decorated callable, let:

\(n\) be the number of times (i.e., loop iterations) each callable is
repetitiously called.
- \(γ\) be the total time in seconds of all calls to that undecorated callable.

- \(λ\) be the total time in seconds of all calls to that `&#64;beartype`-decorated callable.

Then the call-time overhead \(Δ(n, γ, λ)\) added by `&#64;beartype` to each
call is:

\[Δ(n, γ, λ) = \tfrac{λ}{n} - \tfrac{γ}{n}\]
Plugging in \(n = 100000\), \(γ = 0.0435s\), and \(λ = 0.0823s\)
from [aforementioned third-party timings](https://github.com/beartype/beartype/issues/58#issuecomment-940100279), we see
that `&#64;beartype` on average adds call-time overhead of 0.388µsec to each
decorated call: e.g.,

\[\begin{split}Δ(100000, 0.0435s, 0.0823s) &amp;= \tfrac{0.0823s}{100000} - \tfrac{0.0435s}{100000} \\
 &amp;= 3.8800000000000003 * 10^{-7}s\end{split}\]
Again, this superficially *seems* reasonable – but is it? Let’s delve deeper.

#### [Function Call Overhead: The New Glass Ceiling](#id9)[¶](#function-call-overhead-the-new-glass-ceiling)

The added cost of calling `&#64;beartype`-decorated callables is a residual
artifact of the added cost of **stack frames** (i.e., function and method calls)
in Python. The mere act of calling *any* pure-Python callable adds a measurable
overhead – even if the body of that callable is just a noop semantically
equivalent to that year I just went hard on NG+ in *Persona 5: Royal.* This is
the minimal cost of Python function calls.
Since Python decorators *almost* always add at least one additional stack frame
(typically as a closure call) to the call stack of each decorated call, this
measurable overhead is the minimal cost of doing business with Python
decorators. Even the fastest possible Python decorator necessarily pays that
cost.
Our quandary thus becomes: “Is 0.01µsec to 1µsec of call-time overhead
reasonable *or* is this sufficiently embarrassing as to bring multigenerational
shame upon our entire extended family tree, including that second cousin
twice-removed who never sends a kitsch greeting card featuring Santa playing
with mischievous kittens at Christmas time?”
We can answer that by first inspecting the theoretical maximum efficiency for a
pure-Python decorator that performs minimal work by wrapping the decorated
callable with a closure that just defers to the decorated callable. This
excludes the identity decorator (i.e., decorator that merely returns the
decorated callable unmodified), which doesn’t actually perform *any* work
whatsoever. The fastest *meaningful* pure-Python decorator is thus:
def fastest_decorator(func):
 def fastest_wrapper(*args, **kwargs): return func(*args, **kwargs)
 return fastest_wrapper

Replacing `&#64;beartype` with `&#64;fastest_decorator` in aforementioned
third-party timings then exposes the minimal cost
of Python decoration – a lower bound that *all* Python decorators necessarily
pay:
$ python3.7 &lt;&lt;EOF
from timeit import timeit
def fastest_decorator(func):
 def fastest_wrapper(*args, **kwargs): return func(*args, **kwargs)
 return fastest_wrapper

@fastest_decorator
def main_decorated(arg01: str=&quot;__undefined__&quot;, arg02: int=0) -&gt; tuple:
 &quot;&quot;&quot;Proof of concept code implenting bear-typed args&quot;&quot;&quot;
 assert isinstance(arg01, str)
 assert isinstance(arg02, int)

 str_len = len(arg01) + arg02
 assert isinstance(str_len, int)
 return (&quot;bear_bar&quot;, str_len,)

def main_undecorated(arg01=&quot;__undefined__&quot;, arg02=0):
 &quot;&quot;&quot;Proof of concept code implenting duck-typed args&quot;&quot;&quot;
 assert isinstance(arg01, str)
 assert isinstance(arg02, int)

 str_len = len(arg01) + arg02
 assert isinstance(str_len, int)
 return (&quot;duck_bar&quot;, str_len,)

if __name__==&quot;__main__&quot;:
 num_loops = 100000

 decorated_result = timeit(&#39;main_decorated(&quot;foo&quot;, 1)&#39;, setup=&quot;from __main__ import main_decorated&quot;, number=num_loops)
 print(&quot;timeit decorated time: &quot;, round(decorated_result, 4), &quot;seconds&quot;)

 undecorated_result = timeit(&#39;main_undecorated(&quot;foo&quot;, 1)&#39;, setup=&quot;from __main__ import main_undecorated&quot;, number=num_loops)
 print(&quot;timeit undecorated time:&quot;, round(undecorated_result, 4), &quot;seconds&quot;)
EOF
timeit decorated time: 0.1185 seconds
timeit undecorated time: 0.0889 seconds

Again, plugging in \(n = 100000\), \(γ = 0.0889s\), and \(λ =
0.1185s\) from the same timings, we see that `&#64;fastest_decorator` on
average adds call-time overhead of 0.3µsec to each decorated call: e.g.,

\[\begin{split}Δ(100000, 0.0889s, 0.1185s) &amp;= \tfrac{0.1185s}{100000} - \tfrac{0.0889s}{100000} \\
 &amp;= 2.959999999999998 * 10^{-7}s\end{split}\]

#### [Holy Balls of Flaming Dumpster Fires](#id10)[¶](#holy-balls-of-flaming-dumpster-fires)

We saw above that `&#64;beartype` on average only adds call-time overhead of
0.388µsec to each decorated call. But \(0.388µsec - 0.3µsec = 0.088µsec\),
so `&#64;beartype` only adds 0.1µsec (generously rounding up) of *additional*
call-time overhead above and beyond that necessarily added by the fastest
possible Python decorator.
Not only is `&#64;beartype` within the same order of magnitude as the fastest
possible Python decorator, it’s effectively indistinguishable from the fastest
possible Python decorator on a per-call basis.
Of course, even a negligible time delta accumulated over 10,000 function calls
becomes *slightly* less negligible. Still, it’s pretty clear that `&#64;beartype`
remains the fastest possible runtime type-checker for now and all eternity.
*Amen.*

#### [But, But… That’s Not Good Enough!](#id11)[¶](#but-but-that-s-not-good-enough)

*Yeah.* None of us are best pleased with the performance of the official CPython
interpreter anymore, are we? CPython is that geriatric old man down the street
that everyone puts up with because they’ve seen [“Up!”](https://www.youtube.com/watch?v=F2bk_9T482g) and he means
well and he didn’t really mean to beat your equally geriatric 20-year-old tomcat
with a cane last week. Really, that cat had it comin’.
If `&#64;beartype` *still* isn’t ludicrously speedy enough for you under CPython,
we also officially support [PyPy](https://www.pypy.org) – where you’re likely to extract even more
ludicrous speed.
`&#64;beartype` (and every other runtime type-checker) will *always* be negligibly
slower than hard-coded inlined runtime type-checking, thanks to the negligible
(but surprisingly high) cost of Python function calls. Where this is
unacceptable, [PyPy](https://www.pypy.org) is your code’s new BFFL.

## [Nobody Expects the Linearithmic Time](#id12)[¶](#nobody-expects-the-linearithmic-time)

Most runtime type-checkers exhibit \(O(n)\) time complexity (where \(n\)
is the total number of items recursively contained in a container to be checked)
by recursively and repeatedly checking *all* items of *all* containers passed to
or returned from *all* calls of decorated callables.
Beartype guarantees \(O(1)\) time complexity by non-recursively but
repeatedly checking *one* random item at *all* nesting levels of *all*
containers passed to or returned from *all* calls of decorated callables, thus
amortizing the cost of deeply checking containers across calls.
Beartype exploits the [well-known coupon collector’s problem](https://en.wikipedia.org/wiki/Coupon_collector%27s_problem) applied to abstract trees of nested type hints, enabling us to
statistically predict the number of calls required to fully type-check all items
of an arbitrary container on average. Formally, let:

\(E(T)\) be the expected number of calls needed to check all items of a
container containing only non-container items (i.e., containing *no* nested
subcontainers) either passed to or returned from a `&#64;beartype`-decorated
callable.
- \(γ ≈ 0.5772156649\) be the [Euler–Mascheroni constant](https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant).

Then:

\[E(T) = n \log n + \gamma n + \frac{1}{2} + O \left( \frac{1}{n} \right)\]
The summation \(\frac{1}{2} + O \left( \frac{1}{n} \right) \le 1\) is
negligible. While non-negligible, the term \(\gamma n\) grows significantly
slower than the term \(n \log n\). So this reduces to:

\[E(T) = O(n \log n)\]
We now generalize this bound to the general case. When checking a container
containing *no* subcontainers, beartype only randomly samples one item from that
container on each call. When checking a container containing arbitrarily many
nested subcontainers, however, beartype randomly samples one random item from
each nesting level of that container on each call.
In general, beartype thus samples \(h\) random items from a container on
each call, where \(h\) is that container’s height (i.e., maximum number of
edges on the longest path from that container to a non-container leaf item
reachable from items directly contained in that container). Since \(h ≥ 1\),
beartype samples at least as many items each call as assumed in the usual
[coupon collector’s problem](https://en.wikipedia.org/wiki/Coupon_collector%27s_problem) and thus paradoxically takes a fewer number of
calls on average to check all items of a container containing arbitrarily many
subcontainers as it does to check all items of a container containing *no*
subcontainers.
Ergo, the expected number of calls \(E(S)\) needed to check all items of an
arbitrary container exhibits the same or better growth rate and remains bound
above by at least the same upper bounds – but probably tighter: e.g.,

\[E(S) = O(E(T)) = O(n \log n)\]
Fully checking a container takes no more calls than that container’s size times
the logarithm of that size on average. For example, fully checking a list of
50 integers is expected to take **225 calls** on average.
…and that’s how the QA was won: *eventually.*

 
 
 
 
 
 
 **
 
 previous

 Code

 
 
 
 
 next

 See Also

 
 **