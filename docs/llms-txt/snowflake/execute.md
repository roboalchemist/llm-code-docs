# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/streamlit-commands/execute.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/stage-commands/execute.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/snowpark-commands/execute.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/notebook-commands/execute.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/git-commands/execute.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/snowpark/execute.md

# Execute a Snowpark procedure or function

To execute a Snowpark procedure or function, use the `snow snowpark execute OBJECT_TYPE EXECUTION_IDENTIFIER` command, where:

* `OBJECT_TYPE` is one of `function` or `procedure`.
* `EXECUTION_IDENTIFIER` is function or procedure signature, with all arguments provided.

The following example calls a Snowpark function called `hello_function`:

```snowcli
snow snowpark execute function "hello_function('Olaf')"
```

```output
+--------------------------------------+
| key                    | value       |
|------------------------+-------------|
| HELLO_FUNCTION('Olaf') | Hello Olaf! |
+--------------------------------------+
```
