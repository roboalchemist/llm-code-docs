# nsc extend

Prolong the duration of an existing instance.

## Basic Usage

```bash
nsc extend [--duration <duration>] [--ensure_minimum <duration>]
```

## Description

This command extends how long a running instance will remain active before being automatically terminated.

## Options

**--duration <duration>**: Adds a specified amount of time to the instance's remaining lifespan.

**--ensure_minimum <duration>**: Sets a minimum threshold for the instance's total duration. If the instance doesn't already have at least this much time remaining, it extends to meet that minimum.

## Example Usage

```bash
nsc create
nsc extend h9am86n6gi25m --duration 2h

nsc extend h9am86n6gi25m --ensure_minimum 8h
```

Duration format examples: 10m, 1h, 2h30m, 8h

## Related Commands

- `nsc create` - Creates a new instance
- `nsc destroy` - Removes an instance
- `nsc list` - Lists instances
