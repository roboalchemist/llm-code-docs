# Source: https://docs.vast.ai/documentation/teams/teams-roles.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Teams Roles

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Understanding Team Roles on Vast.ai",
  "description": "A comprehensive guide to team roles on Vast.ai including default roles (Owner, Manager, Member), custom roles with tailored permissions, role syntax, and best practices for managing access control.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "datePublished": "2025-01-13",
  "dateModified": "2025-04-04",
  "articleSection": "Teams Documentation",
  "keywords": ["team roles", "permissions", "access control", "custom roles", "vast.ai", "collaboration", "security"]
})
}}
/>

## What Are Team Roles?

Team roles in Vast.ai's platform are designed to streamline collaboration and enhance security by assigning specific permissions and access levels to different members of a team. These roles determine what actions a team member can perform and what data they can access within the team's shared workspace/context.

### Types of Team Roles

1. **Default Roles**: These are the standard roles with preset permissions, suitable for common team structures:
   * *Owner*: Full access to all team resources, settings, and member management.
   * *Manager*: All permissions of Team Owner apart from Team Deletion.
   * *Member*: Has ability to view, create, and interact with instances, but no access to billing info, team management, autoscaler, machines, etc.
2. **Custom Roles**: Custom roles allow team managers to create roles with custom, tailored permissions via permission groups. This feature is particularly useful for teams with unique workflow requirements or specific security protocols.

For more information on Permission Groups and what they allow access to, [click here](/api-reference/permissions-and-authorization).

### Creating Custom Roles

* **Accessing Role Management**: Custom roles can be created and managed through the **Roles** tab of the **Members** Page on the Vast.ai platform.
* **Defining Permissions**: When creating a custom role, you can select from a wide range of read/write permissions, such as instance creation, billing access, etc. This allows for precise control over what each role can and cannot do.
* **Assigning Custom Roles**: Once a custom role is created, it can be assigned to team members through the team management interface.

You can create roles either in the Vast CLI or on your team dashbaord if you have permission to create roles within your team (team\_write).

<Frame caption="Default Roles">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=84dfe4a0e897e0c961ca632abc387069" alt="" data-og-width="963" width="963" data-og-height="284" height="284" data-path="images/teams-roles.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=6f21996b233f92def107771d009e415c 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=13e79c6f70325f74be0a6013c697849c 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=bc91651350694f6c1217a0267812a67e 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=66d7a6093c5a2eb4a0e8cde11d656ce7 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c26cd400855cd8a8b5fcee9e97f6275a 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=3cddd21c57b76c02962212db2e1af2ff 2500w" />
</Frame>

You can easily edit any roles on your team using the team dashboard. When editing a role you should see the same series of checkboxes and categories as before.

<Frame caption="Edit Role">
    <img src="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=52a177afa7a231a9d6b68d2de64f0c84" alt="" data-og-width="800" width="800" data-og-height="712" height="712" data-path="images/teams-roles-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?w=280&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=42c781cb77895536dd26caea6ccffc69 280w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?w=560&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=674601204bcaf58da7ae178a06b67030 560w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?w=840&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=2b20d1d7d076fdc748babbbef11c80db 840w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?w=1100&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=44d13e0233d620702eb20d5c15b1833d 1100w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?w=1650&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=7c40f75d97ad4ad8d72c3ed1080312e8 1650w, https://mintcdn.com/vastai-80aa3a82/LEwury95WvhzGW2f/images/teams-roles-2.webp?w=2500&fit=max&auto=format&n=LEwury95WvhzGW2f&q=85&s=c922d90ff4ad0504c3cd0454aeca9da1 2500w" />
</Frame>

### Role Syntax

All team roles are created through the team dashboard using the role editor. You can also create roles through the Vast CLI by passing in a permissions JSON object that delegates what group of endpoints can be accessed.

Currently, the system only supports groups of endpoint categories, but soon it will be extended for further granularity.

The current activated scopes are as follows

* **misc**: Supports uncategorized operations like search offers, getting logs from various sources, etc
* **user\_read**: Allows the usage of obtaining basic user data like email, credits, etc. Essential for web usage.
* **user\_write**: Allows the ability to change account settings such as email, password, 2FA, etc.
* **instance\_read**: Grants ability to view instances, and certain read-only instance operations
* **instance\_write**: Grants access to instances and all relevant operations such as starting/stopping instances, cloud copy, reserving credits, etc
* **billing\_read**: Ability to view billing page and get billing information
* **billing\_write**: Ability to change billing page information
* **machine\_read**: Read access to machines owned by the team
* **machine\_write**: Ability to add/remove machines, and also edit machine settings

An example of a permissions json would look like this:

```text Text theme={null}
{
    "api": {
        "misc": {},
        "user_read":{},
        "instance_read": {},
        "instance_write": {},
        "team_read": {
            "api.team.members": {}
        }
    }
}
```

In order to create a granular team roles you must either use the CLI or the API. In the above example, the only API under team\_read that the user would have access to would be viewing the list of team members.

For more information on Permissions [click here](/api-reference/permissions-and-authorization).

### Best Practices for Using Team Roles

* **Clear Role Definitions**: Clearly define the responsibilities and permissions for each role to avoid confusion and ensure effective collaboration.
* **Use Custom Roles Judiciously**: Create custom roles when predefined roles do not meet your specific needs. Be mindful of the permissions assigned to ensure team security and efficiency.

### Conclusion

Team roles are a fundamental aspect of managing a secure environment for collaboration on the Vast.ai platform. By effectively utilizing predefined and custom roles, teams can ensure that each member has the appropriate level of access and control, fostering a productive and secure working environment.
