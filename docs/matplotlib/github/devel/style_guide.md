# Documentation style guide

This guide contains best practices for the language and formatting of
Matplotlib documentation.

::: seealso
For more information about contributing, see the
`documenting-matplotlib`{.interpreted-text role="ref"} section.
:::

## Expository language

For explanatory writing, the following guidelines are for clear and
concise language use.

### Terminology

There are several key terms in Matplotlib that are standards for
reliability and consistency in documentation. They are not
interchangeable.

+--------------+--------------+------------------------------------+------------------------------------+
| Term         | Description  | Correct                            | Incorrect                          |
+==============+==============+====================================+====================================+
| `~matplot    | Matplotlib   | -   *For Matplotlib objects*:      | -   \"The figure is the working    |
| lib.figure.F | working      |     Figure, \"The Figure is the    |     space for visuals.\"           |
| igure`{.inte | space for    |     working space for the visual.  | -   \"Methods in the figure        |
| rpreted-text | programming. | -   *Referring to class*:          |     provide the visuals.\"         |
| r            |              |     `~matplotli                    | -   \"The                          |
| ole="class"} |              | b.figure.Figure`{.interpreted-text |     `~matplotli                    |
|              |              |     role="class"}, \"Methods       | b.figure.Figure`{.interpreted-text |
|              |              |     within the                     |     role="class"} Four leglock is  |
|              |              |     `~matplotli                    |     a wrestling move.\"            |
|              |              | b.figure.Figure`{.interpreted-text |                                    |
|              |              |     role="class"} provide the      |                                    |
|              |              |     visuals.\"                     |                                    |
|              |              | -   *General language*: figure,    |                                    |
|              |              |     \"Michelle Kwan is a famous    |                                    |
|              |              |     figure skater.\"               |                                    |
+--------------+--------------+------------------------------------+------------------------------------+
| `~mat        | Subplots     | -   *For Matplotlib objects*:      | -   \"The axes methods transform   |
| plotlib.axes | within       |     Axes, \"An Axes is a subplot   |     the data.\"                    |
| .Axes`{.inte | Figure.      |     within the Figure.\"           | -   \"Each                         |
| rpreted-text | Contains     | -   *Referring to class*:          |     `~matpl                        |
| r            | plot         |     `~matpl                        | otlib.axes.Axes`{.interpreted-text |
| ole="class"} | elements and | otlib.axes.Axes`{.interpreted-text |     role="class"} is specific to a |
|              | is           |     role="class"}, \"Each          |     Figure.\"                      |
|              | responsible  |     `~matpl                        | -   \"The musicians on stage call  |
|              | for plotting | otlib.axes.Axes`{.interpreted-text |     their guitars Axes.\"          |
|              | and          |     role="class"} is specific to   | -   \"The point where the Axes     |
|              | configuring  |     one Figure.\"                  |     meet is the origin of the      |
|              | additional   | -   *General language*: axes,      |     coordinate system.\"           |
|              | details.     |     \"Both loggers and lumberjacks |                                    |
|              |              |     use axes to chop wood.\" OR    |                                    |
|              |              |     \"There are no standard names  |                                    |
|              |              |     for the coordinates in the     |                                    |
|              |              |     three axes.\" (Plural of axis) |                                    |
+--------------+--------------+------------------------------------+------------------------------------+
| `~matplot    | Broad        | -   *For Matplotlib objects*:      | -   \"Configure the legend artist  |
| lib.artist.A | variety of   |     Artist, \"Artists display      |     with its respective method.\"  |
| rtist`{.inte | Matplotlib   |     visuals and are the visible    | -   \"There is an                  |
| rpreted-text | objects that |     elements when rendering a      |     `~matplotli                    |
| r            | display      |     Figure.\"                      | b.artist.Artist`{.interpreted-text |
| ole="class"} | visuals.     | -   *Referring to class*:          |     role="class"} for that visual  |
|              |              |     `~matplotli                    |     in the graph.\"                |
|              |              | b.artist.Artist`{.interpreted-text | -   \"Some Artists became famous   |
|              |              |     role="class"} , \"Each         |     only by accident.\"            |
|              |              |     `~matplotli                    |                                    |
|              |              | b.artist.Artist`{.interpreted-text |                                    |
|              |              |     role="class"} has respective   |                                    |
|              |              |     methods and functions.\"       |                                    |
|              |              | -   *General language*: artist,    |                                    |
|              |              |     \"The artist in the museum is  |                                    |
|              |              |     from France.\"                 |                                    |
+--------------+--------------+------------------------------------+------------------------------------+
| `~mat        | Hu           | -   *For Matplotlib objects*:      | -   \"Plot the graph onto the      |
| plotlib.axis | man-readable |     Axis, \"The Axis for the bar   |     axis.\"                        |
| .Axis`{.inte | single       |     chart is a separate Artist.\"  | -   \"Each Axis is usually named   |
| rpreted-text | dimensional  |     (plural, Axis objects)         |     after the coordinate which is  |
| r            | object of    | -   *Referring to class*:          |     measured along it.\"           |
| ole="class"} | reference    |     `~matpl                        | -   \"In some computer graphics    |
|              | marks        | otlib.axis.Axis`{.interpreted-text |     contexts, the ordinate         |
|              | containing   |     role="class"}, \"The           |     `~matpl                        |
|              | ticks, tick  |     `~matpl                        | otlib.axis.Axis`{.interpreted-text |
|              | labels,      | otlib.axis.Axis`{.interpreted-text |     role="class"} may be oriented  |
|              | spines, and  |     role="class"} contains         |     downwards.\"                   |
|              | edges.       |     respective XAxis and YAxis     |                                    |
|              |              |     objects.\"                     |                                    |
|              |              | -   *General language*: axis,      |                                    |
|              |              |     \"Rotation around a fixed axis |                                    |
|              |              |     is a special case of           |                                    |
|              |              |     rotational motion.\"           |                                    |
+--------------+--------------+------------------------------------+------------------------------------+
| Axes         | Usage        | -   Axes interface                 | -   explicit interface             |
| interface    | pattern in   | -   call methods on the Axes /     | -   object oriented                |
|              | which one    |     Figure object                  | -   OO-style                       |
|              | calls        |                                    | -   OOP                            |
|              | methods on   |                                    |                                    |
|              | Axes and     |                                    |                                    |
|              | Figure (and  |                                    |                                    |
|              | sometimes    |                                    |                                    |
|              | other        |                                    |                                    |
|              | Artist)      |                                    |                                    |
|              | objects to   |                                    |                                    |
|              | configure    |                                    |                                    |
|              | the plot.    |                                    |                                    |
+--------------+--------------+------------------------------------+------------------------------------+
| pyplot       | Usage        | -   `pyplot` interface             | -   implicit interface             |
| interface    | pattern in   | -   call `pyplot` functions        | -   MATLAB like                    |
|              | which one    |                                    | -   Pyplot                         |
|              | only calls   |                                    |                                    |
|              | [.pyplot]    |                                    |                                    |
|              | {.title-ref} |                                    |                                    |
|              | functions to |                                    |                                    |
|              | configure    |                                    |                                    |
|              | the plot.    |                                    |                                    |
+--------------+--------------+------------------------------------+------------------------------------+

### Grammar

#### Subject

Use second-person imperative sentences for directed instructions
specifying an action. Second-person pronouns are for individual-specific
contexts and possessive reference.

  -----------------------------------------------------------------------------------------------------
  Correct                                            Incorrect
  -------------------------------------------------- --------------------------------------------------
  Install Matplotlib from the source directory using You can install Matplotlib from the source
  the Python `pip` installer program. Depending on   directory. You can find additional support if you
  your operating system, you may need additional     are having trouble with your installation.
  support.                                           

  -----------------------------------------------------------------------------------------------------

#### Tense

Use present simple tense for explanations. Avoid future tense and other
modal or auxiliary verbs when possible.

  -----------------------------------------------------------------------------------------------------
  Correct                                            Incorrect
  -------------------------------------------------- --------------------------------------------------
  The fundamental ideas behind Matplotlib for        Matplotlib will take data and transform it through
  visualization involve taking data and transforming functions and methods. They can generate many
  it through functions and methods.                  kinds of visuals. These will be the fundamentals
                                                     for using Matplotlib.

  -----------------------------------------------------------------------------------------------------

#### Voice

Write in active sentences. Passive voice is best for situations or
conditions related to warning prompts.

  -----------------------------------------------------------------------------------------------------
  Correct                                            Incorrect
  -------------------------------------------------- --------------------------------------------------
  The function `plot` generates the graph.           The graph is generated by the `plot` function.

  An error message is returned by the function if    You will see an error message from the function if
  there are no arguments.                            there are no arguments.
  -----------------------------------------------------------------------------------------------------

#### Sentence structure

Write with short sentences using Subject-Verb-Object order regularly.
Limit coordinating conjunctions in sentences. Avoid pronoun references
and subordinating conjunctive phrases.

  -----------------------------------------------------------------------------------------------------
  Correct                                            Incorrect
  -------------------------------------------------- --------------------------------------------------
  The `pyplot` module in Matplotlib is a collection  The `pyplot` module in Matplotlib is a collection
  of functions. These functions create, manage, and  of functions which create, manage, and manipulate
  manipulate the current Figure and plotting area.   the current Figure and plotting area.

  The `plot` function plots data to the respective   The `plot` function plots data within its
  Axes. The Axes corresponds to the respective       respective Axes for its respective Figure.
  Figure.                                            

  The implicit approach is a convenient shortcut for Users that wish to have convenient shortcuts for
  generating simple plots.                           generating plots use the implicit approach.
  -----------------------------------------------------------------------------------------------------

## Formatting

The following guidelines specify how to incorporate code and use
appropriate formatting for Matplotlib documentation.

### Code

Matplotlib is a Python library and follows the same standards for
documentation.

#### Comments

Examples of Python code have comments before or on the same line.

+--------------------------------------------------+--------------------------------------------------+
| Correct                                          | Incorrect                                        |
+==================================================+==================================================+
|     # Data                                       |     years = [2006, 2007, 2008]                   |
|     years = [2006, 2007, 2008]                   |     # Data                                       |
+--------------------------------------------------+--------------------------------------------------+
|     years = [2006, 2007, 2008]  # Data           |                                                  |
+--------------------------------------------------+--------------------------------------------------+

#### Outputs

When generating visuals with Matplotlib using `.py` files in examples,
display the visual with [matplotlib.pyplot.show]{.title-ref} to display
the visual. Keep the documentation clear of Python output lines.

+--------------------------------------------------+--------------------------------------------------+
| Correct                                          | Incorrect                                        |
+==================================================+==================================================+
|     plt.plot([1, 2, 3], [1, 2, 3])               |     plt.plot([1, 2, 3], [1, 2, 3])               |
|     plt.show()                                   |                                                  |
+--------------------------------------------------+--------------------------------------------------+
|     fig, ax = plt.subplots()                     |     fig, ax = plt.subplots()                     |
|     ax.plot([1, 2, 3], [1, 2, 3])                |     ax.plot([1, 2, 3], [1, 2, 3])                |
|     fig.show()                                   |                                                  |
+--------------------------------------------------+--------------------------------------------------+

### reStructuredText

Matplotlib uses reStructuredText Markup for documentation. Sphinx helps
to transform these documents into appropriate formats for accessibility
and visibility.

-   [reStructuredText
    Specifications](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html)
-   [Quick Reference
    Document](https://docutils.sourceforge.io/docs/user/rst/quickref.html)

#### Lists

Bulleted lists are for items that do not require sequencing. Numbered
lists are exclusively for performing actions in a determined order.

+--------------------------------------------------+--------------------------------------------------+
| Correct                                          | Incorrect                                        |
+==================================================+==================================================+
| The example uses three graphs.                   | The example uses three graphs.                   |
+--------------------------------------------------+--------------------------------------------------+
| -   Bar                                          | 1.  Bar                                          |
| -   Line                                         | 2.  Line                                         |
| -   Pie                                          | 3.  Pie                                          |
+--------------------------------------------------+--------------------------------------------------+
| These four steps help to get started using       | The following steps are important to get started |
| Matplotlib.                                      | using Matplotlib.                                |
+--------------------------------------------------+--------------------------------------------------+
| > 1.  Import the Matplotlib library.             | > -   Import the Matplotlib library.             |
| > 2.  Import the necessary modules.              | > -   Import the necessary modules.              |
| > 3.  Set and assign data to work on.            | > -   Set and assign data to work on.            |
| > 4.  Transform data with methods and functions. | > -   Transform data with methods and functions. |
+--------------------------------------------------+--------------------------------------------------+

#### Tables

Use ASCII tables with reStructuredText standards in organizing content.
Markdown tables and the csv-table directive are not accepted.

+--------------------------------------------------+--------------------------------------------------+
| Correct                                          | Incorrect                                        |
+==================================================+==================================================+
|   ---------------------                          |     | Correct | Incorrect |                      |
|   Correct   Incorrect                            |     | ------- | --------- |                      |
|   --------- -----------                          |     | OK      | Not OK    |                      |
|   OK        Not OK                               |                                                  |
|                                                  |                                                  |
|   ---------------------                          |                                                  |
+--------------------------------------------------+--------------------------------------------------+
|     +----------+----------+                      |     .. csv-table::                               |
|     | Correct  | Incorrect|                      |        :header: "correct", "incorrect"           |
|     +==========+==========+                      |        :widths: 10, 10                           |
|     | OK       | Not OK   |                      |                                                  |
|     +----------+----------+                      |        "OK   ", "Not OK"                         |
+--------------------------------------------------+--------------------------------------------------+
|     ===========  ===========                     |                                                  |
|       Correct     Incorrect                      |                                                  |
|     ===========  ===========                     |                                                  |
|     OK           Not OK                          |                                                  |
|     ===========  ===========                     |                                                  |
+--------------------------------------------------+--------------------------------------------------+

## Additional resources

This style guide is not a comprehensive standard. For a more thorough
reference of how to contribute to documentation, see the links below.
These resources contain common best practices for writing documentation.

-   [Python Developer\'s
    Guide](https://devguide.python.org/documenting/#documenting-python)
-   [Google Developer Style Guide](https://developers.google.com/style)
-   [IBM Style
    Guide](https://www.oreilly.com/library/view/the-ibm-style/9780132118989/)
-   [Red Hat Style Guide](https://stylepedia.net/style/#grammar)
