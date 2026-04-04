# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/discover-metadata-from-a-text-file/options-discover-metadata-from-a-text-file-step/delimiter-and-data-type-detection-rules.md

# Delimiter and data type detection rules

Because there are many different variations of delimited files, this step may not be able to detect the structure of every type of delimited file. The following rules are used to evaluate fields:

* The step uses a left outer cartesian join of the delimiter, enclosure, and escape candidate options.
  * The step performs inner joins when the **Enclosure character required** or **Escape is required** options are enabled. This means that a null enclosure or a null escape is not allowed.
  * The delimiter character cannot be the same as the enclosure or escape characters. For example, using double quotes (“) for both your enclosure and escape characters. The step will not fail when this happens, but it will ignore that candidate combination.
* If the enclosure character and escape characters are the same, the delimiter can not be escaped. Only the enclosure character can be escaped.
* If any enclosure errors are found such as an unclosed enclosure or an unescaped enclosure character, the enclosure will not be considered valid. If the enclosure errors are valid, select the **Ignore Enclosure errors** option.
* A header row is defined as any row within the **Maximum number of header** rows value with a number of fields consistent with the number of fields in the data. The row after the last inconsistent row may also be considered a header row if the:
  * Header row strategy is first strings and the first row that only contains string values is the next row after the last inconsistent row.
  * Header row strategy is first any data type and there are no rows with a consistent number of fields prior to the last inconsistent row.
  * Header row strategy is last strings and the next row after the last inconsistent row is all strings.
  * Header row strategy is last any data type.
* A footer row is defined as the first row with an inconsistent number of fields and any following rows. When the **Limit scanned rows** option prevents the entire file from being read, the file is not evaluated for footer rows.
* If multiple delimiters, enclosures, or escape characters appear to match the file, the step is unable to determine the format.
* Multiple character enclosures or escapes may result in incorrect data type results.
* Ignoring enclosure errors may result in incorrect data type results.
* The field length is determined by the length of the longest field detected during the scan. Note that if the **Limit scanned rows** option is set, then only that many rows of data will be checked.
