<!-- Source: https://namespace.so/docs/reference/cli/top -->

# nsc top

Observe resource utilization of the target instance.

`top` starts an interactive process viewer allowing you to observe resource utilization of the target instance.

## Usage

```
nsc top <instance-id>
```

### Example

In the example below, we first create an ephemeral instance, and then observe its resource utilization.

Create an ephemeral instance:

```
$ nsc create
  Created new ephemeral environment! ID: hk99v6hn1tk9m
```

Observe resource utilization:

```
nsc top hk99v6hn1tk9m
```

Last updated July 4, 2025
