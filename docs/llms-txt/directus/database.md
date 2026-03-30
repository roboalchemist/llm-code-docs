# Source: https://directus.io/docs/raw/configuration/database.md

# Database

> Configuration for database connections.

<partial content="config-env-vars">



</partial>

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        DB_CLIENT
      </code>
    </td>
    
    <td>
      <strong>
        Required
      </strong>
      
      . What database client to use. One of <code>
        pg
      </code>
      
       or <code>
        postgres
      </code>
      
      , <code>
        mysql
      </code>
      
      , <code>
        oracledb
      </code>
      
      , <code>
        mssql
      </code>
      
      , <code>
        sqlite3
      </code>
      
      , <code>
        cockroachdb
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_HOST
      </code>
    </td>
    
    <td>
      Database host. Required when using <code>
        pg
      </code>
      
      , <code>
        mysql
      </code>
      
      , <code>
        oracledb
      </code>
      
      , or <code>
        mssql
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_PORT
      </code>
    </td>
    
    <td>
      Database port. Required when using <code>
        pg
      </code>
      
      , <code>
        mysql
      </code>
      
      , <code>
        oracledb
      </code>
      
      , or <code>
        mssql
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_DATABASE
      </code>
    </td>
    
    <td>
      Database name. Required when using <code>
        pg
      </code>
      
      , <code>
        mysql
      </code>
      
      , <code>
        oracledb
      </code>
      
      , or <code>
        mssql
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_USER
      </code>
    </td>
    
    <td>
      Database user. Required when using <code>
        pg
      </code>
      
      , <code>
        mysql
      </code>
      
      , <code>
        oracledb
      </code>
      
      , or <code>
        mssql
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_PASSWORD
      </code>
    </td>
    
    <td>
      Database user's password. Required when using <code>
        pg
      </code>
      
      , <code>
        mysql
      </code>
      
      , <code>
        oracledb
      </code>
      
      , or <code>
        mssql
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_FILENAME
      </code>
    </td>
    
    <td>
      Where to read/write the SQLite database. Required when using <code>
        sqlite3
      </code>
      
      .
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_CONNECTION_STRING
      </code>
    </td>
    
    <td>
      When using <code>
        pg
      </code>
      
      , you can submit a connection string instead of individual properties. Using this will ignore any of the other connection settings.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_EXCLUDE_TABLES
      </code>
    </td>
    
    <td>
      CSV of tables you want Directus to ignore completely
    </td>
    
    <td>
      <code>
        spatial_ref_sys,sysdiagrams
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_CHARSET
      </code>
      
       / <code>
        DB_CHARSET_NUMBER
      </code>
    </td>
    
    <td>
      Charset/collation to use in the connection to MySQL<sup>
        <a href="https://dev.mysql.com/doc/refman/8.0/en/charset-mysql.html" rel="nofollow">
          1
        </a>
      </sup>
      
      /MariaDB<sup>
        <a href="https://mariadb.com/docs/server/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations" rel="nofollow">
          2
        </a>
      </sup>
      
      .
    </td>
    
    <td>
      <code>
        UTF8_GENERAL_CI
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_VERSION
      </code>
    </td>
    
    <td>
      Database version, in case you use the PostgreSQL adapter to connect a non-standard database. Not usually required.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        DB_HEALTHCHECK_THRESHOLD
      </code>
    </td>
    
    <td>
      Healthcheck timeout threshold in milliseconds.
    </td>
    
    <td>
      <code>
        150
      </code>
    </td>
  </tr>
</tbody>
</table>

## Additional Database Variables

All `DB_*` environment variables are passed to the `connection` configuration of a [`Knex` instance](https://knexjs.org/guide/#configuration-options). This means you can extend the `DB_*` environment variables with any values you need to pass to the database instance.

This includes:

- `DB_POOL__` prefixed options which are passed to [`tarn.js`](https://github.com/vincit/tarn.js#usage).
- `DB_SSL__` prefixed options which are passed to the respective database driver. For example, `DB_SSL__CA` which can be used to specify a custom Certificate Authority (CA) certificate for SSL connections. This is required if the database server CA is not part of [Node.js' trust store](https://nodejs.org/api/tls.html).

<callout icon="material-symbols:info-outline">

**Note**<br />

`DB_SSL__CA_FILE` may be preferred to load the CA directly from a file.

</callout>
