# Source: https://docs.pentaho.com/pba-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/look-and-feel.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/look-and-feel.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/look-and-feel.md

# Look and feel

In the Layout perspective you may also provide some look and feel properties. For example, you can configure a background color for an element or a style for rows and columns. If you add a CSS resource, you can apply any of the styles defined in the CSS file to any of the elements in your layout by typing it in the **Css Class** and/or **Bootstrap Css Class** property.

CDE provides several simple properties which can be used to customize each specific component. There are some extra properties which you can set, such as background color or style for the corners of rows. Those properties will take precedence over any existing CSS rule which you may have included in the dashboard.

However, this type of direct customization of an element is not recommended for big production systems, as it requires specific manual reconfiguration of each property in the event of a change to the look and feel. For that reason, it is recommended that you use an external CSS resource file.

In the associated CSS style sheet, create a new class and define its properties. Then add this class in the desired element's**CSS Class** property field in CDE.

In summary, you an adjust the look and feel of you dashboard in the following ways:

* HTML to create dashboard elements.
* CSS to control the style and layout.
* JavaScript to add interactivity.
* jQuery to simplify all those tasks.
