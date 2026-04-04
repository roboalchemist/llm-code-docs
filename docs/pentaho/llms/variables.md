# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/advanced-topics-pdi-perspective/pdi-run-modifiers/variables.md

# Variables

A variable in PDI is a piece of user-supplied information that you can use dynamically and programmatically in a variety of different scopes. A variable can be local to a single step, or be available to the entire JVM (Java Virtual Machine) that PDI is running in.

PDI variables can be used in both [Basic concepts of PDI](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/data-integration-perspective-in-the-pdi-client/basic-concepts-of-pdi) transformation steps and job entries. You define variables with the Set Variable step and Set Session Variables step in a transformation, by hand through the `kettle.properties` file, or through the Set Environment Variables dialog box in the **Edit** menu.

The Get Variable and Get Session Variables steps can explicitly retrieve a value from a variable, or you can use it in any PDI text field which has the dollar sign ![Diamond Dollar Sign](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-3bc34f6128e010b9f917f5d4121fd029ae68d1ef%2Fvariable.png?alt=media) icon next to it by using a metadata string in either the Unix or Windows formats:

* `${VARIABLE}`
* `%%VARIABLE%%`

Both formats can be used and even mixed. In fact, you can create variable recursion by alternating between the Unix and Windows syntax. For example, if you wanted to resolve a variable that depends on another variable, then you could use this example: `${%%inner_var%%}`.

**Note:** If there is a name collision with a parameter or argument, variables will defer.

You can also use ASCII or hexadecimal character codes in place of variables, using the same format: `$[hex value]`. This makes it possible to escape the variable syntax in instances where you need to put variable-like text into a variable. For instance if you wanted to use `${foobar}` in your data stream, then you can escape it like this: `$[24]{foobar}`. PDI will replace `$[24]` with a `$` without resolving it as a variable.
