# Jetify Documentation

Source: https://www.jetify.com/docs/llms-full.txt

---

# Authenticating with the Cache
Source: https://www.jetify.com/docs/docs/cloud/cache/authenticating/index

Your Jetify Cloud organization is automatically provisioned with a shared cache. Any developers invited to your Jetify Cloud org will be automatically authenticated with the cache when they sign in.

## Managing Access to the Cache[​](#managing-access-to-the-cache "Direct link to Managing Access to the Cache")

Team members can be added in one of two Roles, which controls their access to the Jetify Build
Cache.

* **Members** have read-only access to the cache, and cannot push new packages
* **Admins** have full read/write access to the cache, and can push new packages.

You can add or remove team members from your team, or modify their role, using the
[Jetify Cloud Dashboard](/docs/cloud/dashboard/inviting-members/)

## Authenticating from the CLI[​](#authenticating-from-the-cli "Direct link to Authenticating from the CLI")

Once you’ve been invited to a team, you can authenticate from the CLI by running:

```bash  theme={null}
devbox auth login
```

This will launch a browser window where you can authenticate with an email address or via Google
SSO.

You can check your current authentication status by running:

```bash  theme={null}
devbox auth whoami
```

You can check that you are connected to the cache, and your current cache URL, by running:

```bash  theme={null}
devbox cache info
```

You can logout by running:

```bash  theme={null}
devbox auth logout
```

### Authenticating CI or Build Hosts[​](#authenticating-ci-or-build-hosts "Direct link to Authenticating CI or Build Hosts")

Admin users can generate Personal Access Tokens to authenticate on hosts where you cannot login via
the CLI or Browser. This token will have the same push/pull permissions as the account that
generated it.

<Warning>
  Treat your Personal Access Token as a password — keep it secret and secure, and do not share it
  with other users.
</Warning>

To generate a Token, first authenticate as described above, and then run:

```bash  theme={null}
devbox auth tokens new
```

To authenticate with the personal access token, export it as an environment variable on your host:

```
export DEVBOX_API_TOKEN=<personal_token>
```


# Caching and Sharing Packages with Jetify
Source: https://www.jetify.com/docs/docs/cloud/cache/index

The  provides teams with a private, secure Nix package cache that makes it easy to share packages across all your projects and users. With the Jetify cache, you never have to rebuild a package, even if it's removed from the official .

<Info>
  If you want to use the Jetify Cache, you will need to add a payment option and upgrade your
  account to a Solo Plan or higher. For more details, see our [Plans and
  Pricing](https://www.jetify.com/cloud/pricing).
</Info>

Jetify Cache provides the following features:

* **Fast package installations**: Devbox is optimized for downloading and installing packages from
  the Jetify cache, and it can bypass costly Nix evaluation steps when installing your packages.
* **Integrates seamlessly with Devbox**: Devbox automatically configures access to the cache once
  users sign in, and packages are automatically pulled from the cache when running `devbox shell`,
  `devbox run`, or other commands.
* **Integrates with CI/CD**: Jetify Cache can generate a secure token for securely pushing and
  pulling packages in CI/CD.
* **Simple Access Control**: Devbox makes it easy to restrict which users can write to the cache,
  and makes it easy to revoke access directly from the dashboard. Jetify also supports Single Sign
  On for Enterprise Cache users

## Guides[​](#guides "Direct link to Guides")

* [Setting Up Jetify Cache](/docs/cloud/cache/authenticating/)
* [Pushing and Pulling Packages from the Cache](/docs/cloud/cache/usage/)
* [Using the Jetify Prebuilt Cache](/docs/cloud/cache/prebuilt-cache/)


# Using the Jetify Prebuilt Cache
Source: https://www.jetify.com/docs/docs/cloud/cache/prebuilt-cache/index

The Jetify Prebuilt Cache provides users with prebuilt binaries of popular packages for the most common OS(Linux, macOS) + Architecture (x86-64, aarch64) combinations.

The Jetify Prebuilt cache is intended to supplement the official NixOS Cache, and includes packages
which are not available by default. This includes:

1. Older packages that have been garbage collected
2. Packages which have not been built for certain platforms
3. Packages with unfree licenses, which are not automatically built by NixOS

## Using the Prebuilt Cache[​](#using-the-prebuilt-cache "Direct link to Using the Prebuilt Cache")

The Prebuilt Cache is available for free to every developer who signs up for a Jetify Cloud account.
Devbox will automatically configure itself to use the Prebuilt Cache when you login with
`devbox auth login`: no additional action or steps are required.

<Info>
  Free Jetify Cloud accounts are restricted to a **25 GB per month** download limit, and cannot generate access tokens for the cache.

  Solo, Starter, and Scaleup accounts have unlimited access to the Prebuilt Cache.
</Info>

## Packages included in the Prebuilt Cache[​](#packages-included-in-the-prebuilt-cache "Direct link to Packages included in the Prebuilt Cache")

Some of the packages included in the Prebuilt Cache are:

* MongoDB
* Terraform
* Vault
* DynamoDB local
* Pulumi
* Helm
* Unrar
* Graphite

More packages are added regularly. If you encounter a package that you think should be in the
Prebuilt Cache, notify us on our [Discord](https://discord.gg/jetify).


# Pushing and Pulling Packages to the Cache
Source: https://www.jetify.com/docs/docs/cloud/cache/usage/index



## Pulling Packages from the Cache[​](#pulling-packages-from-the-cache "Direct link to Pulling Packages from the Cache")

Once you have authenticated, Devbox will automatically configure your cache for you. You can also
manually configure the cache by running:

```bash  theme={null}
devbox cache configure
```

Once configured, Devbox will attempt to use the cache whenever you run a command that prompts Devbox
to install a package in your project. When installing a package, Devbox will check for a cached
binary in the following locations:

1. Your local Nix Store `/nix/store`
2. The Jetify Cache
3. The Public Nix Cache ([cache.nixos.org](https://cache.nixos.org))

If the package is not available in those locations, then it will build the package from source.

## Pushing to the Cache[​](#pushing-to-the-cache "Direct link to Pushing to the Cache")

You can push custom packages and project closures to your Jetify Cache directly from the Devbox CLI.
Push access is currently only available for authenticated users with Admin permissions.

### **Pushing a Devbox Project**[​](#pushing-a-devbox-project "Direct link to pushing-a-devbox-project")

You can push the entire closure of a Devbox project to the Jetify Cache by navigating to your
project root and running

```bash  theme={null}
devbox cache upload
```

### Pushing a specific package[​](#pushing-a-specific-package "Direct link to Pushing a specific package")

You can also push a single package by passing a flake reference to the Devbox CLI.

For example, to push a custom `mongodb` package from a custom flake.nix on your machine, you can
run:

```bash  theme={null}
devbox cache upload path:./path/to/flake.nix#mongodb
```

You can also cache packages from Github or from Nixpkgs by passing the appropriate Flake reference.
This can be useful for caching build artifacts if a package does not exist in the public Nix cache,
or if it requires you to build it from source:

```bash  theme={null}
# Cache an installable hosted on Github (process-compose)devbox cache upload github:F1bonnac1/process-compose# Cache a package from nixpkgsdevbox cache upload nixpkgs#mongodb
```


# Creating Your Team
Source: https://www.jetify.com/docs/docs/cloud/dashboard/creating-your-team/index

Developers who want to use Jetify for their personal projects can sign up for a free account. The free account comes with basic Jetify Cloud features (like Secrets), with additional features like Deployments and Cache available for purchase.

If you want to collaborate and share your projects with other members on your team, you will need to
upgrade to a **Team Account**. Team accounts let you invite other developers to share resources and
collaborate on projects in Jetify Cloud.

Users with a free account can upgrade to a paid team on the dashboard anytime.

## Creating a New Team Account[​](#creating-a-new-team-account "Direct link to Creating a New Team Account")

1. From the Team Selector in the top right of your dashboard, select **Create a New Team**

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=f27ef1ac588d09c3426d4d91a49357fe" alt="New Team" data-og-width="754" width="754" data-og-height="496" height="496" data-path="docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=6e2b1bd599d27882ca2266284811a8ed 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=9c0a9fbefceef7cbadb181fe46042e83 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=015b583ed1570de7514437c43303933a 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=3e8ed9acce69ae0fe14f6c3f94d87925 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e7443641c687bc981c4b59868ada4935 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/team-selector-dropdown.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=4cd2d1626e12eaf6f0d1f9c9348863cb 2500w" />

1. You may be prompted to sign in again. Log in with the same email or Google Account that you used
   to create your Account.

2. At the bottom of the team selection screen, enter your new Team Name and then click **Create
   Team**

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=27f3c1411c6e9d4935e70a3af1d7c0c8" alt="Create Team Form" data-og-width="1096" width="1096" data-og-height="428" height="428" data-path="docs/cloud/dashboard/creating-your-team/create-team-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=c93f812b5553f7b172e4eb81c75a74bc 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=67746b02939dcea3ff9d75d501c4f3d6 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=4a7997cf51e0e0e1cd5d14c574cb8d96 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e126b2cea1f858652bb3830cae4f3a42 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=cfbd7ffd4ca8275419088d18e7912329 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/creating-your-team/create-team-form.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=dc524e461e46bd9beb474d0a1ca84aa1 2500w" />

1. Your new team will be created, and you will be automatically switched to your new team. You can
   now [invite other members](/docs/cloud/dashboard/inviting-members/) to join your team.

## Billing[​](#billing "Direct link to Billing")

Free accounts are free forever. You will need to add a payment method to unlock paid tier features.

Team accounts are billed monthly based on the number of active members in your team. You can view
your current billing status and update your billing information from the **Billing** tab in the
Jetify Dashboard.


# Introduction
Source: https://www.jetify.com/docs/docs/cloud/dashboard/index

The  lets you manage your team, projects, and secrets from a single interface. You can use the Dashboard to manage your own hobby projects, or to collaborate with other team members.

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e7774a907b874e2a3e6451141e1a7afb" alt="Jetify Dashboard" data-og-width="5088" width="5088" data-og-height="3800" height="3800" data-path="docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e9527fe9b97884121b282efc0df21e97 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=c3e1110319cb63805e2191efffb95ae0 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=db07022f1273ec50e900ad17b7bfc849 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=4529e4ddc6d45ae9a7599e4398585b00 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=7806c101886691be2fae4cf868d02d5a 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/jetify-cloud-dashboard-overview.jpeg?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=baa1c1dafaedc860e5ba16b16f319c69 2500w" />

You can visit the Jetify Dashboard at [cloud.jetify.com](https://cloud.jetify.com)

## Guides[​](#guides "Direct link to Guides")

* [Creating Your Team](/docs/cloud/dashboard/creating-your-team/)
* [Inviting Members](/docs/cloud/dashboard/inviting-members/)
* [Managing Jetify Secrets from the Dashboard](/docs/cloud/secrets/dashboard-secrets/)


# Inviting your Team Members
Source: https://www.jetify.com/docs/docs/cloud/dashboard/inviting-members/index

If you have a paid Team project, you can invite team members to join your project. Team members can configure and use your project’s secrets when developing using the Devbox or Envsec CLI.

<Info>
  If you want to invite team members to your projects, you will need to add a payment option and
  upgrade your account to a Starter Plan. For more details, see our [Plans and
  Pricing](https://www.jetify.com/cloud/pricing).
</Info>

Team members can be added in one of two Roles:

* **Member:** Members can access or add projects, as well as access or modify the secrets for their
  projects
* **Admins:** Have all the permissions of Members, but can also invite new team members and
  configure project billing

## Adding a Team Member[​](#adding-a-team-member "Direct link to Adding a Team Member")

1. In the Jetify Dashboard, navigate to the **Members** tab

   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=c7e1ae6609a093c82893d172a4c97701" alt="Members Tab" data-og-width="2604" width="2604" data-og-height="1004" height="1004" data-path="docs/cloud/dashboard/inviting-members/members-tab-navigation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=dd5f71e19476cef8f50cced184b9a2cf 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=af6759f1c71960375694c533ded6a6c8 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=42d8b11d531ba0be650a6e96ffbc1dc7 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=2ef7791315d7a2527f9587ef505ee10f 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a2cf77b83601378a02c658a236c6755a 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/members-tab-navigation.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=bbb1568c4d461dda3eb6a47b32a416c7 2500w" />

2 . To invite a member, enter their email address, and the **Role** you want to assign to them.

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=688a504c5eab93e9010c748fe0d06a83" alt="Inviting a Member" data-og-width="1646" width="1646" data-og-height="536" height="536" data-path="docs/cloud/dashboard/inviting-members/invite-member-form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=54b6042c4499db3cc2b01a8a8acd3463 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=01a1ecf4c800307b528b1f55d3020834 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=fbd7c8f05e070d51594a67841cb0d548 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=9c07c98eac04c8882015a5ccad293e65 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=72e800aef16a67050600ea1c1c44621d 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/invite-member-form.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0ba5b5dc177e75317b5ece032cc38e0f 2500w" />

1. Once invited, users will receive an email with instructions on how to join your team. They will
   show up in the **Members** tab as invited until they accept the invitation:

   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=19adda3c43457aa02c9dbb1c08a52822" alt="Invited Member" data-og-width="1578" width="1578" data-og-height="164" height="164" data-path="docs/cloud/dashboard/inviting-members/member-status-invited.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e321c12ef18a385e00533e379280a7f3 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b3a8d1a75624264cdaada33d3e5b5822 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=c1937cf8905652662144f8ea60ed1ef4 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=1836ddb4059f7be5a30e7cebb255dd30 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=aa27f7bfbae5f33bf0197820f47bda4a 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-invited.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0180edbf1286c585b2c591b3dc7b9b2b 2500w" />

   Note that invitations will expire if they are not accepted within 7 days, after which you will
   need to re-send the invitation.

   Once they accept the invitation, they will switch to **active**

   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=878745ccef2b6b45a5fd85e6786e0b28" alt="Active Member" data-og-width="1598" width="1598" data-og-height="190" height="190" data-path="docs/cloud/dashboard/inviting-members/member-status-active.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=11edd2f12ede11b4112e18ab27fd2435 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=1936de197869b1acdb4a21746d5b02d7 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=acfc7389067612ed91caaa3ac6f619da 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=22544bb915c497117e83c8908444424f 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=107e58d9d0038244fb1fc804e7160f5d 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/member-status-active.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a4c248b44e3ab79c00a2bc08f26cea8d 2500w" />

## Removing a Team Member[​](#removing-a-team-member "Direct link to Removing a Team Member")

Removing a team member will remove their access to all projects and secrets in your team. To remove
a team member

1. Navigate to the Members tab on the Jetify Dashboard
2. Click the Options button to the right of the member's name
3. Select Delete from the pop up that appears:

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d1ec459866679fef9f7c3e1c6bee442e" alt="Delete a member" data-og-width="1698" width="1698" data-og-height="256" height="256" data-path="docs/cloud/dashboard/inviting-members/delete-member-action.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=3de5809aed2913889cdcdb2287566982 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=22fd969c154544fd6e97a414bc854ecc 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=62caedc48213561bc8aa94dcb2e2119f 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=7b3d3c342eddb21aa2654b1dff8deba3 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=451c533459b0bd814c94177c0241ddd9 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/dashboard/inviting-members/delete-member-action.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0e4ee9eed10666693d8b8beafc1aff1c 2500w" />

1. Click **OK** on the confirmation window that appears to confirm that you want to remove the
   member from your team


# Setting a Custom Domain for your Project
Source: https://www.jetify.com/docs/docs/cloud/deploys/custom-domains/index

Jetify Cloud will automatically configure a unique, private domain for previewing your deployed application. For production purposes, you will probably want to add a more user friendly domain to route users to your application. Jetify will also configure and issue an SSL certificate for your domain automatically.

<Info>
  You will need access to the DNS records for your Domain in order to configure it for Jetify Cloud.
</Info>

## Adding a Custom Domain[​](#adding-a-custom-domain "Direct link to Adding a Custom Domain")

1. In your project on the Jetify Cloud Dashboard, select **Settings**
2. Scroll down to the **Custom Domain** section on the settings page
   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=15b1013bbeab92c120293169def8c738" alt="Custom Domain Section" data-og-width="2056" width="2056" data-og-height="814" height="814" data-path="docs/cloud/deploys/custom-domains/custom-domain-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=1559e90cabb3e82ab61dbc5b1c695630 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=67a3d971aa5d03eca551c794d1a3c3f1 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a7e3923c8d39abf6820c948d6f2c563b 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=335f97b598c5cb7271700ef5e5662ad6 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=6b56240b8158ebd8cf6859a03c57e503 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-settings.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b70201903b83b4be0f29869db9c3a747 2500w" />
3. Enter the custom domain name that you would like to use for your project
4. After you click confirm, your custom domain will be set in a pending state. To validate the
   domain, you will need to add a record to your DNS provider:
   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d415e76ce4c98b77c87260eb022b1c7a" alt="Pending custom domain" data-og-width="2024" width="2024" data-og-height="830" height="830" data-path="docs/cloud/deploys/custom-domains/custom-domain-status-pending.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=31e0213a3c1d8691b09f3e065d1a54f8 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=13801b909e15176633f3c83a612ac6e8 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d19667a54eb48d20ad1d0efb129a9c73 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e603858352db8e8fdfe960329d98b54d 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=6ce68da8dd8da0c7ede0a5c7ce06871f 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-pending.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=cf5240f1b1205fb89b75e65ee6417497 2500w" />
5. Once the correct records have been added to your DNS provider, your Custom Domain will display an
   **Issued** status:
   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0a297b8005bca8e131cc4d89b96cce10" alt="Custom Domain Issued" data-og-width="1990" width="1990" data-og-height="786" height="786" data-path="docs/cloud/deploys/custom-domains/custom-domain-status-issued.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=eeed6c82a897c3a1f6c65844c36b5dc1 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=28c4b30259e70327c058daf75e7ebcf2 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=569f6e2222b1536fecd5346fad442858 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=8b52ba06ab6fe7ae3b028cc9bcaf0739 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=4d98fff6dc90a2fadc152896c4afa820 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/custom-domains/custom-domain-status-issued.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=adb0af1e9bfd896ff6c3bee832dcd664 2500w" />

## Removing a Custom Domain[​](#removing-a-custom-domain "Direct link to Removing a Custom Domain")

You can remove a custom domain by clicking the Delete button. This will remove the domain from your
project. Note that after removing the domain, you may want to also clean up your DNS records.


# Introduction
Source: https://www.jetify.com/docs/docs/cloud/deploys/index

Jetify Deployments is an easy, Devbox friendly way to deploy a stateless application to the cloud in a few minutes. Jetify can build and run any Docker container, and provides easy tools for configuring your project's secrets, custom domains, and more. Jetify connects to your projects Github repo to ensure that you always have the latest version of your application deployed.

<Info>
  If you want to invite team members to your projects, you will need to add a payment option and
  upgrade your account to a Solo Plan or higher. For more details, see our [Plans and
  Pricing](https://www.jetify.com/cloud/pricing).
</Info>

## Quickstart[​](#quickstart "Direct link to Quickstart")

This quickstart will walk through how to configure and deploy a project with Jetify Cloud. We'll
start by forking an example repo that is configured for Jetify Deployments, and then demonstrate how
to connect your Github repo and activate deploys for your account.

## Forking the Example Repo[​](#forking-the-example-repo "Direct link to Forking the Example Repo")

To help you get started with Jetify Cloud, we've created an
[example Rails app](https://github.com/jetify-com/jetify-deploy-example) that's been configured to
deploy with Jetify Cloud.

You can fork this repo from the Github UI to add it to your account, or clone and push the repo to
your Github account.

## Connecting your Repo to Jetify Cloud[​](#connecting-your-repo-to-jetify-cloud "Direct link to Connecting your Repo to Jetify Cloud")

First, you'll need to sign-in with Github and connect your project to Jetify Cloud:

1. From the Create Project screen, select Continue with Github to sign in with Github
2. Select a Github Org to import your project from. If you are only a member of one org, it will be
   selected for you by default.
   1. If this is your first time importing a project from your org, you will need to install the
      Devbox Cloud app to provide access to your project
3. Select a Repository to import your repo. If your project is not in the root directory of your
   repository, you can specify a subdirectory for Jetify to search for your project.

Once your project is added to Jetify Cloud, you can configure your secrets or deployments.

## Deploying your Site[​](#deploying-your-site "Direct link to Deploying your Site")

1. Select the Deploys tab in your project
2. Click the **Enable Deployments** button to turn on Jetify Deployments for your project
3. Once activated, Jetify will automatically attempt to deploy your repository. You can select the
   deployment to view its status and build logs

If your site fails to deploy, or if you want to update your deployment, push a commit to the default
branch of your repo to trigger a new deploy.

## Visiting your Site[​](#visiting-your-site "Direct link to Visiting your Site")

When your site has finished deploying, Jetify Cloud will display a preview URL that you can visit to
test your application.

Congratulations! You've now deployed your first site with Jetify Cloud.

## Next Steps[​](#next-steps "Direct link to Next Steps")

* Learn more about [setting up your project](/docs/cloud/deploys/setup/)
* Set up a [custom domain](/docs/cloud/deploys/custom-domains/) for your application
* Learn how to setup databases, caches, and other [integrations](/docs/cloud/deploys/integrations/)


# Integration Guides
Source: https://www.jetify.com/docs/docs/cloud/deploys/integrations/index

This section contains guides on how to integrate common services with your Jetify deployments.

* [PostgresQL with Supabase](/docs/cloud/deploys/integrations/supabase/)
* [Redis with Upstash](/docs/cloud/deploys/integrations/upstash/)
* [Object Storage with S3](/docs/cloud/deploys/integrations/s3/)


# Monitoring Your Deployments
Source: https://www.jetify.com/docs/docs/cloud/deploys/monitoring-deploys/index

Jetify Cloud automatically provides build and runtime logs for each of your deployments in the Jetify Dashboard.

## Build Logs[​](#build-logs "Direct link to Build Logs")

Build logs include all the logs generated when cloning, building, and uploading your project to
Jetify's Docker Registry. You can check the build logs to see why a build or deployment failed, or
to identify bottlenecks in the build process. Build logs automatically stream in realtime.

You can view the build logs for a specific deployment by selecting the deployment, and then
expanding the Build logs section

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e2638b22168c2bcc05642f41dd46c272" alt="Build logs" data-og-width="3026" width="3026" data-og-height="2150" height="2150" data-path="docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=8c382f223e8a002c0143ff80659ca332 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0fe1de6aae899c938da5e591d708e75e 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=634a4b57b1685b05269066b9c8016c0b 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=f7e4c74c4beb69c3edbe1d50fc5a4ec6 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=fe40500aab09107f9478c1433e36c757 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-build-logs.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ab065d424d12f00d46097c00bd56b7eb 2500w" />

## Runtime Logs[​](#runtime-logs "Direct link to Runtime Logs")

Runtime logs capture everything that has happened in your application after it is deployed to the
Jetify Cloud. You can use these logs to for testing and debugging server-side errors, or for
understanding why a given deployment has failed to start.

Runtime logs stream in realtime, and Devbox retains the last 24 hours of runtime logs for each of
your deployments.

You can view your Runtime Logs by clicking the **Runtime Logs** tab in your Deployment Details page:

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0516e122c8504011fc9623837ad0a6a6" alt="Runtime Logs" data-og-width="2100" width="2100" data-og-height="1554" height="1554" data-path="docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=3eeedeadd2f602dbfa1ba785c27d5a41 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=fb241d8245900b1dca3ece145d726950 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=22b66eeda57acab20314e643cc2f3215 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d5b86907e9b2a558ac9666856d441388 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a330744a310632aed33dba69032e53af 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/monitoring-deploys/deployment-runtime-logs.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d187d3ef9e587cbd9a8d09c7d2a895c2 2500w" />

## Preview URL[​](#preview-url "Direct link to Preview URL")

In addition to build and runtime logs, Jetify Cloud automatically generates a randomized preview URL
that you can use to test your application, or to share a preview of the deployment with other users
and developers. Each deployment receives a unique preview URL.

To preview your deployment, click the **View** button on the Deployment Details page.


# Using Jetify Secrets with your Deployment
Source: https://www.jetify.com/docs/docs/cloud/deploys/secrets/index

Projects deployed with Jetify Cloud are automatically configured to use  when deploying your project. You do not need to authenticate, or add any additional configuration to use your secrets. Your project will deploy using the  environment for your secrets by default.

For more details on how to configure secrets, see:

* [Jetify Secrets Overview](/docs/cloud/secrets/)
* [Setting Secrets from the CLI](/docs/cloud/secrets/secrets-cli/)
* [Setting Secrets from the Dashboard](/docs/cloud/secrets/dashboard-secrets/)


# Setting Up Your Deployment
Source: https://www.jetify.com/docs/docs/cloud/deploys/setup/index



## Configuring your Project[​](#configuring-your-project "Direct link to Configuring your Project")

Deploying a project with Jetify Cloud requires the following:

1. **A devbox.json or Dockerfile**: If your project contains a `devbox.json` file, devbox will
   automatically generate a Dockerfile that can be used to deploy your application to Jetify Cloud.
   You can also check in a custom Dockerfile if you want to precisely control how your project is
   built
2. **A Service Listening on 8080**. Jetify automatically forwards requests to port 8080 on your
   running container, so you will need to ensure that your service is listening to that port. We
   also recommend setting your service host to `0.0.0.0`.

### Deploying with a devbox.json[​](#deploying-with-a-devboxjson "Direct link to Deploying with a devbox.json")

Jetify Cloud can use your `devbox.json` to generate a Docker container that will install your
project dependencies and run your projects. In addition to installing your packages, Jetify will
also look for and attempt to run any `install`, `build`, and `start` scripts defined in your
devbox.json:

* The **install script** will run after your base container has been initialized and your Nix
  packages are installed. This stage should be used to download and build your application's
  dependencies
* The **build script** runs after the install stage, and should be used to build or bundle your
  application.
* The **start script** will run as your container's entrypoint. This stage should include any
  commands needed to start and run your application.

Below is an example `devbox.json` that can be used for a simple Go project in Jetify Cloud:

```json  theme={null}
{
  "packages": ["[email protected]"],
  "env": {
    "GOPATH": "$HOME/go/",
    "PATH": "$PATH:$HOME/go/bin"
  },
  "shell": {
    "init_hook": ["export \"GOROOT=$(go env GOROOT)\""],
    "scripts": {
      "install": "go get ./...",
      "build": "go build -o main.go",
      "start": "go run",
      "run_test": "go run main.go"
    }
  }
}
```

In this case, Jetify Cloud will first install Devbox and all the packages, then run the `install`
and `build` scripts (in that order), and the use `start` as the entrypoint to the application.

You can preview how Jetify will run the project using `devbox generate dockerfile --for prod`

### Deploying with a Custom Dockerfile[​](#deploying-with-a-custom-dockerfile "Direct link to Deploying with a Custom Dockerfile")

If your repo contains a Dockerfile, Jetify Cloud will use that Dockerfile to deploy your service
(even if the project also contains a devbox.json). Your Dockerfile should define an entrypoint that
Jetify can run upon deploying, as well as listen on port 8080.

## Connecting your Repo[​](#connecting-your-repo "Direct link to Connecting your Repo")

Jetify requires you to connect a Github repo in order to deploy your service. To access private
repositories, you will need to install the Devbox Cloud Github app in your repository:

1. From the Create Project screen, select Continue with Github to sign in with Github
2. Select a Github Org to import your project from. If you are only a member of one org, it will be
   selected for you by default.
   1. If this is your first time importing a project from your org, you will need to install the
      Devbox Cloud app to provide access to your project
3. Select a Repository to import your repo. If your project is not in the root directory of your
   repository, you can specify a subdirectory for Jetify to search for your project.

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=3de3d226c4430571d583eddf37afc9f0" alt="Select the Repo for your Jetify Project" data-og-width="3026" width="3026" data-og-height="2150" height="2150" data-path="docs/cloud/deploys/setup/select-repository-for-project.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b8646d2b1fe7a9a349c476434867f294 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=2dce4487c00eaae12711ab10c5566dbd 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=4f699372152e8499aa59913afd741347 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d59285077bf3c56f014b65809ca8ed74 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=18ae13aa833461baa7b546e7bfbe1fb2 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/deploys/setup/select-repository-for-project.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=c7ffbe0c35c40938d764bde12134a75d 2500w" />

## Choosing an Instance Size[​](#choosing-an-instance-size "Direct link to Choosing an Instance Size")

Jetify will default your deployment to the smallest instance size (0.1 CPU + 512MB RAM). To choose a
different size:

1. Navigate to the **Settings** tab of your project
2. Scroll down to **Deployments**
3. Choose the Machine configuration that best matches your project's needs.

Changes to your instance size will take effect on the next deployment.

## Deleting your Project[​](#deleting-your-project "Direct link to Deleting your Project")

If you no longer want to deploy your project with Jetify Deploys, you can disable deployments in the
Settings tab of your project.


# Frequently Asked Questions
Source: https://www.jetify.com/docs/docs/cloud/faq/index

This doc contains answers to frequently asked questions about Jetify Cloud that are not covered elsewhere in our documentation. If you have a question that isn't covered here, feel free to ask us on our

## Do I have to pay to use Jetify Cloud?[​](#do-i-have-to-pay-to-use-jetify-cloud "Direct link to Do I have to pay to use Jetify Cloud?")

Jetify accounts are free for individual developers, and includes access to Jetify Secrets and the
Jetify Prebuilt Cache.

Using Jetify with a team requires a paid Jetify Solo, Starter, or Scale-up account. For details on
other plans and limits, see our [**pricing**](https://www.jetify.com/cloud/pricing) page.

## How can I share my Jetify Cloud project with other developers?[​](#how-can-i-share-my-jetify-cloud-project-with-other-developers "Direct link to How can I share my Jetify Cloud project with other developers?")

To share secrets and access to deployments with other team members, you will need to create a new
Jetify Starter Team and then invite developers to join your team. See the
[cloud dashboard docs](/docs/cloud/dashboard/creating-your-team/) for more details.

## How do Jetify Cloud Plans work?[​](#how-do-jetify-cloud-plans-work "Direct link to How do Jetify Cloud Plans work?")

Jetify Cloud Plans are available for a monthly platform fee, and allow you to share your Jetify
Cloud resources with your team, along with increased support levels. All plans include usage credits
equal to the monthly platform fee, which are billed at standard usage rates.

For more details, see our [**pricing**](https://www.jetify.com/cloud/pricing) page.

## Do you offer self-hosted or private instances of Jetify Cloud?[​](#do-you-offer-self-hosted-or-private-instances-of-jetify-cloud "Direct link to Do you offer self-hosted or private instances of Jetify Cloud?")

We offer private instances and other features as part of our Enterprise Plan.
[Contact us](https://calendly.com/d/3rd-bhp-qym/meet-with-the-jetify-team) so we can build a
solution that meets your needs.

## How does pricing for Jetify Cache work?[​](#how-does-pricing-for-jetify-cache-work "Direct link to How does pricing for Jetify Cache work?")

The Jetify Prebuilt Cache is included in your subscription for no additional cost.

Jetify Private Cache costs $0.60/GB of storage per month for the first 50 GB, and $0.50/GB per month
after that. Jetify Private cache does not charge for bandwidth or downloads.

## My project needs a custom instance size or scaling policy[​](#my-project-needs-a-custom-instance-size-or-scaling-policy "Direct link to My project needs a custom instance size or scaling policy")

We can customize Jetify Deployments for your project's needs.
[Contact us](https://calendly.com/d/3rd-bhp-qym/meet-with-the-jetify-team) for help with a
customized solution.


# Cloud Documentation
Source: https://www.jetify.com/docs/docs/cloud/index

Jetify Cloud gives your team the tools and frameworks to accelerate your development workflow. Jetify Cloud is built on top of , a powerful tool for spinning up reproducible, isolated development environments on any machine.

<Info>
  Jetify Cloud is currently available in Early Access. We're actively working on adding new features
  and improving the platform. To learn more, share your feedback, or follow our progress, join our
  [Discord Channel](https://discord.gg/jetify).
</Info>

Jetify Cloud currently includes:

**[Jetify Cache](/docs/cloud/cache/)**: Provides a secure, private cache to share packages across
all your Devbox projects and environments, whether sourced from Nixpkgs or Flakes. Avoid rebuilding
custom packages locally or in CI.

**[Jetify Secrets](/docs/cloud/secrets/)**: Securely store secrets and variables for all of your
environments, and automatically synchronize them with your Devbox Shells and Scripts.

More features are coming soon, keep an eye on our [**blog**](https://www.jetify.com/blog) for future
updates!

## Getting Started[​](#getting-started "Direct link to Getting Started")

* Speed up your dev environments with [**Jetify Cache**](/docs/cloud/cache/)
* Integrate Secrets with your Devbox project using [**Jetify Secrets**](/docs/cloud/secrets/)
* Learn how to [**create your team**](/docs/cloud/dashboard/creating-your-team/) and
  [**invite members**](/docs/cloud/dashboard/inviting-members/)


# Managing Secrets from the Dashboard
Source: https://www.jetify.com/docs/docs/cloud/secrets/dashboard-secrets/index

You can add or manage secrets for a Jetify Cloud project using the Secrets tab of the Jetify Dashboard. Secrets that you set in the Dashboard will be automatically available when an authenticated member of your team uses Devbox to start a shell, script, or service in the application.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

To manage secrets from the Jetify Cloud Dashboard, you must first:

1. Add the project to your Jetify Cloud account
2. Initialize the project to use Jetify Secrets

## Adding a Secret[​](#adding-a-secret "Direct link to Adding a Secret")

1. From the Jetify Dashboard, select the project whose secrets you want to manage
2. Navigate to the Secrets tab of the Jetify Dashboard
   <img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a146c5c309e4b6e2a464301bab9290ba" alt="Jetify Dashboard Secrets Tab" data-og-width="2366" width="2366" data-og-height="1202" height="1202" data-path="docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a64e7894ef9b9202cc6a00e4ced2a4fd 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ea581430b41ff5968184fa41c52d0518 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=87e58f610512f3fb5ad8829999d0efd0 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=be8b6b04983d0fdaca7446acb79d8953 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a7f40d39014ba1587eafa5f509043561 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/secrets-tab-navigation.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=a5a091224b9d9ad28399f24fd0373472 2500w" />
3. To create a new secret, enter the key name of the secret, along with the value that you want to
   set in the form. Note that secrets are set as environment variables, so the key name must be a
   valid environment variable name.
4. You can also use the Environment checkboxes to set the secret for a specific environment. By
   default, secrets are set for the `Development` environment, but you can also set secrets for a
   `Preview` and `Prod` environment.
5. To add multiple secrets at one time, click the **Add Another** button
6. When you are finished adding secrets, click the **Submit** button

## Updating and Managing Secrets[​](#updating-and-managing-secrets "Direct link to Updating and Managing Secrets")

You can update or manage secrets by clicking the edit button next to the secret that you want to
update. This will open a modal where you can update the value of the secret, or delete the secret
entirely.

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=d375aea5783f0b57e71f857afb9d7298" alt="Editing Secrets" data-og-width="2476" width="2476" data-og-height="940" height="940" data-path="docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=14f174f0bc803aac759d2901e35e395c 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=1b4f90c0ee3ce00e57461e8289c3e5db 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ddc17e9dba22520a96c87e2fc6b42ebc 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ac856db64eccfaee5b9e0fc770b677b7 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=65e40ce451fbab9e0611d6e6cee803e3 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/dashboard-secrets/edit-secrets-interface.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b55635fce3ad5ff33f757a7c98547894 2500w" />

## Further Reading[​](#further-reading "Direct link to Further Reading")

* [Managing Secrets with the Devbox CLI](/docs/cloud/secrets/secrets-cli/)


# Introduction
Source: https://www.jetify.com/docs/docs/cloud/secrets/index

Jetify Secrets is a secure secrets management service that lets you store and access secrets for your projects. Secrets are encrypted and stored in the cloud, and are automatically accessed by your project's Devbox environment whenever you start a shell, run a script, or start a service.

## Key Concepts[​](#key-concepts "Direct link to Key Concepts")

Jetify provides an easy way to manage secrets for your projects. To get started, it’s helpful to
understand the following key concepts:

**Project** - A Jetify project is a git repo that contains a `devbox.json` file. You can add a
project to your Jetify Cloud account by running `devbox secrets init` in the root of your project.
Once a project is added to your Jetify Cloud account, you can use Jetify Secrets to manage secrets
for that project.

**Secrets** - Secrets are key-value pairs that are stored securely in the Jetify Secret store. They
automatically set as environment variables in your Devbox project whenever you start a shell, run a
script, or start a service. Secrets are encrypted at rest and in transit, and are only decrypted
when they are accessed by your Devbox environment or by a user in your Jetify Cloud team.

**Environment** - An environment is a set of secrets that are available to your project. By default,
all secrets are set on the `Development` environment, but Devbox also lets you set secrets for a
`Preview` and `Production` environment. Starting a shell or running a script in a specific
environment gives you access to all the secrets that are set for your environment.

## Getting Started[​](#getting-started "Direct link to Getting Started")

To learn how to set secrets from the Jetify Dashboard, see our
[Dashboard Secrets](/docs/cloud/secrets/dashboard-secrets/) guide.

To learn how to use your Secrets with Devbox and manage your secrets from the command line, see our
[Secrets CLI Guide](/docs/cloud/secrets/secrets-cli/).


# Managing Secrets with the Devbox CLI
Source: https://www.jetify.com/docs/docs/cloud/secrets/secrets-cli/index

You can access your Jetify Secrets locally using Devbox. When you authenticate your Devbox CLI with Jetify Cloud, Devbox will automatically identify your project, and make your secrets available in your Devbox shell. Developers who are part of your Jetify Cloud team can also access your project’s secrets automatically, whenever they use devbox to start a shell, run a script, or launch a service

If you don't already have Devbox installed, see our
[Quickstart](https://www.jetify.com/docs/devbox/quickstart/) guide to get started.

## Authenticating with Devbox[​](#authenticating-with-devbox "Direct link to Authenticating with Devbox")

You can authenticate with Jetify Cloud by running `devbox auth login`. This will launch the browser
authentication flow to sign into Jetify Cloud.

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=9464344a973716038c113405085b7278" alt="Auth Page" data-og-width="1870" width="1870" data-og-height="1354" height="1354" data-path="docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b7095ddef632b95c83fe8d805493c904 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=7c6f55e6382a9d604eba8373ab6e71c3 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ab1f2bf6a46736b6e7dd1fdf78b4d26a 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=f95165ec98e215e97d6fe98aba644a9f 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=3b51201a292d4bb77c4e40aad0d8e357 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/cloud/secrets/secrets-cli/jetify-authentication-page.jpeg?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b142095c5e91bff966e1ebc697c9c74e 2500w" />

Once you complete the authentication flow and select a team, the Devbox CLI will configure itself to
use the team you selected

## Integrating a project with devbox secrets[​](#integrating-a-project-with-devbox-secrets "Direct link to Integrating a project with devbox secrets")

To create a new project on Jetify Cloud, navigate to the root directory of your project and run
`devbox secrets init`

```bash  theme={null}
/Users/puckworth/my-project❯ devbox secrets init
? Setup project in /Users/puckworth/my-project? Yes
Initializing project in org
? What's the name of your new project? my-test-project
Created project my-test-project in org
```

Running `devbox secrets init` will create a new project in your current Jetify Cloud account and
org, and configure your project to use Jetify Secrets. The project should also be visible if you
navigate to the [Jetify Dashboard](/docs/cloud/dashboard/).

## Adding Secrets to your Project[​](#adding-secrets-to-your-project "Direct link to Adding Secrets to your Project")

### Adding Secrets from the Command Line[​](#adding-secrets-from-the-command-line "Direct link to Adding Secrets from the Command Line")

You can set secrets using `devbox secrets set`:

```bash  theme={null}
devbox secrets set FOO=BAR
```

```text  theme={null}
[DONE] Set environment variable 'FOO' in environment: dev
```

By default, variables will be set on the `dev` environment. You can set secrets on other
environments by passing the `--environment` flag:

```bash  theme={null}
devbox secrets set FOO=BAR --environment prod
```

Supported environments include `dev`, `preview`, and `prod`.

### Adding Secrets from a File[​](#adding-secrets-from-a-file "Direct link to Adding Secrets from a File")

You can bulk add secrets from a file by using `devbox secrets import`:

```bash  theme={null}
devbox secrets import .env.dev
[DONE] Uploaded 3 environment variable(s) from file '.env.dev' to environment: dev
```

The file should follow the `.env` format, with each line containing a single environment variable in
the form:

```bash  theme={null}
VARIABLE_NAME=VARIABLE_VALUE
```

## Viewing your Project's Secrets

You can view your project's secrets by running `devbox secrets ls`:

```text  theme={null}
Environment: dev
+-----------------+-------+
|      NAME       | VALUE |
+-----------------+-------+
| FOO             | ***** |
| DEV_SERVER      | ***** |
| PG_PASSWORD     | ***** |
+-----------------+-------+

Environment: prod
+-----------------+-------+
|      NAME       | VALUE |
+-----------------+-------+
| FOO             | ***** |
| PG_PASSWORD     | ***** |
+-----------------+-------+

Environment: preview
+-----------------+-------+
|      NAME       | VALUE |
+-----------------+-------+
| FOO             | ***** |
| PG_PASSWORD     | ***** |
+-----------------+-------+
```

## Accessing your Secrets from a Devbox Shell[​](#accessing-your-secrets-from-a-devbox-shell "Direct link to Accessing your Secrets from a Devbox Shell")

Once your project is configured for Jetify Cloud, Devbox will automatically check whether the
project exists in your Jetify Cloud account based on:

1. Your current project’s Git repository
2. The subfolder where your `devbox.json` is located

If you have a matching project in your Jetify Cloud account, Devbox will automatically set your
secrets as environment variables whenever you:

1. Start a `devbox shell`
2. Start services with `devbox services up` or `devbox services start`
3. Run a script with `devbox run`

## Removing a Secret from your Project[​](#removing-a-secret-from-your-project "Direct link to Removing a Secret from your Project")

You can remove a secret from your project by running `devbox secrets rm`:

```bash  theme={null}
devbox secrets rm FOO
[DONE] Deleted environment variable 'FOO' in environment: dev
```

## Exporting Secrets to a File[​](#exporting-secrets-to-a-file "Direct link to Exporting Secrets to a File")

You can export your secrets to a `.env` file using `devbox secrets download`:

```bash  theme={null}
devbox secrets download .env
[DONE] Downloaded environment variables to '.env' for environment: dev
```

You can download from a specific environment using the `--environment` flag:

## Further Reading[​](#further-reading "Direct link to Further Reading")

* [Devbox Secrets CLI Reference](/docs/devbox/cli-reference/devbox-secrets/)
* [Managing Secrets from the Dashboard](/docs/cloud/secrets/dashboard-secrets/)


# devbox add
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-add/index

Add a new package to your devbox

```bash  theme={null}
devbox add <pkg>... [flags]
```

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Add the latest version of the `ripgrep` package
devbox add ripgrep

# Install glibcLocales only on x86_64-linux and aarch64-linux
devbox add glibcLocales --platform x86_64-linux,aarch64-linux

# Exclude busybox from installation on macOS
devbox add busybox --exclude-platform aarch64-darwin,x86_64-darwin

# Install non-default outputs for a package, such as the promtool CLI
devbox add prometheus --outputs=out,cli
```

## Options[​](#options "Direct link to Options")

| Option                           | Description                                                                                                            |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `--allow-insecure`               | allows Devbox to install a package that is marked insecure by Nix                                                      |
| `-c, --config string`            | path to directory containing a devbox.json config file                                                                 |
| `--disable-plugin`               | disable the build plugin for a package                                                                                 |
| `--environment string`           | Jetify Secrets environment to use, when supported (e.g.secrets support dev, prod, preview.) (default "dev")            |
| `-e, --exclude-platform strings` | exclude packages from a specific platform.                                                                             |
| `-h, --help`                     | help for add                                                                                                           |
| `-o, --outputs strings`          | specify the outputs to install for the nix package                                                                     |
| `-p`, `--platform strings`       | install packages only on specific platforms.                                                                           |
| `--patch`                        | Allow Devbox to patch your packages to fix issues with missing native libraries (auto, always, never) (default "auto") |
| `-q, --quiet`                    | quiet mode: Suppresses logs.                                                                                           |

Valid Platforms include:

* `aarch64-darwin`
* `aarch64-linux`
* `x86_64-darwin`
* `x86_64-linux`

The platforms below are also supported, but will build packages from source

* `i686-linux`
* `armv7l-linux`

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-add.md)


# devbox cache configure
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-cache-configure/index

Configure Nix to use the Devbox cache as a substituter.

If the current Nix installation is multi-user, this command grants the Nix daemon access to Devbox
caches by making the following changes:

* Adds the current user to Nix's list of trusted users in the system nix.conf.
* Adds the cache credentials to \~root/.aws/config.

Configuration requires sudo, but only needs to happen once. The changes persist across Devbox
accounts and organizations.

This command is a no-op for single-user Nix installs that aren't running the Nix daemon.

```bash  theme={null}
  devbox cache configure [flags]
```

## Options[​](#options "Direct link to Options")

| Option          | Description                                                     |
| --------------- | --------------------------------------------------------------- |
| `--user string` | The OS user to configure Nix for. Defaults to the current user. |
| `-h, --help`    | help for configure                                              |
| `-q, --quiet`   | suppresses logs                                                 |

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-cache-configure.md)


# devbox cache info
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-cache-info/index

Output information about the nix cache

```bash  theme={null}
  devbox cache info [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for info   |
| `-q, --quiet` | suppresses logs |

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-cache-info.md)


# devbox cache upload
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-cache-upload/index

Upload specified nix installable or nix packages in current project to cache. If [installable] is provided, only that installable will be uploaded. Otherwise, all packages in the project will be uploaded. To upload to specific cache, use --to flag. Otherwise, a cache from the cache provider will be used, if available.

```bash  theme={null}
devbox cache upload [installable] [flags]
```

## Aliases[​](#aliases "Direct link to Aliases")

upload, copy

## Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for upload                                        |
| `--to string`         | URI of the cache to copy to                            |
| `-q, --quiet`         | suppresses logs                                        |

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-cache-upload.md)


# devbox cache
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-cache/index

A collection of commands to interact with the Jetify Cache or other Nix caches.

```bash  theme={null}
  devbox cache [command]
```

## Subcommands[​](#subcommands "Direct link to Subcommands")

info Output information about the nix cache upload specified or nix packages in current
project to cache

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for cache  |
| `-q, --quiet` | suppresses logs |

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-cache.md)


# devbox completion bash
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-completion-bash/index

Generate the autocompletion script for the bash shell.

This script depends on the 'bash-completion' package. If it is not installed already, you can
install it via your OS's package manager.

To load completions in your current shell session:

```bash  theme={null}
	source <(devbox completion bash)
```

To load completions for every new session, execute once:

## Linux[​](#linux "Direct link to Linux")

```bash  theme={null}
	devbox completion bash > /etc/bash_completion.d/devbox
```

## macOS[​](#macos "Direct link to macOS")

```bash  theme={null}
devbox completion bash > \
  $(brew --prefix)/etc/bash_completion.d/devbox
```

You will need to start a new shell for this setup to take effect.

```bash  theme={null}
devbox completion bash
```

## Options[​](#options "Direct link to Options")

| Option              | Description                     |
| ------------------- | ------------------------------- |
| `-h, --help`        | help for bash                   |
| `--no-descriptions` | disable completion descriptions |
| `-q, --quiet`       | suppresses logs                 |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox completion](/docs/devbox/cli-reference/devbox-completion/) - Generate the autocompletion
  script for the specified shell

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-completion-bash.md)


# devbox completion fish
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-completion-fish/index

Generate the autocompletion script for the fish shell.

To load completions in your current shell session:

```bash  theme={null}
devbox completion fish | source
```

To load completions for every new session, execute once:

```bash  theme={null}
devbox completion fish > ~/.config/fish/completions/devbox.fish
```

You will need to start a new shell for this setup to take effect.

```bash  theme={null}
devbox completion fish [flags]
```

## Options[​](#options "Direct link to Options")

| Option              | Description                     |
| ------------------- | ------------------------------- |
| `-h, --help`        | help for fish                   |
| `--no-descriptions` | disable completion descriptions |
| `-q, --quiet`       | suppresses logs                 |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox completion](/docs/devbox/cli-reference/devbox-completion/) - Generate the autocompletion
  script for the specified shell

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-completion-fish.md)


# devbox completion zsh
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-completion-zsh/index

Generate the autocompletion script for the zsh shell.

If you are using Oh My Zsh, just run the following:

```bash  theme={null}
mkdir -p ~/.oh-my-zsh/completions
devbox completion zsh > ~/.oh-my-zsh/completions/_devbox
```

If you are not using Oh My Zsh and shell completion is not already enabled in your environment you
will need to enable it. You can execute the following once:

```
echo "autoload -U compinit; compinit" >> ~/.zshrc
```

To load completions in your current shell session:

```bash  theme={null}
source <(devbox completion zsh); compdef _devbox devbox
```

To load completions for every new session, execute once:

## Linux[​](#linux "Direct link to Linux")

```bash  theme={null}
devbox completion zsh > "${fpath[1]}/_devbox"
```

## macOS[​](#macos "Direct link to macOS")

```bash  theme={null}
devbox completion zsh > \
  $(brew --prefix)/share/zsh/site-functions/_devbox
```

You will need to start a new shell for this setup to take effect.

```bash  theme={null}
devbox completion zsh [flags]
```

## Options[​](#options "Direct link to Options")

| Option              | Description                     |
| ------------------- | ------------------------------- |
| `-h, --help`        | help for zsh                    |
| `--no-descriptions` | disable completion descriptions |
| `-q, --quiet`       | suppresses logs                 |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox completion](/docs/devbox/cli-reference/devbox-completion/) - Generate the autocompletion
  script for the specified shell

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-completion-zsh.md)


# devbox completion
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-completion/index

Generate the autocompletion script for the specified shell

## Synopsis[​](#synopsis "Direct link to Synopsis")

Generate the autocompletion script for devbox for the specified shell. See each sub-command's help
for details on how to use the generated script.

## Options[​](#options "Direct link to Options")

| Option        | Description         |
| ------------- | ------------------- |
| `-h, --help`  | help for completion |
| `-q, --quiet` | suppresses logs     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments
* [devbox completion bash](/docs/devbox/cli-reference/devbox-completion-bash/) - Generate the
  autocompletion script for bash
* [devbox completion fish](/docs/devbox/cli-reference/devbox-completion-fish/) - Generate the
  autocompletion script for fish
* [devbox completion zsh](/docs/devbox/cli-reference/devbox-completion-zsh/) - Generate the
  autocompletion script for zsh

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-completion.md)


# devbox create
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-create/index

Initialize a directory as a devbox project using a template

## Synopsis[​](#synopsis "Direct link to Synopsis")

Initialize a directory as a devbox project. This will create an empty devbox.json in the current
directory. You can then add packages using `devbox add`

```bash  theme={null}
devbox create [dir] --template <template> [flags]
```

## List of templates[​](#list-of-templates "Direct link to List of templates")

* [**go**](https://github.com/jetify-com/devbox/tree/main/examples/development/go)
* [**node-npm**](https://github.com/jetify-com/devbox/tree/main/examples/development/nodejs/nodejs-npm/)
* [**node-typescript**](https://github.com/jetify-com/devbox/tree/main/examples/development/nodejs/nodejs-typescript/)
* [**node-yarn**](https://github.com/jetify-com/devbox/tree/main/examples/development/nodejs/nodejs-yarn/)
* [**php**](https://github.com/jetify-com/devbox/tree/main/examples/development/php/)
* [**python-pip**](https://github.com/jetify-com/devbox/tree/main/examples/development/python/pip/)
* [**python-pipenv**](https://github.com/jetify-com/devbox/tree/main/examples/development/python/pipenv/)
* [**python-poetry**](https://github.com/jetify-com/devbox/tree/main/examples/development/python/poetry/)
* [**ruby**](https://github.com/jetify-com/devbox/tree/main/examples/development/ruby/)
* [**rust**](https://github.com/jetify-com/devbox/tree/main/examples/development/rust/)

## Options[​](#options "Direct link to Options")

| Option                  | Description                      |
| ----------------------- | -------------------------------- |
| `-h, --help`            | help for init                    |
| `-t, --template string` | Template to use for the project. |
| `-q, --quiet`           | Quiet mode: Suppresses logs.     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-create.md)


# devbox generate devcontainer
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-generate-devcontainer/index

Generate Dockerfile and devcontainer.json files under .devcontainer/ directory

## Synopsis[​](#synopsis "Direct link to Synopsis")

Generate Dockerfile and devcontainer.json files necessary to run VSCode in remote container
environments.

```bash  theme={null}
devbox generate devcontainer [flags]
```

### Options[​](#options "Direct link to Options")

| Option        | Description                                                                          |
| ------------- | ------------------------------------------------------------------------------------ |
| `-f, --force` | force overwrite on existing files                                                    |
| `--root-user` | use `root` as the user for container. Installs nix as single-user mode in Dockerfile |
| `-h, --help`  | help for devcontainer                                                                |
| `-q, --quiet` | Quiet mode: Suppresses logs.                                                         |

### SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox generate](/docs/devbox/cli-reference/devbox-generate/) - Generate supporting files for
  your project

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-generate-devcontainer.md)


# devbox generate direnv
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-generate-direnv/index

Top level command for generating the .envrc file for your Devbox Project. This can be used with  to automatically start your shell when you cd into your devbox directory

```bash  theme={null}
devbox generate direnv [flags]
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `-c, --config string`      | path to directory containing a devbox.json config file                                                                                       |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])                                                                         |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment. If the file does not exist, then this parameter is ignored |
| `-h, --help`               | help for direnv                                                                                                                              |
| `-q, --quiet`              | Quiet mode: Suppresses logs.                                                                                                                 |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox generate](/docs/devbox/cli-reference/devbox-generate/) - Generate supporting files for
  your project

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-generate-direnv.md)


# devbox generate dockerfile
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-generate-dockerfile/index

Generate a Dockerfile that replicates devbox shell

## Synopsis[​](#synopsis "Direct link to Synopsis")

Generate a Dockerfile that replicates devbox shell. Can be used to run devbox shell environment in
an OCI container.

```bash  theme={null}
devbox generate dockerfile [flags]
```

## Options[​](#options "Direct link to Options")

| Option                | Description                                                                          |
| --------------------- | ------------------------------------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file                               |
| `-f, --force`         | force overwrite existing files                                                       |
| `--root-user`         | use `root` as the user for container. Installs nix as single-user mode in Dockerfile |
| `-h, --help`          | help for dockerfile                                                                  |
| `-q, --quiet`         | Quiet mode: Suppresses logs.                                                         |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox generate](/docs/devbox/cli-reference/devbox-generate/) - Generate supporting files for
  your project

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-generate-dockerfile.md)


# devbox generate readme
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-generate-readme/index

Generate a markdown readme file for this project. You must specify a name for the Readme file when running the command:

```bash  theme={null}
devbox generate readme [filename] [flags]
```

## Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for readme                                        |
| `-q, --quiet`         | Quiet mode: Suppresses logs.                           |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox generate](/docs/devbox/cli-reference/devbox-generate/) - Generate supporting files for
  your project

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-generate-readme.md)


# devbox generate
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-generate/index

Top level command for generating Devcontainers, Dockerfiles, and other useful files for your Devbox Project.

```bash  theme={null}
devbox generate <devcontainer|dockerfile|direnv> [flags]
```

## Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for generate                                      |
| `-q, --quiet`         | Quiet mode: Suppresses logs.                           |

## Subcommands[​](#subcommands "Direct link to Subcommands")

* [devbox generate devcontainer](/docs/devbox/cli-reference/devbox-generate-devcontainer/) -
  Generate Dockerfile and devcontainer.json files under .devcontainer/ directory
* [devbox generate direnv](/docs/devbox/cli-reference/devbox-generate-direnv/) - Generate a .envrc
  file to use with direnv
* [devbox generate dockerfile](/docs/devbox/cli-reference/devbox-generate-dockerfile/) - Generate a
  Dockerfile that replicates devbox shell
* [devbox generate readme](/docs/devbox/cli-reference/devbox-generate-readme/) - Generate markdown
  readme file for your project

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-generate.md)


# devbox global add
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-add/index

Add a new global package.

```bash  theme={null}
devbox global add <pkg>... [flags]
```

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Add the latest version of the `ripgrep` package
devbox global add ripgrep

# Install glibcLocales only on x86_64-linux and aarch64-linux
devbox global add glibcLocales --platform x86_64-linux,aarch64-linux

# Exclude busybox from installation on macOS
devbox global add busybox --exclude-platform aarch64-darwin,x86_64-darwin
```

## Options[​](#options "Direct link to Options")

| Option                           | Description                                                                   |
| -------------------------------- | ----------------------------------------------------------------------------- |
| `--allow-insecure`               | allows Devbox to install a package that is marked insecure by Nix             |
| `-c, --config string`            | path to directory containing a devbox.json config file                        |
| `-e, --exclude-platform strings` | exclude packages from a specific platform.                                    |
| `-h, --help`                     | help for add                                                                  |
| `-q, --quiet`                    | quiet mode: suppresses logs.                                                  |
| `-p`, `--platform strings`       | install packages only on specific platforms. Defaults to the current platform |

Valid Platforms include:

* `aarch64-darwin`
* `aarch64-linux`
* `x86_64-darwin`
* `x86_64-linux`

The platforms below are also supported, but will build packages from source

* `i686-linux`
* `armv7l-linux`

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-add.md)


# devbox global install
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-install/index

Install all packages mentioned in your global devbox.json.

```bash  theme={null}
devbox global install <pkg>... [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description             |
| ------------- | ----------------------- |
| `-h, --help`  | help for global install |
| `-q, --quiet` | suppresses logs         |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-install.md)


# devbox global list
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-list/index

Lists all the packages you have installed globally

```bash  theme={null}
devbox global list <pkg>... [flags]
```

## Aliases[​](#aliases "Direct link to Aliases")

list, ls

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for list   |
| `-q, --quiet` | suppresses logs |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-list.md)


# devbox global pull
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-pull/index

Pulls a global config from a file or URL. URLs must be prefixed with 'http://' or 'https://'.

```bash  theme={null}
devbox global pull <file> | <url> [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for pull   |
| `-q, --quiet` | suppresses logs |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-pull.md)


# devbox global push
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-push/index

Push a [global] config. Leave empty to use Jetify sync. Can be a git repo for self storage.

```bash  theme={null}
devbox global push <git-repo> [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for pull   |
| `-q, --quiet` | suppresses logs |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-push.md)


# devbox global rm
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-rm/index

Removes a package from your global config

```bash  theme={null}
devbox global rm <pkg> [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for rm     |
| `-q, --quiet` | suppresses logs |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-rm.md)


# devbox global run
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-run/index

Starts a new shell and runs your script or command in it, exiting when done.

The script must be defined in `devbox.json`, or else it will be interpreted as an arbitrary command.
You can pass arguments to your script or command. Everything after `--` will be passed verbatim into
your command (see example)

```bash  theme={null}
devbox global run <pkg>... [flags]
```

## Examples[​](#examples "Direct link to Examples")

Run a command directly:

```bash  theme={null}
devbox add cowsay
devbox global run cowsay hello
devbox global run -- cowsay -d hello
```

Run a script (defined as `"moo": "cowsay moo"`) in your devbox.json:

```bash  theme={null}
devbox global run moo
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])             |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment |
| `-h, --help`               | help for global run                                                              |
| `-q, --quiet`              | suppresses logs                                                                  |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-run.md)


# devbox global services
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-services/index

Interact with Devbox services for your global packages. This command replicates the subcommands for  but for your global packages.

```bash  theme={null}
devbox global services [command]
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])             |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment |
| `-h, --help`               | help for global services                                                         |
| `-q, --quiet`              | suppresses logs                                                                  |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-services.md)


# devbox global shellenv
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-shellenv/index

Print shell commands that add global Devbox packages to your PATH

* To add the global packages to the PATH of your current shell, run the following command:

  ```bash  theme={null}
  . <(devbox global shellenv)
  ```

* To add the global packages to the PATH of all new shells, add the following line to your shell's
  config file (e.g. `~/.bashrc` or `~/.zshrc`):

  ```bash  theme={null}
  eval "$(devbox global shellenv)"
  ```

## Options[​](#options "Direct link to Options")

| Option        | Description                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--pure`      | If this flag is specified, devbox creates an isolated environment inheriting almost no variables from the current environment. A few variables, in particular HOME, USER and DISPLAY, are retained. |
| `-h, --help`  | help for shellenv                                                                                                                                                                                   |
| `-q, --quiet` | suppresses logs                                                                                                                                                                                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-shellenv.md)


# devbox global update
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global-update/index

Updates packages in your Devbox global config to the latest available version.

## Synopsis[​](#synopsis "Direct link to Synopsis")

If you provide this command with a list of packages, it will update those packages to the latest
available version based on the version tag provided.

For example: if your global config has `[email protected]` in your package list, running
`devbox update` will update to the latest patch version of `python 3.11`.

If no packages are provided, this command will update all the versioned packages to the latest
acceptable version.

```bash  theme={null}
devbox update [pkg]... [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description     |
| ------------- | --------------- |
| `-h, --help`  | help for update |
| `-q, --quiet` | suppresses logs |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox global](/docs/devbox/devbox-global/) - Manages global Devbox packages

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global-update.md)


# devbox global
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-global/index

Top level command for managing global packages.

You can use `devbox global` to install packages that you want to use across all your local devbox
projects. For example -- if you usually use `ripgrep` for searching in all your projects, you can
use `devbox global add ripgrep` to make it available whenever you start a `devbox shell` without
adding it to each project's `devbox.json.`

You can also use Devbox as a global package manager by adding the following line to your shellrc:

`eval "$(devbox global shellenv)"`

For more details, see [Use Devbox as your Primary Package Manager](/docs/devbox/devbox-global/).

```bash  theme={null}
devbox global <subcommand> [flags]
```

## Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for generate                                      |
| `-q, --quiet`         | Quiet mode: Suppresses logs.                           |

## Subcommands[​](#subcommands "Direct link to Subcommands")

* [devbox global add](/docs/devbox/cli-reference/devbox-global-add/) - Add a global package to your
  devbox
* [devbox global list](/docs/devbox/cli-reference/devbox-global-list/) - List global packages
* [devbox global pull](/docs/devbox/cli-reference/devbox-global-pull/) - Pulls a global config from
  a file or URL.
* [devbox global rm](/docs/devbox/cli-reference/devbox-global-rm/) - Remove a global package
* [devbox global shellenv](/docs/devbox/cli-reference/devbox-global-shellenv/) - Print shell
  commands that add global Devbox packages to your PATH

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-global.md)


# devbox info
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-info/index

Display information for a package, including any installed plugins

## Synopsis[​](#synopsis "Direct link to Synopsis")

Devbox info displays all available information from a packages installed plugins, such as
environment variables, configuration files, and services provided by the plugin

```bash  theme={null}
devbox info <pkg> [flags]
```

### Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for info                                          |
| `--markdown`          | Output in markdown format                              |
| `-q, --quiet`         | Quiet mode: Suppresses logs.                           |

### SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-info.md)


# devbox init
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-init/index

Initialize a directory as a devbox project

## Synopsis[​](#synopsis "Direct link to Synopsis")

Initialize a directory as a devbox project. This will create an empty devbox.json in the current
directory. You can then add packages using `devbox add`

```bash  theme={null}
devbox init [<dir>] [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for init                |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-init.md)


# devbox install
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-install/index

Starts a new devbox shell and installs all packages mentioned in devbox.json in current directory or a directory specified via --config.

Then exits the shell when packages are done installing.

```bash  theme={null}
devbox install [flags]
```

## Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for install                                       |
| `-q, --quiet`         | suppresses logs                                        |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-install.md)


# devbox rm
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-rm/index

Remove a package from your devbox

```bash  theme={null}
devbox rm <pkg>... [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for rm                  |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-rm.md)


# devbox run
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-run/index

Starts a new interactive shell and runs your target script in it. The shell will exit once your target script is completed or when it is terminated via CTRL-C. Scripts can be defined in your .

You can also run arbitrary commands in your devbox shell by passing them as arguments to
`devbox run`. For example:

```bash  theme={null}
  devbox run echo "Hello World"
```

Will print `Hello World` to the console from within your devbox shell.

For more details, read our [scripts guide](/docs/devbox/guides/scripts/)

```bash  theme={null}
  devbox run <script | command> [flags]
```

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Run a command directly:
devbox add cowsay
devbox run cowsay hello

# Run a command that takes flags:
devbox run cowsay -d hello

# Pass flags to devbox while running a command.
# All `devbox run` flags must be passed before the command
devbox run -q cowsay -d hello

# Run a script (defined as `"moo": "cowsay moo"`) in your devbox.json:
devbox run moo
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| `-c, --config string`      | path to directory containing a devbox.json config file                           |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])             |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment |
| `-h, --help`               | help for run                                                                     |
| `-q, --quiet`              | Quiet mode: Suppresses logs.                                                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-run.md)


# devbox search
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-search/index

Search for Nix packages

## Synopsis[​](#synopsis "Direct link to Synopsis")

`devbox search` will return a list of packages and versions that match your search query.

You can add a package to your project using `devbox add <package>`.

Too add a specific version, use `devbox add <package>@<version>`.

```bash  theme={null}
devbox search <pkg> [flags]
```

## Example[​](#example "Direct link to Example")

```bash  theme={null}
$ devbox search ripgrep
Warning: Search is experimental and may not work as expected.
Found 8+ results for "ripgrep":
* ripgrep (13.0.0, 12.1.1, 12.0.1)
* ripgrep-all (0.9.6, 0.9.5)

# To add ripgrep 12.1.1 to your project:
$ devbox add [email protected]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for shell               |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-search.md)


# devbox secrets download
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets-download/index

Download environment variables into the specified file

## Synopsis[​](#synopsis "Direct link to Synopsis")

Download environment variables stored into the specified file (most commonly a .env file). The
format of the file is one NAME=VALUE per line.

```bash  theme={null}
devbox secrets download <file1> [flags]
```

## Options[​](#options "Direct link to Options")

```
--environment string   Environment name (e.g. dev, prod)
                       (default "dev")
-f, --format string    File format: env or json (default "env")
-h, --help             help for download
--org-id string        Organization id to namespace secrets by
--project-id string    Project id to namespace secrets by
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets](/docs/devbox/cli-reference/devbox-secrets/) - Manage environment variables and
  secrets

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets-download.md)


# devbox secrets init
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets-init/index

Initialize devbox secrets in the project directory. This setup step creates/connects to an existing jetify cloud project

```bash  theme={null}
devbox secrets init [flags]
```

## Options[​](#options "Direct link to Options")

```
  -h, --help   help for init
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets](/docs/devbox/cli-reference/devbox-secrets/) - Manage environment variables and
  secrets

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets-init.md)


# devbox secrets list
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets-list/index

List all stored environment variables

## Synopsis[​](#synopsis "Direct link to Synopsis")

List all stored environment variables. If no environment flag is provided, variables in all
environments will be listed.

```bash  theme={null}
devbox secrets list [flags]
```

## Options[​](#options "Direct link to Options")

```
--environment string   Environment name (e.g. dev, prod)
                       (default "dev")
-f, --format string    Display format: table or key=value
                       (default "table")
-h, --help             help for ls
--org-id string        Organization id to namespace secrets by
--project-id string    Project id to namespace secrets by
-s, --show             Display the value of each environment variable
                       (secrets included)
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets](/docs/devbox/cli-reference/devbox-secrets/) - Manage environment variables and
  secrets

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets-list.md)


# devbox secrets rm
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets-rm/index

Delete one or more environment variables

## Synopsis[​](#synopsis "Direct link to Synopsis")

Delete one or more environment variables that are stored.

```bash  theme={null}
devbox secrets rm <NAME1> [<NAME2>]... [flags]
```

## Options[​](#options "Direct link to Options")

```
--environment string   Environment name (e.g. dev, prod)
                       (default "dev")
-h, --help             help for rm
--org-id string        Organization id to namespace secrets by
--project-id string    Project id to namespace secrets by
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets](/docs/devbox/cli-reference/devbox-secrets/) - Manage environment variables and
  secrets

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets-rm.md)


# devbox secrets set
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets-set/index

Securely store one or more environment variables

## Synopsis[​](#synopsis "Direct link to Synopsis")

Securely store one or more environment variables.

```bash  theme={null}
devbox secrets set <NAME1>=<value1> [<NAME2>=<value2>]... [flags]
```

## Options[​](#options "Direct link to Options")

```
--environment string   Environment name (e.g. dev, prod)
                       (default "dev")
-h, --help             help for set
--org-id string        Organization id to namespace secrets by
--project-id string    Project id to namespace secrets by
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets](/docs/devbox/cli-reference/devbox-secrets/) - Manage environment variables and
  secrets

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets-set.md)


# devbox secrets upload
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets-upload/index

Upload variables defined in a .env file

## Synopsis[​](#synopsis "Direct link to Synopsis")

Upload variables defined in one or more .env files. The files should have one NAME=VALUE per line.

```bash  theme={null}
devbox secrets upload <file1> [<fileN>]... [flags]
```

## Options[​](#options "Direct link to Options")

```
--environment string   Environment name (e.g. dev, prod)
                       (default "dev")
-f, --format string    File format: env or json (default "env")
-h, --help             help for upload
--org-id string        Organization id to namespace secrets by
--project-id string    Project id to namespace secrets by
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets](/docs/devbox/cli-reference/devbox-secrets/) - Manage environment variables and
  secrets

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets-upload.md)


# devbox secrets
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-secrets/index

Manage environment variables and secrets

## Synopsis[​](#synopsis "Direct link to Synopsis")

Manage environment variables and secrets

Securely stores and retrieves environment variables on the cloud. Environment variables are always
encrypted, which makes it possible to store values that contain passwords and other secrets.

```bash  theme={null}
devbox secrets [flags]
```

## Options[​](#options "Direct link to Options")

```bash  theme={null}
  -h, --help   help for devbox secrets
```

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox-secrets-download](/docs/devbox/cli-reference/devbox-secrets-download/) - Download
  environment variables into the specified file
* [devbox-secrets-init](/docs/devbox/cli-reference/devbox-secrets-init/) - initialize directory and
  devbox secrets project
* [devbox-secrets-list](/docs/devbox/cli-reference/devbox-secrets-list/) - List all stored
  environment variables
* [devbox-secrets-rm](/docs/devbox/cli-reference/devbox-secrets-rm/) - Delete one or more
  environment variables
* [devbox-secrets-set](/docs/devbox/cli-reference/devbox-secrets-set/) - Securely store one or more
  environment variables
* [devbox-secrets-upload](/docs/devbox/cli-reference/devbox-secrets-upload/) - Upload variables
  defined in a .env file

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-secrets.md)


# devbox services attach
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services-attach/index

Attach to a running instance of . This command lets you launch the TUI for process-compose if you started your services in the background with .

Note that terminating the TUI will not stop your backgrounded services. To stop your services, use
`devbox services stop`.

```bash  theme={null}
devbox services attach [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for ls                  |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

### SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with devbox services

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services-attach.md)


# devbox services ls
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services-ls/index

List available services

```bash  theme={null}
devbox services ls [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for ls                  |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

### SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with devbox services

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services-ls.md)


# devbox services restart
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services-restart/index

Restarts service. If no service is specified, restarts all services and process-compose.

```bash  theme={null}
devbox services restart [service]... [flags]
```

<Info>
  Note: We recommend using `devbox services up` if you are starting all your services and
  process-compose. This command lets you specify your process-compose file and whether to run
  process-compose in the foreground or background.
</Info>

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])             |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment |
| `-h, --help`               | help for restart                                                                 |
| `-q, --quiet`              | Quiet mode: Suppresses logs.                                                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with devbox services

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services-restart.md)


# devbox services start
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services-start/index

Starts a service or list of services. If no service is specified, starts all services + process-compose.

```bash  theme={null}
devbox services start [service]... [flags]
```

<Info>
  Note: We recommend using `devbox services up` if you are starting all your services and
  process-compose. This command lets you specify your process-compose file and whether to run
  process-compose in the foreground or background.
</Info>

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])             |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment |
| `-h, --help`               | help for start                                                                   |
| `-q, --quiet`              | Quiet mode: Suppresses logs.                                                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with devbox services

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services-start.md)


# devbox services stop
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services-stop/index

Stops a service. If no service is specified, stops all your running services and shuts down process-compose.

```bash  theme={null}
devbox services stop [service]... [flags]
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                      |
| -------------------------- | -------------------------------------------------------------------------------- |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])             |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment |
| `-h, --help`               | help for stop                                                                    |
| `-q, --quiet`              | Quiet mode: Suppresses logs.                                                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with devbox services

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services-stop.md)


# devbox services up
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services-up/index

Starts process-compose and runs all the services in your project. If a list of services is specified in the arguments, only those services will be started.

```bash  theme={null}
devbox services up [services]... [flags]
```

This command will launch the process-compose TUI in the foreground. To run process-compose and your
services in the background, use the `-b` flag.

Once your services are running, you can manage them using `services start`, `services stop`, and
`services restart`.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Start all services with process compose in the foreground
devbox services up

# Start all services with process compose in the background
devbox services up -b

# Start only the web service with process compose in the foreground
devbox services up web
```

## Options[​](#options "Direct link to Options")

| Option                          | Description                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `-b, --background`              | Run service in background                                                                                                        |
| `-c, --config string`           | path to directory containing a devbox.json config file                                                                           |
| `-e, --env stringToString`      | environment variables to set in the devbox environment (default \[])                                                             |
| `--env-file string`             | path to a file containing environment variables to set in the devbox environment                                                 |
| `-h, --help`                    | help for up                                                                                                                      |
| `--pcflags stringArray`         | additional flags to pass directly to process-compose                                                                             |
| `-p, --pcport int`              | specify the port for process-compose to use. You can also set the pcport by exporting DEVBOX\_PC\_PORT\_NUM                      |
| `--process-compose-file string` | path to process compose file or directory containing process compose-file.yaml\|yml. Default is directory containing devbox.json |
| `-q, --quiet`                   | Quiet mode: Suppresses logs.                                                                                                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with devbox services

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services-up.md)


# devbox services
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-services/index

Interact with Devbox services via process-compose

```bash  theme={null}
devbox services <ls|restart|start|stop> [flags]
```

## Options[​](#options "Direct link to Options")

| Option                | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `-c, --config string` | path to directory containing a devbox.json config file |
| `-h, --help`          | help for services                                      |
| `-q, --quiet`         | Quiet mode: Suppresses logs.                           |

## Subcommands[​](#subcommands "Direct link to Subcommands")

* [devbox services ls](/docs/devbox/cli-reference/devbox-services-ls/) - List available services
* [devbox services restart](/docs/devbox/cli-reference/devbox-services-restart/) - Restarts service.
  If no service is specified, restarts all services
* [devbox services start](/docs/devbox/cli-reference/devbox-services-start/) - Starts service. If no
  service is specified, starts all services
* [devbox services stop](/docs/devbox/cli-reference/devbox-services-stop/) - Stops service. If no
  service is specified, stops all services

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-services.md)


# devbox shell
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-shell/index

Start a new shell or run a command with access to your packages

## Synopsis[​](#synopsis "Direct link to Synopsis")

Start a new shell or run a command with access to your packages. If the --config flag is set, the
shell will be started using the devbox.json found in the --config flag directory. If --config isn't
set, then devbox recursively searches the current directory and its parents.

```bash  theme={null}
devbox shell [flags]
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                                                                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-c, --config string`      | path to directory containing a devbox.json config file                                                                                                                                        |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])                                                                                                                          |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment                                                                                                              |
| `--environment string`     | environment to use, when supported (e.g.secrets support dev, prod, preview.) (default "dev")                                                                                                  |
| `--print-env`              | Print a script to setup a devbox shell environment                                                                                                                                            |
| `--pure`                   | If this flag is specified, devbox creates an isolated shell inheriting almost no variables from the current environment. A few variables, in particular HOME, USER and DISPLAY, are retained. |
| `-h, --help`               | help for shell                                                                                                                                                                                |
| `-q, --quiet`              | Quiet mode: Suppresses logs.                                                                                                                                                                  |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-shell.md)


# devbox shellenv
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-shellenv/index

Print shell commands that add Devbox packages to your PATH

```bash  theme={null}
devbox shellenv [flags]
```

## Options[​](#options "Direct link to Options")

| Option                     | Description                                                                                                                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-c, --config string`      | path to directory containing a devbox.json config file                                                                                                                                              |
| `-e, --env stringToString` | environment variables to set in the devbox environment (default \[])                                                                                                                                |
| `--env-file string`        | path to a file containing environment variables to set in the devbox environment                                                                                                                    |
| `--pure`                   | If this flag is specified, devbox creates an isolated environment inheriting almost no variables from the current environment. A few variables, in particular HOME, USER and DISPLAY, are retained. |
| `-h, --help`               | help for shellenv                                                                                                                                                                                   |
| `-q, --quiet`              | suppresses logs                                                                                                                                                                                     |

### SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable development environments

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-shellenv.md)


# devbox update
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-update/index

Updates packages within your project to the latest available version.

## Synopsis[​](#synopsis "Direct link to Synopsis")

If you provide this command with a list of packages, it will update those packages to the latest
available version based on the version tag provided.

For example: if your project has `[email protected]` in your package list, running `devbox update`
will update your project to the latest patch version of `python 3.11`.

If no packages are provided, this command will update all the versioned packages in your project to
the latest acceptable version.

```bash  theme={null}
devbox update [pkg]... [flags]
```

## Options[​](#options "Direct link to Options")

| Option         | Description                  |
| -------------- | ---------------------------- |
| `-c, --config` | Path to devbox config file.  |
| `-h, --help`   | help for shell               |
| `-q, --quiet`  | Quiet mode: Suppresses logs. |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-update.md)


# devbox version update
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-version-update/index

Check for a new version of devbox and update if available

```bash  theme={null}
devbox version update [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for update              |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-version-update.md)


# devbox version
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox-version/index

Print version information

```bash  theme={null}
devbox version [update] [flags]
```

## Subcommands[​](#subcommands "Direct link to Subcommands")

* [devbox version update](/docs/devbox/cli-reference/devbox-version-update/) - Check for a new
  version of devbox and update if available

## Options[​](#options "Direct link to Options")

| Option          | Description                                      |
| --------------- | ------------------------------------------------ |
| `-h, --help`    | help for version                                 |
| `-v, --verbose` | Verbose: displays additional version information |
| `-q, --quiet`   | Quiet mode: Suppresses logs.                     |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox](/docs/devbox/cli-reference/devbox/) - Instant, easy, predictable shells and containers

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox-version.md)


# devbox
Source: https://www.jetify.com/docs/docs/devbox/cli-reference/devbox/index

Instant, easy, predictable shells and containers

```bash  theme={null}
devbox [flags]
```

## Options[​](#options "Direct link to Options")

| Option        | Description                  |
| ------------- | ---------------------------- |
| `-h, --help`  | help for devbox              |
| `-q, --quiet` | Quiet mode: Suppresses logs. |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [devbox add](/docs/devbox/cli-reference/devbox-add/) - Add a new package to your devbox
* [devbox generate](/docs/devbox/cli-reference/devbox-generate/) - Generate supporting files for
  your project
* [devbox global](/docs/devbox/cli-reference/devbox-global/) - Manages global Devbox packages
* [devbox info](/docs/devbox/cli-reference/devbox-info/) - Display package and plugin info
* [devbox init](/docs/devbox/cli-reference/devbox-init/) - Initialize a directory as a devbox
  project
* [devbox install](/docs/devbox/cli-reference/devbox-install/) - Install your project's packages
* [devbox rm](/docs/devbox/cli-reference/devbox-rm/) - Remove a package from your devbox
* [devbox run](/docs/devbox/cli-reference/devbox-run/) - Starts a new devbox shell and runs the
  target script
* [devbox services](/docs/devbox/cli-reference/devbox-services/) - Interact with Devbox Services
* [devbox shell](/docs/devbox/cli-reference/devbox-shell/) - Start a new shell or run a command with
  access to your packages
* [devbox version](/docs/devbox/cli-reference/devbox-version/) - Print version information

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/cli-reference/devbox.md)


# devbox.json Reference
Source: https://www.jetify.com/docs/docs/devbox/configuration/index

Your devbox configuration is stored in a  file, located in your project's root directory. This file can be edited directly, or using the .

```json  theme={null}
{
  "packages": [] | {},
  "env": {},
  "shell": {
    "init_hook": "...",
    "scripts": {}
  },
  "include": []
}
```

### Packages[​](#packages "Direct link to Packages")

This is a list or map of Nix packages that should be installed in your Devbox shell and containers.
These packages will only be installed and available within your shell, and will have precedence over
any packages installed in your local machine. You can search for Nix packages using
[Nix Package Search](https://search.nixos.org/packages).

You can add packages to your devbox.json using `devbox add <package_name>`, and remove them using
`devbox rm <package_name>`.

Packages can be structured as a list of package names (`<packages>@<version>`) or
[flake references](#adding-packages-from-flakes):

```json  theme={null}
{
  "packages": ["go@latest", "golangci-lint@latest"]
}
```

If you need to provide more options to your packages (such as limiting which platforms will install
the package), you can structure packages as a map, where each package follows the schema below:

```json  theme={null}
{
  "packages": {
    // If only a version is specified, you can abbreviate as:
    // "package_name": "version"
    "package_name": string,
    "package_name": {
      // Version of the package to install. Defaults to "latest"
      "version": string,
      // Whether native library patching is enabled for this package.
      // Defaults to `auto`, can be `always` or `never`
      "patch": ["auto" | "always" | "never"],
      // List of platforms to install the package on.
      // Defaults to all platforms
      "platforms": [string],
      // List of platforms to exclude this package from.
      // Defaults to no excluded platforms
      "excluded_platforms": [string],
      // Whether to disable a built-in plugin, if one exists.
      // Defaults to false
      "disable_plugin": boolean
    }
  }
}
```

For example:

```json  theme={null}
{
  "packages": {
    "go": "latest",
    "golangci-lint": "latest",
    "glibcLocales": {
      "version": "latest",
      "platforms": ["x86_64-linux, aarch64-linux"]
    }
  }
}
```

Note that `devbox add` will automatically format `packages` based on the options and packages that
you provide.

#### Pinning a Specific Version of a Package[​](#pinning-a-specific-version-of-a-package "Direct link to Pinning a Specific Version of a Package")

You can pin a specific version of a package by adding a `@` followed by the version number to the
end of the package name. For example, to pin the `go` package to version `1.19`, you can run
`devbox add [email protected]`, or add `[email protected]` to the packages list in your
`devbox.json`:

```json  theme={null}
{ "packages": ["[email protected]"] }
```

Where possible, pinned packages follow semver. For example, if you pin `python@3`, it will install
the latest version of `python` with major version `3`.

To see a list of packages and their available versions, you can run `devbox search <pkg>`.

#### Adding Packages from Flakes[​](#adding-packages-from-flakes "Direct link to Adding Packages from Flakes")

You can add packages from flakes by adding a reference to the flake in the `packages` list in your
`devbox.json`. We currently support installing Flakes from Github and local paths.

```json  theme={null}
{
  "packages": [
    // Add the default package from a github repository
    "github:numtide/flake-utils",
    // Install a specific attribute or package from a Github flake
    "github:nix-community/fenix#stable.toolchain",
    // Install a package from a specific channel of Nixpkgs
    "github:nixos/nixpkgs/21.05#hello",
    // Install a package from a specific commit of Nixpkgs
    "github:nixos/nixpkgs/5233fd2ba76a3accb5aaa999c00509a11fd0793c#hello",
    // Install a package from a local flake.
    // This should point to a directory with a flake.nix file.
    "path:../my-flake#my-package"
  ]
}
```

To learn more about using flakes, see the [Using Flakes](/docs/devbox/guides/using-flakes/) guide.

#### Adding Platform Specific Packages[​](#adding-platform-specific-packages "Direct link to Adding Platform Specific Packages")

You can choose to include or exclude your packages on specific platforms by adding a `platforms` or
`excluded_platforms` field to your package definition. This is useful if you need to install
packages or libraries that are only available on specific platforms (such as `busybox` on Linux, or
`utm` on macOS):

```json  theme={null}
{
  "packages": {
    // Only install busybox on linux
    "busybox": {
      "version": "latest",
      "platforms": ["x86_64-linux", "aarch64-linux"]
    },
    // Exclude UTM on Linux
    "utm": {
      "version": "latest",
      "excluded_platforms": ["x86_64-linux", "aarch64-linux"]
    }
  }
}
```

Note that a package can only specify one of `platforms` or `excluded_platforms`.

Valid Platforms include:

* `aarch64-darwin`
* `aarch64-linux`
* `x86_64-darwin`
* `x86_64-linux`

The platforms below are also supported, but require you to build packages from source:

* `i686-linux`
* `armv7l-linux`

#### Disabling Built-in Plugins[​](#disabling-built-in-plugins "Direct link to Disabling Built-in Plugins")

Some packages include builtin plugins or services that are automatically started when the package is
installed. You can disable these plugins using `devbox add <package> --disable-plugin`, or by
setting the `disable_plugin` field to `true` in your package definition:

```json  theme={null}
{
  "packages": {
    "glibcLocales": {
      "version": "latest",
      "disable_plugin": true
    }
  }
}
```

### Env[​](#env "Direct link to Env")

This is a a map of key-value pairs that should be set as Environment Variables when activating
`devbox shell`, running a script with `devbox run`, or starting a service. These variables will only
be set in your Devbox shell, and will have precedence over any environment variables set in your
local machine or by [Devbox Plugins](/docs/devbox/guides/plugins/).

For example, you could set variable `$FOO` to `bar` by adding the following to your `devbox.json`:

```json  theme={null}
{ "env": { "FOO": "bar" } }
```

Currently, you can only set values using string literals, `$PWD`, and `$PATH`. Any other values with
environment variables will not be expanded when starting your shell.

### Env From[​](#env-from "Direct link to Env From")

Env from takes a string for loading environment variables into your shells and scripts. Currently it
supports loading from two sources: .env files, and Jetify Secrets.

#### .env Files[​](#env-files "Direct link to .env Files")

You can load environment variables from a `.env` file by adding the path to the file in the
`env_from` field (the file must end with `.env`). This is useful for loading secrets or other
sensitive information that you don't want to store in your `devbox.json`.

```json  theme={null}
{ "env_from": "path/to/.env" }
```

This will load the environment variables from the `.env` file into your shell when you run
`devbox shell` or `devbox run`. Note that environment variables set in the `.env` file will be
overridden if the same variable is set directly in your `devbox.json`

#### Jetify Secrets[​](#jetify-secrets "Direct link to Jetify Secrets")

You can securely load secrets from Jetify Secrets by running `devbox secrets init` and creating a
project in Jetify Cloud. This will add the `jetify-cloud` field to `env_from` in your project.

```json  theme={null}
{ "env_from": "jetify-cloud" }
```

Note that setting secrets securely with Jetify Secrets requires a Jetify Cloud account. For more
information, see the [Jetify Secrets](/docs/cloud/secrets/) guide.

### Shell[​](#shell "Direct link to Shell")

The Shell object defines init hooks and scripts that can be run with your shell. Right now two
fields are supported: `init_hook`, which run a set of commands every time you start a devbox shell,
and `scripts`, which are commands that can be run using `devbox run`

#### Init Hook[​](#init-hook "Direct link to Init Hook")

The init hook is used to run shell commands before the shell finishes setting up. This hook runs
after any other `~/.*rc` scripts, allowing you to override environment variables or further
customize the shell.

The init hook will run every time a new shell is started using `devbox shell` or `devbox run`, and
is best used for setting up environment variables, aliases, or other quick setup steps needed to
configure your environment. For longer running tasks, you should consider using a Script.

This is an example `devbox.json` that customizes the prompt and prints a welcome message:

```json  theme={null}
{
  "shell": {
    "init_hook": [
      "export PS1='📦 devbox> '",
      "echo 'Welcome! See CONTRIBUTING.md for tips on contributing to devbox.'"
    ]
  }
}
```

When run, you'll see:

```bash  theme={null}
> devbox shell
Installing nix packages. This may take a while...
Starting a devbox shell...
Welcome! See CONTRIBUTING.md for tips on contributing to devbox.
📦 devbox>
```

#### Scripts[​](#scripts "Direct link to Scripts")

Scripts are commands that are executed in your Devbox shell using `devbox run <script_name>`. They
can be used to start up background process (like databases or servers), or to run one off commands
(like setting up a dev DB, or running your tests).

Scripts can be defined by giving a name, and one or more commands. Single command scripts can be
added by providing a name, and a string:

```json  theme={null}
{
  "shell": {
    "scripts": {
      "print_once": "echo \"Hello Once!\""
    }
  }
}
```

To run multiple commands in a single script, you can pass them as an array:

```json  theme={null}
{
  "shell": {
    "scripts": {
      "print_twice": ["echo \"Hello Once!\"", "echo \"Hello Twice!\""]
    }
  }
}
```

### Include[​](#include "Direct link to Include")

Includes can be used to explicitly add extra configuration from
[plugins](/docs/devbox/guides/plugins/) to your Devbox project. Plugins are parsed and merged in the
order they are listed.

Note that in the event of a conflict, plugins near the end of the list will override plugins at the
beginning of the list. Likewise, if a setting in your project config conflicts with a plugin (e.g.,
your `devbox.json` has a script with the same name as a plugin script), your project config will
take precedence.

```json  theme={null}
{
    "include": [
        // Include a plugin from a Github Repo. The repo must have a plugin.json in it's root,
        // or in the directory specified by ?dir
        "github:org/repo/ref?dir=<path-to-plugin>"
        // Include a local plugin. The path must point to a plugin.json
        "path:path/to/plugin.json"
        // Force activate a builtin plugin
        "plugin:php-config"
    ]
}
```

### Example: A Rust Devbox[​](#example-a-rust-devbox "Direct link to Example: A Rust Devbox")

An example of a devbox configuration for a Rust project called `hello_world` might look like the
following:

```json  theme={null}
{
  "packages": ["rustup@latest", "libiconv@latest"],
  "env": { "PROJECT_DIR": "$PWD" },
  "shell": {
    "init_hook": [". conf/set-env.sh", "rustup default stable", "cargo fetch"],
    "scripts": {
      "build-docs": "cargo doc",
      "start": "cargo run",
      "run_test": ["cargo test -- --show-output"]
    }
  }
}
```

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/configuration.md)


# Using Devbox in CI/CD with GitHub Actions
Source: https://www.jetify.com/docs/docs/devbox/continuous-integration/github-action/index

This guide explains how to use Devbox in CI/CD using GitHub Actions. The  will install Devbox CLI and any packages + configuration defined in your  file. You can then run tasks or scripts within  to reproduce your environment.

This GitHub Action also supports caching the packages and dependencies installed in your
`devbox.json`, which can significantly improve CI build times.

## Usage[​](#usage "Direct link to Usage")

`devbox-install-action` is available on the
[GitHub Marketplace](https://github.com/marketplace/actions/devbox-installer)

In your project's workflow YAML, add the following step:

```bash  theme={null}
- name: Install devbox  uses: jetify-com/devbox-install-[email protected]
```

## Example Workflow[​](#example-workflow "Direct link to Example Workflow")

The workflow below shows how to use the action to install Devbox, and then run arbitrary commands or
[Devbox Scripts](/docs/devbox/guides/scripts/) in your shell.

```bash  theme={null}
name: Testing with devboxon: pushjobs:  test:    runs-on: ubuntu-latest    steps:      - uses: actions/checkout@v4      - name: Install devbox        uses: jetify-com/devbox-install-[email protected]      - name: Run arbitrary commands        run: devbox run -- echo "done!"      - name: Run a script called test        run: devbox run test
```

## Configuring the Action[​](#configuring-the-action "Direct link to Configuring the Action")

See the [GitHub Marketplace page](https://github.com/marketplace/actions/devbox-installer) for the
latest configuration settings and an example.

For stability over new features and bug fixes, consider pinning `devbox-version`. Remember to update
this pinned version when you update your local Devbox via `devbox version update`.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/continuous-integration/github-action.md)


# Devbox Examples
Source: https://www.jetify.com/docs/docs/devbox/devbox-examples/index

Devbox strives to provide a balance between the immutability of Nix's global store, and the mutability of local project configuration. The examples below show how to configure Devbox for a wide range of development environments and project types.

You can view the full list of examples in our [Example Repo](https://github.com/jetify-com/devbox/)

## Languages[​](#languages "Direct link to Languages")

* [C#/.NET](/docs/devbox/devbox-examples/languages/csharp/)
* [Elixir](/docs/devbox/devbox-examples/languages/elixir/)
* [F#/.NET](/docs/devbox/devbox-examples/languages/fsharp/)
* [Go](/docs/devbox/devbox-examples/languages/go/)
* [Haskell](/docs/devbox/devbox-examples/languages/haskell/)
* [Java](/docs/devbox/devbox-examples/languages/java/)
* [NodeJS](/docs/devbox/devbox-examples/languages/nodejs/)
* [Nim](/docs/devbox/devbox-examples/languages/nim/)
* [PHP](/docs/devbox/devbox-examples/languages/php/)
* [Python](/docs/devbox/devbox-examples/languages/python/)
* [Rust](/docs/devbox/devbox-examples/languages/rust/)
* [Ruby](/docs/devbox/devbox-examples/languages/ruby/)
* [Zig](/docs/devbox/devbox-examples/languages/zig/)

## Databases[​](#databases "Direct link to Databases")

* [MariaDB](/docs/devbox/devbox-examples/databases/mariadb/)
* [MongoDB](/docs/devbox/devbox-examples/databases/mongodb/)
* [MySQL](/docs/devbox/devbox-examples/databases/mysql/)
* [PostgreSQL](/docs/devbox/devbox-examples/databases/postgres/)
* [RabbitMQ](/docs/devbox/devbox-examples/databases/rabbitmq/)
* [Redis](/docs/devbox/devbox-examples/databases/redis/)

## Servers[​](#servers "Direct link to Servers")

* [Apache](/docs/devbox/devbox-examples/servers/apache/)
* [Caddy](/docs/devbox/devbox-examples/servers/caddy/)
* [NGINX](/docs/devbox/devbox-examples/servers/nginx/)

## Full Stack Examples[​](#full-stack-examples "Direct link to Full Stack Examples")

These examples combine configuration from multiple examples to create a full stack for development
and deployment.

* [Django](/docs/devbox/devbox-examples/stacks/django/)
* [Drupal](/docs/devbox/devbox-examples/stacks/drupal/)
* [Jekyll](/docs/devbox/devbox-examples/stacks/jekyll/)
* [Laravel](/docs/devbox/devbox-examples/stacks/laravel/)
* [LAPP (Linux, Apache, PostgreSQL, PHP)](/docs/devbox/devbox-examples/stacks/lapp/)
* [LEPP (Linux, NGINX, PostgreSQL, PHP)](/docs/devbox/devbox-examples/stacks/lepp/)
* [Ruby on Rails](/docs/devbox/devbox-examples/stacks/rails/)
* [Spring Boot](/docs/devbox/devbox-examples/stacks/spring/)

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/devbox-examples/index.md)


# Use Devbox as your Primary Package Manager
Source: https://www.jetify.com/docs/docs/devbox/devbox-global/index

In addition to managing isolated development environments, you can use Devbox as a general package manager. Devbox Global allows you to add packages to a global  This is useful for installing a standard set of tools you want to use across multiple Devbox Projects.

For example — if you use ripgrep as your preferred search tool, you can add it to your global Devbox
profile with `devbox global add ripgrep`. Now whenever you start a Devbox shell, you will have
ripgrep available, even if it's not in the project's devbox.json.

<Frame caption="Installing Packages with Devbox Global">
    <img src="https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=31aa2848da4173b1d80a4c8322f3f058" alt="Devbox global package manager" data-og-width="700" width="700" data-og-height="538" height="538" data-path="docs/devbox/devbox-global/devbox-global-package-manager.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?w=280&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=2384e55a18d976e593cc10d837e074d8 280w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?w=560&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=4cd32632f537c882fc8deea34073edc0 560w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?w=840&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=42c91febec655d81dfde6de1f51906cc 840w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?w=1100&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=b9da0c13bc7292ff941cee470a25dd00 1100w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?w=1650&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=2bf184ea87d0b74d00c41eda3ff5e88d 1650w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-global/devbox-global-package-manager.svg?w=2500&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=e3131de6cdcb51c7998129cc9098941c 2500w" />
</Frame>

You can also use `devbox global` to replace package managers like `brew` and `apt` by adding the
global profile to your path. Because Devbox uses Nix to install packages, you can sync your global
config to install the same packages on any machine.

Devbox saves your global config in a `devbox.json` file in your home directory. This file can be
shared with other users or checked into source control to synchronize it across machines.

## Adding and Managing Global Packages[​](#adding-and-managing-global-packages "Direct link to Adding and Managing Global Packages")

You can install a package using `devbox global add [<package>]`, where the package names should be a
list of [Nix Packages](https://search.nixos.org/packages) you want to install.

For example, if we wanted to install ripgrep, vim, and git to our global profile, we could run:

```bash  theme={null}
devbox global add ripgrep vim git
# Output:
ripgrep is now installed
vim is now installed
git is now installed
```

Once installed, the packages will be available whenever you start a Devbox Shell, even if it's not
included in the project's `devbox.json`.

To view a full list of global packages, you can run `devbox global list`:

```bash  theme={null}
devbox global list
# Output:
* ripgrep
* vim
* git
```

To remove a global package, use:

```bash  theme={null}
devbox global rm ripgrep
# Output:
removing 'github:NixOS/nixpkgs/ripgrep'
```

## Using Global Packages in your Host Shell[​](#using-global-packages-in-your-host-shell "Direct link to Using Global Packages in your Host Shell")

If you want to make your global packages available in your host shell, you can add them to your
shell PATH. Running `devbox global shellenv` will print the command necessary to source the
packages.

### Add Global Packages to your Current Host Shell[​](#add-global-packages-to-your-current-host-shell "Direct link to Add Global Packages to your Current Host Shell")

To temporarily add the global packages to your current shell, run:

```bash  theme={null}
. <(devbox global shellenv --init-hook)
```

You can also add a hook to your shell's config to make them available whenever you launch your
shell:

### Bash[​](#bash "Direct link to Bash")

Add the following command to your `~/.bashrc` file:

```bash  theme={null}
eval "$(devbox global shellenv --init-hook)"
```

Make sure to add this hook before any other hooks that use your global packages.

### Zsh[​](#zsh "Direct link to Zsh")

Add the following command to your `~/.zshrc` file:

```bash  theme={null}
eval "$(devbox global shellenv --init-hook)"
```

### Fish[​](#fish "Direct link to Fish")

Add the following command to your `~/.config/fish/config.fish` file:

```bash  theme={null}
devbox global shellenv --init-hook | source
```

## Sharing Your Global Config with Git[​](#sharing-your-global-config-with-git "Direct link to Sharing Your Global Config with Git")

You can use Git to synchronize your `devbox global` config across multiple machines using
`devbox global push <remote>` and `devbox global pull <remote>`.

Your global `devbox.json` and any other files in the Git remote will be stored in
`$XDG_DATA_HOME/devbox/global/default`. If `$XDG_DATA_HOME` is not set, it will default to
`~/.local/share/devbox/global/default`. You can view the current global directory by running
`devbox global path`.

## Next Steps[​](#next-steps "Direct link to Next Steps")

### Learn more about Devbox[​](#learn-more-about-devbox "Direct link to Learn more about Devbox")

* **[Getting Started](/docs/devbox/quickstart/):** Learn how to install Devbox and create your first
  Devbox Shell.
* **[Devbox Scripts](/docs/devbox/guides/scripts/):** Automate setup steps and configuration for
  your shell using Devbox Scripts.
* **[Configuration Guide](/docs/devbox/configuration/):** Learn how to configure your shell and dev
  environment with `devbox.json`.
* **[Browse Examples](https://github.com/jetify-com/devbox-examples):** You can see how to create a
  development environment for your favorite tools or languages by browsing the Devbox Examples repo.
* **[Using Flakes with Devbox](/docs/devbox/guides/using-flakes/):** Learn how to install packages
  from Nix Flakes.

### Use Devbox with your IDE[​](#use-devbox-with-your-ide "Direct link to Use Devbox with your IDE")

* **[Direnv Integration](/docs/devbox/ide-configuration/direnv/):** Devbox can integrate with
  [direnv](https://direnv.net/) to automatically activate your shell and packages when you navigate
  to your project.
* **[Devbox for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=jetpack-io.devbox):**
  Install our VS Code extension to speed up common Devbox workflows or to use Devbox in a
  devcontainer.

### Get Involved[​](#get-involved "Direct link to Get Involved")

* **[Join our Discord Community](https://discord.gg/jetify):** Chat with the development team and
  our growing community of Devbox users.
* **[Visit us on Github](https://github.com/jetify-com/devbox):** File issues and provide feedback,
  or even open a PR to contribute to Devbox or our Docs.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/devbox-global.md)


# Devbox Env Variables
Source: https://www.jetify.com/docs/docs/devbox/env-variables/index

The following is a list of Environment variables used by Devbox to manage your environment. Some of these variables are set by Devbox, while others can be used to manage how Devbox sets up your shell.

Note that this list only describes variables that are set by Devbox itself.
[Devbox plugins](/docs/devbox/guides/plugins/) may set their own environment variables, which are
documented in their respective pages and via `devbox info <package>`.

## Environment Variables Set by Devbox Shell[​](#environment-variables-set-by-devbox-shell "Direct link to Environment Variables Set by Devbox Shell")

Below are some useful environment variables that Devbox sets up for you. These variables can be used
in your scripts to access information or write scripts for your current project environment.

| Variable               | Description                                                                                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DEVBOX_CONFIG_DIR`    | The directory where Devbox stores user-editable config files for your project's packages. These files can be checked into source control               |
| `DEVBOX_PACKAGES_DIR`  | The directory containing the binaries and files for the packages in your current project                                                               |
| `DEVBOX_PROJECT_ROOT`  | The root directory of your current project. This will match the directory location of the `devbox.json` file for your currently running shell          |
| `DEVBOX_PURE_SHELL`    | Indicates whether you are running your current shell in pure mode. Pure mode clears your current environment variables before starting a devbox shell  |
| `DEVBOX_SHELL_ENABLED` | Whether or not Devbox is enabled in the current shell. This is automatically set to `1` when you start a shell, run a script, or start services        |
| `DEVBOX_WD`            | Your current working directory. This can be used when writing scripts that you want to run in your current directory, instead of DEVBOX\_PROJECT\_ROOT |

## Environment Variables for Managing Devbox[​](#environment-variables-for-managing-devbox "Direct link to Environment Variables for Managing Devbox")

Below are some environment variables that can be used to manage how Devbox sets up your shell. These
variables can be set in your shell or in your `devbox.json` file.

| Variable                          | Description                                                                                                                                                                                                                              | Value   |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `DEVBOX_DEBUG`                    | Enable debug output for Devbox. If set to 1, this will print out additional information about what Devbox is doing.                                                                                                                      | 0       |
| `DEVBOX_FEATURE_DETSYS_INSTALLER` | If enabled, Devbox will use the Determinate Systems installer to setup Nix on your system. *This variable must be set on your host*                                                                                                      | 0       |
| `DEVBOX_NO_PROMPT`                | Disables the default shell prompt modification for Devbox. Usually used if you want to configure your own prompt for indicating that you are in a devbox sell                                                                            | 0       |
| `DEVBOX_PC_PORT_NUM`              | Sets the port number for process-compose when running Devbox services. If this variable is unset and a port is not provided via the CLI, Devbox will choose a random available port                                                      | `unset` |
| `DEVBOX_USE_VERSION`              | Setting this variable will force Devbox to use a different version than the current latest. For example: `DEVBOX_USE_VERSION=0.13.0` will install and use Devbox v0.13 for all Devbox commands. *This variable must be set on your host* | `unset` |

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/env-variables.md)


# Frequently Asked Questions
Source: https://www.jetify.com/docs/docs/devbox/faq/index

This doc contains answers to frequently asked questions about Devbox that are not covered elsewhere in our documentation. If you have a question that isn't covered here, feel free to ask us on our , or  on our GitHub repository.

## How does Devbox work?[​](#how-does-devbox-work "Direct link to How does Devbox work?")

Devbox generates isolated, reproducible development environments using the
[Nix package manager](https://nixos.org/). Devbox uses Nix to install packages, and then creates an
isolated shell environment for your project by symlinking the packages you need into your project
directory.

## Where does Devbox install my packages?[​](#where-does-devbox-install-my-packages "Direct link to Where does Devbox install my packages?")

Devbox and Nix install your packages in the read-only Nix store, usually located at `/nix/store`.
Devbox then creates your environment by symlinking the packages you need into the `.devbox`
directory in your project.

## How do I clean up unused packages from the Nix Store?[​](#how-do-i-clean-up-unused-packages-from-the-nix-store "Direct link to How do I clean up unused packages from the Nix Store?")

You can use `devbox run -- nix store gc --extra-experimental-features nix-command` to automatically
clean up packages that are no longer needed for your projects.

## Does Devbox require Docker or Containers to work?[​](#does-devbox-require-docker-or-containers-to-work "Direct link to Does Devbox require Docker or Containers to work?")

No. Since Devbox uses Nix to install packages and create isolated environments, Docker is not
required. If you want to run your Devbox project inside a container, you can generate a Dockerfile
or devcontainer.json using the `devbox generate` command.

## What versions of Nix are supported by Devbox?[​](#what-versions-of-nix-are-supported-by-devbox "Direct link to What versions of Nix are supported by Devbox?")

Devbox requires Nix >= 2.12. If Nix is not present on your machine when you first run Devbox, it
will automatically try to install the latest supported version for you.

## Can I use Devbox with NixOS?[​](#can-i-use-devbox-with-nixos "Direct link to Can I use Devbox with NixOS?")

Yes! Devbox can be installed on any Linux distribution, including NixOS. You can even install Devbox
via Nixpkgs. See the [installation guide](/docs/devbox/installing-devbox/) for more details.

## A package I installed is missing header files or libraries I need for development. Where do I find them?[​](#a-package-i-installed-is-missing-header-files-or-libraries-i-need-for-development-where-do-i-find-them "Direct link to A package I installed is missing header files or libraries I need for development. Where do I find them?")

In order to save space, Devbox and Nix only install the required components of packages by default.
Development header files and libraries are often installed in a separate output of the package
(usually `dev`), which can be installed using the `--output` flag on the `devbox add` command.

For example, the command below will install both the default output `out`, and the `cli` output for
the prometheus package:

````bash  theme={null}
devbox add prometheus --outputs=out,cli
```bash

You can also specify non-default outputs in [flake references](/docs/devbox/guides/using-flakes/):

```bash
devbox add github:NixOS/nixpkgs#prometheus^out,cli
````

## One of my project's packages is taking a long time to install. How can I speed up the installation process?[​](#one-of-my-projects-packages-is-taking-a-long-time-to-install-how-can-i-speed-up-the-installation-process "Direct link to One of my project's packages is taking a long time to install. How can I speed up the installation process?")

Packages may take a long time to install if they do not have a binary available in the public Nix
Cache. If a prebuilt binary is not available, Nix will built the package from source.

If prebuilt binaries are not available in the public cache, you may want to use the
[Jetify Cache](/docs/cloud/cache/) or the [Jetify Prebuilt Cache](/docs/cloud/cache/prebuilt-cache/)
to cache the binaries you build for future use. Using a package cache can reduce package install by
up to 90% compared to building from source.

## I'm trying to build a project, but it says that I'm missing `libstdc++`. How do I install this library in my project?[​](#im-trying-to-build-a-project-but-it-says-that-im-missing-libstdc-how-do-i-install-this-library-in-my-project "Direct link to im-trying-to-build-a-project-but-it-says-that-im-missing-libstdc-how-do-i-install-this-library-in-my-project")

This message means that your project requires an implementation of the C++ Standard Library
installed and linked within your shell. You can add the libstdc++ libraries and object files using
`devbox add stdenv.cc.cc.lib`.

## I'm seeing errors like \`\`GLIBC\_X.XX' not found\` when I try to install my packages, or when I install packages from PyPi/RubyGems/NPM/Cargo/other package manager in my shell[​](#im-seeing-errors-like-glibc_xxx-not-found-when-i-try-to-install-my-packages-or-when-i-install-packages-from-pypirubygemsnpmcargoother-package-manager-in-my-shell "Direct link to I'm seeing errors like ``GLIBC_X.XX' not found` when I try to install my packages, or when I install packages from PyPi/RubyGems/NPM/Cargo/other package manager in my shell")

This message usually occurs when using older packages, or when mixing different versions of packages
within a single shell. The error tends to occur because each Nix package comes bundled with all of
it's dependencies, including a version of the C Standard Library, to ensure reproducibility. If your
interpreter (Python/Ruby/Node) or runtime is using an older version of `glibc` than what your other
packages expect, they will throw this error.

There are three ways to work around this issue:

1. You can update your packages to use a newer version (using `devbox add`). This newer version will
   likely come bundled with a newer version of `glibc`.
2. You can use `devbox update` to get the latest Nix derivation for your package. Newer derivations
   may come bundled with newer dependencies, including `glibc`
3. If you need to use an exact package version, but you still see this error, you can patch it to
   use a newer version of glibc using `devbox add <package>@<version> --patch always`. This will
   patch your package to use the latest version of glibc available in the Nix store, as well as
   patching it to use any native libraries you have installed with Devbox.

## How can I use custom Nix packages or overrides with Devbox?[​](#how-can-i-use-custom-nix-packages-or-overrides-with-devbox "Direct link to How can I use custom Nix packages or overrides with Devbox?")

You can add customized packages to your Devbox environment using our
[Flake support](/docs/devbox/guides/using-flakes/). You can use these flakes to modify or override
packages from nixpkgs, or to create your own custom packages.

## Can I use Devbox if I use [Fish](https://fishshell.com/)?[​](#can-i-use-devbox-if-i-use-fish "Direct link to can-i-use-devbox-if-i-use-fish")

Yes. In addition to supporting POSIX compliant shells like Zsh and Bash, Devbox also works with
Fish.

Note that `init_hooks` in Devbox will be run directly in your host shell, so you may have encounter
some compatibility issues if you try to start a shell that uses a POSIX-compatible script in the
init\_hook.

## How can I rollback to a previous version of Devbox?[​](#how-can-i-rollback-to-a-previous-version-of-devbox "Direct link to How can I rollback to a previous version of Devbox?")

You can use any previous version of Devbox by setting the `DEVBOX_USE_VERSION` environment variable.
For example, to use version 0.8.0, you can run the following or add it to your shell's rcfile:

```bash  theme={null}
export DEVBOX_USE_VERSION=0.8.0
```

You can upgrade to the latest version of Devbox by unsetting the variable, and running
`devbox version update`

## How can I prevent Devbox from modifying my prompt while inside a shell?[​](#how-can-i-prevent-devbox-from-modifying-my-prompt-while-inside-a-shell "Direct link to How can I prevent Devbox from modifying my prompt while inside a shell?")

By default, Devbox will prefix your prompt with `(devbox)` when inside a `devbox shell`. You can
disable this behavior by setting this environment variable in your shell's rcfile:

````bash  theme={null}
DEVBOX_NO_PROMPT=true
```json

If you are using Fish:

````

set -U devbox\_no\_prompt true

```bash  theme={null}

## How can I uninstall Devbox?[​](#how-can-i-uninstall-devbox "Direct link to How can I uninstall Devbox?")

To uninstall Devbox:

1. Remove the Devbox launcher using `rm /usr/local/bin/devbox`
2. Remove the Devbox binaries using `rm -rf ~/.cache/devbox`
3. Remove your Devbox global config using `rm -rf ~/.local/share/devbox`

If you want to uninstall Nix, you will need to follow the instructions in the Nix Documentation:
[https://nixos.org/manual/nix/stable/installation/uninstall](https://nixos.org/manual/nix/stable/installation/uninstall).

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/faq.md)
```


# Creating a Devbox Plugin
Source: https://www.jetify.com/docs/docs/devbox/guides/creating-plugins/index

Plugins make it easier to get started with packages that require additional setup when installed with Nix, and they offer a familiar interface for configuring packages. They also help keep all of your project's configuration within your project directory, which helps maintain portability and isolation.

## Getting Started[​](#getting-started "Direct link to Getting Started")

Before writing a plugin, we recommend reading the
[User Documentation](https://www.jetify.com/docs/devbox/guides/plugins/) on plugins, as well as
inspecting and testing a few of the plugins in the
[plugin directory](https://github.com/jetify-com/devbox/tree/main/plugins) of our repo. Note that
the plugins in this directory are compiled into the Devbox binary, but your plugin can be sourced
from a local directory or from within your project.

If you're looking for plugin ideas, check out our
[Issues page](https://github.com/jetify-com/devbox/issues?q=is%3Aissue+is%3Aopen+label%3A%22plugin+request%22)
for any user requests.

Before contributing, please consult our
[Contributing Guide](https://github.com/jetify-com/devbox/blob/main/CONTRIBUTING.md) and
[Code of Conduct](https://github.com/jetify-com/devbox/blob/main/CODE_OF_CONDUCT.md) for details on
how to contribute to Devbox.

## Creating a Plugin[​](#creating-a-plugin "Direct link to Creating a Plugin")

We recommend organizing your plugin with the following directory structure, where the top-level
folder matches the name of your plugin:

```
my-plugin/├── README.md├── plugin.json├── config/│   ├── my-plugin.conf│   └── process-compose.yaml└── test/    ├── devbox.json    └── devbox.lock
```

* **README.md** -- Should contain a description of how your plugin works, and what files, variables,
  and services it adds to Devbox Projects
* **plugin.json** -- This file is a Go JSON Template that defines your plugin. See the sections
  below for more detail
* **config/** -- This folder contains any support or configuration files required by your plugin, as
  well as the process-compose.yaml for defining services
* **test/** -- This directory contains an example project for testing your plugin

## Plugin Design[​](#plugin-design "Direct link to Plugin Design")

### Plugin Lifecycle[​](#plugin-lifecycle "Direct link to Plugin Lifecycle")

Plugins are activated whenever a developer runs `devbox shell`, runs a script with `devbox run`, or
starts a service using `devbox services start|restart`. The lifecycle of a devbox shell with plugins
works as follows:

### Plugin.json Schema[​](#pluginjson-schema "Direct link to Plugin.json Schema")

Plugins are defined as Go JSON Template files, using the following schema:

```json  theme={null}
{  "name": "",  "version": "",  "description": "",  "packages":[] | {},  "env": {    "<key>": "<value>"  },  "create_files": {    "<destination>": "<source>"  },  "shell": {    "init_hook": [      "<bash commands>"    ],     "scripts": {      "<key>": "<value>"    }  },  "include": [   "<path_to_plugin>"  ]}
```

A plugin can define services by adding a `process-compose.yaml` file in its `create_files` stanza.

### Template Placeholders[​](#template-placeholders "Direct link to Template Placeholders")

Devbox's Plugin System provides a few special placeholders that should be used when specifying paths
for env variables and helper files:

* `{{ .DevboxProjectDir }}` – points to the root folder of their project, where the user's
  `devbox.json` is stored.
* `{{ .DevboxDirRoot }}` - points to `<projectDir>/devbox.d`. This directory is public and added to
  source control by default.
* `{{ .DevboxDir }}` – points to `<projectDir>/devbox.d/<plugin.name>`. This directory is public and
  added to source control by default. This directory is not modified or recreated by Devbox after
  the initial package installation. You should use this location for files that a user will want to
  modify and check-in to source control alongside their project (e.g., `.conf` files or other
  configs).
* `{{ .Virtenv }}` – points to `<projectDir>/.devbox/virtenv/<plugin_name>` whenever the plugin
  activates. This directory is hidden and added to `.gitignore` by default You should use this
  location for files or variables that a user should not check-in or edit directly. Files in this
  directory should be considered managed by Devbox, and may be recreated or modified after the
  initial installation.

### Fields[​](#fields "Direct link to Fields")

#### `name` *string*[​](#name-string "Direct link to name-string")

The name of your plugin. This is used to identify your plugin when a user runs `devbox info`. If
`match` is not set, the plugin will automatically activate when a package is added to a devbox.json
project that matches `name`.

#### `version` *string*[​](#version-string "Direct link to version-string")

The version of your plugin. You should start your version at 0.0.1 and bump it whenever you merge an
update to the plugin.

#### `description` *string*[​](#description-string "Direct link to description-string")

Special usage instructions or notes to display when your plugin activates or when a user runs
`devbox info`. You do not need to document variables, helper files, or services, since these are
automatically printed when a user runs `devbox info`.

#### `packages` *string\[] | object*[​](#packages-string--object "Direct link to packages-string--object")

A list of packages that the plugin will install when activated or included in a package. This
section follows the same format as [`packages`](/docs/devbox/configuration/#packages) section in a
project's `devbox.json`.

Packages installed by a plugin can be overridden if a user installs a different version of the same
package in their `devbox.json` config. For example, if a plugin installs `[email protected]`, and a
user's devbox.json installs `[email protected]`, the project will use `[email protected]`.

#### `env` *object*[​](#env-object "Direct link to env-object")

A map of `"key" : "value"` pairs used to set environment variables in `devbox shell` when the plugin
is activated. These variables will be printed when a user runs `devbox info`, and can be overridden
by a user's `devbox.json`.

#### `create_files` *object*[​](#create_files-object "Direct link to create_files-object")

A map of `"destination":"source"` pairs that can be used to create or copy files into the user's
devbox directory when the plugin is activated. For example:

```
"create_files": {    "{{ .DevboxDir }}/Caddyfile": "caddy/Caddyfile"}
```

Will copy the Caddyfile in the `plugins/caddy` folder to `devbox.d/caddy/Caddyfile` in the user's
project directory.

You should use this to copy starter config files or templates needed to run the plugin's package.

#### `shell.init_hook` *string | string\[]*[​](#shellinit_hook-string--string "Direct link to shellinit_hook-string--string")

A single `bash` command or list of `bash` commands that should run before the user's shell is
initialized.

This will run every time a shell is started, so you should avoid any resource heavy or long running
processes in this step.

#### `shell.scripts` *object*[​](#shellscripts-object "Direct link to shellscripts-object")

[Scripts](/docs/devbox/guides/scripts/) are commands that are executed in your Devbox shell using
`devbox run <script_name>`. They can be used to start up background process (like databases or
servers), or to run one off commands (like setting up a dev DB, or running your tests).

Scripts can be defined by giving a name, and one or more commands. Single command scripts can be
added by providing a name, and a string:

```json  theme={null}
{
  "shell": {
    "scripts": {
      "print_once": "echo \"Hello Once!\""
    }
  }
}
```

To run multiple commands in a single script, you can pass them as an array:

```json  theme={null}
{
  "shell": {
    "scripts": {
      "print_twice": ["echo \"Hello Once!\"", "echo \"Hello Twice!\""]
    }
  }
}
```

Scripts defined in a plugin will be overridden if a user's `devbox.json` defines a script with the
same name. For example, if both the plugin and the devbox.json that includes it defined a
`print_once` script, the version in the user's `devbox.json` will take precedence in the shell.

#### `include` *string\[]*[​](#include-string "Direct link to include-string")

Include can be used to explicitly add extra configuration from
[plugins](/docs/devbox/guides/plugins/) to your Devbox project. Plugins are parsed and merged in the
order they are listed.

Note that in the event of a conflict, plugins near the end of the list will override plugins at the
beginning of the list. Likewise, if a setting in your plugin.json conflicts with an included plugin,
your setting will take precedence.

```
{    "include": [        // Include a plugin from a Github Repo. The repo must have a plugin.json in it's root,        // or in the directory specified by ?dir        "github:org/repo/ref?dir=<path-to-plugin>"        // Include a local plugin. The path must point to a plugin.json        "path:path/to/plugin.json"    ]}
```

### Adding Services[​](#adding-services "Direct link to Adding Services")

Devbox uses [Process Compose](https://github.com/F1bonacc1/process-compose) to run services and
background processes.

Plugins can add services to a user's project by adding a `process-compose.yaml` file to the
`create_files` stanza. This file will be automatically detected by Devbox, and started when a user
runs `devbox services up` or `devbox services start`.

See the process compose [docs](https://github.com/F1bonacc1/process-compose) for details on how to
write define services in `process-compose.yaml`. You can also check the plugins in this directory
for examples on how to write services.

## Testing your Plugin[​](#testing-your-plugin "Direct link to Testing your Plugin")

Testing plugins can be done using an example Devbox project. Follow the steps below to create a new
test project

1. Create a new `devbox.json` in an empty directory using `devbox init`.
2. Add your plugin to the `include` section of the `devbox.json` file.
3. Add any expected packages using `devbox add <pkg>`.
4. Check that your plugin creates the correct files and environment variables when running
   `devbox shell`
5. If you are looking for sample projects to test your plugin with, check out our
   [examples](https://github.com/jetify-com/devbox/tree/main/examples).

## Example: MongoDB[​](#example-mongodb "Direct link to Example: MongoDB")

The plugin.json below installs MongoDB + the Mongo shell, and sets the environment variables and
config needed to run MongoDB in Devbox.

```json  theme={null}
{
  "name": "mongodb",
  "version": "0.0.1",
  "description": "Plugin for the [`mongodb`](https://www.nixhub.io/packages/mongodb) package. This plugin configures MonogoDB to use a local config file and data directory for this project, and configures a mongodb service.",
  "packages": ["mongodb@latest", "mongosh@latest"],
  "env": {
    "MONGODB_DATA": "{{.Virtenv}}/data",
    "MONGODB_CONFIG": "{{.DevboxDir}}/mongod.conf"
  },
  "create_files": {
    "{{.Virtenv}}/data": "",
    "{{.Virtenv}}/process-compose.yaml": "config/process-compose.yaml",
    "{{.DevboxDir}}/mongod.conf": "config/mongod.conf"
  }
}
```

## Tips for Writing Plugins[​](#tips-for-writing-plugins "Direct link to Tips for Writing Plugins")

* Only add plugins for packages that require configuration to work with Devbox.
* Plugins should try to use the same configuration conventions (environment variables, configuration
  files) as their packages. This lets developers configure their packages in a way that they are
  familiar with, using existing documentation.
* If you think a user may want to override or change a parameter, define it as an environment
  variable in `env`. This makes it possible for a developer to override the parameter in their
  `devbox.json` file
* If you're adding a helper file that you think a developer would want check into source control,
  create it in `{{ .DevboxDir }}`. If you're creating a file that would not be checked into source
  control, create it in `{{ .Virtenv }}`.
* Unless there is a very good reason, we do not recommend creating files outside of
  `{{ .DevboxDir }}` or `{{ .Virtenv }}`. This helps keep user projects clean and well organized.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/creating-plugins.md)


# Installing a Specific Package Version
Source: https://www.jetify.com/docs/docs/devbox/guides/pinning-packages/index

This document explains how to use  and  to install a specific package version in your Devbox project. It also explains how to pin a particular major or minor version for the package in your project.

## The Nixpkgs Repository and the Devbox Search Index[​](#the-nixpkgs-repository-and-the-devbox-search-index "Direct link to The Nixpkgs Repository and the Devbox Search Index")

Devbox installs packages using the [Nix Package Manager](https://nixos.org). Nix maintains over
80,000 build definitions in a Github repo at [NixOS/nixpkgs](https://github.com/NixOS/nixpkgs).
Maintainers add new packages and remove outdated packages by committing changes to this repo.

Because the repository changes frequently, and new releases of Nixpkgs infrequently keep older
packages, installing older package versions with Nix can take effort. Devbox simplifies this by
maintaining a search index that maps package names and version numbers to their latest available
commit in the Nixpkgs repository. Devbox users can select packages by providing the package name and
version without looking up a Nixpkg commit.

## Pinning a Package Version[​](#pinning-a-package-version "Direct link to Pinning a Package Version")

### Searching for Available Packages[​](#searching-for-available-packages "Direct link to Searching for Available Packages")

You can look up the available versions of a package by running `devbox search <package_name>`. For
example, to see the available versions of `nodejs`, you can run `devbox search nodejs`:

```bash  theme={null}
$ devbox search nodejsFound 2+ results for "nodejs":* nodejs  (20.5.1, 20.5.0, 20.4.0, 20.3.1, 20.3.0, 20.2.0, 20.1.0, 20.0.0, 19.9.0, 19.8.1)* nodejs-slim  (20.5.1, 20.5.0, 20.4.0, 20.3.1, 20.3.0, 20.2.0, 20.1.0, 20.0.0, 19.9.0, 19.8.1)Warning: Showing top 10 results and truncated versions. Use --show-all to show all.
```

### Specifying Package Versions[​](#specifying-package-versions "Direct link to Specifying Package Versions")

If you do not include a version string, Devbox will default to using the latest available version of
the package in our Nixpkg index. This is the same as adding `<pkg>@<latest>` to your devbox.json.

For example, to use the latest version of `ripgrep,` run `devbox add ripgrep`,
`devbox add ripgrep@latest`, or add `ripgrep@latest` to your devbox.json package list.

To add a specific version of a package, write `<package_name>@<version>`. For example, to pin the
`nodejs` package to version `20.1.0`, you can run `devbox add [email protected]` or add
`[email protected]` to the packages list in your `devbox.json`:

```
"packages": [	"[email protected]"]
```

For packages that use semver, you can pin a range of versions for your project. For example, if you
pin `nodejs@20`, it will install the latest minor and patch version of `nodejs >=20.0.0`. You can
update to the newest package version that matches your criteria by running `devbox update`.

Whenever you run `devbox update`, packages will be updated to their newest versions that matches
your criteria. This means

* Packages with the latest tag will be updated to the latest version available in our index.
* Packages with a version range will be updated to the newest versions possible under that range

When you run a command that installs your packages (like `devbox shell` or `devbox install`), Devbox
will generate a `devbox.lock` file that contains the exact version and commit hash for your
packages. You should check this file into source control to ensure that other developers will get
the same environment.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/pinning-packages.md)


# Installing Platform Specific Packages
Source: https://www.jetify.com/docs/docs/devbox/guides/platform-specific-packages/index

At times, you may need to install a package or library that is only available on a specific platform. For example, you may want to install a package that is only available on Linux, while still using the same Devbox configuration on your Mac.

Devbox allows you to specify which platforms a package should be installed on using the `--platform`
and `--exclude-platform` flags. When a package is added using these flags, it will be added to your
`devbox.json`, but will only be installed when you run Devbox on a matching platform.

<Info>
  Specifying platforms for packages will alter your `devbox.json` in a way that is only compatible with **Devbox 0.5.12** and newer.

  If you encounter errors trying to run a Devbox project with platform-specific packages, you may need
  to run `devbox version update`
</Info>

## Installing Platform Specific Packages[​](#installing-platform-specific-packages "Direct link to Installing Platform Specific Packages")

To avoid build or installation errors, you can tell Devbox to only install a package on specific
platforms using the `--platform` flag when you run `devbox add`.

For example, to install the `busybox` package only on Linux platforms, you can run:

```bash  theme={null}
devbox add busybox --platform x86_64-linux,aarch64-linux
```

This will add busybox to your `devbox.json`, but will only install it when use devbox on a Linux
machine. The packages section in your config will look like the following

```json  theme={null}
{
  "packages": {
    "busybox": {
      "version": "latest",
      "platforms": ["x86_64-linux", "aarch64-linux"]
    }
  }
}
```

## Excluding a Package from Specific Platforms[​](#excluding-a-package-from-specific-platforms "Direct link to Excluding a Package from Specific Platforms")

You can also tell Devbox to exclude a package from a specific platform using the
`--exclude-platform` flag. For example, to avoid installing `ripgrep` on an ARM-based Mac, you can
run:

```bash  theme={null}
devbox add ripgrep --exclude-platform aarch64-darwin
```

This will add ripgrep to your `devbox.json`, but will not install it when use devbox on an ARM-based
Mac. The packages section in your config will look like the following:

```json  theme={null}
{
  "packages": {
    "ripgrep": {
      "version": "latest",
      "excluded_platforms": ["aarch64-darwin"]
    }
  }
}
```

## Supported Platforms[​](#supported-platforms "Direct link to Supported Platforms")

Valid Platforms include:

* `aarch64-darwin`
* `aarch64-linux`
* `x86_64-darwin`
* `x86_64-linux`

The platforms below are also supported, but will build packages from source

* `i686-linux`
* `armv7l-linux`

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/platform-specific-packages.md)


# Using Plugins
Source: https://www.jetify.com/docs/docs/devbox/guides/plugins/index

This doc describes how to use Devbox Plugins with your project.  provide a default Devbox configuration for a Nix package. Plugins make it easier to get started with packages that require additional setup when installed with Nix, and they offer a familiar interface for configuring packages. They also help keep all of your project's configuration within your project directory, which helps maintain portability and isolation.

## Using Plugins[​](#using-plugins "Direct link to Using Plugins")

### Built-in Plugins[​](#built-in-plugins "Direct link to Built-in Plugins")

If you add one of the packages listed below to your project using `devbox add <pkg>`, Devbox will
automatically activate the plugin for that package.

You can also explicitly add a built-in plugin in your project by adding it to the
[`include` section](/docs/devbox/configuration/#include) of your `devbox.json` file. For example, to
explicitly add the plugin for Nginx, you can add the following to your `devbox.json` file:

```json  theme={null}
{ "include": ["plugin:nginx"] }
```

Built-in plugins are available for the following packages. You can activate the plugins for these
packages by running `devbox add <package_name>`

* [Apache](/docs/devbox/devbox-examples/servers/apache/) (apacheHttpd)
* [Caddy](/docs/devbox/devbox-examples/servers/caddy/) (caddy)
* [Nginx](/docs/devbox/devbox-examples/servers/nginx/) (nginx)
* [Node.js](/docs/devbox/devbox-examples/languages/nodejs/) (nodejs, nodejs-slim)
* [MariaDB](/docs/devbox/devbox-examples/databases/mariadb/) (mariadb, mariadb\_10\_6...)
* [MySQL](/docs/devbox/devbox-examples/databases/mysql/) (mysql80, mysql57)
* [PostgreSQL](/docs/devbox/devbox-examples/databases/postgres/) (postgresql)
* [Redis](/docs/devbox/devbox-examples/databases/redis/) (redis)
* [Valkey](/docs/devbox/devbox-examples/databases/valkey/) (valkey)
* [PHP](/docs/devbox/devbox-examples/languages/php/) (php, php80, php81, php82...)
* [Python](/docs/devbox/devbox-examples/languages/python/) (python, python-full, python-minimal...)
* [Ruby](/docs/devbox/devbox-examples/languages/ruby/)(ruby, ruby\_3\_1, ruby\_3\_0...)
* [Elixir](/docs/devbox/devbox-examples/languages/elixir/)(elixir, elixir\_1\_16, elixir\_1\_15...)

### Local Plugins[​](#local-plugins "Direct link to Local Plugins")

You can also [define your own plugins](/docs/devbox/guides/creating-plugins/) and use them in your
project. To use a local plugin, add the following to the `include` section of your devbox.json:

```
  "include": [    "path:./path/to/plugin.json"  ]
```

### Github Hosted Plugins[​](#github-hosted-plugins "Direct link to Github Hosted Plugins")

Sometimes, you may want to share a plugin across multiple projects or users. In this case, you
provide a Github reference to a plugin hosted on Github. To install a github hosted plugin, add the
following to the include section of your devbox.json

```
  "include": [    "github:<org>/<repo>?dir=<plugin-dir>"  ]
```

Note that Devbox will cache Github plugins for 24 hours. This is to aid performance of
`devbox shell` and similar commands, and avoids downloading the plugin from Github each time. In
extenuating circumstances, you can bypass this cache by setting
`export DEVBOX_X_GITHUB_PLUGIN_CACHE_TTL=<time>` , where time is a valid input to
`time.ParseDuration` (see [doc](https://pkg.go.dev/time#ParseDuration)) such as "120s" or "2m".

## An Example of a Plugin: Nginx[​](#an-example-of-a-plugin-nginx "Direct link to An Example of a Plugin: Nginx")

Let's take a look at the plugin for Nginx. To get started, let's initialize a new devbox project,
and add the `nginx` package:

```bash  theme={null}
cd ~/my_proj
devbox init && devbox add nginx
```

Devbox will install the package, activate the `nginx` plugin, and print a short explanation of the
plugin's configuration

```bash  theme={null}
Installing nix packages. This may take a while... done.

nginx NOTES:
nginx can be configured with env variables

To customize:
* Use $NGINX_CONFDIR to change the configuration directory
* Use $NGINX_LOGDIR to change the log directory
* Use $NGINX_PIDDIR to change the pid directory
* Use $NGINX_RUNDIR to change the run directory
* Use $NGINX_SITESDIR to change the sites directory
* Use $NGINX_TMPDIR to change the tmp directory
* Use $NGINX_USER to change the user
* Use $NGINX_GROUP to customize.

Services:
* nginx

Use `devbox services start|stop [service]` to interact with services

This plugin creates the following helper files:
* ~/my_project/devbox.d/nginx/nginx.conf
* ~/my_project/devbox.d/nginx/fastcgi.conf
* ~/my_project/devbox.d/web/index.html

This plugin sets the following environment variables:
* NGINX_CONFDIR=~/my_project/devbox.d/nginx/nginx.conf
* NGINX_PATH_PREFIX=~/my_project/.devbox/virtenv/nginx
* NGINX_TMPDIR=~/my_project/.devbox/virtenv/nginx/temp

To show this information, run `devbox info nginx`

nginx (nginx-1.22.1) is now installed.
```

Based on this info page, we can see that Devbox has created the configuration we need to run `nginx`
in our local shell. Let's take a look at the files it created:

```
% tree .
├── devbox.d
│   ├── nginx
│   │   ├── fastcgi.conf
│   │   └── nginx.conf
│   └── web
│       └── index.html
└── devbox.json
```

These files give us everything we need to run NGINX, and we can modify the `nginx.conf` and
`fastcgi.conf` to customize how Nginx works.

We can also see in the info page that Devbox has configured an NGINX service for us. Let's start
this service with `devbox services start nginx`, and then test it with `curl`:

```bash  theme={null}
> devbox services start nginx
Installing nix packages. This may take a while... done.
Starting a devbox shell...
Service "nginx" started

> curl localhost:80
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Hello World!</title>
  </head>
  <body>
    Hello World!
  </body>
</html>
```

## Plugin Configuration in detail[​](#plugin-configuration-in-detail "Direct link to Plugin Configuration in detail")

When Devbox detects a plugin for an installed package, it automatically applies its configuration
and prints a short explanation. Developers can review this explanation anytime using
`devbox info <package_name>`.

### Services[​](#services "Direct link to Services")

If your package can run as a daemon or background service, Devbox can configure and manage that
service for you with `devbox services`.

To learn more, visit our page on [Devbox Services](/docs/devbox/guides/services/).

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Devbox stores default environment variables for your package in
`.devbox/virtenv/<package_name>/.env` in your project directory. Devbox automatically updates these
environment variables whenever you run `devbox shell` or `devbox run` to match your current project,
and developers should not check these `.env` files into source control.

#### Customizing Environment Variables[​](#customizing-environment-variables "Direct link to Customizing Environment Variables")

If you want to customize the environment variables, you can override them in the `init_hook` of your
`devbox.json`

### Helper Files[​](#helper-files "Direct link to Helper Files")

Helper files are files that your package may use for configuration purposes, such as NGINX's
`nginx.conf` file. When installing a package, Devbox will check for helper files in your project's
`devbox.d` folder and create them if they do not exist. If helper files are already present, Devbox
will not overwrite them.

#### Customizing Helper Files[​](#customizing-helper-files "Direct link to Customizing Helper Files")

Developers should directly edit helper files and check them into source control if needed

## Plugins Source Code[​](#plugins-source-code "Direct link to Plugins Source Code")

Devbox Plugins are written in JSON and stored in the main Devbox Repo. You can view the source code
of the current plugins [here](https://github.com/jetify-com/devbox/tree/main/plugins)

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/plugins.md)


# Running Scripts
Source: https://www.jetify.com/docs/docs/devbox/guides/scripts/index

Scripts are shell commands that can be defined in your devbox.json file. They can be executed by using the  command. Scripts started with  are launched in a interactive  that terminates once the script finishes, or is interrupted by CTRL-C.

Scripts will run after your packages finish installing, and after your `init_hook` completes.

## Configuring scripts[​](#configuring-scripts "Direct link to Configuring scripts")

Scripts can be added in your `devbox.json`. Scripts require a unique name, and a command or list of
commands to run:

```json  theme={null}
"shell": {
    "init_hook": "echo \"Hello \"",
    "scripts": {
        "echo_once": "echo \"World\"",
        "echo_twice": [
            "echo \"World\"",
            "echo \"Again\""
        ]
    }
}
```

## Running your scripts[​](#running-your-scripts "Direct link to Running your scripts")

To run a script, use `devbox run <script_name>`. This will start your shell, run your `init_hook`,
and then run the script:

```bash  theme={null}
$ devbox run echo_once
Installing nix packages. This may take a while... done.
Starting a devbox shell...
Hello
World

$ devbox run echo_twice
Installing nix packages. This may take a while... done.
Starting a devbox shell...
Hello
World
Again
```

Your devbox shell will exit once the last line of your script has finished running, or when you
interrupt the script with CTRL-C (or a SIGINT signal).

## Running a One-off Command[​](#running-a-one-off-command "Direct link to Running a One-off Command")

You can use `devbox run` to run any command in your Devbox shell, even if you have not defined it as
a script. For example, you can run the command below to print "Hello World" in your Devbox shell:

```bash  theme={null}
devbox run echo "Hello World"
```

You can also run commands that use flags as normal. For example:

```bash  theme={null}
devbox run lsof -i :80
```

Note that if you want to pass flags to `devbox run`, you should pass them before the command. For
example:

```bash  theme={null}
# Run `lsof -i :80` in your devbox shell in quiet mode
devbox run -q lsof -i :80
```

## Run Scripts with Custom Environment Variables[​](#run-scripts-with-custom-environment-variables "Direct link to Run Scripts with Custom Environment Variables")

You can use the `--env` flag to set custom environment variables in your Devbox shell. For example,
the following command will set the `MY_VAR` environment variable to `my_value` when running the
`echo` command:

```bash  theme={null}
devbox run --env MY_VAR=my_value echo $MY_VAR
```

You can also load environment variables from a .env file using the `--env-file` flag. For example,
the following command will load the environment variables from the `.env.devbox` file in your
current directory:

```bash  theme={null}
devbox run --env-file .env.devbox echo $MY_VAR
```

## Tips on using Scripts[​](#tips-on-using-scripts "Direct link to Tips on using Scripts")

1. Since `init_hook` runs every time you start your shell, you should primarily use it for setting
   environment variables and aliases. For longer running tasks like database setup, you can create
   and run a Devbox script
2. You can use Devbox scripts to start and manage long running background processes and daemons.
   1. For example -- If you are working on a LAMP stack project, you can use scripts to start MySQL
      and Apache in separate shells and monitor their logs. Once you are done developing, you can
      use CTRL-C to exit the processes and shells
3. If a script feels too long to put it directly in `devbox.json`, you can save it as a shell script
   in your project, and then invoke it in your `devbox scripts`.
4. For more ideas, see the LAMP stack example in our
   [Devbox examples repo](https://github.com/jetify-com/devbox/tree/main/examples/stacks/lapp-stack).

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/scripts.md)


# Running Services
Source: https://www.jetify.com/docs/docs/devbox/guides/services/index

When working on an application, you often want some services or dependencies running in the background for testing. Take a web app as an example. While working on your application, you will want to test it against a running development server and database. Previously developers would manage these services via tools like Docker Compose or orchestrating them manually.

With Devbox, you can manage these services from the CLI using `devbox services`. Devbox uses
[process-compose](https://github.com/F1bonacc1/process-compose#-launcher) under the hood to start
and manage your project's services.

## Starting your Services[​](#starting-your-services "Direct link to Starting your Services")

You can start all the services in your project by running `devbox services up`. This will start
process-compose in the foreground, and start all the services associated with your project:

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=f5a42b52daa70be4f1b7c62842bddf64" alt="Process Compose running in the foreground" data-og-width="1684" width="1684" data-og-height="1208" height="1208" data-path="docs/devbox/guides/services/process-compose-tui-interface.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e983b2880810ac5fff0c30e39d5775a0 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=69b55b6575deac8a5995ebf063becebe 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=4d126b6b2f3b2ea5b19fb9cf419d0845 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=bd20b234adb655d076aaedf14c0a07a8 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=764b1fce10dff13bbd0bdc60c9a370ee 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/devbox/guides/services/process-compose-tui-interface.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=414edf928f27b3132e2af0ed03a219a9 2500w" />

You can also start a specific service by passing the name as an argument. For example, to start just
`postgresql`, you can run `devbox services up postgresql`

If you want to restart your services (for example, after changing your configuration), you can run
`devbox services restart`

## Starting your Services in the Background[​](#starting-your-services-in-the-background "Direct link to Starting your Services in the Background")

If you want to start your services in the background, without launching the process-compose TUI, you
can use the `-b` flag. For example, to start all services in the background, you can run
`devbox services up -b`.

Services started in the background will continue running, even if the current shell is closed. To
stop your backgrounded services, run `devbox services stop`.

To see the current state of your running services, you can run `devbox services ls`.

You can also attach the process-compose TUI to your running background services by running
`devbox services attach`.

## Defining your Own Services[​](#defining-your-own-services "Direct link to Defining your Own Services")

If you have a process or service that you want to run with your Devbox project, you can define it
using a process-compose.yml in your project's root directory. For example, if you want to run a
Django server, you could add the following yaml:

```yaml  theme={null}
# Process compose for starting django
version: "0.5"
processes:
  django:
   command: python todo_project/manage.py runserver
   availability:
    restart: "always"
```

This will now start your django service whenever you run `devbox services up`.

## Plugins that Support Services[​](#plugins-that-support-services "Direct link to Plugins that Support Services")

The following plugins provide a pre-configured service that can be managed with `devbox services`:

* [Apache](/docs/devbox/devbox-examples/servers/apache/) (apacheHttpd)
* [Caddy](/docs/devbox/devbox-examples/servers/caddy/) (caddy)
* [Nginx](/docs/devbox/devbox-examples/servers/nginx/) (nginx)
* [PostgreSQL](/docs/devbox/devbox-examples/databases/postgres/) (postgresql)
* [Redis](/docs/devbox/devbox-examples/databases/redis/) (redis)
* [Valkey](/docs/devbox/devbox-examples/databases/valkey/) (valkey)
* [PHP](/docs/devbox/devbox-examples/languages/php/) (php, php80, php81, php82)

The service will be made available to your project when you install the packages using `devbox add`.

## Listing the Services in our Project[​](#listing-the-services-in-our-project "Direct link to Listing the Services in our Project")

You can list all the services available to your current devbox project by running
`devbox services ls`. For example, the services in a PHP web app project might look like this:

```text  theme={null}
devbox services ls
No services currently running. Run `devbox services up` to start them:
  django
  postgresql
```

If process-compose is already running, `devbox services ls` will show you the list of services
registered with process-compose and their current status

```text  theme={null}
Services running in process-compose:
NAME              STATUS          EXIT CODE
django            Running         0
postgresql        Launched        0
```

## Stopping your services[​](#stopping-your-services "Direct link to Stopping your services")

You can stop your services with `devbox services stop`. This will stop process-compose, as well as
all the running services associated with your project.

If you want to stop a specific service, you can pass the name as an argument. For example, to stop
just `postgresql`, you can run `devbox services stop postgresql`

## Further Reading[​](#further-reading "Direct link to Further Reading")

* [**Devbox Services CLI Reference**](/docs/devbox/cli-reference/devbox-services/)
* [**Devbox Plugins**](/docs/devbox/guides/plugins/)

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/services.md)


# Installing Packages from Nix Flakes
Source: https://www.jetify.com/docs/docs/devbox/guides/using-flakes/index

Devbox supports installing packages with .

Devbox currently provides two ways to use Flakes to install packages in your project:

1. You can reference a Flake hosted in Github using the `github:` reference
2. You can reference a local Flake using the `path:` reference

## What are Flakes?[​](#what-are-flakes "Direct link to What are Flakes?")

[Flakes](https://www.jetify.com/blog/powered-by-flakes/) are a new feature in the Nix language that
lets you package software and create development shells in a declarative, fully reproducible way.
You can use Nix Flakes to define packages, apps, templates, and dev environments.

Flakes are defined as a directory with a `flake.nix` and a `flake.lock` file. You import flakes to
your project using a flake reference, which describes where to find the Flake, and what version or
revision to use

## Using a Flake from Github[​](#using-a-flake-from-github "Direct link to Using a Flake from Github")

You can add a Flake hosted on Github using the following string in your packages list:

```
"packages": [    "github:<org>/<repo>/<ref>#<optional_flake_attr>"]
```

The Ref and Flake Attribute is optional and will default to the main branch and
`packages.default|defaultPackage` attribute, respectively.

For example, to install [Process Compose](https://github.com/F1bonacc1/process-compose) from its
repository using Nix Flakes, you can use the following string in your packages list. This will
install the latest version of Process Compose from the `main` branch.

```nix  theme={null}
github:F1bonacc1/process-compose
```

### Installing a Flake from a specific branch or tag[​](#installing-a-flake-from-a-specific-branch-or-tag "Direct link to Installing a Flake from a specific branch or tag")

You can install a specific release or branch by adding it to your flake reference. The following
example will install Process Compose version 0.40.2 from the `v0.40.2` tag.

```nix  theme={null}
github:F1bonacc1/process-compose/v0.40.2
```

### Installing a specific attribute or package from a Flake[​](#installing-a-specific-attribute-or-package-from-a-flake "Direct link to Installing a specific attribute or package from a Flake")

You can also install a specific attribute or package from a Flake by adding a `#` and the attribute
name to the end of the package string. If you don't specify an attribute, Devbox will use `default`
or `defaultPackage`

For example, if you want to use [Fenix](https://github.com/nix-community/fenix) to install a
specific version of Rust, you can use the following string in your packages list. This example will
install the `stable.toolchain` packages from the `fenix` package.

```nix  theme={null}
github:nix-community/fenix#stable.toolchain
```

### Using Flakes with Nixpkgs[​](#using-flakes-with-nixpkgs "Direct link to Using Flakes with Nixpkgs")

The Nixpkgs repo on Github also provides a Flake for installing packages. You can use the following
flake reference to install packages from a specific Nixpkgs commit or reference:

```nix  theme={null}
github:NixOS/nixpkgs/<ref>#<package>
```

For example, if you want to install the `hello` package from the `nixos-20.09` branch, you can use
the following string in your packages list:

```nix  theme={null}
github:NixOS/nixpkgs/nixos-20.09#hello
```

## Installing Additional Outputs from a Flake[​](#installing-additional-outputs-from-a-flake "Direct link to Installing Additional Outputs from a Flake")

Some packages provide additional outputs that are not installed by default. For example, the
`libcap` package provides a `dev` output that contains development headers and libraries, or the
`prometheus` package includes the `promtool` CLI in a `cli` output.

You can install these additional outputs by adding a `^` and a comma-separated list of outputs to
the end of your flake reference. For example, the following command will install the default (`out`)
and `dev` outputs of the `libcap` package:

```nix  theme={null}
github:nixos/nixpkgs#libcap^out,dev
```

## Using a Local Flake[​](#using-a-local-flake "Direct link to Using a Local Flake")

You can also use a local Flake using the `path` attribute in your package list. Using a local flake
can be helpful if you want to install your custom packages with Nix, or if you need to modify
packages before using them in your Devbox project

Your flake reference should point to a directory that contains a `flake.nix` file.

```
path:<path_to_flake>#<optional_flake_attr>
```

For example, if you have a local Flake in the `./my-flake` directory, you can use the following
string in your `packages` list. This example will install all the packages under the `my-package`
attribute.

```nix  theme={null}
path:./my-flake#my-package
```

## Caching Flakes with the Jetify Cache[​](#caching-flakes-with-the-jetify-cache "Direct link to Caching Flakes with the Jetify Cache")

Because flakes are not automatically built and cached by Nix, you may experience slower build times
when using flakes in your Devbox project. To speed up your builds, you can use the
[Jetify Cache](/docs/cloud/cache/) to cache the binaries built by your flakes for future use.

After setting up your cache directly, you can upload the flake by running:

```bash  theme={null}
devbox cache upload <flake-reference>
```

Alternatively, you can cache your entire project closure by running the following command from your
project root:

```bash  theme={null}
devbox cache upload
```

### Examples[​](#examples "Direct link to Examples")

For more examples of using Nix Flakes with Devbox, check out the examples in our Devbox Repo:

* [Using Nix Flakes from Github](https://github.com/jetify-com/devbox/tree/main/examples/flakes/remote)
* [Using a Local Flake](https://github.com/jetify-com/devbox/tree/main/examples/flakes/php)
* [Applying an Overlay with Nix Flakes](https://github.com/jetify-com/devbox/tree/main/examples/flakes/overlay)

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/guides/using-flakes.md)


# direnv
Source: https://www.jetify.com/docs/docs/devbox/ide-configuration/direnv/index



## direnv[​](#direnv "Direct link to direnv")

***

[direnv](https://direnv.net) is an open source environment management tool that allows setting
unique environment variables per directory in your file system. This guide covers how to configure
direnv to seamlessly work with a devbox project.

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Install direnv and hook it to your shell. Follow
  [this guide](https://direnv.net/#basic-installation) if you haven't done it.

### Setting up Devbox Shell and direnv[​](#setting-up-devbox-shell-and-direnv "Direct link to Setting up Devbox Shell and direnv")

#### New Project[​](#new-project "Direct link to New Project")

If you have direnv installed, Devbox will generate an .envrc file when you run
`devbox generate direnv` and enables it by running `direnv allow` in the background:

````bash  theme={null}
➜  devbox generate direnvSuccess: generated .envrc fileSuccess: ran `direnv allow`direnv: loading ~/src/docs/devbox/.envrcdirenv: using devbox
```bash

This will generate a `.envrc` file in your project directory that contains `devbox.json`. Run
`direnv allow` to activate your shell upon directory navigation. Run `direnv revoke` to stop.
Changes to `devbox.json` automatically trigger direnv to reset the environment. The generated
`.envrc` file doesn't need any further configuration. Just having the generated file along with an
installed direnv and Devbox is enough to make direnv integrate with Devbox.

#### Existing Project[​](#existing-project "Direct link to Existing Project")

For an existing project, you can add a `.envrc` file by running `devbox generate direnv`:

```bash
➜  devbox generate direnvSuccess: generated .envrc fileSuccess: ran `direnv allow`direnv: loading ~/src/docs/devbox/.envrcdirenv: using devbox
````

The generated `.envrc` file doesn't need any further configuration. Just having the generated file
along with installed direnv and Devbox, is enough to make direnv integration with Devbox work.

#### Adding Custom Env Variables or Env Files to your Direnv Config[​](#adding-custom-env-variables-or-env-files-to-your-direnv-config "Direct link to Adding Custom Env Variables or Env Files to your Direnv Config")

In some cases, you may want to override certain environment variables in your Devbox config when
running it locally. You can add custom environment variables from the command line or from a file
using the `--env` and `--env-file` flags.

If you would like to add custom environment variables to your direnv config, you can do so by
passing the `--env` flag to `devbox generate direnv`. This flag takes a comma-separated list of
key-value pairs, where the key is the name of the environment variable and the value is the value of
the environment variable. For example, if you wanted to add a `MY_CUSTOM_ENV_VAR` environment
variable with a value of `my-custom-value`, you would run the following command:

````bash  theme={null}
devbox generate direnv --env MY_CUSTOM_ENV_VAR=my-value
```bash

The resulting .envrc will have the following:

```bash
# Automatically sets up your devbox environment whenever you cd into this# directory via our direnv integration:eval "$(devbox generate direnv --print-envrc --env MY_CUSTOM_ENV_VAR=my-value)"# check out https://www.jetify.com/docs/devbox/ide-configuration/direnv/# for more details
````

You can also tell direnv to read environment variables from a custom `.env` file by passing the
`--env-file` flag to `devbox generate direnv`. This flag takes a path to a file containing
environment variables to set in the devbox environment. If the file does not exist, then this
parameter is ignored. For example, if you wanted to add a `.env.devbox` file located in your project
root, you would run the following command:

````bash  theme={null}
devbox generate direnv --env-file .env.devbox
```bash

The resulting .envrc will have the following:

```bash
# Automatically sets up your devbox environment whenever you cd into this# directory via our direnv integration:eval "$(devbox generate direnv --print-envrc --env-file .env.devbox)"# check out https://www.jetify.com/docs/devbox/ide-configuration/direnv/# for more details
````

Note that if Devbox cannot find the env file provided to the flag, it will ignore the flag and load
your Devbox shell environment as normal

### Global settings for direnv[​](#global-settings-for-direnv "Direct link to Global settings for direnv")

Note that every time changes are made to `devbox.json` via `devbox add ...`, `devbox rm ...` or
directly editing the file, requires `direnv allow` to run so that `direnv` can setup the new
changes.

Alternatively, a project directory can be whitelisted so that changes will be automatically picked
up by `direnv`. This is done by adding following snippet to direnv config file typically at
`~/.config/direnv/direnv.toml`. You can create the file and directory if it doesn't exist.

```bash  theme={null}
[whitelist]prefix = [ "/absolute/path/to/project" ]
```

### Direnv Limitations[​](#direnv-limitations "Direct link to Direnv Limitations")

Direnv works by creating a sub-shell using your `.envrc` file, your `devbox.json`, and other direnv
related files, and then exporting the diff in environment variables into your current shell. This
imposes some limitations on what it can load into your shell:

1. Direnv cannot load shell aliases or shell functions that are sourced in your project's
   `init_hook`. If you want to use direnv and also configure custom aliases, we recommend using
   [Devbox Scripts](/docs/devbox/guides/scripts/).
2. Direnv does not allow modifications to the \$PS1 environment variable. This means `init_hooks`
   that modify your prompt will not work as expected. For more information, see the
   [direnv wiki](https://github.com/direnv/direnv/wiki/PS1)

Note that sourcing aliases, functions, and `$PS1` should work as expected when using `devbox shell`,
`devbox run`, and `devbox services`

### VSCode setup with direnv[​](#vscode-setup-with-direnv "Direct link to VSCode setup with direnv")

To seamlessly integrate VSCode with a direnv environment, follow these steps:

1. Open a terminal window and activate direnv with `direnv allow`.
2. Launch VSCode from the same terminal window using the command `code .` This ensures that VSCode
   inherits the direnv environment.

Alternatively, you can use the
[direnv VSCode extension](https://marketplace.visualstudio.com/items?itemName=mkhl.direnv) if your
VSCode workspace has a .envrc file.

If this guide is missing something, feel free to contribute by opening a
[pull request](https://github.com/jetify-com/devbox/pulls) in Github.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/ide-configuration/direnv.md)


# Eclipse IDE
Source: https://www.jetify.com/docs/docs/devbox/ide-configuration/eclipse/index



## Java[​](#java "Direct link to Java")

This guide describes how to configure Eclipse to work with a devbox Java environment.

### Setting up Devbox shell[​](#setting-up-devbox-shell "Direct link to Setting up Devbox shell")

To create a devbox shell make sure to have devbox installed. If you don't have devbox installed
follow the installation guide first. Then run the following commands from the root of your project's
repo:

1. `devbox init` if you don't have a devbox.json in the root directory of your project.

2. `devbox add jdk` to make sure jdk gets installed in your devbox shell.

3. `devbox shell -- 'echo $JAVA_HOME'` to activate your devbox shell temporarily to find the path to
   your java home. Copy and save the path. It should look something like:

   ```
   /nix/store/qaf9fysymdoj19qtyg7209s83lajz65b-zulu17.34.19-ca-jdk-17.0.3
   ```

4. Open Eclipse IDE and create a new Java project if you don't have already

5. From the top menu go to Run > Run Configurations > JRE and choose **Alternate JRE:**

6. Click on **Installed JREs...** and click **Add...** in the window of Installed JREs.

7. Choose **Standard VM** as JRE Type and click Next.

8. Paste the value you copied in step 4 in **JRE HOME** and put an arbitrary name such as
   "devbox-jre" in **JRE Name** and click Finish.

9. Click **Apply and Close** in Installed JREs window. Then close Run Configurations.

Now your project in Eclipse is setup to compile and run with the same Java that is installed in your
devbox shell. Next step is to run your Java code inside Devbox.

### Setting up Eclipse Terminal[​](#setting-up-eclipse-terminal "Direct link to Setting up Eclipse Terminal")

The following steps show how to run a Java application in a devbox shell using the Eclipse terminal.
Note that most of these steps are not exclusive to Eclipse and can also be used in any Linux or
macOS terminal.

1. Press `ctrl + alt/opt + T` to open terminal window in Eclipse.

2. Navigate to the projects root directory using `cd` command.

3. Make sure `devbox.json` is present in the root directory `ls | grep devbox.json`

4. Run `devbox shell` to activate devbox shell in the terminal.

5. Use `javac` command to compile your Java project. As an example, if you have a simple hello world
   project and the directory structure such as:

   ```
   my_java_project/-- src/-- -- main/-- -- -- hello.java
   ```

   You can use the following command to compile: to compile:

   ```bash  theme={null}
   javac my_java_project/src/main/hello.java
   ```

6. Use `java` command to run the compiled project. For example, to run the sample project from above:

   ```bash  theme={null}
   cd src/java main/hello
   ```

If this guide is missing something, feel free to contribute by opening a
[pull request](https://github.com/jetify-com/devbox/pulls) in Github.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/ide-configuration/eclipse.md)


# Visual Studio Code
Source: https://www.jetify.com/docs/docs/devbox/ide-configuration/vscode/index



## Devbox Extension[​](#devbox-extension "Direct link to Devbox Extension")

***

Devbox has an accompanying [VSCode extension](vscode:extension/jetify-com.devbox) that makes the
experience of integrating your devbox environment in VSCode much simpler.

### Syncing VSCode with Devbox shell[​](#syncing-vscode-with-devbox-shell "Direct link to Syncing VSCode with Devbox shell")

Follow the steps below to have VSCode's environment be in sync with Devbox shell:

1. [Install](vscode:extension/jetify-com.devbox) Devbox's VSCode extension
2. Open a project that has a devbox.json file in VSCode
3. Open command palette in VSCode (cmd+shift+p) and type:
   `Devbox: Reopen in Devbox shell environment`
4. Press Enter and wait for VSCode to reload.
5. The newly opened VSCode is now integrated with the environment defined your devbox.json. You can
   test it by checking if packages defined in devbox.json are available in VSCode integrated
   terminal.

Keep in mind that if you make changes to your devbox.json, you need to re-run Step 3 to make VSCode
pick up the new changes.

**NOTE:** This integration feature requires Devbox CLI v0.5.5 and above installed and in PATH. This
feature is in beta. Please report any bugs/issues in [Github](https://github.com/jetify-com/devbox)
or our [Discord](https://discord.gg/jetify).

**NOTE2:** This feature is not yet available for Windows and WSL.

### Automatic Devbox shell in VSCode Terminal[​](#automatic-devbox-shell-in-vscode-terminal "Direct link to Automatic Devbox shell in VSCode Terminal")

Devbox extension runs `devbox shell` automatically every time VSCode's integrated terminal is
opened, **if the workspace opened in VSCode has a devbox.json file**.

This setting can be turned off in VSCode's settings. Simply search for `devbox.autoShellOnTerminal`
in settings or add the following to VSCode's settings.json:

```json  theme={null}
"devbox.autoShellOnTerminal": false
```

Note that running `devbox shell` is not necessary if VSCode is reopened in Devbox shell environment
via the steps described in [Syncing VSCode with Devbox shell](#syncing-vscode-with-devbox-shell)

## Direnv Extension[​](#direnv-extension "Direct link to Direnv Extension")

***

Direnv is an open source environment management tool that allows setting unique environment
variables per directory in your file system. For more details on how to set it and integrate it with
Devbox visit [our Direnv setup guide](/docs/devbox/ide-configuration/direnv/).

Once Direnv is installed and setup with Devbox, its [VSCode extension](vscode:extension/mkhl.direnv)
can also be used to integrate the environment defined in your devbox.json to VSCode. To do that
follow the steps below:

1. Install Direnv ([link to guide](https://direnv.net/#basic-installation))
2. Setup Devbox shell with Direnv
   ([link to guide](/docs/devbox/ide-configuration/direnv/#setting-up-devbox-shell-and-direnv))
3. Install Direnv's [VSCode extension](vscode:extension/mkhl.direnv)
4. Open your Devbox project in VSCode. Direnv extension should show a prompt notification to reload
   your environment.
5. Click on reload.

## Windows Setup[​](#windows-setup "Direct link to Windows Setup")

***

Devbox CLI is not supported on Windows, but you can still use it with VSCode by using Windows
Subsystem for Linux ([WSL](https://learn.microsoft.com/en-us/windows/wsl/install)). If you've set up
WSL, follow these steps to integrate your Devbox shell environment with VSCode:

1. [Install](https://www.jetify.com/docs/devbox/installing-devbox/) Devbox in WSL.
2. Navigate to your project directory. (`C:\Users` is `/mnt/c/Users/` in WSL).
3. Run `devbox init` if you don't have a devbox.json file.
4. Run `devbox shell`
5. Run `code .` to open VSCode in Windows and connect it remotely to your Devbox shell in WSL.

## Manual Setup[​](#manual-setup "Direct link to Manual Setup")

***

VS Code is a popular editor that supports many different programming languages. This section covers
how to configure VS Code to work with a devbox Java environment as an example.

### Setting up Run and Debugger[​](#setting-up-run-and-debugger "Direct link to Setting up Run and Debugger")

To create a devbox shell make sure to have devbox installed. If you don't have devbox installed
follow the installation guide first. Then follow the steps below:

1. `devbox init` if you don't have a devbox.json in the root directory of your project.

2. `devbox add jdk` to make sure jdk gets installed in your devbox shell.

3. `devbox shell -- 'which java` to activate devbox shell temporarily and find the path to your
   executable java binary inside the devbox shell. Copy and save that path. It should look something
   like this:

```json  theme={null}
   /nix/store/qaf9fysymdoj19qtyg7209s83lajz65b-zulu17.34.19-ca-jdk-17.0.3/bin/java
```

4. Open VS Code and create a new Java project if you don't have already. If VS Code prompts for
   installing Java support choose yes.

5. Click on **Run and Debug** icon from the left sidebar.

6. Click on **create a launch.json** link in the opened sidebar. If you don't see such a link, click
   on the small gear icon on the top of the open sidebar.

7. Once the `launch.json` file is opened, update the `configurations` parameter to look like snippet
   below:

   ```json  theme={null}
   {
     "type": "java",
     "name": "Launch Current File",
     "request": "launch",
     "mainClass": "<project_directory_name>/<main_package>.<main_class>",
     "projectName": "<project_name>",
     "javaExec": "<path_to_java_executable_from_step_4>"
   }
   ```

```json  theme={null}

   Update the values in between \< and > to match your project and environment.

8. Click on **Run and Debug** or the green triangle at the top of the left sidebar to run and debug
   your project.

Now your project in VS Code is setup to run and debug with the same Java that is installed in your
devbox shell. Next step is to run your Java code inside Devbox.

### Setting up Terminal[​](#setting-up-terminal "Direct link to Setting up Terminal")

The following steps show how to run a Java application in a devbox shell using the VS Code terminal.
Note that most of these steps are not exclusive to VS Code and can also be used in any Linux or
macOS terminal.

1. Open VS Code terminal (`ctrl + shift + ~` in MacOS)

2. Navigate to the projects root directory using `cd` command.

3. Make sure `devbox.json` is present in the root directory `ls | grep devbox.json`

4. Run `devbox shell` to activate devbox shell in the terminal.

5. Use `javac` command to compile your Java project. As an example, if you have a simple hello world
   project and the directory structure such as:

```

my\_java\_project/-- src/-- -- main/-- -- -- hello.java

````json  theme={null}

   You can use the following command to compile: to compile:

   ```bash
   javac my_java_project/src/main/hello.java
````

6. Use `java` command to run the compiled project. For example, to run the sample project from above:

   ```bash  theme={null}
   cd src/java main/hello
   ```

```json  theme={null}

If this guide is missing something, feel free to contribute by opening a
[pull request](https://github.com/jetify-com/devbox/pulls) in Github.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/ide-configuration/vscode.md)
```


# Zed Editor
Source: https://www.jetify.com/docs/docs/devbox/ide-configuration/zed/index

Zed is a fast, open source code editor designed for collaboration and AI support, that is available for macOS and Linux. Zed has support for loading environments directly from Direnv's  files, meaning you can easily use Zed w/ Devbox via our .

## Setting up your Project for Zed[​](#setting-up-your-project-for-zed "Direct link to Setting up your Project for Zed")

1. Make sure that you have direnv installed on your host. To use direnv across all your projects, we
   recommend installing it with [devbox global](/docs/devbox/devbox-global/) using
   `devbox global add direnv`. You can also follow
   [this guide](https://direnv.net/#basic-installation) to configure direnv for your system

2. Generate a `.envrc` file for your project by running `devbox generate direnv` in your project's
   root directory (the same directory with your `devbox.json` file.

3. You can now open your project in Zed and it will automatically load your Devbox shell environment
   variables from the `.envrc` file.

## Troubleshooting your Zed Setup[​](#troubleshooting-your-zed-setup "Direct link to Troubleshooting your Zed Setup")

If you are having trouble getting Zed's LSP to detect your Devbox environment, try the following
steps:

1. Make sure you are up to date with the latest version of Zed. You can check for updates by going
   to `Zed > Check for Updates` in the Zed menu.

2. You may need to explicitly tell your LSP to use the binaries in your \$PATH variable. To do this,
   add the following to the `~/.config/zed/config.json` file:

```json  theme={null}
{
  ...
  "lsp": {
    "<lsp-name>": {
      "binary": {"path_lookup": true}
    }
  },
  ...
}
```

3. If you have a version of the binary/language server installed on your host machine, Zed's default
   behavior for loading direnv directly may cause conflicts with the packages installed via Devbox.
   To fix this, add the following to your `~/.config/zed/config.json` file:

```json  theme={null}
{ "load_direnv": "shell_hook" }
```

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/ide-configuration/zed.md)


# What is Devbox?
Source: https://www.jetify.com/docs/docs/devbox/index

Devbox is a command-line tool that lets you easily create isolated shells for development. You start by defining the list of packages required for your project, and Devbox creates an isolated, reproducible environment with those packages installed.

In practice, Devbox works similar to a package manager like yarn – except the packages it manages
are at the operating-system level (the sort of thing you would normally install with brew or
apt-get).

<Frame caption="Create isolated dev environments on the fly with Devbox">
    <img src="https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=3b991128527cad0eb62569268d2e577c" alt="Devbox isolated shell environment" data-og-width="710" width="710" data-og-height="472" height="472" data-path="docs/devbox/devbox-isolated-shell-environment.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?w=280&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=716425148e24dd338ac1079a887eb55e 280w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?w=560&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=50fa2a42b2cdff607ad909f5d3dd17e3 560w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?w=840&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=3d30b75561f3b48ae592e6f54be12f44 840w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?w=1100&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=28c735b78457fbb39b01bb5cac07cc3b 1100w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?w=1650&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=c98ce8fa5e03151dd3124b7b9b43a3e3 1650w, https://mintcdn.com/jetify/jyk5Hl_irNQ736vI/docs/devbox/devbox-isolated-shell-environment.svg?w=2500&fit=max&auto=format&n=jyk5Hl_irNQ736vI&q=85&s=3d632a442121a442e27c62e973806390 2500w" />
</Frame>

## Why Use Devbox?[​](#why-use-devbox "Direct link to Why Use Devbox?")

Devbox provides a lot of benefits over pure Docker containers, Nix Shells, or managing your own
environment directly:

### A consistent shell for everyone on the team[​](#a-consistent-shell-for-everyone-on-the-team "Direct link to A consistent shell for everyone on the team")

Declare the list of tools needed by your project via a `devbox.json` file and run devbox shell.
Everyone working on the project gets a shell environment with the exact same version of those tools.

### Try new tools without polluting your laptop[​](#try-new-tools-without-polluting-your-laptop "Direct link to Try new tools without polluting your laptop")

Development environments created by Devbox are isolated from everything else in your laptop. Is
there a tool you want to try without making a mess? Add it to a Devbox shell, and remove it when you
don't want it anymore – all while keeping your laptop pristine. Removing or changing a package in
your dev environment is as easy as editing your `devbox.json`.

### Don't sacrifice speed[​](#dont-sacrifice-speed "Direct link to Don't sacrifice speed")

Devbox can create isolated environments right on your laptop, without an extra-layer of
virtualization slowing your file system or every command. When you're ready to ship, it'll turn it
into an equivalent container – but not before.

### Good-bye conflicting versions[​](#good-bye-conflicting-versions "Direct link to Good-bye conflicting versions")

Are you working on multiple projects, all of which need different versions of the same binary?
Instead of attempting to install conflicting versions of the same binary on your laptop, create an
isolated environment for each project, and use whatever version you want for each.

### Take your environment with you[​](#take-your-environment-with-you "Direct link to Take your environment with you")

Devbox's dev environments are *portable*. We make it possible to declare your environment exactly
once, and use that single definition in several different ways, including:

* A local shell created through `devbox shell`
* A devcontainer you can use with VSCode
* A Dockerfile so you can build a production image with the exact same tools you used for
  development.
* A remote development environment in the cloud that mirrors your local environment.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/index.md)


# Installing Devbox
Source: https://www.jetify.com/docs/docs/devbox/installing-devbox/index



## Install Devbox[​](#install-devbox "Direct link to Install Devbox")

Select your OS below for the steps to install Devbox.

* Linux
* MacOS
* Windows/WSL2
* NixOS/Nixpkg
* Nix Flake

Run the following install script as a *non-root user* to install the latest version of Devbox:

```bash  theme={null}
curl -fsSL https://get.jetify.com/devbox | bash
```

Devbox requires the [Nix Package Manager](https://nixos.org/download.html). If Nix is not detected
when running a command, Devbox will install it for you in single-user mode for Linux. Don't worry:
You can use Devbox without needing to learn the Nix Language.

If you would like to install Nix yourself, we recommend the
[Determinate Nix Installer](https://determinate.systems/nix-installer/).

Run the following install script to install the latest version of Devbox:

```bash  theme={null}
curl -fsSL https://get.jetify.com/devbox | bash
```

Devbox requires the [Nix Package Manager](https://nixos.org/download.html). If Nix is not detected
when running a command, Devbox will install it in multi-user mode for macOS. Don't worry: You can
use Devbox without needing to learn the Nix Language.

If you would like to install Nix yourself, we recommend the
[Determinate Nix Installer](https://determinate.systems/posts/determinate-nix-installer).

You can use Devbox on a Windows machine using
[**Windows Subsystem for Linux 2**](https://learn.microsoft.com/en-us/windows/wsl/install).

<Accordion title="Installing WSL2">
  To install WSL2 with the default Ubuntu distribution, open Powershell or Windows Command Prompt as an administrator, and run:

  ```bash  theme={null}
  wsl --install
  ```

  If WSL2 is already installed, you can install Ubuntu by running

  ```bash  theme={null}
  wsl --install -d Ubuntu
  ```

  If you are running an older version of Windows, you may need to follow the
  [manual installation steps](https://learn.microsoft.com/en-us/windows/wsl/install-manual) to enable
  virtualization and WSL2 on your system. See the
  [official docs](https://learn.microsoft.com/en-us/windows/wsl/install) for more details
</Accordion>

Run the following script in your WSL2 terminal as a *non-root user* to install Devbox.

```bash  theme={null}
curl -fsSL https://get.jetify.com/devbox | bash
```

Devbox requires the [Nix Package Manager](https://nixos.org/download/). If Nix is not detected on
your machine when running a command, Devbox will automatically install it in single user mode for
WSL2. Don't worry: You can use Devbox without needing to learn the Nix Language.

Devbox is available through the
[**Nix Package Manager**](https://search.nixos.org/packages?channel=unstable\&show=devbox\&from=0\&size=50\&sort=relevance\&type=packages\&query=devbox).

To install on NixOS:

```bash  theme={null}
nix-env -iA nixos.devbox
```

To install on a non NixOS:

```bash  theme={null}
nix-env -iA nixpkgs.devbox
```

or

```bash  theme={null}
nix profile install nixpkgs#devbox
```

Note: New releases of Devbox need to be updated in Nixpkgs before they are available for
installation. If you want to use the latest version of Devbox, you can install it using the
[Nix Flake](/docs/devbox/installing-devbox/?install-method=flake).

You can also install Devbox on a NixOS/Nixpkgs system using our Nix Flake. Using the Nix Flake can
help you access pre-releases and final releases of Devbox as soon as they are published.

To get the latest version:

```bash  theme={null}
nix profile install github:jetify-com/devbox/latest
```

To install a specific version, you can run the following command (only supports versions 0.13.2 and
above).

```bash  theme={null}
nix profile install github:jetify-com/devbox/0.13.2
```

## Updating Devbox[​](#updating-devbox "Direct link to Updating Devbox")

Devbox will notify you when a new version is available. To update to the latest released version of
Devbox, you can run `devbox version update`.

If you installed Devbox with Nix, you can update Devbox via Nix using `nix-env -u devbox`, or
`nix profile upgrade`.

You can find release notes and details on the
[Releases page](https://github.com/jetify-com/devbox/releases) of the Devbox Github repo.

## Rolling Back or Pinning a Specific Version of Devbox[​](#rolling-back-or-pinning-a-specific-version-of-devbox "Direct link to Rolling Back or Pinning a Specific Version of Devbox")

You can rollback or pin the version of Devbox on your system using the `DEVBOX_USE_VERSION`
environment variable. For example, to use version 0.8.0:

```bash  theme={null}
export DEVBOX_USE_VERSION=0.8.0
```

Setting this variable will use the specified version of Devbox even if a newer version has been
installed on your machine.

If you installed Devbox with Nixpkgs, you will need to pin Devbox in your profile or Nix
configuration. You can find the Nixpkg commits for previous versions of Devbox on
[Nixhub](https://www.nixhub.io/packages/devbox).

## Next Steps[​](#next-steps "Direct link to Next Steps")

* **[Getting Started](/docs/devbox/quickstart/):** Learn how to create a dev environment with Devbox
* **[Devbox Global](/docs/devbox/devbox-global/):** Learn how to use the devbox as a global package
  manager

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/installing-devbox.mdx)


# Create a Dev Environment with Devbox
Source: https://www.jetify.com/docs/docs/devbox/quickstart/index



## Background[​](#background "Direct link to Background")

Devbox is a command-line tool that lets you easily create reproducible, reliable dev environments.
You start by defining the list of packages required by your development environment, and devbox uses
that definition to create an isolated environment just for your application. Developers can start
their dev environment by running `devbox shell` within your project.

To learn more about how Devbox works, you can read our [introduction](/docs/devbox/)

This Quickstart shows you how to install Devbox and use it to create a new Development Environment
for your project.

## Install Devbox[​](#install-devbox "Direct link to Install Devbox")

Follow the instruction from [the installation guide](/docs/devbox/installing-devbox/).

## Create a Development Environment[​](#create-a-development-environment "Direct link to Create a Development Environment")

We'll create a new development environment with the packages we need. These packages will only be
available when using this Devbox shell, ensuring we don’t pollute your machine.

1. Open a terminal in a new empty folder.

2. Initialize Devbox:

   ```bash  theme={null}
   devbox init
   ```

   This creates a `devbox.json` file in the current directory. You should commit it to source
   control.

3. Search for packages to add to your Devbox project with `devbox search`. For example, to search
   for Python packages, you can run the `devbox search python3`

4. You can add a package to your project by running `devbox add <package>`. For example, running the
   following will install the latest available version of RipGrep in your project:

   ```bash  theme={null}
   devbox add ripgrep
   ```

   If you want to install a specific version of a package, you can run
   `devbox add <package>@<version>`. For example, to install Python 3.10, you can run:

   ```bash  theme={null}
   devbox add [email protected]
   ```

5. Your `devbox.json` file keeps track of the packages you've added, it should now look like this:

   ```json  theme={null}
   {
     "packages": ["ripgrep@latest", "[email protected]"]
   }
   ```

## Launch your Development Environment[​](#launch-your-development-environment "Direct link to Launch your Development Environment")

1. Start a new shell that has your packages and tools installed:

   ```bash  theme={null}
   devbox shell
   ```

   <Info>
     The first time you run `devbox shell` may take a while to complete due to Devbox downloading
     prerequisites and package catalogs required by Nix. This delay is a one-time cost, and future
     invocations and package additions should resolve much faster.
   </Info>

   You can tell you're in a Devbox shell (and not your regular terminal) because the shell prompt
   and directory changed.

2. Use your favorite packages.

   In this example we installed Python 3.10, so let's use it.

   ```bash  theme={null}
   $ python --version
   Python 3.10.0
   ```

   We will also have the latest version of ripgrep installed in our shell:

   ```bash  theme={null}
   $ rg --version
   ripgrep 13.0.0-SIMD -AVX (compiled)
   ```

3. Your regular tools are also available including environment variables and config settings.

   ```bash  theme={null}
   git config --get user.name
   ```

4. To exit the Devbox shell and return to your regular shell:

   ```bash  theme={null}
   exit
   ```

5. To share your project and shell, make sure to check in your `devbox.json` and `devbox.lock` file
   into source control. These files will ensure that developers get the same packages and
   environment when they run your project.

## Add the Devbox Badge to your Repo[​](#add-the-devbox-badge-to-your-repo "Direct link to Add the Devbox Badge to your Repo")

Once you publish your Devbox project to Github, you can help other developers get started by adding
the Devbox Badge to your repo. Please copy the code snippets below and paste them into your
README.md to add the badge

[<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=be7849d4f3a3e00cdbe2ba224d03e519" alt="Built with Devbox" data-og-width="110" width="110" data-og-height="20" height="20" data-path="docs/images/devbox/badges/devbox-badge-galaxy.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=91c053fddd06700f361367d707ad9a1b 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=12b52db7a6e3ca4b25c6ced9453ae287 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=36a790e424132ac2f50b1bf8c7d219fa 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=31438086329d7589238ac3f43f800014 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ecd8eaeb818c5e3c8acd2d45eb343e76 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-galaxy.svg?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ab1e3c3cefc4beae8cdea11b54055189 2500w" />](https://www.jetify.com/devbox/docs/contributor-quickstart/)

* Markdown
* HTML

```markdown  theme={null}
[![Built with Devbox](https://www.jetify.com/img/devbox/shield_galaxy.svg)](https://www.jetify.com/devbox/docs/contributor-quickstart/)
```

```html  theme={null}
<a href="https://www.jetify.com/devbox/docs/contributor-quickstart/">
    <img
        src="https://www.jetify.com/img/devbox/shield_galaxy.svg"
        alt="Built with Devbox"
    />
</a>
```

[<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=e64f4e9e90bb6cc9be67c7426b189175" alt="Built with Devbox" data-og-width="110" width="110" data-og-height="21" height="21" data-path="docs/images/devbox/badges/devbox-badge-moon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=efe49dea5abdea0800d265aea21ec2f5 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=ceb943f007e453f03780bcea28913fe5 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=97502a74430543d09a4c089cb8a6850a 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=7cfa0297f26649b0776dc0a17415c8ae 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=1cdb70c63ee3fe10bdb02a32e165d1a3 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/images/devbox/badges/devbox-badge-moon.svg?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=189ab34774f899f208c390d1c4be8b15 2500w" />](https://www.jetify.com/devbox/docs/contributor-quickstart/)

* Markdown
* HTML

```markdown  theme={null}
[![Built with Devbox](https://www.jetify.com/img/devbox/shield_moon.svg)](https://www.jetify.com/devbox/docs/contributor-quickstart/)
```

```html  theme={null}
<a href="https://www.jetify.com/devbox/docs/contributor-quickstart/">
    <img
        src="https://www.jetify.com/img/devbox/shield_moon.svg"
        alt="Built with Devbox"
    />
</a>
```

## Next Steps[​](#next-steps "Direct link to Next Steps")

### Learn more about Devbox[​](#learn-more-about-devbox "Direct link to Learn more about Devbox")

* **[Devbox Global](/docs/devbox/devbox-global/):** Learn how to use the devbox as a global package
  manager
* **[Devbox Scripts](/docs/devbox/guides/scripts/):** Automate setup steps and configuration for
  your shell using Devbox Scripts.
* **[Configuration Guide](/docs/devbox/configuration/):** Learn how to configure your shell and dev
  environment with `devbox.json`.
* **[Browse Examples](https://github.com/jetify-com/devbox/tree/main/examples):** You can see how to
  create a development environment for your favorite tools or languages by browsing the Devbox
  Examples repo.

### Use Devbox with your IDE[​](#use-devbox-with-your-ide "Direct link to Use Devbox with your IDE")

* **[Direnv Integration](/docs/devbox/ide-configuration/direnv/):** Devbox can integrate with
  [direnv](https://direnv.net/) to automatically activate your shell and packages when you navigate
  to your project.
* **[Devbox for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=jetpack-io.devbox):**
  Install our VS Code extension to speed up common Devbox workflows or to use Devbox in a
  devcontainer.

### Boost your dev environment with Jetify Cloud[​](#boost-your-dev-environment-with-jetify-cloud "Direct link to Boost your dev environment with Jetify Cloud")

* **[Jetify Secrets](/docs/cloud/secrets/):** Securely store and access your secrets and environment
  variables in your Devbox projects.
* **[Jetify Cache](/docs/cloud/cache/):** Share and cache packages across all your Devbox projects
  and environments.
* **[Jetify Prebuilt Cache](/docs/cloud/cache/prebuilt-cache/):** Use the Jetify Public Cache to
  speed up your Devbox builds and share packages with the community.

### Get Involved[​](#get-involved "Direct link to Get Involved")

* **[Join our Discord Community](https://discord.gg/jetify):** Chat with the development team and
  our growing community of Devbox users.
* **[Visit us on Github](https://github.com/jetify-com/devbox):** File issues and provide feedback,
  or even open a PR to contribute to Devbox or our Docs.

[Edit this page](https://github.com/jetify-com/devbox/tree/main/docs/app/docs/quickstart.mdx)


# Welcome to Jetify Docs
Source: https://www.jetify.com/docs/docs/index

Find all the guides and resources you need to get started with Jetify's AI agents and developer tools

## What We Do

Jetify builds AI agents and developer tools that automate the tedious parts of software development.
Our flagship product, **Testpilot**, is an AI QA engineer that writes and runs tests for you. We
also offer complementary tools for reproducible environments, package discovery, and cloud
development.

## Explore by Product

<CardGroup cols={2}>
  <Card title="Testpilot" icon="rocket" href="/docs/testpilot/">
    **Your AI QA Engineer**

    AI agent that writes and runs tests for you. No coding required - just describe what you want to
    test in plain English.
  </Card>

  <Card title="Devbox" icon="box" href="/docs/devbox/">
    **Reproducible Development Environments**

    Create isolated development environments that work the same for everyone on your team. No more
    "works on my machine" problems.
  </Card>

  <Card title="NixHub API" icon="gear" href="/docs/nixhub/">
    **Nix Package Discovery**

    Search and find Nix packages easily. Free API to discover over 100,000 packages and their versions.
  </Card>

  <Card title="Jetify Cloud" icon="cloud" href="/docs/cloud/">
    **Cloud Development Environments**

    Cloud tools for faster development. Includes package caching and secure secrets management for your
    team.

    <Info>
      Alpha release
    </Info>
  </Card>
</CardGroup>

## Support & Community

Need help or want to connect with other developers using Jetify tools?

* **Get Help**: Visit our [support portal](https://help.jetify.com)
* **Join Discord**: Connect with the community on [our Discord server](https://discord.gg/jetify)
* **Contact Sales**: Reach out at [sales@jetify.com](mailto:sales@jetify.com)


# Get a Package
Source: https://www.jetify.com/docs/docs/nixhub/get-a-package/index



```
GET
/pkg
```

Get information about a specific package in Nixpkgs. This endpoint returns a JSON object that
contains information about the package, including a list of releases, platforms, and outputs. You
should use this endpoint if you know the name of the package you want to look up. If you need to
search for packages, use `/v2/search`. If you only need the latest version of a package, use
`/v2/resolve`.

## Request[​](#request "Direct link to Request")

<Accordion title="Query Parameters">
  * **name** stringrequired

    The name of the package you want to look up. Must be a valid Nixpkgs package name.
</Accordion>

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404

Ok

* application/json

* Schema

* Example (from schema)

<Accordion title="Response Schema">
  - **name**string

    The name of the package in Nixhub/Devbox

    **summary**string

    A short description of the package

    **homepage\_url**string

    The URL to the package's project homepage

    **license**string

    The software license of the package

    A list of Releases for the package.

    Array \[

  - **version**string

    The version string of the release. This string, combined with a package name, points to a specific
    version of a package

    **last\_updated**string

    The last time this release was updated in Nixpkg.

    A list of platforms this release is available on.

    Array \[

  - **arch**string

    The chip architecture of the platform. This will be one of `arm64` or `x86-64`.

    **os**string

    The operating system of the platform. This will be one of `macOS` or `Linux`.

    **systems**string

    The full Nix compatible name of the system. This will be one of `aarch64-darwin`, `aarch64-linux`,
    `x86_64-darwin`, or `x86_64-linux`.

    **attribute\_path**string

    The attribute path to the package in the Nixpkgs. This can be used to install the package with Nix
    or Devbox.

    **commit\_hash**string

    The hash of the Nixpkgs commit that this package was last updated in.

    **date**string

    The date this package was last updated in Nixpkgs.

    A list of Outputs (e.g., `out`, `lib`, `dev`) that are available for the package on this platform.

    Array \[

  - **name**string

    The name of the output (e.g., `out`, `lib`, `dev`)

    **path**string

    The unique path to the output in the Nix store.

    **default**boolean

    Whether this output is the default output for the package

    **nar**string

    The path to the packages NAR (Nix Archive) file. This file contains the package's build artifacts.

    ]

  - ]

  - **platforms\_summary**string

    A summary string that represents the platforms the release can be installed on.

    **outputs\_summary**string

    A summary string of the outputs (e.g., `out`, `lib`, `dev`) that are available for the release

    ]
</Accordion>

```
{  "name": "string",  "summary": "string",  "homepage_url": "string",  "license": "string",  "releases": [    {      "version": "string",      "last_updated": "string",      "platforms": [        {          "arch": "string",          "os": "string",          "systems": "string",          "attribute_path": "string",          "commit_hash": "string",          "date": "string",          "outputs": [            {              "name": "string",              "path": "string",              "default": true,              "nar": "string"            }          ]        }      ],      "platforms_summary": "string",      "outputs_summary": "string"    }  ]}
```

Bad Request: empty package name (set a ?name=\&ltpkg\&gt query parameter)

Not Found


# Using the Nixhub API
Source: https://www.jetify.com/docs/docs/nixhub/index

Version: 2.0.0

The [**Nixhub**](https://www.nixhub.io) API lets you search over 1 million package versions for over
100,000 Nix packages. You can use the Nixhub API to search for packages, resolve historic versions,
and then install them using Devbox or Nix. Nixhub is designed to be simple and easy to use, and is
free to use for personal use.

Nixhub is a RESTful API that uses standard HTTP methods and status codes. Parameters are passed to
the API as query parameters, and the API returns JSON responses. The current version does not make
use of pagination, though this may be added in the future.

The API is available for free for personal use, subject to rate limiting. If you need a higher rate
limit or wish to use Devbox for a commercial project, you can
[**request access to our paid tier**](https://form.typeform.com/to/hueeLe9S).

### Endpoints[​](#endpoints "Direct link to Endpoints")

Nixhub exposes the following endpoints for searching and resolving packages:

* [`v2/search`](/docs/nixhub/search-packages/) - Search for packages by name
* [`v2/pkg`](/docs/nixhub/get-a-package/) - Get details and version history for a specific package
* [`v2/resolve`](/docs/nixhub/resolve-a-package-version/) - Resolve a package name and version to a
  nixpkgs commit and attribute path.

### Rate Limits[​](#rate-limits "Direct link to Rate Limits")

In order to prevent abuse, personal use of the API is subject to rate limits. API Rate limiting
works as follows:

1. A given IP address starts with a pool of 1000 requests
2. Each request decrements the pool by 1
3. The pool is replenished at a rate of 5 requests per minute

If the pool is empty, the API will return a `429 Too Many Requests` status code.

<Check>
  If you have a use case that requires a higher rate limit or would like to use the API for
  commercial purposes, please fill out [**this form**](https://form.typeform.com/to/hueeLe9S) to
  request access.
</Check>

### Nixhub for Enterprise[​](#nixhub-for-enterprise "Direct link to Nixhub for Enterprise")

Nixhub provides an index of publicly available packages from the
[Nixpkgs](https://github.com/nixos/nixpkgs) repository. If you're interested in using Nixhub to
index and install private packages or Flakes for your team, we'd love to chat with you. You can
request a meeting [**with our team**](https://calendly.com/d/cprm-dq6-y9y/nixhub-enterprise-chat)

### Versioning[​](#versioning "Direct link to Versioning")

The API is versioned using a `v2` prefix in the URL. All `v2` endpoints are considered stable and
will not change in a backwards-incompatible way. Breaking changes will be introduced in a new
version of the API, with a new version prefix.

## API Reference[​](#api-reference "Direct link to API Reference")

* [Search Packages](/docs/nixhub/search-packages/) - Search for packages by name
* [Get Package Details](/docs/nixhub/get-a-package/) - Get details and version history for a
  specific package
* [Resolve Package](/docs/nixhub/resolve-a-package-version/) - Resolve the latest available package
  for a given name and version string


# Resolve a Package Version
Source: https://www.jetify.com/docs/docs/nixhub/resolve-a-package-version/index



```
GET
/resolve
```

Resolve a Package Version. This endpoint resolves a package name + version string to the latest
version of the package available in the Nixpkg repository. The response includes the Flake
installable information for the package on each supported platform.

## Request[​](#request "Direct link to Request")

<Accordion title="Query Parameters">
  * **name** stringrequired

    The name of the package you want to resolve. Must be a valid Nixpkgs package name.

    **version** stringrequired

    The version string of the package you want to resolve.
</Accordion>

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404

OK

* application/json

* Schema

* Example (from schema)

<Accordion title="Response Schema">
  - **name**string

    The name of the package that was resolved.

    **version**string

    The latest version the package that matches the version string provided in the request.

    **summary**string

    A short description of the package

    A list of systems that the package can be installed on, along with the details of the Package on that system.

    The information needed to install this package as a flake reference.

    The full Nix reference to the flake that contains this package.

    **type**string

    The type of flake reference. Usually this will be `github`.

    **owner**string

    The owner of the repository that contains the flake. Usually `NixOS`.

    **repo**string

    the repository that contains the flake. Usually `nixpkgs`

    **rev**string

    The Git revision of the flake. This is usually a commit hash.

    **attr\_path**string

    The attribute path to the package in the flake. This can be used to install the package with Nix or Devbox.

    **last\_updated**string

    The last time this package was updated in the Nixpkgs repo

    A list of Outputs (e.g., `out`, `lib`, `dev`) that are available for the package on this platform.

    Array \[

  - **name**string

    The name of the output (e.g., `out`, `lib`, `dev`)

    **path**string

    The unique path to the output in the Nix store.

    **default**boolean

    Whether this output is the default output for the package

    **nar**string

    The path to the packages NAR (Nix Archive) file. This file contains the package's build artifacts.

    ]

  - The information needed to install this package as a flake reference.

    The full Nix reference to the flake that contains this package.

    **type**string

    The type of flake reference. Usually this will be `github`.

    **owner**string

    The owner of the repository that contains the flake. Usually `NixOS`.

    **repo**string

    the repository that contains the flake. Usually `nixpkgs`

    **rev**string

    The Git revision of the flake. This is usually a commit hash.

    **attr\_path**string

    The attribute path to the package in the flake. This can be used to install the package with Nix
    or Devbox.

    **last\_updated**string

    The last time this package was updated in the Nixpkgs repo

    A list of Outputs (e.g., `out`, `lib`, `dev`) that are available for the package on this platform.

    Array \[

  - **name**string

    The name of the output (e.g., `out`, `lib`, `dev`)

    **path**string

    The unique path to the output in the Nix store.

    **default**boolean

    Whether this output is the default output for the package

    **nar**string

    The path to the packages NAR (Nix Archive) file. This file contains the package's build artifacts.

    ]

  - The information needed to install this package as a flake reference.

    The full Nix reference to the flake that contains this package.

    **type**string

    The type of flake reference. Usually this will be `github`.

    **owner**string

    The owner of the repository that contains the flake. Usually `NixOS`.

    **repo**string

    the repository that contains the flake. Usually `nixpkgs`

    **rev**string

    The Git revision of the flake. This is usually a commit hash.

    **attr\_path**string

    The attribute path to the package in the flake. This can be used to install the package with Nix
    or Devbox.

    **last\_updated**string

    The last time this package was updated in the Nixpkgs repo

    A list of Outputs (e.g., `out`, `lib`, `dev`) that are available for the package on this platform.

    Array \[

  - **name**string

    The name of the output (e.g., `out`, `lib`, `dev`)

    **path**string

    The unique path to the output in the Nix store.

    **default**boolean

    Whether this output is the default output for the package

    **nar**string

    The path to the packages NAR (Nix Archive) file. This file contains the package's build artifacts.

    ]

  - The information needed to install this package as a flake reference.

    The full Nix reference to the flake that contains this package.

    **type**string

    The type of flake reference. Usually this will be `github`.

    **owner**string

    The owner of the repository that contains the flake. Usually `NixOS`.

    **repo**string

    the repository that contains the flake. Usually `nixpkgs`

    **rev**string

    The Git revision of the flake. This is usually a commit hash.

    **attr\_path**string

    The attribute path to the package in the flake. This can be used to install the package with Nix
    or Devbox.

    **last\_updated**string

    The last time this package was updated in the Nixpkgs repo

    A list of Outputs (e.g., `out`, `lib`, `dev`) that are available for the package on this platform.

    Array \[

  - **name**string

    The name of the output (e.g., `out`, `lib`, `dev`)

    **path**string

    The unique path to the output in the Nix store.

    **default**boolean

    Whether this output is the default output for the package

    **nar**string

    The path to the packages NAR (Nix Archive) file. This file contains the package's build artifacts.

    ]
</Accordion>

```json  theme={null}
{
  "name": "string",
  "version": "string",
  "summary": "string",
  "systems": {
    "aarch64-darwin": {
      "flake_installable": {
        "ref": {
          "type": "string",
          "owner": "string",
          "repo": "string",
          "rev": "string"
        },
        "attr_path": "string"
      },
      "last_updated": "string",
      "outputs": [
        {
          "name": "string",
          "path": "string",
          "default": true,
          "nar": "string"
        }
      ]
    },
    "aarch64-linux": {
      "flake_installable": {
        "ref": {
          "type": "string",
          "owner": "string",
          "repo": "string",
          "rev": "string"
        },
        "attr_path": "string"
      },
      "last_updated": "string",
      "outputs": [
        {
          "name": "string",
          "path": "string",
          "default": true,
          "nar": "string"
        }
      ]
    },
    "x86_64-darwin": {
      "flake_installable": {
        "ref": {
          "type": "string",
          "owner": "string",
          "repo": "string",
          "rev": "string"
        },
        "attr_path": "string"
      },
      "last_updated": "string",
      "outputs": [
        {
          "name": "string",
          "path": "string",
          "default": true,
          "nar": "string"
        }
      ]
    },
    "x86_64-linux": {
      "flake_installable": {
        "ref": {
          "type": "string",
          "owner": "string",
          "repo": "string",
          "rev": "string"
        },
        "attr_path": "string"
      },
      "last_updated": "string",
      "outputs": [
        {
          "name": "string",
          "path": "string",
          "default": true,
          "nar": "string"
        }
      ]
    }
  }
}
```

400 Bad Request: empty name (set a ?name=\<value> query parameter)

Not Found


# Search Packages
Source: https://www.jetify.com/docs/docs/nixhub/search-packages/index



```
GET
/search
```

Search Packages. This endpoint allows you to search for packages in the Nixpkgs repository using a
search query. The response includes a list of package names along with their description. To get
available versions and installables for a package, you can use this name with the `/v2/pkg`
endpoint.

## Request[​](#request "Direct link to Request")

<Accordion title="Query Parameters">
  * **q** stringrequired

    Search query.
</Accordion>

## Responses[​](#responses "Direct link to Responses")

* 200
* 400
* 404

OK

* application/json

* Schema

* Example (from schema)

<Accordion title="Response Schema">
  - **query**string

    The search query sent to the `/v2/search` endpoint

    **total\_results**integer

    The total number of results for the search query

    A list of SearchResults that match the query. This array will be empty if no results were found.

    Array \[

  - **name**string

    The name of the package that matched the search query

    **summary**string

    A short description of the package

    **last\_updated**string

    The last time this package was updated in the Nixpkgs repo

    ]
</Accordion>

```
{  "query": "string",  "total_results": 0,  "results": [    {      "name": "string",      "summary": "string",      "last_updated": "string"    }  ]}
```

Bad Request: empty search query (set a ?q=\<query> query parameter)

Not Found


# Advanced Testpilot Features
Source: https://www.jetify.com/docs/docs/testpilot/advanced/index

Advanced features for power users. Explore AI test generation, MCP integration, and specialized testing techniques.

This section covers advanced Testpilot features designed for specific use cases and power users. These features are optional but powerful tools that can enhance your testing workflow.

<Note>
  Before exploring advanced features, you should be comfortable with the basics covered in [Getting Started](/docs/testpilot/getting-started). These features are designed for users who have already run tests successfully and want to extend Testpilot's capabilities.
</Note>

## What You'll Find Here

Advanced features include AI-powered test generation and extensibility through the Model Context Protocol. These capabilities are designed for specific workflows and may not be necessary for all users.

<CardGroup cols={2}>
  <Card title="AI Test Generation" icon="sparkles" href="/docs/testpilot/ai-test-generation">
    Automatically generate test plans from natural language descriptions.
  </Card>

  <Card title="Model Context Protocol (MCP)" icon="link" href="/docs/testpilot/model-context-protocol">
    Extend Testpilot's capabilities with MCP server integrations.
  </Card>
</CardGroup>

## When to Use Advanced Features

Consider using advanced features when:

* **AI Test Generation**: You want to quickly create test plans from descriptions or need inspiration for test scenarios
* **MCP Integration**: You need to integrate with custom APIs, internal tools, or specialized testing infrastructure

These features complement the core testing workflow but are not required for effective testing with Testpilot.

## See Also

* [Getting Started](/docs/testpilot/getting-started) - Learn the basics first
* [Guides](/docs/testpilot/guides) - Practical solutions for common testing scenarios
* [CLI Reference](/docs/testpilot/reference/cli) - Command-line options for advanced features


# AI Test Generation
Source: https://www.jetify.com/docs/docs/testpilot/ai-test-generation

Generate comprehensive test plans automatically from natural language prompts. Create tests faster and discover edge cases with AI assistance.

<Info>
  This feature is experimental. It may generate erroneous or incorrect tests, and you should review
  any tests before executing or checking them in.
</Info>

## Why Generate Tests?[​](#why-generate-tests "Direct link to Why Generate Tests?")

Manually writing test cases can be time-consuming and may miss important scenarios. Testpilot's test
generation capability helps by:

* Creating test plans much faster than manual authoring
* Discovering edge cases you might not have considered
* Providing comprehensive coverage of your application
* Standardizing test structure and approach
* Reducing the expertise required to create quality tests

## Generating Your First Test[​](#generating-your-first-test "Direct link to Generating Your First Test")

To generate tests, use the `testpilot generate` command followed by a prompt that describes what you
want to test:

```bash  theme={null}
testpilot generate "Visit nixhub.com and search for 'go'. Verify that version 1.24 is shown"
```

This command:

1. Processes your prompt using AI
2. Generates a comprehensive test plan in YAML format
3. Saves the test plan to a file in the current directory

You should see something like the following output in a `generated.pilot.yaml` file:

```yaml  theme={null}
schema_version: v1.0.0
name: null
cases:
  - id: testcase_01jy56bqacey0vdkt9qtje76q6
    name: Verify version 1.24 of 'go' on nixhub.com
    description: Users need to find the package 'go' on nixhub.com and ensure that version 1.24 is listed among the search results.
    steps:
      - Enter 'go' into the search bar.
      - Look for search results related to 'go'.
      - Verify that version 1.24 of 'go' is displayed in the search results.
    url: https://nixhub.com
    context:
      - text: Visit nixhub.com and search for 'go'. Verify that version 1.24 is shown
```

For best results, include:

* The URL of the application you want to test
* Specific features or flows you want to test
* Any edge cases or scenarios to include

## Adding Context for Better Tests[​](#adding-context-for-better-tests "Direct link to Adding Context for Better Tests")

You can provide additional context to improve test generation quality using the `--context` flag:

```bash  theme={null}
testpilot generate "Test the checkout process" --context ./api-docs.md --context ./checkout-flow.txt
```

The context files can include:

* API documentation
* User flow descriptions
* Existing test examples
* Application requirements
* Known edge cases

You can specify multiple context files to provide more comprehensive information.

## Customizing Output Location[​](#customizing-output-location "Direct link to Customizing Output Location")

By default, generated tests are saved to the current directory. You can specify a different output
directory:

```bash  theme={null}
testpilot generate "Test search functionality" --outdir ./tests/search
```

## Example: Generated Test Plan[​](#example-generated-test-plan "Direct link to Example: Generated Test Plan")

Here's an example of a test plan generated from a prompt:

```yaml  theme={null}
name: "Login Functionality Test Suite"
context:
  - text: "This test suite verifies the login functionality of the example.com website"
  - text: "The login page has fields for username and password, plus a 'Remember me' checkbox"
cases:
  - id: "login-success-001"
    name: "Successful Login"
    description: "Verify that users can successfully log in with valid credentials"
    url: "https://example.com/login"
    steps:
      - "Navigate to the login page"
      - "Verify the login form is displayed with username and password fields"
      - "Enter a valid username in the username field"
      - "Enter a valid password in the password field"
      - "Click the 'Log in' button"
      - "Verify successful login by checking for the user dashboard"
      - "Verify the username is displayed in the header area"
  - id: "login-failure-001"
    name: "Failed Login - Invalid Password"
    description: "Verify appropriate error message when login fails due to invalid password"
    url: "https://example.com/login"
    steps:
      - "Navigate to the login page"
      - "Enter a valid username in the username field"
      - "Enter an invalid password in the password field"
      - "Click the 'Log in' button"
      - "Verify an error message is displayed"
      - "Verify the user remains on the login page"
  - id: "login-remember-me-001"
    name: "Remember Me Functionality"
    description: "Verify the 'Remember me' option maintains login session across browser restarts"
    url: "https://example.com/login"
    steps:
      - "Navigate to the login page"
      - "Enter valid login credentials"
      - "Check the 'Remember me' checkbox"
      - "Click the 'Log in' button"
      - "Verify successful login"
      - "Close the browser and reopen it"
      - "Navigate to https://example.com"
      - "Verify the user is still logged in without re-entering credentials"
```

## Modifying Generated Tests[​](#modifying-generated-tests "Direct link to Modifying Generated Tests")

Testpilot generates a starting point for your tests, but you should:

1. **Review the tests**: Carefully review all generated test cases
2. **Edit as needed**: Adjust steps to match your application's actual behavior
3. **Add specificity**: Make vague steps more specific when necessary
4. **Add assertions**: Ensure there are clear verification steps
5. **Remove irrelevant tests**: Delete test cases that don't apply to your application

## Running Generated Tests[​](#running-generated-tests "Direct link to Running Generated Tests")

After reviewing and adjusting the generated tests, run them with:

```bash  theme={null}
testpilot test path/to/generated-test.pilot.yaml
```

## Effective Test Generation Prompts[​](#effective-test-generation-prompts "Direct link to Effective Test Generation Prompts")

For the best results, create detailed, specific prompts:

**Basic Prompt:**

```markdown  theme={null}
Test the login functionality at https://example.com
```

**Better Prompt:**

```markdown  theme={null}
Test the login functionality at https://example.com including:
- Successful login with valid credentials
- Failed login with incorrect password
- Failed login with non-existent user
- Password reset flow
- Remember me functionality
- Account lockout after multiple failed attempts
```

## Best Practices for Generated Tests[​](#best-practices-for-generated-tests "Direct link to Best Practices for Generated Tests")

1. **Be specific in your prompts**: The more detail you provide, the better the generated tests
2. **Include application URLs**: Always specify the URL to test in your prompt
3. **Provide context files**: Add relevant documentation to improve generation quality
4. **Review before running**: Always review generated tests before execution
5. **Customize as needed**: Treat generated tests as a starting point, not the final product
6. **Version control**: Save and version your refined test files

By using Testpilot's test generation capabilities, you can quickly create a solid foundation for
your test suite, saving time while ensuring good coverage of your application functionality.


# Testpilot Best Practices
Source: https://www.jetify.com/docs/docs/testpilot/best-practices/index

Best practices for writing effective tests. Learn optimization techniques, testing philosophy, and maintainability patterns.

Writing high-quality tests ensures your test suite is reliable, maintainable, and provides meaningful feedback. This section shares best practices and patterns for getting the most out of Testpilot.

## Testpilot's Testing Philosophy

Testpilot uses AI to test applications visually, the way humans do. This means you should write tests like you would describe actions to a person:

* Describe what you want to accomplish, not how to find specific elements
* Start with general instructions and add specificity only when needed
* Let Testpilot handle the visual navigation and element identification

This approach creates tests that are more resilient to UI changes and easier to maintain.

## What You'll Find Here

This section provides guidance on writing effective tests, optimizing test performance, and maintaining your test suite over time.

<CardGroup cols={2}>
  <Card title="How to Write Effective Tests" icon="check-circle" href="/docs/testpilot/best-practices/write-effective-tests">
    Tips and patterns for creating reliable, maintainable tests.
  </Card>
</CardGroup>

## Key Principles

* **Write for humans first**: Test steps should be readable and understandable
* **Be flexible**: General instructions give Testpilot more flexibility to adapt to UI changes
* **Consolidate steps**: Fewer steps mean faster tests and clearer intent
* **Use context wisely**: Provide additional information only when necessary

## See Also

* [Getting Started](/docs/testpilot/getting-started) - Learn the basics of writing tests
* [Guides](/docs/testpilot/guides) - Practical examples of common testing scenarios
* [Pilotfile Reference](/docs/testpilot/pilotfile-reference) - Complete reference for test file format


# How to Write Effective Tests
Source: https://www.jetify.com/docs/docs/testpilot/best-practices/write-effective-tests

Learn tips and patterns for creating reliable, maintainable tests. Optimize test speed, use context effectively, and improve accuracy.

## General Tips[​](#general-tips "Direct link to General Tips")

* When writing tests, start by providing general steps, and only get more specific or add context as
  needed. General steps give Testpilot more flexibility, and can lead to faster tests.
* If you need to check that something is present on the page before proceeding, start your step with
  "Verify" or "Check". This tells Testpilot that you want to make an assertion about the page's
  state.

## Speeding up Tests[​](#speeding-up-tests "Direct link to Speeding up Tests")

* Testpilot automatically handles launching the app or website provided via the `url` or
  `platform_config` fields in the test. You don't need to add steps like "Wait for the application
  to load," "Launch the app," or "Verify that the app launches successfully."

* Consolidate steps wherever possible. Tests with fewer steps run faster because Testpilot needs to
  capture an initial screenshot for each step and generate results after the test completes.

* Avoid adding "Verify" or "Check" type assertion steps when you can use an action instead. You
  don't need to verify that a text box is present if the next step is to click the text box.

* For example — you can rewrite the following test steps:

  ```yaml  theme={null}
  - Verify that you can see the login form
  - Click the login form
  - Verify that the login form is active
  - Enter your login information
  ```

  into:

  ```yaml  theme={null}
  - Enter your login information in the form
  ```

## Using Context[​](#using-context "Direct link to Using Context")

* Use context fields to provide important information that Testpilot needs for your test case.
  Examples include:
  * **Describing less common UI features or gestures**. For example: "If you see a Welcome Screen
    pop-up in the flow, click the 'Not Interested' button to dismiss it."
  * **Providing user information for Testpilot to model**. For example: "You are a new homeowner
    with a \$200,000 mortgage in Cincinnati, Ohio" helps Testpilot fill out the right details in an
    application form.
  * **Giving Testpilot permission for certain actions**. For example: "You should grant location
    permissions whenever prompted" or "You are authorized to accept terms of service and submit loan
    applications."

* If you need to provide context that applies to multiple test cases, consider using the `context`
  field at the test file level. This way, you can avoid repeating the same context in each test
  case. If the context is only relevant to a single test case, you can use the `context` field at
  the test case level.

* Testpilot responds better to concise, direct context blocks. Instead of writing long paragraphs,
  break important context into separate lines and remove unnecessary text.

* Avoid using context to provide instructions that Testpilot can infer from the steps. For example,
  you don't need to say "You are a user" or "You are testing the application" because Testpilot
  already knows this.


# Testpilot Changelog
Source: https://www.jetify.com/docs/docs/testpilot/changelog/index

Latest Testpilot updates, features, and bug fixes. Track version history and see what's new in each release.

🚀 Features & Improvements

* **Extra Cookie Support**
  * Added ability to set custom cookie data during tests using the `TESTPILOT_EXTRA_COOKIE_DATA`
    environment variable

* **Experimental Action Cache**
  * Introduced an experimental action cache feature to store and reuse actions based on element IDs,
    improving test performance and reliability
  * Users will need to be signed in to their Jetify Cloud account with `testpilot auth login` to
    utilize this feature, and can update the cache using the `--upload-report` flag during test
  * This feature can be enabled with the `FEATURE_FLAG_USE_CACHE_FOR_FAST_EXECUTION` environment
    variable.

🐛 Bug Fixes

* **Screenshot Handling:**
  * Fixed nil-pointer error when checking click elements prior to taking screenshots
  * Fixed mobile viewport screenshot issues affecting test accuracy
  * Improved screenshot timing for click actions on certain elements

* **Performance Optimizations:**
  * Significantly improved cache hit rates (from \~20% to 50% in some cases) through enhanced
    element selection logic
  * Reduced image I/O operations to improve performance
  * Prevented continuous growth of screenshots in cached test reports

* **Element Selection:**
  * Enhanced element filtering to prioritize interactive elements, navigational elements, and
    elements with test identifiers
  * Improved selector preference logic, prioritizing aria-label attributes over CSS class selectors
  * Fixed element selection for dropdown/select actions to use values instead of indices for better
    cache reliability

* **Concurrency & Stability:**
  * Fixed race conditions with report protocol calls by adding proper locking
  * Fixed terminal output handling in concurrency mode for multi-viewport test cases
  * Fixed nil-pointer errors in LLM response handling

* **Login & Authentication:**
  * Improved login test reliability by using API service-hosted login pages
  * Enhanced login password redaction in test reports and JUnit reports for better security

* **Loading Timeouts**
  * Set Playwright page navigation timeout to 10 seconds for more reliable page loading
  * Testpilot will no longer fail a test if a page takes longer than 10 seconds to load, but will
    attempt to continue with the test.


# Evaluating Testpilot Runs
Source: https://www.jetify.com/docs/docs/testpilot/evaluation/analyze-json-report-evaluations

Calculate key metrics from TestPilot JSON reports: latency, pass/fail rates, and cache performance across test runs.

## Overview

In addition to HTML and JUnit reports, Testpilot reports detailed metrics about test executions in a `reports.json` file that is included in the output directory of the test. This report can be uploaded to AI observability or evaluation platforms to understand how your tests are performing over time, and to identify bottlenecks and flaky steps in your tests.

This guide explains how to extract and calculate key metrics from TestPilot JSON reports for evaluation and monitoring purposes:

1. **Latency per step and per test** - Measure execution time performance
2. **Pass/fail per step and per test** - Calculate success rates
3. **Cache performance analysis** - Analyze cache effectiveness and optimization opportunities

These metrics help identify performance regressions, flaky tests, and cache optimization opportunities across multiple test runs.

## Data Sources

TestPilot generates a `report.json` file for each test in your test run in the `testpilot-out/.internal/<report-id>/<test-id>/results.json` directory. You can view a detailed reference of the report structure [here](./testpilot-json-report-reference).

## 1. Latency Metrics

### Understanding Latency Fields

TestPilot provides timing data at multiple levels to help you understand where time is being spent during test execution:

* **Test-level timing**: The `duration` field on each `Test` object represents the total wall-clock time from test start to completion
* **Step-level timing**: Each `Step` has its own `duration` field showing how long that individual step took
* **Action-level timing**: Individual `Action` objects within steps also have `duration` fields for granular analysis

The duration format uses strings like "2.5 s" or "90.2 s" - always in seconds with the "s" suffix. Parse these into numeric values to enable mathematical operations like averaging, percentile calculations, and trend analysis.

### Per-Test Latency Analysis

Test-level latency provides the most important metric for overall user experience - the total time from test start to completion. This end-to-end measurement is crucial for:

* **SLA monitoring**: Ensuring tests complete within acceptable time limits
* **Performance trending**: Tracking whether test execution is getting faster or slower over time
* **Resource planning**: Understanding typical execution times for capacity planning

Key fields for analyzing Per test latency include:

* **Test.id**: Stable Identifier for analyzing your test across runs
* **Test.duration**: Wall time for how long the test took to run
* **Test.startTime**: Useful for organizing your tests chronologically
* **Test.profilingMetrics**: Splits test time into LLM Duration, Tool Duration, and Attempts, which can help you understand what is driving the test's overall duration.

### Per-Step Latency Analysis

Step-level latency analysis helps identify bottlenecks in test execution by examining the `duration` field on each `Step` object. This is particularly useful for:

* **Bottleneck identification**: Finding which types of operations (navigation, form filling, verification) take the longest
* **Optimization targeting**: Prioritizing which steps to optimize for maximum performance impact
* **Regression detection**: Monitoring whether specific step types are getting slower over time

Extract the duration from each step and track it alongside the step title and status to build comprehensive performance profiles.

Key fields for analyzing Per-Step latency include:

* Step.title: The actual wording of the step provided to the LLM. You can use this, or the step's index for analysis across tests.
* Step.duration: Wall time for how long the step took
* Step.profilingMetrics: Shows the breakdown of duration by attempts, LLM Duration, and Tool Duration
* Step.executionMode: Shows how the step was executed (cache, agent, script, etc.) - see [Enum Reference](#enum-reference)
* Step.actions: The actual actions Taken by Testpilot, which can give you a granular understanding of what occurred during the step.
* Step.cacheStatus: Shows whether the step successfully used the Action cache, or had to fall back. See [Enum Reference](#enum-reference)
* Step.explanation: The LLM's interpretation of how the step ended.

Some things to evaluate when analyzing steps include:

* Do the profiling metrics indicate frequent retries of the step, or issues with any of the tool calls you are making?
* Does cache status consistently suggest an issue with caching capability? What reasons are preventing the cache from hitting on the action.
* Do you see a large number of waits, or repetitive actions in the step?

## 2. Pass/Fail Metrics

### Understanding Status Fields

TestPilot uses numeric status codes to indicate the outcome of tests and steps. The `status` field appears on both `Test` and `Step` objects. See the [Status enum table](#status) for complete values and meanings.

### Per-Step Pass/Fail Analysis

Step-level analysis helps identify which specific operations are most prone to failure. This is valuable for:

* **Failure pattern identification**: Understanding which types of steps fail most frequently
* **Root cause analysis**: Distinguishing between action failures and verification failures
* **Test stability assessment**: Identifying steps that contribute to overall test flakiness

Pay attention to the `stepType` field as verification steps failing might indicate different issues than action steps failing. See the [StepType enum table](#steptype) for complete values.

**Key aggregation strategies:**

* **Binary classification**: Treat STATUS\_SUCCEEDED as "pass" and all others as "fail" for most analyses
* **Step type segmentation**: Analyze action steps vs verification steps separately
* **Failure categorization**: Use the `failureReasonCategory` field to group similar failure types

### Per-Test Pass/Fail Analysis

Test-level pass/fail rates are the primary metric for overall test suite health. The test `status` field represents the final outcome after all steps have been attempted. A test is considered successful only if it reaches STATUS\_SUCCEEDED (2).

The `explanation` field often contains valuable context about why a test failed, which can be categorized for root cause analysis and automated triage.

### Pass/Fail Trend Analysis

Tracking pass/fail rates over time is essential for identifying flaky tests and overall test suite stability:

**Critical metrics to track:**

* **Overall pass rate**: Percentage of tests passing in recent runs
* **Test stability**: Individual tests with inconsistent results across runs
* **Flaky test identification**: Tests with pass rates between 20-80% indicating intermittent issues
* **Failure clustering**: Whether failures concentrate around specific time periods or code changes

**Analysis techniques:**

* **Stability scoring**: Calculate pass rates over rolling windows to identify consistently failing vs intermittent tests
* **Trend detection**: Monitor whether test suite health is improving or degrading over time
* **Outlier identification**: Flag tests that deviate significantly from expected pass rates

## 3. Cache Performance Analysis

### Understanding Cache Fields

TestPilot's caching system speeds up test execution by reusing previous step results when conditions are similar. Understanding cache performance helps optimize test execution time and identify optimization opportunities.

**Key fields for cache analysis:**

* **Step.cacheStatus**: Indicates what happened with cache for this step (hit, miss, or unused with reason)
* **Step.executionMode**: Shows how the step was actually executed (cache, agent, script, etc.)
* **Test.cacheSourceId**: When present, indicates this test used another test as a cache source

### Cache Rate Calculation

The most effective cache rate calculation focuses on **non-assertion steps** since verification steps typically cannot be cached. The analysis should:

* **Count cache utilization**: Steps executed with `EXECUTION_MODE_CACHE` (2) or `EXECUTION_MODE_CACHE_FALLBACK_TO_CUA` (3)
* **Exclude assertion steps**: Filter out steps identified as assertions/verifications since they rarely can be cached
* **Calculate hit rate**: Cached steps divided by total non-assertion steps

**Assertion step identification:**

* Step titles beginning with "verify," "assert," or "expect" (case-insensitive).
* Steps with `stepType` of `STEP_TYPE_VERIFICATION` (3).

### Cache Error Rate Analysis

Cache error rate tracks situations where cache was attempted but failed, requiring fallback to live agent execution. This metric helps identify:

* **Cache reliability issues**: How often cache attempts fail
* **Environmental factors**: Whether cache failures correlate with specific conditions
* **Cache optimization opportunities**: Which scenarios need better cache handling

Calculate as the percentage of steps with execution mode `EXECUTION_MODE_CACHE_FALLBACK_TO_CUA` (3) across all steps.

### Cache Status Analysis

Beyond simple hit rates, analyze the specific reasons cache wasn't used:

See the [CacheStatus enum table](#cachestatus) for complete cache status values and their meanings, including detailed unused reasons and optimization strategies.

### Cache Performance Trends

Track cache performance over time to understand optimization effectiveness:

**Key trend indicators:**

* **Declining hit rates**: May indicate tests becoming more dynamic or environmental instability
* **Consistent unused reasons**: Suggest systematic issues addressable through test design changes
* **Cache source stability**: Tests frequently serving as cache sources should be prioritized for stability
* **Performance correlation**: Relationship between cache hit rates and overall execution speed

## Field Selection Best Practices

### Essential Fields by Analysis Type

**Latency Analysis:**

* `Test.duration` and `Step.duration`: Core timing metrics
* `Test.id`: For grouping across runs
* `ProfilingMetrics.totalDuration`, `llmDuration`, `toolDuration`: For detailed breakdowns
* `Report.startTime`: For chronological ordering

**Pass/Fail Analysis:**

* `Test.status` and `Step.status`: Core success metrics (focus on value 2 = SUCCESS)
* `Test.explanation` and `Step.explanation`: Context for failures
* `Step.stepType`: To differentiate verification vs action failures
* `Step.failureReasonCategory`: For categorizing failure types

**Cache Analysis:**

* `Step.executionMode`: How step was executed (primary metric)
* `Step.cacheStatus`: Detailed cache behavior
* `Test.cacheSourceId`: Cache dependency relationships
* `Step.title`: For identifying assertion steps to exclude

## Enum Reference

TestPilot uses numeric enum values throughout the JSON reports. This section provides complete reference tables for all enum types used in evaluation and analysis.

### Status

The `status` field appears on both `Test` and `Step` objects to indicate execution outcomes:

| Number | Name                | Meaning                                       |
| ------ | ------------------- | --------------------------------------------- |
| 0      | STATUS\_UNSPECIFIED | Status is unknown or not set                  |
| 1      | STATUS\_PENDING     | Test or step is still in progress             |
| 2      | STATUS\_SUCCEEDED   | Completed successfully (passed)               |
| 3      | STATUS\_FAILED      | Completed with failure                        |
| 4      | STATUS\_INCOMPLETE  | Did not finish all steps (aborted or skipped) |

### ExecutionMode

The `executionMode` field indicates how each step was executed:

| Number | Name                                      | Meaning                                          |
| ------ | ----------------------------------------- | ------------------------------------------------ |
| 0      | EXECUTION\_MODE\_UNSPECIFIED              | Mode not specified                               |
| 1      | EXECUTION\_MODE\_CUA                      | Executed by Computer Use Agent (LLM-driven)      |
| 2      | EXECUTION\_MODE\_CACHE                    | Step executed from cache (no live LLM run)       |
| 3      | EXECUTION\_MODE\_CACHE\_FALLBACK\_TO\_CUA | Cache attempted but fell back to agent execution |
| 4      | EXECUTION\_MODE\_FALLBACK\_TO\_CUA        | Non-CUA execution failed, fell back to agent     |
| 5      | EXECUTION\_MODE\_NON\_CUA                 | Non-CUA mode (deterministic/scripted)            |
| 6      | EXECUTION\_MODE\_SCRIPT                   | Script mode execution                            |
| 7      | EXECUTION\_MODE\_FORM\_FILLER             | Form filler mode execution                       |

### CacheStatus

The `cacheStatus` field indicates what happened with cache for each step:

| Number | Name                                                     | Meaning                                                                                       |
| ------ | -------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 0      | CACHE\_STATUS\_UNSPECIFIED                               | Cache status not specified                                                                    |
| 1      | CACHE\_STATUS\_HIT                                       | Cache entry found and used - optimal performance                                              |
| 2      | CACHE\_STATUS\_MISS                                      | No suitable cache entry found - expected for first runs                                       |
| 3      | CACHE\_STATUS\_UNUSED\_IS\_RETRY                         | Cache ignored because step needed retry - may indicate flaky steps                            |
| 4      | CACHE\_STATUS\_UNUSED\_IS\_ASSERTION                     | Cache ignored for assertion-only step - expected behavior                                     |
| 5      | CACHE\_STATUS\_UNUSED\_NON\_CACHEABLE\_EXECUTION\_MODE   | Cache ignored due to non-cacheable execution mode                                             |
| 6      | CACHE\_STATUS\_UNUSED\_CONTAINS\_NON\_CACHEABLE\_ACTIONS | Cache ignored due to non-cacheable actions                                                    |
| 7      | CACHE\_STATUS\_UNUSED\_ELEMENT\_IS\_MISSING              | Cache ignored because required element missing - UI changes may have broken cache assumptions |
| 8      | CACHE\_STATUS\_UNUSED\_HAS\_TOOL\_CALLS                  | Cache ignored because step involved tool calls - dynamic behavior prevented caching           |
| 9      | CACHE\_STATUS\_UNUSED\_IS\_SCRIPT                        | Cache ignored for script-based step                                                           |

### StepType

The `stepType` field classifies the type of step being executed:

| Number | Name                        | Meaning                                      |
| ------ | --------------------------- | -------------------------------------------- |
| 0      | STEP\_TYPE\_UNSPECIFIED     | Step type not specified                      |
| 1      | STEP\_TYPE\_REGULAR\_ACTION | Regular user actions (click, type, navigate) |
| 2      | STEP\_TYPE\_FORM\_FILLING   | Data entry or form completion                |
| 3      | STEP\_TYPE\_VERIFICATION    | Assertion or verification of expected state  |

## Key Takeaways

1. **Duration parsing**: Always convert duration strings to numeric seconds for analysis
2. **Test identification**: Use `Test.id` for tracking across runs, not titles
3. **Cache calculation**: Exclude assertion steps for accurate cache hit rates
4. **Status interpretation**: Focus on STATUS\_SUCCEEDED (2) as the only true success state
5. **Trend analysis**: Use rolling averages and percentile calculations for meaningful insights
6. **Failure categorization**: Leverage explanation fields for automated failure triage


# TestPilot JSON Report Reference
Source: https://www.jetify.com/docs/docs/testpilot/evaluation/testpilot-json-report-reference

Complete reference for TestPilot's JSON report structure with schema, field descriptions, and enum tables.

## Overview

TestPilot generates JSON reports in two formats:

* **Aggregated Report**: Top-level report containing all tests from a run
* **Per-test Results**: Individual `results.json` files for each test

Both formats share the same core object structures and use `camelCase` field naming in JSON output.

## Complete JSON Schema

```json  theme={null}
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "TestPilot JSON Report",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "startTime": { "type": "string", "format": "date-time" },
    "duration": { "type": "string" },
    "platforms": { "type": "array", "items": { "type": "string" } },
    "statusSummary": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "count": { "type": "integer" },
          "status": { "type": "integer", "enum": [0, 1, 2, 3, 4] }
        },
        "required": ["count", "status"]
      }
    },
    "tests": { "type": "array", "items": { "$ref": "#/$defs/Test" } },
    "title": { "type": "string" },
    "orgId": { "type": "string" },
    "token": { "type": "string" },
    "ownerName": { "type": "string" },
    "isArchived": { "type": "boolean" }
  },
  "required": ["id", "startTime", "duration", "tests"],
  "$defs": {
    "Test": {
      "type": "object",
      "properties": {
        "id": { "type": "string" },
        "title": { "type": "string" },
        "status": { "type": "integer", "enum": [0, 1, 2, 3, 4] },
        "explanation": { "type": "string" },
        "videoUrl": { "type": "string" },
        "platform": { "type": "string" },
        "steps": { "type": "array", "items": { "$ref": "#/$defs/Step" } },
        "startTime": { "type": "string", "format": "date-time" },
        "duration": { "type": "string" },
        "llmMetrics": { "$ref": "#/$defs/LLMMetrics" },
        "profilingMetrics": { "$ref": "#/$defs/ProfilingMetrics" },
        "platformConfig": { "$ref": "#/$defs/PlatformConfig" },
        "logUrl": { "type": "string" },
        "testCaseId": { "type": "string" },
        "context": { "type": "string" },
        "cacheSourceId": { "type": "string" },
        "viewport": { "$ref": "#/$defs/Viewport" }
      },
      "required": ["id", "status", "steps"]
    },
    "Step": {
      "type": "object",
      "properties": {
        "title": { "type": "string" },
        "status": { "type": "integer", "enum": [0, 1, 2, 3, 4] },
        "explanation": { "type": "string" },
        "actions": { "type": "array", "items": { "$ref": "#/$defs/Action" } },
        "startTime": { "type": "string", "format": "date-time" },
        "duration": { "type": "string" },
        "failureReasonCategory": { "type": "string" },
        "profilingMetrics": { "$ref": "#/$defs/ProfilingMetrics" },
        "executionMode": { "type": "integer", "enum": [0, 1, 2, 3, 4, 5, 6, 7] },
        "cacheStatus": { "type": "integer", "enum": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] },
        "stepType": { "type": "integer", "enum": [0, 1, 2, 3] }
      }
    },
    "Action": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "xCoordinate": { "type": "integer" },
        "yCoordinate": { "type": "integer" },
        "text": { "type": "string" },
        "screenshotUrl": { "type": "string" },
        "llmMessage": { "type": "string" },
        "startTime": { "type": "string", "format": "date-time" },
        "duration": { "type": "string" },
        "element": { "$ref": "#/$defs/HTMLElement" },
        "toolCallId": { "type": "string" },
        "responseId": { "type": "string" },
        "keys": { "type": "array", "items": { "type": "string" } },
        "beforeUrl": { "type": "string" },
        "afterUrl": { "type": "string" },
        "button": { "type": "string" },
        "type": { "type": "string" },
        "path": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "x": { "type": "integer" },
              "y": { "type": "integer" }
            }
          }
        },
        "scrollX": { "type": "integer" },
        "scrollY": { "type": "integer" },
        "toolCalls": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": { "type": "string" },
              "input": { "type": "string" },
              "output": { "type": "string" }
            }
          }
        },
        "swipeParams": { "$ref": "#/$defs/SwipeParams" }
      }
    },
    "HTMLElement": {
      "type": "object",
      "properties": {
        "alt": { "type": "string" },
        "ariaLabel": { "type": "string" },
        "checked": { "type": "boolean" },
        "className": { "type": "string" },
        "disabled": { "type": "boolean" },
        "href": { "type": "string" },
        "id": { "type": "string" },
        "options": { "type": "array", "items": { "type": "string" } },
        "placeholder": { "type": "string" },
        "readonly": { "type": "boolean" },
        "required": { "type": "boolean" },
        "selected": { "type": "boolean" },
        "src": { "type": "string" },
        "tagName": { "type": "string" },
        "testpilotId": { "type": "string" },
        "textContent": { "type": "string" },
        "title": { "type": "string" },
        "value": { "type": "string" },
        "name": { "type": "string" },
        "dataTestid": { "type": "string" },
        "target": { "type": "string" },
        "type": { "type": "string" },
        "selectedValue": { "type": "string" },
        "width": { "type": "integer" },
        "height": { "type": "integer" }
      }
    },
    "LLMMetrics": {
      "type": "object",
      "properties": {
        "promptTokens": { "type": "integer" },
        "completionTokens": { "type": "integer" },
        "anthropicCachedInputTokens": { "type": "integer" },
        "maxScreenshots": { "type": "integer" }
      }
    },
    "ProfilingMetrics": {
      "type": "object",
      "properties": {
        "totalDuration": { "type": "string" },
        "llmDuration": { "type": "string" },
        "toolDuration": { "type": "string" },
        "attempts": { "type": "integer" }
      }
    },
    "PlatformConfig": {
      "type": "object",
      "properties": {
        "url": { "type": "string" },
        "androidPkg": { "type": "string" }
      }
    },
    "Viewport": {
      "type": "object",
      "properties": {
        "width": { "type": "integer" },
        "height": { "type": "integer" }
      }
    },
    "SwipeParams": {
      "type": "object",
      "properties": {
        "repetitions": { "type": "integer" },
        "startX": { "type": "integer" },
        "startY": { "type": "integer" },
        "endX": { "type": "integer" },
        "endY": { "type": "integer" }
      }
    }
  }
}
```

## Field Descriptions

### Report Fields

* **`id`** (string): Unique report identifier with `tpreport_` prefix
* **`startTime`** (string): ISO 8601 timestamp when the test run began
* **`duration`** (string): Total execution time in duration format (for example, "137.221 s")
* **`platforms`** (string\[]): List of platforms/browsers used in the test run
* **`statusSummary`** (StatusSummary\[]): Aggregated count of tests by their final status
* **`tests`** (Test\[]): Array of all test executions in this report
* **`title`** (string): Human-readable name for the report
* **`orgId`** (string): Organization identifier with `org_` prefix
* **`token`** (string): Access token for report authentication
* **`ownerName`** (string): Display name of the report owner
* **`isArchived`** (boolean): Whether the report has been archived

### StatusSummary Fields

* **`count`** (integer): Number of tests with this status
* **`status`** (integer): Status enum value (see Status table below)

### Test Fields

* **`id`** (string): Unique test identifier. This can be used to correlate tests across runs, even if the title or description of the test changes.
* **`title`** (string): Human-readable test name
* **`status`** (integer): Final test execution status (Status enum)
* **`explanation`** (string): Agent's explanation of the test outcome
* **`videoUrl`** (string): URL or path to the test execution video recording
* **`platform`** (string): Platform or browser used for this test
* **`steps`** (Step\[]): Ordered array of test steps executed
* **`startTime`** (string): ISO 8601 timestamp when test execution began
* **`duration`** (string): Test execution time in duration format
* **`llmMetrics`** (LLMMetrics): Token usage and LLM-related metrics
* **`profilingMetrics`** (ProfilingMetrics): Performance timing metrics
* **`platformConfig`** (PlatformConfig): Platform-specific configuration
* **`logUrl`** (string): URL or path to detailed test execution logs
* **`url`** (string): URL of the test case, **Deprecated**, use `platformConfig.url` instead
* **`testCaseId`** (string): Test case identifier from the pilot file
* **`context`** (string): Historical or contextual information for the test
* **`cacheSourceId`** (string): ID of the test used as cache source if applicable
* **`viewport`** (Viewport): Screen dimensions used during test execution

### Step Fields

* **`title`** (string): Human-readable step description
* **`status`** (integer): Step execution status (Status enum)
* **`explanation`** (string): Agent's explanation of what happened in this step
* **`actions`** (Action\[]): Individual actions performed within this step
* **`startTime`** (string): ISO 8601 timestamp when step execution began
* **`duration`** (string): Step execution time in duration format
* **`failureReasonCategory`** (string): Optional categorization of failure reason
* **`profilingMetrics`** (ProfilingMetrics): Step-level performance metrics
* **`executionMode`** (integer): How the step was executed (ExecutionMode enum)
* **`cacheStatus`** (integer): Cache utilization status (CacheStatus enum)
* **`stepType`** (integer): Classification of the step type (StepType enum)

### Action Fields

* **`name`** (string): Human-readable action name (for example, "left click," "screenshot")
* **`xCoordinate`** (integer): X coordinate for pointer-based actions
* **`yCoordinate`** (integer): Y coordinate for pointer-based actions
* **`text`** (string): Text content for typing or text-based actions
* **`screenshotUrl`** (string): URL or path to screenshot taken during action
* **`llmMessage`** (string): Agent's reasoning or message for this action
* **`startTime`** (string): ISO 8601 timestamp when action began
* **`duration`** (string): Action execution time in duration format
* **`element`** (HTMLElement): DOM element that was interacted with
* **`toolCallId`** (string): LLM tool call identifier
* **`responseId`** (string): LLM response identifier
* **`keys`** (string\[]): Array of key names for keyboard actions
* **`beforeUrl`** (string): Page URL before the action was performed
* **`afterUrl`** (string): Page URL after the action was performed
* **`button`** (string): Mouse button used (for example, "left," "right")
* **`type`** (string): Action type classification (for example, "click," "type")
* **`path`** (DragPath\[]): Coordinate path for drag gestures
* **`scrollX`** (integer): Horizontal scroll position
* **`scrollY`** (integer): Vertical scroll position
* **`toolCalls`** (ToolCall\[]): LLM tool calls made during this action
* **`swipeParams`** (SwipeParams): Parameters for mobile swipe gestures

### HTMLElement Fields

* **`alt`** (string): Alt text attribute
* **`ariaLabel`** (string): ARIA label attribute
* **`checked`** (boolean): Whether checkbox/radio is checked
* **`className`** (string): CSS class names
* **`disabled`** (boolean): Whether element is disabled
* **`href`** (string): Link URL for anchor elements
* **`id`** (string): HTML ID attribute
* **`options`** (string\[]): Available options for select elements
* **`placeholder`** (string): Placeholder text
* **`readonly`** (boolean): Whether element is read-only
* **`required`** (boolean): Whether element is required
* **`selected`** (boolean): Whether option is selected
* **`src`** (string): Source URL for media elements
* **`tagName`** (string): HTML tag name (for example, "INPUT," "BUTTON")
* **`testpilotId`** (string): TestPilot-generated element identifier
* **`textContent`** (string): Text content of the element
* **`title`** (string): Title attribute
* **`value`** (string): Current value of form elements
* **`name`** (string): Name attribute
* **`dataTestid`** (string): data-testid attribute for testing
* **`target`** (string): Target attribute for links
* **`type`** (string): Type attribute (for example, input type)
* **`selectedValue`** (string): Value of selected option
* **`width`** (integer): Element width in pixels
* **`height`** (integer): Element height in pixels

### Other Object Fields

#### LLMMetrics

* **`promptTokens`** (integer): Number of input tokens sent to LLM
* **`completionTokens`** (integer): Number of output tokens received from LLM
* **`anthropicCachedInputTokens`** (integer): Number of cached input tokens (Anthropic-specific)
* **`maxScreenshots`** (integer): Maximum number of screenshots allowed

#### ProfilingMetrics

* **`totalDuration`** (string): Total time spent
* **`llmDuration`** (string): Time spent waiting for LLM responses
* **`toolDuration`** (string): Time spent executing tools/actions
* **`attempts`** (integer): Number of execution attempts

#### PlatformConfig

* **`url`** (string): Target URL for web testing
* **`androidPkg`** (string): Android package name for mobile testing
* **`iosPkg`** (string): iOS package name for mobile testing

#### Viewport

* **`width`** (integer): Viewport width in pixels
* **`height`** (integer): Viewport height in pixels

## Enum Reference Tables

### Status

| Number | Name                | Meaning                                       |
| ------ | ------------------- | --------------------------------------------- |
| 0      | STATUS\_UNSPECIFIED | Status is unknown or not set                  |
| 1      | STATUS\_PENDING     | Test or step is still in progress             |
| 2      | STATUS\_SUCCEEDED   | Completed successfully (passed)               |
| 3      | STATUS\_FAILED      | Completed with failure                        |
| 4      | STATUS\_INCOMPLETE  | Did not finish all steps (aborted or skipped) |

### ExecutionMode

| Number | Name                                      | Meaning                                          |
| ------ | ----------------------------------------- | ------------------------------------------------ |
| 0      | EXECUTION\_MODE\_UNSPECIFIED              | Mode not specified                               |
| 1      | EXECUTION\_MODE\_CUA                      | Executed by Computer Use Agent (LLM-driven)      |
| 2      | EXECUTION\_MODE\_CACHE                    | Step executed from cache (no live LLM run)       |
| 3      | EXECUTION\_MODE\_CACHE\_FALLBACK\_TO\_CUA | Cache attempted but fell back to agent execution |
| 4      | EXECUTION\_MODE\_FALLBACK\_TO\_CUA        | Non-CUA execution failed, fell back to agent     |
| 5      | EXECUTION\_MODE\_NON\_CUA                 | Non-CUA mode (deterministic/scripted)            |
| 6      | EXECUTION\_MODE\_SCRIPT                   | Script mode execution                            |
| 7      | EXECUTION\_MODE\_FORM\_FILLER             | Form filler mode execution                       |

### CacheStatus

| Number | Name                                                     | Meaning                                           |
| ------ | -------------------------------------------------------- | ------------------------------------------------- |
| 0      | CACHE\_STATUS\_UNSPECIFIED                               | Cache status not specified                        |
| 1      | CACHE\_STATUS\_HIT                                       | Cache entry found and used                        |
| 2      | CACHE\_STATUS\_MISS                                      | No suitable cache entry found                     |
| 3      | CACHE\_STATUS\_UNUSED\_IS\_RETRY                         | Cache ignored because step needed retry           |
| 4      | CACHE\_STATUS\_UNUSED\_IS\_ASSERTION                     | Cache ignored for assertion-only step             |
| 5      | CACHE\_STATUS\_UNUSED\_NON\_CACHEABLE\_EXECUTION\_MODE   | Cache ignored due to non-cacheable execution mode |
| 6      | CACHE\_STATUS\_UNUSED\_CONTAINS\_NON\_CACHEABLE\_ACTIONS | Cache ignored due to non-cacheable actions        |
| 7      | CACHE\_STATUS\_UNUSED\_ELEMENT\_IS\_MISSING              | Cache ignored because required element missing    |
| 8      | CACHE\_STATUS\_UNUSED\_HAS\_TOOL\_CALLS                  | Cache ignored because step involved tool calls    |
| 9      | CACHE\_STATUS\_UNUSED\_IS\_SCRIPT                        | Cache ignored for script-based step               |

### StepType

| Number | Name                        | Meaning                                      |
| ------ | --------------------------- | -------------------------------------------- |
| 0      | STEP\_TYPE\_UNSPECIFIED     | Step type not specified                      |
| 1      | STEP\_TYPE\_REGULAR\_ACTION | Regular user actions (click, type, navigate) |
| 2      | STEP\_TYPE\_FORM\_FILLING   | Data entry or form completion                |
| 3      | STEP\_TYPE\_VERIFICATION    | Assertion or verification of expected state  |

## Example Usage

### Basic Report Structure

```json  theme={null}
{
  "id": "tpreport_01abc123...",
  "startTime": "2025-10-30T10:00:00Z",
  "duration": "45.123&nbsp;s",
  "platforms": ["Linux - Chrome"],
  "statusSummary": [
    {"count": 3, "status": 2},
    {"count": 1, "status": 3}
  ],
  "tests": [
    {
      "id": "tptest_01def456...",
      "title": "Login Test",
      "status": 2,
      "steps": [
        {
          "title": "Navigate to login page",
          "status": 2,
          "actions": [
            {
              "name": "navigate",
              "type": "navigate",
              "beforeUrl": "",
              "afterUrl": "https://example.com/login"
            }
          ]
        }
      ]
    }
  ]
}
```

## Notes

* **Field Naming**: All JSON fields use `camelCase` convention
* **Timestamps**: Use ISO 8601 format (for example, "2025-10-30T10:00:00Z")
* **Durations**: String format with units (for example, "45.123 s," "1m30.5 s")
* **Enum values**: Always serialized as numeric values in JSON
* **TypeIDs**: Use specific prefixes (`tpreport_`, `tptest_`, `org_`)
* **Optional Fields**: May be omitted entirely or contain zero/empty values
* **File Locations**: Per-test results saved as `results.json`, aggregated reports contain full structure


# Getting Started with Testpilot
Source: https://www.jetify.com/docs/docs/testpilot/getting-started/index

Install Testpilot and run your first AI-powered end-to-end test in minutes. Start testing web, Android, and iOS applications.

Welcome to Testpilot! This section will get you up and running with AI-powered end-to-end testing
quickly.

<CardGroup cols={2}>
  <Card title="Install Testpilot" icon="gear" href="/docs/testpilot/install">
    Install Testpilot and configure your environment in minutes.
  </Card>

  <Card title="Testing Web Apps" icon="browser" href="/docs/testpilot/getting-started/testing-web-apps">
    Write and run your first browser-based test with Testpilot.
  </Card>

  <Card title="Testing Android Apps" icon="mobile" href="/docs/testpilot/getting-started/testing-android-apps">
    Learn to test Android applications and emulators.
  </Card>

  <Card title="Testing iOS Apps" icon="phone" href="/docs/testpilot/getting-started/testing-ios-apps">
    Configure and run tests on iOS devices and simulators.
  </Card>
</CardGroup>

## Next Steps

Once you've completed the setup and run your first test, explore our
[Guides](/docs/testpilot/guides/) section for common testing scenarios. For advanced features like
AI test generation and MCP integration, see the [Advanced](/docs/testpilot/advanced) section.


# Testing Android Apps with Testpilot
Source: https://www.jetify.com/docs/docs/testpilot/getting-started/testing-android-apps

Run automated tests on Android devices and emulators. Set up Appium, configure your device, and execute your first Android test.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you can run tests on Android devices, you'll need to set up Appium:

1. Install Appium Server and dependencies:

   ```bash  theme={null}
   # Install Appium globally
   npm install -g appium

   # Install Appium Doctor for diagnostics
   npm install -g appium-doctor

   # Install the Android driver
   appium driver install uiautomator2
   ```

2. Verify your Appium installation:

   ```bash  theme={null}
   appium-doctor
   ```

   This command will check your system and highlight any issues that need to be fixed.

3. Start the Appium server:

   ```bash  theme={null}
   appium --allow-cors
   ```

   You'll need to keep this server running in a separate terminal window while executing your tests.

## Setting Up an Android Device[​](#setting-up-an-android-device "Direct link to Setting Up an Android Device")

Testpilot discovers Android devices through the Android Debug Bridge (adb). You have several options
for creating test devices:

### Option 1: Android Studio Emulator (Recommended)[​](#option-1-android-studio-emulator-recommended "Direct link to Option 1: Android Studio Emulator (Recommended)")

1. Download and install [Android Studio](https://developer.android.com/studio)
2. Launch Android Studio and open the Device Manager
3. Click on "Create Device" and select "Pixel 7" (recommended for optimal compatibility)
4. Choose a system image (Android 12 or newer is recommended)
5. Complete the setup and start the emulator

### Option 2: Physical Device[​](#option-2-physical-device "Direct link to Option 2: Physical Device")

1. Enable Developer Options on your Android device:
   * Go to Settings > About Phone
   * Tap "Build Number" 7 times to enable Developer Options

2. Enable USB Debugging in Developer Options

3. Connect your device to your computer with a USB cable

4. Accept any authorization prompts on your device

### Option 3: Connecting with Emulator.wtf[​](#option-3-connecting-with-emulatorwtf "Direct link to Option 3: Connecting with Emulator.wtf")

[emulator.wtf](https://emulator.wtf) lets you quickly spin up remote Android emulators, connect over
ADB, and run your Android Unit and Testpilot tests on the remote device. You can connect Testpilot
to your `emulator.wtf` devices using the following steps:

1. Create an [`emulator.wtf`](http://emulator.wtf) account and API token.
2. Set your API token to the following env var: `EW_API_TOKEN`
3. Follow the [documentation](https://docs.emulator.wtf/integrations/cli/) to install the
   `emulator.wtf` CLI
4. Run the following command to create an [`emulator.wtf`](http://emulator.wtf) device and connect
   it to your local `adb`: `ew-cli start-session --device model=Pixel7,version=34,gpu=auto`
5. You’re device is now ready to run Appium tests!

## Creating an Android Test[​](#creating-an-android-test "Direct link to Creating an Android Test")

Create a test file (e.g., `android-test.pilot.yaml`) with the platform\_config specifying your
Android app package:

```yaml  theme={null}
name: "Android App Test"
context:
  - text: "Testing a native Android application"
cases:
  - id: "android-basic-001"
    name: "Basic Android Navigation"
    description: "Test basic navigation in the Android app"
    platform_config:
      android_pkg: "com.example.myapp"  # Replace with your app's package name
    steps:
      - "Verify the app launches successfully"
      - "Tap on the 'Login' button"
      - "Enter username and password"
      - "Tap the Submit button"
      - "Verify successful login"
```

## Running Android Tests[​](#running-android-tests "Direct link to Running Android Tests")

To run a test on an Android device, use the following command:

```bash  theme={null}
testpilot test android-test.pilot.yaml --driver appium --os android --runtime native
```

For testing web content in Chrome on an Android device:

```bash  theme={null}
testpilot test web-test.pilot.yaml --driver appium --os android --runtime chrome
```

## Test Platform Configuration[​](#test-platform-configuration "Direct link to Test Platform Configuration")

The `platform_config` section lets you define the android app that you want to run your tests on.
You can specify an app and URL for both browser based and native application tests

```yaml  theme={null}
platform_config:
  url: "https://example.com"        # For browser-based tests
  android_pkg: "com.example.myapp"  # For native app tests
```

* Use `url` for browser-based tests on Android Chrome
* Use `android_pkg` for native Android app tests


# Testing iOS Apps with Testpilot
Source: https://www.jetify.com/docs/docs/testpilot/getting-started/testing-ios-apps

Run automated tests on iOS devices and simulators. Configure Xcode, set up your iOS simulator, and execute your first iOS test.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you can run tests on iOS devices, you'll need to set up Appium and the iOS-specific
dependencies:

1. Install Appium Server and dependencies:

   ```bash  theme={null}
   # Install Appium globally
   npm install -g appium

   # Install Appium Doctor for diagnostics
   npm install -g appium-doctor

   # Install the XCUITest driver for iOS testing
   appium driver install xcuitest
   ```

2. Verify your Appium installation:

   ```bash  theme={null}
   appium-doctor --ios
   ```

   This command will check your system specifically for iOS testing requirements and highlight any
   issues that need to be fixed.

3. Start the Appium server:

   ```bash  theme={null}
   appium --allow-cors
   ```

   You'll need to keep this server running in a separate terminal window while executing your tests.

## Setting Up an iOS Simulator[​](#setting-up-an-ios-simulator "Direct link to Setting Up an iOS Simulator")

Testpilot works with iOS simulators managed through Xcode. Here's how to set one up:

1. Install Xcode from the Mac App Store (requires macOS)

2. Open Xcode and accept any license agreements

3. Open the simulator by going to Xcode → Open Developer Tool → Simulator

4. Create a new simulator device:
   * In Xcode, go to Window → Devices and Simulators
   * Click the "+" button to add a new simulator
   * Choose a device type (iPhone 13 or newer recommended)
   * Select the latest iOS version
   * Give your simulator a descriptive name and click "Create"

## Creating an iOS Test[​](#creating-an-ios-test "Direct link to Creating an iOS Test")

Create a test file (e.g., `ios-test.pilot.yaml`) with the platform\_config specifying your iOS app
bundle identifier:

```yaml  theme={null}
name: "iOS App Test"
context:
  - text: "Testing a native iOS application"
cases:
  - id: "ios-basic-001"
    name: "Basic iOS Navigation"
    description: "Test basic navigation in the iOS app"
    platform_config:
      ios_bundle: "com.example.MyApp"  # Replace with your app's bundle identifier
    steps:
      - "Verify the app launches successfully"
      - "Tap on the 'Login' button"
      - "Enter username and password"
      - "Tap the Submit button"
      - "Verify successful login"
```

## Running iOS Tests[​](#running-ios-tests "Direct link to Running iOS Tests")

To run a test on an iOS simulator or device, use the following command. You must specify the
`--driver`, `--os`, `--runtime`, `--os-version`, and `--udid` flags to ensure the test runs
correctly on your iOS simulator:

```bash  theme={null}
testpilot test ios-test.pilot.yaml --driver appium --os ios --runtime native --udid <device-udid>
```

<Check>
  You can find your device's UDID using

  ```bash  theme={null}
  xcrun simctl list
  ```

  To get a list of running sims, use:

  ```bash  theme={null}
  xcrun simctl list booted
  ```
</Check>

For testing web content in Safari on an iOS device:

```bash  theme={null}
testpilot test web-test.pilot.yaml --driver appium --os ios --runtime safari --os-version 18.5
```

## Test Platform Configuration[​](#test-platform-configuration "Direct link to Test Platform Configuration")

The `platform_config` section of your test file is crucial for iOS testing:

```yaml  theme={null}
platform_config:
  url: "https://example.com"      # For browser-based tests
  ios_bundle: "com.example.MyApp" # For native app tests
```

* Use `url` for browser-based tests on iOS Safari
* Use `ios_bundle` for native iOS app tests

## iOS-Specific Considerations[​](#ios-specific-considerations "Direct link to iOS-Specific Considerations")

When testing iOS applications, keep in mind:

1. **Permissions**: iOS will prompt for permissions (camera, microphone, etc.). Your test steps
   should account for these permission dialogs.

2. **Security Features**: iOS has stricter security than Android. Your app must be properly signed
   and provisioned for testing.

3. **App Installation**: For simulators, you'll need an .app file; for physical devices, you'll need
   a signed .ipa file.


# Testing Web Apps with Testpilot
Source: https://www.jetify.com/docs/docs/testpilot/getting-started/testing-web-apps

Write and run your first browser-based test with Testpilot. Learn how to create test plans, execute tests, and view detailed results.

## Step 1: Write a Simple Test[​](#step-1-write-a-simple-test "Direct link to Step 1: Write a Simple Test")

Testpilot runs tests that are written in a pilotplan format. For this example we'll use YAML, but
Testpilot can also recognize pilot files written in TOML or JSON:

Here is a simple test that will go to Hacker News, search for a topic, and click the first result.

Copy these contents to a yaml file titled `example-hn-search.pilot.yaml`.

```yaml  theme={null}
name: "Hacker News Search Test"

# List of Cases to Execute
cases:
  - id: "testcase_01jy2m0vh8f05vv5qmkkxf6zxt"
    name: "Search for Devbox on Hacker News"
    description: "Navigate to news.ycombinator.com, search for Devbox, and click the first search result"
    url: "https://news.ycombinator.com"
    
    # List of Test Steps
    steps:
      - "Use the search bar on the front page to search for Devbox"
      - "Verify search results for 'Devbox' are displayed"
      - "Click on the first search result link"
      - "Verify the clicked post or article has loaded correctly"
```

Tests are provided to Testpilot as a list of `cases`, where each case executres one or more `steps`.
When Testpilot executes a test case, it opens the `url` of the test case in a new browser or device
context, and begins executing the `steps`.

## Step 2: Running your Test[​](#step-2-running-your-test "Direct link to Step 2: Running your Test")

You can run your test files using `testpilot test <path_to_file>`. Testpilot runs your tests in
headless mode by default, but you can use `--show-browser` to watch what Testpilot is doing live:

```bash  theme={null}
testpilot test example-hn-search.pilot.yaml --show-browser
```

Testpilot will launch the browser and begin executing your testplan live. You can view the LLM's
actions and reasoning in your terminal:

```bash  theme={null}
❯ testpilot test example-hn-search.pilot.yaml
Info: Found 1 pilot plan
-> Test Case: Search for Devbox on Hacker News
Starting step 1/4: Use the search bar on the front page to search for Devbox
  📸 Action: screenshot
        Reasoning: Scrolling to find search bar
  ↕️ Action: scroll at [513, 742]
        Reasoning: Clicking search bar, entering "Devbox"
  🖱️ Action: left_click at [524, 742]
        Reasoning: Typing "Devbox" in search bar
  ⌨️ Action: type 'Devbox'
        Reasoning: Initiating search for "Devbox"
  🎹 Action: keypress
        Reasoning: Displaying successful search results for Devbox
  📸 Action: screenshot
Finished step 1/4: Use the search bar on the front page to search for Devbox
  🏁 Action: Conclude Step (Success)
Starting step 2/4: Verify search results for 'Devbox' are displayed
  📸 Action: screenshot
        Reasoning: Confirming successful search for Devbox
  📸 Action: screenshot
  🏁 Action: Conclude Step (Success)
Finished step 2/4: Verify search results for 'Devbox' are displayed
Starting step 3/4: Click on the first search result link
  📸 Action: screenshot
        Reasoning: Clicking first search result link
  🖱️ Action: left_click at [184, 81]
        Reasoning: Accessed Devbox page, confirming content
  📸 Action: screenshot
Finished step 3/4: Click on the first search result link
Starting step 4/4: Verify the clicked post or article has loaded correctly
  🏁 Action: Conclude Step (Success)
  📸 Action: screenshot
        Reasoning: Confirming page content relevance, successful.
  📸 Action: screenshot
  🏁 Action: Conclude Step (Success)
Finished step 4/4: Verify the clicked post or article has loaded correctly
```

## Step 3: Viewing your Test Results[​](#step-3-viewing-your-test-results "Direct link to Step 3: Viewing your Test Results")

Once your test is finished, a static HTML report with the results, screenshots, and video of the
test will be written to `testpilot-out`. You can view the results by opening the index.html at the
root of the folder:

```bash  theme={null}
open testpilot-out/index.html
```

<img src="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=be01ffcc6347e29c23880386068c174b" alt="Test Output Example" data-og-width="2528" width="2528" data-og-height="1762" height="1762" data-path="docs/testpilot/getting-started/testpilot-test-output-example.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?w=280&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=bba743cd250780cb8c7f01bb836e0585 280w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?w=560&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=fa81762922778b291563f09f7ab60f1d 560w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?w=840&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=b40f426cb665036e6903a0e742886c4a 840w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?w=1100&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=284633c6ccbe527c78a816b3598e3bb9 1100w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?w=1650&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=444bf19a24d671e9bd56299213f6fada 1650w, https://mintcdn.com/jetify/k7lJpyU9i-Y_obPW/docs/testpilot/getting-started/testpilot-test-output-example.png?w=2500&fit=max&auto=format&n=k7lJpyU9i-Y_obPW&q=85&s=0f7b4bad6c6c4a2a3e486eb45850cb2b 2500w" />


# How to Add Context to Testpilot Tests
Source: https://www.jetify.com/docs/docs/testpilot/guides/add-context-to-tests

Improve test accuracy by adding context to your Testpilot tests. Learn when and how to provide application details and requirements.

## What is Context?[​](#what-is-context "Direct link to What is Context?")

Context in Testpilot is additional information that helps the AI better understand:

* How your application works
* Special requirements or conditions for tests
* Expected behaviors or edge cases
* Login credentials or test data

Context is passed to the AI model along with your test steps, helping it make better decisions
during test execution.

## Adding Context to Your Tests[​](#adding-context-to-your-tests "Direct link to Adding Context to Your Tests")

You can add context at two levels in your pilot files:

### 1. Global Context (Test Suite Level)[​](#1-global-context-test-suite-level "Direct link to 1. Global Context (Test Suite Level)")

Global context applies to all test cases in a file. Add it at the root level of your test file:

```yaml  theme={null}
name: "E-commerce Test Suite"
login_url: "https://example.com/login"
context:
  - text: "This is an e-commerce site that sells electronics"
  - text: "The navigation menu is at the top of every page"
  - text: "Product search requires at least 3 characters"
  - text: "Prices are displayed in USD"
cases:
  # Test cases will inherit all the context above
  - id: "test-001"
    # ...
```

### 2. Test-Specific Context (Test Case Level)[​](#2-test-specific-context-test-case-level "Direct link to 2. Test-Specific Context (Test Case Level)")

Test-specific context applies only to a single test case:

```yaml  theme={null}
cases:
  - id: "checkout-test-001"
    name: "Complete Checkout"
    description: "Test the full checkout process"
    url: "https://example.com/cart"
    context:
      - text: "The checkout process has 3 steps: shipping, payment, and confirmation"
      - text: "Credit card validation happens in real-time as the user types"
      - text: "For test purposes, use credit card number: 4111 1111 1111 1111"
    steps:
      # These steps have access to both global and test-specific context
      - "Click on the checkout button"
      - "Fill in shipping information"
      # ...
```

## Best Practices for Adding Context[​](#best-practices-for-adding-context "Direct link to Best Practices for Adding Context")

### Be Specific and Relevant[​](#be-specific-and-relevant "Direct link to Be Specific and Relevant")

Add context that directly helps with test execution:

```yaml  theme={null}
context:
  - text: "The login button changes to 'Logging in...' while processing"
  - text: "Error messages appear below each form field"
  - text: "The user menu is only visible after successful login"
```

### Explain UI Components[​](#explain-ui-components "Direct link to Explain UI Components")

Describe important UI elements and their behavior:

```yaml  theme={null}
context:
  - text: "The navigation uses a hamburger menu on mobile screens"
  - text: "The search bar expands when clicked"
  - text: "The product filter sidebar can be collapsed by clicking the X button"
```

### Provide Business Rules[​](#provide-business-rules "Direct link to Provide Business Rules")

Include relevant business logic or validation rules:

```yaml  theme={null}
context:
  - text: "Promotional codes are case-sensitive and must be entered without spaces"
```

### Specify Test Environment Details[​](#specify-test-environment-details "Direct link to Specify Test Environment Details")

Include information about your test environment:

```yaml  theme={null}
context:
  - text: "This is a staging environment and emails are not actually sent"
  - text: "The payment gateway is in test mode"
  - text: "API responses may be delayed by 1-2 seconds in this environment"
```

## When to Use Additional Context[​](#when-to-use-additional-context "Direct link to When to Use Additional Context")

Add extra context when:

1. **Your application has unique or complex behaviors** that might not be immediately obvious
2. **Test steps require specific knowledge** about the application state or business rules
3. **Handling error conditions or edge cases** that require special treatment


# Email Testing with Mailosaur
Source: https://www.jetify.com/docs/docs/testpilot/guides/email-testing-mailosaur

Test email registration and verification flows with Mailosaur. Generate email addresses, retrieve OTP codes, and verify email content.

## How It Works[​](#how-it-works "Direct link to How It Works")

When your tests need an email address, Testpilot can:

1. Automatically generate a unique Mailosaur email address
2. Use this email to receive real emails during test execution
3. Access the inbox to retrieve verification codes, magic links, or other information
4. Complete the authentication or verification flow automatically

## Setup[​](#setup "Direct link to Setup")

### 1. Create a Mailosaur Account[​](#1-create-a-mailosaur-account "Direct link to 1. Create a Mailosaur Account")

If you don't already have one, [sign up for a Mailosaur account](https://mailosaur.com/sign-up/) and
retrieve your API credentials. You will need a Mailosaur API Key and Server ID to configure
Testpilot.

### 3. Set Environment Variables[​](#3-set-environment-variables "Direct link to 3. Set Environment Variables")

Configure Testpilot to use your Mailosaur account by setting these environment variables:

```bash  theme={null}
export MAILOSAUR_API_KEY=your_api_key
export MAILOSAUR_SERVER_ID=your_server_id
```

In CI environments, add these to your secure environment variables.

## Using Generated Emails in Tests[​](#using-generated-emails-in-tests "Direct link to Using Generated Emails in Tests")

Once configured, Testpilot will automatically handle email generation. You don't need to explicitly
specify email addresses in your test scenarios - Testpilot will generate and use them as needed. For
example, you can test a signup flow using a unique, randomly generated email as shown below:

### Example Test Scenario[​](#example-test-scenario "Direct link to Example Test Scenario")

```yaml  theme={null}
cases:
  id: email_signup_0001
  name: Sign up with email verification
  description: Use a random email to test the signup flow
  url: https://zillow.com/signup
  steps:
    - Click Create Account
    - Enter an email address to signup for an account
    - Enter a password
```

## Manually Specifying Email Addresses

If you prefer not to use the Mailosaur integration, you can explicitly specify email addresses in your test scenarios:

```yaml  theme={null}
cases:
  id: email_signup_0001
  name: Sign up with email verification
  description: Use a random email to test the signup flow
  url: https://zillow.com/signup
  steps:
    - Click Create Account
    - Sign up for an account with email address "test123@example-email.com"
    - Enter a password
```

Note that without Mailosaur integration, Testpilot won't be able to automatically check inboxes or
handle email verification flows, unless you design a test case specifically for this workflow.


# Testpilot Guides
Source: https://www.jetify.com/docs/docs/testpilot/guides/index

Task-focused guides for common testing scenarios. Learn authentication, email testing, parameterization, and performance optimization.

These guides help you solve specific testing challenges and implement advanced workflows with
Testpilot.

<CardGroup cols={2}>
  <Card title="Adding Context to Tests" icon="info" href="/docs/testpilot/guides/add-context-to-tests">
    Provide additional context to improve AI test understanding and reliability.
  </Card>

  <Card title="Email Testing with Mailosaur" icon="mail" href="/docs/testpilot/guides/email-testing-mailosaur">
    Integrate with Mailosaur for email-based testing and verification.
  </Card>

  <Card title="Testing Authentication" icon="key" href="/docs/testpilot/guides/test-authentication">
    Configure authentication to reuse login sessions across test cases.
  </Card>

  <Card title="Parameterizing Tests" icon="settings" href="/docs/testpilot/guides/parameterize-tests-environment-variables">
    Make tests flexible and reusable with environment variables and parameters.
  </Card>

  <Card title="Testing Responsive Design" icon="monitor" href="/docs/testpilot/guides/test-responsive-design">
    Test your application across different screen sizes and devices.
  </Card>

  <Card title="Parallel Testing" icon="zap" href="/docs/testpilot/guides/parallel-testing">
    Optimize test execution speed with parallel testing strategies.
  </Card>
</CardGroup>

## When to Use These Guides

* **Authentication**: When testing features behind login walls
* **Context**: When tests fail due to ambiguous UI elements
* **Parameterization**: When running tests across multiple environments
* **Viewports**: When ensuring responsive design works correctly
* **Email**: When testing registration or password reset flows
* **Performance**: When test suites take too long to complete

## Related Resources

* [Getting Started](/docs/testpilot/getting-started/) - If you're new to Testpilot
* [CLI Reference](/docs/testpilot/reference/cli/) - For command-line options and flags
* [Pilotfile Reference](/docs/testpilot/pilotfile-reference) - For configuration details


# Parallel Testing with Concurrency and Sharding
Source: https://www.jetify.com/docs/docs/testpilot/guides/parallel-testing

Speed up test execution by running tests in parallel. Configure concurrency for single machines and sharding across multiple workers.

## Concurrency (single machine parallelism)[​](#concurrency-single-machine-parallelism "Direct link to Concurrency (single machine parallelism)")

When you set `--concurrency N`, Testpilot keeps up to N test files in flight on that machine. If you
omit the flag, we apply a sensible default of 10.

::: info Mobile tests are automatically forced to `1` because simulators/devices do not support
running multiple tests or instances of an application concurrently. Future releases will introduce
the option to pass multiple devices to run mobile tests in parallel. :::

Typical usage:

```bash  theme={null}
# Use default concurrency
testpilot test plans/

# Explicit 5-way concurrency
testpilot test --concurrency 5 plans/

# Force serial execution
testpilot test --concurrency 1 plans/
```

## Sharding (splitting the suite across workers)[​](#sharding-splitting-the-suite-across-workers "Direct link to Sharding (splitting the suite across workers)")

Sharding tells multiple independent processes or machines to each take a deterministic slice. You
specify it as `current/total` with a 1-based shard index:

```bash  theme={null}
# First of three shards
testpilot test --shard 1/3 plans/

# Third of five shards
testpilot test --shard 3/5 plans/
```

Distribution is straightforward: we take the ordered test list and partition it as evenly as
possible from the front. If 10 tests are split with `--shard 1/3`, shard 1 receives 4 tests while
shards 2 and 3 receive 3 each. (The earlier shards may receive one extra when it does not divide
cleanly.) There is no dynamic balancing yet; faster shards will simply finish earlier.

### CI matrix example[​](#ci-matrix-example "Direct link to CI matrix example")

```yaml  theme={null}
strategy:
  matrix:
    shard: [1, 2, 3, 4]
steps:
  - run: testpilot test --shard ${{ matrix.shard }}/4 plans/
```

Each job now owns a quarter of the list. See the documentation on
[GitLab Configuration](/docs/testpilot/integrations/gitlab-cicd) for more details on how to set up sharding in your CI
pipeline.

## Caveats and nuances[​](#caveats-and-nuances "Direct link to Caveats and nuances")

**Flaky interaction**: If a test appears flaky only under parallel load, re-run it with
`--concurrency 1`. If the flake disappears, you have a shared state or isolation problem.

**Uneven shards**: Because assignment is static and some tests naturally run longer, total build
time is gated by the slowest shard. If one shard is consistently heavier, consider reorganizing test
files or increasing shard count so large tests disperse.

**Setup overhead**: Each shard performs its own initialization (dependency install, environment
bootstrap, auth, etc.). Extremely high shard counts can waste time in duplicated setup; balance raw
parallelism against this overhead.

**Resource ceilings**: Concurrency does not auto-scale down; if you hit memory or CPU limits, you
must lower `--concurrency` or reduce shard count (fewer processes overall). Mobile always remains
serial, regardless of the flag.

**Mobile**: Since mobile tests cannot be run concurrently on a single device, Testpilot forces
`--concurrency 1` for mobile testing to avoid simulator/device issues. Future releases will
introduce the option to pass multiple devices to run mobile tests in parallel.


# Parameterizing Tests with Environment Variables
Source: https://www.jetify.com/docs/docs/testpilot/guides/parameterize-tests-environment-variables

Make tests flexible and reusable with environment variables. Run the same tests across staging, development, and production environments.

## Using Environment Variables in Tests[​](#using-environment-variables-in-tests "Direct link to Using Environment Variables in Tests")

You can include environment variables in your test files using the format
`${ENV_VAR_NAME:-default_value}`. Testpilot will automatically expand these variables when running
your tests.

The syntax works as follows:

* `${ENV_VAR_NAME}` - Uses the value of the environment variable
* `${ENV_VAR_NAME:-default_value}` - Uses the value of the environment variable if set, otherwise
  uses the default value

## Example: Parameterizing Host URLs[​](#example-parameterizing-host-urls "Direct link to Example: Parameterizing Host URLs")

A common use case is parameterizing the host URL in your tests. This lets you run the same tests
against different environments without modifying your test files:

```yaml  theme={null}
name: "Parameterized URL Test"
context:
  - text: "Test can run against different environments based on the TEST_HOST environment variable"
cases:
  - id: "login-test-001"
    name: "User Login Test"
    description: "Test user login functionality across different environments"
    url: "${TEST_HOST:-https://staging.example.com}/login"
    steps:
      - "Navigate to the login page"
      - "Enter valid username and password"
      - "Click the login button"
      - "Verify successful login"
```

In this example:

* If `TEST_HOST` is set (e.g., `export TEST_HOST=https://dev.example.com`), the test will use that
  value
* If `TEST_HOST` is not set, it will fall back to the default value `https://staging.example.com`

## Running Tests with Different Parameters[​](#running-tests-with-different-parameters "Direct link to Running Tests with Different Parameters")

You can run the same test with different parameter values by changing the environment variables:

```bash  theme={null}
# Run against staging (default)
testpilot test login.pilot.yaml

# Run against development
export TEST_HOST=https://dev.example.com
testpilot test login.pilot.yaml

# Run against production
export TEST_HOST=https://example.com
testpilot test login.pilot.yaml
```

## Parameterizing Other Test Values[​](#parameterizing-other-test-values "Direct link to Parameterizing Other Test Values")

You can parameterize any string value in your test files, not just URLs:

```yaml  theme={null}
name: "User Registration Test"
context:
  - text: "Test registration with configurable user details"
cases:
  - id: "registration-001"
    name: "New User Registration"
    description: "Test new user registration process"
    url: "https://${TEST_HOST:-example.com}/register"
    steps:
      - "Fill in the registration form with email: ${TEST_EMAIL:[email protected]}"
      - "Set password to: ${TEST_PASSWORD:-SecurePass123!}"
      - "Complete registration and verify success"
```

## Use Cases for Parameterized Tests[​](#use-cases-for-parameterized-tests "Direct link to Use Cases for Parameterized Tests")

Parameterizing your tests is useful for:

1. **Environment Switching**: Run the same tests against dev, staging, and production
2. **Configuration Changes**: Test with different feature flags or settings
3. **Test Data Variation**: Use different test accounts or input data
4. **CI/CD Integration**: Configure tests differently based on the build environment
5. **Local Development**: Allow developers to point tests to their local instances

## Example in CI/CD Pipeline[​](#example-in-cicd-pipeline "Direct link to Example in CI/CD Pipeline")

Here's how you might use parameterized tests in a CI/CD pipeline:

```yaml  theme={null}
# In your CI/CD configuration
stages:
  - test

test_staging:
  stage: test
  script:
    - export TEST_HOST=https://staging.example.com
    - testpilot test tests/*.pilot.yaml

test_production:
  stage: test
  when: manual  # Only run when triggered manually
  script:
    - export TEST_HOST=https://example.com
    - testpilot test tests/*.pilot.yaml
```

## Best Practices[​](#best-practices "Direct link to Best Practices")

When parameterizing your tests:

1. **Always provide defaults**: Use the `:-default_value` syntax to ensure tests work even without
   environment variables set
2. **Document parameters**: Include comments or context that explains what parameters are available
3. **Use descriptive names**: Choose environment variable names that clearly indicate their purpose
4. **Group related parameters**: Keep related parameters together (e.g., `TEST_HOST`, `TEST_PORT`,
   `TEST_PROTOCOL`)

By parameterizing your tests, you create more flexible and maintainable test suites that can easily
adapt to different environments and configurations.


# Testing Authentication and Login Flows
Source: https://www.jetify.com/docs/docs/testpilot/guides/test-authentication

Test authenticated features efficiently. Configure login credentials, set up authentication URLs, and reuse sessions across test cases.

## Setting Login Credentials[​](#setting-login-credentials "Direct link to Setting Login Credentials")

Testpilot uses environment variables to securely manage your login credentials:

```bash  theme={null}
# Set your username and password as environment variables
export TESTPILOT_USERNAME="your-username"
export TESTPILOT_PASSWORD="your-password"
```

These credentials will be used whenever a test requires authentication. You can set these in your
shell profile, CI environment, or just before running your tests. You can also use the secret
manager of your choice to set these credentials before running Testpilot

## Configuring Custom Environment Variables For Login[](#configuring-custom-environment-variables-for-login "Direct link to Configuring Custom Environment Variables for Login")

Alternatively, you can also use custom env-vars of your own choosing by specifying them in the pilot file:

```yaml  theme={null}
name: "Configuring Environment Variables for Login"
login:
  username: ${MY_CUSTOM_USERNAME}
  password: ${MY_CUSTOM_PASSWORD}
cases:
  - ... # omitted for clarity
```

## Configuring Login URL [​](#configuring-login-url "Direct link to Configuring Login URL")

To tell Testpilot where to log in, add a `login.url` field to your pilot file:

```yaml  theme={null}
name: "Authenticated Tests Example"
login:
  url: "https://example.com/login"
cases:
  - id: "dashboard-test"
    name: "View Dashboard"
    description: "Test authenticated dashboard access"
    url: "https://example.com/dashboard"
    steps:
      - "Verify the dashboard has loaded"
      - "Check that user information is displayed correctly"
      - "Navigate to settings page"
```

The `login.url` parameter tells Testpilot where to perform the authentication before running your
tests.

## How Authentication Works For Websites[​](#how-authentication-works-for-websites "Direct link to How Authentication Works For Websites")

When you provide both a login URL and credentials, Testpilot will:

1. Launch a browser session
2. Navigate to the login URL
3. Automatically detect and fill in username and password fields
4. Submit the login form
5. Verify successful authentication
6. Reuse this authenticated session for all your test cases

This means you only authenticate once, and all your test cases benefit from the same authenticated
session, saving time and reducing flakiness.

## Example: Testing Authenticated Features in a Website[​](#example-testing-authenticated-features "Direct link to Example: Testing Authenticated Features in a Website")

Here's a complete example of testing features that require authentication:

```yaml  theme={null}
name: "User Account Tests"
login:
  url: "https://myapp.com/login"
  username: ${MY_CUSTOM_USERNAME}
  password: ${MY_CUSTOM_PASSWORD}
cases:
  - id: "profile-edit"
    name: "Edit User Profile"
    description: "Test editing user profile information"
    url: "https://myapp.com/account/profile"
    steps:
      - "Verify the profile page has loaded"
      - "Click the 'Edit Profile' button"
      - "Update the 'About Me' section with new text"
      - "Click the 'Save Changes' button"
      - "Verify success message appears"
      - "Reload the page and verify changes persisted"
  - id: "password-change"
    name: "Change Password"
    description: "Test changing user password"
    url: "https://myapp.com/account/security"
    steps:
      - "Navigate to the security settings page"
      - "Click on 'Change Password'"
      - "Enter current password and new password"
      - "Submit the form"
      - "Verify password change confirmation is displayed"
```

In this example, Testpilot will log in once, then run both test cases using the same authenticated
session.

By properly configuring login credentials and URL, you can easily test authenticated sections of
your application without repeatedly handling the login process in each test case.

## Example: Testing Login Flow for a mobile app[](#example-testing-login-flow-for-a-mobile-app "Direct link to Example: Testing Login Flow for a mobile app")

For mobile apps, the login steps have to be more explicitly specified and tested, notably as done in step 2 below.

```yaml  theme={null}
name: "Login Flow Test"
login:
  username: ${MY_CUSTOM_USERNAME}
  password: ${MY_CUSTOM_PASSWORD}
cases:
  - id: "perform-login"
    name: "Login to the app"
    description: "Test logging in to the app"
    steps:
      - "Click on the Login button on the top right"
      - "Login using username ${MY_CUSTOM_USERNAME} and password ${MY_CUSTOM_PASSWORD}"
      - "Verify the login was successful by confirming the user account's name is displayed on the top-left"
    platform_config:
      android_pkg: com.mymobileapp.android
```

If you are using a custom env-var for the password (i.e. other than `TESTPILOT_PASSWORD`) then you are
encouraged to specify the top-level `login.password` field as well. This helps Testpilot handle the
password string literal more securely.


# Testing Responsive Design with Viewports
Source: https://www.jetify.com/docs/docs/testpilot/guides/test-responsive-design

Ensure your site works across all screen sizes. Define and test multiple viewport dimensions for desktop, tablet, and mobile devices.

## Why Configure Viewports?[​](#why-configure-viewports "Direct link to Why Configure Viewports?")

Configuring viewports allows you to:

* Test responsive design across desktop, tablet, and mobile screen sizes
* Verify that UI elements appear correctly at different resolutions
* Ensure your application is usable on various devices
* Catch layout issues that only appear at specific dimensions

## Configuring Viewports in Your Pilot File[​](#configuring-viewports-in-your-pilot-file "Direct link to Configuring Viewports in Your Pilot File")

You can define viewports at the test case level using the `viewports` field. Here's how to set it
up:

```yaml  theme={null}
cases:
  - id: "responsive-test-001"
    name: "Homepage Responsive Test"
    description: "Verify the homepage displays correctly on multiple devices"
    url: "https://example.com"
    viewports:
      - name: "Desktop"
        size: [1920, 1080]
      - name: "Tablet"
        size: [768, 1024]
      - name: "Mobile"
        size: [375, 667]
    steps:
      - "Verify the navigation menu is visible"
      - "Verify the hero image is displayed properly"
      - "Scroll down to check content layout"
```

Each viewport configuration consists of:

* `name`: A descriptive name for the viewport (e.g., "Desktop", "Tablet", "Mobile")
* `size`: An array of two integers representing width and height in pixels

## How Testpilot Uses Viewports[​](#how-testpilot-uses-viewports "Direct link to How Testpilot Uses Viewports")

When you define multiple viewports for a test case, Testpilot will:

1. Run the test case once for each viewport configuration
2. Resize the browser window to match each viewport's dimensions before starting the test
3. Take screenshots and generate reports that show how your site appears at each size
4. Identify any issues specific to particular screen sizes

## Common Viewport Sizes[​](#common-viewport-sizes "Direct link to Common Viewport Sizes")

Here are some commonly used viewport sizes for different device categories:

### Desktop[​](#desktop "Direct link to Desktop")

```yaml  theme={null}
viewports:
  - name: "Desktop Large"
    size: [1920, 1080]
  - name: "Desktop Small"
    size: [1366, 768]
```

### Tablet[​](#tablet "Direct link to Tablet")

```yaml  theme={null}
viewports:
  - name: "Tablet Landscape"
    size: [1024, 768]
  - name: "Tablet Portrait"
    size: [768, 1024]
```

### Mobile[​](#mobile "Direct link to Mobile")

```yaml  theme={null}
viewports:
  - name: "Mobile Large"
    size: [428, 926]  # iPhone 13 Pro Max
  - name: "Mobile Medium"
    size: [390, 844]  # iPhone 13 Pro
  - name: "Mobile Small"
    size: [375, 667]  # iPhone SE
```

## Tips for Viewport Testing

1. **Start with key breakpoints**: Focus on testing the major breakpoints where your UI changes significantly
2. **Test critical user flows**: Ensure important user journeys work on all screen sizes
3. **Consider device-specific behaviors**: Some features might work differently on touch devices versus desktop
4. **Test orientation changes**: For tablet and mobile viewports, consider testing both portrait and landscape orientations
5. **Check for overflow issues**: Verify that content doesn't overflow or get cut off at smaller screen sizes

By thoroughly testing your application across different viewports, you can ensure a consistent and high-quality user experience for all your users, regardless of the device they're using.


# Testpilot: AI Powered End-to-End Testing
Source: https://www.jetify.com/docs/docs/testpilot/index

Testpilot is an AI testing agent that creates, maintains, and executes tests automatically. Test web and mobile apps with visual AI.

## What is Testpilot?[​](#what-is-testpilot "Direct link to What is Testpilot?")

Testpilot uses generative AI and image recognition to simulate real user interactions with your
applications. Unlike traditional testing frameworks that rely on brittle selectors or complex code,
Testpilot navigates your app visually, just like your users do.

Key features include:

* **No-code test creation**: Describe your test in plain English and Testpilot handles the rest
* **Visual testing**: Tests your app the way real users see it, not through code selectors
* **Intelligent Testing**: Automatically adapts to changes, pop-ups, and other flows that confuse
  traditional test automation.
* **Comprehensive reporting**: Visual reports with screenshots and videos of test runs
* **Cross-platform testing**: Works across web browsers, as well as Android and iOS apps

## How Testpilot Works[​](#how-testpilot-works "Direct link to How Testpilot Works")

Testpilot combines OpenAI's large language models with browser automation to create a testing system
that understands your application at a human level:

1. You describe test scenarios in simple YAML files called "pilot plans"
2. Testpilot interprets your test steps and translates them into actions
3. The AI agent navigates your app visually, taking screenshots to understand the UI
4. It executes the test steps, adapting to what it sees on screen
5. A detailed report is generated with screenshots, videos, and results

## Quick Links[​](#quick-links "Direct link to Quick Links")

Ready to get started with Testpilot? Check out these key resources:

* [Install Testpilot](/docs/testpilot/install) - Install Testpilot in minutes
* [Testing Web Apps](/docs/testpilot/getting-started/testing-web-apps) - Create and run browser-based
  tests
* [Testing Android Apps](/docs/testpilot/getting-started/testing-android-apps) - Test Android
  applications
* [Testing iOS Apps](/docs/testpilot/getting-started/testing-ios-apps) - Test iOS applications
* [GitLab Integration](/docs/testpilot/integrations/gitlab-cicd) - Run Testpilot in your CI/CD pipeline
* [Model Context Protocol](/docs/testpilot/model-context-protocol) - Provide Testpilot with tools and
  context for testing your application
* [Pilotfile Reference](/docs/testpilot/pilotfile-reference) - Learn the test file format
* [AI Test Generation](/docs/testpilot/ai-test-generation) - Let AI create tests for you

## Why Use Testpilot?[​](#why-use-testpilot "Direct link to Why Use Testpilot?")

Traditional testing approaches often suffer from:

* High maintenance costs as UIs change
* Brittle selectors that break easily
* Complicated setup and coding requirements
* Difficulty testing visual aspects of applications

Testpilot solves these problems by using AI to understand your application visually and adapt to
changes automatically. This results in more reliable tests that require less maintenance and can be
created without specialized testing knowledge.

Start exploring the documentation to see how Testpilot can transform your testing workflow!


# Install Testpilot
Source: https://www.jetify.com/docs/docs/testpilot/install

Install Testpilot in minutes. Set up the binary and configure your OpenAI API key to start running AI-powered tests.

## Step 1: Install the Testpilot Binary[​](#step-1-install-the-testpilot-binary "Direct link to Step 1: Install the Testpilot Binary")

Install Testpilot by running the following command in your terminal:

```bash  theme={null}
curl -fsSL https://get.jetify.com/testpilot | bash
```

This command downloads and installs the Testpilot binary on your system. After installation
completes, you'll be able to use the `testpilot` command.

## Step 2: Set Your OpenAI API Key[​](#step-2-set-your-openai-api-key "Direct link to Step 2: Set Your OpenAI API Key")

Testpilot uses OpenAI's API to generate and run tests. You'll need to set your OpenAI API key as an
environment variable:

```bash  theme={null}
export OPENAI_API_KEY=your-api-key-here
```

If you are using a proxy or a different provider for your OpenAI API, you can set the
`OPENAI_BASE_URL` environment variable to point to your API endpoint:

```bash  theme={null}
export OPENAI_BASE_URL=https://your-openai-api-endpoint.com
```

You can add this line to your shell profile (`.bashrc`, `.zshrc`, etc.) to make it persistent across
terminal sessions.

If you don't have an OpenAI API key yet, you can get one by:

1. Going to [OpenAI's platform](https://platform.openai.com/)
2. Creating an account or signing in
3. Navigating to the API keys section
4. Creating a new API key

That's it! With these two steps completed, you're ready to start using Testpilot to generate and run
tests for your projects.


# Testpilot GitLab CI/CD Integration
Source: https://www.jetify.com/docs/docs/testpilot/integrations/gitlab-cicd

Set up Testpilot in GitLab pipelines. Install the component, configure runners, and automate your tests with GitLab CI/CD.

You can check out an [example repo](https://gitlab.com/jetify-com/gitlab-components-example) with
our Gitlab integration for more details.

## Getting Started[​](#getting-started "Direct link to Getting Started")

### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before you begin, make sure you have:

* A GitLab project with CI/CD enabled
* At least one Testpilot test file (`.pilot.yaml`) in your repository
* Access to GitLab runners (SaaS or self-hosted)

### Step 1: Create Your First Pipeline[​](#step-1-create-your-first-pipeline "Direct link to Step 1: Create Your First Pipeline")

Let's start by creating a simple GitLab CI pipeline that installs Testpilot and runs a test. Create
or edit your `.gitlab-ci.yml` file in your project root:

```yaml  theme={null}
# Include the Testpilot component
include:
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install

# Define pipeline stages
stages:
  - install
  - test

# Your test job
run-my-tests:
  stage: test
  needs: ["testpilot-install-linux-amd64"]  # Wait for Testpilot installation
  script:
    - ./bin/testpilot test your_test.pilot.yaml  # Replace with your test file
  # preserve artifacts and reports
  artifacts:
    reports:
      junit: testpilot-out/*.xml
    paths:
      - testpilot-out
    when: always
    expire_in: 1 week
```

### Step 2: Commit and Run[​](#step-2-commit-and-run "Direct link to Step 2: Commit and Run")

Now that you have your pipeline defined, let's run it:

1. Save your `.gitlab-ci.yml` file
2. Commit and push to your GitLab repository
3. Navigate to your project's **CI/CD > Pipelines** section
4. Watch your pipeline run!

You should see two jobs:

* `testpilot-install-linux-amd64` - Downloads and sets up Testpilot
* `run-my-tests` - Runs your Testpilot tests

### Step 3: View your Artifacts[​](#step-3-view-your-artifacts "Direct link to Step 3: View your Artifacts")

The `artifacts` section of the job above will preserve a static report of your Testpilot tests,
including images and videos. You can view it by browsing to the `Artifacts` section of your Gitlab
project.

Testpilot also generates a JUnit report that can be directly reported to your merge requests

### Step 4: Understanding What Happened[​](#step-4-understanding-what-happened "Direct link to Step 4: Understanding What Happened")

The Testpilot component automatically:

* Downloaded the Testpilot installer
* Installed Testpilot and its dependencies (Playwright, Node.js)
* Created a `./bin/testpilot` launcher script
* Cached everything for faster future runs
* Made Testpilot available to your test job

## Platform-Specific Setup[​](#platform-specific-setup "Direct link to Platform-Specific Setup")

Testpilot supports running your tests on Linux and macOS runners. You can easily configure your
pipeline to handle both platforms:

### Setting Up for Linux (Default)[​](#setting-up-for-linux-default "Direct link to Setting Up for Linux (Default)")

The component works out-of-the-box with GitLab's standard Linux runners. No additional configuration
needed!

```yaml  theme={null}
include:
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install

stages:
  - install
  - test

run-tests:
  stage: test
  needs: ["testpilot-install-linux-amd64"]
  script:
    - ./bin/testpilot test your_test.pilot.yaml
```

### Setting Up for macOS[​](#setting-up-for-macos "Direct link to Setting Up for macOS")

Since macOS runners can't (currently) run Docker Images directly, they require a slightly different
setup. Here's how to configure your pipeline to use GitLab's SaaS macOS runners:

**Step 1:** Define your macOS runner configuration at the top of your `.gitlab-ci.yml`:

```yaml  theme={null}
# macOS runner configuration
.macos_saas_runners:
  tags:
    - saas-macos-medium-m1  # Use GitLab's SaaS macOS runners
```

**Step 2:** Include the component with macOS-specific settings:

```yaml  theme={null}
# Include the Testpilot component for macOS
include:
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install                # Install Testpilot in the 'install' stage
      platform: macos               # Target the macOS platform
      runner-extends: .macos_saas_runners  # Use the macOS SaaS runner config

# Define pipeline stages
stages:
  - install
  - test

# Run your tests on macOS
run-tests-macos:
  stage: test
  extends: .macos_saas_runners
  needs: ["testpilot-install-macos"]
  script:
    - ./bin/testpilot test your_test.pilot.yaml  # Replace with your test file
```

### Setting up Custom Runners[​](#setting-up-custom-runners "Direct link to Setting up Custom Runners")

If you're using self-hosted runners, you can configure Testpilot to run on them using a
configuration like the following

```yaml  theme={null}
# Custom runner configurations
.arm_runner:
  tags:
    # custom runner configuration goes here

include:
  # ARM64 runner
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install
      platform: linux-arm64
      runner-extends: .arm_runner

stages:
  - install
  - test

test-arm:
  stage: test
  extends: .arm_runner
  needs: ["testpilot-install-linux-arm64"]
  script:
    - ./bin/testpilot test tests/
```

## Multi-Platform Testing[​](#multi-platform-testing "Direct link to Multi-Platform Testing")

Want to test on both Linux and macOS? Here's how:

```yaml  theme={null}
# Runner configurations
.macos_saas_runners:
  tags:
    - saas-macos-medium-m1

# Install Testpilot on both platforms
include:
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install
      # platform: linux-amd64 is the default
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install
      platform: macos
      runner-extends: .macos_saas_runners

stages:
  - install
  - test

# Run tests on Linux
test-linux:
  stage: test
  needs: ["testpilot-install-linux-amd64"]
  script:
    - ./bin/testpilot test tests/

# Run tests on macOS
test-macos:
  stage: test
  extends: .macos_saas_runners
  needs: ["testpilot-install-macos"]
  script:
    - ./bin/testpilot test tests/
```

## Sharding your Tests and Running in Parallel[​](#sharding-your-tests-and-running-in-parallel "Direct link to Sharding your Tests and Running in Parallel")

Testpilot can shard your test files across multiple runners using the `--shard` flag, which is
useful for parallelizing and speeding up your test runs. Note that after sharding and running your
tests in parallel, you will probably want to merge the reports back together using
`testpilot report merge`.

You can see an example of sharding testpilot files in our
[example repo](https://gitlab.com/jetify-com/gitlab-components-example). An example gitlab.yaml file
is below:

```yaml  theme={null}
include:
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install
      xdg_cache_home: .cache/jetify

stages:
  - install
  - test
  - merge

testpilot-test:
  stage: test
  needs: ["testpilot-install-linux-amd64"]
  parallel: 2
  # Use built in CI_NODE environment variables to shard across runners
  script: ./bin/testpilot test --outdir=testpilot-out-${CI_NODE_INDEX} --shard=${CI_NODE_INDEX}/${CI_NODE_TOTAL} --reporters=junit
  artifacts:
    reports:
      junit: testpilot-out/*.xml
    paths:
      - testpilot-out-${CI_NODE_INDEX}/
    when: always
    expire_in: 1 week

# Merge your test reports together into a single artifact
testpilot_merge:
  stage: merge
  needs:
    - "testpilot-install-linux-amd64"
    - job: "testpilot-test"
      artifacts: true
      optional: true
  script: ./bin/testpilot report merge --outdir=testpilot-out testpilot-out-*
  artifacts:
    paths:
      - testpilot-out/
    when: always
    expire_in: 1 week
```

## Understanding the Component[​](#understanding-the-component "Direct link to Understanding the Component")

### Behind the Scenes[​](#behind-the-scenes "Direct link to Behind the Scenes")

When you include the Testpilot component, it creates a job that:

1. **Downloads the installer** from `https://get.jetify.com/testpilot`
2. **Installs Testpilot** and its dependencies (Playwright, Node.js)
3. **Creates a launcher script** at `./bin/testpilot` that handles environment setup
4. **Caches everything** so future pipeline runs are faster
5. **Shares the installation** with your test jobs via GitLab artifacts

### Component Configuration Options[​](#component-configuration-options "Direct link to Component Configuration Options")

The component accepts these parameters:

| Parameter        | Required | Default       | Description                         | Example                |
| ---------------- | -------- | ------------- | ----------------------------------- | ---------------------- |
| `stage`          | ✅ Yes    | -             | Which stage to install Testpilot in | `install`              |
| `platform`       | No       | `linux-amd64` | Target platform                     | `macos`, `linux-arm64` |
| `runner-extends` | No       | -             | Custom runner configuration         | `.macos_saas_runners`  |
| `xdg_cache_home` | No       | `.cache`      | Cache directory location            | `.custom_cache`        |

## Caching and Performance[​](#caching-and-performance "Direct link to Caching and Performance")

### Caching Strategy[​](#caching-strategy "Direct link to Caching Strategy")

The component automatically caches:

* The Testpilot binary and dependencies
* Your `./bin/testpilot` launcher script

This means the second time your pipeline runs, Testpilot installation will be much faster!

### Custom Cache Directory[​](#custom-cache-directory "Direct link to Custom Cache Directory")

If you need to change where files are cached:

```yaml  theme={null}
include:
  - component: gitlab.com/jetify-com/gitlab-components/testpilot-install@main
    inputs:
      stage: install
      xdg_cache_home: .my_custom_cache

run-tests:
  stage: test
  needs: ["testpilot-install-linux-amd64"]
  script:
    - ./bin/testpilot test tests/
```

## Best Practices Summary[​](#best-practices-summary "Direct link to Best Practices Summary")

✅ **Do:**

* Always use `needs:` to ensure proper job dependencies
* Leverage the built-in caching for faster pipelines
* Use descriptive job names that reflect what you're testing
* Test on multiple platforms if your application supports them
* Structure your tests in logical directories

❌ **Don't:**

* Forget to specify the correct job name in `needs:`
* Modify the cache directory unless necessary
* Run tests without waiting for the installation job
* Use the same job name for multiple platforms


# Testpilot CI/CD Integrations
Source: https://www.jetify.com/docs/docs/testpilot/integrations/index

Integrate Testpilot with your CI/CD pipeline. Set up automated testing in GitLab, GitHub Actions, and other platforms.

Testpilot integrates seamlessly with your existing CI/CD workflows, allowing you to run automated tests on every commit, pull request, or deployment. This helps catch regressions early and ensures your application works as expected before reaching production.

## What You'll Find Here

This section covers integrations with popular CI/CD platforms and development tools. You'll learn how to set up Testpilot in your pipeline, configure test execution, and manage test results.

<CardGroup cols={2}>
  <Card title="GitLab CI/CD Integration" icon="gitlab" href="/docs/testpilot/integrations/gitlab-cicd">
    Set up Testpilot in your GitLab pipelines with the official component.
  </Card>
</CardGroup>

<Note>
  Additional integrations for GitHub Actions, Jenkins, and other platforms are coming soon. For now, you can run Testpilot in any CI/CD environment that supports command-line tools.
</Note>

## Setting Up CI/CD Testing

When integrating Testpilot with your CI/CD pipeline, you'll typically:

1. Install Testpilot in your CI environment
2. Configure your API credentials as secrets
3. Run your test suite as part of your pipeline
4. Collect and publish test results

Each integration guide provides specific instructions for your platform.

## See Also

* [CLI Reference](/docs/testpilot/reference/cli) - Command-line options for running tests
* [Best Practices](/docs/testpilot/best-practices) - Tips for writing effective CI/CD tests


# Model Context Protocol (MCP) Integration
Source: https://www.jetify.com/docs/docs/testpilot/model-context-protocol

Extend Testpilot with MCP servers. Connect to internal APIs, custom scripts, and specialized tools to enhance testing capabilities.

## Adding a Server[​](#adding-a-server "Direct link to Adding a Server")

Use the `testpilot mcp add` command to register an MCP server for the current Git repository or
directory. To add a local server, pass the command that starts the server:

```bash  theme={null}
testpilot mcp add /path/to/mcp-server --flag arg
```

Testpilot will start the server and connect to it the next time you run `testpilot test`.

To add a remote server, pass the server URL:

```bash  theme={null}
testpilot mcp add https://mcp.example.com
```

If the server requires authentication, provide credentials as environment variables or HTTP headers
with the `--env` and `--header` flags. For example, you can pass an environment variable to a local
server:

```bash  theme={null}
testpilot mcp add --env API_KEY=SECRET /path/to/mcp-server
```

Or set an HTTP header for a remote server:

```bash  theme={null}
testpilot mcp add --header 'Authorization: Bearer $MY_TOKEN' https://mcp.example.com
```

Use single quotes to prevent your shell from expanding environment variables (like `$MY_TOKEN`
above). This prevents secrets from being written to the `.testpilot/mcp.json` config file. Testpilot
expands environment variables from the config file before connecting to a server.

See the [Environment Variables](#environment-variables) section for details.

## Configuration File[​](#configuration-file "Direct link to Configuration File")

MCP server configurations are stored in a `mcp.json` file that follows a schema similar to Claude
Code and other agents. The file location depends on whether you're running Testpilot in a Git
repository:

* **Git repos:** Testpilot searches for `.testpilot/mcp.json` starting from the current directory up
  to the repository root. If not found, it creates the file at `.testpilot/mcp.json` in the
  repository root.
* **Non-Git directories:** Testpilot searches for `.testpilot/mcp.json` starting from the current
  directory up through parent directories. If not found, it creates the file at
  `.testpilot/mcp.json` in the current directory.

You should commit the `.testpilot` directory to share MCP server configurations with your team and
use them in CI.

### Local Servers[​](#local-servers "Direct link to Local Servers")

Local servers are commands that Testpilot starts as separate processes. Testpilot communicates with
these servers through standard input/output.

```json  theme={null}
{
  "mcpServers": {
    "filesystem-server": {
      "command": "/path/to/mcp-server",
      "args": ["--verbose"],
      "env": {
        "FOO": "bar"
      }
    }
  }
}
```

If the `command` field contains no path separators ('/'), Testpilot searches for the command in your
`$PATH`. Otherwise, Testpilot launches the command directly from the specified path.

### Remote Servers[​](#remote-servers "Direct link to Remote Servers")

Remote servers communicate with Testpilot over HTTPS.

```json  theme={null}
{
  "mcpServers": {
    "api-server": {
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer $API_KEY"
      }
    }
  }
}
```

Remote servers typically require authentication since they're accessible over the internet. For
non-interactive environments like CI/CD, set credentials in HTTP headers by referencing environment
variables in the `mcp.json` file. The example above sets the `Authorization` header to the value of
the `API_KEY` environment variable.

### Environment Variables[​](#environment-variables "Direct link to Environment Variables")

Testpilot expands environment variables in the `command`, `args`, `env`, `url`, and `headers` fields
before connecting to a server. Use `$VAR` or `${VAR}` to reference environment variables.

Environment variables can also have default values with `${VAR:-default_value}`, where
`default_value` replaces `$VAR` when the variable is empty or unset. The example below uses the
`GH_MCP_SERVER` environment variable for the GitHub MCP server URL, with a fallback to the default
endpoint:

```json  theme={null}
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "${GH_MCP_SERVER:-https://api.githubcopilot.com/mcp/}",
      "headers": {
        "Authorization": "Bearer $GH_TOKEN"
      }
    }
  }
}
```

This configuration uses the default GitHub MCP server while allowing you to override it for specific
Testpilot runs. For example, you can restrict GitHub MCP permissions:

```bash  theme={null}
# Restrict GitHub MCP tools to read-only permissions.
GH_MCP_SERVER=https://api.githubcopilot.com/mcp/readonly testpilot test
```

All environment variables referenced in your MCP configuration must be set when Testpilot starts,
unless they include a default value using the `${VAR:-default}` syntax. If any required environment
variables are missing, Testpilot will fail at startup with an error indicating which variables need
to be set. This ensures your MCP servers receive the necessary credentials and configuration before
any tests run.


# Pilotfile Reference
Source: https://www.jetify.com/docs/docs/testpilot/pilotfile-reference

Complete reference for Testpilot pilot files. Learn the file format, configuration options, and test case structure.

```yaml  theme={null}
name: "My Test Suite"
login_url: "https://example.com/login"
context:
  - text: "Additional context for all test cases"
cases:
  - id: "test-001"
    name: "Login Test"
    description: "Test user login functionality"
    # ... additional test case fields
```

## Root Level Fields[​](#root-level-fields "Direct link to Root Level Fields")

### name[​](#name "Direct link to name")

An optional string that provides a human-readable name for the test suite. If not specified,
Testpilot will derive the name from the filename.

```yaml  theme={null}
name: "E-commerce Checkout Tests"
```

### login\_url[​](#login_url "Direct link to login_url")

An optional URL that specifies the login page for the application under test. When specified,
Testpilot will perform authentication before running test cases.

```yaml  theme={null}
login_url: "https://myapp.com/auth/login"
```

### context[​](#context "Direct link to context")

An optional array of context objects that provide additional information to all test cases in the
plan. This context is inherited by all test cases and can be used to provide background information
or setup details.

```yaml  theme={null}
context:
  - text: "This application requires users to be logged in"
  - text: "All tests assume a clean database state"
```

### cases[​](#cases "Direct link to cases")

An array of test case objects that define the individual tests to be executed. Each test case
represents a specific scenario or user journey to validate.

```yaml  theme={null}
cases:
  - id: "checkout-001"
    name: "Complete Purchase"
    # ... test case configuration
```

## Test Case Fields[​](#test-case-fields "Direct link to Test Case Fields")

Each test case in the `cases` array supports the following fields:

### id (required)[​](#id-required "Direct link to id (required)")

A unique identifier for the test case. This ID is used internally by Testpilot to track and
reference test cases.

```yaml  theme={null}
id: "login-success-001"
```

### name (required)[​](#name-required "Direct link to name (required)")

A human-readable name for the test case that describes what the test validates.

```yaml  theme={null}
name: "Successful User Login"
```

### description (required)[​](#description-required "Direct link to description (required)")

A detailed description of what the test case does and what it validates. This helps with test
documentation and debugging.

```yaml  theme={null}
description: "Verifies that a user can successfully log in with valid credentials"
```

### steps (required)[​](#steps-required "Direct link to steps (required)")

An array of strings that describe the steps to be performed during the test. Each step represents an
action or validation that should be performed.

```yaml  theme={null}
steps:
  - "Navigate to the login page"
  - "Enter valid username and password"
  - "Click the login button"
  - "Verify successful login redirect"
```

### url[​](#url "Direct link to url")

The URL where the test case should begin execution. This is the starting point for the test.

```yaml  theme={null}
url: "https://myapp.com/dashboard"
```

### viewports[​](#viewports "Direct link to viewports")

An array of viewport configurations that define the screen sizes at which the test should be
executed. This is useful for responsive testing across different device sizes.

```yaml  theme={null}
viewports:
  - name: "Desktop"
    size: [1920, 1080]
  - name: "Tablet"
    size: [768, 1024]
  - name: "Mobile"
    size: [375, 667]
```

Each viewport object contains:

* `name`: A descriptive name for the viewport
* `size`: An array of two integers representing width and height in pixels

### context[​](#context-1 "Direct link to context")

Test case-specific context that provides additional information for this particular test. This is
merged with any root-level context.

```yaml  theme={null}
context:
  - text: "This test requires a user with admin privileges"
  - text: "Database should contain sample product data"
```

### headers[​](#headers "Direct link to headers")

Custom HTTP headers to include in all browser requests for this test case. The
browser sends these headers with every request made during test execution.

```yaml  theme={null}
headers:
  X-Custom-Header: "custom-value"
  Token: "Bearer ${MY_TOKEN}"
  User-Agent: "TestPilot/1.0 Custom Agent"
```

**Important**: custom headers are only supported for web testing with
Playwright. They're currently not available when testing mobile applications on
Android or iOS platforms.

### platform\_config[​](#platform_config "Direct link to platform_config")

Configuration for testing on different platforms (web, mobile, etc.). This allows you to specify
different entry points for different platforms.

```yaml  theme={null}
platform_config:
  url: "https://web.myapp.com"
  android_pkg: "com.mycompany.myapp"
  ios_bundle: "com.mycompany.MyApp"
```

The platform configuration includes:

* `url`: The web URL for browser-based testing
* `android_pkg`: The Android package name for mobile app testing
* `ios_bundle`: The iOS bundle identifier for mobile app testing

## Context Objects[​](#context-objects "Direct link to Context Objects")

Context objects provide additional information that can be used by Testpilot during test execution.
Currently, only text-based context is supported.

```yaml  theme={null}
context:
  - text: "User should have completed onboarding"
```

Each context object contains:

* `text`: A string containing contextual information

## File Formats[​](#file-formats "Direct link to File Formats")

Testpilot supports multiple file formats for pilot files:

### YAML Format (Recommended)[​](#yaml-format-recommended "Direct link to YAML Format (Recommended)")

```yaml  theme={null}
name: "My Tests"
cases:
  - id: "test-001"
    name: "Sample Test"
    description: "A sample test case"
    steps:
      - "Step 1"
      - "Step 2"
```

### TOML Format[​](#toml-format "Direct link to TOML Format")

```toml  theme={null}
name = "My Tests"

[[cases]]
id = "test-001"
name = "Sample Test"
description = "A sample test case"
steps = ["Step 1", "Step 2"]
```

### JSON Format[​](#json-format "Direct link to JSON Format")

```json  theme={null}
{
  "name": "My Tests",
  "cases": [
    {
      "id": "test-001",
      "name": "Sample Test",
      "description": "A sample test case",
      "steps": ["Step 1", "Step 2"]
    }
  ]
}
```

## File Naming Conventions[​](#file-naming-conventions "Direct link to File Naming Conventions")

Testpilot recognizes pilot files with the following naming patterns:

* `*.pilot` - Basic pilot file
* `*.pilot.yaml` - YAML format pilot file
* `*.pilot.yml` - YAML format pilot file (alternative extension)
* `*.pilot.toml` - TOML format pilot file
* `*.pilot.json` - JSON format pilot file

## Remote Files[​](#remote-files "Direct link to Remote Files")

Testpilot can load pilot files from remote URLs, including GitHub repositories. When using GitHub
URLs, you can optionally set the `GITHUB_TOKEN` environment variable for authentication.

```bash  theme={null}
# Load from a direct URL
testpilot run https://example.com/tests/pilot.yaml

# Load from GitHub
testpilot run https://github.com/user/repo/raw/main/tests/pilot.yaml
```

## Example: E-commerce Testing Suite[​](#example-e-commerce-testing-suite "Direct link to Example: E-commerce Testing Suite")

Here's a complete example of a pilot file for testing an e-commerce application:

```yaml  theme={null}
name: "E-commerce Application Tests"
login_url: "https://shop.example.com/login"
context:
  - text: "Tests assume a clean database with sample products"
  - text: "Payment gateway is in test mode"
cases:
  - id: "product-search-001"
    name: "Product Search"
    description: "Verify users can search for products and view results"
    url: "https://shop.example.com"
    viewports:
      - name: "Desktop"
        size: [1920, 1080]
      - name: "Mobile"
        size: [375, 667]
    steps:
      - "Navigate to the homepage"
      - "Enter 'laptop' in the search box"
      - "Click the search button"
      - "Verify search results are displayed"
      - "Verify at least 3 products are shown"
    context:
      - text: "Search should return products from the electronics category"
  - id: "checkout-001"
    name: "Complete Checkout Process"
    description: "Test the full checkout flow from cart to payment"
    url: "https://shop.example.com/cart"
    steps:
      - "Add a product to cart"
      - "Navigate to checkout"
      - "Fill in shipping information"
      - "Select payment method"
      - "Complete purchase"
      - "Verify order confirmation"
    context:
      - text: "User must be logged in to complete checkout"
      - text: "Use test credit card: 4111111111111111"
  - id: "mobile-app-001"
    name: "Mobile App Login"
    description: "Test login functionality in mobile application"
    platform_config:
      url: "https://shop.example.com/mobile"
      android_pkg: "com.example.shop"
      ios_bundle: "com.example.Shop"
    steps:
      - "Launch the mobile application"
      - "Tap on login button"
      - "Enter valid credentials"
      - "Verify successful login"
    viewports:
      - name: "Mobile"
        size: [375, 667]
  - id: "api-integration-001"
    name: "Test API Integration"
    description: "Verify custom headers are sent correctly with requests"
    url: "https://shop.example.com/api-test"
    headers:
      X-Shop-Client: "testpilot"
      X-Test-Environment: "staging"
      Authorization: "Bearer test-token-123"
    steps:
      - "Navigate to the API integration test page"
      - "Verify custom headers are displayed in the response"
      - "Check that authentication header was processed correctly"
```

This example demonstrates:

* Root-level configuration with name, login URL, and context
* Multiple test cases with different purposes
* Cross-platform testing configuration
* Responsive testing with multiple viewports
* Test-specific context and configuration
* Custom HTTP headers for API integration testing


# Testpilot CLI Reference
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/index

Complete command-line reference for Testpilot. Learn all CLI commands, options, and flags for running and managing tests.

The Testpilot CLI provides powerful command-line tools for running tests, managing authentication,
and handling reports.

<CardGroup cols={2}>
  <Card title="testpilot" icon="terminal" href="/docs/testpilot/reference/cli/testpilot">
    Main CLI tool for AI-powered end-to-end testing.
  </Card>

  <Card title="testpilot auth" icon="key" href="/docs/testpilot/reference/cli/testpilot-auth">
    Manage your Testpilot account and authentication.
  </Card>

  <Card title="testpilot auth login" icon="log-in" href="/docs/testpilot/reference/cli/testpilot-auth-login">
    Log in to your Testpilot account.
  </Card>

  <Card title="testpilot auth logout" icon="log-out" href="/docs/testpilot/reference/cli/testpilot-auth-logout">
    Log out from your current session.
  </Card>

  <Card title="testpilot auth whoami" icon="user" href="/docs/testpilot/reference/cli/testpilot-auth-whoami">
    Display information about the current user.
  </Card>

  <Card title="testpilot generate" icon="sparkles" href="/docs/testpilot/reference/cli/testpilot-generate">
    Generate test plans from natural language descriptions.
  </Card>

  <Card title="testpilot install" icon="download" href="/docs/testpilot/reference/cli/testpilot-install">
    Download and install required dependencies.
  </Card>

  <Card title="testpilot report" icon="chart" href="/docs/testpilot/reference/cli/testpilot-report">
    View and manage test execution reports.
  </Card>

  <Card title="testpilot report merge" icon="merge" href="/docs/testpilot/reference/cli/testpilot-report-merge">
    Combine multiple test reports into a single report.
  </Card>

  <Card title="testpilot test" icon="play" href="/docs/testpilot/reference/cli/testpilot-test">
    Execute test scenarios from pilot plan files.
  </Card>

  <Card title="testpilot version" icon="tag" href="/docs/testpilot/reference/cli/testpilot-version">
    Check version information and update the CLI.
  </Card>

  <Card title="testpilot version update" icon="refresh-cw" href="/docs/testpilot/reference/cli/testpilot-version-update">
    Update the Testpilot launcher and binary to the latest version.
  </Card>
</CardGroup>

## Getting Help

* Use `testpilot --help` for general help
* Use `testpilot [command] --help` for command-specific help
* Check the [Getting Started](/docs/testpilot/getting-started/) section for tutorials
* Review the [Pilotfile Reference](/docs/testpilot/pilotfile-reference) for configuration
  options


# testpilot
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot

Testpilot CLI - AI-powered end-to-end testing tool

```bash  theme={null}
testpilot [flags]
```

## Options[​](#options "Direct link to Options")

| Option              | Description                                                            |
| ------------------- | ---------------------------------------------------------------------- |
| `-h, --help`        | help for testpilot                                                     |
| `-l, --logs string` | Show logs at level (one of: debug, info, warn, error) (default "info") |
| `-q, --quiet`       | Omit standard output                                                   |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot test](/docs/testpilot/reference/cli/testpilot-test) - Test the scenarios in the
  provided pilot plans
* [testpilot install](/docs/testpilot/reference/cli/testpilot-install) - Download and install
  dependencies
* [testpilot version](/docs/testpilot/reference/cli/testpilot-version) - Print version information
* [testpilot generate](/docs/testpilot/reference/cli/testpilot-generate) - Generate a pilot plan
  from a prompt
* [testpilot report](/docs/testpilot/reference/cli/testpilot-report) - Manage test reports


# testpilot auth
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-auth

Manage your account

```bash  theme={null}
testpilot auth [command]
```

## Available Commands[​](#available-commands "Direct link to Available Commands")

* [testpilot auth login](/docs/testpilot/reference/cli/testpilot-auth-login) - Log in to your
  account
* [testpilot auth logout](/docs/testpilot/reference/cli/testpilot-auth-logout) - Log out from your
  account
* [testpilot auth whoami](/docs/testpilot/reference/cli/testpilot-auth-whoami) - Show information
  about the current user

## Options[​](#options "Direct link to Options")

| Option       | Description   |
| ------------ | ------------- |
| `-h, --help` | help for auth |

## Global Options[​](#global-options "Direct link to Global Options")

| Option              | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| `-l, --logs string` | Show logs at level (one of: debug, info, warn, error) (default "ERROR") |
| `-q, --quiet`       | Omit standard output                                                    |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot auth login
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-auth-login

Log in to your account

```bash  theme={null}
testpilot auth login [flags]
```

## Description[​](#description "Direct link to Description")

The login command authenticates you with your Jetify Cloud or Google Workspace account, allowing you
to access Testpilot services and features that require authentication.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Log in to your account
testpilot auth login
```

## Options[​](#options "Direct link to Options")

| Option       | Description    |
| ------------ | -------------- |
| `-h, --help` | help for login |

## Global Options[​](#global-options "Direct link to Global Options")

| Option              | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| `-l, --logs string` | Show logs at level (one of: debug, info, warn, error) (default "ERROR") |
| `-q, --quiet`       | Omit standard output                                                    |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot auth](/docs/testpilot/reference/cli/testpilot-auth) - Manage your account
* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot auth logout
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-auth-logout

Log out from your account

```bash  theme={null}
testpilot auth logout [flags]
```

## Description[​](#description "Direct link to Description")

The logout command signs you out of your Testpilot account, removing stored authentication
credentials from your local system.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Log out from your account
testpilot auth logout
```

## Options[​](#options "Direct link to Options")

| Option       | Description     |
| ------------ | --------------- |
| `-h, --help` | help for logout |

## Global Options[​](#global-options "Direct link to Global Options")

| Option              | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| `-l, --logs string` | Show logs at level (one of: debug, info, warn, error) (default "ERROR") |
| `-q, --quiet`       | Omit standard output                                                    |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot auth](/docs/testpilot/reference/cli/testpilot-auth) - Manage your account
* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot auth whoami
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-auth-whoami

Show information about the current user

```bash  theme={null}
testpilot auth whoami [flags]
```

## Description[​](#description "Direct link to Description")

The whoami command displays information about the currently authenticated user, including user
details and optionally authentication tokens.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Show current user information
testpilot auth whoami

# Show user information including tokens
testpilot auth whoami --show-tokens
```

## Options[​](#options "Direct link to Options")

| Option              | Description                             |
| ------------------- | --------------------------------------- |
| `-h, --help`        | help for whoami                         |
| `-t, --show-tokens` | Show the access, id, and refresh tokens |

## Global Options[​](#global-options "Direct link to Global Options")

| Option              | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| `-l, --logs string` | Show logs at level (one of: debug, info, warn, error) (default "ERROR") |
| `-q, --quiet`       | Omit standard output                                                    |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot auth](/docs/testpilot/reference/cli/testpilot-auth) - Manage your account
* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot generate
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-generate

Generate a pilot plan from a prompt

```bash  theme={null}
testpilot generate [test prompt] [flags]
```

## Description[​](#description "Direct link to Description")

<Info>
  This feature is experimental. It may generate erroneous or incorrect tests, and you should review
  any tests before executing or checking them in.
</Info>

Generate a pilot plan from a prompt. The prompt should describe the functionality to be tested, and
the command will generate a pilot plan with multiple test cases. For best results, include the URL
of the application under test in the prompt, as well as the expected behavior and any specific
scenarios to cover.

You can also provide additional context by specifying one or more files using the `--context`
option. This is useful for providing API documentation, example tests, or other relevant information
that can help the AI generate more accurate test cases.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Generate a pilot plan for testing login functionality
testpilot generate "Test user login with valid and invalid credentials"

# Generate a plan with context from files
testpilot generate "Test checkout process" --context ./api-docs.md --context ./user-guide.md

# Generate a plan and save to a specific directory
testpilot generate "Test search functionality" --outdir ./tests/search
```

## Options[​](#options "Direct link to Options")

| Option              | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| `--context strings` | Path to a file containing context for pilot plan generation (can be specified multiple times) |
| `-h, --help`        | help for generate                                                                             |
| `--outdir string`   | Directory to write the generated pilot plan to                                                |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot install
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-install

Download and install dependencies

```bash  theme={null}
testpilot install [flags]
```

## Description[​](#description "Direct link to Description")

Download and install the dependencies required to run Testpilot tests. This command does nothing if
Testpilot is already installed unless --force is true.

You usually don't need to run this command explicitly. Testpilot automatically installs dependencies
on-demand when running tests. Use this command to pre-install dependencies when building container
images.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Install dependencies
testpilot install

# Force reinstall dependencies
testpilot install --force
```

## Options[​](#options "Direct link to Options")

| Option        | Description                                       |
| ------------- | ------------------------------------------------- |
| `-f, --force` | Reinstall and overwrite any existing installation |
| `-h, --help`  | help for install                                  |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot report
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-report

Manage test reports

```bash  theme={null}
testpilot report [command]
```

## Description[​](#description "Direct link to Description")

The report command provides utilities for managing Testpilot test reports.

## Available Commands[​](#available-commands "Direct link to Available Commands")

* [testpilot report merge](/docs/testpilot/reference/cli/testpilot-report-merge) - Merge multiple
  test reports into a single report

## Options[​](#options "Direct link to Options")

| Option       | Description     |
| ------------ | --------------- |
| `-h, --help` | help for report |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot report merge
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-report-merge

Merge multiple test reports into a single report

```bash  theme={null}
testpilot report merge <dir1> <dir2> [dir3...] [flags]
```

## Description[​](#description "Direct link to Description")

Merge multiple test reports from different directories into a single consolidated report. This is
useful when you have run tests in parallel or across different environments and want to combine the
results.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Merge two report directories
testpilot report merge ./reports1 ./reports2

# Merge multiple report directories
testpilot report merge ./reports1 ./reports2 ./reports3

# Merge reports and save to a custom output directory
testpilot report merge ./reports1 ./reports2 --outdir ./merged-reports
```

## Options[​](#options "Direct link to Options")

| Option            | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| `-h, --help`      | help for merge                                                         |
| `--outdir string` | Directory in which to save the merged report (default "testpilot-out") |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot report](/docs/testpilot/reference/cli/testpilot-report) - Manage test reports


# testpilot test
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-test

Test the scenarios in the provided pilot plans

```bash  theme={null}
testpilot test [path/to/plan.pilot.yaml | path/to/directory/with/pilot/plans] [flags]
```

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Run all tests in the current directory
testpilot test

# Run tests from a specific pilot plan file
testpilot test ./my-test.pilot.yaml

# Run tests from a specific directory
testpilot test ./tests/

# Run only tests with names containing "login"
testpilot test --filter login

# Run tests and save reports to a custom directory
testpilot test --outdir ./test-results

# Run tests in shard 1 of 3 total shards
testpilot test --shard 1/3
```

## Options[​](#options "Direct link to Options")

| Option                       | Description                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `-f, --filter string`        | only run tests with names containing the given string                                                                              |
| `-h, --help`                 | help for test                                                                                                                      |
| `--concurrency int`          | number of tests to run concurrently (default 10)                                                                                   |
| `--driver string`            | driver to use for the test (playwright or appium) (default "playwright")                                                           |
| --launch-vars stringToString | Environment variables passed when launching the application under test. Currently only applies to iOS apps and tests (default \[]) |
| `--os string`                | operating system to run tests on (local, linux, macos, windows) (default "local")                                                  |
| `--os-version string`        | operating system version to run tests on (e.g., "13", "18.3")                                                                      |
| `--outdir string`            | Directory in which to save reports (default "testpilot-out")                                                                       |
| `--runtime string`           | runtime environment to execute the test in (chromium, firefox, webkit, native) (default "chromium")                                |
| `--shard value`              | Split tests into n shards and only run tests in shard x                                                                            |
| `--udid value`               | specify the UDID of the iOS device you want to test. Note: this cannot be used along with `--os-version`                           |

## Advanced Options[​](#advanced-options "Direct link to Advanced Options")

The following options are available but not commonly used:

| Option            | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| `--show-browser`  | show the browser                                                       |
| `--viewport ints` | screen dimensions to use for your web browser (playwright driver only) |

## Environment Variables[​](#environment-variables "Direct link to Environment Variables")

The following environment variables are required or affect the behavior of the test command:

| Variable            | Required | Description                         |
| ------------------- | -------- | ----------------------------------- |
| `OPENAI_API_KEY`    | Yes      | OpenAI API key for LLM interactions |
| `ANTHROPIC_API_KEY` | No       | Anthropic API key (optional)        |
| `OPENAI_BASE_URL`   | No       | Custom OpenAI API base URL          |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI


# testpilot version
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-version

Print version information

```bash  theme={null}
testpilot version [flags]
```

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Print version number
testpilot version

# Print detailed version information
testpilot version --verbose
```

## Options[​](#options "Direct link to Options")

| Option          | Description                             |
| --------------- | --------------------------------------- |
| `-h, --help`    | help for version                        |
| `-v, --verbose` | displays additional version information |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot](/docs/testpilot/reference/cli/testpilot) - Testpilot CLI
* [testpilot version update](/docs/testpilot/reference/cli/testpilot-version-update) - Update
  launcher and binary


# testpilot version update
Source: https://www.jetify.com/docs/docs/testpilot/reference/cli/testpilot-version-update

Update launcher and binary

```bash  theme={null}
testpilot version update
```

## Description[​](#description "Direct link to Description")

Updates the Testpilot launcher and binary to the latest version.

## Examples[​](#examples "Direct link to Examples")

```bash  theme={null}
# Update Testpilot to the latest version
testpilot version update
```

## Options[​](#options "Direct link to Options")

| Option       | Description     |
| ------------ | --------------- |
| `-h, --help` | help for update |

## SEE ALSO[​](#see-also "Direct link to SEE ALSO")

* [testpilot version](/docs/testpilot/reference/cli/testpilot-version) - Print version information


