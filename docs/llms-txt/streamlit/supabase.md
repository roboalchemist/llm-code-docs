# Source: https://docs.streamlit.io/develop/tutorials/databases/supabase

# Connect Streamlit to Supabase

This guide explains how to securely access a Supabase instance from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection), [Streamlit Supabase Connector](https://github.com/SiddhantSadangi/st_supabase_connection/tree/main), and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). Supabase is the open source Firebase alternative and is based on PostgreSQL.

## Sign in to Supabase and create a project

First, head over to [Supabase](https://app.supabase.io/) and sign up for a free account using your GitHub.

Once you're signed in, you can create a project.

Your screen should look like this once your project has been created:

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `SUPABASE_URL` and `SUPABASE_KEY` here:

```toml
# .streamlit/secrets.toml

[connections.supabase]
SUPABASE_URL = "xxxx"
SUPABASE_KEY = "xxxx"
```

Replace `xxxx` above with your Project URL and API key from [Step 1](/develop/tutorials/databases/supabase#sign-in-to-supabase-and-create-a-project).

Add this file to `.gitignore` and don't commit it to your GitHub repo!

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add st-supabase-connection to your requirements file

If you prefer to use the [Supabase Python Client Library](https://pypi.org/project/supabase/) directly, you can do so by following the steps below.

1. Add your Supabase Project URL and API key to your local app secrets:

   Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `SUPABASE_URL` and `SUPABASE_KEY` here:

   ```toml
   # .streamlit/secrets.toml

   SUPABASE_URL = "xxxx"
   SUPABASE_KEY = "xxxx"
   ```

2. Add `supabase` to your requirements file:

   Add the [st-supabase-connection](https://github.com/supabase-community/supabase-py) Python Client Library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

   ```bash
   # requirements.txt
   supabase==x.x.x
   ```

3. Write your Streamlit app:

   Copy the code below to your Streamlit app and run it.

   ```python
   # streamlit_app.py

   import streamlit as st
   from st_supabase_connection import SupabaseConnection

   # Initialize connection.
   conn = st.connection("supabase", type=SupabaseConnection)

   # Perform query.
   rows = conn.query("*", table="mytable", ttl="10m").execute()

   # Print results.
   for row in rows.data:
       st.write(f"{row['name']} has a :{row['pet']}:")
   ```

   See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

   If everything worked out (and you used the example table we created above), your app should look like this:

   ![Finished app screenshot](/images/databases/supabase-10.png)

   As Supabase uses PostgresSQL under the hood, you can also connect to Supabase by using the connection string Supabase provides under Settings > Databases. From there, you can refer to the [PostgresSQL tutorial](/develop/tutorials/databases/postgresql) to connect to your database.

## Using the Supabase Python Client Library

If you prefer to use the [Supabase Python Client Library](https://pypi.org/project/supabase/) directly, you can do so by following the steps below.

1. Add your Supabase Project URL and API key to your local app secrets:

   Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the `SUPABASE_URL` and `SUPABASE_KEY` here:

   ```toml
   # .streamlit/secrets.toml

   SUPABASE_URL = "xxxx"
   SUPABASE_KEY = "xxxx"
   ```

2. Add `supabase` to your requirements file:

   Add the [st-supabase-connection](https://github.com/supabase-community/supabase-py) Python Client Library to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

   ```bash
   # requirements.txt
   supabase==x.x.x
   ```

3. Write your Streamlit app:

   Copy the code below to your Streamlit app and run it.

   ```python
   # streamlit_app.py

   import streamlit as st
   from supabase import create_client, Client

   # Initialize connection.
   # Uses st.cache_resource to only run once.
   @st.cache_resource
   def init_connection():
       url = st.secrets["SUPABASE_URL"]
       key = st.secrets["SUPABASE_KEY"]
       return create_client(url, key)

   supabase = init_connection()

   # Perform query.
   # Uses st.cache_data to only rerun when the query changes or after 10 min.
   @st.cache_data(ttl=600)
   def run_query():
       return supabase.table("mytable").select("*").execute()

   rows = run_query()

   # Print results.
   for row in rows.data:
       st.write(f"{row['name']} has a :{row['pet']}:")
   ```

   See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).