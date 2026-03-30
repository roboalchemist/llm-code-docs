# Source: https://docs.jit.io/docs/teams.md

# Dev UX in Jit: Team Analytics

## Overview of Jit Teams

Jit Teams provides a dedicated security portal for each development team to understand the security posture of their services. It is based on the configuration of your team structure in GitHub and GitLab, which is imported during your [GitHub integration](https://docs.jit.io/docs/integrating-with-github) or [GitLab integration](https://docs.jit.io/docs/integrating-with-gitlab) step.

To view an individual team, select it from the list.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2e46eee-Frame_281674.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Viewing team data

Each team page shows a team score, list of associated resources, list of team members, and list of child teams. The team score is calculated by averaging the resource scores of all resources associated with the team. Resource scores are calculated as a percentage of passed plan items compared to the total number of plan items scanning the resource.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/59a0bfb-Frame_281681.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Viewing plan items

You can also view the individual plan items that make up the score for a resource by selecting the resource from the list. Select a plan item to view it in the [Backlog page](https://docs.jit.io/docs/backlog-page).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5a23b33-Frame_281680.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Configuring Slack notifications for teams

**To configure Slack notifications for a team—**

1. If you have not already done so, [Integrate with Slack](https://docs.jit.io/docs/integrating-with-slack).
2. Select the team you want to configure for Slack notifications from the Teams page.
3. Select **Set Slack Notification** in the top right corner of the page. The *Configure your Slack Integration* dialog opens.
4. Use the check boxes to select criteria for generating notifications. Use the dropdown menu to select the Slack channel where notifications will display.
5. Select **Done**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f5ca1be-Frame_281701.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]