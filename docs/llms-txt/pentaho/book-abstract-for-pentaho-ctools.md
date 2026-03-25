# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/book-abstract-for-pentaho-ctools.md

# Pentaho CTools

CTools are a set of community-driven tools which are installed as a stack on top of the Pentaho Server and are commonly referred to as CTools.

The core CTools supported by Pentaho include:

* **CDF -** Community Dashboard Framework
* **CDA -** Community Data Access Layer
* **CDE -** Community Dashboard Editor
* **CCC -** Community Charting Components
* **CGG -** Community Graphics Generator

## General overview of Pentaho and CTools

The Pentaho platform allows you to use external components, or plugins, with the purpose of extending the standard functions. These plugins are installed on top of the Pentaho platform, enabling you to add customizations to the BI platform.

### CDF: Community Dashboard Framework

Community Dashboard Framework (CDF) allows BI developers to quickly and easily create dynamic dashboards which allow users to explore and understand large amounts of data using a variety of charts, tables, and other components and then “drill down” to the exact data they want. This framework quickly creates dashboards by using web technologies such as JavaScript, CSS, and HTML, which allows the dashboard designer to control the dashboard’s whole lifecycle without resorting to Java coding. This element of CTools has been a part of the Pentaho platform since the 3.0 version, and is now the foundation for all the implemented dashboards in the system.

CDF has five main advantages:

* Based in open source technology
* Uses popular web technologies, such as Ajax, HTML, and CSS3
* Manages the components' lifecycles and interactions between them
* Separates the HTML design from the component definition
* Allows for extensibility

### CDE: Community Dashboard Editor

Whereas CDF is a development framework directed at users with JavaScript and HTML skills, Community Dashboard Editor (CDE) is a graphical dashboard editor which provides access to the dashboard components in CDF. This tool uses a grid for the layout which enables users to create their own dashboards without needing a lot of JavaScript or HTML expertise. CDE aims to simplify the creation and addition of CTools dashboards.

* [CDE Dashboard Overview](https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-dashboard-overview)
* [CDE Quick Start Guide](https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-quick-start-guide)
* [Activate CDE](https://docs.pentaho.com/pba-ctools/9.3-ctools/activate-cde)
* [Create a Dashboard that uses as Streaming Service as a Data Source](https://docs.pentaho.com/pba-ctools/9.3-ctools/create-a-dashboard-that-uses-a-streaming-service-as-a-data-source)

### CDA: Community Data Access

Community Data Access (CDA) allows you to gather and combine data from several data sources into a single structure, which you can then use in dashboards. Driven by the need to unify access to the Pentaho data layer, CDA was developed to create an abstraction layer between a CTools dashboard and the physical connections to different databases.

CDA has three main objectives:

* Combine data from several sources
* Ensure security while accessing the data (avoiding, for instance, SQL injection problems)
* Ease data exports

### CCC: Community Chart Components

Community Chart Components (CCC) allows dashboard designers to create powerful and custom charts for their dashboards. Essentially, it is a visualization library built on top of [Protovis](http://mbostock.github.com/protovis), a powerful open source data visualization library based in scalable vector graphics (SVG). The included default options can be bolstered with features in CDE, or an advanced user can pass extension points via Protovis commands to enhance chart components in dashboards.

### CGG: Community Graphics Generator

Community Graphics Generator (CGG) allows you to export CCC charts as images which are then available for Pentaho reports. Additionally, this plugin renders the CCC charts in browsers which might have limited capacity for rendering SVG images. In summary, this component is able to draw, within the server, exactly the same chart which is shown in the CTools dashboard using your web browser.

CGG has three main features:

* Full integrated with CDE
* Rendering charts via a URL
* Running SVG-based charts and then converting them into images

<br>
