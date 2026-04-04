# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi.md

# Create a visualization

You create a visualization by defining the following classes:

* **`Model` class**

  identifies the visualization and defines it in terms of its data requirements, such as the visual degrees of freedom it has (x position, color, and size for example) and any major options that affect its rendering.
* **`IView` class**

  implements the actual rendering using chosen technologies, such as [HTML](https://www.w3.org/TR/html/), [SVG](https://www.w3.org/TR/SVG/), [D3](https://d3js.org/), and handles user interaction by dispatching actions including selection, drilling-down, and showing a tooltip.

The following walk-through tutorials guide you through the creation of a custom visualization for the Pentaho platform:

1. [Develop a visualization in a sandbox](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/walk-through-tutorial-cp-visapi)
2. [Create the Pentaho web package](https://docs.pentaho.com/pdia-admin/10.2-admin/pentaho-developer-center-overview-cp/platform-javascript-apis/visualization-api-cp/creating-a-visualization-visapi/creating-the-pentaho-web-package-visapi-custom-visualization-creation)
