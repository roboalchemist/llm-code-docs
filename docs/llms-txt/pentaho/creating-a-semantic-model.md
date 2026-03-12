# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model.md

# Creating a semantic model

Create a semantic model to organize physical data into a multi-dimensional structure that has meaning to your business so that you can better understand the data and make informed decisions about your business based on that data. &#x20;

{% hint style="info" %}
**Note:** Only JDBC connections are supported.&#x20;
{% endhint %}

To create a semantic model for analyzing data, complete the following procedures:&#x20;

* [Create a basic semantic model](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-basic-semantic-model)  &#x20;

  Create a basic semantic model with the minimum information of the model's name and physical data connection details.&#x20;
* [Create a cube in a semantic model](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model)

  Create a cube with a fact table, dimensions, and measures to contain aggregated data from a semantic model’s physical connection. The fact table contains the data you want to aggregate in the cube. Dimensions describe the aggregated data so that it can be grouped for analysis. Measures quantify the data in the cube to facilitate operations for analyzing the data.
* [Create a shared dimension](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-shared-dimension)

  Create a shared dimension for aggregated data that you want to use consistently across multiple cubes in the same semantic model. For example, a shared time dimension with annotations like Year, Month, and Week can be linked to several cubes, ensuring uniform time-based analysis.
