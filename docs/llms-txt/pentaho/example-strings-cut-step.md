# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/strings-cut/example-strings-cut-step.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/strings-cut/example-strings-cut-step.md

# Example

Given the string “example”, you can use Strings cut to parse out the first letter “e” by understanding the index of each character in the string, as shown in the following table:

| Character | e | x | a | m | p | l | e |
| --------- | - | - | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 | 5 | 6 |

The \*\*Cut from\*\* position of the first letter “e” is 0. The \*\*Cut to\*\* position is 1.

To parse out “am”, the **Cut from** position represents the start of the substring at 2. The **Cut to** position should include the end of the substring, which is before 4.
