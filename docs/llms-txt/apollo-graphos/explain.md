# Source: https://www.apollographql.com/docs/rover/commands/explain.md

# The Rover explain Command

Usually when a Rover command results in an error, the command's output includes an error code:

```sh
rover supergraph compose --config supergraph.yaml

Composing supergraph with Federation v2.0.5.
error[E029]: Encountered 1 build error while trying to build a supergraph.
```

The command above resulted in an error with code `E029`.

You can use the `rover explain` command to output the description for a particular error code:

```text
rover explain E029
```

Descriptions for all Rover error codes are also available in [this article](https://www.apollographql.com/docs/rover/errors/).
