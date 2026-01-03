# API guidelines {#api_changes}

API consistency and stability are of great value; Therefore, API changes
(e.g. signature changes, behavior changes, removals) will only be
conducted if the added benefit is worth the effort of adapting existing
code.

Because we are a visualization library, our primary output is the final
visualization the user sees; therefore, the appearance of the figure is
part of the API and any changes, either semantic or aesthetic, are
backwards-incompatible API changes.

## Add new API

Every new function, parameter and attribute that is not explicitly
marked as private (i.e., starts with an underscore) becomes part of
Matplotlib\'s public API. As discussed above, changing the existing API
is cumbersome. Therefore, take particular care when adding new API:

-   Mark helper functions and internal attributes as private by
    prefixing them with an underscore.

-   Carefully think about good names for your functions and variables.

-   Try to adopt patterns and naming conventions from existing parts of
    the Matplotlib API.

-   Consider making as many arguments keyword-only as possible. See also
    [API Evolution the Right Way \-- Add Parameters
    Compatibly]{.title-ref}\_\_.

    \_\_
    <https://emptysqua.re/blog/api-evolution-the-right-way/#adding-parameters>

## Add or change colormaps, color sequences, and styles

Visual changes are considered an API break. Therefore, we generally do
not modify existing colormaps, color sequences, or styles.

We put a high bar on adding new colormaps and styles to prevent
excessively growing them. While the decision is case-by-case, evaluation
criteria include:

-   novelty: Does it support a new use case? e.g. slight variations of
    existing maps, sequences and styles are likely not accepted.
-   usability and accessibility: Are colors of sequences sufficiently
    distinct? Has colorblindness been considered?
-   evidence of wide spread usage: for example academic papers, industry
    blogs and whitepapers, or inclusion in other visualization libraries
    or domain specific tools
-   open license: colormaps, sequences, and styles must have a BSD
    compatible license (see `license-discussion`{.interpreted-text
    role="ref"})

## Deprecate API {#deprecation-guidelines}

When deciding to deprecate API we carefully consider the balance between
the advantages (clearer interfaces, better usability, less maintenance)
and the disadvantages (users have to learn new API and have to modify
existing code).

::: tip
::: title
Tip
:::

A rough estimate on the current usage of an API can be obtained by a
GitHub code search. A good search pattern is typically
`[expression] language:Python NOT is:fork`. `[expression]` may be a
simple string, but often regular expressions are helpful to exclude
incorrect matches. You can start simple and look at the search results,
if there are too many incorrect matches, gradually refine your search
criteria.

It can also be helpful to add
`NOT path:**/matplotlib/** NOT path:**/site-packages/**` to exclude
matches where the matplotlib codebase is checked into another repo,
either as direct sources or as part of an environment.

*Example*: Calls of the method `Figure.draw()` could be matched using
`/\bfig(ure)?\.draw\(/`. This expression employs a number of patterns:

-   Add the opening bracket `(` after the method name to only find
    method calls.
-   Include a common object name if there are otherwise too many false
    positives. There are many `draw()` functions out there, but the ones
    we are looking for are likely called via `fig.draw()` or
    `figure.draw()`.
-   Use the word boundary marker `\b` to make sure your expression is
    not a matching as part of a longer word.

[Link to the resulting GitHub
search](https://github.com/search?q=%2F%5Cbfig%28ure%29%3F%5C.draw%5C%28%2F+language%3APython+NOT+is%3Afork&type=code)
:::

API changes in Matplotlib have to be performed following the deprecation
process below, except in very rare circumstances as deemed necessary by
the development team. Generally API deprecation happens in two stages:

-   **introduce:** warn users that the API *will* change
-   **expire:** API *is* changed as described in the introduction period

This ensures that users are notified before the change will take effect
and thus prevents unexpected breaking of code. Occasionally deprecations
are marked as **pending**, which means that the deprecation will be
introduced in a future release.

### Rules

-   Deprecations are targeted at the next
    `meso release <pr-milestones>`{.interpreted-text role="ref"} (e.g.
    3.Y)
-   Deprecated API is generally removed (expired) two point-releases
    after introduction of the deprecation. Longer deprecations can be
    imposed by core developers on a case-by-case basis to give more time
    for the transition
-   The old API must remain fully functional during the deprecation
    period
-   If alternatives to the deprecated API exist, they should be
    available during the deprecation period
-   If in doubt, decisions about API changes are finally made by the
    [API consistency
    lead](https://matplotlib.org/governance/people.html) developer.

### Introduce deprecation {#intro-deprecation}

Deprecations are introduced to warn users that the API will change. The
deprecation notice describes how the API will change. When alternatives
to the deprecated API exist, they are also listed in the notice and
decorators.

1.  Create a `deprecation notice <api_whats_new>`{.interpreted-text
    role="ref"}

2.  If possible, issue a
    [\~matplotlib.MatplotlibDeprecationWarning]{.title-ref} when the
    deprecated API is used. There are a number of helper tools for this:

    -   Use `_api.warn_deprecated()` for general deprecation warnings
    -   Use the decorator `@_api.deprecated` to deprecate classes,
        functions, methods, or properties
    -   Use `@_api.deprecate_privatize_attribute` to annotate
        deprecation of attributes while keeping the internal private
        version.
    -   To warn on changes of the function signature, use the decorators
        `@_api.delete_parameter`, `@_api.rename_parameter`, and
        `@_api.make_keyword_only`

    All these helpers take a first parameter *since*, which should be
    set to the next point release, e.g. \"3.x\".

    You can use standard rst cross references in *alternative*.

3.  Make appropriate changes to the type hints in the associated `.pyi`
    file. The general guideline is to match runtime reported behavior.

    -   Items marked with `@_api.deprecated` or
        `@_api.deprecate_privatize_attribute` are generally kept during
        the expiry period, and thus no changes are needed on
        introduction.
    -   Items decorated with `@_api.rename_parameter` or
        `@_api.make_keyword_only` report the *new* (post deprecation)
        signature at runtime, and thus *should* be updated on
        introduction.
    -   Items decorated with `@_api.delete_parameter` should include a
        default value hint for the deleted parameter, even if it did not
        previously have one (e.g. `param: <type> = ...`).

### Expire deprecation

The API changes described in the introduction notice are only
implemented after the introduction period has expired.

1.  Create a
    `deprecation announcement <api_whats_new>`{.interpreted-text
    role="ref"}. For the content, you can usually copy the deprecation
    notice and adapt it slightly.
2.  Change the code functionality and remove any related deprecation
    warnings.
3.  Make appropriate changes to the type hints in the associated `.pyi`
    file.
    -   Items marked with `@_api.deprecated` or
        `@_api.deprecate_privatize_attribute` are to be removed on
        expiry.
    -   Items decorated with `@_api.rename_parameter` or
        `@_api.make_keyword_only` will have been updated at
        introduction, and require no change now.
    -   Items decorated with `@_api.delete_parameter` will need to be
        updated to the final signature, in the same way as the `.py`
        file signature is updated.
    -   Any entries in
        `ci/mypy-stubtest-allowlist.txt`{.interpreted-text role="file"}
        which indicate a deprecation version should be double checked.
        In most cases this is not needed, though some items were never
        type hinted in the first place and were added to this file
        instead. For removed items that were not in the stub file, only
        deleting from the allowlist is required.

### Pending deprecation

A pending deprecation is an announcement that a deprecation will be
introduced in the future. By default, pending deprecations do not raise
a warning to the user; however, pending deprecations are rendered in the
documentation and listed in the release notes. Pending notices are
primarily intended to give downstream library and tool developers time
to adapt their code so that it does not raise a deprecation warning.
This is because their users cannot act on warnings triggered by how the
tools and libraries use Matplotlib. It\'s also possible to run Python in
dev mode to raise [PendingDeprecationWarning]{.title-ref}.

To mark a deprecation as pending, set the following parameters on the
appropriate deprecation decorator: \* the *pending* parameter is set to
`True` \* the *removal* parameter is left blank

When converting a pending deprecation to an introduced deprecation,
update the decorator such that: \* *pending* is set to `False` \*
*since* is set to the next meso release (3.Y+1) \* *removal* is set to
at least 2 meso releases after (3.Y+3) introduction.

Pending deprecations are documented in the
`API change notes <api_whats_new>`{.interpreted-text role="ref"} in the
same manner as introduced and expired deprecations. The notice should
include *pending deprecation* in the title.

::: redirect-from
/devel/coding_guide#new-features-and-api-changes
:::

## Announce new and deprecated API {#api_whats_new}

When adding or changing the API in a backward in-compatible way, please
add the appropriate
`versioning directive <versioning-directives>`{.interpreted-text
role="ref"} and document it in the
`release notes <release-notes>`{.interpreted-text role="ref"} by adding
an entry to the appropriate folder:

+-------------+---------------------+---------------------------------+
|             | > versioning        | > announcement folder           |
|             | > directive         |                                 |
+=============+=====================+=================================+
| new feature | `..                 | `doc/release/nex                |
|             | versionadded:: 3.N` | t_whats_new/`{.interpreted-text |
|             |                     | role="file"}                    |
+-------------+---------------------+---------------------------------+
| API change  | `.. ve              | `doc/api/next_api_ch            |
|             | rsionchanged:: 3.N` | anges/[kind]`{.interpreted-text |
|             |                     | role="file"}                    |
+-------------+---------------------+---------------------------------+

When deprecating API, please add a notice as described in the
`deprecation guidelines <deprecation-guidelines>`{.interpreted-text
role="ref"} and summarized here:

+-------+---------------------------+---------------------------------+
| >     |                           | > announcement folder           |
| stage |                           |                                 |
+=======+===========================+=================================+
| `     |                           | `doc/api/next_api_changes       |
| intro |                           | /deprecation`{.interpreted-text |
| duce  |                           | role="file"}                    |
| depre |                           |                                 |
| catio |                           |                                 |
| n <in |                           |                                 |
| tro-d |                           |                                 |
| eprec |                           |                                 |
| ation |                           |                                 |
| >`{.i |                           |                                 |
| nterp |                           |                                 |
| reted |                           |                                 |
| -text |                           |                                 |
| r     |                           |                                 |
| ole=" |                           |                                 |
| ref"} |                           |                                 |
+-------+---------------------------+---------------------------------+
| `exp  |                           | `doc/api/next_api_ch            |
| ire d |                           | anges/[kind]`{.interpreted-text |
| eprec |                           | role="file"}                    |
| ation |                           |                                 |
|  <exp |                           |                                 |
| ire-d |                           |                                 |
| eprec |                           |                                 |
| ation |                           |                                 |
| >`{.i |                           |                                 |
| nterp |                           |                                 |
| reted |                           |                                 |
| -text |                           |                                 |
| r     |                           |                                 |
| ole=" |                           |                                 |
| ref"} |                           |                                 |
+-------+---------------------------+---------------------------------+

Generally the introduction notices can be repurposed for the expiration
notice as they are expected to be describing the same API changes and
removals.

### Versioning directives

When making a backward incompatible change, please add a versioning
directive in the docstring. The directives should be placed at the end
of a description block. For example:

    class Foo:
        """
        This is the summary.

        Followed by a longer description block.

        Consisting of multiple lines and paragraphs.

        .. versionadded:: 3.5

        Parameters
        ----------
        a : int
            The first parameter.
        b: bool, default: False
            This was added later.

            .. versionadded:: 3.6
        """

        def set_b(b):
            """
            Set b.

            .. versionadded:: 3.6

            Parameters
            ----------
            b: bool

For classes and functions, the directive should be placed before the
*Parameters* section. For parameters, the directive should be placed at
the end of the parameter description. The micro release version is
omitted and the directive should not be added to entire modules.

### Release notes

For both change notes and what\'s new, please avoid using
cross-references in section titles as it causes links to be confusing in
the table of contents. Instead, ensure that a cross-reference is
included in the descriptive text.

#### API change notes

API change notes for future releases are collected in
`doc/api/next_api_changes/`{.interpreted-text role="file"}. They are
divided into four subdirectories:

-   **Deprecations**: Announcements of future changes. Typically, these
    will raise a deprecation warning and users of this API should change
    their code to stay compatible with future releases of Matplotlib. If
    possible, state what should be used instead.
-   **Removals**: Parts of the API that got removed. If possible, state
    what should be used instead.
-   **Behaviour changes**: API that stays valid but will yield a
    different result.
-   **Development changes**: Changes to the build process, dependencies,
    etc.

Please place new entries in these directories with a new file named
`99999-ABC.rst`, where `99999` would be the PR number, and `ABC` the
author\'s initials. Typically, each change will get its own file, but
you may also amend existing files when suitable. The overall goal is a
comprehensible documentation of the changes.

A typical entry could look like this:

    Locators
    ~~~~~~~~
    The unused `Locator.autoscale()` method is deprecated (pass the axis
    limits to `Locator.view_limits()` instead).

Please avoid using references in section titles, as it causes links to
be confusing in the table of contents. Instead, ensure that a reference
is included in the descriptive text. Use inline literals (double
backticks) to denote code objects in the title.

#### What\'s new notes

Each new feature (e.g. function, parameter, config value, behavior,
\...) must be described through a \"What\'s new\" entry.

Each entry is written into a separate file in the
`doc/release/next_whats_new/`{.interpreted-text role="file"} directory.
They are sorted and merged into `whats_new.rst`{.interpreted-text
role="file"} during the release process.

When adding an entry please look at the currently existing files to see
if you can extend any of them. If you create a file, name it something
like `cool_new_feature.rst`{.interpreted-text role="file"} if you have
added a brand new feature or something like
`updated_feature.rst`{.interpreted-text role="file"} for extensions of
existing features.

Include contents of the form:

    Section title for feature
    -------------------------

    A description of the feature from the user perspective. This should include
    what the feature allows users to do and how the feature is used. Technical
    details should be left out when they do not impact usage, for example
    implementation details.

    The description may include a a short instructive example, if it helps to
    understand the feature.

Please avoid using references in section titles, as it causes links to
be confusing in the table of contents. Instead, ensure that a reference
is included in the descriptive text. Use inline literals (double
backticks) to denote code objects in the title.

## Discourage API

We have API that we do not recommend anymore for new code, but that
cannot be deprecated because its removal would be breaking
backward-compatibility and too disruptive. In such a case we can
formally discourage API. This can cover specific parameters, call
patterns, whole methods etc.

To do so, add a note to the docstring :

    .. admonition:: Discouraged

       [description and suggested alternative]

You find several examples for good descriptions if you search the
codebase for `.. admonition:: Discouraged`.

Additionally, if a whole function is discouraged, prefix the summary
line with `[*Discouraged*]` so that it renders in the API overview like
this

> \[*Discouraged*\] Return the XAxis instance.
