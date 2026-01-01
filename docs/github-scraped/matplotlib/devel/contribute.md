::: redirect-from
/devel/contributing
:::

# Contributing guide {#contributing}

You\'ve discovered a bug or something else you want to change in
Matplotlib --- excellent!

You\'ve worked out a way to fix it --- even better!

You want to tell us about it --- best of all!

Below, you can find a number of ways to contribute, and how to connect
with the Matplotlib community.

## Ways to contribute

::: {.dropdown open="" icon="person-fill"}
Do I really have something to contribute to Matplotlib?

100% yes! There are so many ways to contribute to our community. Take a
look at the following sections to learn more.

There are a few typical new contributor profiles:

-   **You are a Matplotlib user, and you see a bug, a potential
    improvement, or something that annoys you, and you can fix it.**

    You can search our [issue
    tracker](https://github.com/matplotlib/matplotlib/issues) for an
    existing issue that describes your problem or open a new issue to
    inform us of the problem you observed and discuss the best approach
    to fix it. If your contributions would not be captured on GitHub
    (social media, communication, educational content), you can also
    reach out to us on
    [gitter](https://gitter.im/matplotlib/matplotlib),
    [Discourse](https://discourse.matplotlib.org/) or attend any of our
    [community meetings](https://scientific-python.org/calendars).

-   **You are not a regular Matplotlib user but a domain expert: you
    know about visualization, 3D plotting, design, technical writing,
    statistics, or some other field where Matplotlib could be
    improved.**

    Awesome --- you have a focus on a specific application and domain
    and can start there. In this case, maintainers can help you figure
    out the best implementation; [open an
    issue](https://github.com/matplotlib/matplotlib/issues/new/choose)
    in our issue tracker, and we\'ll be happy to discuss technical
    approaches.

    If you can implement the solution yourself, even better! Consider
    contributing the change as a
    `pull request <how-to-pull-request>`{.interpreted-text role="ref"}
    right away.

-   **You are new to Matplotlib, both as a user and contributor, and
    want to start contributing but have yet to develop a particular
    interest.**

    Having some previous experience or relationship with the library can
    be very helpful when making open-source contributions. It helps you
    understand why things are the way they are and how they *should* be.
    Having first-hand experience and context is valuable both for what
    you can bring to the conversation (and given the breadth of
    Matplotlib\'s usage, there is a good chance it is a unique context
    in any given conversation) and make it easier to understand where
    other people are coming from.

    Understanding the entire codebase is a long-term project, and nobody
    expects you to do this right away. If you are determined to get
    started with Matplotlib and want to learn, going through the basic
    functionality, choosing something to focus on (3d, testing,
    documentation, animations, etc.) and gaining context on this area by
    reading the issues and pull requests touching these subjects is a
    reasonable approach.
:::

### Code {#contribute_code}

You want to implement a feature or fix a bug or help with maintenance -
much appreciated! Our library source code is found in:

-   Python library code: `lib/`{.interpreted-text role="file"}
-   C-extension code: `src/`{.interpreted-text role="file"}
-   Tests: `lib/matplotlib/tests/`{.interpreted-text role="file"}

Because many people use and work on Matplotlib, we have guidelines for
keeping our code consistent and mitigating the impact of changes.

-   `coding_guidelines`{.interpreted-text role="ref"}
-   `api_changes`{.interpreted-text role="ref"}
-   `pr-guidelines`{.interpreted-text role="ref"}

Code is contributed through pull requests, so we recommend that you
start at `how-to-pull-request`{.interpreted-text role="ref"} If you get
stuck, please reach out on the `contributor_incubator`{.interpreted-text
role="ref"}

### Documentation {#contribute_documentation}

You, as an end-user of Matplotlib can make a valuable contribution
because you can more clearly see the potential for improvement than a
core developer. For example, you can:

-   Fix a typo
-   Clarify a docstring
-   Write or update an `example plot <gallery>`{.interpreted-text
    role="ref"}
-   Write or update a comprehensive
    `tutorial <tutorials>`{.interpreted-text role="ref"}

Our code is documented inline in the source code files in
`matplotlib/lib`{.interpreted-text role="file"}. Our website structure
mirrors our folder structure, meaning that a narrative document\'s URL
roughly corresponds to its location in our folder structure:

::: grid
1 1 2 2

::: grid-item
using the library

-   `galleries/plot_types/`{.interpreted-text role="file"}
-   `users/getting_started/`{.interpreted-text role="file"}
-   `galleries/user_explain/`{.interpreted-text role="file"}
-   `galleries/tutorials/`{.interpreted-text role="file"}
-   `galleries/examples/`{.interpreted-text role="file"}
-   `doc/api/`{.interpreted-text role="file"}
:::

::: grid-item
information about the library

-   `doc/install/`{.interpreted-text role="file"}
-   `doc/project/`{.interpreted-text role="file"}
-   `doc/devel/`{.interpreted-text role="file"}
-   `doc/users/resources/index.rst`{.interpreted-text role="file"}
-   `doc/users/faq.rst`{.interpreted-text role="file"}
:::
:::

Other documentation is generated from the following external sources:

-   matplotlib.org homepage:
    <https://github.com/matplotlib/mpl-brochure-site>
-   cheat sheets: <https://github.com/matplotlib/cheatsheets>
-   third party packages:
    <https://github.com/matplotlib/mpl-third-party>

Instructions and guidelines for contributing documentation are found in:

-   `document`{.interpreted-text role="doc"}
-   `style_guide`{.interpreted-text role="doc"}
-   `tag_guidelines`{.interpreted-text role="doc"}

Documentation is contributed through pull requests, so we recommend that
you start at `how-to-pull-request`{.interpreted-text role="ref"}. If
that feels intimidating, we encourage you to [open an
issue](https://github.com/matplotlib/matplotlib/issues/new?assignees=&labels=Documentation&projects=&template=documentation.yml&title=%5BDoc%5D%3A+)
describing what improvements you would make. If you get stuck, please
reach out on the `contributor_incubator`{.interpreted-text role="ref"}

### Triage {#contribute_triage}

We appreciate your help keeping the [issue
tracker](https://github.com/matplotlib/matplotlib/issues) organized
because it is our centralized location for feature requests, bug
reports, tracking major projects, and discussing priorities. Some
examples of what we mean by triage are:

-   labeling issues and pull requests
-   verifying bug reports
-   debugging and resolving issues
-   linking to related issues, discussion, and external work

Our triage process is discussed in detail in
`bug_triaging`{.interpreted-text role="ref"}.

If you have any questions about the process, please reach out on the
`contributor_incubator`{.interpreted-text role="ref"}

### Community {#other_ways_to_contribute}

Matplotlib\'s community is built by its members, if you would like to
help out see our `communications-guidelines`{.interpreted-text
role="ref"}.

It helps us if you spread the word: reference the project from your blog
and articles or link to it from your website!

If Matplotlib contributes to a project that leads to a scientific
publication, please cite us following the
`/project/citing`{.interpreted-text role="doc"} guidelines.

If you have developed an extension to Matplotlib, please consider adding
it to our [third party
package](https://github.com/matplotlib/mpl-third-party) list.

## Restrictions on Generative AI Usage {#generative_ai}

We expect authentic engagement in our community.

-   Do not post output from Large Language Models or similar generative
    AI as comments on GitHub or our discourse server, as such comments
    tend to be formulaic and low content.
-   If you use generative AI tools as an aid in developing code or
    documentation changes, ensure that you fully understand the proposed
    changes and can explain why they are the correct approach.

Make sure you have added value based on your personal competency to your
contributions. Just taking some input, feeding it to an AI and posting
the result is not of value to the project. To preserve precious core
developer capacity, we reserve the right to rigorously reject seemingly
AI generated low-value contributions.

## New contributors {#new_contributors}

Everyone comes to the project from a different place --- in terms of
experience and interest --- so there is no one-size-fits-all path to
getting involved. We recommend looking at existing issue or pull request
discussions, and following the conversations during pull request reviews
to get context. Or you can deep-dive into a subset of the code-base to
understand what is going on.

### New contributors meeting {#new_contributors_meeting}

Once a month, we host a meeting to discuss topics that interest new
contributors. Anyone can attend, present, or sit in and listen to the
call. Among our attendees are fellow new contributors, as well as
maintainers, and veteran contributors, who are keen to support
onboarding of new folks and share their experience. You can find our
community calendar link at the [Scientific Python
website](https://scientific-python.org/calendars/), and you can browse
previous meeting notes on
[GitHub](https://github.com/matplotlib/ProjectManagement/tree/master/new_contributor_meeting).
We recommend joining the meeting to clarify any doubts, or lingering
questions you might have, and to get to know a few of the people behind
the GitHub handles 😉. You can reach out to us on
[gitter](https://gitter.im/matplotlib/matplotlib) for any clarifications
or suggestions. We ❤ feedback!

### Contributor incubator {#contributor_incubator}

The incubator is our non-public communication channel for new
contributors. It is a private
[gitter](https://gitter.im/matplotlib/matplotlib) (chat) room moderated
by core Matplotlib developers where you can get guidance and support for
your first few PRs. It\'s a place where you can ask questions about
anything: how to use git, GitHub, how our PR review process works,
technical questions about the code, what makes for good documentation or
a blog post, how to get involved in community work, or get a
\"pre-review\" on your PR.

To join, please go to our public [community
gitter](https://gitter.im/matplotlib/community) channel, and ask to be
added to `#incubator`. One of our core developers will see your message
and will add you.

### Good first issues {#good_first_issues}

While any contributions are welcome, we have marked some issues as
particularly suited for new contributors by the label [good first
issue](https://github.com/matplotlib/matplotlib/labels/good%20first%20issue).
These are well documented issues, that do not require a deep
understanding of the internals of Matplotlib. The issues may
additionally be tagged with a difficulty. `Difficulty: Easy` is suited
for people with little Python experience. `Difficulty: Medium` and
`Difficulty: Hard` require more programming experience. This could be
for a variety of reasons, among them, though not necessarily all at the
same time:

-   The issue is in areas of the code base which have more
    interdependencies, or legacy code.
-   It has less clearly defined tasks, which require some independent
    exploration, making suggestions, or follow-up discussions to clarify
    a good path to resolve the issue.
-   It involves Python features such as decorators and context managers,
    which have subtleties due to our implementation decisions.

### First contributions {#first_contribution}

If this is your first open source contribution, or your first time
contributing to Matplotlib, and you need help or guidance finding a good
first issue, look no further. This section will guide you through each
step:

1.  Navigate to the [issues
    page](https://github.com/matplotlib/matplotlib/issues/).
2.  Filter labels with [\"Difficulty:
    Easy\"](https://github.com/matplotlib/matplotlib/labels/Difficulty%3A%20Easy)
    & [\"Good first
    Issue\"](https://github.com/matplotlib/matplotlib/labels/good%20first%20issue)
    (optional).
3.  Click on an issue you would like to work on, and check to see if the
    issue has a pull request opened to resolve it.
    -   A good way to judge if you chose a suitable issue is by asking
        yourself, \"Can I independently submit a PR in 1-2 weeks?\"
4.  Check existing pull requests (e.g., `28476`{.interpreted-text
    role="ghpull"}) and filter by the issue number to make sure the
    issue is not in progress:
    -   If the issue has a pull request (is in progress), tag the user
        working on the issue, and ask to collaborate (optional).
    -   If there is no pull request,
        `create a new pull request <how-to-pull-request>`{.interpreted-text
        role="ref"}.
5.  Please familiarize yourself with the pull request template (see
    below), and ensure you understand/are able to complete the template
    when you open your pull request. Additional information can be found
    in the [pull request
    guidelines](https://matplotlib.org/devdocs/devel/pr_guide.html).

::: {.dropdown open=""}
[Pull request
template](https://github.com/matplotlib/matplotlib/blob/main/.github/PULL_REQUEST_TEMPLATE.md)

::: {.literalinclude language="markdown"}
../../.github/PULL_REQUEST_TEMPLATE.md
:::
:::

## Get connected {#get_connected}

When in doubt, we recommend going together! Get connected with our
community of active contributors, many of whom felt just like you when
they started out and are happy to welcome you and support you as you get
to know how we work, and where things are. You can reach out on any of
our `communication-channels`{.interpreted-text role="ref"}. For
development questions we recommend reaching out on our development
[gitter](https://gitter.im/matplotlib/matplotlib) chat room and for
community questions reach out at [community
gitter](https://gitter.im/matplotlib/community).

## Choose an issue {#managing_issues_prs}

In general, the Matplotlib project does not assign issues. Issues are
\"assigned\" or \"claimed\" by opening a PR; there is no other
assignment mechanism. If you have opened such a PR, please comment on
the issue thread to avoid duplication of work. Please check if there is
an existing PR for the issue you are addressing. If there is, try to
work with the author by submitting reviews of their code or commenting
on the PR rather than opening a new PR; duplicate PRs are subject to
being closed. However, if the existing PR is an outline, unlikely to
work, or stalled, and the original author is unresponsive, feel free to
open a new PR referencing the old one.

## Start a pull request {#how-to-pull-request}

The preferred way to contribute to Matplotlib is to fork the [main
repository](https://github.com/matplotlib/matplotlib/) on GitHub, then
submit a \"pull request\" (PR). To work on a a pull request:

1.  **First** set up a development environment, either by cloning a copy
    of the Matplotlib repository to your own computer or by using Github
    codespaces, by following the instructions in
    `installing_for_devs`{.interpreted-text role="ref"}
2.  **Then** start solving the issue, following the guidance in
    `development workflow <development-workflow>`{.interpreted-text
    role="ref"}
3.  **As part of verifying your changes** check that your contribution
    meets the
    `pull request guidelines <pr-author-guidelines>`{.interpreted-text
    role="ref"} and then
    `open a pull request <open-pull-request>`{.interpreted-text
    role="ref"}.
4.  **Finally** follow up with maintainers on the PR if waiting more
    than a few days for feedback.
    `Update the pull request <update-pull-request>`{.interpreted-text
    role="ref"} as needed.

If you have questions of any sort, reach out on the
`contributor_incubator`{.interpreted-text role="ref"} and join the
`new_contributors_meeting`{.interpreted-text role="ref"}.
