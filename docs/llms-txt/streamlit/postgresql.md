# Source: https://docs.streamlit.io/develop/tutorials/databases/postgresql

# Connect Streamlit to PostgreSQL

This guide explains how to securely access a **remote** PostgreSQL database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

## Create a PostgreSQL database

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Create this file if it doesn't exist yet and add the name, user, and password of your database as shown below:

```toml
# .streamlit/secrets.toml

[connections.postgresql]
dialect = "postgresql"
host = "localhost"
port = "5432"
database = "xxx"
username = "xxx"
password = "xxx"
```

## Copy your app secrets to the cloud

As the `secrets.toml` file above is not committed to GitHub, you need to pass its content to your deployed app (on Streamlit Community Cloud) separately. Go to the [app dashboard](https://share.streamlit.io/) and in the app's dropdown menu, click on **Edit Secrets**. Copy the content of `secrets.toml` into the text area. More information is available at [Secrets management](/deploy/streamlit-community-cloud/deploy-your-app/secrets-management).

![Secrets manager screenshot](/images/databases/edit-secrets.png)

## Add dependencies to your requirements file

Add the [psycopg2-binary](https://www.psycopg.org/) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
psycopg2-binary==x.x.x
sqlalchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM mytable;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl="10m"` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)