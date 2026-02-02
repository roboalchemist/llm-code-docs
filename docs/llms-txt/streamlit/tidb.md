# Connect Streamlit to TiDB

This guide explains how to securely access a **remote** TiDB database from Streamlit Community Cloud. It uses [st.connection](/develop/api-reference/connections/st.connection) and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management). The below example code will **only work on Streamlit version >= 1.28**, when `st.connection` was added.

## Sign in to TiDB Cloud and create a cluster

First, head over to [TiDB Cloud](https://tidbcloud.com/free-trial) and sign up for a free account, using either Google, GitHub, Microsoft or E-mail:

![Sign up TiDB Cloud](/images/databases/tidb-1.png)

Once you've signed in, you will already have a TiDB cluster:

![List clusters](/images/databases/tidb-2.png)

You can create more clusters if you want to. Click the cluster name to enter cluster overview page:

![Cluster overview](/images/databases/tidb-3.png)

Then click **Connect** to easily get the connection arguments to access the cluster. On the popup, click **Generate Password** to set the password.

![Get connection arguments](/images/databases/tidb-4.png)

Make sure to note down the password. It won't be available on TiDB Cloud after this step.

## Create a TiDB database

Your local Streamlit app will read secrets from a file `.streamlit/secrets.toml` in your app's root directory. Learn more about [Streamlit secrets management here](/develop/concepts/connections/secrets-management). Create this file if it doesn't exist yet and add host, username and password of your TiDB cluster as shown below:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
create_engine_kwargs = { connect_args = { ssl = { ca = "<path_to_CA_store>" }}}
```

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of **host**, **username** and **password** with those of your **remote** TiDB cluster!

## Add dependencies to your requirements file

Add the [mysqlclient](https://github.com/PyMySQL/mysqlclient) and [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) packages to your `requirements.txt` file, preferably pinning its version (replace `x.x.x` with the version you want installed):

```bash
# requirements.txt
mysqlclient==x.x.x
SQLAlchemy==x.x.x
```

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection('tidb', type='sql')

# Perform query.
df = conn.query('SELECT * from mytable;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
```

See `st.connection` above? This handles secrets retrieval, setup, query caching and retries. By default, `query()` results are cached without expiring. In this case, we set `ttl=600` to ensure the query result is cached for no longer than 10 minutes. You can also set `ttl=0` to disable caching. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)

## Connect with PyMySQL

Other than [mysqlclient](https://github.com/PyMySQL/mysqlclient), [PyMySQL](https://github.com/PyMySQL/PyMySQL) is another popular MySQL Python client. To use PyMySQL, first you need to adapt your requirements file:

```bash
# requirements.txt
PyMySQL==x.x.x
SQLAlchemy==x.x.x
```

Then adapt your secrets file:

```toml
# .streamlit/secrets.toml

[connections.tidb]
dialect = "mysql"
driver = "pymysql"
host = "<TiDB_cluster_host>"
port = 4000
database = "pets"
username = "<TiDB_cluster_user>"
password = "<TiDB_cluster_password>"
create_engine_kwargs = { connect_args = { ssl = { ca = "<path_to_CA_store>" }}}}
```