# Source: https://docs.replit.com/teams/identity-and-access-management/managing-members.md

# Managing Members

> You can manage members on your Replit team to control access, collaboration, and permissions across your organization's apps and projects.

Managing members is one of the most important functions of Replit Teams, allowing you to add collaborators to your organization and control who has access to your team's resources.

## Features

The **Members** tab displays a list of current organization members, showing their default group and recent activity. From this view, you can manage your team through several key capabilities:

* **Add Members**: Invite new collaborators to join your organization and assign them appropriate permissions
* **Remove Members**: Remove people from your organization when they no longer need access
* **Assign Roles**: Set member permissions with Admin, Member, Guest, or Viewer roles
* **Manage Invitations**: Send email invitations to non-Replit users and track invitation status
* **Seat Management**: Control billing capacity and monitor available seats

<CardGroup cols={2}>
  <Card title="Add Members" icon="person">
    Add team members so you can share apps and ideas.
  </Card>

  <Card title="Remove Members" icon="trash">
    Remove members or change who's on your team.
  </Card>
</CardGroup>

## Usage

### Adding members

<Note>
  For automated user management and bulk operations, see [SCIM](/teams/identity-and-access-management/scim) instead.
  *Note: SCIM is available for enterprise customers only.*
</Note>

Selecting the **Add** button in the corner of the Members page opens a modal with a search input. The **Add** button may become disabled if there are not enough seats available or if you don't have permissions to add new organization members.

You can find existing Replit members via username or email, while you can add non-Replit members by email. After selecting someone or entering an email address, you can set the member's group with the following options:

* **Admin**: Admins have full administrative access to organization settings and all resources.
* **Member**: Members can see all other members, and can create Apps and Projects.
* **Guest**: Guests can only edit and access apps shared with them.
* **Viewer**: Viewers have read-only access to apps and deployments in your organization.

Existing members join immediately, and the seat becomes active immediately. Non-Replit members join the organization after creating an account. The seat won't become active until this happens. The invitation sent via email expires after seven days.

<Frame>
  <img src="https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=9bb7af12906e5f2d04cc6fba67b1cf0a" alt="Invitation email" data-og-width="1550" width="1550" data-og-height="1436" height="1436" data-path="images/teams/identity-and-access-management/invitation-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?w=280&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=e392f86ccd3d786f9a3b24cb41107ba4 280w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?w=560&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=36139bdf3506c1942f3a85bc77a0cc7a 560w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?w=840&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=cb9f0cbd555cda32a9b0929772a08c4f 840w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?w=1100&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=227c54f247483d1fc655d09ce7d814f9 1100w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?w=1650&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=f4028f9ebb63211bcc5da40b12472050 1650w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/invitation-email.png?w=2500&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=e5a98ac73257a99b1f28249072579a3a 2500w" />
</Frame>

Additional documentation:

* [SCIM](/teams/identity-and-access-management/scim)
* [SAML](/teams/identity-and-access-management/saml)
* [Viewer Seats](/teams/identity-and-access-management/viewer-seats)

### Removing members

Eligible members can remove people from the organization using the trash can icon. You can also use the context menu opened from the triple dot to the right of each member row.

Removing someone from the organization requires a confirmation step. After you remove them, a seat becomes available immediately and you can use it to invite a new organization member.

<Frame>
  <img src="https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=11139a6f19b3bb3f4ca24053e57c009c" alt="Removing a member" data-og-width="2880" width="2880" data-og-height="1800" height="1800" data-path="images/teams/identity-and-access-management/removing-a-member.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?w=280&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=91632bb103f2d2ab089fb34d11104646 280w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?w=560&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=3384692abce1b8de2b9fdf49e4560ff0 560w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?w=840&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=ebbe3097b95212669620a75f63994d47 840w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?w=1100&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=277ce0a7f5a9f7568be15e0e717b032d 1100w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?w=1650&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=fdc1bf677159a6cfd1ff61b11ff6df53 1650w, https://mintcdn.com/replit/0UCOQvZyQpUEM03B/images/teams/identity-and-access-management/removing-a-member.png?w=2500&fit=max&auto=format&n=0UCOQvZyQpUEM03B&q=85&s=9804c94e5e73aead4e4d8df9ef14241a 2500w" />
</Frame>

### Managing seats

Managing seats is different from managing members. While member management involves adding or removing people from your team, seat management controls your billing capacity—how many seats you're paying for.

For detailed information on adding seats and removing seats, see [Managing Seats](/billing/teams-billing/managing-seats).
