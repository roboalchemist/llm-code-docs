# Source: https://docs.apify.com/platform/actors/development/deployment/continuous-integration.md

# Continuous integration for Actors

**Learn how to set up automated builds, deploys, and testing for your Actors.**

<!-- -->

***

Automating your Actor development process can save time and reduce errors, especially for projects with multiple Actors or frequent updates. Instead of manually pushing code, building Actors, and running tests, you can automate these steps to run whenever you push code to your repository.

You can automate Actor builds and tests using your Git repository's automated workflows like [GitHub Actions](https://github.com/features/actions) or [Bitbucket Pipelines](https://www.atlassian.com/software/bitbucket/features/pipelines).

Using Bitbucket?

Follow our step-by-step guide to set up continuous integration for your Actors with Bitbucket Pipelines: [Read the Bitbucket CI guide](https://help.apify.com/en/articles/6988586-setting-up-continuous-integration-for-apify-actors-on-bitbucket).

Set up continuous integration for your Actors using one of these methods:

*
*

Choose the method that best fits your workflow.

## Option 1: Trigger builds with a Webhook

1. Push your Actor to a GitHub repository.

2. Go to your Actor's detail page in Apify Console, click on the API tab in the top right, then select API Endpoints. Copy the **Build Actor** API endpoint URL. The format is as follows:


   ```
   https://api.apify.com/v2/acts/YOUR-ACTOR-NAME/builds?token=YOUR-TOKEN-HERE&version=0.0&tag=beta&waitForFinish=60
   ```


   API token

   Make sure you select the correct API token from the dropdown.

3. In your GitHub repository, go to Settings > Webhooks > Add webhook.

4. Paste the API URL into the Payload URL field and add the webhook.

![GitHub integration](/assets/images/ci-github-integration-2ee82ac772eb3280155b7027a4259528.png)

Now your Actor will automatically rebuild on every push to the GitHub repository.

## Option 2: Set up automated builds and tests with GitHub Actions

1. Push your Actor to a GitHub repository.

2. Get your Apify API token from the [Apify Console](https://console.apify.com/settings/integrations)

   ![Apify token in app](/assets/images/ci-token-b623bba2addc8778a802a97aabda2ada.png)

3. Add your Apify token to GitHub secrets

   1. Go to your repository > Settings > Secrets and variables > Actions > New repository secret
   2. Name the secret and paste in your token

   ![Add Apify token to secrets](/assets/images/ci-add-token-ff0020fecc1f213927e24987c5145a61.png)

4. Add the Build Actor API endpoint URL to GitHub secrets

   1. Go to your repository > Settings > Secrets and variables > Actions > New repository secret

   2. In Apify Console, go to your Actor's detail page, click the API tab in the top right, and then select API Endpoints. Copy the **Build Actor** API endpoint URL. The format is as follows:

      API token

      Make sure you select the correct API token from the dropdown.


      ```
      https://api.apify.com/v2/acts/YOUR-ACTOR-NAME/builds?token=YOUR-TOKEN-HERE&version=0.0&tag=latest&waitForFinish=60
      ```


   3. Name the secret & paste in your API endpoint

      ![Add build Actor URL to secrets](/assets/images/ci-add-build-url-b1d008e3713646e5a9c26de2dc84ba4c.png)

5. Create GitHub Actions workflow files:

   1. In your repository, create the `.github/workflows` directory
   2. Add `latest.yml`. If you want, you can also add `beta.yml` to build Actors from the develop branch (or other branches).

   * latest.yml
   * beta.yml

   Use your secret names

   Make sure to use the exact secret names you set in the previous step.


   ```
   name: Test and build latest version
   on:
     push:
       branches:
         - master
         - main
   jobs:
     test-and-build:
       runs-on: ubuntu-latest
       steps:
         # Install dependencies and run tests
         - uses: actions/checkout@v2
         - run: npm install && npm run test
         # Build latest version
         - uses: distributhor/workflow-webhook@v1
           env:
             webhook_url: ${{ secrets.BUILD_ACTOR_URL }}
             webhook_secret: ${{ secrets.APIFY_TOKEN }}
   ```


   With this setup, pushing to the `main` or `master` branch tests the code and builds a new latest version.

   Use your secret names

   Make sure to use the exact secret names you set in the previous step.


   ```
   name: Test and build beta version
   on:
     push:
       branches:
         - develop
   jobs:
     test-and-build:
       runs-on: ubuntu-latest
       steps:
         # Install dependencies and run tests
         - uses: actions/checkout@v2
         - run: npm install && npm run test
         # Build beta version
         - uses: distributhor/workflow-webhook@v1
           env:
             webhook_url: ${{ secrets.BUILD_ACTOR_URL }}
             webhook_secret: ${{ secrets.APIFY_TOKEN }}
   ```


   With this setup, pushing to the `develop` branch tests the code and builds a new beta version.

## Conclusion

Setting up continuous integration (CI) for your Apify Actors ensures that CI automatically tests and builds your code whenever you push changes to your repository. This helps catch issues early and streamlines your deployment process, whether you're releasing to production or maintaining a beta branch.

You can also integrate directly with GitHub, check out the [official Apify GitHub integration documentation](https://docs.apify.com/platform/integrations/github.md).
