# Source: https://loops.so/docs/deliverability/adding-a-sending-avatar.md

# Add a sending avatar

> Set up your email sending avatar through third-party platforms like Gmail and Outlook.

Adding an avatar to your emails can improve open rates and brand recall.

<img src="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=89f7c1024a6df80e4edb4a104548d6d4" alt="example of email sending avatar" data-og-width="722" width="722" data-og-height="160" height="160" data-path="images/add-a-sending-avatar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?w=280&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=4dffeedf02c885e0c8f64867692e18e5 280w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?w=560&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=9f2bfddaa8bb3eccafd1553ee248a04a 560w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?w=840&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=3a4af2764a7af4804e8ac23e5110cb05 840w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?w=1100&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=39a6c40e5984d2488efeb910bddc4369 1100w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?w=1650&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=7b97f8e8ad30b5d0b8e724e03a7679d7 1650w, https://mintcdn.com/loops/Vqx-auiVy74YQr9S/images/add-a-sending-avatar.png?w=2500&fit=max&auto=format&n=Vqx-auiVy74YQr9S&q=85&s=935488096ae019ef6fecbcde17e1ade2 2500w" />

## Basic setup

1. Login to the Google Workspace account linked to your Loops sending domain
2. Click the Google logo in the top right corner
3. Click "Add a Profile Picture"
4. Save

<Tip>
  For full coverage, add a [Gravatar](https://en.gravatar.com) icon to the email
  address.
</Tip>

## Advanced setup

### Adding a sending avatar on a secondary domain

To send email from a secondary domain (e.g., mail.loops.so) with a sending avatar:

1. Log into your Google Admin console with an administrator account
2. Go to "Manage domains" in the dropdown menu
3. Click "Add a domain" and enter the domain name
4. Select "User alias domain" (recommended) or "secondary domain"  as appropriate:
   1. **User alias domain** (recommended) – add notifications.example.com as an alias domain. This automatically assigns each primary user ([john@example.com](mailto:john@example.com), [jane@example.com](mailto:jane@example.com)) a corresponding @ [notifications.example.com](http://notifications.example.com) address without requiring additional seats, and their profile pictures (avatars) will carry over.\
      \
      The User alias domain approach is generally simpler and avoids managing duplicate user accounts.
   2. **Secondary domain** – creates a separate user set, meaning you’ll need to create either a full account or alias for each sender under  [notifications.example.com](http://notifications.example.com) and upload their profile picture individually.\
      \
      After setup and assigning avatars to each alias in Google, please allow a few minutes for Gmail to update, and your avatars should display consistently.
5. Continue and start verification

Once verified, the secondary domain will use the same sending avatar as the primary domain.

At the end of the day, whoever you are sending from in Loops needs to be a user in G Suite. For example, if you are sending from a `notifications@mail.example.com`, you need a user with that name in G Suite. It can be an alias or secondary domain, as long as that user exists with a profile pic.

Note that avatars are only visible within the same email client. To display your avatar across all clients, create accounts and upload avatars in each one's settings.

Alternatively, consider using BIMI (Brand Indicators for Message Identification), a new email standard for displaying authenticated logos. BIMI requires some setup and legal work but provides an added layer of trust.
