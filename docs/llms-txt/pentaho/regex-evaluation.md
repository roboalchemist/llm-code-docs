# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/regex-evaluation.md

# Regex Evaluation

The Regex evaluation step matches the strings of an input field against a text pattern you define with a regular expression (regex). This step uses the `java.util.regex` package. The syntax for creating the regular expressions used by this step is defined in the [java.util.regex.Pattern javadoc](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).

You can use this step to parse a complex string of text and create new fields out of the input field with capture groups (defined by parentheses). For example, if you have an input field containing an author's name in quotes and the number of posts made by them, you can create two new fields in your transformation - one for the name, and one for the number of posts as shown below:

Text to parse:

```
"Author, Ann" - 53 posts
```

Regex to create two capture groups:

```
^"([^"]*)" - (\d*) posts$
```

The resulting field values are: Ann and 53.
