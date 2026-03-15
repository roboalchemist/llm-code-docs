# Source: https://help.aikido.dev/getting-started/core-functionalities/enable-slas-in-aikido.md

# Enable SLAs in Aikido

## Enable SLAs in Aikido

You can enable SLA settings in Aikido to automatically assign due dates to tickets. This facilitates a structured and timely approach to issue resolution based on their reported time and severity.

#### Detection and SLA Reset Logic <a href="#how-to-enable-slas-in-aikido" id="how-to-enable-slas-in-aikido"></a>

* SLA countdown starts the moment Aikido first detects the issue and are measured in calendar days, not business days
* When the severity of an issue is manually changed, the SLA date resets.
* When an issue is unsnoozed, the SLA date resets.
* When an issue is unignored, the SLA date resets.

#### How to enable SLAs in Aikido <a href="#how-to-enable-slas-in-aikido" id="how-to-enable-slas-in-aikido"></a>

1. Navigate to the Settings -> [SLA settings](https://app.aikido.dev/settings/sla)
2. Ensure the 'Enable SLAs' option is turned on to implement SLA rules.\
   ​

   ![Set and enable SLAs per severity to manage vulnerabilities and notify stakeholders via Slack.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f93ecd6cd8d715bea613c848c784fda38a7260e2%2Fenable-slas-in-aikido_1ff28d9b-3344-4de1-bcfd-f50e669ab680.png?alt=media)
3. Input the **number of days** for resolution in the fields for Critical, High, Medium, and Low priority issues to establish SLA time frames.\
   ​

   ![Issue resolution deadlines by priority: critical (5 days), high (20), medium (60), low (100).](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8cd7d0b03d924c45304bbf39e83cd6592d71ad71%2Fenable-slas-in-aikido_c1e31d14-d808-4f55-a853-117c72d67aba.png?alt=media)

   ​
4. Set up the '**Due Soon' notification threshold** by specifying the number of days before the SLA deadline, which will highlight impending due dates on the [SLA Due Soon](https://app.aikido.dev/queue?filter=due_soon) view.\
   ​

   ![Set the 'Due Soon' issue status by days before the SLA deadline.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8df4724d3cbe60f6148b02c611be9fdc39ec56a5%2Fenable-slas-in-aikido_e8abe17c-281e-4a5f-9947-3caf00ca1536.png?alt=media)
5. Click **'Save'** to apply these configurations.

#### SLA Information in Aikido UI <a href="#sla-information-in-aikido-ui" id="sla-information-in-aikido-ui"></a>

After setting up your SLA parameters, here's how you can monitor your SLA due dates.

* **Sidebar Information**: Next to each subissue in the sidebar, you will see the SLA information, providing a quick reference to gauge urgency. Hover over the label in order to view the date.\
  ​

  ![NodeGoat subissues list with priorities, due dates, authors, and commit links.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-f8dfd18aeef9f2f73ab8ed912d1c03846cefe425%2Fenable-slas-in-aikido_9b8a2056-6d6a-4314-a7cc-3efff950ad43.png?alt=media)
* **SLA Due Soon Filter**: The [**SLA Due Soon**](https://app.aikido.dev/queue?filter=due_soon) view view displays issues that are close to breaching the SLA, based on the threshold set. **Enable this filtered view** by clicking the Filter Icon on your Feed and select SLA Due Soon.\
  ​

  ![Security vulnerabilities dashboard showing severity, status, and assignment for identified software issues.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-08454e035e1cfc5cc11a90a388476bddd7d5fb78%2Fenable-slas-in-aikido_b8bdc36a-51a0-4742-9ec8-ce0d1dc6cc90.png?alt=media)
* **Out of SLA View**: The [**Out of SLA**](https://app.aikido.dev/queue?filter=out_of_sla) view lists all issues and subissues that have exceeded their SLA limits. **Enable this filtered view** by clicking the Filter Icon on your Feed and select Out of SLA.\
  ​

  ![Critical vulnerabilities dashboard showing unassigned open tasks and their fix times.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-efacf0999b36f0f471bf1cc0265efff45b4597c7%2Fenable-slas-in-aikido_ba292c16-3b12-456a-b0a4-5e118b7638c8.png?alt=media)

***
