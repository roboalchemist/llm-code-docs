# Source: https://docs.streamlit.io/develop/concepts/architecture/app-chrome

# The app chrome

Your Streamlit app has a few widgets in the top right to help you as you develop. These widgets also help your viewers as they use your app. We call this things “the app chrome”. The chrome includes a status area, toolbar, and app menu.

Your app menu is configurable. By default, you can access developer options from the app menu when viewing an app locally or on Streamlit Community Cloud while logged into an account with administrative access. While viewing an app, click the icon in the upper-right corner to access the menu.

## Menu options

The menu is split into two sections. The upper section contains options available to all viewers and the lower section contains options for developers. Read more about [customizing this menu](#customize-the-menu) at the end of this page.

### Clear cache

Reset your app's cache by clicking "Clear cache" from the app's menu or by pressing "C" on your keyboard while not focused on an input element. This will remove all cached entries for `@st.cache_data` and `@st.cache_resource`.

### Deploy this app

If you are running an app locally from within a git repo, you can deploy your app to Streamlit Community Cloud in a few easy clicks! Make sure your work has been pushed to your online GitHub repository before beginning. For the greatest convenience, make sure you have already created your [Community Cloud account](/deploy/streamlit-community-cloud/get-started/create-your-account) and are signed in.

1. Click "Deploy" next to the app menu icon (more_vert).
2. Click "Deploy now".
3. You will be taken to Community Cloud's "Deploy an app" page. Your app's repository, branch, and file name will be prefilled to match your current app! Learn more about [deploying an app](/deploy/streamlit-community-cloud/deploy-your-app) on Streamlit Community Cloud.

The whole process looks like this:

## Customize the menu

Using `client.toolbarMode` in your app's [configuration](/develop/concepts/configuration), you can make the app menu appear in the following ways:

- `developer` — Show the developer options to all viewers.
- `viewer` — Hide the developer options from all viewers.
- `minimal` — Show only those options set externally. These options can be declared through [st.set_page_config](/develop/api-reference/configuration/st.set_page_config) or populated through Streamlit Community Cloud.
- `auto` — This is the default and will show the developer options when accessed through localhost or through Streamlit Community Cloud when logged into an administrative account for the app. Otherwise, the developer options will not show.