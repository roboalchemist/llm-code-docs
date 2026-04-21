<!-- Source: https://namespace.so/docs/reference/github-actions/setup-turbocache -->

# namespace-actions/setup-turbocache

namespace-actions/setup-turbocache@v0

[setup-turbocache](https://github.com/namespace-actions/setup-turbocache) is a GitHub action that configures your workflows to use Namespace's high-performance
[turborepo](https://turbo.build) caching.

## Example

```
jobs:
  build:
    runs-on: namespace-profile-default
 
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      - name: Set up caching
        uses: namespace-actions/setup-turbocache@v0
      - name: Go turbo
        run: turbo build
```

## Options

### team

By default, caching is performed to a single shared storage `main`. But you can isolate your caches by specifying a separate team (in turbo parlance).

Last updated September 1, 2025
