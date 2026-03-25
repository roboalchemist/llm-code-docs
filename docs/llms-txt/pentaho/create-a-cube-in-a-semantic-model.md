# Source: https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model.md

# Create a cube in a semantic model

Create a cube with a fact table, dimensions, and measures to contain aggregated data from a semantic model’s physical connection. The fact table contains the data you want to aggregate in the cube. Dimensions describe the aggregated data so that it can be grouped for analysis. Measures quantify the data in the cube to facilitate operations for analyzing the data.&#x20;

You can create a new cube by dragging a view or table onto a blank area of the canvas and then selecting to use the view or table as a fact table or dimension to create the new cube.&#x20;

{% hint style="info" %}
**Note:** When you drag a view or table onto the canvas, you also have the option to create a shared dimension that you can add to an existing cube. For details, see [Create a shared dimension](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-shared-dimension).
{% endhint %}

For instructions on creating a cube by adding a fact table, dimensions, and measures to the cube, see the following topics: &#x20;

* [Add a fact table to a cube](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-fact-table-to-a-cube)

  Add a fact table that contains data from a semantic model’s physical connection that you want aggregated in a cube. You can either create a new cube while adding the fact table or add the fact table to an existing cube.
* [Add a dimension to a cube](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-dimension-to-a-cube)

  Add a dimension that describes aggregated data in a cube so that the data can be grouped for analysis. You can either create a new cube while adding the dimension or add the dimension to an existing cube.
* [Add a measure to a cube](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-measure-to-a-cube)

  Add a measure to a cube so that you can quantify data in the cube and facilitate operations for analyzing the data, such as slicing, dicing, and drilling down.&#x20;
* [Add a degenerate dimension to a cube](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/add-a-degenerate-dimension-to-a-cube)

  Add a degenerate dimension when you want to use only the information in a cube’s fact table to describe the aggregated data in the cube. The degenerate dimension describes aggregated data in the cube so that the data can be grouped together for analysis.&#x20;
* [Use a shared dimension in a cube](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model/create-a-cube-in-a-semantic-model/use-a-shared-dimension-in-a-cube)

  Use a shared dimension in a cube when you want the aggregated data to be consistent with other cubes in the same semantic model.
