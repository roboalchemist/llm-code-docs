# Source: https://docs.statsig.com/access-management/scim/okta_scim_user_management.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Okta SCIM User and Project/Role Management

## Import Existing Statsig Users and Groups

<Note>
  Users not assigned to the integration cannot be pushed into groups.
</Note>

* In Okta, go to the Statsig app's "Import" tab
* Click "Import Now" to fetch existing Statsig users and groups
* Process the imported users as needed

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step6-import-existing-users.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=5614b5de292ff6d608475ee7ed59a8d1" alt="Okta Import tab listing Statsig users ready to be brought into Okta" width="2040" height="1440" data-path="images/okta_scim_steps/step6-import-existing-users.png" />
</Frame>

## Manage User Assignments

* Use the "Assignments" tab in Okta to add or remove users from Statsig
* Adding a user assignment in Okta will create the user in Statsig, while removing the assignment will deactivate the user's Statsig account

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step7-manage-user-assignments.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=bd2feed8ce0a6c854d9b7d641d7bfa1d" alt="Okta Assignments tab showing Statsig app user assignment controls" width="2084" height="1366" data-path="images/okta_scim_steps/step7-manage-user-assignments.png" />
</Frame>

## Push Groups to Statsig

1. In Okta, go to the Statsig Integration's "Push Groups" tab
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-1.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=866024fc948dc38fa28ec88ae702b03e" alt="Push Groups tab in Okta Statsig integration" width="2042" height="1428" data-path="images/okta_scim_steps/step8-push-groups-1.png" />
   </Frame>

2. Click the settings button and disable "Rename Groups"
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-2.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=30b150505cd5ba55d9be904c3a69d6f0" alt="Push group settings dialog with Rename Groups toggle" width="2066" height="1336" data-path="images/okta_scim_steps/step8-push-groups-2.png" />
   </Frame>

3. Click "Push Groups" and select the method for finding groups in Okta.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-3.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=f6415c7e7364f12ce5bed15fd9326334" alt="Okta modal prompting to find groups by name for push" width="2034" height="1436" data-path="images/okta_scim_steps/step8-push-groups-3.png" />
   </Frame>

4. Type in and select the Okta group that will push to a Statsig Project x Role Group.

* You can find Groups in left nav of Okta: `Directory > Groups`. In there, you will see the groups created from Okta and groups created by Statsig.
* The required groups are groups you created from Okta. You can filter by choosing `Group source type` and set to `Okta groups`. If you don't have any, go ahead and create it with members as well.
  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-4.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=c4999e3e52e63a3cb4f03385763ea536" alt="Directory listing of Okta groups filtered to Okta source" width="2038" height="1054" data-path="images/okta_scim_steps/step8-push-groups-4.png" />
  </Frame>

5. Now let's link/assign Okta group you created from Okta to the Statsig groups with role you want.

* Change `Match Result & Push Action` to `Link Group`
  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-5.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=5c0de2fdd125d094103b3cfbcf5335d8" alt="Push group configuration selecting Link group action" width="2054" height="1616" data-path="images/okta_scim_steps/step8-push-groups-5.png" />
  </Frame>

6. Select the Statsig Project x Role Group that the Okta group will push to.

* We display the Statsig Project x Role Group with the format `Statsig-<Project Name>-<Role Name>` on Okta.
* By default Okta only allows you to map 1 Okta Group to 1 Statsig Group.
  <Frame>
    <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-6.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=fe5a3aa3a9d28644881a1f14cf200e6a" alt="Statsig project role group dropdown showing Statsig-Project-Role format" width="2052" height="1596" data-path="images/okta_scim_steps/step8-push-groups-6.png" />
  </Frame>

7. Then link the Okta group to a Statsig Project x Role Group. On save the group should push to Statsig. All future group changes on Okta will be pushed to Statsig.
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/WSul5JjdT4kF2k8h/images/okta_scim_steps/step8-push-groups-7.png?fit=max&auto=format&n=WSul5JjdT4kF2k8h&q=85&s=197fcd0c693421d967bfbcd5980354fd" alt="Summary screen confirming Okta group linked to Statsig project role" width="2062" height="1612" data-path="images/okta_scim_steps/step8-push-groups-7.png" />
   </Frame>


Built with [Mintlify](https://mintlify.com).