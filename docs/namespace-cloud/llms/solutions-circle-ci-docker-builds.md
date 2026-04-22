<!-- Source: https://namespace.so/docs/solutions/circle-ci/docker-builds -->

# Optimizing Docker Build Performance in Circle CI

Namespace provides high-performance Remote Builders that can significantly speed up your Docker builds in CircleCI workflows.
The easiest way to use Namespace Remote Builders is through the `namespacelabs/build` orb, which handles all the configuration automatically.

## Access to Namespace

Namespace federates with CircleCI using [OpenID Connect](https://circleci.com/docs/openid-connect-tokens/) to generate short-lived access tokens.

After a one-time setup, your workflows can access Namespace indefinitely, without relying on pre-shared keys which can be more easily compromised:

1. **Find your CircleCI Organization ID** in [Organization Settings > Overview](https://app.circleci.com/settings/organization) in the CircleCI web application.
2. **Email support** at [support@namespace.so](mailto:support@namespace.so) with both your Organization ID and your Namespace workspace ID from the [Dashboard](https://cloud.namespace.so/workspace/settings).

## Using Remote Builders

### Add the orb to your CircleCI configuration

```
orbs:
  build: namespacelabs/build@0.2.1
```

### Configure the Namespace Remote Builder environment

```
steps:
  - checkout
  - build/setup
```

### Use the Remote Builder

When invoking `docker build`, pass `namespace` as `--builder` to `buildx`:

```
docker buildx build --builder namespace .
```

## Complete example

```
version: 2.1
 
orbs:
  build: namespacelabs/build@0.2.1
 
jobs:
  docker-build:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - build/setup
      - run:
          name: Build and push Docker image
          command: |
            docker buildx build --builder namespace .
 
workflows:
  build:
    jobs:
      - docker-build
```

Last updated August 22, 2025
