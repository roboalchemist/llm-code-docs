# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/apply-advanced-conditional-formatting-with-mdx-expressions.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/apply-advanced-conditional-formatting-with-mdx-expressions.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/apply-advanced-conditional-formatting-with-mdx-expressions.md

# Apply advanced conditional formatting with MDX expressions

If the premade conditional formatting options in Analyzer are not precise enough for your needs, you can apply custom formatting to a measure by using an MDX expression.

1. Right-click a measure in the grid, then select **Column Name and Format** from the context menu.

   The Edit Column dialog box appears.
2. Select **Expression** from the **Format** drop-down list.

   A default MDX expression that prints green or red arrows in cells if their values are greater than or less than zero, respectively, appears in the **MDX Format Expression** field.

   ```
   Case
   When [Measures].CurrentMember > 0
   Then '|#,##0|arrow=up'
   When [Measures].CurrentMember < 0
   Then '|#,##0|arrow=down'
   Else '|#,##0'
   End
   ```
3. Modify the expression to suit your needs. Consult [Conditional Formatting Expressions](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/applying-conditional-formatting-to-measures-pentaho-analyzer/conditional-formatting-expressions) for more information on conditional formatting syntax and options.

   **Note:** If the MDX expression is invalid, an invalid report definition error appears at the top of the dialog box.
4. Click **OK** to commit the change.

The Analyzer report will refresh and apply the formatting choices you specified.
