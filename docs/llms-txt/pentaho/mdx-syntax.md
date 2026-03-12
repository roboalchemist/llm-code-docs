# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/about-multidimensional-expression-language/mdx-syntax.md

# MDX Syntax

If you are already familiar with SQL, then much of the MDX syntax will look familiar, and the rest should be relatively easy to learn. You can edit the MDX using Analyzer or a text editor.

There are six MDX data types:

* Dimension or hierarchy
* Level
* Member
* Tuple
* Scalar
* Set

Below is an example of a very simple MDX query:

```
SELECT
   { [Measures].[Salesfact] } ON COLUMNS,
   { [Date].[2004], [Date].[2005] } ON ROWS
FROM Sales
```

MDX was initially developed by Microsoft for its SQL Server analysis products, though it has since become an independent standard. It's been around long enough now that there are many MDX tutorials and references, most notably:

* <http://msdn.microsoft.com/en-us/library/ms145506.aspx>
* <http://en.wikipedia.org/wiki/Multidimensional_Expressions>

MDX implementations vary, and many MDX documentation resources are specific to certain niche products or standards. Not all MDX functions and extensions are supported in Pentaho Analysis.
