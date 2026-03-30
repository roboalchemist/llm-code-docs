# Source: https://playwright.dev/python/docs/ci

Title: Continuous Integration | Playwright Python

URL Source: https://playwright.dev/python/docs/ci

Published Time: Thu, 26 Mar 2026 01:00:24 GMT

Markdown Content:
## Introduction[​](https://playwright.dev/python/docs/ci#introduction "Direct link to Introduction")

Playwright tests can be executed in CI environments. We have created sample configurations for common CI providers.

3 steps to get your tests running on CI:

1.   **Ensure CI agent can run browsers**: Use [our Docker image](https://playwright.dev/python/docs/docker) in Linux agents or install your dependencies using the [CLI](https://playwright.dev/python/docs/browsers#install-system-dependencies).

2.   **Install Playwright**:

`pip install playwrightplaywright install --with-deps`
3.   **Run your tests**:

`pytest`

## CI configurations[​](https://playwright.dev/python/docs/ci#ci-configurations "Direct link to CI configurations")

The [Command line tools](https://playwright.dev/python/docs/browsers#install-system-dependencies) can be used to install all operating system dependencies in CI.

### GitHub Actions[​](https://playwright.dev/python/docs/ci#github-actions "Direct link to GitHub Actions")

#### On push/pull_request[​](https://playwright.dev/python/docs/ci#on-pushpull_request "Direct link to On push/pull_request")

Tests will run on push or pull request on branches main/master. The [workflow](https://docs.github.com/en/actions/using-workflows/about-workflows) will install all dependencies, install Playwright and then run the tests.

.github/workflows/playwright.yml

`name: Playwright Testson:  push:    branches: [ main, master ]  pull_request:    branches: [ main, master ]jobs:  test:    timeout-minutes: 60    runs-on: ubuntu-latest    steps:    - uses: actions/checkout@v5    - name: Set up Python      uses: actions/setup-python@v6      with:        python-version: '3.13'    - name: Install dependencies      run: |        python -m pip install --upgrade pip        pip install -r requirements.txt    - name: Ensure browsers are installed      run: python -m playwright install --with-deps    - name: Run your tests      run: pytest --tracing=retain-on-failure    - uses: actions/upload-artifact@v5      if: ${{ !cancelled() }}      with:        name: playwright-traces        path: test-results/`

#### Via Containers[​](https://playwright.dev/python/docs/ci#via-containers "Direct link to Via Containers")

GitHub Actions support [running jobs in a container](https://docs.github.com/en/actions/using-jobs/running-jobs-in-a-container) by using the [`jobs.<job_id>.container`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idcontainer) option. This is useful to not pollute the host environment with dependencies and to have a consistent environment for e.g. screenshots/visual regression testing across different operating systems.

.github/workflows/playwright.yml

`name: Playwright Testson:  push:    branches: [ main, master ]  pull_request:    branches: [ main, master ]jobs:  playwright:    name: 'Playwright Tests'    runs-on: ubuntu-latest    container:      image: mcr.microsoft.com/playwright/python:v1.58.0-noble      options: --user 1001    steps:      - uses: actions/checkout@v5      - name: Set up Python        uses: actions/setup-python@v6        with:          python-version: '3.13'      - name: Install dependencies        run: |          python -m pip install --upgrade pip          pip install -r local-requirements.txt          pip install -e .      - name: Run your tests        run: pytest`

#### On deployment[​](https://playwright.dev/python/docs/ci#on-deployment "Direct link to On deployment")

This will start the tests after a [GitHub Deployment](https://developer.github.com/v3/repos/deployments/) went into the `success` state. Services like Vercel use this pattern so you can run your end-to-end tests on their deployed environment.

.github/workflows/playwright.yml

`name: Playwright Testson:  deployment_status:jobs:  test:    timeout-minutes: 60    runs-on: ubuntu-latest    if: github.event.deployment_status.state == 'success'    steps:    - uses: actions/checkout@v5      uses: actions/setup-python@v6      with:        python-version: '3.13'    - name: Install dependencies      run: |        python -m pip install --upgrade pip        pip install -r requirements.txt    - name: Ensure browsers are installed      run: python -m playwright install --with-deps    - name: Run tests      run: pytest      env:        # This might depend on your test-runner        PLAYWRIGHT_TEST_BASE_URL: ${{ github.event.deployment_status.target_url }}`

### Docker[​](https://playwright.dev/python/docs/ci#docker "Direct link to Docker")

We have a [pre-built Docker image](https://playwright.dev/python/docs/docker) which can either be used directly or as a reference to update your existing Docker definitions. Make sure to follow the [Recommended Docker Configuration](https://playwright.dev/python/docs/docker#recommended-docker-configuration) to ensure the best performance.

### Azure Pipelines[​](https://playwright.dev/python/docs/ci#azure-pipelines "Direct link to Azure Pipelines")

For Windows or macOS agents, no additional configuration is required, just install Playwright and run your tests.

For Linux agents, you can use [our Docker container](https://playwright.dev/python/docs/docker) with Azure Pipelines support [running containerized jobs](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/container-phases?view=azure-devops). Alternatively, you can use [Command line tools](https://playwright.dev/python/docs/browsers#install-system-dependencies) to install all necessary dependencies.

For running the Playwright tests use this pipeline task:

`trigger:- mainpool:  vmImage: ubuntu-lateststeps:- task: UsePythonVersion@0  inputs:    versionSpec: '3.13'  displayName: 'Use Python'- script: |    python -m pip install --upgrade pip    pip install -r requirements.txt  displayName: 'Install dependencies'- script: playwright install --with-deps  displayName: 'Install Playwright browsers'- script: pytest  displayName: 'Run Playwright tests'`

#### Azure Pipelines (containerized)[​](https://playwright.dev/python/docs/ci#azure-pipelines-containerized "Direct link to Azure Pipelines (containerized)")

`trigger:- mainpool:  vmImage: ubuntu-latestcontainer: mcr.microsoft.com/playwright/python:v1.58.0-noblesteps:- task: UsePythonVersion@0  inputs:    versionSpec: '3.13'  displayName: 'Use Python'- script: |    python -m pip install --upgrade pip    pip install -r requirements.txt  displayName: 'Install dependencies'- script: pytest  displayName: 'Run tests'`

### CircleCI[​](https://playwright.dev/python/docs/ci#circleci "Direct link to CircleCI")

Running Playwright on CircleCI is very similar to running on GitHub Actions. In order to specify the pre-built Playwright [Docker image](https://playwright.dev/python/docs/docker), simply modify the agent definition with `docker:` in your config like so:

`executors:  pw-noble-development:    docker:      - image: mcr.microsoft.com/playwright/python:v1.58.0-noble`

Note: When using the docker agent definition, you are specifying the resource class of where playwright runs to the 'medium' tier [here](https://circleci.com/docs/configuration-reference?#docker-execution-environment). The default behavior of Playwright is to set the number of workers to the detected core count (2 in the case of the medium tier). Overriding the number of workers to greater than this number will cause unnecessary timeouts and failures.

### Jenkins[​](https://playwright.dev/python/docs/ci#jenkins "Direct link to Jenkins")

Jenkins supports Docker agents for pipelines. Use the [Playwright Docker image](https://playwright.dev/python/docs/docker) to run tests on Jenkins.

`pipeline {   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.58.0-noble' } }   stages {      stage('e2e-tests') {         steps {            sh 'pip install -r requirements.txt'            sh 'pytest'         }      }   }}`

### Bitbucket Pipelines[​](https://playwright.dev/python/docs/ci#bitbucket-pipelines "Direct link to Bitbucket Pipelines")

Bitbucket Pipelines can use public [Docker images as build environments](https://confluence.atlassian.com/bitbucket/use-docker-images-as-build-environments-792298897.html). To run Playwright tests on Bitbucket, use our public Docker image ([see Dockerfile](https://playwright.dev/python/docs/docker)).

`image: mcr.microsoft.com/playwright/python:v1.58.0-noble`

### GitLab CI[​](https://playwright.dev/python/docs/ci#gitlab-ci "Direct link to GitLab CI")

To run Playwright tests on GitLab, use our public Docker image ([see Dockerfile](https://playwright.dev/python/docs/docker)).

`stages:  - testtests:  stage: test  image: mcr.microsoft.com/playwright/python:v1.58.0-noble  script:  ...`

## Caching browsers[​](https://playwright.dev/python/docs/ci#caching-browsers "Direct link to Caching browsers")

Caching browser binaries is not recommended, since the amount of time it takes to restore the cache is comparable to the time it takes to download the binaries. Especially under Linux, [operating system dependencies](https://playwright.dev/python/docs/browsers#install-system-dependencies) need to be installed, which are not cacheable.

If you still want to cache the browser binaries between CI runs, cache [these directories](https://playwright.dev/python/docs/browsers#managing-browser-binaries) in your CI configuration, against a hash of the Playwright version.

## Debugging browser launches[​](https://playwright.dev/python/docs/ci#debugging-browser-launches "Direct link to Debugging browser launches")

Playwright supports the `DEBUG` environment variable to output debug logs during execution. Setting it to `pw:browser` is helpful while debugging `Error: Failed to launch browser` errors.

`DEBUG=pw:browser pytest`

## Running headed[​](https://playwright.dev/python/docs/ci#running-headed "Direct link to Running headed")

By default, Playwright launches browsers in headless mode. See in our [Running tests](https://playwright.dev/python/docs/running-tests#run-tests-in-headed-mode) guide how to run tests in headed mode.

On Linux agents, headed execution requires [Xvfb](https://en.wikipedia.org/wiki/Xvfb) to be installed. Our [Docker image](https://playwright.dev/python/docs/docker) and GitHub Action have Xvfb pre-installed. To run browsers in headed mode with Xvfb, add `xvfb-run` before the actual command.

`xvfb-run pytest`
