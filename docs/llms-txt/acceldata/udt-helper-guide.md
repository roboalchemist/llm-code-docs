# Source: https://docs.acceldata.io/documentation/udt-helper-guide.md

# UDT Helper Guide



This section explains how programmers can create UDT using the interfaces offered by Acceldata and the unit test case suite to write cover test cases.



> Please refer to the ADOC-cli-readme.pdf usage documentation for information on how to create projects and manage their lifecycles, which include test runs, packaging, and pushing.



**Prerequisites**:

1. Zip and unzip software or command line utility
2. Java 8
3. Spark 2.4 or 3.2
4. Scala 2.12.x in case of Spark 3.2 or Scala 2.11.x in case of Spark 2.4
5. Gradle 7.4.2
6. IDE (Integrated Development Environment) supports gradle projects (preferably IntelliJ)



> At this time, you must get in touch with the **Acceldata Support** **Representative** to download this package.





#### 1. Create a new project



```bash
./adoc-cli-2.6.0-release-95-mac-amd64 udt new --language scala --project-
name sample-udt-repo   --spark-major-version 32  --destination-dir .
```





The repository structure will look like:



```bash
├── ADOC-cli-usage.pdf 
├── UDT-helper-guide.pdf 
├── adoc-udt-manifest-gcp-template.json  // GCP Storage driven template 
├── adoc-udt-manifest-s3-template.json   // S3 Storrage driven template 
├── build.gradle.kts 
├── gradle 
│   └── wrapper 
├── gradlew 
├── gradlew.bat 
├── libs 
│   └── ad-udt-spark-32-2.6.0-release-95.jar  //  Acceldata SDK need to be 
part of project and should be in lib dir  
├── settings.gradle.kts 
└── src 
    ├── main // Sample Codes , User need to use same to create new UDT 
definitions 
    └── test // Sample Test Cases , User need to use same to cover test 
    cases for new UDT definitions
```





## Interfaces

There are two types of UDTs:

1. Transform: When creating a new transform column for a data quality policy, the user wants to have a transformation at runtime. This transformation can also be used to consume a portion of a rule.
2. Filter: User wants to use filter as a straightforward filter-driven rule in data quality policy.
3. Lookup Filter: User wants to use lookup filter as a filter-driven rule in data quality policy using reference lookup.
4. Group By Lookup Filter: User wants to use Group by reference lookup as a filter-driven rule when using By Lookup Filter in data quality policy.



#### 1. Transform

- Scala Interface - io.ad.udt.types.scalatype.TransformUDT
- Java Interface - io.ad.udt.types.javatype.TransformUDT



> To get the same sample for each programming language and project, please refer to udt/sample src.



Using Scala:



```scala
class TransformSampleUDT extends TransformUDT { 
 
  override val variables = List[String]("FIRST_COLUMN_NAME", 
"SECOND_COLUMN_NAME") 
 
  override def evaluate(row: Row, parameters: Map[String, String]): String 
= { 
    val firstName = row.getAs[String]
(parameters.get("FIRST_COLUMN_NAME").get) 
    val lastName = row.getAs[String]
(parameters.get("SECOND_COLUMN_NAME").get) 
    firstName + "_" + lastName 
  } 
}
```





Steps:

- Extends TransformUDT
- variables : Define variables if they are a part of UDT; otherwise, leave them empty
- evaluate : There are two parameters
    1. row: Row is an object that contains row data with corresponding column
    2. parameters: Map[String, String] - We use these parameters as dynamic variables, and they will be passed when attaching the UDT when creating the DQ policy.
    3. Supported return type for primitive types



#### 2. Filter

- Scala Interface - io.ad.udt.types.scalatype.TransformUDT
- Java Interface - io.ad.udt.types.javatype.TransformUDT

Using Scala:



```scala
class FilterSampleUDT extends FilterUDT { 
  override val variables = List[String]("COUNTRY_COLUMN_NAME") 
 
  override def evaluate(row: Row, parameters: Map[String, String]): 
Boolean = { 
    val country = row.getAs[String]
(parameters.get("COUNTRY_COLUMN_NAME").get) 
    if (country == null || country.trim.isEmpty) false 
    else country.equalsIgnoreCase("US") 
  } 
 
}
```





Steps:

- Extends FilterUDT
- variables : Define variables if they are a part of UDT; otherwise, leave them empty
- evaluate : There are two parameters
    1. row: Row is an object that contains row data with corresponding column
    2. parameters: Map[String, String] - We use these parameters as dynamic variables, and they will be passed when attaching the UDT when creating the DQ policy.
    3. Return type should be always Boolean



#### 3. Filter Using Reference Lookup

- Scala Interface - io.ad.udt.types.scalatype.TransformUDT
- Java Interface - io.ad.udt.types.javatype.TransformUDT

Using Scala:



```scala
class FilterLookUpSampleUDT extends LookUpFilterUDT { 
  override val variables = List[String]("COUNTRY_COLUMN_NAME") 
 
  override def evaluate(row: Row, parameters: Map[String, String], store: 
HelperStore): Boolean = { 
    val country = row.getAs[String]
(parameters.get("COUNTRY_COLUMN_NAME").get) 
    if (country == null || country.trim.isEmpty) { 
      false 
    } else { 
      val lookup = store.lookup("country_alias") 
      lookup.contains("country_code", country) 
    } 
  } 
}
```





Steps:

- Extends LookUpFilterUDT
- variables : Define variables if they are a part of UDT; otherwise, leave them empty
- evaluate : There are two parameters
    1. row: Row is an object that contains row data with corresponding column
    2. parameters: Map[String, String] - We use these parameters as dynamic variables, and they will be passed when attaching the UDT when creating the DQ policy.
    3. store: HelperStore is a lookup store that must be used to reference as an asset and retrieve the appropriate columns' data for subsequent use.
    4. Return type should be always Boolean



> HelperStore provides a lookup API. Please visit [https://docs.acceldata.io/torch/torch/lookup-data-quality-policy-rule#lookup-rule-usage-methods](https://docs.acceldata.io/torch/torch/lookup-data-quality-policy-rule#lookup-rule-usage-methods) to obtain the API lists.





#### 4. Filter Using Reference Lookup Group By

It is the same as Filter Using Reference Lookup; the only distinction is that we are using group by reference here, for which HelperStore requires the use of the get api and requires the same to be passed from the UI as well.

- Scala Interface - io.ad.udt.types.scalatype.LookUpFilterUDT
- Java Interface - io.ad.udt.types.javatype.LookUpFilterUDT



```scala
class FilterLookUpSampleUDT extends LookUpFilterUDT { 
  override val variables = List[String]("COUNTRY_COLUMN_NAME") 
 
  override def evaluate(row: Row, parameters: Map[String, String], store: 
HelperStore): Boolean = { 
    val country = row.getAs[String]
(parameters.get("COUNTRY_COLUMN_NAME").get) 
    if (country == null || country.trim.isEmpty) { 
      false 
    } else { 
      val lookup = store.lookup("country_alias") 
      lookup.contains("country_code", country) 
    } 
  } 
}
```





Steps:

- Extends LookUpFilterUDT
- variables : Define variables if they are a part of UDT; otherwise, leave them empty
- evaluate : There are two parameters
    1. row: Row is an object that contains row data with corresponding column
    2. parameters: Map[String, String] - We use these parameters as dynamic variables, and they will be passed when attaching the UDT when creating the DQ policy.
    3. store: HelperStore is a lookup store that must be used to reference as an asset and retrieve the appropriate columns' data for subsequent use.
    4. Return type should be always Boolean



#### 5. Plain Filter or Reference Lookup Filter with Failure Metadata

With Plain Filter and Reference Lookup Filter, Failure Meta is an added feature. This enables the user to return the result as true or false as well as any error feedback as meta.

Here you must return io.ad.udt.model.PredicateResult object with two parameters:

1. result:  It is of boolean type, if you want to treat the record as good or bad depending on the business logic.
2. metadata: Metadata can be of any native collection. It is failure meta per record basis, which will be used later while running Data Quality to collect the feedback of any bad records.

Syntax for Scala PredicateResult



```scala
PredicateResult( 
      result = false, 
      metadata = Map[String, String]("error" -> "Some error") 
    )
```





Syntax for Java PredicateResult



```scala
Map<String, String> error_meta = new HashMap<>(); 
  error_meta.put("error" , "Some error"); 
  new PredicateResult(false, error_meta);
```





- Scala Interface - io.ad.udt.types.scalatype.FilterUDT
- Java Interface - io.ad.udt.types.javatype.FilterUDT
- Scala Interface - io.ad.udt.types.scalatype.LookUpFilterUDT
- Java Interface - io.ad.udt.types.javatype.LookUpFilterUDT

To obtain the same sample for each programming language and project, please refer to udt/sample src. For the sample below, utilizing Scala:



```scala
import io.ad.udt.model.PredicateResult 
import io.ad.udt.types.scalatype.FilterUDT 
import org.apache.spark.sql.Row 
 
class FilterWithMetaDataSampleUDT extends FilterUDT { 
  override val variables = List[String]("COUNTRY_COLUMN_NAME") 
 
  override def evaluate(row: Row, parameters: Map[String, String]): 
PredicateResult = { 
    val country = row.getAs[String]
(parameters.get("COUNTRY_COLUMN_NAME").get) 
 
    var error = "" 
 
    if (country == null) { 
      error = "country is null" 
    } else if (country.trim.isEmpty) { 
      error = "country is empty" 
    } else if (!country.equalsIgnoreCase("US")) { 
      error = s"country == US check failed. country got ${country}" 
    } else { 
      return PredicateResult(result = true, metadata = null) 
    } 
    PredicateResult( 
      result = false, 
      metadata = Map[String, String]("error" -> error) 
    ) 
  } 
}
```





- Extends FilterUDT
- variables: Define variables if they are a part of UDT; otherwise, leave them empty
- evaluate: There are two of parameters
    1. row: Row is an object that contains row data with corresponding column
    2. parameters: Map[String, String] - We use these parameters as dynamic variables, and they will be passed when attaching the UDT when creating the DQ policy.
    3. The return type should be always PredicateResult with result as boolean and metadata as any
native collection.

## Unit Test Case Suite

- Scala Test Suite Class - io.ad.udt.suite.UDTScalaTestSuite
- Java Test Suite Class - io.ad.udt.suite.UDTJavaTestSuite

Here is an example test case for Group By Lookup:



```scala
import io.ad.analysis.config.ReferenceDataFramePerAsset 
import io.ad.udt.suite.UDTScalaTestSuite 
import org.apache.spark.sql.DataFrame 
import org.junit.runner.RunWith 
import org.scalatestplus.junit.JUnitRunner 
import udt.sample.scalacode.model.{Country, Employee, Location} 
 
import scala.collection.mutable 
 
@RunWith(classOf[JUnitRunner]) 
class FilterGroupByLookUpSampleUDTTest extends UDTScalaTestSuite { 
 
  val udt = new FilterGroupByLookUpSampleUDT() 
 
  override def input(): DataFrame = { 
    val data = Seq( 
      Employee(1, "Sigal", "Tobias", "Purchasing", "US", "Howland 
Island"), 
      Employee(2, "Susan", "Mavris", "Human Resources", "US", "Delaware"), 
      Employee(3, "Britney", "Everett", "Shipping", "US", "Alaska"), 
    ) 
 
    spark.createDataFrame(data) 
  } 
 
  override def configureReferenceAssets(): mutable.Map[String, 
ReferenceDataFramePerAsset] = { 
 
    val countryData = Seq( 
UDT-helper-guide.md2/23/2023
6 / 7
      Country(1, "US", "UNITED STATES", true), 
      Country(2, "IN", "INDIA", true), 
      Country(3, "CA", "CANADA", false), 
      Country(4, "AU", "AUSTRALIA", false) 
    ) 
    val countryDataFrame = spark.createDataFrame(countryData) 
 
 
    val locationData = Seq( 
      Location(1, "United States", "US", "Howland Island", "UM - 84", 
true), 
      Location(2, "United States", "US", "Maryland", "MD", false), 
      Location(3, "India", "IN", "Delhi", "DL", true), 
      Location(4, "India", "IN", "Maharashtra", "MH", false), 
      Location(5, "Canada", "CA", "Ontario", "ON", true), 
      Location(6, "Canada", "CA", "Manitoba", "MB", false) 
    ) 
    val locationDataFrame = spark.createDataFrame(locationData) 
 
    mutable.Map[String, ReferenceDataFramePerAsset]( 
      "country_alias" -> ReferenceDataFramePerAsset(  assetUid = 
"country",   dataframe = countryDataFrame,  referenceAssetColumns = 
List("country_code"), referenceAssetSqlFilter = "is_active == true" ), 
      "location_alias" ->  ReferenceDataFramePerAsset(  assetUid = 
"country",  dataframe = locationDataFrame, referenceAssetColumns = 
List("country_code", "state_name"),   referenceAssetSqlFilter = null ) 
    ) 
  } 
 
  test("Check if country code and state name both are present in 
respective country and lookup reference table") { 
    val parametersForVariables = Map[String, String]("COUNTRY_COLUMN_NAME" 
-> "country_iso_code", "STATE_COLUMN_NAME" -> "state_name") 
    val result = validate(udt, parametersForVariables) 
 
    val output = result.select("predicate_Result").collect() 
      .map(_.get(0).asInstanceOf[Boolean]) 
      .filter(_ == true) 
      .toList 
    assertResult(1)(output.size) 
  } 
 
}
```





Steps:

- Extends UDTScalaTestSuite or UDTJavaTestSuite depending upon the language
- input : Create the input data frame and return the same
- configureReferenceAssets: This one is optional, so we can leave it blank if not used. It will be applied to UDTs that involve lookups. Here, the map must be made using the asset alias key and the reference table data frame. See how we can create by referring to the relevant sample.
- validate : The user must call validate with two parameters for each test case.
    1. udt: Create a object for the respective UDT definition and pass as parameter
    2. parameters: The UDT must use this map with key and value to resolve internal dependencies.
    3. It will return the data frame with data type as provided and compute in UDT.



> For examples of the test cases we've provided based on language, please refer to the test module. For each of the UDT options, test case examples will be provided.





