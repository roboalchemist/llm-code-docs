# Source: https://tyk.io/docs/portal/customization/menus.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Menus in Developer Portal

> How to customize menus in developer portal

The Developer portal has two types of menus:

1. The main navigation at the top (in the header)
2. The footer at the bottom.

Both of them are defined as [partials](/portal/customization/themes#file-structure-of-a-theme) in the portal directory in `/themes/default/partials/`.

## Top Navigation Menu

The Enterprise Developer portal enables admin users to customize the navigation menu that appears on the top navigational bar of the live portal. An admin user can create and manage menu items without any code from the admin dashboard of the Developer portal.

<img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/top-nav-menu.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=4460e6f50a62a6ae5eff22265c07bcf1" alt="The navigation menu" width="2262" height="934" data-path="img/dashboard/portal-management/enterprise-portal/top-nav-menu.png" />

Each menu item may:

* lead to a specific page or URL:
  <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/regular-menu-item.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=08482daba18b59ba81c8d3463f484138" alt="Regular menu item" width="746" height="408" data-path="img/dashboard/portal-management/enterprise-portal/regular-menu-item.png" />
* show a dropdown list with possible navigational options:
  <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/dropdown-menu-item.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=598547cf8178245bb57a46eb1197c760" alt="Dropdown menu item" width="820" height="410" data-path="img/dashboard/portal-management/enterprise-portal/dropdown-menu-item.png" />

Admin users can create additional navigational menus and render them on any page of the live portal. This customization requires changes to a theme and is covered in the [Full customization section](/portal/customization/menus).

### Manage Menu Items

The management of the menu items is done from the **Menus** section of the Developer portal.

1. Open the admin dashboard. Navigate to the **Menus** section.
   <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/navigation-to-menus-section.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=b350e1887a11896cd0a67a0c025a07e8" alt="Navigate to the Menus section" width="3360" height="1678" data-path="img/dashboard/portal-management/enterprise-portal/navigation-to-menus-section.png" />

2. Select a menu that you want to modify. By default, the Developer portal has only one **Primary** menu. If you want to add more menus and render them on the live portal, please refer to [Full customization section](/portal/customization/menus).
   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/select-a-menu.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=8591b70872f7affa8b6d1af621815c4e" alt="Select a menu" width="3356" height="1640" data-path="img/dashboard/portal-management/enterprise-portal/select-a-menu.png" />

3. Click on a **menu item** to modify it. You can change the following items:
   1. **Title** that will be exposed to developers.
   2. **Path** where developers will be redirected by clicking on that menu item.
   3. **Children** items that will be exposed in the dropdown list that will appear when hovering mouse over the menu item.
   4. To make the changes effectively, you need to save the changes by clicking on the **Save changes** button.
      <img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/menu-item.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=b811fb148db5bce43a99093a22cabe40" alt="Modify a menu item" width="3348" height="1664" data-path="img/dashboard/portal-management/enterprise-portal/menu-item.png" />

4. To remove a menu item from the menu click on the **bin** icon and click on the **Save changes** button.
   <img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/delete-a-menu-item.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=881fd7954ae0ba3615523fe0f9be3cb8" alt="Delete a menu item" width="3358" height="1650" data-path="img/dashboard/portal-management/enterprise-portal/delete-a-menu-item.png" />

### Create New Menu Items

To create a new menu item, you need to:

1. Click on the **Add Menu Item** button.
2. Fill **Title**, **Path**, and **Children** fields. Save the changes by clicking on the **Save changes** button.
   <img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/save-new-menu-item.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=94899c0790d0b6ff0803c76890d41b30" alt="Save a menu item" width="3360" height="1636" data-path="img/dashboard/portal-management/enterprise-portal/save-new-menu-item.png" />

The new menu item will appear on the live portal immediately.
<img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/new-menu-item-on-the-live-portal.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=e84b23b01504efadecbe0fbe140d9d82" alt="New menu item on the live portal" width="2266" height="922" data-path="img/dashboard/portal-management/enterprise-portal/new-menu-item-on-the-live-portal.png" />s

### Update Existing Menus

1. Log into your portal
2. Select **Menus** from the navigation menu
3. Click **Primary** to edit the menu

<img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/edit-menu.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=0819a58253027bcd0ce531705fd356fc" alt="Edit Menu dialog" width="950" height="763" data-path="img/dashboard/portal-management/enterprise-portal/edit-menu.png" />

**Field Descriptions**

* **Name**: You can give it any name you like, it does not have any effect in the live portal nor the admin app.
* **Path**: This will be used in the code as a reference in order to render the menu. If you don’t have access to the template files, we recommend that you do not edit this field. Editing the `Path` for the default menus will hide the menu as there will be a mismatch between the Path and the reference in the template.
* **Menu Items**:
  1. **Title**: This will be the text that will be displayed in the live portal.
  2. **Path**: this is where the user will be redirected to.
  3. **Children**: In this section you add another nested menu item. We have added a dummy item (Product 1) to demonstrate

Below is the menu item from its own view, which is available from the **Menu Items** option in the admin app side menu.

<img src="https://mintcdn.com/tyk/p6VDuboOnNxaT_QZ/img/dashboard/portal-management/enterprise-portal/edit-menu-item.png?fit=max&auto=format&n=p6VDuboOnNxaT_QZ&q=85&s=13b73b85782cd4535eb8f2dd66e4a83a" alt="Edit Menu item dialog" width="957" height="551" data-path="img/dashboard/portal-management/enterprise-portal/edit-menu-item.png" />

Here's the menu as displayed in the app:

<img src="https://mintcdn.com/tyk/UiKBFLPkIyNRnItY/img/dashboard/portal-management/enterprise-portal/portal-menu-live.png?fit=max&auto=format&n=UiKBFLPkIyNRnItY&q=85&s=e7ea2909aa9c439bbb80a620575efb83" alt="Live menu in app" width="1350" height="101" data-path="img/dashboard/portal-management/enterprise-portal/portal-menu-live.png" />

We have mentioned above the relationship between a menu’s `Path` and the code reference in the menu template. Let’s see how the main menu template looks like (the file is `/themes/default/partials/` directory and is called `top_nav.tmpl`) for the part that we are interested in:

```go  theme={null}
{{ if GetMenus.Primary }}
  {{ range GetMenus.Primary.Children }}
    <li class="nav-item {{ if .Children }}dropdown{{end}} mr-2">
      <a class="nav-link {{ if .Children }}dropdown-toggle{{end}}" href="{{.Path}}" {{ if .Children }}data-toggle="dropdown" aria-haspopup=”true" aria-expanded="false"{{end}}>{{.Tag}}</a>
      {{ if .Children }}
        <ul class="dropdown-menu submenu" aria-labelledby="navbarDropdownMenuLink">
          {{ range .Children }}
            <li class="nav-item">
              <a class="dropdown-item" href="{{.Path}}">{{.Tag}}</a>
            </li>
          {{ end }}
        </ul>
      {{ end }}
    </li>
  {{ end }}
{{ end }}
```

Let's pick each line that is used to render the menu attributes and see how they work:

1. `{{ if GetMenus.Primary }}`: This statement calls the “GetMenus” function and checks if there is a menu called `Primary`. If present, it goes into the next line:
2. `{{ range GetMenus.Primary.Children }}` Each Menu (Primary) has some children (Menu items) so what this code does is loop through all the children and they are rendered as below:

```go  theme={null}
<li class="nav-item {{ if .Children }}dropdown{{end}} mr-2">
<a class="nav-link {{ if .Children }}dropdown-toggle{{end}}" href="{{.Path}}" {{ if .Children }}data-toggle="dropdown" aria-haspopup=”true" aria-expanded="false"{{end}}>{{.Tag}}</a>
```

Where:

* `{{ .Path }}` is the Path we have defined from the UI and
* `{{ .Tag }}` is the Name we have defined from the UI.

So this will render all the menu items (Catalogs - as per screenshot) of the menu (Primary - the name we’ve given to the menu).

1. `{{ if .Children }}`: This line checks if the menu item has any submenus. If it does it loops through those children `{{ range .Children }}` and finally renders them `<a class="dropdown-item" href="{{.Path}}">{{.Tag}}</a>` similarly as the main menu items.
   So now the child of **Catalogs** which we named **Product 1** has been rendered.

Built with [Mintlify](https://mintlify.com).
