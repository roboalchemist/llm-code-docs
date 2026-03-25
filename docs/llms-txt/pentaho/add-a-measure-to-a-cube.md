# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube.md

# Add a measure to a cube

Add a measure to a cube so that you can quantify data in the cube and facilitate operations for analyzing the data, such as slicing, dicing, and drilling down. &#x20;

{% hint style="info" %}
**Note:** The cube must have a fact table before you can add a measure to it.&#x20;
{% endhint %}

Complete one of the following procedures for the type of measure you want to add:&#x20;

* [Add a simple measure to a cube ](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-a-simple-measure-to-a-cube)

  Add a simple measure to use values pulled directly from a column in the cube’s fact table as a measure.
* [Add simple measures in bulk](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-simple-measures-in-bulk-to-a-cube)

  When a cube’s fact table has many fact columns, and you need to create one or more simple measures for each column, you can create simple measures in bulk by defining criteria to select columns and apply an aggregation function to those columns.&#x20;
* [Add a calculated measure to a cube ](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-a-calculated-measure-to-a-cube)

  Add a calculated measure when you want to calculate values for the data you are measuring in a cube by using a multidimensional (MDX) expression. &#x20;
* [Add a measure created with SQL to a cube](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube/add-a-measure-created-with-sql-to-a-cube)

  Add a measure created with SQL to a cube when you want to calculate the values for the data you are measuring in a cube by using an SQL expression that references data from multiple tables or views in the cube.  &#x20;
