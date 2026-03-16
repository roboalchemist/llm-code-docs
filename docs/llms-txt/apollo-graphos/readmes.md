# Source: https://www.apollographql.com/docs/rover/commands/readmes.md

# Rover README Commands

These Rover commands enable you to publish and fetch the [README](https://www.apollographql.com/docs/graphos/graphs/studio-features/#the-readme-page) associated with a particular graph variant.

READMEs are [Markdown-based](https://www.apollographql.com/docs/graphos/graphs/studio-features/#supported-markdown) and support Apollo-specific shortcodes, which are documented [here](https://www.apollographql.com/docs/graphos/graphs/studio-features/#readme-shortcodes).

## Fetching a README from GraphOS

### `readme fetch`

This command requires [authenticating Rover with GraphOS](https://www.apollographql.com/docs/rover/configuring/#authenticating-with-graphos).

You can use Rover to fetch the README of any Studio graph variant you have access to.

Run the `readme fetch` command, like so:

```bash
rover readme fetch my-graph@my-variant
```

The argument `my-graph@my-variant` is the `graph ref`, which you can read about [here](https://www.apollographql.com/docs/rover/conventions#graph-refs).

### Output format

By default, the README is output to `stdout`. You can also save the output to a `.md` file like so:

```bash
# Creates README.md or overwrites if it already exists
rover readme fetch my-graph@my-variant --output README.md
```

You can also request the output as JSON with the `--format json` option:

```bash
rover readme fetch my-graph@my-variant --format json
```

For more on passing values via `stdout`, see [Conventions](https://www.apollographql.com/docs/rover/conventions#using-stdout).

## Publishing a README to GraphOS

### `readme publish`

This command requires [authenticating Rover with GraphOS](https://www.apollographql.com/docs/rover/configuring/#authenticating-with-graphos).

You can use Rover to publish a README to one of your [GraphOS graphs](https://www.apollographql.com/docs/graphos/graphs/).

Use the `readme publish` command, like so:

```bash
rover readme publish my-graph@my-variant --file ./README.md
```

The argument `my-graph@my-variant` is the `graph ref`, which you can read about [here](https://www.apollographql.com/docs/rover/conventions#graph-refs).

You can also pipe in the README's contents via `stdin` by providing `-` as the value of the `--file` option, like so:

```bash
echo "sample readme contents" | rover readme publish my-graph@my-variant --file -
```

For more on accepting input via `stdin`, see [Conventions](https://www.apollographql.com/docs/rover/conventions#using-stdin).
