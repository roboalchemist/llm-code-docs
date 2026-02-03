# Run Postman Collections in your CI environment using Newman

You can use [Newman](/docs/collections/using-newman-cli/command-line-integration-with-newman/) and the [Postman API](https://api.postman.com/) to run Postman Collections in your continuous integration (CI) environment. First install Node.js and Newman in your CI environment. You can then use Newman to get and run your collection using the Postman API.

## Prerequisites

Before you begin, check the following prerequisites for running collections using Newman and the Postman API:

* Make sure you have a CI system setup that can run shell commands and that you have edit access.
* [Generate a Postman API key](/docs/developer/postman-api/authentication/#generate-a-postman-api-key), and copy it for later use.
* Make sure you have a Postman Collection that tests your localhost server, and copy the collection ID for later use. If your collection needs an environment, copy the environment ID for later use.

**Developing an API?** Postman offers built-in tools to integrate your API with some of the most popular continuous integration (CI) tools. After you set up CI for your API, you can view the status of builds or start a new build, all from within Postman. You can also use Newman to run API tests as part of your CI pipeline. To learn more, see [CI integrations](/docs/integrations/ci-integrations/).

## Install Newman and Node.js

To learn how to install Newman and Node.js, see [Install and run Newman](/docs/collections/using-newman-cli/installing-running-newman/).

You don't need to install Node.js if your CI environment already has it installed.

## Run a collection using Newman and the Postman API

To run a collection using Newman and Postman API, use the following command:

```bash
newman run "https://api.getpostman.com/collections/collection-id?apikey=postman-api-key"
```

If you need to provide an environment to the collection, add the `--environment` option with the appropriate parameters to the Newman command:

```bash
newman run "https://api.getpostman.com/collections/collection-id?apikey=postman-api-key"
--environment "https://api.getpostman.com/environments/environment-id?apikey=postman-api-key"
```

Learn more about [using Newman with the Postman API](https://github.com/postmanlabs/newman?tab=readme-ov-file#using-newman-with-the-postman-api).