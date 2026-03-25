# Source: https://www.apollographql.com/docs/rover/commands/contracts.md

# Rover contract Commands

GraphOS [contracts](https://www.apollographql.com/docs/graphos/delivery/contracts/) enable you to create variants of a supergraph that filter out schema elements according to inclusion and exclusion rules:

```mermaid
graph LR;
  subgraph "Source variant";
  api("Supergraph<br/>schema<br/>▉");
  end
  subgraph "Contract variant B"
  contractB("Contract schema B<br/>▟")
  end
  subgraph "Contract variant A"
  contractA("Contract schema A<br/>▛");
  end
  api -."Filter schema<br/>according to contract A".->contractA
  api -."Filter schema<br/>according to contract B".->contractB
```

The `rover contract` command set enables you to interact with your existing contracts and create new ones.

## Publishing a contract to GraphOS

### `contract publish`

This command requires [authenticating Rover with GraphOS](https://www.apollographql.com/docs/rover/configuring/#authenticating-with-graphos).

You can use Rover to publish a new contract or publish configuration changes to an existing contract.

Run the `contract publish` command, like so:

```bash
rover contract publish my-graph@my-contract-variant \
  --source-variant my-source-variant \
  --include-tag foo \
  --include-tag bar \
  --exclude-tag baz \
  --hide-unreachable-types
```

The argument `my-graph@my-contract-variant` in the example above is a [graph ref](https://www.apollographql.com/docs/rover/conventions/#graph-refs) that specifies the ID of the graph you're publishing to, along with which contract variant you're creating or modifying.

If this contract variant already exists in the graph registry, its configuration is updated. Otherwise, a new contract variant is created.

Options include:

Name
Description

###### `--source-variant`

The name of the [source variant](https://www.apollographql.com/docs/graphos/delivery/contracts/#2-fed1-enable-variant-support-for-tag) to use for supergraph schema filtering.

The source variant must belong to the same graph as the contract variant. It must also be a federated variant with subgraphs. If your graph uses Federation 1, you must enable its support for the `@tag` directive in GraphOS Studio.

**Required** the first time you publish a contract.

**Optional** after your first publish. If provided, it must match the value provided for the first publish (the source variant for a particular contract variant can't change).

###### `--include-tag`

A tag name to [include](https://www.apollographql.com/docs/graphos/delivery/contracts/#contract-filters) when filtering. To include multiple tag names, specify `--include-tag` multiple times:

```bash
--include-tag foo --include-tag bar
```

To specify an empty include list, provide`--no-include-tags` instead of this option.

Every tag name **must**:

* Begin with a letter (capital or lowercase) or underscore.
* Include only letters, numbers, underscores (`_`), hyphens (`-`), or slashes (`/`).
* Have a maximum of 128 characters.

One of `--include-tag` or `--no-include-tags` is **required**.

###### `--no-include-tags`

Specifies an empty [include list](https://www.apollographql.com/docs/graphos/delivery/contracts/#contract-filters) for the published contract.

One of `--include-tag` or `--no-include-tags` is **required**.

###### `--exclude-tag`

A tag name to [exclude](https://www.apollographql.com/docs/graphos/delivery/contracts/#contract-filters) when filtering. To exclude multiple tag names, specify `--exclude-tag` multiple times:

```text
--exclude-tag foo --exclude-tag bar
```

To specify an empty exclude list, provide`--no-exclude-tags` instead of this option.

Every tag name **must**:

* Begin with a letter (capital or lowercase) or underscore.
* Include only letters, numbers, underscores (`_`), hyphens (`-`), or slashes (`/`).
* Have a maximum of 128 characters.

One of `--exclude-tag` or `--no-exclude-tags` is **required**.

###### `--no-exclude-tags`

Specifies an empty [exclude list](https://www.apollographql.com/docs/graphos/delivery/contracts/#contract-filters) for the published contract.

One of `--exclude-tag` or `--no-exclude-tags` is **required**.

###### `--hide-unreachable-types`

If provided, the contract automatically [hides](https://www.apollographql.com/docs/graphos/delivery/contracts/#contract-filters) types that are unreachable from the contract schema's root fields.

One of `--hide-unreachable-types` or `--no-hide-unreachable-types` is **required**.

###### `--no-hide-unreachable-types`

If provided, the contract doesn't automatically hide types that are unreachable from the contract schema's root fields.

One of `--hide-unreachable-types` or `--no-hide-unreachable-types` is **required**.

###### `--no-launch`

**Optional.** If provided, this command does not trigger a [launch](https://www.apollographql.com/docs/graphos/delivery/contracts/#review-and-launch) in GraphOS after updating the contract configuration.

## Fetching contract details

### `contract describe`

This command requires [authenticating Rover with GraphOS](https://www.apollographql.com/docs/rover/configuring/#authenticating-with-graphos).

You can use Rover to fetch the configuration of any contract variant that Rover has access to.

Run the `contract describe` command, like so:

```bash
rover contract describe my-graph@my-contract-variant
```

The argument `my-graph@my-contract-variant` in the example above is a [graph ref](https://www.apollographql.com/docs/rover/conventions/#graph-refs) that specifies the ID of the GraphOS graph you're fetching from, along with which contract variant you're fetching.

This command prints a summary of the contract's configuration, including its source variant and include/exclude lists:

```text
Fetching description for configuration of my-graph@my-contract-variant using credentials from the default profile.

Configuration Description:

Contract variant "my-graph@my-contract-variant" is derived from the source variant "my-graph@my-source-variant".

Included tags:

- "foo"
- "bar"

Excluded tags:

- "baz"

Unreachable types are automatically hidden.

View the variant's full configuration at https://studio.apollographql.com/graph/my-graph/settings/variant?variant=my-contract-variant
```
