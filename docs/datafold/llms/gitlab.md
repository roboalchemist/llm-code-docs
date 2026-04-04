# Source: https://docs.datafold.com/integrations/code-repositories/gitlab.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GitLab

To get the [project access token](https://docs.gitlab.com/ee/user/project/settings/project%5Faccess%5Ftokens.html), navigate to your GitLab project settings and create a new token.

<Tip>
  **TIP**

  Project access tokens are preferred over personal tokens for security.
</Tip>

When configuring your token, select the **Maintainer** role and select the **api** scope.

<Frame caption="GitLab Access Token">
  <img src="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=3b4f13fecd884a73f79fc5f29ed635d0" data-og-width="1541" width="1541" data-og-height="970" height="970" data-path="images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=280&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=e14c77bfa9c922fe95bf31ca0816daa5 280w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=560&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=49cafe904b45ca280c0277eaae1990f9 560w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=840&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=415d7a83e6355e9af220a0b29301c702 840w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=1100&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=921ef53fc15fc1f17c35dcc0beb58e8a 1100w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=1650&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=5b2ef6941943b34a7149dfa897643ab1 1650w, https://mintcdn.com/datafold/6zQ11m2yiOVjYXTT/images/gitlab_access_token-3c34d99f464332fd5e1a3dc672c89d36.png?w=2500&fit=max&auto=format&n=6zQ11m2yiOVjYXTT&q=85&s=f92882e757e73d4396d4dba68b5eb700 2500w" />
</Frame>

**Project Name** is your Gitlab project URL after `gitlab.com/`. For example, if your Gitlab project URL is `https://gitlab.com/datafold/dbt/`, your Project Name is `datafold/dbt/`

Finally, navigate back to Datafold and enter the **Project Token** and the name of your **Project** before hitting **Save**:

<Frame caption="New GitLab Integration in Datafold">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1c65ed01289e60b48693cca20d5e9d75" data-og-width="897" width="897" data-og-height="423" height="423" data-path="images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=542c25d2b59aa6f014e80327300c85f9 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=9586ccb24ce5515ac01d1ec30bbca3ec 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=ef74c6101145fc1fb404dce3769b286f 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a8572ad991d2ff8989fd8ca64f09521f 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a37dde70dedfc2cb91012079968455f0 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_new_integration-556436f49dbd3ab4da5448a17540abd9.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=a9998b17350a04b42154524cd793d8b3 2500w" />
</Frame>

If you want to change the GitLab URL, you can do so after setting up the integration. To do so, navigate to **Settings**, then **Org Settings**:

<Frame caption="Change GitLab URL">
  <img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=bcfd8113d0beecd9fc51341f22ce3c8b" data-og-width="1058" width="1058" data-og-height="819" height="819" data-path="images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=33418eb4e8b420075d4bbb4ce3c3a0a2 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f31735ff0fe22efda30df333e113f09c 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=29d5e7a86c9de7e402ef9280f26c52b2 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=95df988be241f25cfd157960193515da 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=43560ac997f5146c34681ca6a9c0a1d5 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data_app_gitlab_change_url-f8ee1e8babed20cf8cb78318526d9f3e.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=84ffdd694df48e54815ec8bcdc34a9e6 2500w" />
</Frame>
