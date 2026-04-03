Skip to main content

    Technology areas

        close

                      AI and ML

                      Application development

                      Application hosting

                      Compute

                      Data analytics and pipelines

                      Databases

                      Distributed, hybrid, and multicloud

                      Industry solutions

                      Migration

                      Networking

                      Observability and monitoring

                      Security

                      Storage

    Cross-product tools

        close

                      Access and resources management

                      Costs and usage management

                      Infrastructure as code

                      SDK, languages, frameworks, and tools

            /

  Console

      English

      Deutsch

      Español

      Español – América Latina

      Français

      Indonesia

      Italiano

      Português

      Português – Brasil

      中文 – 简体

      中文 – 繁體

      日本語

      한국어

              Sign in

          Cloud Build

  Start free

    Overview

    Guides

    Reference

    Samples

    Support

    Resources

      Technology areas

      More

      Overview

      Guides

      Reference

      Samples

      Support

      Resources

      Cross-product tools

      More

      Console

        Discover

  Cloud Build overview

        Quickstarts
      BuildDeployAutomateCreate private pools

        Get started

  Set up Cloud Build

        Set up private pools
      OverviewCreate and manage private poolsPrivate pool configuration file schemaRun builds in a private pool

        Control access
      IAM roles and permissionsConfigure access to resourcesManage resources with custom constraints

        Configure

  Create a build config file

  Build configuration file schema

  Cloud builders

  Use community-contributed and custom builders

  Substitute variable values

  Run bash scripts

  Interact with Docker Hub images

  Configure the order of build steps

  Pass data between build steps

  Use payload bindings and bash parameter expansions in substitutions

        Build, test, and store

  Develop applications

  Manage dependencies

  Build container images

  Build and test Node.js applications

        Build and test Java applications
      Build and test Java applicationsBuild, test, and containerize Java applications

        Build and test Python applications
      Build and test Python applicationsBuild, test, and containerize Python applications

        Build and test Go applications
      Build and test Go applicationsBuild, test, and containerize Go applications

  Build VM images using Packer

  Store build artifacts in Artifact Registry

  Store build artifacts in Cloud Storage

  Provision Cloud Build resources with Terraform

        Deploy

  Deploy to GKE

  Deploy to Cloud Run

  Deploy to App Engine

  Deploy to Cloud Functions

  Deploy to GKE Enterprise

  Deploy to Compute Engine

  Deploy to Firebase

        Run builds

  Triggers overview

  Repositories overview

        Manually run a fully-managed build
      Submit a build via the command line and APIManually build code in source repositories

  Create and manage build triggers

        GitHub
      Connect to a GitHub repositoryBuild repositories from GitHubAccess GitHub from a build via SSH keys

        GitHub Enterprise
      Connect to a GitHub Enterprise hostConnect to a GitHub Enterprise repositoryBuild repositories from GitHub EnterpriseBuild repositories from GitHub Enterprise in a private network

        GitLab
      Connect to a GitLab hostConnect to a GitLab repositoryBuild repositories from GitLab

        GitLab Enterprise Edition
      Connect to a GitLab Enterprise Edition hostConnect to a GitLab Enterprise Edition repositoryBuild repositories from GitLab Enterprise EditionBuild repositories from GitLab Enterprise Edition in a private network

        Bitbucket Server
      Connect to a Bitbucket Server hostConnect to a Bitbucket Server repositoryBuild repositories from Bitbucket ServerBuild repositories from Bitbucket Server in a private network

        Bitbucket Data Center
      Connect to a Bitbucket Data Center hostConnect to a Bitbucket Data Center repositoryBuild repositories from Bitbucket Data CenterBuild repositories from Bitbucket Data Center in a private network

        Bitbucket Cloud
      Connect to a Bitbucket Cloud hostConnect to a Bitbucket Cloud repositoryBuild repositories from Bitbucket Cloud

  Automate builds in response to Pub/Sub events

  Automate builds in response to webhook events

  Schedule builds

  GitOps-style continuous delivery with Cloud Build

        View results and monitor

  Audit logging

        Store and manage build logs
      Store and view build logsUse structured logging with build logs

  View build results

  View build results for triggers

  View build security insights

        Configure downstream notifications

  Cloud Build notifiers overview

  Configure BigQuery notifications

  Configure GitHub Issue notifications

  Configure Google Chat notifications

  Configure HTTP notifications

  Configure Slack notifications

  Configure SMTP notifications

  Automate configuration for notifications

  Create your own notifier

  Subscribe to build notifications

        Secure builds

  Statement of shared responsibility

        Secrets and credentials
      Use secrets from Secret ManagerUse encrypted credentials

  CMEK compliance

  Generate and validate build provenance

  Secure image deployments to Cloud Run and Google Kubernetes Engine

  Use on-demand scanning in Cloud Build pipelines

        Gate builds
      Gate builds on approvalsGate builds on organization policy

  Configure Cloud Build service account impersonation for managed services

        Secure the network

  Use Cloud Build in a private network

  Set up environment to use private pools in a VPC network

  Access resources in a private JFrog Artifactory with private pools

  Access external resources in a private network using a static external IP

  Access private GKE clusters with Cloud Build private pools

  Access private GKE clusters from Cloud Build private pools using Identity Service for GKE

  Use VPC Service Controls

        Integrate with Google Cloud services

  Configure user-specified service accounts

  Default Cloud Build service account

  Configure access for the default Cloud Build service account

  Authorize service-to-service access

  Cloud Build default service account change

        Optimize

  Increase vCPU for builds

  Best practices to speed up builds

  Build leaner containers

  Manage infrastructure as code with Terraform, Cloud Build, and GitOps

        Troubleshoot

  Troubleshoot build errors

      AI and ML

      Application development

      Application hosting

      Compute

      Data analytics and pipelines

      Databases

      Distributed, hybrid, and multicloud

      Industry solutions

      Migration

      Networking

      Observability and monitoring

      Security

      Storage

      Access and resources management

      Costs and usage management

      Infrastructure as code

      SDK, languages, frameworks, and tools

          Home

          Documentation

          Application development

          Cloud Build

          Guides

    Send feedback

      Substituting variable values

      Stay organized with collections

      Save and categorize content based on your preferences.

Use `substitutions` in your build config file to substitute specific variables at
build time.

Substitutions are helpful for variables whose value isn&#39;t known until
build time, or to re-use an existing build request with different variable
values.

Cloud Build provides built-in substitutions or you can define your own
substitutions. Use `substitutions` in your build&#39;s `steps` and `images`
to resolve their values at build time.

This page explains how to use default substitutions or define your own
`substitutions`.

## Using default substitutions

Cloud Build provides the following default substitutions for all
builds:

- `$PROJECT_ID`: ID of your Cloud project

- `$BUILD_ID`: ID of your build

- `$PROJECT_NUMBER`: your project number

- `$LOCATION`: the region associated with your build

Cloud Build provides the following default substitutions for builds
invoked by triggers:

- `$TRIGGER_NAME`: the name associated with your trigger

- `$COMMIT_SHA`: the commit ID associated with your build

- `$REVISION_ID`: the commit ID associated with your build

- `$SHORT_SHA` : the first seven characters of `COMMIT_SHA`

- `$REPO_NAME`: the name of your repository

- `$REPO_FULL_NAME`: the full name of your repository, including either the user or organization

- `$BRANCH_NAME`: the name of your branch

- `$TAG_NAME`: the name of your tag

- `$REF_NAME`: the name of your branch or tag
`$TRIGGER_BUILD_CONFIG_PATH`: the path to your build configuration file used
during your build execution; otherwise, an empty string if your build is
configured inline on the trigger or uses a `Dockerfile` or `Buildpack`.
`$SERVICE_ACCOUNT_EMAIL`: email of the service account you are using for the
build. This is either a default service account or a user-specified service
account.
`$SERVICE_ACCOUNT`: the resource name of the service account, in the format
`projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL`

Note: Both `$COMMIT_SHA` and `$REVISION_ID` represent the commit ID associated
with your build. Support for both substitutions is available.
Cloud Build provides the following GitHub-specific default
substitutions available for pull request triggers:

- `$_HEAD_BRANCH` : head branch of the pull request

- `$_BASE_BRANCH` : base branch of the pull request

- `$_HEAD_REPO_URL` : URL of the head repository of the pull request

- `$_PR_NUMBER` : number of the pull request

If a default substitution is not available (such as with sourceless builds,
or with builds that use storage source), then occurrences of the missing
variable are replaced with an empty string.

When starting a build using `gcloud builds submit`, you can specify
variables that would normally come from triggered builds with the
`--substitutions` argument. Specifically,
you can manually provide values for:

- `$TRIGGER_NAME`

- `$COMMIT_SHA`

- `$REVISION_ID`

- `$SHORT_SHA`

- `$REPO_NAME`

- `$REPO_FULL_NAME`

- `$BRANCH_NAME`

- `$TAG_NAME`

- `$REF_NAME`

- `$TRIGGER_BUILD_CONFIG_PATH`

- `$SERVICE_ACCOUNT_EMAIL`

- `$SERVICE_ACCOUNT`

For example, the following command uses the `TAG_NAME` substitution:

gcloud builds submit --config=cloudbuild.yaml \
    --substitutions=TAG_NAME="test"

The following example uses the default substitutions `$BUILD_ID`, `$PROJECT_ID`, `$PROJECT_NUMBER`, and `$REVISION_ID`.

###  YAML 
steps:
# Uses the ubuntu build step:
# to run a shell script; and
# set env variables for its execution
- name: 'ubuntu'
  args: ['bash', './myscript.sh']
  env:
  - 'BUILD=$BUILD_ID'
  - 'PROJECT_ID=$PROJECT_ID'
  - 'PROJECT_NUMBER=$PROJECT_NUMBER'
  - 'REV=$REVISION_ID'

# Uses the docker build step to build an image called my-image
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/my-image', '.']

# my-image is pushed to Artifact Registry
images:
- '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/my-image'

###  JSON 
{
  "steps": [{
      "name": "ubuntu",
      "args": [
        "bash",
        "./myscript.sh"
      ],
      "env": [
        "BUILD=$BUILD_ID",
        "PROJECT_ID=$PROJECT_ID",
        "PROJECT_NUMBER=$PROJECT_NUMBER",
        "REV=$REVISION_ID"
      ]
    }, {
      "name": "gcr.io/cloud-builders/docker",
      "args": ["build", "-t", "gcr.io/$PROJECT_ID/my-image", "."]
    }],
  "images": [
    "gcr.io/$PROJECT_ID/my-image"
  ]
}

The following example shows a build request using the `docker` build step to
build an image, then pushes the image to Artifact Registry using the default
`$PROJECT_ID` substitution:

In this example:

The build request has one build step, which uses the `docker` build step in
`gcr.io/cloud-builders` to build the Docker image.

The `args` field in the step specifies the arguments to pass to the
`docker` command, in this case `build -t gcr.io/my-project/cb-demo-img .`,
will be invoked (after `$PROJECT_ID` is substituted with your project ID).

The
`images`
field contains the image&#39;s name. If the build is successful, the resulting
image is pushed to Artifact Registry. If the image is not created successfully
by the build, the build will fail.

### YAML
steps:
- name: gcr.io/cloud-builders/docker
  args: ["build", "-t", "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/cb-demo-img", "."]
images:
- '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/cb-demo-img'

### JSON
{
  "steps": [{
      "name": "gcr.io/cloud-builders/docker",
      "args": ["build", "-t", "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/cb-demo-img", "."]
    }],
  "images": [
    "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/cb-demo-img"
  ]
}

## Using user-defined substitutions

You can also define your own substitutions. User-defined substitutions must conform to the following rules:

Substitutions must begin with an underscore (`_`) and use
only uppercase-letters and numbers (respecting the regular expression
`_[A-Z0-9_]+`). This prevents conflicts with built-in substitutions. To use
an expression starting with `$` you must use `$$`. For example:

- `$FOO` is invalid since it is not a built-in substitution.

- `$$FOO` evaluates to the literal string `$FOO`.

The number of parameters is limited to 200 parameters. The length of a
parameter key is limited to 100 bytes and the length of a parameter value is
limited to 4000 bytes.

You can specify variables in one of two ways: `$_FOO` or `${_FOO}`:

Both `$_FOO` and `${_FOO}` evaluate to the value of `_FOO`. However, `${}`
lets the substitution work without surrounding spaces, which allows for
substitutions like `${_FOO}BAR`.
`$$` lets you include a literal `$` in the template. For example:

- `$_FOO` evaluates to the value of `_FOO`.

- `$$_FOO` evaluates to the literal string `$_FOO`.
`$$$_FOO` evaluates to the literal string `$` followed by the value of
`_FOO`.

To use the substitutions, use the `--substitutions`
argument in the `gcloud` command
or specify them in the config file.

The following example shows a build config with two user-defined substitutions
called `_NODE_VERSION_1` and `_NODE_VERSION_2`:

###  YAML 
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build',
          '--build-arg',
          'node_version=${_NODE_VERSION_1}',
          '-t',
          '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_1}',
          '.']
- name: 'gcr.io/cloud-builders/docker'
  args: ['build',
          '--build-arg',
          'node_version=${_NODE_VERSION_2}',
          '-t',
          '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_2}',
          '.']
substitutions:
    _NODE_VERSION_1: v6.9.1 # default value
    _NODE_VERSION_2: v6.9.2 # default value
images: [
    '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_1}',
    '${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_2}'
]

###  JSON 
{
    "steps": [{
        "name": "gcr.io/cloud-builders/docker",
        "args": [
            "build",
            "--build-arg",
            "node_version=${_NODE_VERSION_1}",
            "-t",
            "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_1}",
            "."
        ]
    }, {
        "name": "gcr.io/cloud-builders/docker",
        "args": [
            "build",
            "--build-arg",
            "node_version=${_NODE_VERSION_2}",
            "-t",
            "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_2}",
            "."
        ]
    }],
    "substitutions": {
        "_NODE_VERSION_1": "v6.9.1",
        "_NODE_VERSION_2": "v6.9.2",
    },
    "images": [
        "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_1}",
        "${_LOCATION}-docker.pkg.dev/$PROJECT_ID/${_REPOSITORY}/build-substitutions-nodejs-${_NODE_VERSION_2}"
    ]
}

To override the substitution value you specified in the build config file,
use the `--substitutions` flag in the `gcloud builds submit` command. Note
that substitutions are a mapping of variables to values rather than arrays or
sequences. You can override default substitution variable
values except for `$PROJECT_ID` and `$BUILD_ID`. The following command overrides
the default value for `_NODE_VERSION_1` specified in the previous build config
file:
gcloud builds submit --config=cloudbuild.yaml \
  --substitutions=_NODE_VERSION_1="v6.9.4",_NODE_VERSION_2="v6.9.5" .

By default, the build returns an error if there&#39;s a
missing substitution variable or a missing substitution. However, you can set
the `ALLOW_LOOSE` option to skip this check.

The following snippet prints &quot;hello world&quot; and defines an unused substitution.
Because the `ALLOW_LOOSE` substitution option is set, the build will be
successful despite the missing substitution.

###  YAML 
steps:
- name: 'ubuntu'
  args: ['echo', 'hello world']
substitutions:
    _SUB_VALUE: unused
options:
    substitutionOption: 'ALLOW_LOOSE'

###  JSON 
{
    "steps": [
    {
        "name": "ubuntu",
        "args": [
            "echo",
            "hello world"
        ]
    }
    ],
    "substitutions": {
        "_SUB_VALUE": "unused"
},
    "options": {
        "substitution_option": "ALLOW_LOOSE"
    }
}

If your build is invoked by a trigger, the `ALLOW_LOOSE` option is set by
default. In this case, your build won&#39;t return an error if there is a
missing substitution variable or a missing substitution. You cannot override
the `ALLOW_LOOSE` option for builds invoked by triggers.

If the `ALLOW_LOOSE` option is not specified, unmatched keys in your substitutions
mapping or build request will result in error. For example, if your build request
includes `$_FOO` and the substitutions mapping doesn&#39;t define `_FOO`, you
will receive an error after running your build or invoking a trigger if your
trigger includes substitution variables.

The following substitution variables always contain a default empty-string
value even if you don&#39;t set the `ALLOW_LOOSE` option:

- `$REPO_NAME`

- `$REPO_FULL_NAME`

- `$BRANCH_NAME`

- `$TAG_NAME`

- `$COMMIT_SHA`

- `$SHORT_SHA`

When defining a substitution variable, you aren&#39;t limited to static strings.
You also have access to the event payload that invoked your trigger. These
are available as payload bindings. You can also apply bash parameter expansions
on substitution variables and store the resulting string as a new
substitution variable. To learn more, see
Using payload bindings and bash parameter expansions in substitutions.

### Dynamic substitutions

You can reference the value of another variable within a user-defined
substitution by setting the `dynamicSubstitutions` option to `true` in
your build config file. If your build is invoked by a trigger, the
`dynamicSubstitutions` field is always set to `true` and does not need to
be specified in your build config file. If your build is invoked manually,
you must set the `dynamicSubstitutions` field to `true` for bash parameter
expansions to be interpreted when running your build.

The following build config file shows the substitution variable `${_IMAGE_NAME}` referencing the variable, `${PROJECT_ID}`. The
`dynamicSubstitutions` field is set to `true` so the reference
is applied when invoking a build manually:

###  YAML 
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', '${_IMAGE_NAME}', '.']
substitutions:
    _IMAGE_NAME: '${_LOCATION}-docker.pkg.dev/${PROJECT_ID}/${_REPOSITORY}/test-image'
options:
    dynamicSubstitutions: true

###  JSON 
{
    "steps": [
      {
          "name": "gcr.io/cloud-builders/docker",
          "args": [
            "build",
            "-t",
            "${_IMAGE_NAME}",
            "."
          ]
      }
    ],
    "substitutions": {
      "_IMAGE_NAME": "${_LOCATION}-docker.pkg.dev/${PROJECT_ID}/${_REPOSITORY}/test-image"
    },
    "options": {
      "dynamic_substitutions": true
    }
}

For more information, see Applying bash parameter expansions.

## Mapping substitutions to environment variables

Scripts don&#39;t directly support substitutions, but they support environment
variables. You can map substitutions to environment variables, either
automatically all at once, or manually by defining every environment variable
yourself.

### Map substitutions automatically

At the build level. To automatically map all the substitutions to
environment variables, which will be available throughout the entire build,
set `automapSubstitutions` to `true` as an option at the build level. For
example, the following build config file shows the user-defined
substitution `$_USER` and the default substitution `$PROJECT_ID` mapped to
environment variables:

###  YAML 
steps:
- name: 'ubuntu'
  script: |
    #!/usr/bin/env bash
    echo "Hello $_USER"
- name: 'ubuntu'
  script: |
    #!/usr/bin/env bash
    echo "Your project ID is $PROJECT_ID"
options:
  automapSubstitutions: true
substitutions:
  _USER: "Google Cloud"

###  JSON 
{
  "steps": [
    {
      "name": "ubuntu",
      "script": "#!/usr/bin/env bash echo 'Hello $_USER'"
    },
    {
      "name": "ubuntu",
      "script": "#!/usr/bin/env bash echo 'Your project ID is $PROJECT_ID'"
    }
  ],
  "options": {
    "automap_substitutions": true
  },
  "substitutions": {
    "_USER": "Google Cloud"
  }
}

At the step level. To automatically map all the substitutions and make
them available as environment variables in a single step, set the
`automapSubstitutions` field to `true` in that step. In the following
example, only the second step will show the substitutions correctly,
because it&#39;s the only one with automatic substitutions mapping enabled:

###  YAML 
steps:
- name: 'ubuntu'
  script: |
    #!/usr/bin/env bash
    echo "Hello $_USER"
- name: 'ubuntu'
  script: |
    #!/usr/bin/env bash
    echo "Your project ID is $PROJECT_ID"
  automapSubstitutions: true
substitutions:
  _USER: "Google Cloud"

###  JSON 
{
  "steps": [
    {
      "name": "ubuntu",
      "script": "#!/usr/bin/env bash echo 'Hello $_USER'"
    },
    {
      "name": "ubuntu",
      "script": "#!/usr/bin/env bash echo 'Your project ID is $PROJECT_ID'",
      "automap_substitutions": true
    }
  ],
  },
  "substitutions": {
    "_USER": "Google Cloud"
  }

Additionally, you can make the substitutions available as environment
variables in the entire build, then ignore them in one step. Set
`automapSubstitutions` to `true` at the build level, then set the same
field to `false` in the step where you want to ignore the substitutions. In
the following example, even though mapping substitutions is enabled at the
build level, the project ID will not be printed in the second step, because
`automapSubstitutions` is set to `false` in that step:

###  YAML 
steps:
- name: 'ubuntu'
  script: |
    #!/usr/bin/env bash
    echo "Hello $_USER"
- name: 'ubuntu'
  script: |
    #!/usr/bin/env bash
    echo "Your project ID is $PROJECT_ID"
  automapSubstitutions: false
options:
  automapSubstitutions: true
substitutions:
  _USER: "Google Cloud"

###  JSON 
{
  "steps": [
    {
      "name": "ubuntu",
      "script": "#!/usr/bin/env bash echo 'Hello $_USER'"
    },
    {
      "name": "ubuntu",
      "script": "#!/usr/bin/env bash echo 'Your project ID is $PROJECT_ID'",
      "automap_substitutions": false
    }
  ],
  "options": {
    "automap_substitutions": true
  },
  },
  "substitutions": {
    "_USER": "Google Cloud"
  }

### Map substitutions manually

You can manually map the substitutions to environment variables. Every
environment variable is defined at the step level using the `env`
field, and the scope of the variables is restricted to the step
where they are defined. This field takes a list of keys and values.

The following example shows how to map the substitution `$PROJECT_ID` to the
environment variable `BAR`:

###  YAML 
steps:
- name: 'ubuntu'
  env:
  - 'BAR=$PROJECT_ID'
  script: 'echo $BAR'

###  JSON 
{
  "steps": [
    {
      "name": "ubuntu",
      "env": [
        "BAR=$PROJECT_ID"
      ],
      "script": "echo $BAR"
    }
  ]
}

## What's next

Learn how to use payload bindings and bash parameter expansions in
substitutions.

- Learn how to create a basic build configuration file.

- Learn how to create and manage build triggers.

- Learn how to run builds manually in Cloud Build.

    Send feedback

  Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

  Last updated 2026-04-01 UTC.

    Need to tell us more?

      [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]]

### Products and pricing

            See all products

            Google Cloud pricing

            Google Cloud Marketplace

            Contact sales

### Support

            Community forums

            Support

            Release Notes

            System status

### Resources

            GitHub

            Getting Started with Google Cloud

            Code samples

            Cloud Architecture Center

            Training and Certification

### Engage

            Blog

            Events

            X (Twitter)

            Google Cloud on YouTube

            Google Cloud Tech on YouTube

          About Google

          Privacy

          Site terms

          Google Cloud terms

          Manage cookies

          Our third decade of climate action: join us

        Sign up for the Google Cloud newsletter

          Subscribe

      English

      Deutsch

      Español

      Español – América Latina

      Français

      Indonesia

      Italiano

      Português

      Português – Brasil

      中文 – 简体

      中文 – 繁體

      日本語

      한국어