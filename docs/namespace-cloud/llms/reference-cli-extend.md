<!-- Source: https://namespace.so/docs/reference/cli/extend -->

# nsc extend

Extends the duration of an instance.

`extend` prolongs the duration of an existing instance.

## Usage

```
nsc extend [--duration <duration>] [--ensure_minimum <duration>]
```

### Example

```
$ nsc create
 
  Created new ephemeral environment! ID: s6h6i70uk2nqe
 
$ nsc extend s6h6i70uk2nqe --ensure_minimum 8h
New deadline: 2024-08-09T19:29:09.296810204Z
```

## Options

### --duration <duration>

Extend the duration of the target instance by this duration.

### --ensure\_minimum <duration>

Ensure that the target instance has a minimum of the specified duration.

Last updated July 4, 2025
