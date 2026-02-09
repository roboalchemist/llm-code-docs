# Source: https://docs.sandboxes.cloud/docs/login.md

# Login

A user's main identity on Crafting Platform is his/her email address, typically work email address. For Crafting SaaS users, you can login at [https://sandboxes.cloud](https://sandboxes.cloud) for Crafting Self-hosted, you can login with your custom URL that is specific to your site.

To get an account, you can ask for an invitation from your organization's administrator. Your administrator can also choose to use domain-based account setup where all users from a certain domain will automatically create an account upon first time login.

<Image align="center" width="80% " src="https://files.readme.io/8cfd52d-user-guide-login.JPG" />

## Login with Google Single-Sign-On (SSO)

The main login method we provide is Google SSO. If your organization is using [Google Workspace](https://workspace.google.com/) (previously known as G Suite), you can simply login use your work email. Or if you have a trial account with us based on your Gmail address, it should work directly.

## Login with GitHub

You can also login with GitHub identity, in which case, your email address needs to be associated with your GitHub account and listed as "Public email". You can adjust see the setting at your GitHub [profile page](https://github.com/settings/profile) as follows.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/1ce58d9-GitHubPublic.PNG" />

## Where Login is Needed Other than Accessing Web Console

A few other cases you will need to login in to authenticate yourself:

* When you access an endpoint for a sandbox that is not made public to the Internet, you will need to authenticate yourself just like accessing the web console.
* When you first time use CLI from your local machine, you will be prompt to login and authenticate yourself

> 🚧 Password Login
>
> For security reasons, we currently do not support password-based authentication. Please contact us at [contact@crafting.dev](mailto:contact@crafting.dev) to talk about your specific case.