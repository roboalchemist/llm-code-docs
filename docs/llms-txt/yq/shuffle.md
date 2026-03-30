# Source: https://mikefarah.gitbook.io/yq/operators/shuffle.md

# Shuffle

Shuffles an array. Note that this command does *not* use a cryptographically secure random number generator to randomise the array order.

## Shuffle array

Given a sample.yml file of:

```yaml
- 1
- 2
- 3
- 4
- 5
```

then

```bash
yq 'shuffle' sample.yml
```

will output

```yaml
- 5
- 2
- 4
- 1
- 3
```

## Shuffle array in place

Given a sample.yml file of:

```yaml
cool:
  - 1
  - 2
  - 3
  - 4
  - 5
```

then

```bash
yq '.cool |= shuffle' sample.yml
```

will output

```yaml
cool:
  - 5
  - 2
  - 4
  - 1
  - 3
```
