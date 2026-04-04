# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/embed-and-extend-pentaho-functionality-cp/multi-tenancy/data-multi-tenancy-and-supported-methods-multi-tenancy.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/embed-and-extend-pentaho-functionality-cp/multi-tenancy/data-multi-tenancy-and-supported-methods-multi-tenancy.md

# Data multi-tenancy and supported methods

The most common category of multi-tenancy is data multi-tenancy. Data multi-tenancy allows developers to apply their own custom data access rules at run time. For example, each tenant might only be allowed to see data which is associated with their tenant ID. Here are the most common methods for data multi-tenancy in Pentaho Business Analytics.

* **Sharding**

  Each tenant has its own database or schema. This approach has the advantage of controlling per database and ensuring data is separated. Note that with this approach, multiple databases and servers will need to be managed.
* **Striping**

  Tenants share a database, but the tables have a tenant ID column to indicate which tenant can see the specified data. This approach has the advantage of managing only a single database. Note that with this approach, databases can become very large.
* **Data Models**

  Tenancy is controlled at the data level where different tenants (or sub-tenants) are only able to see certain data. This approach is very flexible, but the data to restrict on must usually be known in advance.
* **Hybrid**

  Combinations of sharding, striping, and data model. Each of the approaches above can be combined into a single, flexible solution to data multi-tenancy.

Each database implementation has advantages and disadvantages, based on factors of performance management, maintenance, security, efficiency, available resources, and database vendor features. For best practices in database architecture, Pentaho recommends working with an expert in your chosen database and data modeling.

## Sharding data multi-tenancy

Sharding involves separating data by database or by database connection properties. The Pentaho Business Analytics platform manages access to database connections through a central mechanism called a data source. The platform delegates to the IDBDatasource object whenever a connection is requested to a given data source. Through Java code and Pentaho configuration files, developers can plug in their own object to apply rules at run time as shown in the following example.

#### Reference

IDBDatasourceService JavaDoc: <https://javadoc.pentaho.com/bi-platform102/pentaho-platform-api-10.2.0.0-218-javadoc/org/pentaho/platform/api/data/IDBDatasourceService.html>

## IDBDatasourceService implementation example

An IDBDatasourceService implementation uses two methods to modify the data source name: `getDataSource()` and `clearDataSource()`. The following code sample adds a tenant ID to the data source name. Adding the tenant ID allows the system to publish report definitions with a common data source name. At run time, the platform will use the dynamically created data source name.

```java
public class MyTenantedDatasourceService extends PooledOrJndiDatasourceService {
    @Override
    public DataSource getDataSource(String dsName) throws DBDatasourceServiceException {
        return super.getDataSource(modifyDsNameForTenancy(dsName));
    }
    @Override
    public void clearDataSource(String dsName) {
        super.clearDataSource(modifyDsNameForTenancy(dsName));
    }
    private String modifyDsNameForTenancy(String dsName){
        logger.debug("Original DSName is "+dsName);
        IPentahoSession session = PentahoSessionHolder.getSession();
        if (session == null) {
            logger.warn("Session is null; no modifications made to the JNDI dsName.");
            return dsName;
        }
        String tenantId = (String)session.getAttribute("tenantId");
        if (StringUtils.isEmpty(tenantId)){
            logger.warn("ID not found; no modifications made to the JNDI dsName.");
            return dsName;
        }
        String dsname = tenantId.concat("_").concat(dsName);
        logger.debug("New DSName is "+dsname);
        return dsname;
    }
}
```

## Configuring IDBDatasourceService

You must configure the class you want to use.

1. Place your compiled class or JAR file in the `webapps/pentaho/WEB-INF/lib` folder.
2. Modify `pentahoObjects.spring.xml` to point to your class name.

   ```xml
   <bean id="IDBDatasourceService" class="org.myorganization.MyTenantedDatasourceService" scope="singleton"/>
   ```
3. Restart the server for the configuration change to take effect.

## Using the data source

The following steps describe how the data source in this example is used at run time.

1. A report is published to Pentaho which refers to a JNDI data source called 'MyDataSource'.
2. A user with the tenant ID of 'CompanyA' runs a report.
3. The IDBDatasourceService appends the tenant ID to the data source name, resulting in 'MyDataSource\_CompanyA', and returns the connection.
4. The report is run using data from the 'MyDataSource\_CompanyA' connection.

The IDBDatasourceService interface can be used any time a connection uses either JNDI or Pentaho database-pooled connections. This approach works for reports generated with Report Designer, Analyzer, dashboards, data model-based reports, and action sequences using named data sources. Note that the IDBDatasource is implemented on the Pentaho Server and is not directly available to BA design tools, such asReport Designer and Schema Workbench.

**CAUTION:** If you are using only the IDBDatasourceService for multi-tenancy and also using Pentaho Analyzer, it is recommended that you have a DSP (see below) which will modify the Analyzer schema in a benign way, such as modifying the description. This is because the schema is used to determine caching. If only the IDBDatasourceService is used, it is possible for data from one tenant to be exposed to another tenant.

## Striping and data model multi-tenancy

Striping involves filtering tenant data within a single database connection. To allow a user to interactively query or navigate this data, access rules must exist between the user actions and the data. Data models provide a place to embed these access rules. Pentaho Business Analytics natively supports two types of data models: Pentaho Metadata and Analyzer schemas.

* Pentaho Metadata allows you to define business abstractions of relational database models. The Pentaho Metadata Editor and the Pentaho Data Source Wizard are used to build and set up data models. Pentaho Metadata is used by Pentaho Interactive Reports report files (`.prpti`) and can be used by Pentaho Report Designer report files (`.prpt`), dashboards, Pentaho Data Integration, and CTools dashboards.
* Analysis schemas define multi-dimensional data models. These schemas are created by Pentaho Schema Workbench, Data Source Wizard, and other parts of Pentaho software. Analyzer schemas can be used by Analyzer, Pentaho Report Designer reports (`.prpt`) and CTools dashboards.
