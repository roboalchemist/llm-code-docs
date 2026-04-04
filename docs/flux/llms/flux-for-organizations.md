# Source: https://docs.flux.ai/Introduction/flux-for-organizations.md

# Flux for Organizations



Flux Organizations is a shared space for your team to collaborate. Manage access to projects, and libraries and create templates from a centralized place.





## Overview

Organizations in Flux allow your entire team to be on the same page. By setting the correct default permissions, rule checks, templates, or Flux presets, you can ensure your whole team can access the tools they need to do their job.

## Getting Started with Organizations

You can benefit from being part of an organization by creating a new organization or joining an existing one.

To join an existing organization, ask someone with the correct permissions to add you as a member. You will then see the organization in your profile menu.

{% image url="https://uploads.developerhub.io/prod/86Yw/dl8po90vvym3zt9r9bybdlt3vh73g7mbrhkivx0xe66aduzlj9fpwle8gk3ozz1j.png" mode="600" height="1488" width="2520" %}
{% /image %}

Organizations can do everything users do: [create new parts](https://docs.flux.ai/flux/tutorials/tutorial-add-part-library), [fork or clone projects,](https://docs.flux.ai/flux/reference/reference-forking-cloning) and collaborate to design new projects or [modules](https://docs.flux.ai/flux/tutorials/tutorial-parts-and-sublayouts).

### Creating an Organization

To create a new organization:

- Click on the profile menu on the top-right
- Find the "Organizations" menu and click on "Create an Organization"

You will be prompted to provide an account name and a display name:

- _Account name:_ is the "username" of your organization. It will be used to create your organization's URL. For example, an account name `neworg` will result in the URL `www.flux.ai/neworg`
- _Display name:_ the full name will be displayed on the organization's page. You can add spaces and special characters in the display name. For example, you can use `My Org!` as a display name

{% image url="https://uploads.developerhub.io/prod/86Yw/a47es425t1re2j80ktvycmh2xyossts3y8pbhvf7sqk1bt4amztvu14nb6aai8es.png" mode="600" height="736" width="1186" %}
{% /image %}

### Managing Members

Organization members can be managed from that organization's "Members" tab. From this tab, members with the correct permissions can add, remove, and change the type of each member.

{% image url="https://uploads.developerhub.io/prod/86Yw/sj0d7hrrbwbgbgb6hnix5m8091edupk6r61yfdubv1fb7iz3bwpiry9gslph06rk.png" mode="600" height="1548" width="2628" %}
{% /image %}



#### Adding a Member

Click on the `ADD MEMBERS` menu and type the username of the member you'd like to add.



#### Removing a Member

To remove a member, click the three dots button next to the member's name and select "Remove from Organization".

## Organization Member's Permissions

There are two kinds of users within an organization: owners and members

For a comprehensive guide to how organization permissions work within Flux's multi-layered permission system, see [Permission Tiers and Access Control](https://docs.flux.ai/flux/reference/reference-permission-tiers).

### Members

Members are intended to participate in the organization's projects and components library but lack permissions to manage the organization. These are the actions members can do within an organization:

- Add new projects or components to the organization.
- Remove projects they created themselves.
- Edit projects within the organization that have not been set to "Only owners can view". More on that in the project access section.
- Publish projects to the library

### Owners

Owners have the same access as members but can also manage the organization. These are the things only owners can do:

- Add/remove users from the organization.
- Change a user's membership type from member to owner and vice versa.
- Remove, view or edit **any** project within the organization.

## Project Access for Organizations

By default, any organization member can edit newly created projects within an org, but those permissions can be modified for each project individually. To change access to a project, click on the "SHARE" menu on the top right.

Remember that projects created under your own personal account will not have access to permission settings for organizations. To move a project from your personal account to an organization, you can fork the project and select the organization as the target account.

{% image url="https://uploads.developerhub.io/prod/86Yw/ggk7lk6ro8d599fy97kuj3qd0s86esn7rrh5domghokrgdxsnvkfp827yhvlav3s.png" mode="600" height="1548" width="2630" %}
{% /image %}

### Standard Permissions

The standard share view allows you to manage permissions for other members of the organization:

- PRIVATE: Only the user who created the project and every organization owner can view or edit the project.
- Members of [Organization] can edit/view/comment: every organization member in which the project has been created will be able to edit/view/comment.

{% image url="https://uploads.developerhub.io/prod/86Yw/6xkuzanqsypfqoqjkutc869426rsbs7yvuluy0fzro48bo2mx00pr8xt1vcrtk28.png" mode="600" height="786" width="1276" %}
{% /image %}

### Advanced Permissions

The advanced menu allows you to manage permissions for users outside the organization.

- _Invite people:_ You can add individual users from within or outside the organization to the project.
- _Members of [Organization]:_ sets permissions for other organization members. Same as the standard permissions menu
- _Anyone on the internet:_ sets permissions for everyone on the internet at once. This means that anyone, Flux user or not, will have view/comment/edit access to your project.

{% image url="https://uploads.developerhub.io/prod/86Yw/qecp28ngdryzdoyg8x6qqu5lhpumenhjil78pko274xeamswjlb3ch6frnyka7vj.png" mode="responsive" height="790" width="1280" %}
{% /image %}

## Library Access for Organizations

Access to published components works in a very similar fashion as they do for personal accounts. When an organization-owned component is published to the library, anyone with the proper permissions will be able to find said component in the library.

### Example - User with access to multiple organizations

Consider a `docbrown`, a user who has access to multiple organizations, `Org1` and `Org2`.

When working on a project under his own personal account; `docbrown` will have access to:

- Every component under his own personal account
- Components that have been shared to his username `docbrown`
- All the [public](https://docs.flux.ai/flux/faq/private-and-public-projects) components created by any other user, including Org1 and Org2

When working on a project under `Org1`; `docbrown` will have access to:

- Every component under his personal username (`docbrown`)
- Components that have been shared to his personal username (`docbrown`)
- All the [public](https://docs.flux.ai/flux/faq/private-and-public-projects) components created by any other user, including `Org1` and `Org2`
- Private components that are only accessible within `Org1`

When working on a project under `Org2`; `docbrown` will have access to:

- Every component under his personal username (`docbrown`)
- Components that have been shared to his personal username (`docbrown`)
- All the [public](https://docs.flux.ai/flux/faq/private-and-public-projects) components created by any other user, including `Org1` and `Org2`
- Private components that are only accessible within `Org2`

### Filtering Library Search for Organization-owned parts

Similarly to how you can filter by only parts that you've created with your own personal account, you can filter by only parts the organization has created.

Keep in mind that this filter only works for projects that have been created within an organization. If a user is part of multiple organizations, only parts created by the organization in which the project has been created will be shown.

{% image url="https://uploads.developerhub.io/prod/86Yw/0ngcz2e0nzb2i4gcj8zaydzdo6klia8a6wp7zrux1ihda31u9y0pl88qyl3karnm.png" mode="600" height="780" width="1262" %}
{% /image %}

## FAQ

**I have an open-source organization, do I still need to pay?**

Organizations are free as long as you only host public projetcts.

**Can I be part of multiple organizations?**

Absolutely. Users can be part of as many organizations as they want.

**How does pricing for organizations work?**

Organizations allow you to centralize [payments](https://www.flux.ai/p/pricing) for your team.

**Can I delete an organization?**

Organizations cannot be deleted at the time of writing. This feature is in our roadmap and will be released soon after the organization's feature launch.

**What happens if I remove a member and I'm on the annual plan?**

Removing an editor in an annual plan before the next billing period will result in a discount on your next invoice.

For example, this happens if you downgrade from 3 editors to 2 editors in an annual plan halfway through the year. Your following annual invoice will get a 50% editor discount. So, if you maintain two editors for the next year, you will end up paying for 1.5 editors.
