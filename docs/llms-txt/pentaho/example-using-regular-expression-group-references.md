# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/replace-in-string/example-using-regular-expression-group-references.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/replace-in-string/example-using-regular-expression-group-references.md

# Example: Using regular expression group references

When using regex (regular expression) group references, matching patterns are represented by a sequence of integer values with a dollar sign prefix. For example: **$1** for the first group match, **$2** for the second group match, and so forth.

To replace a portion of the incoming value contained in the **In stream field** column, use one of the group value tokens to represent the portion of the string that group matched.

As an example, suppose the string value of **In stream field** is: `Homer Simpson`

To switch the first and last name, you would set up the table fields as follows:

1. Set the **use RegEx** column to: **Y**
2. The value of the **Search** column would look similar to: `/([a-zA-Z]*) ([a-zA-Z]*)/`

   Each pattern inside the parenthesis represents a grouping, so that now **$1** = `Homer` and **$2** = `Simpson`

   ![Regular expression group example](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-4f4a09b8aefca7d7774c810b588ccdcee087e65b%2FPDI_TransStep_Table_Replace-In-String_Example.png?alt=media)
3. To switch the first and last name, set the value of the **Replace with** field as: `$2 $1`

   This places the string `Simpson` first, followed by `Homer` second.

   For more information about regular expressions, see <https://www.regular-expressions.info/brackets.html>
