# Source: https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart

# Quickstart

This is a concise set of steps to create your Streamlit Community Cloud account, deploy a sample app, and start editing it with GitHub Codespaces. For other options and complete explanations, start with [Create your account](/deploy/streamlit-community-cloud/get-started/create-your-account).

## Prerequisites

- You must have a GitHub account.

## Sign up for Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io).
2. Click "Continue to sign-in".
3. Click "Continue with GitHub".
4. Enter your GitHub credentials and follow GitHub's authentication prompts.
5. Fill in your account information, and click "I accept" at the bottom.

## Add access to your public repositories

1. In the upper-left corner, click "Workspaces" warning.
2. From the drop down, click "Connect GitHub account".
3. Enter your GitHub credentials and follow GitHub's authentication prompts.
4. Click "Authorize streamlit".

## Create a new app from a template

1. In the upper-right corner, click "Create app".

   ```diff
   -st.title("🎈 My new app")
   +st.title("🎈 My new Streamlit app")
   ```

   Files are automatically saved in your codespace with each edit.

   A moment after typing a change, your app on the right side will display a rerun prompt. Click "Always rerun". If the rerun prompt disappears before you click it, you can hover over the overflow menu icon (more_vert) to bring it back.

   Optional: Continue to make edits and observe the changes within seconds.

## Publish your changes

1. In the left navigation bar, click the source control icon.

   ![See your deployed Streamlit app](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-source-control.png)

2. In the source control sidebar on the left, enter a name for your commit.

   ![See your deployed Streamlit app](/images/streamlit-community-cloud/deploy-template-blank-codespace-edit-commit.png)

3. To stage and commit all your changes, in the confirmation dialog, click "Yes". Your changes are committed locally in your codespace.

4. To push your commit to GitHub, in the source control sidebar on the left, click "cached 1 arrow_upward". To push commits to "origin/main", in the confirmation dialog, click "OK". Your changes are now saved to your GitHub repository. Community Cloud will immediately reflect the changes in your deployed app.

5. Optional: To see your updated, published app, return to the "My apps" section of your workspace at [share.streamlit.io](https://share.streamlit.io/) and click on your app.

## Stop or delete your codespace

When you stop interacting with your codespace, GitHub will generally stop your codespace for you. However, the surest way to avoid undesired use of your capacity is to stop or delete your codespace when you are done.

1. Go to [github.com/codespaces](https://github.com/codespaces). At the bottom of the page, all your codespaces are listed. Click the overflow menu icon (more_horiz) for your codespace.

   ![Stop or delete your GitHub Codespace](/images/streamlit-community-cloud/deploy-hello-codespace-manage.png)

2. If you want to return to your work later, click "Stop codespace". Otherwise, click "Delete".

   ![Stop your GitHub codespace](/images/streamlit-community-cloud/codespace-menu.png)

   Congratulations! You just deployed an app to Streamlit Community Cloud. 🎉 Return to your workspace at [share.streamlit.io](https://share.streamlit.io/) and [deploy another Streamlit app](/deploy/streamlit-community-cloud/deploy-your-app).