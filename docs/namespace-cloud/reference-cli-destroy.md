<!-- Source: https://namespace.so/docs/reference/cli/destroy -->

# nsc destroy

Destroy an instance.

`destroy` destroys a Namespace instance by its instance id.

## Usage

```
nsc destroy <instance-id> [--force]
```

### Example

The following example creates a new instance with the
default machine shape (4 CPUs and 8 GiB of memory).

```
$ nsc create
  Created instance "h9am86n6gi25m"
    deadline: 2023-04-25T08:48:38Z
```

Now, let's destroy the instance.

```
$ nsc destroy h9am86n6gi25m --force
```

## Options

### --force

Skip the confirmation when destroying the instance.

Last updated July 4, 2025
