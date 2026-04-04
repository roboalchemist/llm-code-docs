# Source: https://screenshotone.com/docs/organizations/

# Organizations and Roles

Organizations are the core unit for managing your ScreenshotOne account. Every user belongs to one organization, and all billing, API access, and resources are scoped to the organization level.

## Roles

There are three roles in an organization:

### Owner

The owner has full control over the organization:

- Full access to billing, invoices, and subscription management
- Can invite and remove members
- Can change member roles
- Can transfer ownership to another member
- Can delete the organization
- Can configure notifications

Every organization has exactly one owner. When you sign up, you automatically become the owner of your organization.

### Admin

Admins are trusted team members who can help manage the organization:

- Can view and manage billing information
- Can invite and remove members
- Can change member roles (promote/demote between admin and developer)
- Can edit organization settings
- Can configure notifications
- **Cannot** transfer ownership
- **Cannot** delete the organization

Use the admin role for team leads, managers, or anyone who needs to manage the team without having full control.

### Developer

Developers have access to everything needed to integrate with ScreenshotOne:

- Can view and manage API keys
- Can view request logs and screenshot history
- Can access the playground
- Can configure S3 storage
- Can view organization members (read-only)
- **Cannot** manage members or invites
- **Cannot** view billing or payment information
- **Cannot** change organization settings

Use the developer role for engineers and team members who need to work with the API but don't need administrative access.

## Managing Your Team

### Inviting Members

1. Go to the **Organization** page
2. Click **Invite new member**
3. Enter the email address
4. Select a role (Developer or Admin)
5. Click **Invite**

The invited user will receive an email with instructions to join. They can sign in (or sign up if new to ScreenshotOne) to accept the invitation.

**Note:** You cannot invite users who already have an active subscription or are owners of another organization with members.

### Changing Roles

1. Go to the **Organization** page
2. Find the member in the list
3. Click **Change role**
4. Select the new role (Developer or Admin)
5. Click **Change Role**

Only owners and admins can change roles. You cannot change the owner's role or your own role.

### Removing Members

1. Go to the **Organization** page
2. Find the member in the list
3. Click **Remove member**
4. Confirm the removal

When a member is removed, they are moved to their own organization with fresh API keys. **Important:** They may still have copies of your API keys. Consider regenerating your keys after removing a member.

### Transferring Ownership

If you need to transfer ownership to another member:

1. Go to the **Organization** page
2. Find the member who will become the new owner
3. Click **Transfer ownership**
4. Confirm the transfer

After transfer, you will become a developer in the organization. Only the owner can transfer ownership, and only if no members have active legacy subscriptions.

## Common Use Cases

### Small Team

- **Owner**: Founder or team lead (handles billing)
- **Developers**: Engineers working on the integration

### Medium Team

- **Owner**: Finance or operations (manages billing)
- **Admins**: Team leads (manage their developers)
- **Developers**: Engineers

### Enterprise

- **Owner**: Account administrator
- **Admins**: Department heads or project managers
- **Developers**: Development teams

## FAQ

**Can I have multiple owners?**
No, each organization has exactly one owner. Use the admin role for additional people who need management access.

**What happens to removed members?**
They get their own organization with a free plan and new API keys. They lose access to your organization's resources immediately.

**Can developers see billing information?**
No, only owners and admins can view billing, invoices, and subscription details.

**Can admins change the subscription?**
Yes, admins have full access to billing and can change plans, update payment methods, and manage the subscription.

**What if I need help?**
Contact us at support@screenshotone.com or use the support chat. We're happy to help with any organization-related questions.