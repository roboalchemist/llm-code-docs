# Use the Google Auth Platform to authenticate users

Google is one of the most popular identity providers for social logins. You can use the Google Auth Platform with both private and organizational Google accounts. This tutorial configures authentication for anyone with a Google account. For more information, see Google's overview of the [Google Auth Platform](https://support.google.com/cloud/topic/15540269?hl=en&ref_topic=3473162&sjid=576431444945556851-NC) and [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect#discovery).

## Prerequisites

- This tutorial requires the following Python libraries:
  ```text
  streamlit>=1.42.0
  Authlib>=1.3.2
  ```
- You should have a clean working directory called `your-repository`.
- You must have a Google account and accept the terms of [Google Cloud](https://console.cloud.google.com/) to use their authentication service.
- You must have a project in Google Cloud within which to create your application. For more information about managing your projects in Google Cloud, see [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in Google's documentation.

## Summary

In this tutorial, you'll build an app that users can log in to with their Google accounts. When they log in, they'll see a personalized greeting with their name and have the option to log out.

Here's a look at what you'll build:

```text
. streamlit/secrets.toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "xxx"
client_id = "xxx"
client_secret = "xxx"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

```python
import streamlit as st

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)

if not st.user.is_logged_in:
    login_screen()
else:
    st.header(f"Welcome, {st.user.name}")
    st.button("Log out", on_click=st.logout)
```

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Deploy your app on Community Cloud

When you are ready to deploy your app, you must update your application on Google Cloud and your secrets. The following steps describe how to deploy your app on Community Cloud.

1. Add a `requirements.txt` file to your repository with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `requirements.txt` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community-cloud/deploy-your-app).

4. In your `app settings` in Community Cloud, select "Secrets".

5. Copy the contents of your local `secrets.toml` file, and paste them into your app settings.

6. Change your `redirect_uri` to reflect your deployed app's URL, which you copied earlier in this tutorial.

7. Save and close your settings.

8. Return to the clients page in the Google Auth Platform, and select your client.

9. Under "Authorized redirect URIs", add or update a URI to match your new `redirect_uri`.

10. At the bottom of the page, select "SAVE".

11. Open your deployed app, and test it.

Your Google Cloud application's status is still `Testing`. You should be able to log in and out of your app with the personal Google account you entered on the "Audience" page.

## Configure your secrets

1. In `your_repository`, create a `secrets.toml` file with the following lines:
   ```text
   streamlit>=1.42.0
   Authlib>=1.3.2
   ```
2. Save your `secrets.toml` file.

3. Deploy your app, and copy your app's URL into your text editor.

You'll use your app's URL to update your secrets and client configuration in the following steps. For more information about deploying an app on Community Cloud, see [Deploy your app](https://docs.streamlit.io/develop/deploy/streamlit-community