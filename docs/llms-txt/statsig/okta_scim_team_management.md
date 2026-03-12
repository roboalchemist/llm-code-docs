# Source: https://docs.statsig.com/access-management/scim/okta_scim_team_management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta SCIM Team Management

## Import Existing Statsig Teams

<Note>
  Teams are specific Statsig groups that exist within projects. They are not shared across projects. They also have two possible roles: `Admin` and `Member`.
</Note>

## Setup

* Ensure you have some teams created in Statsig.
* Navigate to the Statsig Project and create a team if you have none.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/team_steps/step1-create-team.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=d0681c7d32957eb49c93fa9e75bd246d" alt="Statsig project team creation dialog showing fields for team name and members" width="3296" height="1824" data-path="images/okta_scim_steps/team_steps/step1-create-team.png" />
</Frame>

## Import Existing Groups

* In Okta, go to the Statsig app's "Import" tab
* Click "Import Now" to fetch existing Statsig users, groups, and teams
* After importing, you should see the group in your Okta groups following the format `Statsig-ProjectName-TeamName-RoleName`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step2-verify-import.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=1a3627d12f1999d85a83f27d057dc1bd" alt="Okta Import tab displaying Statsig team groups discovered from SCIM" width="1960" height="838" data-path="images/okta_scim_steps/team_steps/step2-verify-import.png" />
</Frame>

## Create a Mapping Group

* To push a group of Okta users to a Statsig team, you must first create a mapping group.
* This group will contain the Okta members which will be part of the Team x Role Group.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step3-create-mapping-group.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=e21fe226740abfcd4ea1ffaf4669d0b8" alt="Okta group creation screen for mapping Statsig team members" width="2042" height="1318" data-path="images/okta_scim_steps/team_steps/step3-create-mapping-group.png" />
</Frame>

## Push Teams to Statsig

1. In Okta, go to the Statsig Integration's "Push Teams" tab and select "Push Groups". Then pick the mapping group created in the previous step.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step4-push-teams-1.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=b1cf669f82918fc397dd9eef9764e03f" alt="Okta Push Groups dialog selecting mapping group to link with Statsig team" width="1970" height="1146" data-path="images/okta_scim_steps/team_steps/step4-push-teams-1.png" />
   </Frame>

2. Change the Match result & push action to Link group. Then select the Statsig team you want to push to. It should follow the format `Statsig-ProjectName-TeamName-RoleName`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step4-push-teams-2.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=3d7861944f13c7c7c0385295d805c6ca" alt="Match result settings linking Okta group to Statsig-Project-Team role name" width="1888" height="1458" data-path="images/okta_scim_steps/team_steps/step4-push-teams-2.png" />
</Frame>

3. When you are finished setting up the push, click "Save".

## Verify the Push

* Navigate to the Statsig Project and verify that the team has the new members.
* This could take some time for Okta to push the members to the team.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step5-verify-push.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=5c16366ad4deadd4bdd8702d86eb76a4" alt="Statsig team detail page showing synced Okta members" width="3266" height="1408" data-path="images/okta_scim_steps/team_steps/step5-verify-push.png" />
</Frame>

## Delete the Team

* On Okta, navigate to push groups and find the pushed group that maps to the Statsig team.
* Click the push status section and select "Unlink Group".

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step6-delete-1.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=916b2603c7dc33084bcd8e958ebdc12c" alt="Okta push groups status view with unlink group option" width="1508" height="696" data-path="images/okta_scim_steps/team_steps/step6-delete-1.png" />
</Frame>

* When prompted to delete the group or leave it in the app, select "Delete".
* After Okta pushes the deletion, the team should be deleted from Statsig. This may take a few minutes to complete.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step6-delete-2.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=101c5ae73ef83423c0535b4b9700dd49" alt="Confirmation dialog asking to delete pushed group from app" width="1108" height="842" data-path="images/okta_scim_steps/team_steps/step6-delete-2.png" />
</Frame>

## Optional: Create a Team Via SCIM

* Find an existing Okta group with the members for a new Statsig Team.
* Navigate to Push Groups and Select "Push Groups".
* Select the group you want to push to Statsig.
* Change the Match result & push action to Create Group.
* The naming for this group must match the format `Statsig-ProjectName-TeamName-Member`.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step7-create-1.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=f65f6741f4a596cfd0c509f0f88cd380" alt="Okta push groups workflow set to create new Statsig team group" width="1944" height="982" data-path="images/okta_scim_steps/team_steps/step7-create-1.png" />
</Frame>

* When you are finished setting up the push, click "Save".
* Afterwards, you should see the new team in the Statsig Project you specified.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/MVGh1601-syUdAtS/images/okta_scim_steps/team_steps/step7-create-2.png?fit=max&auto=format&n=MVGh1601-syUdAtS&q=85&s=9f03701390d9fbb12e91013517dab4d3" alt="Statsig console showing newly created team populated from SCIM push" width="3272" height="1742" data-path="images/okta_scim_steps/team_steps/step7-create-2.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).