# Source: https://docs.curator.interworks.com/site_content_design/org_chart/org_chart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Org Chart

> Create and display organizational charts with hierarchical employee structure and reporting relationships visualization.

The Org Chart provides a visual representation of the organizational structure within a company or organization. It
outlines the hierarchy of positions, roles, and reporting relationships.

## Creating an Org Chart

### Preparing the data

The Curator Org Chart is built using the
[Data Manager](/embedding_using_analytics/data_manager/data_manager_basics)
for its underlying data. You'll need to create an Attribute for each column in the employee data you'll be adding or
importing. It's important the names of the Attributes match the names of the columns from your data if you'll be
importing from another system. Once you have created the Attributes, you'll need to create a Data Manager Group and
select the Attributes you've just created. Finally, you can use the "Batch Import" button on the Data Manager > Manage
Data page in your Curator backend. There, you can upload a CSV with all of your employee data.

### Creating the Org Chart

Navigate to the Data Manager > Org Chart area of your Curator backend. There, you can click "New Org Chart" and fill
out the form. Below are descriptions of each field:

* **Title**: This is the title for your Org Chart. The primary place this will be displayed is in the browser tab
  displaying the Org Chart on the frontend.
* **Data Manager Group**: This is the Data Manager Group we created and imported the data to.
* **Employee Name Attribute**: This is the Attribute name that corresponds to the column in the data for the employee’s
  name. This will be displayed on the employee’s node in the chart.
* **Employee ID Attribute**: This is the Attribute name that corresponds to the column in the data for the employee’s
  ID. This column and the Supervisor ID column will be how the chart knows where to put each employee in the tree.
* **Supervisor Name Attribute**: This is the Attribute name that corresponds to the column in the data for the
  employee’s supervisor’s name.
* **Supervisor ID Attribute**: This is the Attribute name that corresponds to the column in the data for the
  supervisor’s ID. This column and the Employee ID column will be how the chart knows where to put each employee in the
  tree.
* **Role Name Attribute**: This is the Attribute name that corresponds to the column in the data for the employee’s
  role at the company.
* **Who is the top node for the Org Chart?**: Enter the name here for who is at the top of the Org Chart (typically a
  CEO). This needs to match the Employee Name Attribute value of your highest ranking employee.
* **Slug**: This is the bit at the end of the URL for the page where the Org Chart will be displayed. This will be
  automatically generated based on the Title field, but you can change it if you’d like.

### Customize the Org Chart Design

Below the primary configuration for the Org Chart are many fields that can be used to customize the look of the Org
Chart. Here are descriptions of each option in the Design tab:

* **What shape should the nodes be?**: You can choose a circle or a rectangle. The rectangle allows you to show more
  information in each node.
* **How should nodes be named?**: You can choose to show the employee’s name or, if you’d like to be a bit more
  confidential, the employee’s role at the company on the node in the chart.
* **Specify any additional attributes to show in each node**: This is where we can add more information to the
  rectangular nodes. *(This only appears if the node shape is set to rectangle.)*
* **Show employee headshot?**: This will tell the Org Chart you have URLs in your data and would like to show those
  images.
* **Employee Headshot Attribute**: This is the Attribute name that corresponds to the column in the data for the
  employee’s headshot URL. Users will be able to flip the switch in the top right of the chart to toggle headshots and
  the employee info. *(This only shows if the “Show employee headshot?” switch is on.)*
* **Show tooltip on hover with additional employee details?**: This will tell the Org Chart you’d like to show a
  tooltip when hovering over a node. It’s very useful if you’re wanting to display employee details without making the
  chart look too busy.
* **Attributes to show in tooltip**: Add any Attributes here you’d like to appear in the tooltip. *(This only appears*
  *if the tooltip option is flipped on.)*
* **Color employee nodes by attribute?**: This allows adding a visual way to differentiate each employee. The most
  common use cases are coloring by employee department and full-time vs. part-time. A legend will be shown in the
  top-left corner of the chart designating what each color means.
* **Specify any additional attributes for the search bar to parse (default is only employee name)**: This adds
  Attributes/columns that the search will parse. Sometimes you don’t know the employee’s name but know their department,
  so this improves parsing a large org chart.

### Frontend Org Chart Editing

While the Org Chart is more for reporting pre-determined organization data, we do have some light editing tools. Here
are descriptions of each option in the Editing tab:

* **Which Frontend Groups can edit?**: You don’t want just anyone to be able to edit or delete employees from your Org
  Chart, so you can choose specific Frontend Groups to give these privileges to. There will be an Edit button and a
  Delete button that become visible on each node. The Edit button will show a pop-up window with the employee’s relevant
  details, which can be changed and saved. The Delete button will give a confirmation message before sending the node
  into oblivion. *Note: The Edit and Delete buttons are omitted from the top node because changing those details could*
  *easily break the underlying data and leave the Org Chart blank.*
* **Fields to show in edit Form**: By default, only the name, role and supervisor Attributes are shown in the edit
  form. You can use this field to add additional Attributes to the form.
* **PDF Download**: Sometimes the browser’s print functionality doesn’t quite hit the mark with visualizations like
  this, so we’ve added a PDF download option for a much more visually appealing download of the chart.
* **PDF Download Watermark**: The data being revealed on the Org Chart could be sensitive, so it’s important to make it
  known this shouldn’t be shared. Whatever text is added to this field will be slapped over the chart in the PDF.
* **CSV Download**: This will generate a CSV containing data for the visible nodes, as opposed to the full data the Org
  Chart is running on. The button for this, as well as the PDF download, will be in the top-right corner of the Org Chart
  page.
