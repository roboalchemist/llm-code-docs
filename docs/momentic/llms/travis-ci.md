# Source: https://momentic.ai/docs/ci/travis-ci.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Travis CI

The following example shows how to use Momentic with
[Travis CI](https://docs.travis-ci.com/).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `.travis.yml` in your repository with the following
contents:

```yaml .travis.yml theme={null}
language: node_js
node_js:
  - lts/*
install:
  - npm install
script:
  - npx momentic run
after_script:
  - npx momentic results upload test-results
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `MOMENTIC_API_KEY` environment variable to your Travis CI workflow.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/create-api-key.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=54eb9f3c01e00a3ae7d71996760dcd39" width="3616" height="2434" data-path="images/create-api-key.png" />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your Travis repository settings and scroll down to the Environment
   Variables section. Create a new variable called `MOMENTIC_API_KEY` and enter
   the value of your API key.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/ci/travis-variables.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=f79b45cabe2648253f3be60c649751df" width="1920" height="722" data-path="images/ci/travis-variables.png" />
</Frame>

3. Travis CI automatically loads environment variables stored in project
   settings into the CI environment. No modifications are necessary for the CI
   file.


Built with [Mintlify](https://mintlify.com).