# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-submit-install.md

# Install Snowpark Submit

You can install Snowpark Submit to run batch-oriented Spark workloads directly on Snowflake’s infrastructure.

To install Snowpark Submit, complete the following steps:

1. Install Snowpark Submit by using `pip`.

   ```bash
   pip install snowpark-submit
   ```

2. In a [connections.toml](../python-connector/python-connector-connect.md) file for Snowflake authentication, add a Snowflake connection. If you already have a Snowflake connection, you can use that connection.

   If you don’t have a [connections.toml](../python-connector/python-connector-connect.md) file already, create one as described in [Connecting using the connections.toml file](../python-connector/python-connector-connect.md).

   Once you have a [connections.toml](../python-connector/python-connector-connect.md) file, you can add a Snowflake connection to it. For example, to add a Snowflake connection called `snowpark-submit`, add the following lines to the configuration file:

   ```toml
   [snowpark-submit]
   host = "<account>.snowflakecomputing.com"
   port = 443
   account = "<account>"
   user = "test_user"
   role = "test_role"
   password = "<password for user>"
   protocol = "https"
   warehouse = "test_warehouse"
   database = "test_db"
   schema = "test_schema"
   compute_pool = "test_compute_pool"
   ```

3. Verify that you can connect to Snowflake from your client computer.

   To verify that the connection works from your client computer, create a `.py` file with code that connects to Snowflake.

   1. Create a `connection_test.py` file, and then add the following code:

      ```python
      # connection_test.py code

      import sys
      import snowflake.connector

      conn_name = sys.argv[1]

      print(f"Trying connection named {conn_name}..")
      conn = snowflake.connector.connect(connection_name=conn_name)
      print("Connected.")

      cursor = conn.cursor()
      cursor.execute("SELECT 'Connection successful'")
      for col in cursor:
          print(col)

      print("\nListing first 5 tables:\n")
      cursor = conn.cursor()
      cursor.execute('show tables limit 5')
      for col in cursor:
          print(col)
      print("\nDone")
      ```

   2. From your active Python virtual environment, run the following command, specifying the name of the connection that you added to your
      `connections.toml` file.

      ```bash
      python connection_test.py snowpark-submit
      ```

Once you have verified that you can connect to Snowflake from your client computer, you can use Snowpark Submit to run batch-oriented Spark workloads directly on Snowflake’s infrastructure. See [Snowpark Submit reference](snowpark-submit-reference.md) for the Snowpark Submit command-line reference or [Snowpark Submit examples](snowpark-submit-examples.md) for examples of how to use Snowpark Submit.
