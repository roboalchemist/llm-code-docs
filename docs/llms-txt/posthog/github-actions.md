# Source: https://posthog.com/docs/error-tracking/upload-source-maps/github-actions.md

# Upload source maps with GitHub Actions - Docs

1.  1

    ## Prerequisites

    Required

    Uploading source maps with GitHub Actions requires your build to have already generated source maps. This action does not build your project, it only injects source map metadata into the built files and uploads them to PostHog. Make sure to run your production build first (for example, `npm run build`).

2.  2

    ## Use the GitHub action

    Required

    Add a workflow step to run the PostHog upload action after your build:

    YAML

    PostHog AI

    ```yaml
    name: Upload source maps to PostHog
    on:
      push:
        branches: [main]
    jobs:
      build_and_upload:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v6
          - uses: actions/setup-node@v4
            with:
              node-version: 20
              cache: npm
          - run: npm ci
          - run: npm run build
          # Inject and upload source maps using the PostHog action
          - name: Inject & upload source maps to PostHog
            uses: PostHog/upload-source-maps@v2
            with:
              directory: dist
              project-id: ${{ secrets.POSTHOG_PROJECT_ID }}
              api-key: ${{ secrets.POSTHOG_CLI_API_KEY }}
              # host: https://eu.posthog.com # Required only for EU cloud
              # release-name: my-awesome-project  # Optional; falls back to repo name
              # release-version: ${{ github.sha }}   # Optional; falls back to current commit SHA
    ```

    This step:

    -   Injects a `//# chunkId=...` comment into your built source files so PostHog can match them with uploaded source maps
    -   Uploads the source maps to your PostHog project

3.  3

    ## Inputs

    *Reference for action configuration*

    | Name | Required | Description |
    | --- | --- | --- |
    | directory | Yes | Directory containing built assets (for example, dist) |
    | project-id | Yes | PostHog project ID. Get it from your [project settings](https://app.posthog.com/settings/project#variables) |
    | api-key | Yes | Personal API key with error tracking write and organization read scopes. Get it from your [personal API key settings](https://app.posthog.com/settings/user-api-keys#variables) |
    | release-name | No | Release name. Defaults to the Git repository name when available |
    | release-version | No | Release version (for example, commit SHA). Defaults to current commit SHA when available |
    | host | No | PostHog host URL. Defaults to https://us.posthog.com. For EU cloud, set it to https://eu.posthog.com |

    We recommend storing `project-id` and `api-key` in GitHub Secrets (for example, `POSTHOG_PROJECT_ID` and `POSTHOG_CLI_API_KEY`).

4.  ## Verify upload and injection

    Checkpoint

    1.  Confirm symbol sets are present in PostHog after the workflow runs.

    [Check symbol sets in PostHog](https://app.posthog.com/settings/project-error-tracking#error-tracking-symbol-sets)

    2.  Confirm your served production files include an injected comment at the end of the file similar to:

    JavaScript

    PostHog AI

    ```javascript
    //# chunkId=0197e6db-9a73-7b91-9e80-4e1b7158db5c
    ```

5.  4

    ## Serve injected assets

    Required

    You must deploy the injected build artifacts to production. PostHog reads the injected `chunkId` metadata during error capture to resolve stack traces. If you deploy files that were not processed by the action, uploaded source maps cannot be used to unminify your stack traces.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better