# Source: https://kreya.app/docs/cli/integrations/github.md

# GitHub Actions

The Kreya CLI can be used in GitHub Actions to automatically test APIs with the kreyac docker image.

```
on: [push]

env:
  KREYA_ENV_MySecret: ${{ secrets.MY_SECRET }} # gets merged into the active Kreya environment as MySecret

jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: riok/kreyac:1
    steps:
      - uses: actions/checkout@v3
      - run: kreyac info
      - run: kreyac environment set-active Production
      - run: kreyac operation invoke "REST/Get books.krop" # invoke a single REST operation by name
      - run: kreyac operation invoke "gRPC/Say hello.krop" # invoke a single gRPC operation by name
      - run: kreyac operation invoke "WebSocket/Echo.krop" # invoke a single WebSocket operation by name
```
