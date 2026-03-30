# Source: https://docs.acceldata.io/documentation/oracle.md

# Oracle

Integrate **Oracle Database** with **Acceldata Data Observability Cloud (ADOC)** to ensure end-to-end data reliability and observability across your Oracle ecosystem.

Oracle Database is a leading relational database management system (RDBMS) used for enterprise-scale data storage and processing. Integrating Oracle with ADOC enables organizations to gain visibility into data health, performance, and reliability. Once configured, ADOC continuously monitors data quality and operational metrics from your Oracle instances.

---

## Supported Versions

ADOC supports integration with Oracle Database (both Standalone and Oracle Cloud Autonomous Database environments).

| Component | Supported Versions | 
| ---- | ---- | 
| Oracle Database | Oracle Database 21c Enterprise Edition Release 21.0.0.0.0 – Production&lt;br&gt;Version 21.3.0.0.0 | 
| Oracle Cloud Autonomous Database (ADB) | Supported | 


> Ensure your Oracle instance is reachable through the configured JDBC connection before integration.

---

## Supported Authentication Methods

| Authentication Type | Description | 
| ---- | ---- | 
| **Username/Password** | Standard authentication using Oracle database credentials. | 
| **Wallet-based Authentication (for Oracle ADB)** | Uses Oracle Cloud wallet credentials for secure access. | 


---

## Prerequisites and Permissions

Before connecting Oracle to ADOC, ensure the following prerequisites are met:

1. You have an existing or newly created **Data Plane** in ADOC. See [Data Plane Installation Guide](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) for setup instructions.
2. The Oracle user account used for integration must have the following permissions:

```bash
GRANT SELECT ANY DICTIONARY TO <ORACLE_USER>;;
GRANT SELECT_CATALOG_ROLE TO <ORACLE_USER>;;
```



    Replace &lt;ORACLE_USER&gt; with your Oracle username. Contact your DBA if additional privileges are required.

3. You have the following **Oracle connection details** ready:
    - JDBC URL (for example, `jdbc:oracle:thin:@<HOST>:<PORT>/<SERVICE_NAME>`)
    - Username and password
    - (Optional) Wallet credentials for Oracle Cloud ADB

---

## Configuration Parameters

The following configuration parameters are required when adding Oracle as a data source:

| Parameter | Description | Mandatory | Example | 
| ---- | ---- | ---- | ---- | 
| **Data Source Name** | Unique name for the Oracle connection. | ✅ | `Oracle-Prod-DB` | 
| **Description** | Optional notes about the data source. | ❌ | `Production Oracle data source` | 
| **Data Plane** | Select the Data Plane to be used for observability. | ✅ | `dp-west-us` | 
| **JDBC URL** | Oracle JDBC connection string. | ✅ | `jdbc:oracle:thin:@mydb.us-east-1.oraclecloud.com:1521/ORCLPDB1` | 
| **JDBC Username** | Oracle database username. | ✅ | `adoc_user` | 
| **JDBC Password** | Oracle database password. | ✅ |  | 
| **Wallet Credentials (ADB only)** | Credential zip file for Oracle Cloud ADB. | ⚙️ Required for ADB | `/path/to/wallet.zip` | 
| **Database Name(s)** | List of Oracle databases to monitor. | ✅ | `HRDB, SALESDB` | 
| **Crawler Execution Schedule** | Time and frequency for data crawler jobs. | Optional | `Daily 12:00 UTC` | 


---

## Adding Oracle as a Data Source

Follow these steps to integrate Oracle Database with ADOC:

1. Navigate to the **Register** page from the left main navigation menu.
2. Click **Add Data Source** under the **Data Sources** tab.
3. Choose **Oracle** from the list of supported data sources.
4. Fill in the **Data Source Details**:
    1. Enter a name and optional description.
    2. Ensure the **Data Reliability** toggle is enabled.
    3. Select an existing or create a new **Data Plane**.

5. Click **Next** to configure **Connection Details**.
6. Choose your **Oracle Environment Type**:
    - **Standalone**: Enter JDBC URL, username, and password.
    - **Oracle Cloud ADB:** Provide JDBC URL, credentials, and upload wallet files.

7. Click **Test Connection** to verify connectivity.
8. On the **Set Up Observability** page:
    1. Enter one or more database names to monitor.
    2. (Optional) Enable **Crawler Execution Schedule** and set a preferred frequency.

9. Click **Submit** to complete setup.

Once completed, an Oracle card appears in the Data Sources page, showing key statistics such as connection health, crawler status, and monthly cost.

---

## Troubleshooting

### Issue: Cadence Jobs Failing with `ORA-00942` (Table or View Does Not Exist)

**Possible Cause:** The Oracle user does not have required permissions to access metadata tables.

**Solution:** Ensure the Oracle user is granted the following permissions:

```sql
GRANT SELECT ANY DICTIONARY TO <ORACLE_USER>;
GRANT SELECT_CATALOG_ROLE TO <ORACLE_USER>;
```



Replace `<ORACLE_USER>` with the user specified during configuration.

---

## Next Steps

Explore the [Data Reliability](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/advanced) module for detailed monitoring options.