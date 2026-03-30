# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/run-modifiers.md

# Source: https://docs.pentaho.com/pdia-data-integration/pipeline-designer/run-modifiers.md

# Run modifiers

* `${VARIABLE}`
* `%%VARIABLE%%`

Both formats can be used and even mixed. In fact, you can create variable recursion by alternating between the Unix and Windows syntax. For example, if you wanted to resolve a variable that depends on another variable, then you could use this example: `${%%inner_var%%}`.

**Note:** If there is a name collision with a parameter or argument, variables will defer.

You can also use ASCII or hexadecimal character codes in place of variables, using the same format: `$[hex value]`. This makes it possible to escape the variable syntax in instances where you need to put variable-like text into a variable. For instance if you wanted to use `${foobar}` in your data stream, then you can escape it like this: `$[24]{foobar}`. Pipeline Designer will replace `$[24]` with a `$` without resolving it as a variable.

### Environment variables

This is the traditional variable type in Pipeline Designer. You define an environment variable through the Set Environment Variables dialog box in the **Edit** menu, or by hand by passing it as an option to the Java Virtual Machine (JVM) with the -D flag.

Environment variables are an easy way to specify the location of temporary files in a platform-independent way; for example, the\*\*${java.io.tmpdir}\*\* variable points to the `/tmp/` directory on Unix/Linux/OS X and to the `C:\Documents and Settings\<username\Local Settings\Temp\` directory on Windows.

The only problem with using environment variables is that they cannot be used dynamically. For example, if you run two or more transformations or jobs at the same time on the same application server, you may get conflicts. Changes to the environment variables are visible to all software running on the virtual machine.

### Kettle Variables

Kettle variables provide a way to store small pieces of information dynamically in a narrower scope than environment variables. A Kettle variable is local to Kettle, and can be scoped down to the job or transformation in which it is set, or up to a related job. The Set Session Variables step in a transformation allows you to specify the related job that you want to limit the scope to (for example, the parent job, grandparent job, or the root job).

Kettle variables configure various Pipeline Designer-specific options such as the location of the shared object file for transformations and jobs or the log size limit.&#x20;

To edit Kettle variables manually, complete these steps.

1. Open the `kettle.properties` file in a text editor. By default, the `kettle.properties` file is typically stored in your home directory or the `.pentaho` directory.
2. Edit the file.
3. When complete, close and save the file.

#### Set the LAZY\_REPOSITORY variable

The LAZY\_REPOSITORY variable restores the directory-loading behavior of the repository to be as it was before Pentaho 6.1.&#x20;

**Note:** Changing this variable to `false` will make repository loading more expensive.

To set the **LAZY\_REPOSITORY** variable, complete these steps.

1. Open the `kettle.properties` file in a text editor. By default, the `kettle.properties` file is typically stored in your home directory or the `.pentaho` directory.
2. Look for **KETTLE\_LAZY\_REPOSITORY** and, if it is set to `false`, change the value to `true`.
3. When complete, close and save the file.

## Arguments

An argument is a named, user-supplied, single-value input given as a command line argument (running a transformation or job manually from Pan or Kitchen, or as part of a script). Each transformation or job can have a maximum of 10 arguments. Each argument is declared as space-separated values given after the rest of the Pan or Kitchen line:

```
sh pan.sh -file:/example_transformations/example.ktr argOne argTwo argThree
```

In the above example, the values **argOne**, **argTwo**, and **argThree** are passed into the transformation, where they will be handled according to the way the transformation is designed. If it was not designed to handle arguments, nothing will happen. Typically, these values would be numbers, words (strings), or variables (system or script variables, not Pipeline Designer variables).

In Pipeline Designer, you can test argument handling by defining a set of arguments when you run a transformation or job. For details, see [Run a transformation](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference) or [Run a job](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference).
