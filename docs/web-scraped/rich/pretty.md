# Source: https://rich.readthedocs.io/en/latest/pretty.html

# Pretty Printing[](#pretty-printing "Link to this heading")

In addition to syntax highlighting, Rich will format (i.e. *pretty print*) containers such as lists, dicts, and sets.

Run the following command to see an example of pretty printed output:

    python -m rich.pretty

Note how the output will change to fit within the terminal width.

## pprint method[](#pprint-method "Link to this heading")

The [[`pprint()`]](reference/pretty.html#rich.pretty.pprint "rich.pretty.pprint") method offers a few more arguments you can use to tweak how objects are pretty printed. Here's how you would import it:

    >>> from rich.pretty import pprint
    >>> pprint(locals())

### Indent guides[](#indent-guides "Link to this heading")

Rich can draw *indent guides* to highlight the indent level of a data structure. These can make it easier to read more deeply nested output. The pprint method enables indent guides by default. You can set [`indent_guides=False`] to disable this feature.

### Expand all[](#expand-all "Link to this heading")

Rich is quite conservative about expanding data structures and will try to fit as much in each line as it can. If you prefer, you can tell Rich to fully expand all data structures by setting [`expand_all=True`]. Here's an example:

    >>> pprint(["eggs", "ham"], expand_all=True)