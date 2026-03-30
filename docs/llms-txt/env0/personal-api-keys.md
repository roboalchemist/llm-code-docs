# Source: https://docs.envzero.com/changelogs/2022/11/personal-api-keys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔑 Personal API Keys

> In addition to our web app, you can deploy and interact with env0 using any of these 3 major options:Terraform Provider, Directly invoking the API &Remote Backend. All of the mentioned options require an `API Key` to be passed so we will be able to authenticate, authorize and audit all the actions you do in env0. The most convenient approach to generating an API Key is to generate a `Personal API Key`. A `Personal API Key` is an API Key linked to your actual user. It is directly linked to your user account and therefore It will have the exact same permissions your user has and will share all of your user's details (such as your avatar and email address).

In addition to our web app, you can deploy and interact with env0 using any of these three major options - Terraform Provider, Directly invoking the API, and our Remote Backend. All of the mentioned options require an `API Key` to be passed so we can authenticate, authorize and audit all your actions in env0. The most convenient approach to generating an API Key is to generate a `Personal API Key`.

A `Personal API Key` is an API Key linked to your actual user. It is directly linked to your user account, and therefore it will have the same permissions your user has and will share all of your user's details (such as your avatar and email address).

## ✨ Generating a Personal API Key ✨

Generating a `Personal API Key` is fairly simple:

1. Click on your avatar in the top right corner
2. Click on `Personal Settings`

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/11/0aee9ff-screen_shot_2022-11-13_at_18.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=a31704b3d6c25094f37afedffd8e98cb" alt="Feature demonstration screenshot showing new functionality" width="364" height="151" data-path="images/changelogs/2022/11/0aee9ff-screen_shot_2022-11-13_at_18.png" />
</Frame>

1. Click on the `Personal API Keys` tab
2. Click on `Add Personal API Key` and insert a name for your key

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/11/1620c68-screen_shot_2022-11-17_at_15.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=4fb3b2e7719a2c4269830a1402f26bb5" alt="Feature demonstration screenshot showing new functionality" width="1427" height="409" data-path="images/changelogs/2022/11/1620c68-screen_shot_2022-11-17_at_15.png" />
</Frame>

1. Copy the values you need (either for the `API` / `Remote Backend` / `Terraform Provider`)

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/4i75qYgyhlssLgkA/images/changelogs/2022/11/866a969-screen_shot_2022-11-20_at_11.png?fit=max&auto=format&n=4i75qYgyhlssLgkA&q=85&s=8b7512e5686ea812b36098019cd945d6" alt="Feature demonstration screenshot showing new functionality" width="527" height="828" data-path="images/changelogs/2022/11/866a969-screen_shot_2022-11-20_at_11.png" />
</Frame>

> 👍 Personal API Key Permissions
>
> The generated `Personal API Key` will be coupled with your user. It will have the exact same permissions as the user that generated it (not only at the time of creation, it will keep updating as your permissions change).

Built with [Mintlify](https://mintlify.com).
