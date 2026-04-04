# Source: https://docs.pentaho.com/pba-report-designer/add-report-elements-in-report-designer-cp/report-layout-types.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/add-report-elements-in-report-designer-cp/report-layout-types.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-report-elements-in-report-designer-cp/report-layout-types.md

# Report layout types

You can change the layout type by selecting any of the band elements in the **Master Report** item in the **Structure** pane, then selecting one of the options from the layout drop-down box in the **Size & Position** section of the **Properties** pane. Choosing a layout scheme will deselect the layout checkbox.

The bands in a report can have a few different methods of content layout:

* **Canvas**

  The default layout scheme is canvas, in which report elements have no positioning relationship to one another, and can potentially encroach on the space occupied by other elements in the band. The three other layout types are defined in the sections below.
* **Block**

  Elements in a block layout band are arranged vertically. Block-level elements span the full width of the parent band. If an element expands, it pushes all other elements down so that no element overlaps any other elements. Master Report and SubReport elements, as well as Groups, are always block elements.
* **Inline**

  In an inline formatting context, elements are arranged horizontally, one after the other, beginning at the top of a containing block. Horizontal margins, borders, and padding are respected between these boxes. The boxes may be aligned vertically in different ways: their bottoms or tops may be aligned, or the baselines of text within them may be aligned. The rectangular area that contains the boxes that form a line is called a line box. An inline element that is placed in a non-inline layout band creates an artificial paragraph to wrap around this element. The most common use of this layout strategy is to produce rich-text content from several independent report elements.
* **Row**

  The row layout scheme positions elements one after each other on the horizontal axis. All elements are printed in a single row, expanding their height as needed. If all elements expand to the height of tallest element, set the min-height to "100%" to even them out. This layout type is a natural match for list reports, where multiple columns of data should be printed per row. When an element expands its width, all other elements get pushed to the right. When you use a row layout for your list reports, you will no longer need to arrange elements manually. To create spacing between elements, use either padding on your elements, or place an empty band as a padding element into the row layout band. The Report Design Wizard makes use of the row layout to position elements in the details and details-header bands.
