# Source: https://docs.mystic.ai/docs/teams.md

# Teams

Collaborate with others in a team

Teams allow users to view, edit and use shared pipelines, BYOC clusters and more. Each user has a role within a team that grants them certain privileges and access to the features on [mystic.ai](https://mystic.ai).

# Creating a team

Creating a team is simple. Navigate to your user drop down, and click create team. Fill in the fields as desired.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2f92fa1-Screenshot_2024-05-23_at_13.14.46.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

Once created, you can switch to the team context through the same dropdown menu, which will allow you to create runs, pipelines, clusters, etc. through a team that will be visible to others in the team.

You can also manage your team on the Teams settings page. This page allows you to add additional team members, change their roles, change team settings, etc.

To perform API requests in a team context, you can create a new API token through the usual process, in that team's context.

# Billing

Each team has its own billing profile which can be managed by the owner of the team through the usual interface. any pipeline runs or add-ons will incur charges to the team billing profile, not the users - as long as the user performs those actions in the team context.

# User roles

Each user has role in a team. By default, the user that creates a team has the owner role. The other roles are:

* admin
* developer
* viewer

You can change a member's role from the team settings page.

The viewer role only grants read access to resources, and prevents any editing or deleting.

Developers are able to perform create and and edit requests on most resources such as pipelines, runs and clusters.

Admins inherit developer permissions and are also able to delete resources, as well as edit team settings.

Lastly owners are able to delete teams, and are the only users that can create or edit cloud credentials for BYOC integration.

# Performing actions within a team

Like most resources, API tokens are specific to a team. Creating a token for a team and authenticating with it therefore allows you to perform usual actions like uploading pipelines and performing runs, through the team.

To create a token for the team, make sure you select your team context from the dropdown menu in the top right of the dashboard. Then navigate to Developers -> API Tokens, and click the Create Token button.

Once the token is created you can authenticate with it as normal through a command such as:

`pipeline cluster login team-mystic-api MY_TEAM_TOKEN -u https://www.mystic.ai -a`