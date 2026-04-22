<!-- Source: https://namespace.so/docs/federation/circleci -->

# Identity Federation with CircleCI

Namespace maintains a direct integration with CircleCI, allowing any of your CircleCI workflows to interact with Namespace resources.
Whether you run builds, create previews, or access your workspace, you can seamlessly connect your CircleCI jobs to Namespace.

## From CircleCI

Namespace federates with CircleCI using [OpenID Connect](https://circleci.com/docs/openid-connect-tokens/) to generate short-lived access tokens.

After a one-time setup, your workflows can access Namespace indefinitely, without relying on pre-shared keys which can be more easily compromised.

### Associate your CircleCI organization with Namespace

1. **Find your CircleCI Organization ID** in [Organization Settings > Overview](https://app.circleci.com/settings/organization) in the CircleCI web application.
2. **Email support** at [support@namespace.so](mailto:support@namespace.so) with both your Organization ID and your Namespace workspace ID from the [Dashboard](https://cloud.namespace.so/workspace/settings).

### Initialize access to Namespace

After the association is complete, simply add the setup step to your CircleCI job.
Subsequent steps can now access Namespace resources.

The Namespace team will release a Circle CI Orb in the future to simplify these steps.

```
version: 2.1
 
jobs:
  test:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: Configure access to Namespace
          command: |
            curl -H 'CI: true' -fsSL https://get.namespace.so/cloud/install.sh | sh
 
            nsc auth exchange-circleci-token
      - run:
          name: Use Namespace
          command: |
            nsc cache bazel setup --bazelrc /etc/bazel.bazelrc
 
workflows:
  main:
    jobs:
      - test
```

## Using Remote Builders

Namespace provides high-performance Remote Builders that can significantly speed up your Docker builds in CircleCI workflows.
The easiest way to use Namespace Remote Builders is through the

`namespacelabs/build`
orb, which handles all the configuration automatically.

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
$

```
docker buildx build --builder namespace .
```
```

### Complete example

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

Last updated March 5, 2026
