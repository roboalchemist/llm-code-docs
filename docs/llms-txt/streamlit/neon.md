# Source: https://docs.streamlit.io/develop/tutorials/databases/neon

# Connect Streamlit to Neon

This guide explains how to securely access a [Neon database](https://neon.tech/) from Streamlit. Neon is a fully managed serverless PostgreSQL database that separates storage and compute to offer features such as instant branching and automatic scaling.

## Prerequisites

- The following packages must be installed in your Python environment:
  ```txt
  streamlit>=1.28
  psycopg2-binary>=2.9.6
  sqlalchemy>=2.0.0
  ```
- You must have a Neon account.
- You should have a basic understanding of [st.connection](https://docs.streamlit.io/develop/api-reference/connections/st.connection) and [Secrets management](https://docs.streamlit.io/develop/concepts/connections/secrets-management).

## Create a Neon project

If you already have a Neon project that you want to use, you can [skip to the next step](#add-neon-connection-string-to-your-local-app-secrets).

1. Log in to the Neon console and navigate to the [Projects](https://console.neon.tech/app/projects) section.
2. If you see a prompt to enter your project name, skip to the next step. Otherwise, click the "New Project" button to create a new project.
3. Enter "Streamlit-Neon" for your project name, accept the other default settings, and click "Create Project".
4. After Neon creates your project with a ready-to-use `neondb` database, you will be redirected to your project's Quickstart.

## Add the Neon connection string to your local app secrets

1. Within your Neon project, click "Dashboard" in the left sidebar.
2. Within the "Connection Details" tile, locate your database connection string. It should look similar to this:
   ```bash
   postgresql://neondb_owner:xxxxxxxxxxxx@ep-adjective-noun-xxxxxxxx.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```
3. If you do not already have a `.streamlit/secrets.toml` file in your app's root directory, create an empty secrets file.
4. Copy your connection string and add it to your app's `.streamlit/secrets.toml` file as follows:
   ```toml
   # .streamlit/secrets.toml

   [connections.neon]
   url="postgresql://neondb_owner:xxxxxxxxxxxx@ep-adjective-noun-xxxxxxxx.us-east-2.aws.neon.tech/neondb?sslmode=require"
   ```
   Add this file to `.gitignore` and don't commit it to your GitHub repo!

## Write your Streamlit app

1. Copy the code below to your Streamlit app and save it.
   ```python
   # streamlit_app.py

   import streamlit as st

   # Initialize connection.
   conn = st.connection("neon", type="sql")

   # Perform query.
   df = conn.query('SELECT * FROM home;', ttl="10m")

   # Print results.
   for row in df.itertuples():
       st.write(f"{row.name} has a :{row.pet}:")
   ```

   The `st.connection` object above handles secrets retrieval, setup, query caching and retries.

   By default, `query()` results are cached without expiring. Setting the `ttl` parameter to `"10m"` ensures the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](https://docs.streamlit.io/develop/concepts/architecture/caching).

2. Run your Streamlit app.
   ```bash
   streamlit run streamlit_app.py
   ```

   If everything worked out (and you used the example table we created above), your app should look like this:

   ![Finished app screenshot](https://docs.streamlit.io/images/databases/streamlit-app.png)