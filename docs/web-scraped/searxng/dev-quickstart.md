# Source: https://docs.searxng.org/dev/quickstart.html

[]

# Development Quickstart[¶](#development-quickstart "Link to this heading")

further read

-   [[Makefile & ./manage]](makefile.html#makefile)

-   [[Buildhosts]](../admin/buildhosts.html#buildhosts)

SearXNG loves developers; Developers do not need to worry about tool chains, the usual developer tasks can be comfortably executed via [[make]](makefile.html#makefile).

Don't hesitate, just clone SearXNG's sources and start hacking right now ..

    git clone https://github.com/searxng/searxng.git searxng

For the developer environment, [mise en place](https://mise.jdx.dev/getting-started.html) is recommended:

    $ curl https://mise.run | sh

The tools required for a developer environment are provided via [mise.toml](https://github.com/searxng/searxng/blob/master/mise.toml), trust the project:

    $ mise trust

Here is how a minimal workflow looks like:

1.  *start* hacking

2.  *run* your code: [[make run]](makefile.html#make-run)

3.  *format & test* your code: [[make format]](makefile.html#make-format) and [[make test]](makefile.html#make-test)

If you think at some point something fails, go back to *start*. Otherwise, choose a meaningful commit message and we are happy to receive your pull request. To not end in *wild west* we have some directives, please pay attention to our "[[How to contribute]](contribution_guide.html#how-to-contribute)" guideline.

If you want to debug with the *good old Python Debugger* [pdb](https://docs.python.org/3/library/pdb.html#module-pdb): Alternatively to [`make`]` `[`run`] (2.) which starts a [[Granian]](../admin/installation-granian.html#searxng-granian) server you can jump into the developer environment and start a python based HTTP server by:

    $ ./manage dev.env
    ...
    (dev.env)$ SEARXNG_DEBUG=1 python -m searx.webapp

Since this is a pure Python solution, you can set breakpoints in your code with [`pdb.set_trace()`] and the debugger will wait for you in the terminal prompt.

further read

-   [[NVM make nvm.install nvm.status]](makefile.html#make-nvm)

-   [[make themes.\*]](makefile.html#make-themes)

If you implement themes, you will need to setup a [[Node.js environment]](makefile.html#make-node-env). Before you call *make run* (2.), you need to compile the modified styles and JavaScript: [`make`]` `[`node.clean`]` `[`themes.all`]. If [Biome](https://biomejs.dev/) or [Stylelint](https://stylelint.io/) reports issues, try [`make`]` `[`themes.fix`].

Alternatively you can also compile selective the theme you have modified, e.g. the *simple* theme.

    make themes.simple

Tip

To get live builds while modifying CSS & JS use: [`LIVE_THEME=simple`]` `[`make`]` `[`run`]

further read

-   [[make static.build.\*]](makefile.html#make-static-build)

If you finished your *tests* you can start to commit your changes. To separate the modified source code from the build products first run:

    make static.build.restore

This will restore the old build products and only your changes of the code remain in the working tree which can now be added & committed. When all sources are committed, you can commit the build products simply by:

    make static.build.commit

Committing the build products should be the last step, just before you send us your PR. There is also a make target to rewind this last build commit:

    make static.build.drop