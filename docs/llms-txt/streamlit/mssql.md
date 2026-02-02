# Connect Streamlit to Microsoft SQL Server

This guide explains how to securely access a **remote** Microsoft SQL Server database from Streamlit Community Cloud. It uses the [pyodbc](https://github.com/mkleehammer/pyodbc/wiki) library and Streamlit's [Secrets management](/develop/concepts/connections/secrets-management).

## Create an SQL Server database

If you are connecting locally, use `sqlcmd` to connect to your new local SQL Server instance.

1. In your terminal, run the following command:
   ```bash
   sqlcmd -S localhost -U SA -P "<YourPassword>"
   ```
   As you are connecting locally, the SQL Server name is `localhost`, the username is `SA`, and the password is the one you provided during the SA account setup.

2. You should see a **sqlcmd** command prompt `1>`, if successful.

3. If you run into a connection failure, review Microsoft's connection troubleshooting recommendations for your OS (Linux & Windows).

## Add pyodbc to your requirements file

To connect to SQL Server locally with Streamlit, you need to `pip install pyodbc`, in addition to the Microsoft ODBC driver you installed during the SQL Server installation.

On Streamlit Cloud, we have built-in support for SQL Server. On popular demand, we directly added SQL Server tools including the ODBC drivers and the executables `sqlcmd` and `bcp` to the container image for Cloud apps, so you don't need to install them.

All you need to do is add the [pyodbc](https://github.com/mkleehammer/pyodbc) Python package to your `requirements.txt` file, and you're ready to go! 🎈

Replace `x.x.x` ☝️ with the version of pyodbc you want installed on Cloud.

When copying your app secrets to Streamlit Community Cloud, be sure to replace the values of `server`, `database`, `username`, and `password` with those of your **remote** SQL Server!

## Write your Streamlit app

Copy the code below to your Streamlit app and run it. Make sure to adapt `query` to use the name of your table.

```python
import streamlit as st
import pyodbc

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
```

See `st.cache_data` above? Without it, Streamlit would run the query every time the app reruns (e.g. on a widget interaction). With `st.cache_data`, it only runs when the query changes or after 10 minutes (that's what `ttl` is for). Watch out: If your database updates more frequently, you should adapt `ttl` or remove caching so viewers always see the latest data. Learn more in [Caching](/develop/concepts/architecture/caching).

If everything worked out (and you used the example table we created above), your app should look like this:

![Finished app screenshot](/images/databases/streamlit-app.png)