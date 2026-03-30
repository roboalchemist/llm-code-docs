# Source: https://docs.earthly.dev/ci-integration/vendor-specific-guides/bitbucket-pipelines-integration.md

# Source: https://docs.earthly.dev/earthly-0.7/ci-integration/vendor-specific-guides/bitbucket-pipelines-integration.md

# Bitbucket Pipelines

Bitbucket Pipelines run in a shared Docker environment and do not support running Earthly builds directly due to [restrictions](https://jira.atlassian.com/browse/BCLOUD-21419) that Bitbucket has put in place.

You can however, run Earthly builds on Bitbucket pipelines via [remote runners](https://docs.earthly.dev/earthly-0.7/docs/remote-runners) such as [Earthly Satellites](https://docs.earthly.dev/earthly-0.7/earthly-cloud/satellites). Because Bitbucket Pipelines run as containers you can also use the official Earthly Docker image. Here is an example of a Bitbucket Pipeline build. This example assumes your Earthfile has a `+build` target defined.

```yml
# ./bitbucket-pipelines.yml

image: earthly/earthly:v0.7.23

pipelines:
  default:
    - step:
        name: "Set Earthly token"
        script:
          - export EARTHLY_TOKEN=$EARTHLY_TOKEN
          # See https://docs.earthly.dev/docs/earthly-command#earthly-account-create-token to obtain a token.
          - earthly --version
    - step:
        name: "Docker login"
        script:
          - docker login --username "$DOCKERHUB_USERNAME" --password "$DOCKERHUB_TOKEN"
    - step:
        name: "Build"
        script:
          - earthly --push --sat $EARTHLY_SAT --org $EARTHLY_ORG +build
```

For a complete guide on CI integration see the [CI integration guide](https://docs.earthly.dev/earthly-0.7/ci-integration/overview).
