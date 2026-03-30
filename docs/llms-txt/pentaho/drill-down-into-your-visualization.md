# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/data-integration-perspective-in-the-pdi-client/work-with-transformations-cp/run-your-transformation/inspect-your-data/use-filters-to-explore-your-data/drill-down-into-your-visualization.md

# Drill down into your visualization

**Drill down** is used to explore a specific dimension or measure of your data and to obtain more details on the next hierarchy levels. In **Model View**, you can drill down within a visualization into the hierarchies in your dataset.

When drilling down, you automatically apply filters according to the hierarchical field structure of your data, which replaces the parent with the child in the associated drop zone (except when using the Pivot Table, where the child is added to the hierarchy). The filter used for the drill down is added to the **Filters** panel and the visualization is updated accordingly.

In following examples, various drill down and filtering actions are illustrated:

* To drill down into the next layer of dimensional data, you can click a data point in a visualization and then select **Drill down**.

  ![Drill Down Selection](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-120c9eff241161d76080c0b687c88cfac88b18cf%2FDET_DrillDown_Viz1B.png?alt=media)
* To drill down into layers of hierarchical data, you can double-click a data point, axis label, or legend. Note that in cases where more than one hierarchy is available for drill down, the first available option is automatically selected.

  ![Drill Down Features](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-d56799a99358661dad3f554b4522716bebe08d75%2FDET_DrilldownExample2_UseFilters.png?alt=media)
* When a data point has more than one dimension, you can select what dimension to drill down to from the menu.

  ![Drill Down Selections](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-05b27359b4250f41930dd6132d53ff948c45453c%2FDET_DrilldownExample3_UseFilters.png?alt=media)

In this example, you want to explore motorcycle sales data for the EMEA geography field to analyze the results for each country inside that territory.

![Drill Down Filter, Example 1](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-13d79f150c7f8a8678e2fdf63951d4e701c814c3%2FDET_DrilldownExample4_UseFilters.png?alt=media)

* A filter to show the value that was drilled down on is added to the **Filters** panel. The chart updates to break down the motorcycles sales data by ‘COUNTRY’ for the 'EMEA' territory.

  ![Drill Down Filter, Example 2](https://3411831820-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FAYwCj9fPr1B2pjC11IOQ%2Fuploads%2Fgit-blob-0562bf78cf09c182a107645248a7fe9c8ed4e82c%2FDET_DrilldownExample5_UseFilters.png?alt=media)
