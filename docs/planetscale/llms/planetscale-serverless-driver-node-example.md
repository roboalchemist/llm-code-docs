# Source: https://planetscale.com/docs/vitess/tutorials/planetscale-serverless-driver-node-example.md

# Node.js example using the PlanetScale serverless driver

> This guide will cover how to use the provided Node.js sample application using the PlanetScale serverless driver for JavaScript.

## Overview

<Note>
  This guide will be using VS Code as the IDE, but you may use your preferred IDE.
</Note>

## Use the sample repository

We offer a sample repository that can be used as an educational resource. It is an Express API that can be run locally with sample `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements mapped to the proper API endpoints.

To follow along, you’ll need the following:

* A PlanetScale account, as well as knowing how to create a database.
* The PlanetScale CLI is installed on your computer, which will be used to seed data.

Start by creating a database in PlanetScale by clicking **"New database"** > **"Create new database"**.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c498f865bb460d39374b40aa0d0c9f5e" alt="How to create a new database. priority" data-og-width="1604" width="1604" data-og-height="825" height="825" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6ba0a2413fa5c5b8d8a6eab6695c7ed3 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=072bebd5e88951b1a9c40876d3256b21 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6971bb21d99e5993a6b8495f27335440 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=5f9290f26dd8697d532adc60c11033e8 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=fdf571502d7224b8dbd096aa06e0f5fc 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/how-to-create-a-new-database-2.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=1e6ed9155a19c7e37cecd9459c60b9fa 2500w" />
</Frame>

Name the database `travel_db`. Click **"Create database"**. Wait for the database to finish initializing before moving on.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8581222d3e5be6da8671460a14a4dd31" alt="The travel_db initializing." data-og-width="3490" width="3490" data-og-height="1144" height="1144" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=0f584bc7a8f23915f2a74bff0e42156c 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d3db45498496e194383b146d895e7b6d 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=d16fc1daa20742f695b053849365d6d6 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=a38bf28ff2741360175e8a5aaa900f37 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=af6f7566a850750db1175ef0c42ee839 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/initializing.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=fa407b86be8240b3489d7e29db36b748 2500w" />
</Frame>

Generate a set of credentials by clicking the **"Connect"** button.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=03865ddef1ce2c082d0988a0ae14f1a7" alt="The Connect button in the PlanetScale dashboard." data-og-width="3494" width="3494" data-og-height="1078" height="1078" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ec43ffb42a8c8ca24bf755ee89c24ec9 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=bc2c4e32abf80f10808d1a7733b7c2eb 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6f99c1a695581319b6ad8aecbb1014d0 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=a8c772b9413aef4dc952b21a5cda167e 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=8c7252745f5e5a1dba80447221207042 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-connect-button-in-the-planetscale-dashboard.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=59b71b28a3bc48a1e72489ba0ea245a3 2500w" />
</Frame>

Copy your password credentials first:

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7891a38fffcd855a7f8b4361bae2e6b3" alt="The password details." data-og-width="3498" width="3498" data-og-height="1118" height="1118" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=487986ba44c9e925e50505ea6239eb7c 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=6b7d27c21a9b792d8ade9db1bcd24180 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=fa598f2f16d18b462ea5266a65b36141 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=1936b2e9146bb188adbd0282f39c8e46 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c2ddbead3b61cdb65401a51198458ed8 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9c69974c751ed28d91c7995c1025a4c1 2500w" />
</Frame>

Scroll down and select **"database-js"** from the "Select your language or framework" options. Copy the text from the **".env"** section, as we'll be putting this in the project after it's pulled down from GitHub.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=622d7b1deca3f77fafec63775742caad" alt="The password env details." data-og-width="3496" width="3496" data-og-height="618" height="618" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=9f9983feac3311480ce6b167292223cb 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7020db0bd4442ea094d25ea789f2d18b 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=c11cede2439a0acab38ead59bf1c6092 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=47f1ab272b2ab8e76d9cb73a7b02e967 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=46d4352255fac2e718d05787c0ae9ed1 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/the-serverlessjs-connect-modal-env.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=f28174b61ece42508546aee7e3454559 2500w" />
</Frame>

On your workstation, open a terminal and clone the repository to your computer by running the following command:

```bash  theme={null}
git clone https://github.com/planetscale/database-js-starter
```

Navigate to the `scripts` folder and run the `seed_database.sh` script to populate a small database simulating a travel agency.

```bash  theme={null}
cd database-js-starter/scripts
./seed-database.sh
```

<Note>
  If you are using Windows, run this command through the [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/)
</Note>

Create a new file named `.env` in the root of the project and paste in the sample provided from PlanetScale that you copied earlier.

To run the project, run the following commands from the root of the project.

```bash  theme={null}
npm install
npm start
```

If the project is running properly, you should receive a message stating that the API is running.

The `tests.http` file is designed to work with the [VS Code Rest Client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client), but can be used as a reference when testing with the tool of your choosing. If you are using the plugin, you may click the **"Send request"** button that appears above each request to see the API in action.

<Frame>
    <img src="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=278a59dab18c19f67f075a275fcb0691" alt="An example of a POST request to the sample project." data-og-width="860" width="860" data-og-height="310" height="310" data-path="docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?w=280&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=49f55ad87b30ef8ddddd2cac501e0e60 280w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?w=560&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=7049d0e1d996f3ddf5e54234a28b3889 560w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?w=840&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=ea3d665a9d45e25e6736a2f9a6aab1b2 840w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?w=1100&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=39e4d13a9d9635aa72ab0a48650bf7db 1100w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?w=1650&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=91b173e646538f38c8ea0964ebfb40fc 1650w, https://mintcdn.com/planetscale-cad1a68a/FWWWKZleEvIA3gmW/docs/images/assets/docs/tutorials/planetscale-serverless-driver-node-example/an-example-of-a-post-request-to-the-sample-project.png?w=2500&fit=max&auto=format&n=FWWWKZleEvIA3gmW&q=85&s=74f69c690c3aa96f20b12836ea0240d5 2500w" />
</Frame>

If you check the terminal where the API was started, the response from the `execute` function is logged out for review.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt