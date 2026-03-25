# Source: https://docs.axonius.com/docs/adding-multiple-values-to-query-expression.md

# Adding Multiple Values to Query Expressions

You can add multiple values to a query expression either using the *in (equals)*, *in (contains)*, or *in (plain text)* operators. The *in (equals)*, and *in (plain text)* operators are case sensitive and function like the Equals operator for each value added to the list. The *in (contains)* operator is NOT case sensitive and functions like the Contains operator for each value added to the list.

## In Operator

You can copy a list of multiple values from an external file into the [Query Wizard](/docs/query-wizard-and-query-filter) by using the **In** operator to streamline the process. Multiple values from an existing list can be separated by a comma, semicolon, **Enter**, or **Tab** key. In addition, you can copy the values listed in the Query Wizard to an external file. In operator supports copying of up to 2000 values.

**To copy a list of multiple values to Query Expression**

1. From an external text editor or spreadsheet, highlight the list of values and right-click and select **Copy** from the dropdown. The values are copied to the Clipboard.

2. From the Query, select a query expression, such as **Host Name**.

3. From the dropdown to the right of the query expression, select **in (equals)** or **in (contains)**.

4. From the dropdown to the right of the **in** selection, right-click and select **Paste**. Alternatively, select **Ctrl`+`V** or **Command`+`V** (depending on your OS). The values from the Clipboard are pasted into the Query Expression.
   ![IN\_Equals\_query](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IN_Equals_query.png)

5. Deselect a value from the list by clicking the value. Toggle  ![DownArrow](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DownArrow.png) (**Down Arrow**) to collapse/expand the list. Click **Clear All** to remove all values from the list.

**To copy a list of multiple values to an external file**

1. From the Query, select a query expression, such as **Host Name**.
2. From the dropdown to the right of the query expression, select **in (equals)** or **in (contains)**.
3. If the list is collapsed, click ![DownArrow](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DownArrow.png) (**Down Arrow**) to expand the list.
4. Exclude a value from the list by clicking its value.
5. Copy the values in the list by selecting **Copy Selected Tags**.

<Image alt="CopyTags" width="250px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CopyTags.png" />

6. From your text editor or spreadsheet, select **Ctrl`+`V** or **Command`+`V** (depending on your operating system). The values are pasted  into the external file and separated by commas.

## *in (plain text)*

You can also use *in (plain text)* to add multiple values to a query expression. This is useful if you need to enter more than 2000 values.

* The text value should be a list of values separated by a comma, **Enter** or **Tab** key.
* The comma (,) character can be escaped by using a single backslash (e.g \\,)