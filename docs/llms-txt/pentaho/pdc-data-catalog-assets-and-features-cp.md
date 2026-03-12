# Source: https://docs.pentaho.com/pdc-get-started/pdc-get-started-get-started-cp/pdc-data-catalog-assets-and-features-cp.md

# Data Catalog assets and features

Pentaho Data Catalog provides data management and data representation with its own logical data entities, including the following assets:

## Data sets

Data sets are named logical groupings of related data objects. They are primarily used to organize data objects together visually, but you can also run a process on the data set.

While in the Data Canvas tree view, you can create a data set, or collection, of data objects by selecting the check box next to those objects you want to organize into a single data set. You can choose to display only user-defined data sets in the tree view, greatly simplifying the navigation of these objects.

## Workers

Data Catalog uses Open AI-architected digital worker processes that connect to data sources to perform the following tasks in an automated way:

* Test connection
* Ingesting metadata
* Data profiling
* Data identification
* Key discovery
* Data quality
* Sensitive data discovery

Workers are the background processes that are launched whenever any activity is initiated, either manually or scheduled. You can view and manage workers, cancel worker processes, review the worker's progress and any details or exceptions relating to the worker process.

## Dictionaries and data patterns

Data identification uses two data discovery methods, dictionaries and data pattern analysis. Data Catalog installs a set of pre-configured dictionaries and patterns, but you can define custom dictionaries and patterns if they are necessary for your specific requirements.

* **Dictionaries**

  Dictionaries are word or term lists used to create bitsets and data patterns that you can then use to match column data.
* **Data patterns**

  You can use data patterns for a variety of purposes, such as regular expression (RegEx) generation, data identification, and data quality checking.

## Glossary

The business glossary is an organized list of business terms and their definitions intended to serve as the single and definitive reference for an organization. You can associate business terms with data elements, business rules, related terms, and custom attributes to form a comprehensive view of your organization’s business concepts and data landscape.

## Business rules

Business rules translate business requirements into logic-based rules you can use to tag your data. You can define business rules to manage your data and track its quality by designating whether that data is compliant.

You can use the Business Glossary page to define the compliant and non-compliant data and data formats.

Using these definitions, you can use business rules to apply SQL commands (called data quality rules) that identify non-compliant rows in your data. You can add any number of data quality rules to a business rule.

The business rules act as a hierarchal layer above the data quality rules:

* You can choose whether to enable data quality rules.
* You can also decide if a rule requires supervisor approval before being deployed.
* Use custom tags to track and group business rules according to your needs.

## Physical Assets

The Physical Assets feature in Pentaho Data Catalog is a key component of IT-OT integration, bridging the gap between Information Technology (IT) and Operational Technology (OT) systems. As part of the Pentaho+ offering, this integration leverages Pentaho Edge as the source for operation technology (OT) assets and Pentaho Data Catalog as the platform to visualize and manage these physical assets.

In Data Catalog, Physical Assets section is designed to organize and manage OT asset data points in a structured and intuitive manner. This hierarchy provides a centralized framework to represent OT assets, including components such as device services (protocols), locations, devices, and data point (tags) values, to provide a comprehensive view of the entire data ecosystem.

Physical Assets section provides unified access to OT assets data within the context of IT systems by integrating IT with OT systems to enable better data decision-making by providing the right data is available at the right time. Using Physical Assets feature, you can visualize data in a tree structure, making it easier to navigate, understand, and analyze OT assets. This feature supports the ingestion of both analyzed and underutilized data points, ensuring that no data is siloed. By incorporating metadata tagging, lineage tracking, and contextual insights, from the Physical Assets section, you can manage and utilize OT assets data for better decision-making and compliance. To learn more about the Physical Assets feature, see **Physical Assets** in the **Use Pentaho Data Catalog** document.

## Metadata rules

If your assigned role allows it, you see a **Metadata Rules** card on the Data Catalog **Management** page. These metadata rules enable you to tag, assign business terms, and add properties to already scanned or ingested metadata. By doing so, you can streamline the process of searching for data while minimizing the potential for errors.

If you have a license for Data Optimizer and your assigned role allows it, you can perform additional optimization actions within metadata rules. Leveraging the Data Optimizer metadata rule engine capabilities, you can simplify data management by setting up rules to automate your data tiering, purging, and rehydration operations. You can use a single rule to both identify and move data.

## Dashboards

Dashboards extend the visual discovery and relationship discovery capabilities of Data Catalog in several ways. They also provide a way to add your own customized insight assets, unique to your organization.

Licensed Pentaho Data Optimizer users can access optional dashboards for centralized monitoring of Data Optimizer operations. Information about your migrated, deleted, and rehydrated files, according to source and type, is given through a combination of visualizations and summary details. To learn more, see the **Dashboards** section in the **Use Pentaho Data Catalog** document.
