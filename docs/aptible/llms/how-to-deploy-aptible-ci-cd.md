# Source: https://www.aptible.com/docs/how-to-guides/app-guides/how-to-deploy-aptible-ci-cd.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to deploy to Aptible with CI/CD

## Overview

To make it easier to deploy on Aptible—whether you're migrating from another platform or deploying your first application—we offer integrations with several continuous integration services.

* [Deploying with Git](/how-to-guides/app-guides/how-to-deploy-aptible-ci-cd#deploying-with-git)

* [Deploying with Docker](/how-to-guides/app-guides/how-to-deploy-aptible-ci-cd#deploying-with-docker)

If your team is already using a Git-based deployment workflow, deploying your app to Aptible should be relatively straightforward.

## Deploying with Git

### Prerequisites

To deploy to Aptible via Git, you must have a public SSH key associated with your account. We recommend creating a robot user to manage your deployment:

1. Create a "Robots" [custom role](/core-concepts/security-compliance/access-permissions) in your Aptible [organization](/core-concepts/security-compliance/access-permissions), and grant it "Full Visibility" and "Deployment" [permissions](/core-concepts/security-compliance/access-permissions) for the [environment](/core-concepts/architecture/environments) where you will be deploying.

2. Invite a new robot user with a valid email address (for example, `deploy@yourdomain.com`) to the `Robots` role.

3. Sign out of your Aptible account, accept the invitation from the robot user's email address, and set a password for the robot's Aptible account.

4. Generate a new SSH key pair to be used by the robot user, and don't set a password: `ssh-keygen -t ed25519 -C "your_email@example.com"`

5. Register the [SSH Public Key](/core-concepts/security-compliance/authentication/ssh-keys) with Aptible for the robot user.

<Tabs>
  <Tab title="GitHub Actions">
    ### Configuring the Environment

    First, you'll need to configure a few [environment variables](https://docs.github.com/en/actions/learn-github-actions/variables#defining-configuration-variables-for-multiple-workflows) and [secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#using-encrypted-secrets-in-a-workflow) for your repository:

    1. Environment variable: `APTIBLE_APP`, the name of the App to deploy.
    2. Environment variable: `APTIBLE_ENVIRONMENT`, the name of the Aptible environment in which your App lives.
    3. Secret: `APTIBLE_USERNAME`, the username of the Aptible user with which to deploy the App.
    4. Secret: `APTIBLE_PASSWORD`, the password of the Aptible user with which to deploy the App.

    ### Configuring the Workflow

    Finally, you must configure the workflow to deploy your application to Aptible:

    ```sql  theme={null}
    on:
      push:
        branches: [ main ]

    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
            with:
              fetch-depth: 0
          - name: Deploy to Aptible
            uses: aptible/aptible-deploy-action@v4
            with:
              type: git
              app: ${{ vars.APTIBLE_APP }}
              environment: ${{ vars.APTIBLE_ENVIRONMENT }}
              username: ${{ secrets.APTIBLE_USERNAME }}
              password: ${{ secrets.APTIBLE_PASSWORD }}
    ```
  </Tab>

  <Tab title="CircleCI">
    ### Configuring SSH

    To deploy to Aptible via CircleCI, [add your SSH Private Key via the CircleCI Dashboard](https://circleci.com/docs/2.0/add-ssh-key/#circleci-cloud-or-server-3-x) with the following values:

    * **Hostname:** `beta.aptible.com`
    * **Private Key:** The contents of the SSH Private Key created in the previous step.

    ### Configuring the Environment

    You also need to set environment variables on your project with the name of your Aptible environment and app, in `APTIBLE_ENVIRONMENT` and `APTIBLE_APP`, respectively. You can add these to your project using [environment variables](https://circleci.com/docs/2.0/env-vars/) on the Circle CI dashboard.

    ### Configuring the Deployment

    Finally, you must configure the Circle CI project to deploy your application to Aptible:

    ```sql  theme={null}
    version: 2.1

    jobs:
      git-deploy:
        docker:
          - image: debian:latest
        filters:
          branches:
            only:
              - circle-deploy
        steps:
          # Add your private key to your repo: https://circleci.com/docs/2.0/configuration-reference/#add-ssh-keys
          - checkout
          - run:
              name: Git push and deploy to Aptible
              command: |
                apt-get update && apt-get install -y git openssh-client
                ssh-keyscan beta.aptible.com >> ~/.ssh/known_hosts
                git remote add aptible git@beta.aptible.com:$APTIBLE_ENVIRONMENT/$APTIBLE_APP.git
                git push aptible $CIRCLE_SHA1:master

    workflows:
      version: 2
      deploy:
        jobs:
          - git-deploy
    ```

    Let’s break down how this works. We begin by defining when the deployment should run (when a push is made to the `circle-deploy` branch):

    ```sql  theme={null}
    jobs:
      git-deploy:
        docker:
          - image: debian:latest
        filters:
          branches:
            only:
              - circle-deploy
    ```

    The most important part of this configuration is the value of the `command` key under the `run` step. Here we add our SSH private key to the Circle CI environment, configure a new remote for our repository on Aptible’s platform, and push our branch to Aptible:

    ```sql  theme={null}
    jobs:
      git-deploy:
        # # #
        steps:
          - checkout
          - run:
              name: Git push and deploy to Aptible
              command: |
                apt-get update && apt-get install -y git openssh-client
                ssh-keyscan beta.aptible.com >> ~/.ssh/known_hosts
                git remote add aptible git@beta.aptible.com:$APTIBLE_ENVIRONMENT/$APTIBLE_APP.git
                git push aptible $CIRCLE_SHA1:master
    ```

    From there, the procedure for a [Dockerfile-based deployment](/how-to-guides/app-guides/deploy-from-git) remains the same!
  </Tab>

  <Tab title="Travis CI">
    ### Configuring SSH

    To deploy to Aptible via Travis CI, [add your SSH Private Key via the Travis CI repository settings](https://docs.travis-ci.com/user/environment-variables/#defining-variables-in-repository-settings) with the following values:

    * **Name:** `APTIBLE_GIT_SSH_KEY`
    * **Value:** The ***base64-encoded*** contents of the SSH Private Key created in the previous step.

    > ⚠️ Warning
    >
    > The SSH private key added to the Travis CI environment variable must be base64-encoded.

    ### Configuring the Environment

    You also need to set environment variables on your project with the name of your Aptible environment and app, in `APTIBLE_ENVIRONMENT` and `APTIBLE_APP`, respectively. You can add these to your project using [environment variables](https://docs.travis-ci.com/user/environment-variables/#defining-variables-in-repository-settings) on the Travis CI dashboard.

    ### Configuring the Deployment

    Finally, you must configure the Travis CI project to deploy your application to Aptible:

    ```sql  theme={null}
    language: generic
    sudo: true

    services:
      - docker

    jobs:
      include:
        - stage: push
          if: branch = travis-deploy
          addons:
            ssh_known_hosts: beta.aptible.com
          before_script:
            - mkdir -p ~/.ssh
            # to save it, cat <<KEY>> | base64 and save that in secrets
            - echo "$APTIBLE_GIT_SSH_KEY" | base64 -d > ~/.ssh/id_rsa
            - chmod 0400 ~/.ssh/id_rsa
            - eval "$(ssh-agent -s)"
            - ssh-add ~/.ssh/id_rsa
            - ssh-keyscan beta.aptible.com >> ~/.ssh/known_hosts

          script:
            - git remote add aptible git@beta.aptible.com:$APTIBLE_ENVIRONMENT/$APTIBLE_APP.git
            - git push aptible $TRAVIS_COMMIT:master
    ```

    Let’s break down how this works. We begin by defining when the deployment should run (when a push is made to the `travis-deploy` branch) and where we are going to deploy (so we add `beta.aptible.com` as a known host):

    ```sql  theme={null}
    # # #
    jobs:
      include:
        - stage: push
          if: branch = travis-deploy
          addons:
            ssh_known_hosts: beta.aptible.com
    ```

    The Travis CI configuration then allows us to split our script into two parts, with the `before_script` configuring the Travis CI environment to use our SSH key:

    ```sql  theme={null}
          # Continued from above
          before_script:
            - mkdir -p ~/.ssh
            # to save it, cat <<KEY>> | base64 and save that in secrets
            - echo "$APTIBLE_GIT_SSH_KEY" | base64 -d > ~/.ssh/id_rsa
            - chmod 0400 ~/.ssh/id_rsa
            - eval "$(ssh-agent -s)"
            - ssh-add ~/.ssh/id_rsa
            - ssh-keyscan beta.aptible.com >> ~/.ssh/known_hosts
    ```

    Finally, our `script` block configures a new remote for our repository on Aptible’s platform, and pushes our branch to Aptible:

    ```sql  theme={null}
          # Continued from above
          script:
            - git remote add aptible git@beta.aptible.com:$APTIBLE_ENVIRONMENT/$APTIBLE_APP.git
            - git push aptible $TRAVIS_COMMIT:master
    ```

    From there, the procedure for a [Dockerfile-based deployment](/how-to-guides/app-guides/deploy-from-git) remains the same!
  </Tab>

  <Tab title="GitLab CI">
    ### Configuring SSH

    To deploy to Aptible via GitLab CI, [add your SSH Private Key via the GitLab CI dashboard](https://docs.gitlab.com/ee/ci/ssh_keys/#ssh-keys-when-using-the-docker-executor) with the following values:

    * **Key:** `APTIBLE_GIT_SSH_KEY`
    * **Value:** The ***base64-encoded*** contents of the SSH Private Key created in the previous step.

    > ⚠️ Warning
    >
    > The SSH private key added to the GitLab CI environment variable must be base64-encoded.

    ### Configuring the Environment

    You also need to set environment variables on your project with the name of your Aptible environment and app, in `APTIBLE_ENVIRONMENT` and `APTIBLE_APP`, respectively. You can add these to your project using [project variables](https://docs.gitlab.com/ee/ci/variables/#add-a-cicd-variable-to-a-project) on the GitLab CI dashboard.

    ### Configuring the Deployment

    Finally, you must configure the GitLab CI pipeline to deploy your application to Aptible:

    ```sql  theme={null}
    image: debian:latest

    git_deploy_job:
      only:
        - gitlab-deploy
      before_script:
        - apt-get update && apt-get install -y git
        # taken from: https://docs.gitlab.com/ee/ci/ssh_keys/
        - 'command -v ssh-agent >/dev/null || ( apt-get update -y && apt-get install openssh-client -y )'
        - eval $(ssh-agent -s)
        # to save it, cat <<KEY>> | base64 and save that in secrets
        - echo "$DEMO_APP_APTIBLE_GIT_SSH_KEY" | base64 -d | tr -d '
    ' | ssh-add -
        - mkdir -p ~/.ssh
        - chmod 700 ~/.ssh
      script:
        - |
          ssh-keyscan beta.aptible.com >> ~/.ssh/known_hosts
          git remote add aptible git@beta.aptible.com:$DEMO_APP_APTIBLE_ENVIRONMENT/$DEMO_APP_APTIBLE_APP.git
          git push aptible $CI_COMMIT_SHA:master
    ```

    Let’s break down how this works. We begin by defining when the deployment should run (when a push is made to the `gitlab-deploy` branch), and then we define the `before_script` that will configure SSH in our job environment:

    ```sql  theme={null}
      # . . .
      before_script:
        - apt-get update && apt-get install -y git
        # taken from: https://docs.gitlab.com/ee/ci/ssh_keys/
        - 'command -v ssh-agent >/dev/null || ( apt-get update -y && apt-get install openssh-client -y )'
        - eval $(ssh-agent -s)
        - echo "$DEMO_APP_APTIBLE_GIT_SSH_KEY" | base64 -d | tr -d '
    ' | ssh-add -
        - mkdir -p ~/.ssh
        - chmod 700 ~/.ssh
    ```

    Finally, our `script` block configures a new remote for our repository on Aptible’s platform, and pushes our branch to Aptible:

    ```sql  theme={null}
      # Continued from above
      script:
        - |
          ssh-keyscan beta.aptible.com >> ~/.ssh/known_hosts
          git remote add aptible git@beta.aptible.com:$DEMO_APP_APTIBLE_ENVIRONMENT/$DEMO_APP_APTIBLE_APP.git
          git push aptible $CI_COMMIT_SHA:master
    ```

    From there, the procedure for a [Dockerfile-based deployment](/how-to-guides/app-guides/deploy-from-git) remains the same!
  </Tab>
</Tabs>

## Deploying with Docker

### Prerequisites

To deploy to Aptible with a Docker image via a CI integration, you should create a robot user to manage your deployment:

1. Create a `Robots` [custom Aptible role](/core-concepts/security-compliance/access-permissions) in your Aptible organization. Grant it "Read" and "Manage" permissions for the environment where you would like to deploy.

2. Invite a new robot user with a valid email address (for example, `deploy@yourdomain.com`) to the `Robots` role.

3. Sign out of your Aptible account, accept the invitation from the robot user's email address, and set a password for the robot's Aptible account.

<Tabs>
  <Tab title="GitHub Actions">
    Some of the below instructions and more information can also be found on the Github Marketplace page for the [Deploy to Aptible Action.](https://github.com/marketplace/actions/deploy-to-aptible#example-with-container-build-and-docker-hub)

    ## Configuring the Environment

    To deploy to Aptible via GitHub Actions, you must first [create encrypted secrets for your repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) with Docker registry and Aptible credentials:

    `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`
    The credentials for your private Docker registry (in this case, DockerHub).

    `APTIBLE_USERNAME` and `APTIBLE_PASSWORD`
    The credentials for the robot account created to deploy to Aptible.

    ## Configuring the Workflow

    Additionally, you will need to set some environment variables within the GitHub Actions workflow:

    `IMAGE_NAME`
    The Docker image you wish to deploy from your Docker registry.

    `APTIBLE_ENVIRONMENT`
    The name of the Aptible environment acting as the target for this deployment.

    `APTIBLE_APP`
    The name of the app within the Aptible environment we are deploying with this workflow.

    ## Configuring the Workflow

    Finally, you must configure the workflow to deploy your application to Aptible:

    ```ruby  theme={null}
    on:
      push:
        branches: [ main ]

    env:
      IMAGE_NAME: user/app:latest
      APTIBLE_ENVIRONMENT: "my_environment"
      APTIBLE_APP: "my_app"

    jobs:
      deploy:
        runs-on: ubuntu-latest

        steps:
          # Allow multi-platform builds.
          - name: Set up QEMU
            uses: docker/setup-qemu-action@v2

          # Allow use of secrets and other advanced docker features.
          - name: Set up Docker Buildx
            uses: docker/setup-buildx-action@v2

          # Log into Docker Hub
          - name: Login to DockerHub
            uses: docker/login-action@v2
            with:
              username: ${{ secrets.DOCKERHUB_USERNAME }}
              password: ${{ secrets.DOCKERHUB_TOKEN }}

          # Build image using default dockerfile.
          - name: Build and push
            uses: docker/build-push-action@v3
            with:
              push: true
              tags: ${{ env.IMAGE_NAME }}

          # Deploy to Aptible
          - name: Deploy to Aptible
            uses: aptible/aptible-deploy-action@v4
            with:
              username: ${{ secrets.APTIBLE_USERNAME }}
              password: ${{ secrets.APTIBLE_PASSWORD }}
              environment: ${{ env.APTIBLE_ENVIRONMENT }}
              app: ${{ env.APTIBLE_APP }}
              docker_img: ${{ env.IMAGE_NAME }}
              private_registry_username: ${{ secrets.DOCKERHUB_USERNAME }}
              private_registry_password: ${{ secrets.DOCKERHUB_TOKEN }}
    ```
  </Tab>

  <Tab title="TravisCI">
    ## Configuring the Environment

    You also need to set environment variables on your project with the name of your Aptible environment and app, in APTIBLE\_ENVIRONMENT and APTIBLE\_APP, respectively. You can add these to your project using environment variables on the Travis CI dashboard.

    To define how the Docker image is built and deployed, you’ll need to set a few additional variables:

    `APTIBLE_USERNAME` and `APTIBLE_PASSWORD`
    The credentials for the robot account created to deploy to Aptible.

    `APTIBLE_DOCKER_IMAGE`
    The name of the Docker image you wish to deploy to Aptible.

    If you are using a private registry to store your Docker image, you also need to specify credentials to be passed to Aptible:

    `APTIBLE_PRIVATE_REGISTRY_USERNAME`
    The username of the account that can access the private registry containing the Docker image.

    `APTIBLE_PRIVATE_REGISTRY_PASSWORD`
    The password of the account that can access the private registry containing the Docker image.

    ## Configuring the Deployment

    Finally, you must configure the workflow to deploy your application to Aptible:

    ```ruby  theme={null}
    language: generic
    sudo: true

    services:
      - docker

    jobs:
      include:
      - stage: build-and-test
        script: |
          make build
          make test
      - stage: push
        if: branch = main
        script: |
          # login to your registry
          docker login \
            -u $APTIBLE_PRIVATE_REGISTRY_EMAIL \
            -p $APTIBLE_PRIVATE_REGISTRY_PASSWORD
          # push your docker image to your registry
          make push

          # download the latest aptible cli and install it
          wget https://omnibus-aptible-toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-toolbelt/latest/aptible-toolbelt_latest_debian-9_amd64.deb && \
            dpkg -i ./aptible-toolbelt_latest_debian-9_amd64.deb && \
            rm ./aptible-toolbelt_latest_debian-9_amd64.deb

          # login and deploy your app
          aptible login \
            --email "$APTIBLE_USERNAME" \
            --password "$APTIBLE_PASSWORD"
          aptible deploy \
            --environment "$APTIBLE_ENVIRONMENT" \
            --app "$APTIBLE_APP"
    ```

    Let’s break down how this works. The script for the `build-and-test` stage does what it says on the label: It builds our Docker image as runs tests on it, as we’ve defined in a Makefile.

    Then, script from the `push` stage pushes our image to the Docker registry:

    ```ruby  theme={null}
    # login to your registry
    docker login \
      -u $APTIBLE_PRIVATE_REGISTRY_EMAIL \
      -p $APTIBLE_PRIVATE_REGISTRY_PASSWORD
    # push your docker image to your registry
    make push
    ```

    Finally, it installs the Aptible CLI in the Travis CI build environment, logs in to Aptible, and deploys your Docker image to the specified envrionment and app:

    ```ruby  theme={null}
    # download the latest aptible cli and install it
    wget https://omnibus-aptible-toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-toolbelt/aptible-toolbelt-latest_amd64.deb && \
      dpkg -i ./aptible-toolbelt-latest_amd64.deb && \
      rm ./aptible-toolbelt-latest_amd64.deb

    # login and deploy your app
    aptible login \
      --email "$APTIBLE_USERNAME" \
      --password "$APTIBLE_PASSWORD"
    aptible deploy \
      --environment "$APTIBLE_ENVIRONMENT" \
      --app "$APTIBLE_APP"
    ```
  </Tab>
</Tabs>

From there, you can review our resources for [Direct Docker Image Deployments!](/how-to-guides/app-guides/migrate-dockerfile-to-direct-image-deploy)
