# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/strings-cut.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/strings-cut.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/strings-cut.md

# Strings cut

The Strings cut step returns a snippet of an input string based on a range of character locations. For example, you may need to parse the time “11:00” out of a filename “11:00 am update”. You would use Strings cut to return the substring starting at an index of 0 and ending before the index 5.

**Note:** If you specify locations outside of the character length of the string, Strings cut returns a blank string.
