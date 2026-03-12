# Source: https://docs.statsig.com/experiments/templates/decision-framework.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Decision Framework

A Decision Framework for experiment templates allows teams to standardize their interpretation of results and decision-making process. Once configured, it provides clear recommendations for which group to ship based on experimental outcomes. While the framework highlights recommended actions based on metric movements, it does not enforce any actions.

## Setup

To configure a Decision Framework, find your desired experiment template under **Settings** → [**Templates**](https://console.statsig.com/templates), then navigate to the **Decision Framework** tab. By selecting one primary metric and one or more guardrail metrics, you can choose a recommended action based on metric performance.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xPRxhrUTAr9IlDUC/images/templates/df_setup_3.png?fit=max&auto=format&n=xPRxhrUTAr9IlDUC&q=85&s=22be257db37b2f873f306871331bc0cb" alt="Team-level Templates Settings" width="677" height="339" data-path="images/templates/df_setup_3.png" />
</Frame>

Three different types of recommendations can be configured:

* **Rollout Winning Group**: An icon appears next to the winning group in the Make Decision button
* **Discuss**: A message appears on the experiment page recommending discussion before making a ship decision
* **Do Not Roll Out**: An icon appears next to the control group in the Make Decision button

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xPRxhrUTAr9IlDUC/images/templates/df_icon.png?fit=max&auto=format&n=xPRxhrUTAr9IlDUC&q=85&s=9fe3efb7b031d2141464e139716cb872" alt="recommendation" width="359" height="352" data-path="images/templates/df_icon.png" />
</Frame>

## Reviews for shipping negative results

Reviewers can be set up when a shipping decision doesn't align with the recommendations configured in the decision framework. All it takes is to toggle on "Require reviews when decision opposes recommended decision" and add reviewers in the following dialogue box.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xPRxhrUTAr9IlDUC/images/templates/df_review.png?fit=max&auto=format&n=xPRxhrUTAr9IlDUC&q=85&s=b2c630a8670a35d0e0f0b81bc3935518" alt="recommendation" width="2000" height="293" data-path="images/templates/df_review.png" />
</Frame>

Once set up, a reviewer will be required in the following situations:

* **Rollout Winning Group**: Shipping a treatment group that is not recommended
* **Discuss**: Shipping any treatment group
* **Do Not Roll Out**: No review will be required

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xPRxhrUTAr9IlDUC/images/templates/df_ship_review_2.png?fit=max&auto=format&n=xPRxhrUTAr9IlDUC&q=85&s=9b816e85e7d0de109b8e13ff119b346c" alt="recoomendation" width="901" height="966" data-path="images/templates/df_ship_review_2.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).