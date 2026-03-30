# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation/options-regex-evaluation/settings-tab/regular-expression-evaluation-window.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation/options-regex-evaluation/settings-tab/regular-expression-evaluation-window.md

# Regular expression evaluation window

You can test your regular expression against three different input strings using the following **Regular expression evaluation** window:

![Regular expression evaluation window](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-a77b682dc66b5db2a2de086d20c455762cc400e4%2FPDI_RegEx_Eval_Window.png?alt=media)

If your expression contains a group field, type a string in the Compare section and the option below the string will be split according to your group(s).

The window contains the following options:

| Field                                               | Description                                                                                                                                                                            |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Please enter a new regular expression or modify** | Specify your regular expression.                                                                                                                                                       |
| **Values to test**                                  | Specify the values (**Value1**, **Value2**, or **Value3**) to test your string. The background will turn green if that value is a match against your expression or red if it does not. |
| **Capture from value**                              | Displays the value of the captured string.                                                                                                                                             |
| **Captured fields**                                 | Displays the value of the captured groups.                                                                                                                                             |
