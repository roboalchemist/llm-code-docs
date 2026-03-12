# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-workloads-jupyter.md

# Run Spark workloads from VS Code, Jupyter Notebooks, or a terminal

You can run Spark workloads interactively from Jupyter Notebooks, VS Code, or any Python-based interface without needing to manage a
Spark cluster. The workloads run on the Snowflake infrastructure.

For example, you can do the following tasks:

1. Confirm that you have prerequisites.
2. Set up your environment to connect with Snowpark Connect for Spark on Snowflake.
3. Install Snowpark Connect for Spark.
4. Run PySpark code from your client to run on Snowflake.

## Prerequisites

Confirm that your Python and Java installations are based on the same computer architecture. For example, if Python is based is arm64, Java
must also be arm64 (not x86_64, for example).

## Set up your environment

You can set up your development environment by ensuring the your code can connect to Snowpark Connect for Spark on Snowflake. To connect to Snowflake
client code will use a `.toml` file containing connection details.

If you have Snowflake CLI installed, you can use it to define a connection. Otherwise, you can manually write connection parameters in a
`config.toml` file.

### Add a connection by using Snowflake CLI

You can use Snowflake CLI to add connection properties that Snowpark Connect for Spark can use to connect to Snowflake. Your changes are saved to a
`config.toml` file.

1. Run the following command to add a connection using the snow connection **add** command.

   ```snowcli
   snow connection add
   ```

2. Follow the prompts to define a connection.

   Be sure to specify `spark-connect` as the connection name.

   This command adds a connection to your `config.toml` file, as in the following example:

   ```toml
   [connections.spark-connect]
   host = "example.snowflakecomputing.com"
   port = 443
   account = "example"
   user = "test_example"
   password = "password"
   protocol = "https"
   warehouse = "example_wh"
   database = "example_db"
   schema = "public"
   ```

3. Run the following command to confirm that the connection works.

   You can test the connection in this way when you’ve added it by using Snowflake CLI.

   ```snowcli
   snow connection list
   snow connection test --connection spark-connect
   ```

### Add a connection by manually writing a connection file

You can manually write or update a `connections.toml` file so that your code can connect to Snowpark Connect for Spark on Snowflake.

1. Run the following command to ensure that your `connections.toml` file allows only the owner (user) to have read and write access.

   ```bash
   chmod 0600 "~/.snowflake/connections.toml"
   ```

2. Edit the `connections.toml` file so that it contains a `[spark-connect]` connection with the connection properties in the
   following example.

   Be sure to replace values with your own connection specifics.

   ```toml
   [spark-connect]
   host="my_snowflake_account.snowflakecomputing.com"
   account="my_snowflake_account"
   user="my_user"
   password="&&&&&&&&"
   warehouse="my_wh"
   database="my_db"
   schema="public"
   ```

### Install Snowpark Connect for Spark

You can install Snowpark Connect for Spark as a Python package.

1. Create a Python virtual environment.

   Confirm that your Python version is 3.10 or later and earlier than 3.13 by running `python3 --version`.

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the Snowpark Connect for Spark package.

   ```bash
   pip install --upgrade --force-reinstall 'snowpark-connect[jdk]'
   ```

3. Add Python code to start a Snowpark Connect for Spark server and create a Snowpark Connect for Spark session.

   ```python
   from snowflake import snowpark_connect
   spark=snowpark_connect.init_spark_session()
   ```

## Run Python code from your client

Once you have an authenticated connection in place, you can write code as you normally would.

You can run PySpark code that connects to Snowpark Connect for Spark by using the PySpark client library.

```python
# Row is imported in the previous code snippet

df = spark.createDataFrame([
    Row(a=1, b=2.),
    Row(a=2, b=3.),
    Row(a=4, b=5.),])

print(df.count())
```

## Run Scala code from your client

You can run Scala applications that connect to Snowpark Connect for Spark by using the Spark Connect client library.

This guide walks you through setting up Snowpark Connect and connecting your Scala applications to the Snowpark Connect for Spark server.

### Step 1: Set up your Snowpark Connect for Spark environment

Set up your environment by using steps described in the following topics:

1. Create a Python virtual environment and install Snowpark Connect.
2. Set up a connection.

### Step 2: Create a Snowpark Connect for Spark server script and launch the server

1. Create a Python script to launch the Snowpark Connect for Spark server.

   ```python
   # launch-snowpark-connect.py

   from snowflake import snowpark_connect

   def main():
       snowpark_connect.start_session(is_daemon=False, remote_url="sc://localhost:15002")
       print("SAS started on port 15002")

   if __name__ == "__main__":
       main()
   ```

2. Launch the Snowpark Connect for Spark server.

   ```python
   # Make sure you're in the correct Python environment
   pyenv activate your-snowpark-connect-env

   # Run the server script
   python launch-snowpark-connect.py
   ```

### Step 3: Set up your Scala application

1. Add the Spark Connect client dependency to your build.sbt file.

   ```scala
   libraryDependencies += "org.apache.spark" %% "spark-connect-client-jvm" % "3.5.6"

   // Add JVM options for Java 9+ module system compatibility
   javaOptions ++= Seq(
     "--add-opens=java.base/java.nio=ALL-UNNAMED"
   )
   ```

2. Execute Scala code to connect to the Snowpark Connect for Spark server.

   ```scala
   import org.apache.spark.sql.SparkSession
   import org.apache.spark.sql.connect.client.REPLClassDirMonitor

   object SnowparkConnectExample {
     def main(args: Array[String]): Unit = {
       // Create Spark session with Snowpark Connect
       val spark = SparkSession.builder().remote("sc://localhost:15002").getOrCreate()

       // Register ClassFinder for UDF support (if needed)
       // val classFinder = new REPLClassDirMonitor("target/scala-2.12/classes")
       // spark.registerClassFinder(classFinder)

       try {
         // Simple DataFrame operations
         import spark.implicits._

         val data = Seq(
           (1, "Alice", 25),
           (2, "Bob", 30),
           (3, "Charlie", 35)
         )

         val df = spark.createDataFrame(data).toDF("id", "name", "age")

         println("Original DataFrame:")
         df.show()

         println("Filtered DataFrame (age > 28):")
         df.filter($"age" > 28).show()

         println("Aggregated result:")
         df.groupBy().avg("age").show()

       } finally {
         spark.stop()
       }
     }
   }
   ```

3. Compile and run your application.

   ```bash
   # Compile your Scala application
   sbt compile

   # Run the application
   sbt "runMain SnowparkConnectExample"
   ```

### Scala UDF support on Snowpark Connect for Spark

When using user-defined functions or custom code, do one of the following:

* Register a class finder to monitor and upload class files.

  ```scala
  import org.apache.spark.sql.connect.client.REPLClassDirMonitor

  val classFinder = new REPLClassDirMonitor("/absolute/path/to/target/scala-2.12/classes")
  spark.registerClassFinder(classFinder)
  ```

* Upload JAR dependencies if needed. You can include the workload JAR itself if a class finder is not used.

  ```scala
  spark.addArtifact("/absolute/path/to/dependency.jar")
  ```

* Use a staged JAR.

  ```scala
  spark.conf.set("snowpark.connect.udf.java.imports", "[@mystage/dependency.jar, @db.schema.stage/other_dependency.jar]")
  ```

### Using Scala 2.13

By default, Snowpark Connect for Spark uses Scala 2.12. Workloads built with Scala 2.13 must specify the Scala version using the “snowpark.connect.scala.version” configuration option.

```scala
// Directly in the session builder
val spark = SparkSession.builder()
  .remote("sc://localhost:15002")
  .config("snowpark.connect.scala.version", "2.13")
  .getOrCreate()

// Or via session configuration
spark.conf.set("snowpark.connect.scala.version", "2.13")
```

### Troubleshoot Snowpark Connect for Spark installation

With the following list of checks, you can troubleshoot Snowpark Connect for Spark installation and use.

* Ensure that Java and Python are based on the same architecture.
* Use the most recent Snowpark Connect for Spark package file, as described in Install Snowpark Connect for Spark.
* Confirm that the **python** command with PySpark code is working correctly for local execution—that is, without Snowflake connectivity.

  For example, execute a command such as the following:

  ```python
  python your_pyspark_file.py
  ```

## Open source clients

You can use standard, off-the-shelf open source software (OSS) Spark client packages—such as PySpark and Spark clients for Java or
Scala—from your preferred local environments, including Jupyter Notebooks and VS Code. In this way, you can avoid installing packages
specific to Snowflake.

You might find this useful if you want to write Spark code locally and have the code use Snowflake compute resources and enterprise governance.
In this scenario, you perform authentication and authorization through programmatic access tokens (PATs).

The following sections cover installation, configuration, and authentication. You’ll also find a simple PySpark example to validate your
connection.

### Step 1: Install Required Packages

* Install `pyspark`. You don’t need to install any Snowflake packages.

  ```bash
  pip install "pyspark[connect]>=3.5.0,<4"
  ```

### Step 2: Setup and Authentication

1. Generate a programmatic access token (PAT).

   For more information, see the following topics:

   * [Using programmatic access tokens for authentication](../../user-guide/programmatic-access-tokens.md)
   * [ALTER USER … ADD PROGRAMMATIC ACCESS TOKEN (PAT)](../../sql-reference/sql/alter-user-add-programmatic-access-token.md)

   The following example adds a PAT named `TEST_PAT` for the user `sysadmin` and sets the expiration to 30 days.

   ```sqlexample
   ALTER USER add PAT TEST_PAT ROLE_RESTRICTION = sysadmin DAYS_TO_EXPIRY = 30;
   ```

2. Find your Snowflake Spark Connect host URL.

   Run the following SQL in Snowflake to find the hostname for your account:

   ```sqlexample
   SELECT t.VALUE:type::VARCHAR as type,
          t.VALUE:host::VARCHAR as host,
          t.VALUE:port as port
     FROM TABLE(FLATTEN(input => PARSE_JSON(SYSTEM$ALLOWLIST()))) AS t where type = 'SNOWPARK_CONNECT';
   ```

### Step 3: Connect to Spark Connect server

* To connect to the Spark Connect server, use code such as the following:

  ```python
  from pyspark.sql import SparkSession
  import urllib.parse

  # Replace with your actual PAT.
  pat = urllib.parse.quote("<pat>", safe="")

  # Replace with your Snowpark Connect host from the above SQL query.
  snowpark_connect_host = ""

  # Define database/schema/warehouse for executing your Spark session in Snowflake (recommended); otherwise, it will be resolved from your default_namespace and default_warehouse

  db_name = urllib.parse.quote("TESTDB", safe="")
  schema_name = urllib.parse.quote("TESTSCHEMA", safe="")
  warehouse_name = urllib.parse.quote("TESTWH", safe="")

  spark = SparkSession.builder.remote(f"sc://{snowpark_connect_host}/;token={pat};token_type=PAT;database={db_name};schema={schema_name};warehouse={warehouse_name}").getOrCreate()

  # Spark session is ready to use. You can write regular Spark DataFrame code, as in the following example:

  from pyspark.sql import Row

  df = spark.createDataFrame([
      Row(a=1, b=2.),
      Row(a=2, b=3.),
      Row(a=4, b=5.),])
  print(df.count())
  ```
