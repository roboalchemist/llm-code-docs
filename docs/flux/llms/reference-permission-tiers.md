# Source: https://docs.flux.ai/reference/reference-permission-tiers.md

# Permission Tiers and Access Control


Flux uses a sophisticated multi-layered permission system to control access to projects. Understanding how these layers work together helps you manage collaboration effectively across individuals, organizations, and enterprises.

## Permission Types

Flux supports four distinct permission levels that determine what actions users can perform on a project:

### Edit (Write)

Users with edit permissions have full control over the project. They can:

- Modify the schematic and PCB layout
- Add, remove, or change components
- Update design rules and constraints
- Manage project settings
- Make changes to any aspect of the design

### View (Read)

Users with view permissions can access the project but cannot make changes. They can:

- View all project content
- Navigate through schematic and PCB views
- Download project files
- Review design specifications

View access is ideal for stakeholders who need visibility into project progress without editing capabilities.

### Comment

Users with comment permissions can view the project and participate in discussions. They can:

- View all project content
- Add, edit, and resolve comments
- Participate in design reviews
- View chat history and contribute to conversations

Comment access enables collaboration without allowing direct changes to the design, perfect for reviewers and consultants.

### None

Users with no permissions cannot access the project at all. This is the default state for any user not explicitly granted access.

## Permission Layers

Flux implements a four-layer permission system that provides flexible access control for different scenarios. These layers work together to determine a user's effective permissions for any given project.

### Layer 1: Anonymous Access

The anonymous access layer controls whether anyone on the internet can view your project. When you make a project public:

- Anyone with the project URL can access it
- No Flux account is required
- This is ideal for sharing example projects or open-source designs

By default, all projects are private, meaning anonymous access is disabled.

### Layer 2: User-Specific Permissions

You can grant specific permissions to individual Flux users. This layer provides fine-grained control over who can access your project and what they can do.

To grant user-specific permissions:

1. Open the share menu from the toolbar
2. Add users by their email address or Flux handle
3. Select the appropriate permission level (Edit, View, or Comment)

User-specific permissions override anonymous access settings. For example, you can keep a project private (no anonymous access) while granting specific users view or edit access.

### Layer 3: Organization Permissions

When a project is owned by an organization, organization membership affects access permissions. There are two roles within an organization:

**Organization Owners** have administrative control over the organization and all its projects. They can:

- Manage organization members
- Set default permissions for organization projects
- Access all projects owned by the organization
- Configure organization-wide settings

**Organization Members** receive access to projects based on the organization's default permission settings. By default, organization members receive edit access to all organization-owned projects, but this can be customized per project.

The organization owner can set a default permission type for members (typically Edit, but can be set to View, Comment, or None). This default applies to all organization members unless overridden by user-specific permissions.

[Learn more about organizations](https://docs.flux.ai/flux/Introduction/flux-for-organizations)

### Layer 4: Enterprise Permissions

Enterprise accounts add an additional layer of access control for large organizations. When an organization belongs to an enterprise:

**Enterprise Owners** have access to all projects across all organizations within the enterprise. This ensures enterprise administrators maintain visibility and control.

**Enterprise Members** receive access through their organization's default organization. The enterprise owner can set a default permission level that applies to all enterprise members (typically Edit). This permission flows through the enterprise's default organization to grant members access to projects.

The relationship works as follows:

1. An enterprise owns multiple organizations
2. One organization is designated as the enterprise's default organization
3. All enterprise members automatically belong to the default organization
4. Projects owned by the default organization inherit enterprise member permissions

This structure enables large organizations to manage access control at scale while maintaining security and proper segregation of projects across different teams.

## Permission Inheritance and Precedence

When multiple permission layers apply to a user, Flux uses the most permissive access level. Here's how permissions are evaluated:

1. **Enterprise owner access**: Enterprise owners always have full access to all projects within their enterprise
2. **Organization owner access**: Organization owners have full access to projects owned by their organization
3. **User-specific permissions**: Explicitly granted permissions override organization and anonymous settings
4. **Organization member permissions**: Organization members receive the default permission set by the organization owner
5. **Enterprise member permissions**: Enterprise members receive access through the default organization's settings
6. **Anonymous access**: If enabled, provides the baseline access level for anyone with the URL

For example:
- If a project has anonymous View access enabled, but you grant a specific user Comment access, that user will be able to comment
- If an organization member has the default Edit permission, but you grant them View permission specifically, they will only be able to view (the specific permission overrides the default)

## Managing Project Access

### For Individual Projects

To manage access to an individual project:

1. Click the share button in the toolbar
2. Configure anonymous access (public/private)
3. Add specific users and assign permission levels
4. Review current access in the sharing panel

[Learn more about sharing](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions)

### For Organization Projects

Organization owners can set default permissions that apply to all organization members:

1. Configure the default member permission type (Edit, View, Comment, or None)
2. This setting applies to all projects owned by the organization
3. Override defaults for specific projects or users as needed

### For Enterprise Projects

Enterprise administrators should:

1. Set default member permissions at the enterprise level
2. Organize projects across appropriate organizations
3. Use the default organization for projects that should be accessible to all enterprise members
4. Create separate organizations for projects that need restricted access

## Security Best Practices

When managing permissions:

- **Start with minimal access**: Grant the least privilege necessary for each user's role
- **Use organizations for teams**: Group related users into organizations to simplify permission management
- **Review access regularly**: Periodically audit who has access to sensitive projects
- **Leverage enterprises for scale**: If you're managing multiple teams, enterprise accounts provide the structure you need
- **Document access policies**: Clearly communicate your organization's access control policies to team members

## Related Documentation

- [Sharing and Permissions](https://docs.flux.ai/flux/reference/reference-sharing-and-permissions) - Basic sharing concepts and how to share projects
- [Organizations](https://docs.flux.ai/flux/Introduction/flux-for-organizations) - Setting up and managing organizations
- [Collaboration Deep Dive](https://docs.flux.ai/flux/tutorials/tutorial-collaboration-deep-dive) - Best practices for team collaboration
