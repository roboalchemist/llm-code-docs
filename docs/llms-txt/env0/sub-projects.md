# Source: https://docs.envzero.com/guides/admin-guide/projects/sub-projects.md

# Source: https://docs.envzero.com/changelogs/2023/02/sub-projects.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🗃 Sub Projects

> As your organization's IaC use grows, it is increasingly challenging to organize all resources. With the addition of env0 Sub Projects, you can now access additional layers of granularity to model even the most complex of deployment structures, and effectively manage your resources and configurations across different teams.

As your organization's IaC use grows, it is increasingly challenging to organize all resources. With the addition of env0 Sub Projects, you can now access additional layers of granularity to model even the most complex of deployment structures, and effectively manage your resources and configurations across different teams.

## ✨ Sub Projects ✨

*Sub Projects* allow you to create a hierarchy of projects to manage, helping create a hierarchy for your environments and configurations. *Sub Projects* have similar configurations to *Projects* but are nested within other *Projects*. Each *Sub Project* may have unique *Environments*, *Templates*, *Variables*, and so on.

Once you've set up your *Sub Projects*, you can view the entire project structure with ease. In the Projects menu, hover over Projects with an arrow next to them. This will allow you to see the *Project*'s *Sub Projects*. Clicking on the *Project* will let you see its environments or configurations.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/02/projects_menu_showing_project_hierarchy_with_expandable_arrows_for_sub-projects.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=4e4d1485d2f855804ef9b9f3d16f0517" alt="Projects menu showing project hierarchy with expandable arrows for sub-projects" width="618" height="212" data-path="images/changelogs/2023/02/projects_menu_showing_project_hierarchy_with_expandable_arrows_for_sub-projects.png" />
</Frame>

When choosing a *Project*, you may navigate to its *Sub Projects* page from the menu.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/02/projects_menu_showing_project_hierarchy_with_expandable_arrows_for_sub-projects.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=4e4d1485d2f855804ef9b9f3d16f0517" alt="Project navigation menu with sub-projects page option highlighted" width="618" height="212" data-path="images/changelogs/2023/02/projects_menu_showing_project_hierarchy_with_expandable_arrows_for_sub-projects.png" />
</Frame>

## Creating a Sub Project

In the *Sub Projects* page, clicking on  *Create New Sub Project* will open a modal for creating a standard *Projects*, but the created *Project* will be associated with the current *Project* as its parent.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/U9rcMIDzc38oPcXx/images/changelogs/2023/02/create_new_sub_project_modal_dialog_with_project_configuration_form.png?fit=max&auto=format&n=U9rcMIDzc38oPcXx&q=85&s=66510cb902dea53c91670c7a612f23c2" alt="Create New Sub Project modal dialog with project configuration form" width="1444" height="282" data-path="images/changelogs/2023/02/create_new_sub_project_modal_dialog_with_project_configuration_form.png" />
</Frame>

## RBAC for Sub Projects

Each *Sub Project* inherits the *Roles* from its parent *Project* down to the root *Project*. So for example, if a team was granted the *"View Project"* permission, every person in the team would be able to view environment from the *Project*, its *Sub Projects*, its *Sub Projects'* *Sub Projects*, and so forth

This allows you to easily give users and teams permissions for multiple *Projects*, but also allows for granular permissions for specific *Sub Projects*

For more information, please visit our [docs](/guides/admin-guide/projects/sub-projects)

Built with [Mintlify](https://mintlify.com).
