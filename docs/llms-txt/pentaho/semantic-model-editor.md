# Source: https://docs.pentaho.com/pba/semantic-model-editor.md

# Semantic Model Editor

The Semantic Model Editor enables you to create and manage semantic data models for multidimensional analysis, bridging the gap between data integration and business analytics. By providing a centralized, reusable semantic layer, Semantic Model Editor helps teams standardize business logic, simplify report creation, and improve data accessibility for analysts and decision-makers.

Use Semantic Model Editor to build semantic models that define how your data should be grouped and aggregated for analysis. The models you create can later be consumed by [Pentaho Analyzer](https://docs.pentaho.com/pba/pentaho-analyzer-cp) and other tools, ensuring consistent reporting across your organization.

Semantic models are structured using Mondrian XML schemas that define OLAP cubes using fact tables, dimensions, and measures. Each semantic model is tied to a physical connection, which serves as the source for the data being modeled. The Semantic Model Editor provides two modes: a visual canvas for drag-and-drop modeling and an advanced XML editor for direct schema editing. This dual-mode interface supports both rapid prototyping and precise control over model structure.

## Before you begin

Before you get started with Semantic Model Editor, take the following actions:

* Ensure you have the Data Modeling EE license for the Semantic Model Editor plugin. For details about licenses, see [Acquire and install enterprise licenses](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/pentaho-installation-overview-cp/acquire-and-install-enterprise-licenses).
* Verify that your administrator has assigned to you the appropriate permissions to work with models. For information about permissions, see [Permissions for semantic models](https://docs.pentaho.com/pba/semantic-model-editor/sharing-a-semantic-model/permissions-for-semantic-models).&#x20;
* Verify that your administrator has configured an appropriate maximum value for the number of rows shown when you preview tables and views in a semantic model. By default, the maximum number of rows shown is 100. The administrator can change the maximum value by editing the `row-limit` property in the `application.properties` file, located in: `\Pentaho\server\pentaho-server\pentaho-solutions\system\semantic-model-editor`. The administrator must restart the Server for the new row value maximum to take effect.
* Install Semantic Model Editor plugin. For installation instructions, see [Install plugins](https://docs.pentaho.com/pba/pentaho-user-console/modern-design/plugin-manager#install-plugins).&#x20;

  <div data-gb-custom-block data-tag="hint" data-style="warning" class="hint hint-warning"><p><strong>Important:</strong> If you are using MariaDB, MySql or Oracle as your Pentaho Server repository, your administrator must manually execute scripts for the repository before you can use Semantic Model Editor. Database scripts and documentation for executing the scripts are included with the Semantic Model Editor plugin installation files on the <a href="https://support.pentaho.com">Customer Portal</a>.</p></div>

## Work with semantic models

For instructions on creating and working with semantic models, see the following topics:&#x20;

* [Canvas mode](https://docs.pentaho.com/pba/semantic-model-editor/canvas-mode)

  While working in the canvas, you can control your view of a semantic model and its elements by using layout modes, the cards Legend, node expand and collapse controls, the canvas toolbar, and cube resizing.
* [Advanced mode](https://docs.pentaho.com/pba/semantic-model-editor/advanced-mode)

  Advanced mode is intended for expert users who are familiar with Mondrian XML syntax and want to create or modify semantic models by directly editing the underlying XML.
* [Creating a semantic model](https://docs.pentaho.com/pba/semantic-model-editor/creating-a-semantic-model)

  Create a semantic model to organize physical data into a multi-dimensional structure that has meaning to your business so that you can better understand the data and make informed decisions about your business based on that data. &#x20;
* [Import a semantic model](https://docs.pentaho.com/pba/semantic-model-editor/import-a-semantic-model)

  You can import an existing data source that you published in the **Pentaho Server** as a semantic model. Data sources imported as semantic models are no longer available in the **Pentaho User Console**. &#x20;
* [Editing a semantic model](https://docs.pentaho.com/pba/semantic-model-editor/editing-a-semantic-model)

  A semantic model organizes physical data into a multi-dimensional structure that has meaning to your business. Edit a semantic model to rename it, change its connection details or attributes, or to edit the elements inside model. You can also delete the model or the elements inside of it.
