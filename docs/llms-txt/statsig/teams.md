# Source: https://docs.statsig.com/access-management/teams.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Teams

<Info>
  Teams are an Enterprise-only feature. If you are on the Developer or Pro tiers, this guide will not apply to you. To upgrade to Enterprise, feel free to reach out to our team [here](https://www.statsig.com/contact/demo).
</Info>

## Overview

For larger organizations, the Teams feature enables an organizational and settings/ permissions layer on top of a Project. Teams are configured at the Project (not Organization) level, and are default-editable by all Project Admins.

Once teams are configured and a user is assigned to a team, any config (gates/ experiments/ metrics, etc.) they create will be associated with the team they belong to, and will inherit the settings of that team. Users who are members of multiple teams will have the choice of which team to associate their config with at creation time.

## Creating Teams

To create a team, navigate to **Settings** -> **People** -> **Teams**. Create a new team via the **+Create** button, where you'll be asked to name the team and add members. You can add/ remove members from a team at any time, not just at initial team creation.

Each team has a **Members** page and a **Settings** page. Within **Members** you can see all members of the team, including the team members project role and team role (which can be member or admin). Team members can be promoted or removed.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/la4FaREqFx2hg5ox/images/team_create_1.png?fit=max&auto=format&n=la4FaREqFx2hg5ox&q=85&s=55e417814a23c379e49a7b8b254ce335" alt="Statsig Teams page showing member list with project and team roles" width="2760" height="1476" data-path="images/team_create_1.png" />
</Frame>

## Configuring Team Settings

At the Project-level, you can require all config creations are associated with a team via the "Require teams" setting under **Settings** -> **Product Configuration** -> **General**. Note that this will block anyone who isn't yet assigned to a team from creating a config, so should only be enabled after all members of the project have been added to (at least) one team.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/d11ed451-7fff-4031-b117-4cd05cb3b960.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=64190730b52da75a5b01d975bf5dfe68" alt="Project configuration toggle requiring configs to be associated with teams" width="1103" height="92" data-path="images/access-management/teams/d11ed451-7fff-4031-b117-4cd05cb3b960.png" />
</Frame>

Within each team, there are a number of settings you can configure:

**Default Monitoring Metrics/ Scorecard Metrics:** This setting enables pre-configuration of a set of metrics to add to every new gate/ experiment/ holdout at the team level. These might be a mix of top-line company metrics every team must monitor (e.g. revenue/ app performance), as well as a set of team-specific KPIs all rollouts and experiments should be tracking.

<Frame>
  <img width="881" alt="Statsig Team settings showing default monitoring metrics selection" src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/16f0ccfd-05d6-4fb2-8992-ec8780ff3778.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=c41575d870ae7e34f9997c746c79e1f1" data-path="images/access-management/teams/16f0ccfd-05d6-4fb2-8992-ec8780ff3778.png" />
</Frame>

**Require Reviews:** If reviews are not already required at the Project-level, this setting enables you to require reviews at the individual team level. Note that this setting won't appear if you're already requiring reviews at the Project level (controlled via **Settings** -> **Product Configuration** -> **Reviews**).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/554e0f6a-c9ce-466a-b5a4-db94b0cb24fa.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=15bc9a74b889246f1283929852ca1013" alt="Team require reviews option within settings" width="1171" height="297" data-path="images/access-management/teams/554e0f6a-c9ce-466a-b5a4-db94b0cb24fa.png" />
</Frame>

**Default Allowed Reviewers:** This setting enables more granular control of *who* is allowed to review and approve changes to a team's configs. There are three options here- "Anyone in the Project" (least restrictive), "Team Members Only" (keep reviews within the team), and "Team or Project Admins Only" (most restrictive).

Note that team-based review configurations layer on top of [role-based review settings](/guides/setting-up-reviews#enforcing-team-reviews). For example, if your role has permission to approve reviews and your team has review settings set to “Team members only”, then an approver would need to both be in a role with review approval permission AND be on the team to approve a review pending for that team’s config.

<Frame>
  <img width="924" alt="Default allowed reviewers dropdown specifying who can approve changes" src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/39263840-cb37-4286-b30a-c6d255f218d0.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=570ddbc6d0eb3996fe7d089b3fb1b312" data-path="images/access-management/teams/39263840-cb37-4286-b30a-c6d255f218d0.png" />
</Frame>

**Create/ Edit Configs and Metrics:** This setting dictates which members of a team are allowed to edit or create configs tagged with the team. There are two options here- "Anyone in the Project" (no restrictions, anyone can edit the team's configs), or "Team Members Only".

<Frame>
  <img width="919" alt="Create and edit configs permissions for team members only or entire project" src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/df517c17-acdd-4516-a9ee-bc612a0bfdc9.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=78d1ede16bc685f1303c3287fd96861f" data-path="images/access-management/teams/df517c17-acdd-4516-a9ee-bc612a0bfdc9.png" />
</Frame>

**Default Target Applications:** This setting will auto-apply any assigned Target Applications to all configs created that are associated with this team. Note that this only impacts which Target Applications are added to the config by default at creation time, but can be edited/ overridden as needed.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/2cf75c17-9441-4645-beef-feb57578fb46.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=0ff069b5a9528ebef82911de1b73ae80" alt="Team default target applications selector" width="1098" height="241" data-path="images/access-management/teams/2cf75c17-9441-4645-beef-feb57578fb46.png" />
</Frame>

**Default Holdout:** It's a common use-case for teams to want to measure cumulative impact of their new features/ experiments over the course of a Quarter/ Half, etc. To make this easier and more automatic, you can associate a default Holdout to a team. This will cause all subsequent configs associated with the team will be auto-added to this default Holdout.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/8f5a2226-c716-4882-939a-8ba53e852b22.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=94c442acfc0253d7fc76b5985804e9c5" alt="Team default holdout configuration UI" width="1165" height="268" data-path="images/access-management/teams/8f5a2226-c716-4882-939a-8ba53e852b22.png" />
</Frame>

## How Teams are Used Throughout the Console

Once a user is associated with a team, every config they create will now be default-associated with their team. For users on multiple teams, they will be able to choose which team to associate their config with at creation time. This will apply the team’s relevant settings to that config.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/dbdc681d-3918-4da1-b9e3-6e43ecb744f8.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=e51974cf9ef19bf58743b3c003f36e16" alt="Config creation screen with team selection dropdown" width="1405" height="1042" data-path="images/access-management/teams/dbdc681d-3918-4da1-b9e3-6e43ecb744f8.png" />
</Frame>

Every config will have a field in the header for “Team”. This field is separate from “Owner"- whereby "Owner" is a single individual, "Team" is a group of individuals and will not automatically update if, for example, the Owner moves to a different team within the organization. Teams must be manually changed (subject to the review requirements) at the config level.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/7fc0faf7-c059-451b-8a44-6f58e526ef8e.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=b8bb73cfd935a9642c75dbdf22cfdce3" alt="Config header showing Team field separate from Owner" width="1286" height="193" data-path="images/access-management/teams/7fc0faf7-c059-451b-8a44-6f58e526ef8e.png" />
</Frame>

Finally, with the addition of teams, every user can now filter Gate/ Experiment/ Metric lists and the Home Feed by team. The Home Feed will default to a user's team(s), ensuring the most relevant content is surfaced.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/SnkiaVI10G4C2tMJ/images/access-management/teams/299cc0ad-5878-454b-9186-e005f8f442b5.png?fit=max&auto=format&n=SnkiaVI10G4C2tMJ&q=85&s=1e076e10554ab4dda64939ad2bf5538d" alt="Console list filters for gates experiments and metrics by team" width="1404" height="961" data-path="images/access-management/teams/299cc0ad-5878-454b-9186-e005f8f442b5.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).