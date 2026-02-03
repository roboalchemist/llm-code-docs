# Source: https://docs.streamlit.io/develop/concepts/app-testing/automate-tests

# Automate your tests with CI

One of the key benefits of app testing is that tests can be automated using Continuous Integration (CI). By running tests automatically during development, you can validate that changes to your app don't break existing functionality. You can verify app code as you commit, catch bugs early, and prevent accidental breaks before deployment.

There are many popular CI tools, including GitHub Actions, Jenkins, GitLab CI, Azure DevOps, and Circle CI. Streamlit app testing will integrate easily with any of them similar to any other Python tests.

## GitHub Actions

Since many Streamlit apps (and all Community Cloud apps) are built in GitHub, this page uses examples from [GitHub Actions](https://docs.github.com/en/actions). For more information about GitHub Actions, see:

- [Quickstart for GitHub Actions](https://docs.github.com/en/actions/quickstart)
- [GitHub Actions: About continuous integration](https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration)
- [GitHub Actions: Build & test Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)

## Streamlit App Action

[Streamlit App Action](https://github.com/marketplace/actions/streamlit-app-action) provides an easy way to add automated testing to your app repository in GitHub. It also includes basic smoke testing for each page of your app without you writing any test code.

To install Streamlit App Action, add a workflow `.yml` file to your repository's `.github/workflows` folder. For example:

```yaml
# .github/workflows/streamlit-app.yml
name: Streamlit app

on:
  push:
    branches: ["main"]
  pull_request:
    branches: ["main"]

permissions:
  contents: read

jobs:
  streamlit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - uses: streamlit/streamlit-app-action@v0.0.3
        with:
          app-path: streamlit_app.py
```

Streamlit App Action does the following:

- Install `pytest` and install any dependencies specified in `requirements.txt`.
- Run the built-in app smoke tests.
- Run any other Python tests found in the repository.

If your app doesn't include `requirements.txt` in the repository root directory, you will need to add a step to install dependencies with your chosen package manager before running Streamlit App Action.

## Writing your own actions

The above is just provided as an example. Streamlit App Action is a quick way to get started. Once you learn the basics of your CI tool of choice, it's easy to build and customize your own automated workflows. This is a great way to improve your overall productivity as a developer and the quality of your apps.

## Working example

As a final working example example, take a look at our [streamlit/llm-examples Actions](https://github.com/streamlit/llm-examples/actions), defined in [this workflow file](https://github.com/streamlit/llm-examples/blob/main/.github/workflows/app-testing.yml).

[forum](https://docs.streamlit.io/develop/concepts/app-testing/automate-tests#forum)

### Still have questions?

Our [forums](https://discuss.streamlit.io) are full of helpful information and Streamlit experts.