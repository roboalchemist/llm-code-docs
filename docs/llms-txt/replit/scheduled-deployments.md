# Source: https://docs.replit.com/cloud-services/deployments/scheduled-deployments.md

# Scheduled Deployments

> Scheduled deployments run your Replit App tasks on a schedule with minimal setup.

Define a command-line operation and a schedule, and Replit runs it automatically
in your Replit App's environment. After completion, the operation terminates until the
next scheduled run.

Scheduled deployments, also known as scheduled jobs, work best for handling periodic tasks
such as checking status, sending notifications, and starting backups. They are not designed
for continuous or long-running tasks such as web applications.

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=bbc6ef88e692b2fbe28b42f205b3b665" alt="Scheduled Deployments" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/deployments/scheduled/scheduled-deployments.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2c183fbd4a8f25180236d3b7e95569a1 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=eb8d2fc8b688a071f182bd7437148795 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=24c480817879d80901484979573a7182 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=d3cc6463cc4197ff67127869732d4269 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=622562da0027c1249413b20e6effd087 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployments.jpg?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=b8dfcfb4379c26e880d590832512cd98 2500w" />
</Frame>

## Features

Scheduled deployments include the following features:

* **Automatic scheduling**: Schedule your task, and Replit runs it automatically.
* **Natural language scheduling**: Enter a human-readable description of the schedule, and AI converts it into a cron expression, a computer-readable schedule format.
* **Error alerts**: Receive notifications when your scheduled task fails.
* **Monitoring**: View logs and monitor your scheduled deployment's status.

## Usage

You can access scheduled deployments in the Deployments workspace tool.

The following sections guide you through setting up and managing your scheduled deployments.

<Accordion title="How to access Scheduled Deployments">
  From the left **Tool dock**:

  1. Select <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5b2c72713cc17ac272098bcbfd624d84" alt="All tools icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-all-tools-button.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=284639f38f8e91da05d14611e44a9ae6 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d0e802a9c50a81e5c825cf1ddce00a64 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=b5c4e38a7cf923221d2412e904bbdc94 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=3b43a87adf314fbb300376b404ab8a22 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a11f8a405c4156ff625219a372c2ceca 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-all-tools-button.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=7c86d2f1bfa4611aeca168daf29d08ff 2500w" /> **All tools** to see a list of workspace tools.
  2. Select <img class="icon-svg" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=df3fa2573b451c54591523c9d9111db1" alt="Deployments icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/deploy-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=115e9383e0350a6ef201a41f78f8a19a 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=667b93ae66d0b69569409fb90d9fc280 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ae927e5aadcb7a470ad726f0acb0f782 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=16ee8f7b3d9db6b4f74ea8c2ebb6730f 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ad04a5984543c13895fd30182294ec0a 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/deploy-icon.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=2449268bce371256727b17027eb180f3 2500w" /> **Deployments**.
  3. Select the **Scheduled** option and then select **Set up your published app**.

  From the **Search bar**:

  1. Select the <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=4a0eb8f6b17ff6761d53167334a68b30" alt="magnifying glass icon" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/workspace-search-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=baa20919b2c8e7db2fad2562c732edd0 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5fcfa3935da89ed6c1c6f893998c4f4a 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2a24f3fcc4dd990d9062598eab165cff 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a3258e068d5ead6bacadcbe6e5785575 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d08ebecb3063ed18a657beb563ac9c3c 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/workspace-search-icon.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e63dd2009929a4b375b86e44ed6d7732 2500w" /> magnifying glass at the top to open the search tool
  2. Type "Deployments" to locate the tool and select it from the results.
  3. Select the **Scheduled** option and then select **Set up your published app**.
</Accordion>

<Frame caption="Scheduled Job configuration screen in the Deployments tool">
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2a2c4a5e202f767336eae9fba99b5363" alt="Scheduled Deployment options" data-og-width="4052" width="4052" data-og-height="2040" height="2040" data-path="images/deployments/scheduled/scheduled-deployment-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=22479719d46482aa9986691093511770 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=8e03b302a2e438aa38128bbb443eb55d 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=1fdbdd7ebe598fd48dd8f4d416d0ae17 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=91ef9e3ca67e6ae1610ab412ab874ce9 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=47847f1278f8cfe005f19353fc8d78ac 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/scheduled/scheduled-deployment-options.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=e595c870a2836f8eda58b67cb978a3fe 2500w" />
</Frame>

### Machine configuration

This field lets you view the machine's CPU, RAM, and usage cost for your scheduled deployment.

### Schedule fields

* **Schedule description**: Enter a natural language description of the schedule, such as "Every Monday and Wednesday at 10 AM" or "March 24th, 2024 at 3 PM."
* **Cron expression**: Optionally, enter a computer-readable string that defines when the task should run.
* **Timezone selection**: Select the timezone for the schedule from the dropdown menu.

When you enter a value in the **Schedule description** or **Cron expression** field, AI translates it automatically to match.
To learn more about cron expressions, see the <a href="https://en.wikipedia.org/wiki/Cron" target="_blank">cron</a> Wikipedia page.

### Job timeout

Enter the maximum amount of time the job can run before the scheduler terminates it. Select either "minutes" or "hours from the time unit dropdown.

<Tip>
  Scheduled jobs may run slower than in the Replit App workspace. Test the
  deployment and adjust the timeout accordingly.
</Tip>

### Build command

Enter the shell command that compiles or sets up your app before running the Run command in the **Build command** field.
For example, to install your Node.js app dependencies, you might add the `npm install` build command.

The build command time does not count toward your usage and is not counted against the job timeout.

### Run command

Enter the shell command that launches your task in the **Run command** field.
For example, to run a Python script, you might add `python app.py` as the run command.

The Replit scheduler executes the run command at the scheduled times.
The time it takes to run the command counts toward your usage. For more information on usage billing,
see the [Scheduled Deployments section](/billing/deployment-pricing#scheduled-deployments) in our pricing documentation.

### Deployment secrets

Select **Add deployment secret** to add environment variables or secrets your app needs to run securely.

If your Replit App has environment variables or secrets, the Deployment tool adds them to the list automatically.

To edit the values of an environment variable select the

<img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d6ac2757eaf25e61d31ce51316ec91ad" width="16" height="16" alt="three vertical dots icon" data-og-width="24" data-og-height="24" data-path="images/icons/vertical-dots.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=cf215ef22f55bf163c0037f923584e37 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=9659b713156cc159f2b9107450cc0fbd 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=73cb1af8587233823aba8f0aec72d1d9 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5d633ba6d10d1d6d6d179b3086869257 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=5255815ba3d626d74ede11e23698ccbd 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/vertical-dots.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=15dffd4252b85614141c73a628671cf1 2500w" /> vertical dots and choose **Edit** from the menu. The Secrets manager only applies
value to the deployment and does not change environment variables defined in your
Replit App.

## Next steps

To learn more about deployments, see the following resources:

* [Published App Monitoring](/cloud-services/deployments/monitoring-a-deployment): Learn how to view logs and monitor your published app.
* [Publishing costs](/billing/deployment-pricing): View the costs associated with publishing.
* [Pricing](https://replit.com/pricing): View the pricing and allowances for each plan type.
* [Usage Allowances](/billing/about-usage-based-billing): Learn about scheduled deployment usage limits and billing units.
* [Create a HackerNews Slack bot](https://docs.replit.com/getting-started/quickstarts/webscrape-and-slack-notifications): Learn how to create a Slack bot that checks a website for new content and sends you notifications on a schedule.
