# Source: https://docs.pentaho.com/pba/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-dashboard-designer-cp/advanced-topics/use-content-linking-to-create-interactive-dashboards.md

# Use content linking to create interactive dashboards

Depending on your needs, you can create a static dashboard, which contains content in each panel that is separate but related. For example, you may provide users with a bar chart that contains total sales figures by region. Additionally, you may provide a data table that displays sales details for each state in a specific region. You may also want to provide sales data associated with each salesperson in a specific region. The content in your dashboard is useful to dashboard consumers, but to make it more interactive, you may want to consider using content linking.

The content linking features in dashboards allow you to associate (link) content in one dashboard panel to content on another dashboard panel as long as query parameters have been defined. These features are particularly helpful for drilling down or for dynamic filtering; for example, when dashboard consumers explode a single slice in a pie chart to launch content in a data table associated with that pie slice. In this instance, dashboard consumers are moving from a summary view to a detailed view interactively.

You can use content linking if your dashboard panel contains a data table, chart, `.xaction`, `.prpt`, and Analyzer report.
