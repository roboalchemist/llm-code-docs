# Source: https://infisical.com/docs/integrations/platforms/pm2.md

> ## Documentation Index
> Fetch the complete documentation index at: https://infisical.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PM2

> How to use Infisical to inject environment variables and secrets with PM2 into a Node.js app

Prerequisites:

* Set up and add envars to [Infisical Cloud](https://app.infisical.com)
* [Install the CLI](/cli/overview)

## Initialize Infisical for your Node.js app

```bash  theme={"dark"}
# navigate to the root of your of your project
cd /path/to/project

# then initialize infisical
infisical init
```

## Create a bash or js script

<CodeGroup>
  ```bash infisical-run.sh theme={"dark"}
  infisical run -- npm start
  ```

  ```js infisical-run.js theme={"dark"}
  const spawn = require("child_process").spawn;

  const infisical = spawn("infisical", ["run", "--", "npm", "start"]);

  infisical.stdout.on("data", (data) => console.log(`${data}`));
  infisical.stderr.on("data", (data) => console.error(`${data}`));
  ```
</CodeGroup>

## Start your application as usual but with the script

<CodeGroup>
  ```bash infisical-run.sh theme={"dark"}
  pm2 start infisical-run.sh
  ```

  ```bash infisical-run.js theme={"dark"}
  pm2 start infisical-run.js
  ```
</CodeGroup>
