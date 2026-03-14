# Source: https://docs.mystic.ai/docs/cicd-integration.md

# CI/CD Integration

Upload and deploy pipelines as part of your CI/CD flows

GitHub (and other platforms) offer a variety of tools to allow automated execution of arbitrary workflows when new code is committed, or under other conditions such as PR merges. This guide covers how to upload pipelines to Mystic as part of this automation system. We will be covering the use of GitHub actions but the insights are easily transferrable.

All code is available in our example repo here: [mystic-ai/ci-cd-example](https://github.com/mystic-ai/ci-cd-example), for this guide.

## Overview

Our CI/CD flow works by using the docker buildx action with our python dependencies installed to build the pipeline and then push it to specific tags. In this example we have a `src/` directory with out pipeline files that will then be targeted later on.

This guide will not cover the basics on how to use GitHub actions, but if you are unfamiliar with them I recommend reading the GitHub docs here: <<https://docs.github.com/en/actions>>.

## Workflows

We will be considering the simple case of a manually triggered workflow. You can create github actions by placing in yaml configuration files into your repo in the `.github/workflows` directory. We will be using two files in our example:

* `.github/workflows/docker-build.yaml` - This contains the pipeline specific build code that can be used by any github action
* `.github/workflows/manual-docker.yaml` - This is the manual github action that calls the above workflow

> 📘 Secrets
>
> This example does use the `PIPELINE_API_TOKEN` which you will have to have present in your GitHub actions secrets or Organisation secrets.

Here's the code:

```yaml
# manual-docker.yaml
name: Manual docker building
on:
  workflow_dispatch:
    inputs:
      pipeline_tag:
        description: "Pipeline tag"
        required: true
        default: "manual"
run-name: "Building pipeline: ${{ github.ref_name }} -> ${{ inputs.pipeline_tag }}"
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check formatting
        uses: psf/black@stable
        with:
          version: 23.12.0
  build-pipeline:
    needs:
      - lint
    uses: ./.github/workflows/docker-build.yaml
    with:
      pipelineTag: ${{ inputs.pipeline_tag }}
    secrets:
      PIPELINE_API_TOKEN: ${{ secrets.PIPELINE_API_TOKEN }}

```

```yaml
# docker-build.yaml
name: Build and push Docker image
on:
  workflow_call:
    inputs:
      pipelineTag:
        required: true
        type: string
      commitRef:
        description: "Commit reference to checkout"
        type: string
        # Empty value uses the default behaviour of actions/checkout@v3.with.ref
        default: ""
    secrets:
      PIPELINE_API_TOKEN:
        required: true
        description: The API token to authenticate with the pipeline
jobs:
  build-push-image:
    runs-on: ubuntu-latest
    env:
      PIPELINE_API_TOKEN: ${{secrets.PIPELINE_API_TOKEN}}
    steps:
      - uses: actions/checkout@v3
        with:
          ref: ${{ inputs.commitRef }}
      - uses: docker/setup-buildx-action@v2
      - name: Setup environment
        run: |
          pip install -U poetry
          poetry install
      - name: Build pipeline
        run: |
          cd src/
          poetry run pipeline container build
      - name: Push pipeline image
        run: |
          cd src/
          poetry run pipeline container push -p paulh/random-generator:${{ inputs.pipelineTag }} -o

```

In this example we take a single user input of `pipelineTag` in the `manual-docker.yaml` file to pass into the pointer definition when we finally push.

## How it works

To build and push a pipeline we will need:

* Docker to be installed
* `poetry` to be running our python virtual environment (you can use another venv but it will be more complicated)
* `pipeline-ai` python SDK installed

Heres the steps in our build/push flow:

```yaml
steps:
  - uses: actions/checkout@v3
    with:
      ref: ${{ inputs.commitRef }}
  - uses: docker/setup-buildx-action@v2
  - name: Setup environment
    run: |
      pip install -U poetry
      poetry install
  - name: Build pipeline
    run: |
      cd src/
      poetry run pipeline container build
  - name: Push pipeline image
    run: |
      cd src/
      poetry run pipeline container push -p paulh/random-generator:${{ inputs.pipelineTag }} -o
```

This works by:

1. Performing a checkout on the target branch to make sure the correct code will be present on the system
2. Poetry is installed and then our project dependencies are also installed with `poetry install` - this installs `pipeline-ai`
3. We build the container with `poetry run pipeline container build`. By prepending `poetry run` we ensure that we're using the poetry venv. This step also communicates with the local docker installation. Docker is setup in line 5 above when we run `- uses: docker/setup-buildx-action@v2`
4. We push the pipeline to Mystic with a fixed tag that was passed in as an input. The `-o` field is for overwriting existing pointers if they already exist.

One additional useful modification could be to associate a pipeline with a specific commit hash, this is possible by adding an additional pointer to the push command:

```yaml
...
  - name: Build pipeline
    run: |
      cd src/
      poetry run pipeline container build
  - name: Push pipeline image
    run: |
      cd src/
      poetry run pipeline container push -p paulh/random-generator:${{ inputs.pipelineTag }} -p paulh/random-generator:${{ inputs.commitRef }} -o
```

It's possible to do this as the `commitRef` is passed as an input from the main `manual-docker.yaml` file.

<br>