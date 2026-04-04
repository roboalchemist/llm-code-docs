# Source: https://docs.streamlit.io/develop/tutorials/authentication/microsoft

# Use Microsoft Entra to authenticate users

[Microsoft Identity Platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview) is a service within Microsoft Entra that lets you build applications to authenticate users. Your applications can use personal, work, and school accounts managed by Microsoft.

## Prerequisites

1. In your repository, create a `.streamlit/secrets.toml` file.
2. Add `secrets.toml` to your `.gitignore` file.
3. Generate a strong, random secret to use as your cookie secret.
4. In `.streamlit/secrets.toml`, add your connection configuration:
   ```toml
   [auth]
   redirect_uri = "http://localhost:8501/oauth2callback"
   cookie_secret = "xxx"
   client_id = "xxx"
   client_secret = "xxx"
   server_metadata_url = "https://login.microsoftonline.com/consumers/v2.0/.well-known/openid-configuration"
   ```
   Replace the values of `client_id`, `client_secret`, and `server_metadata_url` with the values you copied into your text editor earlier. Replace the value of `cookie_secret` with the random secret you generated in the previous step.
5. Save your `secrets.toml` file.
6. In your app, select "Always rerun", or press the "A" key.
7. Your preview will be blank but will automatically update as you save changes to `app.py`.
8. Return to your code.
9. Replace `st.user` with a personalized greeting:
   ```python
   else:
     st.header(f"Welcome, {st.user.name}")
   ```
10. Add a logout button:
    ```python
    st.button("Log out", on_click=st.logout)
    ```
11. Save your `app.py` file and test your running app.
12. In your live preview, if you log out of your app, it will return to the login prompt.

## Deploy your app on Community Cloud

When you are ready to deploy your app, you must update your application in Microsoft Azure and your secrets. The following steps describe how to deploy your app on Community Cloud.

1. Add a `requirements.txt` file to your repository with the following lines:
   ```txt
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `requirements.txt` file.
3. Deploy your app, and copy your app's URL into your text editor.
4. In your `app settings` in Community Cloud, select "Secrets".
5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.
6. Change your `redirect_uri` to reflect your deployed app's URL.
7. Save and close your settings.
8. Return to your application in Microsoft Azure.
9. If you've closed Microsoft Azure and need to navigate back to your application, go to your Azure portal → Microsoft Entra ID → App registrations, and select it from the list.
10. In the left navigation, select "Authentication".
11. Under "Platform configurations" → "Web", add or update a URI to match your new `redirect_uri`.
12. At the bottom of the page, select "Save".
13. Open your deployed app, and test it.