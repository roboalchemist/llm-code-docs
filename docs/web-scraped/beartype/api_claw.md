# Source: https://beartype.readthedocs.io/en/latest/api_claw/

Tip

💗 **Upbear us** at [GitHub Sponsors](https://github.com/sponsors/leycec) and SonarQube Advanced Security
(Tidelift). **Follow us** [on Bluesky](https://leycec.bsky.social). **Friendzone us** [at Zulip](https://beartype.zulipchat.com).
Your generous support is our quality assurance. 💗

# Beartype Import Hooks[¶](#beartype-import-hooks)

**Beartype import hooks** enforce type hints across your entire app in two lines
of code with *no* runtime overhead. This is beartype import hooks in ten
seconds. dyslexia notwithstanding
# Add *ONE* of the following semantically equivalent two-liners to the very
# top of your &quot;{your_package}.__init__&quot; submodule. Start with *THE FAST WAY*.

# ....................{ THE FAST WAY }....................
from beartype.claw import beartype_this_package # &lt;-- this is boring, but...
beartype_this_package() # &lt;-- the fast way

# ....................{ THE LESS FAST WAY }....................
from beartype.claw import beartype_package # &lt;-- still boring, but...
beartype_package(&#39;{your_package}&#39;) # &lt;-- the less fast way

# ....................{ THE MORE SLOW WAY }....................
from beartype.claw import beartype_packages # &lt;-- boring intensifies
beartype_packages((&#39;{your_package}&#39;,)) # &lt;-- the more slow way

Beartype import hooks extend the surprisingly sharp claws of [`beartype`](../api_decor/#module-beartype) to
your full app stack, whether anyone else wanted you to do that or not. Claw your
way to the top of the bug heap; then sit on that heap with a smug expression. Do
it for the new guy sobbing quietly in his cubicle.

**Bear with Us**

- [Import Hooks Overview](#import-hooks-overview)

[Import Hooks Overview, Part Deux](#import-hooks-overview-part-deux)

- [What Is beartype_this_package()?](#what-is-beartype-this-package)

- [Why Is beartype_this_package()?](#why-is-beartype-this-package)

[Import Hooks API](#import-hooks-api)

- [Global Import Hooks](#global-import-hooks)

- [Import Hook Configuration](#import-hook-configuration)

## [Import Hooks Overview](#id5)[¶](#import-hooks-overview)

Beartype import hooks implicitly perform both:

Standard **runtime type-checking** (ala the [`beartype.beartype()`](../api_decor/#beartype.beartype)
decorator).
Standard **static type-checking** (ala [mypy](http://mypy-lang.org) and [pyright](https://github.com/Microsoft/pyright)) but **at runtime**
– and that ain’t standard.

Automate the [`beartype.beartype()`](../api_decor/#beartype.beartype) decorator away today with magical import
hooks published by the [`beartype.claw`](#module-beartype.claw) subpackage. When you install import
hooks from beartype, you augment beartype from a pure-runtime
second-generation type-checker into a hybrid runtime-static
third-generation type-checker. That’s right.
Beartype is now a tentacular cyberpunk horror like that mutant brain baby from
Katsuhiro Otomo’s dystopian 80’s masterpiece *Akira*. You can’t look away!
[](https://user-images.githubusercontent.com/217028/272775190-8996c4a2-b320-4ca1-ba83-5c4dd36e6165.png)
May Neo-Tokyo have mercy on your codebase’s soul.

## [Import Hooks Overview, Part Deux](#id6)[¶](#import-hooks-overview-part-deux)

Beartype import hooks is a hobbit hole so deep we had to deescalate it with
decrepit manga panels from *Akira*. Prepare to enter that hole.

### [What Is beartype_this_package()?](#id7)[¶](#what-is-beartype-this-package)

Let’s begin by outlining exactly **what** [`beartype_this_package()`](#beartype.claw.beartype_this_package) does.

As the simplest and most convenient of several import hooks published by the
[`beartype.claw`](#module-beartype.claw) subpackage, [`beartype_this_package()`](#beartype.claw.beartype_this_package) type-checks
*all* subsequently imported submodules of `{your_package}`. Notably,
[`beartype_this_package()`](#beartype.claw.beartype_this_package):

Implicitly decorates *all* callables and classes across `{your_package}` by
the [`beartype.beartype()`](../api_decor/#beartype.beartype) decorator. Rejoice, fellow mammals! You no
longer need to explicitly decorate anything by [`beartype.beartype()`](../api_decor/#beartype.beartype) ever
again. Of course, you *can* if you want to – but there’s no compelling reason
to do so and many compelling reasons *not* to do so. You have probably just
thought of five, but there are even more.
Implicitly appends *every* [**PEP 526**](https://peps.python.org/pep-0526/)-compliant annotated variable
assignment (e.g., muh_int: int = 'Pretty sure this isn't an integer, but
not sure.') across `{your_package}` by a new statement at the same
indentation level calling the [`beartype.door.die_if_unbearable()`](../api_door/#beartype.door.die_if_unbearable) function
passed both that variable and that type hint. Never do that manually. Now, you
never do.

Examples or we’re lying again. [`beartype_this_package()`](#beartype.claw.beartype_this_package) transforms your
`{your_package}.{buggy_submodule}` from this quietly broken code that you
insist you never knew about, you swear:
# This is &quot;{your_package}.{buggy_submodule}&quot;. It is bad, but you never knew.
import typing as t

bad_global: int = &#39;My eyes! The goggles do nothing.&#39; # &lt;-- no exception

def bad_function() -&gt; str:
 return b&quot;I could&#39;ve been somebody, instead of a bum byte string.&quot;
bad_function() # &lt;-- no exception

class BadClass(object):
 def bad_method(self) -&gt; t.NoReturn:
 return &#39;Nobody puts BadClass in the corner.&#39;
BadClass().bad_method() # &lt;-- no exception

…into this loudly broken code that even your unionized QA team can no longer
ignore:
# This is &quot;{your_package}.{buggy_submodule}&quot; on beartype_this_package().
# Any questions? Actually, that was rhetorical. No questions, please.
from beartype import beartype
from beartype.door import die_if_unbearable
import typing as t

bad_global: int = &#39;My eyes! The goggles do nothing.&#39;
die_if_unbearable(bad_global, int) # &lt;-- raises exception

@beartype
def bad_function() -&gt; str:
 return b&quot;I could&#39;ve been somebody, instead of a bum byte string.&quot;
bad_function() # &lt;-- raises exception

@beartype
class BadClass(object):
 def bad_method(self) -&gt; t.NoReturn:
 return &#39;Nobody puts BadClass in the corner.&#39;
BadClass().bad_method() # &lt;-- raises exception

By doing nothing, you saved five lines of extraneous boilerplate you no longer
need to maintain, preserved [DRY (Don’t Repeat Yourself)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), and mended
your coworker’s career, who you would have blamed for all this. You had nothing
to do with that code. It’s a nothingburger!
Beartype believes you. This is why we [`beartype_this_package()`](#beartype.claw.beartype_this_package).

This is what happens when we don’t beartype_this_package().

### [Why Is beartype_this_package()?](#id8)[¶](#why-is-beartype-this-package)

Let’s continue by justifying **why** you want to use
[`beartype_this_package()`](#beartype.claw.beartype_this_package). Don’t worry. The “why?” is easier than the
“what?”. It often is. The answer is: “Safety is my middle name.”
&lt;– more lies
[`beartype_this_package()`](#beartype.claw.beartype_this_package) isolates its bug-hunting action to the current
package. This is what everyone wants to try first. Type-checking only *your*
first-party package under *your* control is the safest course of action, because
you rigorously stress-tested your package with beartype. You did, didn’t you?
You’re not making us look bad here? Don’t make us look bad. We already have
GitHub and Reddit for that.
Other beartype import hooks – like [`beartype_packages()`](#beartype.claw.beartype_packages) or
`beartyping()` – can be (mis)used to dangerously type-check *other*
third-party packages outside your control that have probably never been
stress-tested with beartype. Those packages could raise type-checking violations
at runtime that you have no control over. If they don’t now, they could later.
Forward compatibility is out the window. `git blame` has things to say about
that.
If [`beartype_this_package()`](#beartype.claw.beartype_this_package) fails, there is no hope for your package. Even
though it might be beartype’s fault, beartype will still blame you for its
mistakes.

## [Import Hooks API](#id9)[¶](#import-hooks-api)

Beartype import hooks come in two flavours:

[Global import hooks](#api-claw-global), whose effects encompass *all*
subsequently imported packages and modules matching various patterns.
[Local import hooks](#api-claw-local), whose effects are isolated to only
specific packages and modules imported inside specific blocks of code. Any
subsequently imported packages and modules remain unaffected.

### [Global Import Hooks](#id10)[¶](#global-import-hooks)

Global beartype import hooks are… well, *global*. Their claws extend to a
horizontal slice of your full stack. These hooks globally type-check *all*
annotated callables, classes, and variable assignments in *all* subsequently
imported packages and modules matching various patterns.
With great globality comes great responsibility.

beartype.claw.beartype_this_package(***, *conf: [beartype.BeartypeConf](../api_decor/#beartype.BeartypeConf) = beartype.BeartypeConf()*) &#x2192; [None](https://docs.python.org/3/library/constants.html#None)[[source]](../_modules/beartype/claw/_clawmain/#beartype_this_package)[¶](#beartype.claw.beartype_this_package)

Parameters:
**conf** ([*beartype.BeartypeConf*](../api_decor/#beartype.BeartypeConf)) – Beartype configuration. Defaults to the default configuration
performing \(O(1)\) type-checking.

Raises:
**beartype.roar.BeartypeClawHookException** – If either:

This function is *not*
called from a module (i.e.,
this function is called
directly from within a
read–eval–print loop
(REPL)).
`conf` is *not* a
beartype configuration.

**Self-package runtime-static type-checking import hook.** This hook accepts
*no* package or module names, instead type-checking *all* annotated
callables, classes, and variable assignments across *all* submodules of the
**current package** (i.e., the caller-defined package directly calling this
function).
This hook only applies to subsequent imports performed *after* this hook, as
the term “import hook” implies; previously imported submodules and
subpackages remain unaffected.
This hook is typically called as the first statement in the `__init__`
submodule of whichever (sub)package you would like to type-check. If you
call this hook from:

Your top-level `{your_package}.__init__` submodule, this hook type-checks
your entire package. This includes *all* submodules and subpackages across
your entire package.
Some mid-level `{your_package}.{your_subpackage}.__init__` submodule,
this hook type-checks only that subpackage. This includes *only* submodules
and subsubpackages of that subpackage. All other submodules and subpackages
of your package remain unaffected (i.e., will *not* be type-checked).

# At the top of your &quot;{your_package}.__init__&quot; submodule:
from beartype import BeartypeConf # &lt;-- boilerplate
from beartype.claw import beartype_this_package # &lt;-- boilerplate: the revenge
beartype_this_package(conf=BeartypeConf(is_color=False)) # &lt;-- no color is best color

This hook is effectively syntactic sugar for the following idiomatic
one-liners that are so cumbersome, fragile, and unreadable that no one should
even be reading this:
beartype_this_package() # &lt;-- this...
beartype_package(__name__.rpartition(&#39;.&#39;)[0]) # &lt;-- ...is equivalent to this...
beartype_packages((__name__.rpartition(&#39;.&#39;)[0],)) # &lt;-- ...is equivalent to this.

When in doubt, have no doubt. Just call [`beartype_this_package()`](#beartype.claw.beartype_this_package).

New in version 0.15.0.

beartype_this_package(): It do be like that.

beartype.claw.beartype_package(*package_name: [str](https://docs.python.org/3/library/stdtypes.html#str)*, ***, *conf: [beartype.BeartypeConf](../api_decor/#beartype.BeartypeConf) = beartype.BeartypeConf()*) &#x2192; [None](https://docs.python.org/3/library/constants.html#None)[[source]](../_modules/beartype/claw/_clawmain/#beartype_package)[¶](#beartype.claw.beartype_package)

Parameters:

- **package_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – Absolute name of the package or module to be type-checked.

**conf** ([*beartype.BeartypeConf*](../api_decor/#beartype.BeartypeConf)) – Beartype configuration. Defaults to the default configuration
performing \(O(1)\) type-checking.

Raises:
**beartype.roar.BeartypeClawHookException** – If either:

`conf` is *not* a
beartype configuration.
`package_name` is either:

- *Not* a string.

- The empty string.

A non-empty string that
is *not* a valid
package or module
name (i.e.,
`&quot;.&quot;`-delimited
concatenation of valid
Python identifiers).

**Uni-package runtime-static type-checking import hook.** This hook accepts
only a single package or single module name, type-checking *all* annotated
callables, classes, and variable assignments across either:

If the passed name is that of a (sub)package, *all* submodules of that
(sub)package.
- If the passed name is that of a (sub)module, *only* that (sub)module.

This hook should be called *before* that package or module is imported; when
erroneously called *after* that package or module is imported, this hook
silently reduces to a noop (i.e., does nothing regardless of how many times
you squint at it suspiciously).
This hook is typically called as the first statement in the `__init__`
submodule of your top-level `{your_package}.__init__` submodule.
# At the top of your &quot;{your_package}.__init__&quot; submodule:
from beartype import BeartypeConf # &lt;-- &lt;Ctrl-c&gt; &lt;Ctrl-v&gt;
from beartype.claw import beartype_package # &lt;-- &lt;Ctrl-c&gt; &lt;Ctrl-v&gt; x 2
beartype_package(&#39;your_package&#39;, conf=BeartypeConf(is_debug=True))
 # ^-- they said explicit is better than implicit,
 # but all i got was this t-shirt and a hicky.

Of course, that’s fairly worthless. Just call [`beartype_this_package()`](#beartype.claw.beartype_this_package),
right? But what if you want to type-check just *one* subpackage or submodule
of your package rather than your *entire* package? In that case,
[`beartype_this_package()`](#beartype.claw.beartype_this_package) is overbearing. badum ching
Enter [`beartype_package()`](#beartype.claw.beartype_package), the outer limits of QA where you control the
horizontal and the vertical:
# Just because you can do something, means you should do something.
beartype_package(&#39;good_package.m.A.A.d_submodule&#39;) # &lt;-- fine-grained precision strike

[`beartype_package()`](#beartype.claw.beartype_package) shows it true worth, however, in type-checking
*other* people’s code. Because the [`beartype.claw`](#module-beartype.claw) API is a permissive
Sarlacc pit, [`beartype_package()`](#beartype.claw.beartype_package) happily accepts the absolute name of
*any* package or module – whether they wanted you to do that or not:
# Whenever you want to break something over your knee, never leave your
# favorite IDE [read: Vim] without beartype_package().
beartype_package(&#39;somebody_elses_package&#39;) # &lt;-- blow it up like you just don&#39;t care

This hook is effectively syntactic sugar for passing the
[`beartype_packages()`](#beartype.claw.beartype_packages) function a 1-tuple containing only this package or
module name.
beartype_package(&#39;your_package&#39;) # &lt;-- this...
beartype_packages((&#39;your_package&#39;,)) # &lt;-- ...is equivalent to this.

Pretend you didn’t see that. Just call [`beartype_package()`](#beartype.claw.beartype_package).

New in version 0.15.0.

Truer words were never spoken, wizened psychic baby lady.

beartype.claw.beartype_packages(*package_names: [collections.abc.Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[str](https://docs.python.org/3/library/stdtypes.html#str)]*, ***, *conf: [beartype.BeartypeConf](../api_decor/#beartype.BeartypeConf) = beartype.BeartypeConf()*) &#x2192; [None](https://docs.python.org/3/library/constants.html#None)[[source]](../_modules/beartype/claw/_clawmain/#beartype_packages)[¶](#beartype.claw.beartype_packages)

Parameters:

**package_name** ([*collections.abc.Iterable*](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – Iterable of the absolute names of one or more packages or
modules to be type-checked.
**conf** ([*beartype.BeartypeConf*](../api_decor/#beartype.BeartypeConf)) – Beartype configuration. Defaults to the default configuration
performing \(O(1)\) type-checking.

Raises:
**beartype.roar.BeartypeClawHookException** – If either:

`conf` is *not* a
beartype configuration.
`package_names` is
either:

- *Not* an iterable.

- The empty iterable.

A non-empty iterable
containing at least one
item that is either:

- *Not* a string.

- The empty string.

A non-empty string that
is *not* a valid
package or module
name (i.e.,
`&quot;.&quot;`-delimited
concatenation of valid
Python identifiers).

**Multi-package runtime-static type-checking import hook.** This hook accepts
one or more package and module names in any arbitrary order (i.e., order is
insignificant), type-checking *all* annotated callables, classes, and
variable assignments across:

For each passed name that is a (sub)package, *all* submodules of that
(sub)package.
- For each passed name that is a (sub)module, *only* that (sub)module.

This hook should be called *before* those packages and modules are imported;
when erroneously called *after* those packages and modules are imported, this
hook silently reduces to a noop. Squinting still does nothing.
This hook is typically called as the first statement in the `__init__`
submodule of your top-level `{your_package}.__init__` submodule.
# At the top of your &quot;{your_package}.__init__&quot; submodule:
from beartype import BeartypeConf # &lt;-- copy-pasta
from beartype.claw import beartype_packages # &lt;-- copy-pasta intensifies
beartype_packages((
 &#39;your_package&#39;,
 &#39;some_package.published_by.the_rogue_ai.Johnny_Twobits&#39;, # &lt;-- seems trustworthy
 &#39;numpy&#39;, # &lt;-- ...heh. no one knows what will happen here!
 &#39;scipy&#39;, # &lt;-- ...but we can guess, can&#39;t we? *sigh*
), conf=BeartypeConf(is_pep484_tower=True)) # &lt;-- so. u 2 h8 precision.

This hook is the penultimate force in [global import hooks](#api-claw-global). The terser [`beartype_this_package()`](#beartype.claw.beartype_this_package) and
[`beartype_package()`](#beartype.claw.beartype_package) hooks are effectively syntactic sugar for this
verboser hook.

One hook to QA them all, and in the darkness of your codebase bind them.

New in version 0.15.0.

[](https://user-images.githubusercontent.com/217028/272775529-42b85874-56b7-40b4-b9d8-19b603df1657.png)
It’s almost as if we know what “penultimate” means.

beartype.claw.beartype_all(***, *conf: [beartype.BeartypeConf](../api_decor/#beartype.BeartypeConf) = beartype.BeartypeConf()*) &#x2192; [None](https://docs.python.org/3/library/constants.html#None)[[source]](../_modules/beartype/claw/_clawmain/#beartype_all)[¶](#beartype.claw.beartype_all)

Parameters:
**conf** ([*beartype.BeartypeConf*](../api_decor/#beartype.BeartypeConf)) – Beartype configuration. Defaults to the default configuration
performing \(O(1)\) type-checking.

Raises:
**beartype.roar.BeartypeClawHookException** – If `conf` is *not* a
beartype configuration.

**All-packages runtime-static type-checking import hook.** This hook accepts
*no* package or module names, instead type-checking *all* callables, classes,
and variable assignments across *all* submodules of *all* packages.
This hook should be called *before* those packages and modules are imported;
when erroneously called *after* those packages and modules are imported, this
hook silently reduces to a noop. Not even squinting can help you now.
This hook is typically called as the first statement in the `__init__`
submodule of your top-level `{your_package}.__init__` submodule.
# At the top of your &quot;{your_package}.__init__&quot; submodule,
from beartype import BeartypeConf # &lt;-- @beartype seemed so innocent, once
from beartype.claw import beartype_all # &lt;-- where did it all go wrong?
beartype_all(conf=BeartypeConf(claw_is_pep526=False)) # &lt;-- U WILL BE ASSIMILATE

This hook is the ultimate import hook, spasmodically unleashing a wave of
bug-defenestrating action over **the entire Python ecosystem.** After calling
this hook, *any* package or module authored by *anybody* (including packages
and modules in CPython’s standard library) will be subject to the iron claw
of [`beartype.claw`](#module-beartype.claw). Its rule is law!
This hook is the runtime equivalent of a full-blown [pure-static](../faq/#faq-third) type-checker like [mypy](http://mypy-lang.org) or [pyright](https://github.com/Microsoft/pyright), enabling [full-stack](https://en.wikipedia.org/wiki/Solution_stack)
[runtime-static](../faq/#faq-hybrid) type-checking over your entire app. This
includes submodules defined by both:

- First-party proprietary packages authored explicitly for this app.

- Third-party open-source packages authored and maintained elsewhere.

Nothing is isolated. Everything is permanent. Do not trust this hook.

#### Caveat Emptor: Empty Promises Not Even a Cat Would Eat[¶](#caveat-emptor-empty-promises-not-even-a-cat-would-eat)

This hook imposes type-checking on *all* downstream packages importing your
package, which may not necessarily want, expect, or tolerate type-checking.
This hook is *not* intended to be called from intermediary APIs, libraries,
frameworks, or other middleware. Packages imported by other packages should
*not* call this hook. This hook is *only* intended to be called from
[full-stack](https://en.wikipedia.org/wiki/Solution_stack) end-user applications as a convenient alternative to manually
passing the names of all packages to be type-checked to the more granular
[`beartype_packages()`](#beartype.claw.beartype_packages) hook.
This hook is the extreme QA nuclear option. Because this hook is the extreme
QA nuclear option, **most codebases should not call this hook.**
[`beartype`](../api_decor/#module-beartype) cannot be held responsible for a sudden rupture in the
plenæne of normalcy, the space-time continuum, or your once-stable job. Pour
one out for those who are about to vitriolically explode their own code.

Nuke Python from orbit. Because now you can.

New in version 0.15.0.

[](https://github.com/beartype/beartype-assets/assets/217028/cf43dca7-1852-4fec-bcbc-6d4aeca23230)
The beartype_all() lifestyle. Short but sweet.

## [Import Hook Configuration](#id11)[¶](#import-hook-configuration)

Beartype import hooks accept an optional keyword-only `conf` parameter whose
value is a **beartype configuration** (i.e., [`beartype.BeartypeConf`](../api_decor/#beartype.BeartypeConf)
instance), defaulting to the default beartype configuration `BeartypeConf()`.
Unsurprisingly, that configuration configures the behaviour of its hook: e.g.,
# In your &quot;{your_package}.__init__&quot; submodule, enable @beartype&#39;s support for
# the PEP 484-compliant implicit numeric tower (i.e., expand &quot;int&quot; to &quot;int |
# float&quot; and &quot;complex&quot; to &quot;int | float | complex&quot;):
from beartype import BeartypeConf # &lt;-- it all seems so familiar
from beartype.claw import beartype_package # &lt;-- boil it up, boilerplate
beartype_package(&#39;your_package&#39;, conf=BeartypeConf(is_pep484_tower=True)) # &lt;-- *UGH.*

Equally unsurprisingly, [`beartype.BeartypeConf`](../api_decor/#beartype.BeartypeConf) has been equipped with
import hook-aware super powers. Fine-tune the behaviour of our import hooks for
your exact needs, including:

`BeartypeConf(claw_is_pep526: bool = True)`. By default,
[`beartype.claw`](#module-beartype.claw) type-checks annotated variable assignments like
`muh_int: int = 'Pretty sure this isn't an integer.'`. Although this is
*usually* what everyone wants, this may not be what someone suspicious wearing
aviator goggles, a red velvet cape, and too-tight black leather wants. Nobody
knows what those people want. If you are such a person, consider disabling
this option to reduce type safety and destroy your code like Neo-Tokyo vs.
Mecha-Baby-Godzilla: …who will win!?!?

BeartypeConf(warning_cls_on_decorator_exception: Optional[Type[Warning]] =
None). By default, [`beartype.claw`](#module-beartype.claw) emits non-fatal warnings rather than
fatal exceptions raised by the [`beartype.beartype()`](../api_decor/#beartype.beartype) decorator at
decoration time. This is *usually* what everyone wants, because
[`beartype.beartype()`](../api_decor/#beartype.beartype) currently fails to support all possible edge cases
and is thus likely to raise at least one exception while decorating your
entire package. To improve the resilience of [`beartype.claw`](#module-beartype.claw) against
those edge cases, [`beartype.beartype()`](../api_decor/#beartype.beartype) emits one warning for each
decoration exception and then simply continues to the next decoratable
callable or class. This is occasionally unhelpful. What if you really *do*
want [`beartype.claw`](#module-beartype.claw) to raise a fatal exception on the first such edge
case in your codebase – perhaps because you want to either see the full
exception traceback *or* punish your coworkers who are violating typing
standards by trying to use an imported module as a type hint?
…this actually happened In this case, consider:

Passing [`None`](https://docs.python.org/3/library/constants.html#None) as the value of this parameter. Doing so forces
[`beartype.claw`](#module-beartype.claw) to act strictly, inflexibly, and angrily. Expect
spittle-flecked mouth frothing and claws all over the place:

# In your &quot;{your_package}.__init__&quot; submodule, raise exceptions because you
# hate worky. The CI pipeline you break over your knee may just be your own.
from beartype import BeartypeConf # &lt;-- boiling boilerplate...
from beartype.claw import beartype_this_package # &lt;-- ...ain&#39;t even lukewarm
beartype_this_package(conf=BeartypeConf(warning_cls_on_decorator_exception=None)) # &lt;-- *ohboy*

 
 
 
 
 
 
 **
 
 previous

 Beartype API: It Bears Bookmarking

 
 
 
 
 next

 Beartype Decoration

 
 **