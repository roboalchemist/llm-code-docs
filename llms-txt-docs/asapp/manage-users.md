# Source: https://docs.asapp.com/getting-started/setup/manage-users.md

# Manage Users

> Learn how to set up and manage users.

You are in control of user management within ASAPP. This includes inviting users, granting access to applications, and assigning specific permissions for features and tooling.

<Warning> Managing users for ASAPP dashboard is separate from the [Digital Agent Desk](/messaging-platform/digital-agent-desk/user-management)</Warning>

Manage users from within the ASAPP dashboard, including [inviting users](#invite-users), deleting users, and managing [application access and permissions](#application-access-and-permissions).

We also support [SSO](#sso), allowing you to manage user access via your own auth system.

## Invite Users

To Invite Users:

* Navigate to Home > Admin > User management
  <Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=cc6a7c0e5e4edc9d55a6bee7a3e2f78a" data-og-width="1064" width="1064" data-og-height="378" height="378" data-path="images/getting-started/user-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=23398ed8d4ddb79ab1c5de59fcc5ba85 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=87fbf81fba34ebc5896d4c44eeb41f57 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=62b377209f5ea71871f1d7d94166cdd2 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=678e08258eb4b3d014ed1baa8c01f104 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=fbaedbb7f693ba9feb3ac6f58c62c251 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/user-list.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=5335bebcafb98433cc622621bede3eb9 2500w" />
  </Frame>
* Click Invite Users
* Enter in the email and name for the user.
  * By default, users have the "Basic" role, but you may choose others. We will cover roles and permissions further below.
  * You may invite multiple users at once.
  <Frame>
    <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=b0f32ce9a13f52b61ae47da8760a3f1e" data-og-width="1065" width="1065" data-og-height="332" height="332" data-path="images/getting-started/invite-user.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=0ad66b9d4ed67f44d0a904f2d28c51cf 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=44222b7a0abebf394c647fa7c889381d 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=3b970ed192320efb6201cf58fe1510ac 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=fc7ffa53568e38bb7cdae5f038e37c7f 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=64825a362cc565f1a25d605596c35355 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/invite-user.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=f174524b72dd95571c84b213d516490e 2500w" />
  </Frame>

## Roles and Permissions

Access to ASAPP is managed via roles. A role is a collection of permissions which dictate what UI elements a user has access to.

By default, all users must have the Basic role, allowing them to log in to the dashboard. But you may create and assign as many roles as you like per given user.

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=90bcd3c71adc424b1b723baefef4e8e3" data-og-width="1065" width="1065" data-og-height="332" height="332" data-path="images/getting-started/role-list.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=daef431f2c1b081317e77649db83728a 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=b6ebb7234b4533bf487829269e3a2844 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=a522f3d80e6f1329a203f0a343bfe0ad 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=dc671772c4c8ba0a554e87bda1e06d72 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=0942aac42670354c88d55fde35ef7350 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/role-list.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8e362086bb29796da96909c02fb5d7b6 2500w" />
</Frame>

### Creating a Role

To create a role:

1. Navigate to Home > Admin > Roles & Permissions.
2. Click "Create Role".
3. Enter a name and description for the role.
4. Select the permissions for the role.
5. Optionally, if you are using SSO, [add IDP mapping](#idp-mapping) to the role user.
6. Click "Save Permission".

### IDP Mapping

If you are using SSO, you can map roles in your Identity Provider (IDP) to the roles in ASAPP, allowing you to manage access to ASAPP via your own IDP.

You must work with your ASAPP account team to determine which claim from your IDP contains the roles list.

For each role in ASAPP, you specify one or more roles within your IDP that should be mapped to it. You can map multiple ASAPP roles to the same IDP role.

<Frame>
  <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=d66e7e6a40dc3a6fea9cf1430ad37183" data-og-width="1222" width="1222" data-og-height="283" height="283" data-path="images/getting-started/idp-mapping.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=db4b5058affe807b157240c8d1d850ef 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=e42cd7b62cd03d7f2fda61e886384252 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=d2c2601dd0b989a2ac9d714d1f53b737 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=218888fe87f5ac4d5353df2f4cd68cd6 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=805b4c73ac55453726cbe7663a3dcba1 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/getting-started/idp-mapping.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=78cd1aead7388b65b8d20e7f19ad021e 2500w" />
</Frame>

## SSO

ASAPP supports Single Sign-On (SSO). SSO allows you to manage your team's access through an Identity Provider (IDP). ASAPP supports SSO using OpenID Connect and SAML.

When using SSO, your IDP manages the creation and authentication of user accounts, and determines which roles a user should have in ASAPP. You still need to manage the permissions for a given role within ASAPP via [IDP mapping](#idp-mapping).

If you are interested in using SSO, please reach out to your ASAPP account team to get set up.
