# Source: http://dev.cs.ovgu.de/java/dbjunit/changes-report.html

Title: DbUnit - Changes

URL Source: http://dev.cs.ovgu.de/java/dbjunit/changes-report.html

Markdown Content:
**Quick Links**

**Overview**

**Project Documentation**

[![Image 1: Powered by Maven](http://dev.cs.ovgu.de/java/dbjunit/images/logos/maven-propaganda.png)](http://maven.apache.org/ "Powered by Maven")### [Release History](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Version | Date | Description |
| --- | --- | --- |
| [2.1](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#2.1) | May 31, 2004 | Multiple bugfixes and enhancements. |
| [2.0](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#2.0) | January 22, 2004 | Major release. |
| [1.5.6](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.5.6) | October 5, 2003 |  |
| [1.5.5](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.5.5) | July 16, 2003 |  |
| [1.5.1](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.5.1) | April 4, 2003 |  |
| [1.5](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.5) | March 1, 2003 |  |
| [1.4](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.4) | July 17, 2002 |  |
| [1.3](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.3) | April 4, 2002 |  |
| [1.2.4](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.2.4) | March 19, 2002 |  |
| [1.2](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.2) | March 15, 2002 |  |
| [1.1](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.1) | March 10, 2002 |  |
| [1.0](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html#1.0) | Febuary 27, 2002 | Initial public release. |

### [Release 2.1 - May 31, 2004](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 2: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 741394 - New database compare Ant tag. See Ant task documentation. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 3: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New Comma Separated Values (CSV) dataset implementation. | [fspinazzi](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#fspinazzi) |
| ![Image 4: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 824328 & 948479 - Ability to add DOCTYPE declaration when writing a flat Xml dataset. See FAQ. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 5: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 884422 - FlatDtdWriter has now the ability to generate DTDs with choice model instead of sequence model. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 6: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Ability to import external file for binary data types like BLOB; the value can be either a qualified URL o r a file path name. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 7: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Do not omit NULL values anymore in INSERT statements. Now only XmlDataSet's < none/ > tag are omitted. With FlatXmlDataSet you must use the ReplacementDataSet to achieve the same behavior. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 8: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 937732 - XlsDataSet now use UTF-16 encoding to support Asian characters. Patch submitted by Shuhei Kondo. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 9: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Applied XlsTable empty table detection patch submitted by Deepak Kaimal. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 10: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Added back FlatXmlDataSet constructors taking URL as argument missing in version 2.0. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 11: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 918631 & 925585 - Fixed FlatXmlDataSet constructors taking InputStream/Reader for loading DTD. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 12: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | DELETE_ALL operation now deletes tables only *once* in reverse order they are encountered. Before, duplicate tables were resulting in multiple deletes. Patch submitted by John Hurst. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 13: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | DELETE_ALL operation now compatible with StreamingDataSet. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 14: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 947330 - Now closing ResultSet before Statement to fix exceptions thrown by the Firebird JDBC driver and the OpenBase 8.0 JDBC driver. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 15: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 921869 - Fixed ParameterIndexOutOfBoundsException with InterBase. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 16: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | 947809 - Moved createMetaData() static method from AbstractResultSet to DatabaseTableMetaData and made it public. Can now be used to create ITable from a ResultSet. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 17: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Support for large Oracle BLOB. Must use OracleDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 18: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Oracle LONG RAW data type support via OracleDa taTypeFactory. Original patch submitted by Markus Muller. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 19: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Added back support for Oracle FLOAT missing in DbUnit 2.0. Must use OracleDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 20: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Support for Oracle NCHAR2 as proposed by Deepak Kaimal. Must use OracleDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 21: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Added DataType.isDateTime() method proposed by Ayman Mahfouz. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 22: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 726366 & 884422 - Added IColumnFilter interface. Can be used to filter out some table columns. See FAQ. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 23: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Renamed ITableFilter.isValidName() method to accept() to be consistent with the new IColumnFilter interface. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 24: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 955354 - Ability to determine the primary keys with IColumnFilter interface instead of DatabaseMetaData.getPrimaryKeys(). Primar y keys sequence is not predictable when using filter. See FAQ. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 25: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Ability to plug custom IDENTITY column detection strategy for InsertIdentityOperation when using user defined types. See FAQ. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 26: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added DefaultTableFilter class, which combines capability of the Include/ExcludeTableFilter classes. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 2.0 - January 22, 2004](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 27: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Mavenized the build and the website! | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 28: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Now use SAX2 instead of Electric XML DOM parser. Streamed mode allows importing and exporting very large XML datasets with minimal memory consumption. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 29: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Flat XML dataset validation. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 30: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New ITableIterator interface used to iterate thru dataset tables. Allows lazy tables initialization for some dataset implementations. The IDataSet.getTables method have been deprecated and usage should be avoided. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 31: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Global System properties are not supported anymore. You must now use the new DatabaseConfig object to alter DbUnit behaviours. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 32: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Configurable data type factory to easily integrates new data types with the DbUnit core. Factory implementations available for some database vendors. Submit your own! | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 33: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Oracle TIMESTAMP data type support via the OracleDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 34: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Fix truncated Oracle DATE. Must use the OracleDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 35: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Fix for Oracle CLOB greater than 4000 bytes. Must use the OracleDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 36: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | MySQL 'longtext' data type support via the MySqlDataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 37: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | DB2 XML data types support via the Db2DataTypeFactory. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 38: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Database views support. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 39: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New pluggable filter strategies for DataSetFilter. You can now exclude/include tables using wildcard patterns. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 40: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Ability to sort tables by their dependencies with the new DatabaseSequenceFilter strategy. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 41: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New ReplacementDataSet decorator, which can replace decorated dataset values on the fly. Can be used with flat XML dataset as a new way to specify null values. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 42: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New XlsDataSet. An MS Excel dataset implementation. Uses the Jakarta POI package. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 43: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Assertion.assertEquals is now performing typed comparison instead of string representation comparison. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 44: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | INSERT, CLEAN_INSERT and REFRESH operations do not override database default values anymore with null values. Null values are now omitted from insert statements. Operations use multiple prepared statements for the same table, when null values vary from row to row. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 45: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Moved InsertIdentityOperation to "org.dbunit.ext.mssql" package to be consistent with other vendor extensions. Temporary keep a deprecated copy in "org.dbunit.operation.mssqlserver" to ease transition to DbUnit 2. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.5.6 - October 5, 2003](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 46: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 786543 - NULL primitive values incorrectly returned as zero (0). | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 47: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Fix Oracle CLOB values incorrectly returned as NULL. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.5.5 - July 16, 2003](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 48: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | DatabaseDataSet improvements: faster access to metadata cache and keep original database table ordering. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 49: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Better handling of the various data types in general. WARNING! New abstract methods have been added to the DataType class. This change may break your environment if you have implemented your own data types. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 50: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | More efficient XmlDataSet writing. Now put values in CData block only when necessary. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 51: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Do not enable batched statement by default anymore. Many JDBC drivers have problems with this feature. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 52: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Fixed table name issue with case sensitive database. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 53: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 615636 & 735095 - Incorrect XML encoding. Better handling of the XML encoding while writing and reading XML datasets. InputStream and OutputStream methods in XML dataset implementations are no more deprecated. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 54: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 736439 - Problems with InsertOperation and triggers. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 55: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 736967 - Wrong scale for numeric value with the jConnect driver for Sybase ASE. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.5.1 - April 4, 2003](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 56: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Fixed DELETE operation that was not deleting tables in reverse order as expected. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 57: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 7123 29 - setObject fails on BEA JDriver for MS-SQL. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 58: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | DbUnitTask DTD export optimization. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 59: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | REFRESH operation optimization. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.5 - March 1, 2003](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 60: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | Multiple bugfixes. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 61: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 533321 - DbUnit is now case insensitive. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 62: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 555455 - Supports table names escaping (see escapePattern property). | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 63: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 551925 - Allows duplicate table names in datasets. A new method, getTables(), have been added in the IDataSet interface. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 64: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 590245 & 684610 - New Reader and Writers methods to read and write XML datasets. InputStream and OutputStream methods are now deprecated. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 65: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New SortedTable and SortedDataSet decorator classes. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 66: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 645691 - Added the < classpath > nested element in DbUnitTask ant task; used to load the JDBC classes. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 67: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added < query > nested element in DbUnitTask < export > . Allows exporting the result of a SELECT as a table of a dataset. See ant task documentation. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 68: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | New Canoo Webtest integration guide. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.4 - July 17, 2002](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 69: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | DbUnitTask for Ant contributed by Timothy Ruppert and Ben Cox. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 70: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Moved the Base64 class to the org.dbunit.util package because Visual Age for Java is not able to handle classes located in the default package. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 71: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Added system properties documentation. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 72: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | 542034 - Detect ambiguous table names. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 73: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | 542462 - Added a system property to disable usage of batch statement even if the target database support it.. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 74: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | 545238 - Sort tables prior to comparing them. DbUnit now generates an ORDER BY clause in the select statement used by DatabaseDataSet.getTable(). Rows are sorted by primary keys. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 75: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | 554249 - None column values. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 76: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added support for BLOB and CLOB data types. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.3 - April 4, 2002](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 77: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added support for binary data types: BINARY, VARBINARY and LONGVARBINARY. Binary data is persisted in xml datasets using the base64 encoding scheme. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 78: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Deprecated the DataSetUtils.assertEquals() methods. You should now use Assertion.assertEquals(). | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 79: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 533537 - FlatXmlDataSet and null values. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 80: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 533537 - Problem with single quotes. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 81: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 534810 - Problem when primary key include all columns | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.2.4 - March 19, 2002](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 82: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added support for multiple schemas per connection. See FAQ document. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 83: remove](http://dev.cs.ovgu.de/java/dbjunit/images/remove.gif) | Removed element < none/ > from dataset.dtd. This feature was incompatible with future support for the binary data types. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 84: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 530998 - DataSetUtils.AssertEquals(ITable table, ITable table). | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 85: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 533540 - Problem with DATE, TIME and TIMESTAMP. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.2 - March 15, 2002](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 86: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added the flat XML dataset format. See the FlatXmlDataSet in Core Components document. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 87: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added database data verification feature. See Getting Started document. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 88: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Updated Electric XML parser to version 3.2. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.1 - March 10, 2002](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
| ![Image 89: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Connections are now closed in each setUp() and tearDown(). You must override the DatabaseTestCase.closeConnection() and provide an empty body to modify this behavior. This is not recommended to bypass connection close if you use connection pooling. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 90: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added the IDatabaseConnection interface. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 91: add](http://dev.cs.ovgu.de/java/dbjunit/images/add.gif) | Added the DatabaseDataSourceConnection class. This class provi des support for accessing JDBC connections from a DataSource. JDBC connections are requested on demand from the DataSource. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 92: update](http://dev.cs.ovgu.de/java/dbjunit/images/update.gif) | Multiple performance improvement. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |
| ![Image 93: fix](http://dev.cs.ovgu.de/java/dbjunit/images/fix.gif) | 526235 - Cannot export tables with JDBC-ODBC bridge and MS-SQL. | [](http://dev.cs.ovgu.de/java/dbjunit/team-list.html#) |

### [Release 1.0 - Febuary 27, 2002](http://dev.cs.ovgu.de/java/dbjunit/changes-report.html)

| Type | Changes | By |
| --- | --- | --- |
