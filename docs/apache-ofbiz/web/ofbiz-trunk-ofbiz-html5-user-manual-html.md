# Source: https://nightlies.apache.org/ofbiz/trunk/ofbiz/html5/user-manual.html

Title: Apache OFBiz User Manual

URL Source: https://nightlies.apache.org/ofbiz/trunk/ofbiz/html5/user-manual.html

Markdown Content:
Apache OFBiz User Manual
The Apache OFBiz Project
Version Trunk
Table of Contents
1. Introduction to OFBiz
1.1. What is Apache OFBiz
1.2. The main parts of Apache OFBiz
1.2.1. Web MVC Framework
1.2.2. Entity Engine
1.2.3. Service Engine
1.2.4. Widget System
1.2.5. Data Model Library
1.2.6. Service Library
1.2.7. Core Applications
1.2.8. Plugins
1.3. The Apache OFBiz documentation system
1.3.1. Overview
1.3.2. Contributing a new help screen, a few steps.
1.3.3. Internationalization of the help system
2. Quick start
2.1. Download the Gradle wrapper:
2.2. Prepare OFBiz:
2.2.1. Clean system and load the complete OFBiz data
2.3. Start OFBiz:
2.4. Visit OFBiz through your browser:
3. The OFBiz Setup application Overview
3.1. Why we have OFBiz Setup Application?
3.2. How to get started.
3.3. Steps for setup
3.3.1. The Main OFBiz Setup Overview
3.3.2. Help for Setup Edit Facility
3.3.3. Help for Setup Edit Product Store
3.3.4. Help for Setup Edit WebSite
3.3.5. Help for Setup Create First Customer
3.3.6. Help for Setup Edit First Catalog
3.3.7. Help for Setup Edit First Product Category
3.3.8. Help for Setup Edit First Product
3.3.9. Help for View Organization Profile
Core Business Applications
4. Party
4.1. Overview
4.2. Parties management in UI
4.2.1. Help for The Party Find screen.
4.3. Parties Processes
4.3.1. How to Create the main Company
4.4. Communications
4.5. Visits
4.6. Classifications
4.7. Security
4.8. Miscellaneous
Party Glossary
5. Catalog
5.1. Overview
5.1.1. Help for Catalog Main screen
5.2. Products
5.3. Catalogs
5.3.1. Catalogs overview
5.3.2. Working with Catalogs
5.3.3. Browse Categories links
5.3.4. Catalog Administration Main Page
5.4. Categories
5.5. Product Features
5.5.1. Standard features
5.5.2. Selectable features
5.5.3. Distinguishing features
5.5.4. Working with Product Features
5.5.5. Create and Maintain Product Features
5.5.6. Feature Categories and Feature Groups
5.5.7. Add Features to a Category
5.5.8. Feature Categories
5.5.9. Working with Feature Groups
5.5.10. Implement Feature-based Product Search
5.6. Promotions
5.6.1. Similar to Price Rules
5.6.2. Opening Screen
5.6.3. Promo tab
5.6.4. Rules tab
5.6.5. Stores tab
5.6.6. Codes tab
5.7. Price Rules
5.8. Product Stores
5.8.1. Main Store screen
5.8.2. Why use stores?
5.8.3. Working with Product Stores
5.9. Configurations
5.10. Image Management
5.10.1. How To Add Security Group For Image Management User
5.10.2. Gallery
5.10.3. Upload
5.10.4. Recently Approved
5.10.5. Approve
5.10.6. Rejected
5.10.7. Manage
5.10.8. Replace
5.11. Miscellaneous
6. Facility
6.1. Facility management in UI
6.1.1. Receive Return
Facility Glossary
7. Order
7.1. Overview
7.1.1. Business Purpose
7.1.2. Create Order Diagrams
7.1.3. Order Status
7.1.4. Update Order
7.1.5. Payment Terms and Method
7.2. Orders management in UI
7.2.1. Orders of the day
7.2.2. List Orders
7.2.3. Find Orders
7.2.4. Order View
7.2.5. Order Entry
7.2.6. Order Entry Init
7.2.7. Order Currency, Agreements, and Ship Dates
7.2.8. Add Item(s) to cart
7.2.9. Quick Finalize Order
7.2.10. Set Shipping address and Group
7.2.11. Set Item to ShipGroup
7.2.12. Order Option Settings
7.2.13. Order Term
7.2.14. Payment setting
7.2.15. Additional Party Entry
7.2.16. Order confirmation
7.2.17. Order Entry is now completed
7.3. Orders Processes
7.3.1. Order Entry
7.4. Help for Order Reports
7.4.1. Initial steps.
7.4.2. Reports List
7.5. Requests
7.6. Quotes
7.7. Returns
7.7.1. Return Process Overview
7.7.2. Sales Return Diagrams
7.7.3. Sales Return management in UI
7.8. Requirements
7.9. Stats
Order Glossary
8. Accounting
8.1. About Accounting
8.1.1. Accounting Features
8.2. Invoices.
8.2.1. Invoices management in User Interface
8.3. Payments.
8.3.1. Payments management in User Interface
8.4. Payment Gateway
8.4.1. Payment Gateway Config management in User Interface
8.4.2. Payment Transaction management in User Interface
8.5. Billing Accounts.
8.5.1. Billing Account management in User Interface
8.6. Agreements
8.6.1. Sales Agreement
8.6.2. Purchase Agreement
8.6.3. Commission Agreement
8.6.4. Agreement management in User Interface
8.7. Financial Accounts
8.7.1. Bank Account
8.7.2. Credit Card Account
8.7.3. Deposit Account
8.7.4. Equity Line Account
8.7.5. Gift Certificate
8.7.6. Investment Account
8.7.7. Loan Account
8.7.8. Replenish Account
8.7.9. Service Credit Account
8.7.10. Store Credit Account
8.7.11. Financial Accounts in User Interface
8.8. Tax Authorities.
8.8.1. Tax Authorities management in User Interface
8.9. Global General Ledger Settings
8.9.1. Master Template - Chart of Accounts
8.9.2. Custom Time Periods
8.9.3. Costs
8.9.4. Payment Method Type
8.9.5. Invoice Item Types
8.9.6. Rates
8.9.7. Foreign Exchange Rates
8.9.8. GL Account Category
8.9.9. Cost Centers
8.10. Organization GL Settings.
8.10.1. Help for setting by domain
Accounting Glossary
9. Content Management
9.1. Overview
9.2. Security
9.3. Major CMS entities
9.3.1. DataResource
9.3.2. dataTemplateTypeId
9.3.3. objectInfo
9.4. Content
9.4.1. dataResourceId
9.4.2. contentName
9.4.3. description
9.4.4. templateDateResourceId
9.5. ContentRole
9.6. ContentPurpose
9.7. ContentPurposeOperation
9.8. ContentAssoc
9.8.1. contentId
9.8.2. contentIdTo
9.8.3. contentAssocTypeId
9.8.4. fromDate
10. Manufacturing
10.1. About Manufacturing and MRP
10.1.1. What is Manufacturing?
10.1.2. What is MRP?
10.2. JobShop, or ProductionRun
10.2.1. ProductionRun management in UI
10.3. Routing
10.3.1. Routing management in UI
10.4. Routing Task
10.4.1. Routing Task management in UI
10.5. Calendar
10.5.1. Calendar management in UI
10.6. Manage Cost Component Calc Entries
10.6.1. Cost Component Calc management in UI
10.7. Bill Of Material
10.7.1. Bill Of Material management in UI
10.8. MRP
10.8.1. MRP management in UI
11. SFA
11.1. Overview
11.2. SFA in User Interface
11.2.1. Main screen
11.2.2. SFA Accounts find/list screen
11.2.3. SFA Contacts find/list screen
11.2.4. SFA Leads find/list screen
11.2.5. SFA SalesOpportunity find/list screen
12. Human Resources
12.1. About Human Resources
12.1.1. The Human Resources Main screen.
12.2. HR Processes
12.2.1. Organization, Job Position and Definition
12.2.2. Employee Salary and Benefits Administration
12.2.3. Employee Training and Development
12.2.4. Performance Management and Employee Evaluation
12.2.5. Recruitment, Candidate Selection and Hiring
12.3. HR core object
12.3.1. Employee Positions
12.3.2. Employees
12.3.3. Employments
12.3.4. List Employments
12.3.5. Performance Review
12.3.6. Qualifications
12.3.7. Recruitment
12.3.8. Skills
12.3.9. Resumes
12.3.10. Training
12.3.11. Leave
12.3.12. Security
12.4. Global HR Settings
12.4.1. Employee Leave Type
12.4.2. Pay Grades
12.4.3. Position Types
12.4.4. Skills Types
12.5. HR Data model
12.5.1. Employee Position
12.5.2. Employment
12.5.3. Qualification, Skill, Review
12.5.4. HR App intra-application integration
HR Glossary
Appendix A: HR Data Model Resource Book Difference
Appendix B: HR Enhancement & Bug
12.B.1. Functional bug
12.B.2. Functional Enhancement
13. Marketing
13.1. Marketing in User Interface
13.1.1. Help for main screen
13.2. Marketing Contact Lists.
13.2.1. Contact Lists management in UI
13.3. Web tools
13.3.1. Help for Webtools Main page.
Apache OFBiz Plugins
14. Project Manager
14.1. ProjectMgr in UI
14.1.1. Main screen.
14.1.2. My tasks
14.1.3. My Timesheets
14.1.4. Find Projects
14.1.5. Project - billing
14.1.6. Project - edit info
14.1.7. Project - orders
14.1.8. Project - phases
14.1.9. Project - resources
14.1.10. Project - tasks
14.1.11. Project - Requests
14.1.12. Tasks
14.1.13. Timesheets
15. My portal Plugin
15.1. Some Portlet in other components
16. Asset Maintenance plugin
17. The Scrum Component.
17.1. Introduction
17.2. Administration
17.3. Product Backlog.
17.4. Task
17.4.1. View Task
17.5. Sprint Demonstration and Evaluation meeting
17.6. Security
18. Birt OFBiz® plugin
18.1. OFBiz Flexible Reports
18.2. Technical Documentation
18.2.1. Report creation
18.2.2. Using the Birt Report Designer
18.2.3. Report master creation
18.3. User documentation
18.3.1. Using a flexible report
18.4. BIRT in OFbiz User Interface
18.4.1. PDF tab
18.4.2. Send any format through Mail tab
18.4.3. Chart tab
18.4.4. Examine the Example Report
18.4.5. How do I send parameter to report?
18.4.6. Which are the supported content types?
19. The Ebay Component
19.1. main Features
19.2. Ebay management in User Interface
20. Ebay Store
20.1. Ebay Store management in User Interface
20.1.1. Ebay Store main screen.
20.1.2. New Ebay Account.
20.1.3. Ebay Store Detail screen.
20.1.4. Export categories to ebay store screen.
20.1.5. EBay Leave Feedback.
20.1.6. EBay Feedback.
20.1.7. Ebay Store Auto-Setting
20.1.8. Automation Re-list Items
20.1.9. Handle Ebay Product Inventory.
20.1.10. Reserve Product From Ofbiz Inventory.
20.1.11. Block item that out of stock.
21. Example Plugin
21.1. Help file organization
21.2. Development help sub-subject
21.3. UI help for Example
22. Apache OFBiz® plugin for REST
22.1. Important URLs
22.2. Endpoints
22.3. Authentication
22.4. Example
22.5. Refresh Token Mechanism
22.5.1. Login API Enhancement
22.5.2. Get Access Token Using Refresh Token
General Glossary
1. Introduction to OFBiz

Welcome to Apache OFBiz! A powerful top level Apache software project. OFBiz is an Enterprise Resource Planning (ERP) System written in Java and houses a large set of libraries, entities, services and features to run all aspects of your business.

This manual will describe all aspects of this powerful ERP system. The manual starts with the basics of what OFBiz is and how it works, and describes high level concepts like the entity engine, service engine, widget system and so on. In addition the manual explains the core application of this framework like the Party Manager, Order Manager, Accounting system, and others.

If you wish to contribute to OFBiz and help make it better, you may wish to read the "Apache OFBiz Developer Manual" for a deeper understanding of the architectural concepts of the framework.

1.1. What is Apache OFBiz

It is hard to define OFBiz because it offers many different solutions targeted at different levels of interests (users, developers, business owners). At a low level it may considered a web framework, at another level, it may considered a full fledged ERP system, and yet it can also be considered a business automation suite.

1.2. The main parts of Apache OFBiz

Perhaps to better understand what OFBiz is, it may be necessary to understand its main parts and the purpose that each part plays. Thus the main parts or sub-systems are summarized below.

1.2.1. Web MVC Framework

The lowest or most foundational part of Apache OFBiz is a classical web MVC (Model View Controller) framework. This part of the system is designed for basic routing of web requests and may be considered as the infrastructure or plumbing where everything is wired together.

1.2.2. Entity Engine

The entity engine allows OFBiz users to define entities, data, and queries in a database-independent domain specific language (DSL) based on XML. Thus, without learning any SQL users can create and interact with databases in a platform-independent manner and Apache OFBiz would make the translations under the hood to each database system.

1.2.3. Service Engine

Apache OFBiz is designed specifically around a Service Oriented Architecture (SOA). Services are units of business logic that take a set of input values and produces a set of output values.

Services are programming-language-independent. It does not matter whether a service is implemented using Java, Groovy, Jython, or something else because services are an abstraction away from the underlying technology. This provides maximum flexibility for designing business logic without worrying about interoperability between different languages.

1.2.4. Widget System

Whether the output is HTML, CSV, PDF, or something else, Apache OFBiz provides a system for creating user interface that is independent of the actual implementation. This makes it possible to publish the same widget to HTML, PDF, CSV or some other output format.

However, the widget system allows users, if needed, to drop down to any platform-specific code and mix it with widget designs, thus providing a mix between ease of use, platform independence and customizability.

1.2.5. Data Model Library

Apache OFBiz is heavily inspired by a book called the "The Data Model Resource Book". This book provides a "A Library of Universal Data Models for All Enterprises". These models cover things like parties, orders, invoices, payments, general ledgers, quotes and much more.

By using OFBiz, adopters start with a full pre-designed data model that covers common and universal business requirements. Hundreds of entities are defined which save many hours of thinking, designing, and testing such models.

It is important to note that the data model library does not only cover entities, but also the data that comes with these entities. Data is further categorized by function (seed, demo, etc …​)

1.2.6. Service Library

Having a rich and powerful data model is not very useful on its own without services that apply business logic on this data model. That is where the services defined in Apache OFBiz come into play.

OFBiz provides, out-of-the-box, thousands of services to create, retrieve, update, delete, search, and do many other operations on the data model.

1.2.7. Core Applications

The core applications in Apache OFBiz are web applications that serve common business needs found in most enterprises such as accounting, order management, party management and so on.

These core applications are built on top of the data model and service library earlier described. The core applications are further described in the relevant section.

1.2.8. Plugins

OFBiz extends any basic functionality through plugins. Plugins are very similar to the core applications in design and structure, but are not shipped with OFBiz by default. Thus to install a plugin a user must add it to the framework first.

1.3. The Apache OFBiz documentation system
1.3.1. Overview

there are two supports for OFbiz documentation, the wiki and some mains documents (in pdf and html format)

user-manual

developer-manual

documentation_guidelines

README

Asciidoc

The OFBiz documents are generated from a number of Asciidoc files. In general the files are stored on each component in the 'src/docs/asciidoc' directories.
The general main documents include all files from component.

The manuals and guidelines documents are located in docs/asciidoc directories, and REAME.adoc is in root directory.

Help link in the OFBiz user interface, are link to the user-manual generated by buildbot process from Apache OFBiz community. It’s possible to change a property in OFBiz to have link to your own generation.

For details about asciidoc rules used in Apache OFBiz have a look to Documentation Guidelines

Application components

All main files of each component are included in user-manual.adoc

Framework components

All main files of each component are included in developer-manual.adoc except for webtools which is included in user-manual

Plugins

For the main files of the plugin components, there are two ways to read them.

On the one hand, the plugin documentation generation process generates one document per plugin, so that you can see the list of documents in the pluginsdoc directory and thus read each of them;

On the other hand, each plugin master file is included in the plugin chapter of the user manual or developer manual, depending on whether the plugin is "technical" or "functional".

Wiki

Wiki is the second way to contribute to the documentation. Detail on how to Help for providing help content is on the wiki 

Most of wiki page has been or will be migrated to the asciidoc pages, but, as wiki is more easier to be update (update existing page or create new one) the two system will continue to exist and live.

1.3.2. Contributing a new help screen, a few steps.

Documentation Guidelines is the first doc to read to be able to contribute to documentation and/or help.

If you are looking for asciidoc files format examples, please look at the following files:

An example for a chapter of a component at: applications/humanres/src/docs/asccidoc/_include/hr-intro.adoc

An example of a help screen: applications/humanres/src/docs/asccidoc/_include/HELP-hr-main.adoc

Screens

If you would like to create a new help for a certain screen, you need to do the following:

Write documentation in a functional point of view and in a process perspective.

Each title (in all level) generate in html an anchor, so starting point of the help should be a title.

Take the anchor generated (something like _the_title , with only lowercase), for example by looking in the html file generated.

In the screen add a <set field for helpAnchor with anchor generated as value.

1.3.3. Internationalization of the help system

Currently documentation is only in English (except for 3 or 4 files, not included).

In near future, there will be a solution to be able to have documentation/help in multiple languages, a jira (OFBIZ-12030) is open of that.

The switching between locale will be completely automatic (depending on OFBiz user local)

2. Quick start

To quickly install and fire-up OFBiz, please follow the below instructions from the command line at the OFBiz top level directory (folder).

2.1. Download the Gradle wrapper:

MS Windows: init-gradle-wrapper

	

If you cross the error

"Powershell is not recognized as an internal or external command, operable program or batch file"

follow the advice there: https://s.apache.org/vdcv8. If you want more details see: https://s.apache.org/urnju

If you run into problems check the the execution policy of PowerShell. See https://s.apache.org/urnju for details. By setting the execution policy to "unrestricted", you’ll be prompted to run the script once you run the init-gradle-wrapper command.

	

If you wonder where are stored the PowerShell Executables, here are the answers: https://s.apache.org/w5dye

Unix-like OS: ./gradle/init-gradle-wrapper.sh

2.2. Prepare OFBiz:
2.2.1. Clean system and load the complete OFBiz data

Note: Depending on your Internet connection speed it might take a long time for this step to complete if you are using OFBiz for the first time as it needs to download all dependencies. So please be patient!

MS Windows: gradlew cleanAll loadAll

Unix-like OS: ./gradlew cleanAll loadAll

	This command deletes all previous data and resets it to the initial demo data.
2.3. Start OFBiz:

MS Windows: gradlew ofbiz

Unix-like OS: ./gradlew ofbiz

Note: Ignore the % progress indicator because this task does not end as long as OFBiz is running.

2.4. Visit OFBiz through your browser:

Order Back Office interface

Accounting Back Office interface

Administrator interface

You can log in with the user admin and password ofbiz.

3. The OFBiz Setup application Overview

The OFBiz Setup application is supporting for immediate setup your organization. For example, Product Store, WebSite , Facility , product catalog, category , product, and etc. and then be able to create orders from data that is created.

3.1. Why we have OFBiz Setup Application?
	For manual setup instructions, please see the Business Setup Guide on the wiki.

If you are the company and also want to use OFBiz for running your business then you easily be able to setting your information for start running the system quickly via The OFBiz Setup Application.

3.2. How to get started.
	TO CHECK add link to Readme and better information between demo data and seed

For instructions to run and load data to have OFBiz ready to be used, please read the README documentation.

For having OFBiz ready to be setup, it’s needed to load data from reader seed and seed-initial

Open a new terminal.

Go to your ofbiz directory.

Clean out all built classes with : gradlew cleanAll

Start with a database clean and empty. If you use Derby it’s already done with previous command.

Load the seed data with gradlew "ofbiz --load-data readers=seed,seed-initial"

Create the admin user with login name MyUserName and default password with value "ofbiz": gradlew loadAdminUserLogin -PuserLoginId=MyUserName

start ofbiz with : gradlew ofbiz

Connect to the OFBiz Setup application with your browser at https://localhost:8443/ofbizsetup.

follow each step of the next chapter "Steps for setup"

3.3. Steps for setup
3.3.1. The Main OFBiz Setup Overview

The main page on OFBiz Setup application including 2 sections, following this:

Available Internal Organizations Section

This section shows list of organizations which store in the system. You be able to edit an information of your orgainzation via click setup then it will go to view profile screen, you will see other tab button including Facility, Product Store, Web Site, First Customer, and First Product where you would like to edit an information.

When you created an information of your orgainzation and also created product. And the last step is click "Set to complete" button.

Create New Organization Section

This section provides a form for create a new an organization(the first step of setup organization) and also setup the "Billing (AP) Address" , "Payment (AR) Address", "General Correspondence Address", any telephone numbers, and email addresses you want for your Company.

3.3.2. Help for Setup Edit Facility

The Edit Facility screen is used to manage a warehouse, a store with related inventory.

How do I create a facility?

Select the 'Facility' sub menu and the screen will be displayed

Enter the 'Facility Id' field
(NOTE: If you do not enter the 'Facility Id' field it will be used the default as 'Organization Party Id')

Enter the 'Name' field

Enter a description describing what the line item is

Enter a number in the 'Default Days To Ship ' field

Press the 'Save' button

How do I update a facility?

Not all the fields on the facility can be updated.
For example Facility Id cannot be updated. If these fields need to be amended then the facility will need to be removed and then re-created.

Select the 'Facility' sub menu and the screen will be displayed: Any existing line items will be displayed in the 'Items' box

Amend the details in the line item that needs to be updated (eg Name, Description, Default Days To Ship)

Press the 'Update' button displayed at the end of the line item that has been updated

3.3.3. Help for Setup Edit Product Store

The Product Store screen is used to manage a store with has all the information needed to sell products.

For example shippings ,a series of catalogs, which are composed of product categories and products, and also used to configure the payment processing settings , fulfillment, notification, promotions, payment processing, and tax calculation policies , and etc.

How do I create a Product Store?

Select the 'Product Store' sub menu and the screen will be displayed

Enter the 'Product Store Id' field
(NOTE: If you do not enter the 'Product Store Id' field it will be used the default as 'Organization Party Id')

Enter the 'Store Name' field

Press the 'Update' button

How do I update a Product Store?

Not all the fields on the Product Store can be updated.
For example Product Store Id cannot be updated. If these fields need to be amended then the Product Store will need to be removed and then re-created.

Select the 'Product Store' sub menu and the screen will be displayed: Any existing Product Store will be displayed in the 'Items' box

Amend the details in the line item that needs to be updated (eg Store Name)

Press the 'Update' button displayed at the end of the line item that has been updated

3.3.4. Help for Setup Edit WebSite

The WebSite screen is used to manage the details of a WebSite.

The WebSite record is used to configure which Product Store to use for your site that references it.

How do I create a Web Site?

Select the 'Web Site' sub menu and the screen will be displayed

Enter the 'Web Site Id' field
(NOTE: If you do not enter the 'Web Site Id' field it will be used the default as 'Organization Party Id')

Enter the 'Site Name' field

Select the 'Visual Theme Set' field

Press the 'Save' button

How do I update a Web Site?

Not all the fields on the web site can be updated.
For example Web Site Id cannot be updated.
If these fields need to be amended then the web site will need to be removed and then re-created.

Select the 'Web Site' sub menu and the screen will be displayed

Any existing line items will be displayed in the 'Items' box

Amend the details in the line item that needs to be updated (eg Site Name, Visual Theme Set)

Press the 'Update' button displayed at the end of the line item that has been updated

3.3.5. Help for Setup Create First Customer

The First Customer screen provides
- create/edit the first customer of your organization
- and also setup the "Shipping Destination Address" , "General Correspondence Address", any telephone numbers, and email addresses you want for your first customer.

How do I update the profile information of the first customer?

After the first customer is created the profile and contact information screen will be displayed

Select the 'Update' button on the top corner of the profile information and the screen will be displayed: Any existing information will be displayed in the box

Amend the details in the profile information that needs to be updated

Press the 'Save' button

Press the 'Cancel/Done' button for go back to the first customer screen

3.3.6. Help for Setup Edit First Catalog

It provides an overview on Catalog, Category, and Product which is the first one of your organization.

You will be able to create/edit Catalog, Category, and Product for your organization and also be able to create order by that product.

How do I create a Catalog?

Select the 'Product Catalog' sub menu and the screen will be displayed

Enter the 'Prod Catalog Id' field
(NOTE: If you do not enter the 'Prod Catalog Id' field it will be used the default as 'Organization Party Id')

Enter the 'Catalog Name' field

Press the 'Update' button

How do I update a Catalog?

Not all the fields on the Catalog can be updated.
For example Prod Catalog Id cannot be updated.
If these fields need to be amended then the Catalog will need to be removed and then re-created.

Select the 'Product Catalog' sub menu and the screen will be displayed

Any existing Catalog will be displayed in the box

Amend the details in the line item that needs to be updated (eg Catalog Name)

Press the 'Update' button displayed at the end of the line item that has been updated

3.3.7. Help for Setup Edit First Product Category

The Edit First Product Category screen is used to manage the first category with related the first catalog.

How do I create a Category?

Select the 'Category' sub menu and the screen will be displayed

Enter the 'Product Category Id ' field
(NOTE: If you do not enter the 'Product Category Id' field it will be used the default as 'Organization Party Id')

Enter the 'Category Name' field

Enter a description describing what the category is

Press the 'Update' button

How do I update a Category?

Not all the fields on the Category can be updated.
For example Prod Catalog Id cannot be updated.
If these fields need to be amended then the Category will need to be removed and then re-created.

Select the 'Category' sub menu and the screen will be displayed: Any existing Category will be displayed in the box

Amend the details in the line item that needs to be updated (eg Category Name, Product Description )

Press the 'Update' button displayed at the end of the line item that has been updated

3.3.8. Help for Setup Edit First Product

The Edit First Product screen is used to manage the first product with related the first catalog and the first category.

How do I create a Product?

Select the 'Product' sub menu and the screen will be displayed

Enter the 'Product Id' field
(NOTE: If you do not enter the 'Product Id' field it will be used the default as 'Organization Party Id')

Enter the 'Internal Name' field

Enter the 'Product Name' field

Enter a description describing what the category is

Enter a number in the 'Default Price' field

Enter a number in the 'Average Cost ' field

Press the 'Update' button

How do I update a Product?

Not all the fields on the Product can be updated.
For example Product Id cannot be updated.
If these fields need to be amended then the Product will need to be removed and then re-created.

Select the 'Product' sub menu and the screen will be displayed: Any existing Product will be displayed in the box

Amend the details in the line item that needs to be updated (eg Internal Name, Product Name, Short Description, Default Price, Average Cost)

Press the 'Update' button displayed at the end of the line item that has been updated

3.3.9. Help for View Organization Profile

This screen shows details of an individual profile.

It displays specific information regarding the contact and profile information. The lower part of the screen shows the contact information details indicating the address, telephone number, or email used to communicate with your organization.

Core Business Applications

Most businesses share universal needs. They require accounting functionality, managing customers, placing orders, book-keeping, invoicing and so on.

OFBiz is designed so that such basic universal business needs are available through a set of core business applications. These applications all share a unified data-model with a set of unified services to implement this functionality.

This section of the manual will describe each core business application starting with a high level overview of design and purpose down to the details of how to achieve common tasks.

4. Party

The Party Manager application is used to manage the parties, i.e any legal entity your company has to deal with.

4.1. Overview

A party can be a person or a company (or a group of parties).

Party application can be use to manage:

customer

supplier

employee

…​

This application is used to manage profile, contact information, relationship, role, communication, classification, …​

4.2. Parties management in UI
4.2.1. Help for The Party Find screen.

The 'Find Party' is the default screen for the Party Manager application.
It is used to locate existing parties.
Various search criteria can be used, either based on the general party data like name role and type but also on the postal address, telephone (Telecom) and other like email address.

If the find button is pressed, a list is presented containing several columns.

The first column shows the Party ID. This is a string that uniquely identifies the Party in the system.

The second column shows the Party logins.
This is the string the user enters when logging into the system.
A single Party can have more than one login. In this case the "(many)" string is showed in place of the login string. The complete list of user logins can still be seen in the Party details screen. If a Party has no user login associated the string "(none)" is shown.

In the "Main Roletype" column the role is listed which is a child of the "Main role"" roletype. It is currently set to "Organisation" and "SFA Role". The later to be prepared to use he party in he SFA component. See the marketing application for more information

From Party to Order

This screen can be a starting point for Order management (view existing, create a new one, …​).

For each Parties listed, there are links to Order management action.

Before taking the order, you might want to update the party’s information: is the address and phone number current, how will they be paying for the order (credit card number current? EFT information correct?), or perhaps review their ordering history (are there an excessive number of returns?). To look at their file, either click on the [Party ID] or the [Details] link.

If the contact from your customer is specifically about a previous order, you can click on the [Orders] link which will take you to a table of all their previous orders.

4.3. Parties Processes
4.3.1. How to Create the main Company

OFBiz needs to have at least on main company set up that will represent the main business or organization.
If you have installed OFBiz with the demo data then the main company already exists.
If you have installed OFBiz without the demo data then it will not exist so you will need to create it.

This is is done in Party Manager.

	Party Manager is the application where we create all the entities (companies, people, groups, departments) that we deal with in the course of doing business.

This tutorial is quite simple, only 4 step.

This process is running automatically every day in Apache OFBiz demo (trunk) as a GUI process test.
The associated video (showing all the actions described in this tutorial) can be visualize at How to Create the main Company

step Party

Login to OFBiz

Create Party

Select “Party” from the Applications drop down menu if you are not already in

Click “Create New Party Group”
The company we are creating is not an individual (person, customer, prospect or employee). It is an organization and in OFBiz this is called a "party group" (a group of people)

fill in the form fields

Party ID (e.g COMPANY)
(NOTE: that you can enter the Party ID manually. If it is not entered OFBiz will auto generate an ID. If you enter the ID it will make it easier to locate it quickly in future; but it’s dangerous to create wrong ID, in ID only standard characters and without space are authorized. ID length must be less than 20 characters. Best practice is to use only UpperCase.)

Group Name (e.g “My OFBiz Main Company”). This will be the name of your company)

it’s possible to leave al other field blank

Click “Save”

You are now on profile page.

step Address

Next we need to enter some contact details. Find the "Contact Information" section (box)

Click "Create" on the screenlet title

Select "Postal Address"

Click "Create"

fill in the form fields

Address Line 1

Address Line 2 (not mandatory)

City

State / Province (not mandatory)

Zip / Postal Code

Country

Click Save

The address is added - but - there is still some missing setup.

step Address purpose

We need to include a purpose (or use) for the address.

Click “Update” next to the address details

Select "Primary Address" and Click "Add Purpose

Select "Shipping Origin Address" and Click "Add Purpose"

Select "Shipping Destination Address" and Click "Add Purpose"

click to GoBack or on Profile in the screen-sub-menu

The address purpose is be updated.

step role

We now need to add a specific role to this party group to let OFBiz know that is an organization that will have an accounting setup.

Click "Roles" in screen-sub-menu

In the 'Add to Role : view All' section, use the dropdown box to:

Select the Role Type Id "Internal Organization"

Click "Add"

The internal organization role will be added to our new Party Group.

Now this is done we can begin the Accounting setup.

4.4. Communications
4.5. Visits
4.6. Classifications
4.7. Security
4.8. Miscellaneous
Party Glossary
Agreement

An agreement is a way of recording a business arrangement or contract that your business makes with other companies or individuals. For more details have a look to Agreements management in accounting component.

	Examples: Customer or Supplier payment terms (eg.30 days to pay); Discounts (e.g products or volume); Commissions; Customer Contracts (agreement to sell x number of widgets for y price, or sell at y price for a certain time frame)
Person

Person is a human being as distinguished from a party group which is an organization. Human beings and organizations have different attributes i.e. People have first and last names while groups have group names. Both person and party group are types of parties and share information and processes common to parties.

Security Group

A security group is a collection (or a set) of application privileges that can be assigned to a user login id. A user can be assigned to multiple security groups

	Example: FULLADMIN; BIZADMIN; ECOMMERCE_CUSTOMER.
Supplier

Role of a party that something if purchased from

Vendor

Role of a party that sells something with the system

5. Catalog

The Catalog Manager creates or provides access to a variety of information. Whether Products, Catalogs, or Categories, this screen offers search tools and links to get you to the type of information you need or are working with quickly and accurately.

The Catalog Manager application is used to manage the products, all what is purchase, sale, build, used, …​ by the company. A product can be physical or digital.

With catalog application, you can manage all data associated with Product : category, catalog, price, id, …​.

5.1. Overview

TODO

5.1.1. Help for Catalog Main screen

Down the left hand column are 4 sections:

Search Products,

Browse Catalogs,

Browse Categories,

Product Categories.

	You can click on the colored '_' to close a section;
later, click on the colored '[]' to reopen the section.

Each of those sections are discussed below before we begin to explore the Catalog Administration Main Page.

Navigation Panel The Left-hand Navigation Panel is visible even when working under the other tabs.
The content displayed will vary according to what choices you have made.

This document is arranged to walk you through the Navigation Panel search tools (Search Products, Browse Catalogs, Browse Categories, and Category Products) and links first.

As you come to the desired Edit or Creation window, jump in this document to the associated 'Edit' discussion.

Some symbols used as shortcuts Brackets [] Application links as found on the screens are represented in this document with brackets around them like [this]. When you see a bracketed item, you can know we are referring to a link or key or 'button' which will initiate the indicated action.

Greater than symbols >> The single (>) or double (>>) greater than symbols can be read as 'takes you to' or 'leads to' or 'results in.' These are sometimes used in this document to indicate that from this screen, if you click on the [Bracketed Link], you will be taken to Next Process.

Within the pop-up calendars, however, the (>>) jumps you ahead one year and the (<<) jumps you back a year.

An asterisk * marks those items which must be completed on a screen before the desired action can occur.

5.2. Products
5.3. Catalogs
5.3.1. Catalogs overview

A product catalog is used to group many product categories together and forms an intermediate step in the organization between products, categories, and stores.

The product catalog can be used to define a common look and feel for all categories in this catalog and specify the way different categories will behave.

For example, it is very useful for stores which sell products from different manufacturer or completely different product types that require differing presentations to the customer.

Sequence from a Store to the Products

Although the process sequence through the tabs discussed below does not correspond with the tab layout within the Catalog Manager, the progression of the steps is intentional.

Promotions and Price Rules cannot exist without Products.

Products are usually so numerous that you wish to divide them into Categories and distinguish them by their Features.

Categories are then the major sections of your Catalogs.

And Catalogs must be associated with their related Stores.

Therefore, when setting up your business, you need to start with the Store.

All of these details are handled within the Catalog Manager.

5.3.2. Working with Catalogs

To follow this topic, click on the 'Catalog Detail List' in the left-hand panel under the 'Browse Catalogs' section.
Then click on any catalog in the table of current catalogs presented in the main screen.

You will see the top-level editing screen for that catalog.
Along the top of the working screen are four sub-tabs: Catalog, Stores, Parties and Catalogs.
Each of those are discussed as a topic below.

Catalog tab

The main Catalog tab for a product catalog is mostly for establishing the look and feel.

Each catalog can have its own style sheet (CSS), its own logo, and its own content repository (the content path prefix) and templates prefix (where its freemarker templates are located).

The Stores tab

The 'Stores' tab shows a list of Stores that this Catalog is currently featured in.

	Stores and Catalogs do not have a one-to-one relationship: the same Store can feature multiple Catalogs, and the same Catalog could be featured in many Stores.
The Parties tab

Here you identify which Party is responsible for or assigned to work with the specific Catalog selected.

The Party’s Role is assigned or identified and, if appropriate, a start and/or finish date for the assignment can be specified.

Categories tab

The 'categories' tab shows the different product categories and their roles for this catalog. Specifically:

Each catalog can (should) have a 'Browse Root' category, which is used as the root category for navigation.
For example, the navigation menu would start at this category and show its child categories.

Each catalog can also have a 'Promotions' category, which is shown first to the customer when he signs in to the site.

There is also a 'Default Search' category.
Products in this category are used for search results first.

'Quick add' categories are used to specify categories where products can be added in bulk to the cart from the same screen.

5.3.3. Browse Categories links

In the left-hand panel is a section labeled 'Browse Categories.' You can click on one of the -indented- categories to begin editing it directly, or click on the [Choose Top Category] link to view a list of links to all Parent categories.

5.3.4. Catalog Administration Main Page

The catalog administration main page has several small menus for finding catalogs, categories, or products.

The first three menus allow you to edit catalogs, categories, or products by their respective IDs, or create new catalogs, categories, or products.
The last one allows you to look for a product using an ID other than its product ID, such as upc or isbn number (see below.)
Under these menus are two more links.

Auto create keywords

Fast load catalog into cache.

Auto create keywords

Auto create keywords will create keywords for all of the products identified with the current Catalog.
The keywords are based on product descriptions and are used for searching for products.

Fast load catalog

Fast load catalog into cache will load all products and product categories into the cache; this is good for improved application performance.

	only basic product and category information from the first Product and Category tabs is loaded, so additional information such as content, associations, and pricing will still have to be retrieved from the database and cached later by the applications.
5.4. Categories
5.5. Product Features

To Sell and to Differentiate Products, Features are characteristics used to sell and to differentiate products.

The Apache OFBiz catalog manager allows you to define any feature set you wish for your products.
Typical features include size and color.

In Apache OFBiz, features are associated, or applied, to products as Standard Features, Selectable Features, or Distinguishing Features.

5.5.1. Standard features

Standard features are features which are associated with every instance of a product.

An example might be the brand name of a product — all instances of the product share the same brand name.

5.5.2. Selectable features

Selectable features are features which the customer selects one from many available choices.

For example, a shirt may be available in White, Blue, Green, Yellow, Pink.
These colors would be selectable features of the variant product shirt, and the customer would be prompted to choose a color.

Each color, though, would be a standard feature of the physical product.
Thus, White would be a selectable feature of the virtual product 'shirt' but a standard feature of 'white shirt.'

5.5.3. Distinguishing features

Distinguishing features are features which distinguish one product from another and are used to show the customer which item she chose.

5.5.4. Working with Product Features

Click on Features tab.

Defaults to Product Features

5.5.5. Create and Maintain Product Features

These screens are for creating and maintaining product features, which are features or characteristics that are available for products.

Here you will define what features can be available for products.
Later, when working with the products, you will have a chance to define what features a particular product may have.

5.5.6. Feature Categories and Feature Groups

Notice the sub-tabs for Feature Categories and Feature Groups.

These are both used to help you organize your product features.

Each feature can only belong to one category but as many groups as you need.

For example, you can have :

a colors category that has colors White, Blue, Grey, Green, Yellow, Pink, Red, and Orange

and a sizes category that has sizes XXS, XS, S, M, L, XL, XXL.

Then, you can have :

one group for shirts that would have colors White, Blue, Grey and sizes S, M, L, XL, XXL,

and another group for dresses that have colors Yellow, Pink, Red, Orange and sizes XXS, XS, S, M, and L.

5.5.7. Add Features to a Category

Once you have created a feature category, you can click on it to add features to it.

There is a link [Create new feature] which takes you to a screen to create a new product feature.
Below this link is a list of product features already in this category.

Important fields for product features are listed below.

5.5.8. Feature Categories

Click on [Feature Categories] (this is the default screen when you clicked on 'Features' above), and you will see a menu for editing a particular feature, if you remember its feature ID.
(If not, you can edit it from the feature categories below.) Next, you will see a list of feature categories and their parent categories.

The categories' ID codes are highlighted, and you can click on one to go to the feature category.

At the very bottom is a menu for creating a new feature category.
Here, you would enter the new feature category’s name and specify a parent category for it (if it has one.) The category ID is automatically created for you.

5.5.9. Working with Feature Groups

Click on [Feature Groups] and you will see a screen showing a list of available feature groups, and an option to create a new feature group at the bottom.

Click on the ID of the feature group, and you will be taken to a screen which shows all the features in this group (if there are any) and a menu to add more features to this group.

Like feature categories, the IDs of feature groups are automatically created.

5.5.10. Implement Feature-based Product Search

You can associate feature categories or feature groups to a Product Category.
Buy doing this will provide web store customer feature based product search ability.

If customers choose to search within a given category and that category has features associated with it then they will be displayed as selectable filtering options (based on the associated product features) on the search form.

5.6. Promotions
5.6.1. Similar to Price Rules

Promotions are similar to Price Rules (see Price Rules, below) but are used to record special promotional offers which apply to the entire order, rather than prices for a particular product.

For example, the promotional manager can be used to set up rules to give customers a percentage discount if they purchase a minimum quantity, or to create a coupon code.

	Promotions are tied to specific stores, whereas price rules are applicable to all products
(although you can specify the website, product catalog, or category for which a price rule is applicable).
5.6.2. Opening Screen

The opening screen lists all promotions which are currently available and a link for creating additional promotions;
click on one to go to a promotion.

You will also see a series of four tabs: [Promo], [Rules], [Stores] and [Codes].

5.6.3. Promo tab

At the top is general information about this promotion.

Each promotion has an ID, a name and a longer descriptive text, which are shown to customers.

If no text is entered, Apache OFBiz will automatically generate text for you.

5.6.4. Rules tab

Rules for promotions are used to determine what actions should be taken in the promotion.

Each promotion can have multiple rules, and each rule can have multiple conditions and actions.

If a promotion had multiple rules, they would all be checked in sequence, and the rules whose conditions were true will be activated. This is especially helpful for complicated promotions that have multiple offers.

5.6.5. Stores tab

The stores tab shows a list of product stores in which this promotion is active.

You can add additional stores here or delete them.

5.6.6. Codes tab

The codes tab is used to associate codes for a promotion, similar to coupon codes.

5.7. Price Rules
5.8. Product Stores

A product store has all the information needed to sell products.

It is composed of a series of catalogs, which are composed of product categories and products.

Each store can have its own shipping, fulfillment, notification, promotions, payment processing, and tax calculation policies.

A product store can point to several different websites, allowing the same products to be sold on multiple hosted sites or domains.
Alternatively, multiple stores, each with their own website, can be set up to allow different pricing and fulfillment procedures for, say, different countries or different market segments (wholesale versus retail.)

5.8.1. Main Store screen

Go to Catalog Manager

Go to Catalog Manager - Stores tab
Stores tab (with a store selected) brings up

Roles,

Promos,

Catalogs,

Web Sites,

Sales Tax,

Shipping,

Payments,

Emails,

Surveys,

and Override tabs to perform a host of other store-related functions.

Select existing store

If none, Create New Product Store

Complete fields

Click on Update

5.8.2. Why use stores?

The 'Stores' tab in the catalog manager as used to define all the properties of a working store, is a group of products sold together under the same policies.

Stores greatly improve the flexibility of Apache OFBiz applications.

It is possible for a company to set up multiple stores, each with its warehouses, fulfillment policies, currencies, languages, promotions, and look-and-feel.

These stores can be web-based b2b or consumer ecommerce stores or for internal order entry.

They could even be in different countries with different shipping and taxation rules.

5.8.3. Working with Product Stores

When you click on 'Stores,' you will see a list of product stores that have been defined.
Click on one and you will see several tabs for administering different aspects of that store. Some of those aspects are discussed below.

Product Store

This very complete screen provides entry for all of the myriad choices available which define the store and establish parameters.

Roles

Defines parties with specific roles for this store.

For an employee to be able to take orders using the internal order manager application, he must be defined as a 'Sales Representative' here.

Restrictions are enforced through the Party Manager - SecurityGroupsList which grants rights according to party roles.

Promos

Shows a list of active promotions for this store.

Catalogs

Catalogs which are available for the current store and the sequence in which they are to be shown to the user in a navigation menu.

Web Sites

Websites which are related to this store.
This is directly used to link a store to a web application.

Each web application has a configuration file called web.xml, and it is defined to reference a particular web site.
The web site in turn is defined to relate to a product store.

Thus, by setting a store on a web site, it becomes 'live' on that web application.

	It is possible for a web application to have more than one store associated with it, as long as the application knows how to use the correct one.
Shipping

This page shows the shipping options available to store customers.
A list of shipping options and their pricing is shown.

Click on View for a shipping option shows all the settings for this shipping option.
At this point, this tab can only view shipping options available and can not be used to define them.

Payments

his is used to set up payment processing for the store.

The payment processing interfaces are defined as Apache OFBiz services.

Each payment method will have a series of service types available to it, such as for authorizing, capturing, and refunding payment.

This page links the payment types and the services together by their purpose.
Thus, one service would be used for credit card authorizations, another for credit card capture, and so forth

Emails

This defines emails which the store would send to customers.

The actual email services are either mounted in the controller, such as the order confirmation email, or from scheduled services, such as back order notifications.

This page defines where the template for the email is located on the file system, the addresses and subject of each email, and a content type (which can be left blank).

Surveys

This page is for adding surveys to the store.
Surveys can be associated with certain events or with products and categories.

Override

Allows certain keywords to be ascendant at this store for a particular time period.

Segments

Identifies the Sales or Market Segments targeted for this Store.

The actual assignment is made under the Marketing tab > Segment sub-tab.
Here under the Product Store you will see a summary table of those assignments along with links to make any additions or changes.

5.9. Configurations
5.10. Image Management

The Image Management module manages many kind of image what user want.
There are various functions including 'Gallery', 'Upload', 'Approved', 'Manage' etc.

Go to Catalog Component > tab Image Management.

5.10.1. How To Add Security Group For Image Management User

There are three security groups related in the Image Management including 'IMAGEADMIN', 'IMAGEAPPROVE' and ' IMAGEUPLOAD'.

Howto add a security group

Go to 'Party' component.

Search 'UserLogin' or 'Party Id'.

Click 'UserLogin' or 'Party Id'.

At 'User Name(s)', click 'Security Groups' button.

At 'Add UserLogin go to Security Group',

select group 'IMAGEADMIN Image Management Admin' for use all operations in the Image Management.

select 'IMAGEUPLOAD Image Management Upload': To add party’s permission for uploading,

select 'IMAGEAPPROVE Image Management Approve': To add party’s permission for approving.

Howto Add Role For Approve Image To Party Id

Click partyId into party’s screen already present.
Select the submenu 'Role(s)' to add the role to party

There is Add To Role screenlet, select role 'Image Approver'(on the combobox role type Id) then click 'add' button.

5.10.2. Gallery

Gallery shows all images which have approved.

	Everybody can access Gallery function.

Click 'Gallery' button, then choose a 'Product Id' by type or click a find icon.

Click 'Submit' button, then you will see all images which have approved.

You can click 'Share' button that generates any codes to share your images to any people.

5.10.3. Upload

In this function, you can upload image files into system.
You can upload many image files up to 10 files.

	You must have Image Management Upload permission for access Upload function.

Go to 'Upload' section, Enter 'Product Id' by type or click a find icon.

Optional, you can specify the size of images.

Then click 'Browse' button to choose image file(s).

Click 'Upload' button.

5.10.4. Recently Approved

In this function, you can see the images which have been approved for 14 days recently.

	You must have Image Management Admin permission for access this function.

Click 'Recently Approved' Button, then you will see the lists of recently approved product which are separated by date.

Click on product id to see its images with details.

5.10.5. Approve

In this function, you can set the status of each image including 'Approve', 'Pending' and 'Rejected'.

	You must have Image Management Admin permission for access this function.

Click 'Approve' Button, then specify the status of each image.

Choose 'Approve' status for approve image.

Choose 'Reject' status for reject image..

Choose 'Pending' status for pending image..

Click 'Submit' button.

The images will be approved if all image administrators approved them.
But if only one person rejects an image then that image will be rejected.

5.10.6. Rejected

The Rejected function shows the images which have rejected.

	You must have Image Management Admin permission for access this function.

Click 'Rejected' button, then you specify the reason of rejection each image.

Then click 'Submit' button.

5.10.7. Manage

You can edit image such as add frame, crop image etc.
You can also add caption, sort order, enable image and choose thumbnail in this function.

	You must have Image Management Admin permission for access this function.

Click 'Manage' Button, then you can choose action including 'Frame', 'Crop' and 'Rotate' (see below for more details).

Enter your image caption.

Sort order of image by enter order number.

Enable image by tick enable checkbox.

Select image thumbnail of product.

Click 'Submit' button.

Frame

In Frame function, you can merge your image with the frame image (transparent image file e.g. PNG type) together.

The frame image should be larger than selected image.

Choose 'Frame' then choose the image you want to merge frame.

Select the frame image by browsing transparent image file, such as PNG type.

Click 'Upload' button to upload the frame image.

Enter width and height of image.

Optional, you click 'Preview' to see example image.

Click 'Create' button.

Crop

You can crop any images in this function.

Choose 'Crop' then choose your image.

Move your cursor on the image, then drag your mouse to crop image.

You can see the preview image in the right hand side.

Finally, you click 'Crop' button.

Rotate

You can rotate images in this function.

Choose 'Rotate' then click clockwise or counterclockwise button for ratating image.

'Submit' button

5.10.8. Replace

In this function, you can replace the selected image with other image.

The image which you want to replace must be approved first.

Click 'Replace' button, Enter 'Product Id' by type or click a find icon.

Then choose the image which you want to replace.

Choose the other image to replace with the selected image.

Click 'Submit' button.

5.11. Miscellaneous
6. Facility

The Facility Manager is used to manage a warehouse, a store with related inventory.

All operations relating to stock:

defining locations (in a hierarchical and multi-level ways)

receiving

picking, packing

shipping

transfer

return

physical inventory

…​

6.1. Facility management in UI
6.1.1. Receive Return

For details about Sale Return look at Return Process Overview

	What the customer needs from you at this point are three pieces of information to include on the outside of the package he is returning:

His original OrderNumber.

This Return Number (shown in the screen after the words 'Receive Return’and highlighted inside the link box).

The exact Return Address where you want him to return the item(s).
That may be different from the address shown on the package he received.

They should keep this information available for themselves in case they need to call back to check on the status of their return.

Facility Glossary
Inventory

These are goods are held for sale to customers. Inventory is also referred to a Stock. Inventory can be items that are bought for resale or it can be products that are manufactured and sold to the customer.

Stock

These are goods are held for sale to customers. Stock is also referred to as Inventory. Stock can be items that are bought for resale or it can be products that are manufactured and sold to the customer.

7. Order

The order manager allows you to enter and maintain orders, quotes, requests and report on them.

It allow to manage purchase and sales orders from the creation and approval to the goods packing and shipping.

7.1. Overview

A sales order is an agreement between a business association and a customer concerning the delivery of products or provision of services. This process involves order capturing, order status management, payment terms and method setup etc.

A customer can place an order from the storefront or a customer service representative (CSR) can place the order on behalf of a customer from the back end.

7.1.1. Business Purpose

A Sales Order from the customer notifies the business of customer wants. It tells the business who is the customer, what are the products or services ordered, what is the payment term and method, what are the billing and shipping addresses, any special instructions for delivery, order priority etc.

Sales Order document is created in the system with a unique reference number that comes in handy for better customer service afterward. It enables a business to offer the customer to have a choice to change ordered items. The customer also gets the details of the order which can be accessed through his profile on the storefront (eCommerce front) at any time if registered or else can use the order reference number while contacting the business for reporting any issues.

Order status transitions help business to filter orders based on status (Created, Approved, Rejected, Completed etc.) Current order status tells the state of order in the system at any given time which is used effectively by CSRs while communicating with customers over the phone.

Order payment terms and method tells the business how the order payment is going to be processed. It helps in timely fulfillment of orders, which is key to success for any business. Same is with billing and shipping information on the order, it tells the business which address to be used for invoicing and which one for shipping. Having an effective order capturing process helps to engage your customers.

The Accounting manager keeps track of financial charges, credit card processes, and receipts of payment. The link from the Order Manager to the Accounting Manager is the Invoice Number

A customer always provide shipping method details to let the business know about his shipping preference to ship the order and in other ends, CSR always captures shipping method along with special instructions for delivery.

7.1.2. Create Order Diagrams

CSR creates a sales order for the customer from the backend as per the given information like personal details, contact information, billing and shipping information, and payment terms and methods. A customer can create a sales order from the storefront (ecommerce) as well.

Start process with screen Order Entry from Order appl on Apache OFBiz demo site

Sales Order from Backend Level 1

Product Store and Customer Details

Add Item(s) to cart

Set Shipping Method and Payment Term

Create Order

Sales Order from Backend Level 2

Product Store and Customer Details

Order Name and other Information

Add Item(s) to cart

Set Shipping Address

Select Shipping Method

Payment Terms

Additional Party Entry

Create Order

Sales Order from Backend Level 3

Product Store and Customer Details

Add Additional Information

Add Item(s) to cart

Set Shipping Address

Select Shipping Method

Order Terms

Payment Method

Create Order

7.1.3. Order Status

An Order Status is an easy visual indication to alert business about the orders requiring actions or not.
Order status is indicated on Order View screen on top of main part and just below there are history of change.

An Order can have the following status:

Created

Approved

Processing

Sent

Held

Rejected

Completed

Cancelled

Status change on actions on order (ex: payment is received) or on direct action button on Order View screen on main part in top menu bar.

Order Status diagram

Approved Order

f you have an approval process, you will want to check over the details to confirm that the shipping information is complete and accurate, that the billing details are acceptable and that the requested shipping dates (if specified) are within your company’s capabilities.

When all is ok click on the [Approve Order] link in Order View

7.1.4. Update Order

A [CSR] can edit or update in order to make changes in it based on customer requests or can add notes for handling.

Overview update order process diagram

Find Orders or List Orders or Orders of the day

Order View

Detail update order process diagram

All informations on order are modified, but depending on order status or packing / shipping started.

Find Orders or List Orders or Orders of the day

Order View

7.1.5. Payment Terms and Method

Payment Terms are conditions agreed between business and customers for the payment of invoices.

Selecting Payment Terms and Methods are key things in fulfillment of any order process.

Payment process diagram

Select Payment Term

Select Payment Method

Payment Method diagram

Depending on payment method process is not exactly the same.

Credit Card

Billing Account

For information about Billing Account look at Accounting - Billing Accounts

7.2. Orders management in UI

Sales and Purchase management are done on the same screen, so depending on what you want, don’t forget to select the correct Order Type.

7.2.1. Orders of the day

Upon opening the Order Manager, your first screen will be a short sale "dashboard of the day" with: * the new sales orders (enter today) * the top 5 of the product sales today

This screen is a portal page, so in some case it’s possible to choose which portlet to put.

On the first part, only order with status and type selected in the <Order List> screen appears. For example, if you work on purchase department, on Order List screen, if you select purchase type and only Approved status, on the main screen you will will see only purchase order created today and already in approved status.

Even if this screen is useful, it’s also a example a developer can personalize to give orders to follow in your business situation.

7.2.2. List Orders

The focus of this screen is order status
retrieve all orders for one type and a selection of status.

It lists all the current orders in need of processing. You should spot the one prepared above in the list; click on the Order Number to proceeed. If too many orders are listed in the first screen (List Orders), unclick the 'Approved' checkbox and click on [Submit]. If still too many, unclick either the 'Created' or the 'Processing' status checkbox and try again.

Using the check boxes and the [Submit] link, you will bring up a list of all orders in any category selected.

Order list give you main information on parties associated to the order and a link to the order details.

To narrow your search, use the Find Orders tab. This brings up a complete search screen which will take any possible parameters to find the one you want to work with.

7.2.3. Find Orders

This screen brings up a complete search screen which will take any possible parameters.

Enter information about the order and click on [Find].
Existing Orders are listed and you can complete it or modify it, if that is what the customer is calling for.
Or, reduce the number or Orders presented by entering parameters in the search screen, above (you may need to click [Show Lookup Fields] and trying to find what you want more specifically.

There is a direct action button on the top left of the list, to directly change status

choose the action to be done in the drop-down

select one orders or more

click on <run action>

In the Order list, there will be a link from that order to the PartyID;
click on the ID and you are in the Party Manager > Profile page for the customer.
On the profile page, one of the links there is [New Order] which takes you back to the initial Order Entry screen, discussed below.

If specifics about the order are not known, you might prefer to find it through the Party. In that case, select [Lookup Party]. The Party Manager can link you back to previous orders.

7.2.4. Order View

This screen allow not only to view an order but also to change it

Note the link to [PDF]. This will create a PDF formatted document which can be used internally for paper processing the order or sent to the customer as an attachment or hard copy to confirm the order. The customer should be told that the Order Number should be referenced in any correspondence regarding the order.

Order Information Sections

Status and General Info
Notice the Status History? This tells you when the order was placed, when it was approved and, later, where it is at in the shipping process.

The section labeled 'Created by' will give you the login ID of the person taking or making the order. This is who you need to talk with if there are any problems in the original order. Remember, it could be your customer service rep or it could be the customer herself if the order came in through ecommerce.

Payment Information Section
This section will reflect the type of payment selected by the customer. If Debit or Credit Card, the card number last 4 digits will show; if EFT (Electronic Funds Transfer - electronic checking withdrawal), the bank account number will appear.

Shipment of the order against customer payment by check or money order will appear as shown below. It might be your practice to withhold shipment until payment is received. When it arrives, pull up the order and click on [Receive Payment].

Order Items Section
All the products, whether ordered or being sent as promos, are listed here. Note the many details shown in this section.

What do we need to ship?

Product Information links
Click on the [Catalog] or the [Ecommerce] link to get detailed information about the product from either of those sources.

Inventory is very important. This shows the Inventory ID for the item and whether enough inventory exists to fill the order. Here the Inventory number given matches the order quantity, indicating sufficient inventory to fulfill the order.

Status, The first line gives the current status. Beneath that is the history of status changes.

Adjustments, Jurisdictions and rates are given for taxes applied. Amounts of the adjustment are shown in the column to the right.

Beneath Adjustments is the Price Rule applied to determine the effective price for the item.

The Ship Groups listed, If the order was being split between two or more recipients, each would have its own Ship Group with the quantity going to each one being listed. In this instance, there is only one destination so there is only one Ship Group.

Pricing and adjustments information, To the right in this section is all the financial details on each item. When taking back a return, be sure that no more is credited to the customer than what the order shows for a charge.

Actions Section
[Quick Ship Entire Order] is a powerful link built on a great many assumptions that everything needful to complete the order is in place, including financial arrangements, inventory, manpower to fulfill the order, etc. This powerful action will by-pass many of the normal processing screens, accomplishing most steps behind the scenes. See the topic QuickShip Fulfillment Path for more details

Shipment Information Section
Steps for shipping the order start here.

Remember there are two different uses of the word 'Splitting' and you need to know which meaning is being used. When the phrase 'Splitting Preferences' is used here we mean: Does the customer want a part of his order to be shipped as soon as any portion is available, allowing the delayed balance to follow at a later date? If splitting is not desired, all elements of the order must be gathered together for a unified shipment.

In this order as shown, if you were to click on the link [Allow Split], you would reverse the customer’s original choice to wait for all items in one order. Do NOT select that link unless the customer has informed you of a change in her former preference!

When the next item is considered, 'Ship Group,' we would be looking at a Split Order with part of it going to one destination and the other part to another if there were two Ship Groups indicated. As the order in this example shows only one Ship Group, you can know that all items are destined for the same location.

The [Pack Shipment For Ship Group] button Initiates the preparation of packages for shipping the order under the Facility Manager. This is just one of many screens where this step can be triggered.

There are several approaches to having the products Picked and Packed in the system. One method is to open the Facility Manager, click on the Facilities tab, select your Facility, then click on the Picking tab.
After identifying and submitting orders that need Picking to the floor, you move over to the Packing tab. This one is more individualized; you can see the screen shot below. You must enter the Order number, then enter the Product ID for each item as it is accepted.
A much easier method is right there in the Order Manager. Pull up the Order and look under Shipment Information. See the link labeled Pack Shipment For Ship Group [00001]? Click on that and you will see the second screen below.

The link [New Shipment for Ship Group {00001}] will bring up a working screen in the Facility Manager to allow you to begin the Warehouse Path, discussed below.

QuickShip Fulfillment Path

QuickShip presumes several things:

That inventory is on hand and ready to be shipped or taken from the premises by the purchaser.

That third parties, such a shipping company, a warehouseman, a picker, etc., are not needed to fulfill the order.

That the method of payment is acceptable: that the customer has paid or that credit has been extended for payment to be received later.

Essentially, QuickShip allows OFBiz to bypass all of the procedures for identifying, picking, packing, billing and shipping so that the package is immediately dispatched.

Click on 'Quick-Ship Entire Order'

Confirm Quick-Ship Success

and the screen shows

Under the ' Order #WS10082 Information' section

  Status History Current Status: Completed
  ________________________________
  Completed - 2006-02-16 20:18:35.281
  Approved - 2006-02-16 10:11:26.437
  Created - 2006-02-16 08:29:56.265

Under the Payment Information section

Invoices # [10060] has been added in a new sub-section.
Click on the Invoice # to view the invoice in the Accounting Manager.

Under the Shipment Information section
Splitting Preference no longer presents an opportunity to change the preference; chosen method is displayed.

Shipments affords two links:

#[10050] → Facility Manager > Shipments tab > View Shipment document 10050.

[Packing Slip] generates a PDF document for including with the order as a Packing Slip.

[Quick-Refund Entire Order] link could be used to immediately reverse a completed order which had been charged to a Credit Card, an Electronics Fund Transfer (EFT), or a Gift Card. Best used before the items leave the Facility. If already shipped, use the [Create Return] link.

[Create Return] brings up a working screen to begin the complex process of bringing products from the customer back into your facility, reversing charges, etc.

The Quick-Ship Shipment document
Even though the 'Shipment' did not follow a complete course through the Facility Manager and elsewhere, paperwork is still needed to confirm stock deletions and track where products have gone.

You can see the highlighted 'Shipments #' link. Click on that number to see the details as shown immediately below.

View Shipment Details
In so much as shipping methods were specified in the ordering process (UPS Ground), this example is somewhat skewed. If you knew the customer was going to retrieve the products personally, you would so indicate in the original order entry process.

You will notice in the document that inventory adjustments and other issues are all presented. You can bore down into any of the highlighted links or select one of the sub-tabs to bring up further details about the order, the products, the customer, etc.

A final link to follow is the 'Generate Shipment Manifest Report' which produces a PDF form to send with the purchaser or to serve as a hard copy for your internal purposes. An example is given below.

Warehouse Fulfillment Path

The Sales Order process is not complete until the Shipment is generated. This is begun by clicking on the link [New Shipment for Ship Group #].

The following screen in the Facility Manager is sometimes brought up with the Order Number and little else completed in it.

When you generate the Shipment by clicking on 'New Shipment For Ship Group [00001]' link, your screen might not appear as completed as shown above. Before you enter information in the address fields, for example, try clicking on the [Submit] or [Update] link at the bottom of the screen. The system usually will retrieve these addresses from the Sales Order and from the Party Profile to enter the address ID numbers as you see here.

The Status ID wil generally be updated as you go through the following steps. That Status includes Scheduled, Picked, Packed, etc.

If the Order had a desired delivery date, or if you have a good idea what the shipping dates could or should be, here and now is a good time to complete them. Those dates would be the Ready date, the Ship date and the Receive date. The Latest Cancel Date is the last possible moment the order can be canceled before it is committed to the shipping company.

Destination Facility would seldom be used for retail customers. This would be for wholesale customers or established high-volume Business to Business clients.

7.2.5. Order Entry

In this screen you can create a Sales order on the first part, or a Purchase Order on the second part.

For Purchase Order entry, all parties with role "SUPPLIER" are listed in the drop down supplier.

Using the top portion labeled Sales Order, identify the Party placing the order, either with their User Login Id or Party Id. The search tool can be a help.
You have several means to reach the PartyID for the person or company which wishes to place an order.

Enter the PartyID or LoginID directly if either of those are known. OR

Enter the known information, such as name in the search fields; the return will appear in the table as shown below. OR

click on the link to the Popup search tool to the right of the User Login and Party ID box in the Sales Order section;
and you have a search tool where you can either scroll the listing of known Parties or enter the information you might have and let the search find the party for you.

If specifics about the order are not known, you might prefer to find it through the Party. In that case, select [Lookup Party]. The Party Manager can link you back to previous orders.


Basically, you cannot place an order until the Party is identified. There are several ways to establish the Party ID from within the Order Manager. Since several of those ways take you back through the Party Manager, it might be just as easy to begin with the Party Manager.

Placing a New Order

Once you click on the [New Order] link, you have begun the order taking process through the Order Manager. The internal, 'behind the scenes' processing of the order is very similar to the Ecommerce order. Unlike the Ecommerce ordering process, the customer will not see all of the screens you have available; only the person taking the order can see all the special offers and the details presented. This is why it is important when taking an order over the phone or completing a transcription from a hard copy or email order, that the processor be alert to special offers or to error messages that might appear.

Order from eCommerce

When a customer first enters the Ecommerce website, they are challenged for a Username and a Password. If they are first time visitors, they are provided an opportunity to create an account. If they have visited before, they are asked for their username and password. All of their entries are automatically logged into the OFBiz databases for your review in OFBiz and for their ordering processes. They never see any part of OFBiz except the Ecommerce interface which includes the content posted from OFBiz to the Ecommerce portion as called up by their preferences.

7.2.6. Order Entry Init

Order Entry begin with this screen. Using the top portion labeled "Sales Order" identify the Party placing the order, either with their User Login Id (when a ecommerce customer give it to you) or their Party Id. The lookup can help you to search the Id if you have only name, or other details.

Sales Order vs. Purchase Order
Disregard the Purchase Order section of this screen. That is only used when you (as a representative of your company) are ordering product or services from another vendor for your company’s use.

Product Store
It is probable that your CSR (Customer Service Representative) is processing orders for more than one 'Store' which could be an actual physical presence or a virtual shopping center seen on-line by the customer.
Confirming the correct Store at this point is critical.

Sales Channel
How did this order reach you? Here are some possibilities:

The customer is standing in front of you at your terminal, probably in an actual store front — POS Channel.

The customer called in the order and you are on the phone with them at this time — phone channel.

You are reading from a fax sheet, an e-mail printout, a letter or order form — FAX channel, e-mail channel, or snail mail channel, as appropriate.

Some other party gathered one or more orders together and has forwarded a consolidated order to you — affiliate channel.

You are not taking the order but it is being processed through the ecommerce website — defaults the category to web channel.

7.2.7. Order Currency, Agreements, and Ship Dates

On a back office perspective, order entry can be use on a B2B context,

order Name and PO number are customer informations

default currency used for this order

Catalog and Dates are use as default value on next screen

Across the top bar is the link button [Continue] to go to the next step

7.2.8. Add Item(s) to cart

Primary order entry screen is complex, and after one item has been entered, promotional items were added automatically and so more information.

Order Header Info Before proceeding with the order entry, confirm that the Party is correctly identified, and that the Currency is in the correct denomination.
Click on the Party ID number to go to the Party Manager for confirming or updating information about the Party.
A running total of the current order is displayed for quick reference.

Shortcuts,


Quotes
If the customer refers to a quotation submitted to them from your company, go here to locate the Quote.

Create New Quote From Cart
Use the items accumulated in the Shopping Cart and, rather than fulfilling an order, prepare a Quotation for the customer. This Quote would go into the system established for Quotes as discussed under the Order Manager.

Create a Request for Quote
This more formal process provides a vehicle to identify products of interest to the Customer and assemble a Quotation based upon the Request initiated here. The Request is initially based upon products identified in the Customers Cart, and is created for this named Customer. To follow through on this, see the Requests tab under the Order Manager.

Find Party
Takes you to the Party Manager - Find Party screen.

Create Customer
If this Order is for a new Customer, here is the link to the Party Manager to establish the information needed in the system.

Change Party
Cancels the current Sales Order process and takes you to the initial Order Entry screen where you need to identify the Party.

Create New Product
If your customer asks for a product which has not yet been established in the system, and you know you can get it for them, this link allows you to quickly create the product identity within OFBiz before proceeding with the order.

Quick Add
Let’s say that you are dealing with a customer who knows what he wants and you do not need many of the features and links given on this particular screen. By choosing [Quick Add] you are taken to a simplified ordering screen where the order taking can be quickly accomplished. Compare the current screen with the Quick Add screen to visualize the differences.
The Quick Add screen removes many of the links and features of the full Order Entry screen, but may easier to use.

Shopping List
Brings up a table of the Party’s existing Lists. It’s possible to [Quick Add All] to brings all of the items on a selected List into this current Order, or Choose single items from a selected Shopping List ([View List] button)

Choose Catalog
Your customer might be ordering from your Spring catalog, your Outdoor Specials catalog, or whatever Catalog you may have placed into his hands. Establish the Catalog here so that prices reflect the Catalog he sees. This will also govern what products, special offers, discounts, and other details of the marketing process are presented in this screen and for the order itself.
Default value is coming from previous screen.

Search Catalog
While talking with the customer, this will give you access to the Catalog to help him locate what he wants.

Browse Categories
Here is another way to find products within categories.

Create Sales Order section


Links to processes
Across the top bar are these link buttons:

Clear Order which removes all data from the screen except the Party ID.

Remove selected, remove all items selected

Recalculate Order which is selected when a quantity or other adjustment has been made.

Finalize Order which should not be selected until all entries have been made on this page.

This one takes you to the next step in the order process.

Finalize Order with default option, less step than previous button

Quick Finalize Order which consolidates several steps into one screen for faster completion.

ProductId,
Popup Search tool help you finds products quickly.

Quantity
How many the customer are wanted

Desired delivery date (optional)
Note that this does not say Promised delivery dated. If the customer indicates a date when he would like to have the delivery, this date can serve as a guide to when to process the order in house. It also guides you to recommend the appropriate shipping method, ensuring compliance with this date but at the lowest cost to the customer.
You can used the popup calendar to find the date.
Use as default desired delivery date for next entry, if checked, will keep this date for all the items ordered.

Ship After Date (optional)
This item (and also the shipping group to which it belongs) will not be pick before this date.

Ship Before Date (optional)
To have warning if it’s not possible to pick or to produce before this date.

Reserve After Date (optional)
No stock reservation will be done before this date.

Comment
Be judicious what you write here: this may appear on paperwork reaching the customer such as packing slips, invoices, etc. This may be the place for comments such as 'wrap each item separately' when several units of the same item are being sent in an order to the same address but are intended for different recipients, for example.
If the comment applies to more than this item in the order, check the box labeled Use as default comment for next entry

Add To Order
This button should not be clicked until all details in this section are confirmed: quantity, product, dates, etc. It updates the totals and enters particulars into the next section.

Add Order Items to Shopping List section


Add To Shopping list
First select a list from the drop-down box, then click on [Add To Shopping List]. All of the ordered items to that point will be added to the selected List, in the quantity ordered.

Order Items section
All the informations about items in the cart.
In this section it’s possible to modify Product description, Quantity, Price, Date, …​, to validate and save modification click on [Recalculate Order] on the Create Sale Order top bar.
In this section there are all items, including those added by promotions (the gift !) and if there are some choice, it’s the place to give the answers.
Note the informations beside the Inventory buttons :

ATP : Available To Promise, quantity in the inventory not yet reserved

QOH : Quantity On Hand, quantity in the inventory

Promotion/ Coupon Codes
Enter the code number from other Promotions or Coupons and click on [Add Code]. Appropriate discounts or promotional consideration will be calculated into the order if the Code is currently valid.

Special Offers
Give some promotion which can be applied if you add some product or quantity. It’s useful when you have the customer on phone, to propose him additional product to access for a specific promotion.
Click on detail for a promotion to have the detail condition and result.

You might also be interested in
Strictly a promotional tool, here is a selection of items which you can offer to the customer before moving past this screen. Simply enter the quantity and [Add to Cart] when he indicates acceptance.

Promotion Information
In first, this section, all those Promotions which have been applied to the order are given. Select [Details] to obtain more information.
In second part, the ordered items which made the customer eligible for a promotion are given.
Every item being shipped as a promotional give away is listed as well.

When all items is entered click on [Finalize Order] to give all other order conditions.

7.2.9. Quick Finalize Order

In this screen you have a summary of 3 screens for details look at

Set Shipping address and Group

Order Option Settings

Payment setting

7.2.10. Set Shipping address and Group

On this screen it’s possible to choose

the delivery address and/or create a new one,

to create multiple shipping group, and so multiple delivery address or multiple delivery date

the party to shipping to if it’s not the same as which one ordered

7.2.11. Set Item to ShipGroup

If you have defined multiple ship group, in this screen you can choose for each item (and each quantity) with which group it will be ship

7.2.12. Order Option Settings

There are the same options list for each Ship Group, except for internal and ship Notes

Shipping methods
Select the radio button for the preferred shipping method. Consider the customer’s desired delivery date, the availability of product, your order processing time, and the transportation time required before agreeing with the customer to a specific mode of shipping.
Note how the cost of each method is already determined and displayed for you. Let the customer know the cost involved and obtain his consent to the cost.
Parameters about shipping cost are associated with Product Store (entered in first screen).

Single or multiple shipments
Sometimes the customer needs to have all parts of the order available at the same time; they will elect to wait until all of the items are available before shipping. Others want whatever items are available immediately and prefer not to wait for the rest. Select the radio button to match their preference, but explain that an additional shipping cost might be incurred.

Special Instructions
If you get them, record any special instructions here. These will appear on the Pick Sheets.

Gift? / Gift Message
The Yes radio button selection will direct packers to Gift Wrap if that was requested in the order. Also, it directs them to attach the Message which follows in the next section.

Ship Before / After Date (optional)
The customer could have any one of many different reasons for wanting the order to be shipped before or after a specific date. For example, budget that must be spent within a certain quarter would require the order be fulfilled before the end of the quarter. Similarly, if the item is not budgeted until next quarter, but they want to receive it early within that quarter, they might specify the first day of the next business quarter.
Use the popup calendar to identify and insert the date.

7.2.13. Order Term

If there are multiple "payment" term, it’s the place to enter them. It’s optional and you can enter as many as you want.

Various payment terms in OFBiz are:

Financial

Payment Net Days

Late Fee (percent)

Penalty for Collection Agency

Non-compete etc.

7.2.14. Payment setting

Payment method

How will the customer pay ? Select the radio button to correspond with he payment method preferred by the customer.
Billing information is to completed when credit card or eft payments are not used.

Various payment methods in OFBiz are:

Billing Account

Cash

Cash on Delivery

Certified Check

Company Account

Company Check

Credit Card

Electronic Fund Transfer

Financial Account

Gift Card

Gift Certificate

Money Order

Offline Payment

Paypal

Personal Check etc.

7.2.15. Additional Party Entry

There may be reasons for associating another Party or Group with the order. For example, the person placing the order might be an member of an existing customer group, such as a shopping club, or they might be a purchasing agent for a company and need to be identified with that company.

When you select to identify another group or individual for association, a process will be followed.
Select a Party (use the lookup or auto-completion in field) and after the apply button you have to select which role for this party for this order. Only Existing role associated with the party selected appear.

7.2.16. Order confirmation

If there are any discrepancies in the order, this the time to fix them. Click on the appropriate link on Order Confirmation Top Bar to be returned to the applicable screen.

When review is finished and everything meets with the customer’s approval then click on [Create Order].

7.2.17. Order Entry is now completed

Congratulations! You have completed all the aspects of entering an order into the system. Be sure the customer receives the Order Confirmation number. You might wish to mail or fax a copy of this screen to the customer for their reference.

Work has just begun behind the scenes for processing the order, however.

The next step will be giving Acceptance and/or Approval for the order which will trigger the processes needed to get the product out the door.

7.3. Orders Processes
7.3.1. Order Entry

Order entry can come from 2 path, Order management (back office) and eCommerce.

The company’s order entry process is discussed below under the Order Manager Path. You may jump there directly if you wish. Both the ecommerce entry and the Order Manager entry methods are discussed in this section to the point where the order entry is finished and Order Approval is needed before proceeding. It is valuable for you to be familiar with the ecommerce order entry process so that when a customer writes or calls in with a problem from that process you can be understanding and helpful.

Remember that an order can be canceled anytime up to the final confirmation point! Encourage your staff, especially your customer service people, to walk through an on-line order. They should try to see what happens when clicking on links or following paths that they wouldn’t ordinarily follow, just to see what happens! Then, when a customer describes their situation, you can relate to what they are seeing on their screen.

Order Manager path

Start process with screen Order Entry from Order appl on Apache OFBiz demo site and have a look at Create Order Diagrams

ECommerce Entry path

On default main screen eCommerce appl from Apache OFBiz demo site there are multiple widgets

Customer-centered widgets

language, If your site is available in more than one language, this user-friendly feature should be very much appreciated.

Mini-Poll Poll, you can do surveys with your customers here

Did you know? Marketing facts, comparisons, plugs, promos, whatever, can be introduced here in a low-key setting.

Browse Forums, links to forums, boards, or other websites are gathered here.

Special Offers, discounts and special promotions are presented here to reward the customer for purchases she has made and to encourage additional purchases. He can click on the link [View All Promotions] to see even more offers than what are presented here.

Ordering Process

Choose catalog,
your customer might be ordering from your Spring catalog, your Outdoor Specials catalog, or whatever electronic Catalog he may have come across online or through email. Establish or confirm the Catalog here so that details (including prices!) reflect the Catalog he has seen.
You might need additional login programming to arrive at the correct catalog if the customer is referred here through internet solicitation and linkage; asking the customer to specify the catalog he saw in the ad is not always productive. The catalog specified here will govern what products, special offers, discounts, and other details of the marketing process are presented in this screen and for the order itself. All of your marketing efforts must be coordinated with the presentation now seen by the customer. Your default catalog needs to be broad enough to cover all the instances where a customer’s choices or the login protocol bring him to the default.

Find Product,
opportunities to select and order product abound on this screen. The customer can follow whichever path attracts his interest or matches his needs. Those sections of the screen are each discussed below, not necessarily in order of appearance.

Featured Products,
the center of the screen is a list of all or most of the products under the heading of Featured Products. These can include a photo, description, price, promotional information, discounts, links to the catalog page, link from Virtual products to their variations, place to specify quantity being ordered and the most important link: [Add To Cart]. If more than one page of products is needed, scrolling links are given.
This section of the page is replaced by other functions when in use, such as search engines, category lists, etc. The customer can always return to this portion of the screen by clicking on the Main link on the upper Menu bar.

Additional information
Clicking on the product name either here or anywhere in the screen will bring up the product detail screen.
Every product name is hotkey to this information which drops into the center of the screen. You can establish what information will appear for each of your feature products.

Last Products,
Shows the product which the customer has looked at more closely by clicking on the product name; cumulative until [Clear] is pressed.

Quick Reorder,
Items from previous orders are listed here with a link to add them to this order in the same quantity as before.

Why offer re-order ?
Previously ordered items are displayed here. Studies have indicated that repeat customers are like gold. By presenting them with reminders of their previous purchases, you are both flattering them and providing an opportunity for another purchase of the same items.
This section also saves the customer from having to lookup the items she previously ordered. All are presented here.
Doesn’t this make the Shopping List concept unnecessary? Not really, because the Shopping Lists can carry 'Wish Lists' as well as previously ordered items. Also, Shopping Lists can be plugged into the order 'en masse' rather than item by item. There could be dozens of different Lists, each tailor-designed for a specific purpose.
For regular, heavy-hitter customers, you might want to limit the list of previously-ordered items to only the most recent 10 or so.

Browse Categories,
Categories are collections of related items. If the customer is looking for Books, for example, this would quickly get him to that portion of the inventory with presentations of Book titles or sub-catgories from which to choose.
Another way to consider this section: whereas the initial screen might show all the products (with scrolling), the Category selection will eliminate all products displayed except those in the Category he has chosen.

Search in Category,
A click on [Advanced Search] to have a dedicated search sub-screen
When the [Search In Category] link is selected, a simple but powerful search tool opens in the center screen. By making a few choices and entering a keyword or two, the customer can look for products that exist in the Featured Products category.
After a successful find, the customer is presented with a second screen, titled productFound. Here she has a couple of choices. If the returns are too extensive, she could refine the search. If she sees what she wants, a quick click on [Add To Cart] will select the product in whatever quantity she enters.

Last Categories,
As the Customer browses around the screen, looking into various products, categories, or other content, this section is constantly updated with links back to previously-viewed screens. Therefore, he will be able to quickly return to something that has stayed in his memory.

Browse Content,
Brings up a powerful tool for searching Content which could be documents, case studies, test results, testimonials, additional graphics, specifications, or whatever Content you choose to have accessible to the customer.

Search Catalog,
Entering a term in the search Catalog field resulted in a Product Search screen with some results.
Customers will use this to search the catalog by keywords, such as the name of the product or one of its features. You can help their search by keeping the Thesaurus updated.

Walk through an order
Let’s assume that our phantom customer, Sherry Shopper, has logged in, selected the Demo Catalog, and is ready to order. We will now follow her through the ordering process.

From previous orders, a click on the Order History link
Shopper repeats previous Order Items by calling [Order History]. Click on [view] to select
A complete order detail is shown.
Clearly still within the ecommerce website, here the shopper sees details of the previous order. She has options to [Add All to Cart], [Add Checked to Cart] or request an auto-ship [Send me this every month].
By checking on the item she wants to re-order, then clicking on [Add Checked to Cart], the item (in the same quantity as before) is added to her shopping cart. The screen will not clear out the earlier order, however, until she selects another process for finding her items. This gives her time to consider possibly re-ordering another item from the same list.

with Quick Add screen
Now Sherry can select from the drop-down screen to find a different Quick Add screen, she can add all of the items on this screen, or she can do what she wants, directly enter quantity for each she want.
If she elects to click on the link to the Giant Widget, the configuration screen appear, to be able to choose among the variants.
Sherry has choosen Silver over Black in the 4-Wheel version and can now click to [Add to Cart] (or to the [Add to Shopping List] link).

Final Choices
For her last two items, Sherry chose a His/Her Gizmo (GZ-9290) from the list of Quick Reorder items in the left-hand panel. Note how each time an item is selected, the display of that item is removed from the panel. Finally, on impulse, she added a Round Gizmo from the items listed under 'You might be interested in these as well:' You can see all these purchases now reflected in the Cart Summary.
Four Items were selected; four other were added by the system at no cost as promos.

View Cart
When [View Cart] is selected, all details of the order-in-progress are displayed to the shopper. She can change quantities, remove selected items, or even add more products as desired.


First, note how even at this point of viewing the cart, there is an option to quick add another product! From here, the customer can recalculate her cart or continue shopping (which returns her to the previous screen), or proceed with Checkout.

Second, there are various promotional messages around this screen to encourage further shopping.

Finally, many primary links are available. Notice that the shopper can go into her Profile, she can view established Shopping Lists that she might have created before, she can look at her own Shopping History, etc.

Proceed to Checkout

Confirm the shipping address, using the radio buttons. If a tax exemption applies, enter details.

Shipping address and details, confirm the shipping information, method, split, gift, and other details.

Payment particulars, both general methods and those on file for Sherry are shown. Use links to [Single use Credit Card], [Single use ..], etc.., when the order is being billed to an account not associated with the customer.

Review the Order to Checkout, Final Review gives the customer the opportunity to review and confirm all details about the order.

Submit the order, when the Submit button was selected, behind the scenes wheels were placed in motion, and the order is prepared to Accepted or Approved. Note the Order #WS10070 near the upper LH corner, that is the customer’s link to this order as well as your tracking number for processing through the Picking, Packing and Shipping processes.

Some comments on the process
The process is or should be as intuitive as possible so the customer is not frustrated or confused. Note the many links provided for shopping, searching for products, finding promotions, and so forth. You might want to add a link to a Customer Service bot where on-line help could answer their immediate questions. The final screen even shows a large [Continue Shopping] link, but the [logout] link is rather inconspicuous.

Also not discussed yet are the links to [Requests] and [Quotes]. Mechanisms are in place to let the customer go from the ecommerce screen to check on a Request or to view a Quote using links on the top menu bar.

Final discussion of the Ecommerce Path
What we show here is the generic look and feel of an on-line ordering system. The applications are there for you to make this reflect your image while maintaining the underlying tools. You do not need to use all of the marketing or redundant convenience processes shown, but it is good to practice running through this system as a shopper to understand how the customer will interface with your store. Let your customer be treated as you would like to be when you shop online.

7.4. Help for Order Reports

The Order Reports provide general information about orders in the system.

7.4.1. Initial steps.

If your reports look empty it may be required to initialize the warehouse entities in the BI component.

Go to :https://localhost:8443/bi/control/main[Business Intelligence]

Click "Quick Init DataWarehouse". System will automatic initial Data in the warehouse for Reports

Go back to : Order Reports.

7.4.2. Reports List
1. Sales Order By Referrer Report

There are referrers, link, totals orders, quantity totals and amount totals. They are grouped by referrer.

2. Sales Order By Channel Report

There are total Orders, total Items, quantity totals and amount totals. They are grouped by Sales Channel.

3. Sale Orders Discount Code Report

There are order, product, promotion and discount. This report is list of All orders.

4. Last Three Months Sales Report

There are products, prices, stock, sale out quantity and sale out total amount. This report is list of all products, it contains the sales and movements in last 3 months.

5. Coupon Sales Report

This report lists promotions, total orders, percent of total orders, total orders amount, percent of total orders amount and shipping amounts.

6. Sales Report

This Sales report contains paid and unpaid sales orders.

7. Net Before Overhead Report

Net Before Overhead Report is the profit calculation of paid-shipped orders and all the occurred fee excluding the overhead cost. They are grouped by Product Store Id.(Demo data for Net Before Overhead Report have in Product Store Id "B2CStore")

8. Product Demand Report

Product Demand Report is the report to show us which product sells good and which product doesn’t sell good or not selling at all in one account as well as for all accounts in last 4 weeks. They are grouped by Product Store Id.(Demo data for Product Demand Report have in Product Store Id "B2CStore")

7.5. Requests
7.6. Quotes
7.7. Returns
7.7.1. Return Process Overview

Sales Return is merchandise returned back to the seller by a customer. Sales return is a common concept used in sales and purchase terminology. The main purpose of the sales return is to provide easy returns to the customers to maintain long relationships with them.

While viewing an existing order, you can create a return from that order by clicking on the [Create Return] button (in Action section). That will take you to the quickreturn screen, from where you identify which item(s) the customers wants to return.

A sales return can be created for one of the following Reasons:

Excess quantity shipped

Excess quantity ordered

Defective Goods

Goods shipped too late

Product specifications are incorrect

Wrong items shipped

Sales Return types can be:

Store credit

Refund

Exchange

Store credit replacement

When a product is returned, the process impacts many different components of your business. Consider:

Customer must coordinate the physical return of the item(s) with your company. This is controlled by the document called the 'Return'. Be sure the Customer encloses a copy of the Return with his package or at least includes the Return ID on the shipping label and documents.

Your Facility needs to be alerted that the item(s) will be coming in from a source other than a regular supplier.

The value of the returned item(s) must be credited back to the Customer.

Taxes credited to taxing authorities must be reversed.

Costs for shipping, handling, perhaps re-shelving, must all be accounted for.

Possible replacement of the item must go through the entire Order Fulfillment chain.

The returned item(s) must be inspected with a determination made whether to:

place an item back into Inventory for re-sale; OR

repair/ re-furbish/ re-packag before return to Inventory; OR

return a defective product to YOUR supplier for credit or refund; OR

dispose of it with a loss write-off.

Adjustments must be made to Inventory, Sales Figures, perhaps to Sales Commissions, and other records within the company.

As you scroll through the screens, try to envision how each of these areas are impacted within the Company. Realize that the Order Manager, Work Effort Manager, Accounting Manager, and Facility Manager are primary players. The Marketing Manager and perhaps the Manufacturing Manager might be involved if some adjustments are needed.

Fortunately, the systems set up within Open For Business have automated much of this for you. However, by understanding the entire process, you can better stay alert for steps that might be needed as returns come back to your company.

7.7.2. Sales Return Diagrams
Create Sales Return

A customer requests for the return of the product. The reason for returning the merchandise can be defective goods, incorrect product specification, excess quantity shipped or wrong items shipped. The [CSR] accepts the return request and fills out the return details and creates a return with respect to the sales order.

Update Sales Return

A user can request the CSR to update the return. The reason can be to add/remove items in previously created sales return or editing the returnable quantity. A CSR opts to put notes on the return related to communication or conclusion drawn on that return.

Overview

Details

7.7.3. Sales Return management in UI
Quick Return

While viewing an existing order, you can create a return from that order by clicking on the [Create Return] button (actions section).That will take you to the quickreturn screen, from where you identify which item(s) the customers wants to return.

Be clear about the reason and the quantity to be returned. Also be sure that the Return Price does not exceed how much the customer actually paid for the item.
Return Type is important because it is always to your advantage to have the purchase price applied as a credit towards another purchase rather than having to take money out of your business to pay a refund.

When the information is correctly selected and entered, click the link[Return Selected Items] to create the Return.
Next screen show you Return Request creation successful, and you can directly [Accept Return]

That also takes you to the Returns tab, Return Items sub-tab, discussed further below.

Notice you can:

select All (check box)

choose Return Qty, just behind Order Qty
Be sure this does not exceed the Order Qty. If that attempt ismade, have them return any surplus against another order from where they probably obtained it.

Return Price, just behind Unit Price
The Price at which the customer will be credited. This is a mandatory field (*).
For example, if the customer received a promotional discount of 10% on a $100 item, you would not return $100 (the Unit Price) but only the discounted price of $90 which they originally paid for it.

Return Reason
Select the best-stated reason for the return. Remember that Returns need to be approved. Some items may be sold with a re-shelving fee, others may be close-outs with no returns authorized.
If reason you want is not listed, Additional reasons can be programmed into the system as their need develops (or just added by a administrator via webtools if it’s only for better information).
Why is a reason needed? This information is used when receiving the return to help decide whether to put the item back into inventory,throw it out, schedule it for repairs, etc.
Choices in the drop-down box might include:

Defective Item

Did Not Want Item

Miss-Shipped Item

Digital Fulfillment Failed

Return Type
This establishes how the financial aspects of the return will be handled. Choices in the drop-down box might include:

Store Credit

Refund

Replacement

Cross-Ship Replacement

Item Status
What is the current status of the Item?
The status could be one of the following:

---, the item status is unknown

On Order, the item was not yet shipped but is no longer wanted

Available, the item is in your facility

Promised, the item is committed to fulfilling another order

Delivered, the item is on its way to the Customer now wanting to return it

Being Transferred, the item is being moved from one location or section to another

Being Transferred (Promised), the item is being moved AND it has already been committed to fulfilling another order

Returned, the item has physically been sent back from the customer to your facilities

Defective, whatever the location or other status may be, the item itself is considered defective and should not be promised to fulfill another order.

Select a ship from address
Click on the radio button corresponding with the address from which the items will be returned. This will generally match the ship-to address for the original Sales Order.

Find Return

In the status field, You can select multiple values.

Create Return

If you are not starting from View Order Screen, you can initiate the creation of a new Return from dedicate screen.

First screen is for the header informations

The Return process involves a coordinated effort with Facilities, Accounting, and the Order managers. The tab [Receive Return] is not visible on this screen until the Return has been Accepted. That tab actually takes you into the Facilities Manager for further processing of the Return.

Return ID This is a number assigned by the system when the Return is first requested.

Field Needs Inventory Receive: or Auto-Receive means that the item is already here and that when the Return is Accepted, it will be processed as an Auto Receive rather than through the normal steps in the facility.

Second screen, tabs is for the return Items

It’s not possible to add manually items, you should choose in the drop box Order Id on bottom to load directly Items from an existing order.
After loading items from an order, select the one you want to add them to this return.

For more details on field, look at Quick Return.

After loading items, update Status to accepted under Return Header, you now have a new link button [Receive Return]. When you click on that, you are taken to the Facility Manager > Facilities tab > Receive Return sub-tab.

7.8. Requirements
7.9. Stats
Order Glossary
CSR

Customer Service Representative; A customer service representative (CSR) can place the order on behalf of a customer from the back end

8. Accounting

The OFBiz accounting system is a core application component and has most of the modern features you would expect in a general purpose double-entry accounting system. However, OFBiz goes beyond that by and seamlessly integrates with other OFBiz applications such as Inventory, Purchasing and Manufacturing to give your business a complete ERP solution. This makes the system as a whole robust and integrated to provide more value than a plain accounting system.

8.1. About Accounting

The Accounting system is organised according to generally accepted principles such as double-entry accounting, a General Ledger with hierarchical accounts, journals and posting of transactions and corresponding entries.

The structure is primary based on the OMG GL standard and the work that was done on an AR/AP extension of the OMG GL standard. This correlates well with other standards such as ebXML and OAGIS.

The Accounting entities are structured such that accounts for multiple organisations can be managed. The multiple organisations could be multiple companies, or departments or other organisations within a company. Each organisation can have various GL Accounts associated with it so that it can operate with its own subset of the Master Chart of Accounts.

Each organisation can also have its own set of Journals for flexibility, even though the use of Journals should be as minimal as possible in favour of allowing the system to automatically create and post transactions based on business events triggered by standard procedures and documents such as purchase and sales orders, invoices, inventory transfers, payments, receipts, and so on.

8.1.1. Accounting Features

General Ledger

Accounts Receivable

Accounts Payable

Agreements

Multi-currency Support

Billing Accounts

Fixed Asset Accounting

OFBiz accounting can be configured to handle multiple organisations including an unlimited number of companies, subsidiaries and departments.

Help for Accounting Main screen

This is the default tab for the Accounting Manager application. The screen currently shows links that will display more detailed screens related to Agreements, Billing Accounts, Invoices and Payments.

With accounting application mmenu, it’s possible to have a lot of more details

8.2. Invoices.

Sales invoices are generated when customers buy something from your business. You will need to provide a detailed list of the items bought and relevant taxes paid. They are often referred to a 'tax invoices' as they contain information relating to the amount of sales tax (eg VAT / GST) charged on the product or service.

Purchase invoices are generated by your suppliers when you order something from them.
You may send them an order in the form of a Purchase Order.
They will then send you the products and an invoice for payment.
This invoice is the Purchase Invoice and it will contain details of the items bought plus any taxes.


Both of these documents are used as proof to various tax authorities (eg Inland Revenue, Customs etc) that the required tax has been charged or collected.

	The following is an extract from Ian McNulty’s documentation work on accounting:

Invoices are created automatically by the system when certain criteria are met for each item on an order. The criteria will vary depending on the type of product associated with the order item, and the type of order (ie purchase/sales).

For Sales Orders that include digital goods, an invoice will be created when the order is placed, and that invoice will be for all digital goods in the order.
If there are non-digital or physical goods they will go in a separate invoice.

For Sales Orders that need physical fulfillment, an invoice will be created for all items in a shipment when the shipment goes into the 'Packed' status.

For Purchase Orders an invoice will be created from a shipment when the shipment goes into the Received status.

8.2.1. Invoices management in User Interface
Help for Find Invoices

The default screen is for the Invoices tab is 'Find Invoices'. It is used to locate existing invoices that have been created automatically by the system or manually by the user. It can also be used to create a new Sales or Purchase Invoice.

How do I view all invoices?

Press the 'Search' button to view all invoices

How do I locate an existing invoice?

Enter the 'Invoice ID' if known

Enter a word from the invoice description in the 'Description' field if known

Enter the 'Invoice Type' if known

Enter the 'From Party Id' if known
(NOTE: In most cases for a Sales Invoices this will be Company. For Purchase Invoice it will be the supplier party id)

Enter the 'Billing Account Id' if known

Enter the invoice status in the 'Status Id' field if known

Enter the 'To Party Id' if known
(NOTE: In most cases for a Purchase Invoice this will be company. For Sales Invoices it will be the customer party id)

Press the 'Search' button to view all invoices

All invoices that meet the search criteria will be displayed.

How do I update an invoice?

Locate the invoice using the 'Find Invoices' screen

Using the relevant sub menu make the required changes.

How do I delete an invoice?

Invoices cannot be deleted through the user interface. They can only be cancelled (eg if they have been entered or created by mistake).

	They can probably be deleted using Entity Data Maintenance in the Webtools menu but this is not recommended for 2 reasons:
1) It may cause data integrity problems.
2) In case of audit it would be a problem.
Help for Invoice Overview

The Invoice Overview screen is used to display the summary of an invoice in a single view. The screen is divided into sections that show various information related to the invoice (eg Roles, Status, Terms, Items, Payments Applied, etc).

The following options are currently available from this screen:

Create New (Create a new invoice)

Copy (Create a copy of the current invoice)

PDF (View a PDF of the current invoice)

PDF default currency
(NOTE TO CHECK: Need to see how this is different from just the PDF view…​…​)

Status to 'Approved' (Change the status of the current invoice to 'Approved)

Status to 'Sent' (Change the status of the current invoice to 'Sent')

Status to 'Ready' (Change the status of the current invoice to 'Ready'.
NOTE: This will create the relevant accounting transactions and post them to the general ledger)

Status to 'Cancelled' (Change the status of the current invoice to 'Cancelled')

Save as Template
(NOTE TO CHECK: Save the current invoice format as a template)

Help for Edit Invoice Header

The Invoice Header screen is used to view or update details from the invoice header.

Examples of the type of information that can be changed are Due Date, Description, Currency.

How do I update the header details for an Invoice?

Select the 'Header' sub menu and the header details of the invoice will be displayed

Update the fields required

Press the 'Update' button

Help for New Invoice

This screen allows the user to create a new Sales or Purchase Invoice.
Sales Invoices are created when a customer buys something from you.
Purchase Invoices are created when you buy something from a supplier.

How do I create a new Sales invoice?

Press the 'Create New' button

The New Sales Invoice / New Purchase Invoice screen is displayed>

Using the top part of the screen, leave Invoice type with its default of 'Sales Invoice'

Leave 'Organization Party Id' with its default of 'Company'

Enter or use the lookup to find the 'To Party Id' (eg DemoCustomer)

Press the 'Create' button in the top part of the screen

The invoice header has been created and the default header screen will be displayed

Details on the invoice will need to be entered via the other sub menus (eg Items, Time Entries etc)

How do I create a new Purchase invoice?

Press the 'Create New' button

The New Sales Invoice / New Purchase Invoice screen is displayed>

Using the bottom part of the screen, leave Invoice type with its default of 'Purchase Invoice'

Leave 'Organization Party Id' with its default of 'Company'

Enter or use the lookup to find the 'From Party Id' (eg DemoSupplier)

Press the 'Create' button in the bottom part of the screen

The invoice header has been created and the default header screen will be displayed

Details on the invoice will need to be entered via the other sub menus (eg Items, Time Entries etc)

Help for Edit Invoice Applications

The Invoice Applications sub menu is where payments that have been made (or received) can be linked or allocated to an invoice.
The phrase 'applying' an amount to an invoice is often used to describe this.

The screen is divided into 3 main areas as follows.

Payments Applied (which shows details of the total amount 'Applied' and the total amount 'Open'.
Note that 'Open' here means outstanding)

Possible Payments to Apply (which shows all the payments that have been sent from the same party id as the invoice, for a sales invoice this would be the customer party id)

Assign Payment to Invoice (which allows you to manually assign a specific payment id to this invoice)

	General Ledger accounting transactions are generated during the payment application process but unless your GL is setup with Unapplied Cash and Applied Cash accounts
- I’m not sure that there will be any true accounting impact.
In the Sales Order process the accounting transaction generated the following GL Accounting transaction is generated for 'Payment Applied' o add some text here.

DR 120000 Accounts Receivable / CR 120000 Accounts Receivable - This transaction doesnt really do anything!

It is used to link payments to invoices. It is also used to allocate which part of a payment is allocated or applied to a specific invoice. This is extremely useful if your customers pay multiple invoices with a single payment.

Example:

A customer could send a single payment of $1000 that can be used to pay for two invoices (eg $400 and $600)

Using this applications sub menu allows you to allocate part of the $400 to one invoice and the balance ($600) to the other invoice

By default all 'unapplied' payments that have been entered into OFBiz from the customer will be available for selection even if they have not yet been flagged as formally 'Received'. This means that these are payments that have not already been linked to another invoice.

If only part of a payment amount has been linked to an invoice then the remaining amount is left available to be allocated to another invoice.
Also note that a single invoice could be paid by multiple payments being applied to it.

How do I apply a payment (or payments) to an invoice?

Select the 'Applications' sub menu for the invoice

A list of unapplied payments for the party id will be displayed

Press the 'Apply' button next to the entry that needs to be applied to the invoice
(NOTE: More than one entry may be used. Also only part of a larger amount may be used)
The Payments Applied total at the top of the screen will be updated with the amount selected. Also the Amount Open will be reduced by the amount selected.

Once the total invoice amount has been selected a message will be displayed and only the first part of the screen will be displayed

The top part of the screen will now be updated to show the 'Payments Applied' total is equal to the invoice total and the 'Amount Open' is zero.

How do I update an applied payment for an invoice?

Payments that have been applied to an invoice can be updated. This means that you can change the details of the payment transaction or adjust the amount that was applied to the invoice.

Select the 'Applications' sub menu for the invoice

A list of payments already applied to the invoice will be displayed in the top part of the screen

Enter or use the lookup to change the 'Payment Id' if required

Enter the updated amount in the 'Amount to Apply' field if required

Press the 'Update' button

How do I remove an applied payment (or payments) from an invoice?
	TO CHECK: It can be done before transaction has been posted to GL but also need to check if its can be done if the transaction has been posted.

Select the 'Applications' sub menu for the invoice

A list of payments already applied to the invoice will be displayed in the top part of the screen

Press the 'Remove' button next to the payment entry that needs to be removed

The entry will be removed and the top part of the screen will be update the 'Payments Applied' total and 'Amount Open'

Help for Edit Invoice Items

The Invoice Items screen displays the individual invoice line details and allows the user to update or remove an entry. As each invoice line is created it is allocated a specific sequence (or Item Number) which acts as a unique identifier.

How do I create a new invoice line item?

Note that only invoices that have specific statuses can have new line items created. This means that if an invoice has already been paid and processed OFBiz will not allow any amendments to it.

Select the 'Items' sub menu for the invoice

The 'Add a new invoice item' screen will be displayed

Leave the 'Item No' field blank (as it will be automatically generated)

Select the 'Invoice Item Type' from the drop down box
(NOTE: A typical line using the demo could be 'Invoice Finished Good Item' but ensure that it corresponds with the type of products setup in your catalog)

Enter a description describing what the line item is
(NOTE: If you are going to enter a product in the Product Id field from the catalog then leave the 'Description' field blank as it will be used to show the product description)

Leave the 'Override GL Account Id' field blank as it will use the default account based on the Chart of Accounts setup

Use the lookup or enter a product code in the 'Product Id' field
(NOTE: This can be left blank if your invoice line is not related to a product in the catalog)

Enter a number in the 'Quantity' field

Enter a 'Unit Price' only if the Product Id field is blank
(NOTE: If a Product Id has been entered then leave the 'Unit Price' field blank as it will pick up the product price from the catalog)

Leave the 'Inventory Item' field blank

Leave the 'Product Feature Id' field blank

Leave the 'UOM' field blank

Select 'Yes' for the 'Taxable Flag' field

	TO CHECK: Need to do some tests to see what line item type needs to be used for 'Sales Tax'.
I think that it could be 'Invoice Item Sales Tax' since tax is currently calculated at invoice item line level.
Also the automatically generated invoices from Order Entry and E-Commerce show taxes at the invoice item line level (think there may be some work going on - see JIRA on to consolidate entries).
Need to do some tests using 'Invoice Sales Tax' to see how it works…​…​…​
How do I update an invoice line item?

Not all the fields on the invoice item line can be updated. For example Taxable Flag and Inventory Item cannot be updated.

If these fields need to be amended then the invoice item will need to be removed and then re-created.

Select the 'Items' sub menu for the invoice

Any existing line items will be displayed in the 'Items' box

Amend the details in the line item that needs to be updated (eg Quantity, Invoice Item Type, Product Id, Description, Override GL Account, Unit Price)

Press the 'Update' button displayed at the end of the line item that has been updated

How do I delete an invoice item?

Select the 'Items' sub menu for the invoice

Any existing line items will be displayed in the 'Items' box

Press the 'Remove' button displayed at the end of the line item that needs to be deleted

Help for Edit Invoice Time Entries

he Time Entries screen displays any time logged against the invoice. For example these time entries can be from employee or external supplier timesheets that are tracked within OFBiz. It is used to track any individual work or billable hours against an invoice.

How do I add a new time entry for an invoice?

Threre are two options

Add time entry to a new invoice and add time entry to an existing invoice.

Timesheet entries can be added to an existing invoice from Workeffort Manager.

How do I update a time entry for an invoice?
	To CHECK if this can only be done via timesheets.
How do I remove a time entry from an invoice?
	TO CHECK if this is done via timesheets
Help for Send Per Email

This is used to send a copy of the invoice details to one or more email addresses. The invoice is included as an attachment and the user can add a simple accompanying email message.

How do I send a copy of an invoice via email?

Select the 'Send per Email' sub menu

The 'Send per Email' default screen will be displayed

Enter the 'From Email Address'
(NOTE TO CHECK: Shouldnt this be defaulted from the user login…​..????)

Leave the 'To Email Address' as it is as this will be defaulted using the customer details from the invoice

If required enter the 'Copy Email address' for anyone that needs to be copied on the email

Leave the 'Subject' as the default of 'Please find attached invoice'

Leave the 'Other Currency' box blank
(NOTE TO CHECK: Investigate what effect this has on the email…​..)

Enter a short email message in the 'Email Body'

Press the 'Submit' button

Help for Invoice Roles

The Invoice Roles screen allows parties with specific roles to be associated with and invoice. If the e-commerce or Sales Order entry route has already been used then the invoice generated will already contain the relevant roles from the various parties.

For a Sales Order examples of roles will include Bill From Customer, Bill To Customer, End User Customer,Ship To Customer etc.

How do I add a party role to an invoice?

Party roles will automatically be added to an invoices that have been generated as a result of E-Commerce order entry or Sales Order entry.
They can also be added be added manually.

Select the 'Roles' sub menu

Enter or use the lookup to enter the party to be added to the invoice in the 'Party Id' field

Use the drop down box to select the 'Role Type Id'

Leave the 'Date Time Performed' field blank
(NOTE: This field is optional and can be entered if required. This field can be used to indicate the date and time this role was performed by the party for this invoice)

Leave the 'Percentage' field blank
(NOTE: This field is optional and can be entered if required. If roles are shared then this field can be used to indicate the assigned percentage for this role)

Press the 'Submit' button

The new role entry will be displayed on the bottom part of the screen

	If you select a role that is not associated with the party that has been entered an error message will be displayed. To fix it you will need to add the role to the party or choose another party that already has that role associated with it.
How do I update a party role on an invoice?

A party role cannot be updated via the current user interface. It can only be removed. If a party role needs to be updated then the entry must be deleted and then re-created.

How do I remove a party role from an invoice?

Locate the entry that needs to be removed

Press the 'Remove' button next to the entry that needs to be deleted

The entry is now removed from the list of invoice roles

8.3. Payments.

Payments are transactions that received by or generated by a business.

They can be incoming or outgoing.

Incoming payments are normally from customers and outgoing ones to suppliers.

the Payment screen contains a lot of information not normally at your fingertips. The screen for creating a Payment looks very similar to the View Payment screen: you have drop-down boxes for Payment Type, Payment Method Type, and Status. The other fields are asking for ID numbers which may be more difficult to obtain.

For the above reasons, it is probably quicker and easier to click on the [Receive Payment] link from the View Order screen than to try to create a Payment from the Accounting Manager.

8.3.1. Payments management in User Interface
Help for Find Payments

The default screen is 'Find Payment' which allows the user to search for and view the details related to a payment transaction. Specific search criteria can be entered as a filter to locate the payment quickly.

Payments can be incoming or outgoing and the demo data contains a list of payment type descriptions that describe the reason for the payment in more detail (eg Customer Deposit, Tax Payment, Commission Payment etc).

This screen is used to locate existing payments that have been created automatically by the system or manually by the user. There are links from this page that can be used to do the following:

Create a new incoming or outgoing payment

Find Sales Invoices by due date

Find Purchase Invoices by due date

How do I view all payments?

Press the 'Search' button to view all payments

How do I locate an existing payment?

Enter the 'Payment ID' if known

Enter a word from the payments 'Comment’field if known

Enter the 'Payment Type Id' if known

Enter the 'From Party Id' if known
(NOTE: In most cases for an incoming payment this will be the customer party id)

Enter the payment amount in the 'Amount' field if known

Enter some details from the payment reference number in the 'Reference No' field if known

Enter the status of the payment in the 'Status Id' field if known

Enter the 'To Party Id' if known
(NOTE: In most cases for an incoming payment this will the the customer party id. For outgoing payments this will be the supplier id, or customer id for a refund)

Press the 'Search' button to view all payments

All payments that meet the search criteria will be displayed.

Help for New Payment

This screen is used to create a new payment. Payments can be incoming (eg from a customer) or outgoing (eg to a supplier). Payment types are used to describe what the payments are used for in the system.

Examples of incoming payment types are as follows:

Customer Deposit

Customer Payment

Interest In

Examples of outgoing payment types are as follows:

Commission Payment

Pay Check

Income Tax Payment

Vendor Payment

How do I create a new incoming payment?

Press the 'Create New Payment' button

The New Incoming Payment / New Outgoing Payment screen is displayed

Leave 'Organization Party Id' with its default of 'Company'

Select the 'Payment Type Id' from the drop down box
(NOTE: This is currently limited to the following: Customer Deposit, Customer Payment, Interest In and Gift Certificate Deposit)

Enter the payment amount in the 'Amount' field

Enter or use the lookup to find the 'From Party Id'

Select the 'Payment Method Type' from the drop down box (eg how the payment was paid - cash, cheque, money order etc)

Leave the 'Currency' field with its default of 'USD'
(NOTE: This default comes from Company)

Press the 'Create' button

The payment header is created and the default header screen will be displayed subsection content

	TO CHECK Need to understand what happens if customer pays in a currency that is not the company default…​.
if the exchange rate is specified then I think it should convert the currency to the default currency for accounting purposes…​.
need to investigate and test.
How do I create a new outgoing payment?

Press the 'Create New Payment' button

The New Incoming Payment / New Outgoing Payment screen is displayed

Leave 'Organization Party Id' with its default of 'Company'

Select the 'Payment Type Id' from the drop down box
(NOTE: This is currently limited to 11 entries including Commission Payment, Customer Refund, Vendor Payment, Income Tax Payment)

Enter the payment amount in the 'Amount' field

Enter or use the lookup to find the 'To Party Id'

Select the 'Payment Method Type' from the drop down box
(eg how the payment is to be paid - cash, cheque, money order etc)

Leave the 'Currency' field with its default of 'USD'
(NOTE: This default comes from Company)

Press the 'Create' button

The payment header is created and the default header screen will be displayed subsection content

Help for Payment Overview

The Payments Overview screen displays the summary details of the payment.

On one side it shows information related to the payment transaction header (eg Payment Type, Status, Amount, Effective Date etc) and the other it shows if the payment has been applied (or matched) to an invoice or billing account etc.

The following options are currently available from this screen:

Create New (Create a new payment)

Status to 'Received' (Change the status of the current payment to 'Received.
NOTE: This will create the relevant accounting transactions and post them to the general ledger)

Status to 'Cancelled' (Change the status of the current payment to 'Cancelled')

Status to 'Confirmed' (Change the status of the current invoice to 'Confirmed'.
NOTE: This status option will not appear until the status has been changed to 'Received')

	The general ledger transactions generated as a result of the payment are based on the GL Account Type defaults for Company as follows:
1) Debit Entry (GL Account Type defaults)
2) Credit Entry (Payment Method Id / GL Account Id)
Help for Payment Applications

The Payments Applications sub menu is where payments that have been made (or received) can be linked or allocated to an invoice, another payment, a billing account or a tax authority.

	General Ledger accounting transactions are generated during the payment application process but unless your GL is setup with Unapplied Cash and Applied Cash accounts
TO CHECK I’m not sure that there will be any true accounting impact.

In the Sales Order process the accounting transaction generated the following GL Accounting transaction is generated for 'Payment Applied'

The following options are currently available from this screen:

Create New (Create a new payment)

Status to 'Received' (Change the status of the current payment to 'Received.
NOTE: This will create the relevant accounting transactions and post them to the general ledger)

Status to 'Cancelled' (Change the status of the current payment to 'Cancelled')

Status to 'Confirmed' (Change the status of the current invoice to 'Confirmed'.
NOTE: This status option will not appear until the status has been changed to 'Received')

How do I apply a payment to an invoice?

Select the 'Applications' sub menu for the payment

A list of invoices will be displayed in the 'Possible Invoices to Apply' box
(NOTE: If no open invoices exist for the party that is sending the payment then this may not list any invoices)

Press the 'Apply' button next to the invoice (or invoices) that this payment is for

	Although it can be overriden the 'Amount to Apply' field will default to the lesser of the invoice total or the payment amount.

This can be shown by examples as follows:

If a payment of $150 is received but the invoice total is $120 then the 'Amount to Apply' will default to $120

If a payment of $150 is received but the invoice total is $170 then the 'Amount to Apply' will default to $150

How do I apply a payment to an invoice, tax authority, billingaccount or another payment?

Select the 'Applications' sub menu for the payment

Using the 'Apply this payment to' box at the bottom of the screen

Enter or use the lookup to enter the 'Invoice Id' to apply the payment to
(NOTE: This can be used if the invoice is to another party eg ordered by a subsidiary but paid for by another company of the same group)

Enter or use the lookup to enter the 'To Payment Id' to apply the payment to if required
(NOTE TO CHECK: How does this work…​.?)

Enter or use the lookup to enter the 'Billing Account Id' to apply the payment to if required

Enter or use the drop down box to select the 'Tax Auth Geo Id' to apply the payment to if required
(NOTE TO CHECK: This is a country so need to test how this actually works…​…​)

Enter an amount in the 'Amount to Apply'
(NOTE: This must be less than or equal to the payment amount)

Press the 'Apply' button

Help for Payment Header

The Header screen displays the header details for the payment transaction and allows all fields to be updated if required.

The following options are currently available from this screen:

Create New (Create a new payment)

Status to 'Received' (Change the status of the current payment to 'Received.
NOTE: This will create the relevant accounting transactions and post them to the general ledger)

Status to 'Cancelled' (Change the status of the current payment to 'Cancelled')

Status to 'Confirmed' (Change the status of the current invoice to 'Confirmed'.
NOTE: This status option will not appear until the status has been changed to 'Received')

How do I update the header details for a Payment?

Select the 'Header' sub menu and the header details of the payment will be displayed

Update the fields required

Press the 'Update' button

Help for Find Sales Invoices By Due Date

This screen allows the user to search for and locate Sales Invoices based on their due date.

The 'Due Date' can be defined as the last possible date that payments can be received for the invoice without triggering late payment penalties.

The 'Invoice Date' can be defined as the date that the invoice was created and this is normally based on when products were shipped or services were provided.

	TO CHECK: There appears to be a minor bug here as if the Invoice 'Due Date' is different to the Invoice Date (eg. Invoice Creation Date) then the Invoice Date is used as the Due Date in this screen which I dont think is correct…​…​

A Sales Invoice may be due to be paid immediately or as in some cases the customer is given a 'grace period' after which the invoice is generated and becomes due.

Examples of this include only generating a customer invoice after a certain amount of time after the dispatch of their order.
(NOTE: There are several ways this can be achieved in OFBiz including the use of agreements and billing accounts).

This screen can be used to locate Sales Invoices as follows:

That will become due within a fixed timeframe (eg the next 5 days)

That may already be overdue

That have been automatically generated by the system
(eg as a result of Agreements based on payment in 30 days etc…​.TO CHECK)

	TO CHECK See details from Jacopo below regarding future work regarding Find Sales Invoice by Due Date and Find Purchase Invoice by Due Date functionality:
- The two links are used to search invoices' due dates for payments - there are plans to add links to quickly create payments for them etc.
- So they are somewhat in the middle between an invoice thing and a payment thing.
- By the way, for now I will close this issue because the best spot to place them is in the AR and AP applications, but there is still a lot of work to do to make them usable.
How do I find a Sales Invoice by Due Date?

Press the 'Find Sales Invoices by Due Date' button

The Find Sales Invoices by Due Date screen is displayed

Enter the 'Organization Party Id' (eg. Normally this will be Company)

Enter the 'Party Id' that the Sales Invoice (eg. Normally this will be the Customer Party Id)

Enter a number in the 'Days Offset' field that represents the number of in which the invoice will become due
(eg If an invoice is due to be paid in 5 days then enter 5 or greater)

Press the 'Select' button

Help for Find Purchase Invoices By Due Date

This screen allows the user to search for and locate Purchase Invoices based on their due date.

The 'Due Date' can be defined as the last possible date that payments can be received for the invoice without triggering any late payment penalties.

The 'Invoice Date' can be defined as the date that the invoice was created and this is normally based on when products were received or services were provided.

	TO CHECK: See if the same bug that exists with Sales Invoices is here too.

A Purchase Invoice may be due to be paid immediately or you may be given a 'grace period' after which the invoice is due.

How do I find Purchase Invoices by Due Date?

Press the 'Find Purchase Invoices by Due Date' button

The Find Purchase Invoices by Due Date screen is displayed

Enter the 'Organization Party Id' (eg. Normally this will be Company)

Enter the 'Party Id' that the Purchase Invoice (eg. Normally this will be the Supplier Party Id)

Enter a number in the 'Days Offset' field that represents the number of in which the invoice will become due
(eg If an invoice is due to be paid in 5 days then enter 5 or greater)

Press the 'Select' button

8.4. Payment Gateway

The Payment Gateway is made up of a configurable interface that processes payments.

Before using using them, it’s needed to config them.
Payment Gateway Configuration is used to setup the parameters required for the system to accept payments via different or external applications

Examples of these include:

Paypal

PayFlow

Authorise.net

Clear Commerce

When config is done, Payment transactions can be authorised, captured and processed or refunded via the selected mechanism, (eg Paypal, Authorise.net, etc) more details are explained in Payment Transaction management in User Interface

8.4.1. Payment Gateway Config management in User Interface
Help for Edit Payment Gateway Config

This screen allows the user to update the payment gateway configuration.

A range of parameters need to be set before the payment gateway will work This includes details of the username and password required for the validation of the external account that will be using the gateway.

How do I update a Payment Gateway Configuration?

Select the gateway Find Payment Gateway Config screen

Enter the details required for the configuration type selected
(NOTE: This will be different for each individual configuration selected)

Press the 'Update' button

Help for Find Payment Gateway Config Types

This screen lists some of the most common payment gateway configuration types that have been created as part of the seed or demo data.

Press the 'Lookup' button to see a list of existing payment gateway configuration types.

Help for Edit Payment Gateway Config Type

This screen allows the update of an existing payment gateway configuration type.

	New Payment Gateway Configuration Types cannot be created via this screen.
8.4.2. Payment Transaction management in User Interface
Help for Find Gateway Responses

This is the default screen for the 'Transactions' sub menu.
Press the 'Lookup' button to display details of all transactions that have been authorised, captured or manually entered.

How do I view all Gateway response transactions?

Press the 'Lookup' button

A list of all transactions that have been authorised, captured or manually entered will be displayed.

Transaction results (external link)

http://www.authorize.net/support/merchant/Transaction_Response/Transaction_Response.htm
can give the List of all the transaction results

Help for The Authorize Transaction

An authorization is a temporary transaction that shows a commitment to take money from an account.

The 'Authorize' process is the first step in allowing a sales transaction payment to be accepted.
In OFBiz a service would be defined to carry out the authorisation process each time for example, a credit card is used. It will perform specific validation tests before the payment can be classes as 'authorised'.

When a payment is authorised it means that it has been validated and that the credit card or bank account has been checked to ensure that it has sufficient funds available to cover the proposed transaction.
A number or code may be issued as evidence of the authorisation.

	In the 'Payment' settings for a store as part of the Product Payment setup the user can specify various services that will process a payment transactions through to completion.

This includes the following:

Payment Authorisation

Payment Capture

Payment Credit

Payment Authentication Verification

Payment Re-Authorisation

Payment Refund

Payment Release Authorisation

This is used to provide verification and approval for the first step of the sales transaction payment process.

An 'Authorize' button is also displayed on Sales Order detail screen if a Credit Card payment was specified for a sales order. This is probably a more natural place for a payment transaction to be authorised.

	Using OFBiz demo data if DemoCustomer uses their credit card for payment then an transaction is created that is automatically authorised and can be viewed using the Gateway Responses.
How do I create and authorise a transaction?

Enter the 'Order Id' of the sales order for which payment is being made

Enter the 'Order Payment Preference Id'
(NOTE: This is automatically generated at sales order creation and may be difficult to find out…​
I found it by initially doing an order and then paying by DemoCustomer’s credit card and checking Gateway Responses for what was displayed in that field for the order)

Select the 'Payment Method Type'
(NOTE TO CHECK: What happens if you use other selections not just credit card?)

Enter the 'Amount'

Press the 'Authorize' button

A new transaction should be displayed with the status of authorised

	The demo data payment settings for the Payment authorisation Service is set to always approve so no transactions will display here because of this.
TO CHECK: Need to test and maybe try removing the 'always approve' to see if the transaction will be created as 'unauthorised'
Help for Capture Transaction

This screen is used to input or 'capture' a payment against a Sales Order.

Unlike the authorise, this function will actually deduct the amount from eg a credit card and apply the payment to a specific order.

It is likely that the before the payment is 'captured' in this screen, it would have been through an authorisation first.

	TO CHECK: Investigate how this links in with the Payment Gateway Configurations screens
How do I capture a transaction?

Enter the Order Id for the payment (eg Sales Order Id)

Enter Order Payment Preference Id
(TO CHECK Unsure of what this is…​a type of unique identifier perhaps?)

Select the 'Payment Method Type'

Select the 'Payment Type'

Enter the 'Amount'

Press the 'Capture' button

A transaction will be created and can be viewed via the 'Gateway Responses' screen.

Help for View Gateway Response

This screen shows details of an individual gateway transaction.

It displays specific information regarding the order and the payment.

The lower part of the screen shows the gateway response details indicating the time and codes used to process the transaction through the gateway.

Help for Manual Transaction

The Manual Electronic Transaction screen allows the user to manually input and process payment related transactions.

Options available include the following:

Authorising payment transactions

Refunding payments

Payment Re-Authorisation

Payment Capture

How do I create a manual electronic transaction?

Select the 'Payment Method Type' (eg Credit Card)

Select the 'Product Store'

Select the 'Transaction Type'
(NOTE: This is the type of transaction that needs to be created, eg authorisation, capture,refund etc)
Additional fields will be displayed

Enter the required details (eg name, credit card, billing address, amount etc)

Press the 'Submit' button

A transsaction will be created that can be viewed via the Gateway Transactions screen

	TO CHECK: Possible bug as could not get this to work using 'Payment Authorisation Service' and error message appeared regarding a missing parameter missing for Order Preference Id but the Order Preference Id was not displayed on the screen
8.5. Billing Accounts.

A billing account is a way of allowing customers to consolidate several invoices into an account that is paid off at a later date. Customers can be allocated a credit limit and orders can be taken up to the value of the credit limit without any payment being made. Statements to the customer can then be generated (eg monthly) and payment is made based on the outstanding amount.

	A billing account does not change the flow of the normal Invoice and Payment processes. It simply allows for a more structured organisation of Invoices and Payments..

Billing Accounts can be used for the following:

Setting credit limits for customers

Keeping track of credit available to customer for purchase on account

Keeping track of payments made in advance
(NOTE TO CHECK: Could also use Financial Account for advance payments but need to understand the differences in functionality and process)

Keeping track of a subset of payments and invoices for a specific client, i.e. allowing them to have multiple billing accounts
(NOTE TO CHECK: This is from David - does this mean having multiple accounts for one customer or does it mean one billing account can track a hierarchy of invoices and payments…​..)

Allow multiple authorised parties to bill against the same account which one party is responsible for paying
(e.g. different offices of the same organisation may have one single account with a supplier to make use of order volume discounts)

Managing and generating customer statements ??

Customer specific order tracking

Accounts Receivable / Debt Management

Analysis and monitoring customer spending (creditworthiness / discounts / product popularity ???)

	A payment that is applied (or matched) to a Billing Account it should still be applied to an invoice. In the case where the payment arrives before the invoice has been generated then once the invoice is generated it should be applied to the payment or payments.
8.5.1. Billing Account management in User Interface
Help for Find Billing Account

The default screen is for the Billing Account tab is 'Find Billing Account'. It is used to locate existing billing accounts that have been created.

The user has the option to select an existing billing account or create a new one by clicking on the 'New' button.

Help for Edit Billing Account

The 'Account' sub menu is used to enter the basic details required for setting up a new billing account or editing an existing one.

It can be used to create or update the following details for a Billing Account:

Billing Account Identification

Party to be Billed

Billing Account Limit
(NOTE: This is how much credit the customer will be given eg $5000)

Currency to be used for Billing Account

Start and End Dates

	There are currently two ways to add a party to a billing account.

Enter a party id in the 'Party Billed To' field

Use the 'Roles' sub menu to add a party id with the role of 'Bill To Customer'

If using the first method then when you press the update button this removes the party id from this field and automatically creates the party under the Roles sub menu with the role of 'Bill To Customer'

How do I create a new Billing Account?
	TO CHECK: If the party doesnt have the role 'Bill To Customer' is it automatically added when the billing account is created or will the creation fail?..

Example: To create a new Billing Account

Press the 'New' button and the 'Edit Billing Account' screen is displayed

Enter a code or number for the 'Billing Account Id'
(NOTE: If this is left blank a number will be automatically generated)

Enter a number for the 'Billing Account Limit' (eg 5000)

Leave the 'Account Currency UOM Id' as it is
(NOTE: This should be the default currency for Company…​)

Enter a description that can be used to identify the Billing Account (eg Joe Bloggs Builders Billing Account)

Leave the 'Contact Mech' field as it is
(NOTE: This field cannot be filled in until either the 'Party Billed To' has been filled in or a party with the role of 'Bill To Customer' has been added under the 'Roles' sub menu)

Enter the Billing Account start date in the 'From Date' field.
(NOTE: If left blank then this will default to the current date and time.
TO CHECK: Can this date be in the future…​..?)

Leave the 'Thru date' field blank

Enter or use the lookup to select the 'Party Billed To'

Press the 'Update' button

After the 'Update' button has been pressed then the 'Contact Mech Id' field will either be automatically filled in or will allow you to select a contact mech from a drop down list

How do I update an existing Billing Account?

Billing Account details can be updated.
A key field that may need to be updated is the actual Billing Account Limit if a customer reduces or improves their credit rating

Example: To Update a Billing Account

Click on the 'Billing Account Id' of the Billing Account to updated

The 'Edit Billing Account' screen is displayed

Enter the changes required

Press the 'Update' button

How do I delete a Billing Account?

Billing Accounts cannot be deleted.
They can only be expired.
This means that they will no longer be able to be used to associate invoices or payments against.

Example: To Expire a Billing Account

Click on the 'Billing Account Id' of the Billing Account to be expired

The 'Edit Billing Account' screen is displayed

Enter the current date in the 'Thru date' field

Press the 'Update' button

Help for Billing Account Roles

This sub menu allows parties with specific roles to be associated with to a Billing Account.


It is used to specify which party should be billed for the billing account.

It can be used as follows:

Simple billing account for a single party

More complex billing account where multiple parties (eg company subsidiaries) charge invoices to the billing account but a different party (eg head office) will pay the account

How do I add a party role to a billing account?

Select the 'Roles' sub menu

Enter or use the lookup to select the 'Party Id'

Select the 'Role Type Id' from the drop down box (eg Bill To Customer)

Leave the 'From Date' blank
(NOTE: If left blank it will default to the current date and time)

Leave the 'Thru Date' blank

Press the 'Add' button

The new party role is displayed at the bottom of the screen

How do I update a party role for a billing account?

The only field that can be updated for a party role is the 'Thru Date'. If any other details need to be amended then the entry will need to be deleted and then recreated.

Select the 'Roles' sub menu

Locate the entry that needs to be amended

Enter or use the lookup to enter the 'Thru Date'

Press the 'Update' button for the entry

How do I delete a party role from a billing account?

Locate the entry that needs to be deleted

Press the 'Delete' button next to the entry

The entry will be removed from the bottom of the screen

Help for Billing Account Terms

This sub menu allows terms to be associated with a billing account.

Currently these can be the following:

payment terms (discounted if paid within specified days)

payment terms (due on a specified day per month)

payment terms (net days)

penalty terms (late fee)

penalty terms (collection agency fee)

miscellaneous (non returnable sales item)

	TO CHECK: There is an overlap here with the terms that can be specified in an agreement. Would a billing account party also have an agreement for payment terms…​? .
How do I add terms to a billing account?

Select the 'Terms' sub menu

Select a 'Term Type' from the drop down box (eg. Payment net days)

Leave the 'UOM' field blank

Enter a number in the 'Term Value' field
(eg. 30 which would mean '30 days' when related to 'Payment net days')

Press the 'Save' button

The term is displayed in the top part of the screen

How do I update terms for a billing account?

Select the 'Terms' sub menu

Press the 'Edit' button next to the entry that needs to be amended

The details are displayed in the 'Edit Billing Account Terms' box

Update the 'Term Type', 'UOM' or 'Term Value' as required

Press the 'Save' button

The updated term is displayed in the top part of the screen

How do I remove terms from a billing account?

Select the 'Terms' sub menu

Press the 'Delete' button next to the entry that needs to be removed

Help for Billing Account Invoices

The Billing Account Find Invoices screen displays by default a list of invoices that have been charged to the billing account.

Any invoice displayed here means that its invoice amount has been deducted from the billing account credit limit. For example: If the Billing Account Credit Limit is $100 and the there are 2 invoices displayed with amounts $10 and $25 then the available credit for the billing account will be $75.

The invoice can be at various statues and there is an option to locate an invoice by status.

It is also used to apply any payments that have been made into the Billing Account to an invoice. A 'Capture' button is displayed next to each invoice displayed that has an amount outstanding.

Example:

Two invoices are charged to a Billing Account (Invoice A $10 and Invoice B $25)

A payment of $17 has been paid into the Billing Account

If the Capture button is pressed for the invoice A then $10 of the $17 payment will be applied to this invoice and a new payment transaction of $7 will be created and available to apply to a different invoice

How do I locate an invoice by status?

Select the 'Invoices' sub menu

Use the drop down box to select the 'Status Id' for the invoice required

Press the 'Submit' button

A list of invoices with the required status will be displayed

How do I capture a payment for an invoice?
	In order for this to work a payment needs to have been made to the billing account that has not been completely applied to any other invoices.

Payments to a billing account can be done via the 'Payments' sub menu for the billing account or by using Accounting / Payments menu.

Select the 'Invoices' sub menu

Locate the invoice required
(NOTE: The 'Amount to Apply' is the same as the 'Total' column)

Press the 'Capture' button
(NOTE: The 'Amount to Apply' is different to the 'Total' column)

The 'Capture' button is no longer displayed next to the invoice and an additional payments transaction will be created for any difference between the invoice total and the amount paid (Eg Invoice Total $100, Payment Amount $125, the new payment transaction amount will be $25)

	The above example assumes that the payment available will cover the total amount outstanding for the invoice
Help for Billing Account Payments

This sub menu allows the creation of a payment that is automatically applied to the billing account.

It is used when a payment has been received from a customer that is used to pay off the balance (or part balance) of a billing account.

An example of how this works is similar to a credit card statement where a list of transactions have been incurred over the previous month and one payment is used to settle the outstanding balance.

How do I add a payment to a billing account?

Select the 'Payments' sub menu

The 'Create Payment' screen is displayed

Enter or use the lookup to enter the 'From Party Id'
(NOTE: By default this will be the Bill To Party of the Billing Account)

Select the 'Organisation Party Id' from the drop down box

Select the 'Payment Type Id' from the drop down box
(NOTE: By default this will be set to 'Customer Deposit')

Leave the 'Payment Method Type' as 'Billing Account'
(NOTE TO CHECK: What happens if you do change this…​.)

Enter the 'Amount' of the payment

Press the 'Create' button

The new entry is displayed at the bottom of the screen.

	The total amount of the payment will be applied to the Billing Account.
This can be verified by going to Accounting / Payments menu and locating the newly created payment.
The 'Amount to Apply' column will be zero.
How do I update a payment for a billing account?

A payment can be updated for a billing account by amending the amount of the payment that has been applied to the billing account.

For example if a payment of $100 has been applied to a billing account it can be amended so that only $75 will be applied and $25 will be available to be applied elsewhere.

Click on the 'Payment Id' of the payment that needs to be removed

The 'Payment Overview' screen is displayed

Press the 'Update' button in the 'Payments Applied' box

The 'Payment Applications' screen is displayed

Locate the 'Billing Account Id' and 'Amount Applied'

Amend the 'Amount Applied' for the billing account

Press the 'Update' button next to the entry that refers to the 'Billing Account Id'

A message will be displayed saying that the payment has been removed from the billing account

How do I delete a payment from a billing account?

A payment can be removed from billing account by removing the link that has applied the payment to the billing account.

Click on the 'Payment Id' of the payment that needs to be removed

The 'Payment Overview' screen is displayed

Press the 'Update' button in the 'Payments Applied' box

The 'Payment Applications' screen is displayed

Press the 'Remove' button next to the entry that refers to the 'Billing Account Id'

A message will be displayed saying that the payment has been removed from the billing account

	The above example was done when the payment status was at 'Not Paid'
TO CHECK: need to test if it still works if the payment status is at 'Received' or 'Confirmed' too.
Help for Billing Account Orders

This sub menu lists the details of any Sales Orders that have been charged to the billing account.

A Sales Order is charged to a billing account by selecting the billing account as the Payment Method.

	The details displayed here in conjunction with the 'Payments' sub menu could also be used to generate a customer statement or account showing details of customer activity during a specified time period.
8.6. Agreements

An “agreement” is a way of recording a business arrangement or contract that your business makes with other companies or individuals. Some common examples of agreements include Payment Terms (where you allow a customer up to 30 days to pay you) or Prompt Payment Discounts (where you offer a reduction on the amount owing if your customer pays you before a certain date)

At the time of writing, OFBiz allows you to create the following type of agreements

Product

Purchase

Sales

Employee

Commission

End User Licence

The most common agreements you will use will be Sales Agreements (for your Customers), Purchase Agreements (for your Suppliers) and Commission Agreements (for your Sales Representatives).

8.6.1. Sales Agreement

A “Sales Agreement” is an agreement between you and your customers. A customer can also be another business. You can create a range of conditions for your customer including giving them such as payment discounts or special payment terms and credit limits.

If you have installed OFBiz with the demo data then there are already examples of Sales Agreements created for you.

8.6.2. Purchase Agreement

A “Purchase Agreement” is an agreement between your business and a supplier. You may have negotiated special conditions such as delivery, volume pricing and invoice terms.

If you have installed OFBiz with the demo data then there are already examples of Purchase Agreements created for you.

8.6.3. Commission Agreement

A “Commission Agreement” is an agreement that is used to calculate how much money a Sales Representative will get when products they have promoted or marketed are sold to customers. The rate paid to the Sales Representative is can be based on a fixed or variable on a percentage of each sale they make. These amounts can be quite small amounts so it can be easier to consolidate multiple commission payments into one large payment that is paid monthly.

If you have installed OFBiz with the demo data then there are already two example Commission Agreements created for you.

8.6.4. Agreement management in User Interface
Help for Find Agreements

The default screen is for the Agreements tab is 'Find Agreements'. It is used to locate existing agreements that have been created. The user has the option to

use the 'Find' button to locate an existing agreement or

create a new one by clicking on the 'Create Agreement' button.

How do I locate an existing agreement?

Enter search option details if known

Press the 'Find' button party

A list of existing agreements will be displayed

How do I create a new agreement?

Press the 'Create Agreement' button

The 'Edit Agreement' screen is displayed

Enter the details required and press the 'Submit' button

How do I cancel an agreement?

Locate the agreement required

Press the 'Cancel' button on the agreement entry that needs to be cancelled

Help for Edit Agreement

The 'Agreement' sub menu is used to enter the basic details required for setting up a new agreement or editing an existing one.

It can be used to create or update the following details for an Agreement:

The parties the agreement is between and their roles

The agreement type (eg Sales, Purchase, Commission, Employment etc)

Specific products

Start and End Date

Description

How do I edit an agreement?

Find the agreement that needs to be amended

Click on Agreement Id

The 'Edit Agreement' screen will be displayed

Amend the details required and press the 'Submit' button (NOTE: Additional agreement details can be updated via the other tabs eg Agreement Terms, Agreement Roles, Agreement Items and Agreement Work Effort Appls)

How do I copy an existing agreement?

Find the agreement that needs to be copied

Click on the Agreement Id How do it?

The 'Edit Agreement' screen will be displayed

At the bottom of the screen press the 'Copy' in the 'Copy Agreement' window (NOTE: The default tick boxes will copy the agreement terms, products and party. If not required then click on the boxes to stop them being copied)

Help Agreement Items List

This screen is used to display a list of items that have been created for an agreement.

Help for Edit Agreement Item

This screen allows specific items to be added to agreement. Currently these are limited to the following:

Pricing

Commission Rate

Sub-Agreement

Exhibit

Section

How do I create an agreement item?

Press the 'Create Agreement Item' button

The 'Edit Agreement Item' screen is displayed

Select the 'Agreement Item Type Id' from the drop down box

Use the drop down box to select the 'Currency' for the Agreement Item

Enter any 'Agreement Text' if required

Enter path for 'Agreement Image' if required

Press the 'Submit' button

A new sub menu will be displayed containing 'Promotions','Terms','Products','Party' and 'Geo' for additional details that can be setup for the agreement item

How do I edit an agreement item?

Select the agreement item to be updated by clicking on the Agreement Item Id

The 'Edit Agreement Item' screen is displayed How do it?

Update the fields required (NOTE: Additional details can be updated by selecting the Promotions, Terms, Product, Party or Geo sub menus)

The for Agreement Items Parties help screen

This screen is used to display any parties that have been linked to this agreement item.

How do I create a party for an agreement item?

Press the 'New' button

The 'Edit Agreement Item Party' screen is displayed

Manually enter or use the lookup to select the 'Party Id'

Press the 'Submit' button

How do I remove a party for an agreement item?

Press the 'Delete' button for the entry that needs to be deleted.

Help Edit Agreement Item Party

This screen is used to add or update a party linked to an agreement item. This could be useful for storing specific contact names associated with an agreement item.

How do I update a party for an agreement item?

Parties for an agreement item cannot be updated. They can only be added or removed.

Help for Agreements Item Terms

This screen is used to enter or maintain terms that are specific to an agreement item. The terms available are the same as those found under the 'Agreement Terms' tab and any related terms will be displayed both here and under the 'Agreement Items' tab .

How do I create a term for an agreement item?

Press the 'Create Term' button

The 'Edit Agreement Item Term' screen is displayed

Enter the term details required

Press the 'Submit' button

How do I update a term for an agreement item?

Select the term for the agreement item by clicking on the term id

The 'Edit Agreement Item Term' screen is displayed

Update the details required

Press the 'Submit' button

How do I delete a term for an agreement item?

Press the 'Remove' button on the term entry that needs to be deleted.

Help Edit Agreement Item Term

This screen is used to create or update the terms for an agreement item.
For more information about Agreement Term look at Help for Edit Agreement Terms

Help for Agreement Item Products

This screen is used to link a specific product or products to an agreement. This can be useful for restricting a discount or product pricing to a particular product (or range of products) for a specific customer.

How do I add a product to an agreement item?

Press the 'New Product' button

The 'Edit Agreement Item Product' screen is displayed

Manually enter or use the lookup to select the 'Product Id'

Enter the 'Price' to be associated to the product for this agreement item

Press the 'Submit' button

How do I update a product linked to an agreement item?

Select the product required by clicking on the 'Product Id'

The 'Edit Agreement Item Product' screen is displayed

Update the 'Price' for the product (NOTE: Only product price is available for update)

Press the 'Submit' button

How do I delete a product from an agreement item?

Press the 'Remove' button on the entry that needs to be deleted

Help Edit Agreement Item Product

This screen is used to create or update a product entry for an agreement item.

Help for List Agreement Item Supplier Products

This screen is used to link a specific product (or range of products) to an agreement. This can be useful for restricting a discount or product pricing to a product (or range of products) for a particular supplier.

	Products created here will be linked to the product and can be view using Catalog Manager. Entries can be viewed under the Product 'Suppliers' and 'Agreements' tabs.
How do I add a product to an agreement item?

Press the 'New Product' button

The 'Edit Agreement Item Product' screen is displayed

Manually enter or use the lookup to select the 'Product Id'

Enter the 'Available From Date'

Leave the 'Thru Date' blank

Using the drop down box select the 'Supplier Order Pref Id'

Enter the 'Last Price'

Enter 'Supplier Product Id'

Enter any other details as required or leave blank

Press the 'Submit' button

How do I update a product linked to an agreement item?

Select the product required by clicking on the 'Product Id'

The 'Edit Agreement Item Product' screen is displayed

Update the details as required

Press the 'Submit' button

How do I delete a product from an agreement item?

Press the 'Remove' button on the entry that needs to be deleted

Help Edit Agreement Item Supplier Product

This screen is used to create or update a product entry for a supplier agreement item. Any updates made in this screen can also be viewed in Catalog Manager for the product under the product 'Suppliers' and 'Agreements' tabs.

Help for List Agreement Geo

This screen is used to display a list of the geographical locations that are valid for the agreement item.

How do I create a new geographical location for an agreement item?

Press the 'New' button

The 'Edit Agreement Geographical Application' screen is displayed

Use the drop down box to select the 'Geo Id'

Press the 'Submit' button

How do I delete a geographical location for an agreement item?

Press the 'Delete' button for the entry that needs to be deleted

Help Edit Agreement Geo

This screen is used to create a geographical location for an agreement item.

	A new entry can be created or removed but not updated.
Help for Agreements Item Promotions

This screen is used to enter or maintain any promotions that are associated with the Agreement Item. This can be useful if you want to limit where a particular promotion is applied. Promotions are setup in Catalog Manager and can be selected here.

How do I add a promotion to an agreement item?

Press the 'Add New Promotion' button

The 'Edit Agreement Promo Applications' screen is displayed

Select the 'Product Promo Id' from the drop down box

Enter the 'From Date'

Enter the 'Thru Date' if required (NOTE:This can be left blank)

Enter the 'Sequence Num' if required

Press the 'Submit' button

How do I edit an existing promotion for an agreement item?

Select the agreement item promotion by clicking on on the promotion id

The 'Edit Agreement Promo Applications' screen is displayed

Update the details required

Press the 'Submit' button

How do I delete a promotion from an agreement item?

Press the 'Remove' button on the entry that needs to be deleted.

Help for Edit Agreements Roles

This screen is used to assign a party roles for an agreement.

How do I add a party role to an agreement?

Use the lookup to select the 'Party Id'

Use the drop down box to select the 'Party Role Id'

Press the 'Add' button (NOTE: If the party does not have this role associated with them then an error will be displayed)

The new entry will be displayed in the lower part of the screen

How do I update a party role for an agreement?

Party roles can only be added and deleted. They cannot be updated.

How do I delete a party role from an agreement?

Press the 'Remove' button for the entry that needs to be deleted.

Help for Edit Agreement Terms

Agreement Terms are the rules that make up the agreement. Agreements may have a one or more terms.

Examples of agreement terms from a sales and purchase viewpoint include the following:

Payment due within a certain timeframe (eg 30 days)

Discounts for early payment

Specifying Late fee penalties

Purchasing agreements

Specifying commission rates

Exclusive Relationship

	Agreements can also be specified for Employment, Legal, Non Compete etc.

Agreement terms are configured by linking them to the Invoice Item Type.

	The drop down box for 'Invoice Item Type' contains what appears to be duplicates for items such as 'Invoice Fee', 'Invoice Discount', 'Invoice Finished Good Item' etc.
These are NOT duplicates
- one of these entries refers to the Sales Invoice
- and the other refers to the Purchase Invoice.
As the descriptions are exactly the same it is impossible to know which refers to which so needs to be done using trial and error!
How do I add a payment term for 30 days?

Select 'Payment Net Days' from the 'Term Type Id' drop down box

Enter '30' in the 'Term Days' field

Press the 'Submit' button

How do I add a discount term of 2% if paid within 10 days?

Select 'Payment Discounted if paid with Specified Days' from the 'Term Type Id' drop down box

Enter '2' in the 'Term Value' field

Enter '10' in the 'Term Days' field

Press the 'Submit' button

How do I specify pricing in a specific currency only for thiscustomer or supplier?

This is done using the 'Agreement Items' sub menu

How do I delete a payment term?

Locate the payment term required

Press the 'Remove’on the entry that needs to be removed

Help for Agreement Work Effort Applications

This screen is used to link a work effort to the whole agreement or an individual agreement item.

How do I add a work effort to an agreement?

Use the drop down box to select the 'Agreement Item Seq Id'

Use the lookup to select the 'Workeffort Id'

Press the 'Add' button

The new entry is displayed in the lower part of the screen

How do I update a work effort for an agreement?

Work efforts can only be added or deleted. They cannot be updated

How do I delete a work effort from an agreement?

Press the 'Delete' button for the entry that needs to be deleted

Help for Agreement Content

This screen use for uploading any contents that concern the agreement. The screen consists of :

Add Agreement Content

Agreement Content List

Add Agreement Content

To upload the content. The content can be classified by choosing the Content Type Id and Mime Type Id.

Agreement Content List

To Show the list of contents. There are 2 buttons in each content:

Download : To download the uploaded content

Delete : To delete the uploaded content

8.7. Financial Accounts

A "Financial Account" is a tool (similar to bank account statement) that is used for monitoring monetary transactions. Normally it will be linked to a party and the various transactions details (e.g. payments or receipts) will be shown as entries.

Financial Accounts can be used for the following :

Managing and Tracking Customer Prepaid Accounts

Managing and Tracking Customer Credit Limit (NOTE: Need to verify this)

Managing Electronic Gift Certificates / Gift Vouchers/ Gift Card

Reload of Electronic Gift Card

Company Bank Account Transaction Tracking

At the time of writing, OFBiz allows you to create the following type of financial accounts

Bank Account

Credit Card Account

Deposit Account

Equity Line Account

Gift Certificate

Investment Account

Loan Account

Replenish Account

Service Credit Account

Store Credit Account

8.7.1. Bank Account

A "Bank Account" is a financial account between a bank and their customer. By default this type of financial account will post to 213500 CUSTOMER DEPOSIT ACCOUNTS.

If you have installed OFBiz with the demo data then there are already examples of Bank Accounts created for you.

8.7.2. Credit Card Account
8.7.3. Deposit Account

A "Deposit Account" is a financial account which allows money to be deposited and withdrawn by the account holder. By default this type of financial account will post to 213500 CUSTOMER DEPOSIT ACCOUNTS.

8.7.4. Equity Line Account
8.7.5. Gift Certificate

A "Gift Certificate" is something that entitles the recipient to select merchandise up to a specified value from a store. It is usually presented as a gift. By default this type of financial account will post to 213200 GIFT CERTIFICATES UNREDEEMED.

8.7.6. Investment Account

An "Investment Account" is a financial account that contains deposits of funds and/or securities that are held at a at a bank, stock exchange or other financial Institution. By default this type of financial account will post to 213500 CUSTOMER DEPOSIT ACCOUNTS.

8.7.7. Loan Account
8.7.8. Replenish Account
8.7.9. Service Credit Account
8.7.10. Store Credit Account

A "Store Credit Account" is a financial account that is used to to maintain the refund amount Specify the type (Billing Account or Financial Account) of Store Credit Account used for refund return. Default to Financial Account.

8.7.11. Financial Accounts in User Interface
Setup
	1) In GL Account Defaults there is a specific tab 'FinAccount Type Gl Account' for specifying which type of Financial accounts are posted to which general ledger account.
2) In GL Account Defaults there is also a tab 'Payment Method Id / GL Account ID' for specifying the account to post transactions to if 'Financial Account' is selected as the Payment Method instead of (Cash, Cheque, Credit Card, etc). By default the demo setup posts transactions to 111100 GENERAL CHECKING ACCOUNT.

You can also setup each financial account to post to a specific general ledger account for each party. This is done via a specific field during the creation or update of a financial account. This will override the default setting by type.

Help for Financial Account GL Account Type

The FinAccount Type GL Account (Financial Account Type / GL Account Type) is used to specify the default account to be used for a specific type of Financial Account.
This setup will translate to one side of the journal entry only.

	There is a limitation that only one account can be specified per Financial Account type.
Currently there are 6 types of Financial Account
(Bank, Deposit, Investment, Gift Certificate, Replenish, Service Credit)
so if you have more than one of these type of accounts that you need to track separately then there could be a problem.

This mapping is normally be triggered if something is paid or uses a Financial Account. Using the demo data this mapping is triggered when someone purchases a gift certificate, or pays money into a financial account.

How do I add a new Financial Account Type / GL Account mapping?

By default there are 4 Financial Account Type / GL Type mappings that are configured as part of the OFBiz demo data.

Select the 'FinAccount Type Id' from the drop down list

Select the ' GL Account' to map it to from the drop down list

Press the 'Add' button

The new mapping will be displayed in the list at the bottom of the screen

How do I update a Financial Account Type / GL Account mapping?

A Financial Account Type / GL Account Type mapping can be updated by modifying the GL Account only.
Unlike other screens in this area if the GL Account Type needs to be updated then it can be done by creating a new record with the correct GL Account type which will overwrite the existing record.

Locate the entry that needs to be updated in the list of Financial Account Type / GL Account Type mappings

Modify the 'GL Account 'by using the drop down list next to the GL Account field

Press the 'Update' button

The updated mapping will be displayed

How do I remove a Financial Account Type / GL Account mapping?

Locate the entry that needs to be deleted in the list of Financial Account Type / GL Account Type mappings

Press the 'Remove' button next to the entry

The Financial Account Main screen.

The default screen for Financial Accounts displays a list of any bank accounts that have been created. Details listed include the account the following

account name

organisation the account is linked to

account balances (available and actual)

Help for Find Financial Accounts.

This screen is used to locate existing financial accounts that have been created.

It also includes the option to use the 'Advanced Search' button to display additional fields that can be used to locate a specific financial account.

New Financial Accounts can be created using the 'Create New Financial Account' button.

How do locate an existing Financial Account?

Press the 'Search' button

A list of all existing Financial Accounts will be displayed.

How do I delete an existing Financial Account?

Press the 'Search' button on the Financial Account main screen

A list of all existing Financial Accounts will be displayed

Press the 'Delete' button next to the Financial Account that needs to be deleted.

Help for Edit Financial Account

This screen allows the user to create a new financial account or to edit an existing one.

The 'Financial Account' submenu is the first of four submenus used in the creation or update of a Financial Account. On the creation or update of a Financial Account it is the default screen that is displayed.

It can be used for updating the basic details of a Financial account such as:

Type of Account (eg Deposit, Investment, Gift Certificate)

Account Status (Active, Frozen, Cancel, etc)

Account Name and Code

Currency

Owner Party ID

Default GL Account for Posting

Replenishment Level

How do I create a new Financial Account?

Select the 'Create New Financial Account' button from the 'Find Financial Accounts' screen

The 'Create/Update Financial Account' screen is displayed.

Keep the default entry of 'Deposit Account' for the Fin Account Type field

Keep the default entry of 'Active' for the status field

Enter a description (eg ABC Customer Prepaid Account) for the 'Fin Account Name' field

Leave the Fin Account Pin field blank
(NOTE TO CHECK: I think this is only used in creation of Gift Cards and Certificates..)

Leave the Fin Account Code field blank
(NOTE TO CHECK: I think this is only used in the creation of Gift Cards and Certificates…​)

The currency field will be the default currency of Company (eg USD). If this account is to be in another currency (eg EUR) then select it from the drop down list.

Set the Organization Party ID field to be 'Company'

Fill in the Owner Party Id field with the party id of the customer who has the Financial Account (eg DemoCustomer or DemoCustCompany)

Fill in the 'Post to Gl Account field' to post the transactions for this financial account to post to a specific GL Account

Select the current date from the calendar to fill in the 'From date' field (NOTE: It can be left blank and still appears to work)

Leave the 'Thru date' field blank
(NOTE TO CHECK: I think this could be used to close or stop the use of an account ..)

Leave the default of 'Is Refundable' as 'Y'
(NOTE TO CHECK: I think this will allow money to be refunded to this account - eg if you have a return or credit for the customer)

Leave the 'Replenish Payment ID' blank
(NOTE TO CHECK: Not sure what this is - maybe to automatically replenish account if it gets to a certain limit???)

Leave the 'Replenish Level' blank
(NOTE TO CHECK: Not sure what this is but probably linked to Replenish Payment ID where you set the limit - eg $100)

Press the 'Create' button and message appears saying that the account was successfully created

How do I update an existing Financial Account?

Press the 'Search' button on the Financial Account main screen

A list of all existing Financial Accounts will be displayed

The 'Create/Update Financial' screen is displayed

Update the details of the financial account

Press the 'Update' button

Help for Edit Financial Account Authorizations.

An authorization is a temporary transaction showing a commitment to take money from a financial account. It is like a 'transaction in progress' where there can be delay between when you buy something and the time it actually appears on your statement.

Authorizations can be time limit specific meaning that they can be controlled by entering a start and end date so that they are only valid for a certain length of time.
They can also be expired.
When an authorization is expired it removes the commitment from the financial account.
The history of expired authorizations are shown on the financial account.

	This could be very useful in ensuring that customers are not overcommitted and keeping within their approved credit limits.
How do I add an authorization?

Enter an amount in the 'Amount' field (Eg 1000)

Leave the 'Currency' field blank as the default currency will be used

Enter a date in the 'Authorisation Date' field

Leave the 'From Date' field blank

Leave the 'Thru Date' field blank

Press the 'Add' button

	When you now view the Financial Account detail the 'Actual Balance' and 'Available Balance' fields will be different.
How do I update an authorization?

An authorization cannot be updated. It can only be expired. If you have made a mistake and need to change an authorization then it needs to expired and then re-created correctly.

How do I delete an authorization?

Authorizations are not deleted they are instead expired.
This means that the history of the authorizations will remain on the account as an audit trail.

Example: To expire an authorisation

Select the 'Authorizations' tab for the Financial Account

Any authorizations will be displayed at the bottom of the screen

If the authorization is still current the 'Thru Date' field will be blank
(NOTE TO CHECK: May not always be true as you can specify a future date for it to expire…​…​!!!)

Select the 'Expire' button next to the authorisation to be expired

The authorization is removed from the financial account and the screen is redisplayed with the 'Thru Date' field completed

Help for Edit Financial Account Roles.

The Financial Account Roles sub menu screen allows you specify a party and link them to a role for a particular financial account.

It can be used to add party roles eg 'Approver' or 'Administrator' for credit limits or updates to the account. If an account belongs to a company then you may want to add a person as a 'Contact' for dealing with the account.

The roles can also be time bound. This means that you can specify a start and end date for the party role.

How do I add a Party Role to a Financial Account?

Select the 'Roles' sub menu for the Financial Account

Fill in the Party Id field by using the field lookup tool or by directly entering the party id (eg flexadmin)

Select the role from the drop down list for the Role Type Id field (eg administrator)

Enter the From Date field

Enter if the Thru Date field (optional)

Press the 'Add' button

Help for Find Financial Account Transactions

A transaction is an entry that is shown on the financial account.

Transactions can be one of the following types:

Deposits

Withdrawals

Adjustments

Transactions are used to show entries and the financial history of the financial account. Similar to a bank account or credit card statement the transaction will show details of what was spent or paid into the account.

Some transaction totals have been added to this screen to help as part of the reconciliation processes. Additional details available include number of transactions, transaction totals and status.

How do I find transactions for a Financial Account?

Press the 'Search' button

A list of transactions for the financial account will be displayed

Help for Financial Account Transactions List.
How do I add transactions to a financial account?

An example of how to bring in an opening balance is shown below:

Navigate to the the Financial Account Transactions sub menu

Select 'Adjustment' in the Fin Account Trans Type Id field

Leave the 'Party Id' field blank

Fill in the 'Transaction Date' field

Fill in the 'Entry Date' field (NOTE TO CHECK: Need to check exactly what this is - is it the date the transaction is entered or is it the date the transaction is processed?)

Fill in the 'Amount' field with the transaction amount (Eg. In our case this is the opening balance such as 353.88 - dont think we need the $ sign)

Leave the 'Payment Id' field blank

Leave the 'Order Id' field blank

Leave the 'Order Item Seq Id' field blank

Leave the 'Reason Enum Id' field blank (NOTE TO CHECK: This could be useful in identifying transactions to a greater level of detail…​.)

Fill in the 'Comments' field (Eg: Opening Balance from XYZ Statement)

Press the 'Add' button and the transaction will be displayed at the bottom of the screen

	When you now view the Financial Account detail the 'Actual Balance' and 'Available Balance' fields will show the entered opening balance (eg 353.88)
Other ways to add transactions to a financial account?

By selecting financial account as a payment method for a customer

By selecting financial account as a refund method for a customer

Help for Financial Account Deposit / Withdraw

By default this screen will display all payment transactions both incoming and outgoing that have not already been associated with a financial account that represents one of the company’s bank accounts.

This screen also gives the option to create new deposit or withdrawal payments.

The user can select a number of incoming deposit payments (eg Customer Payments etc) and group them together into a payment group (i.e AR Batch of Payments) that will create a 'deposit slip'.

If you select a number of incoming payments and dont group them then no payment group is created (and therefore not deposit slip either) but the individual transactions will be created for the 'bank account' financial account.

	Outgoing payments cannot be grouped together and will not create a 'deposit slip'.
How do I list Deposit or Withdrawal Payments not linked to a Bank Account?

Press the 'Find' button on the 'Deposit/Withdraw' screen.

All deposit and withdrawal transactions not associated with a bank 'financial account' will be displayed.

How do I group payments and create a deposit slip?

Press 'Find' to list all Deposit or Withdrawal payments

Use the 'Select All' or click on the check box associated with the transactions required

Enter a name for the Payment Party Group Name (eg XYZ Deposits) to group the transactions together

Press the 'Deposit/Withdraw' button

A deposit will be created that can be viewed under the 'Deposit Slip' tab and grouped transaction will be created under the 'Transactions' tab with a link to the deposit slip breakdown

Help for Financial Account New Deposit Payment

This screen allows the user to create an incoming payment to a financial account that has been linked to the company bank account.

How do I create a New Deposit Payment?

Press the 'Create New Deposit Payment' button

The 'Create New Deposit for Financial Account' screen is displayed

Select the 'Payment Type' from the drop down menu (NOTE: Only incoming transaction payment types are shown)

Select the 'Payment Method Type' from the drop down menu (eg Cash)

Enter or use the lookup to select the 'From Party Id' (eg DemoCustomer)

Enter or use the lookup to select the 'To Party Id' (eg Company)

Enter the date of the deposit in the 'Effective Date' field

Enter the amount in the 'Amount' field for the deposit

If required then tick the box next to 'Deposit Payment in:…​.'
(NOTE: If this is ticked then the transaction will not be displayed and so will not have a deposit slip associated with it)

Press the 'Create' button

The new transaction will be created.

	The default status of the payment will be 'Received'.A new payment transaction will be created and it will be linked to the specified bank account but the status of the transaction will be 'Created'.
How do I view a newly created Deposit Payment transaction?

Go to the 'Transactions' submenu

Press the 'Search' button

The newly created transaction should be displayed in the search results at the bottom of the screen.

	If when the transaction was created the 'Deposit Payment in:…​.' was ticked then the transaction will not be displayed on this screen.
It will still show up under the 'Transactions' tab and linked to the bank account.
Help for Financial Account New Withdrawal Payment.

This screen allows the user to create an outgoing payment to a financial account that has been linked to the company bank account.

How do I create a New Withdrawal Payment?

Press the 'Create New Withdrawal Payment' button

The 'Create New Withdrawal for Financial Account' screen is displayed

Select the 'Payment Type' from the drop down menu (NOTE: Only outgoing transaction payment types are shown)

Select the 'Payment Method Type' from the drop down menu (eg Cash)

Enter or use the lookup to select the 'From Party Id' (eg Company)

Enter or use the lookup to select the 'To Party Id' (eg DemoSupplier)

Enter the date of the withdrawal in the 'Effective Date' field

Enter the amount in the 'Amount' field for the withdrawal

If required tick the box next to 'Withdrawal Payment from:…​.'
(NOTE: If this is ticked then the transaction will not be displayed but it can be found under the 'Transactions' tab for the bank account.)

Press the 'Create' button

The new transaction will be created.

	The default status of the payment will be 'Sent'. A new payment transaction will be created and it will be linked to the specified bank account and will have a default status of 'Created'.
How do I view a newly created Withdrawal Payment transaction?

Go to the 'Transactions' submenu

Press the 'Search' button

The newly created transaction should be displayed in the search results at the bottom of the screen.

	If when the transaction was created the 'Withdrawal Payment from:…​.' was ticked then the transaction will not be displayed on this screen.
It will still show up under the 'Transactions' tab and linked to the bank account
Help for Find Deposit Slips.

This screen is used to locate payment groups and their associated deposit slips that have been created.
Deposit slips are created by grouping transactions together into a Payment Group.
This can be done using the 'Accounting / Payment Group' tab, the 'Financial Account / Deposit Withdraw' tab or the 'Create New Deposit Slip' button.

Currently Deposit Slips are created for AR Batch Payments only.

The deposit slips are available in PDF format and there is an option to cancel the batch that generated the deposit slip if required.

How do I locate an existing Deposit Slip?

Enter some characters from the 'Payment Group Id' or 'Payment Group Name' if known

Press the 'Search' button

How do I update an existing Deposit Slip?

Locate the Payment Group required

Select the Payment Group by clicking on the Payment Group Id

The 'Edit Payment Group' screen is displayed

Add any new payment deposits or update existing deposits for the Payment Group

All changes in the Payment Group will automatically be updated to the Deposit Slip

How do I delete an existing Deposit Slip?

A deposit slip can not be directly deleted but it is removed when a Payment Group is cancelled

Press the 'Cancel' button next to the Payment Group required to cancel a payment group

The Payment Group is removed from the 'Find Deposits' screen and no deposit slips can be viewed or printed.

Help for Financial Account New Deposit Slip

This screen allows the user to create an Payment Group and the transactions associated with the Payment Group will generate a deposit slip.

How do I create a New Deposit Slip?

Press the 'Find' button to list all the available transactions

Select the transactions to include in the Payment Group by using the 'Select All' or the check box that corresponds to the transactions required

Enter a 'Payment Group Name' if required (If none is entered then by default this will be 'Payment Group Name')

Press the 'Create Batch' button

A button to print the deposit slip will be displayed as well as the edit screen to make any further changes to the Payment Batch

Help for Financial Account Edit Deposit Slip and member

This screen displays the details of a Payment Group and its transactions. The Deposit Slip for the Payment Group can be printed if required and the Payment Group itself can be updated.

Details that can be updated include the name of the Payment Group itself and the addition, removal or update of transactions.

	Any changes to the Payment Group will be automatically updated to the Deposit Slip.
How do I update a Deposit Slip?

Select the Payment Group required

Update the 'Payment Group Name' if required

Use the lookup for 'Payment Id' to add new transactions to the Payment Group if required

Use the 'Cancel' button next to a particular transaction to remove it from the Payment Group

Press the 'Update' or 'Add' buttons as required

Press the 'Print Deposit Slip' button

The Deposit Slip will be displayed with the latest details of the transactions for the Payment Group

Help Find Financial Account Reconciliations.

This screen displays the details of any reconciliations in progress for a financial account.
Only reconciliations that have actual transactions associated with them will be displayed.
If a reconciliation group has no transactions assigned to it then it will not be displayed.


Help for Financial Account Bank Reconciliation.

Bank Reconciliation is a regular task where transactions from the company bank statement are matched against transactions that have occurred in the General Ledger. This is done based on a specific date

	This can be done daily, weekly but is usually an end of month.

A specific GL account is normally used to represent the company bank account and any accounting transaction that involves the bank account will automatically record and entry in the GL.

The bank reconciliation process ensures that the GL account and the bank statement reconcile to the same amounts.

Differences can occur between the GL and the bank statement for a variety of valid reasons including the following:

Payments or Deposits in process (especially cheques)

Interest or Bank Charges that are not known in advance but are applied to the bank account

Currency or Exchange Rate variations / charges

Any outstanding

	The differences will occur because of timing differences of when and how transactions are recorded. Examples are as follows:
1) Bank charges are known to the bank first and only once they have applied the charge to the bank account can the company duplicate the transaction in the GL to make the balance reconcile.
2) A customer cheque payment may be recorded in the GL first before it is paid into the bank account
How do I create a Bank Reconciliation?

The bank reconciliation process is made up of 3 steps.

Creating an account reconciliation group

Assigning transactions to the reconciliation

Validating the figures and confirming the reconciliation

How do I create an account reconciliation group for BankReconciliation?

Go to the Financial Account 'Reconciliation' sub menu for the bank account to be reconciled

Press the 'Create New Financial Account Reconciliations' button

Complete the details (eg name, description, organisation and opening balance) required on the 'Add New Financial Account Reconciliations' screen and press the 'Create' button

The new account reconciliation group is created and may be used to assign transactions to

How do I locate transactions that have not been assigned to aBank Reconciliation?

Go to the Financial Account 'Transactions' sub menu of the bank account to be reconciled

The 'Find Transactions For Financial Account: XXXX' is displayed

Use the dropdown box for 'GL Reconciliation Id' field to select 'Not Assigned' and then press the 'Search' button

A list of transactions (deposits, withdrawals or adjustments) that have not been reconciled will be displayed
(NOTE: If no transactions are displayed then there are no transactions to reconcile)

Click on the 'check box' at the end of the transaction line that corresponds to the entry that needs to be assigned
(NOTE:More than one transaction can be selected at a time)

Above the 'check box' is the 'Assign to Reconciliation' button and to the left of this is a dropdown box to select the reconciliation that the transaction is to be assigned to.

Using the drop down box select the reconciliation required and press the 'Assign to Reconciliation' button

The transaction is removed from the 'Not Assigned' status and added to the specified reconciliation group

How do I validate and confirm the Bank Reconciliation?

Validation can be done for individual transactions or for the complete account reconciliation group.
The user controls this by the search criteria entered on this screen.

Go to the 'Transactions' sub menu for the bank account and press the 'Bank Reconciliation' button

Select the 'GL Reconciliation Id' that is to be reconciled

Click on the 'Select All' check box on the right hand side of the screen. (NOTE: All transactions in this group will be reconciled)

Press the 'Reconcile' button above the 'Select All' check box

How do I view a Bank Reconciliation?

Once all the transactions in a reconciliation group have been reconciled then the status of the group is changed to 'Reconciled'. This means that no new transactions can be added to the is group and the reconciled balance is fixed.

Go to the 'Reconciliation' sub menu for the bank account

A list of all the bank reconciliation groups are displayed with details of the status (eg Created or Reconciled)

Click on the 'GL Reconciliation Id' of the group and the details are displayed

How do I cancel a Bank Reconciliation?

If a bank reconciliation needs to be cancelled due to a mistake or error then the bank reconciliation can be cancelled as long as it has not been fully reconciled (i.e. the status of the reconciliation has not been changed to 'Reconciled'). This will allow you to start the bank reconcilation again.

Go to the 'Reconciliation' sub menu for the bank account

A list of all the bank reconciliation groups are displayed (NOTE: If no transactions are associated with a reconciliation group then it will not be displayed here)

Click on the 'Cancel' button associated with the 'GL Reconciliation Id' of the group that needs to be cancelled

All transactions will be removed from the reconciliation group and their status will be changed back to 'Not Assigned' so that they can be re-assigned to this or any other reconciliation.

Help for Edit Financial Account Reconciliations

This screen is used to create or update a reconciliation group / bank reconciliation.

The following details can be input or updated for the reconciliation:

GL Reconciliation Name or Identifier

Description for the reconciliation

Organisation Party Id for the reconciliation

Opening Balance for the reconciliation

Reconciliation date

Help for View Financial Account Reconciliations

This screen gives an overview of a reconciliation group / bank reconciliation.
Note that a reconciliation must have at least one transaction associated with it for this screen to be displayed. It is used as follows:

to view transactions associated with a reconciliation group / bank reconciliation

to remove transactions from a reconciliation group / bank reconciliation

to reconcile the reconciliation group / bank reconciliation

The screen displays the current reconciliation details plus details of the previous reconciliation if one exists. This ensures the closing balance of the previous reconciliation is the same as the opening balance for the current one.

How do I edit reconciliation?

Press the 'Edit' button in the 'Current Bank Reconciliation’part of the screen

The 'Edit Financial Account Reconciliations' screen isdisplayed

Update the details required

Press the 'Update' button

How do I remove a transaction from a bank reconciliation?

On the lower part of the screen a list of all transactions associated with the reconciliation is displayed.

Press the 'Remove' button next to the entry that needs to be removed

The transaction is removed

How do I reconcile a bank reconciliation?

A total of all transactions associated with the reconciliation is shown in the lower part of the screen

Press the 'Reconcile' button next to the total

Each transaction status will be changed to 'Approved' and the reconciliation / bank reconciliation status will be changed to 'Reconciled'
(NOTE: This means that no new transactions can be added to this reconciliation and it will no longer be available to assign transactions to)

8.8. Tax Authorities.

A tax authority is legal body usually the state (country) that imposes a financial levy on business transactions.

In OFBiz tax authorities are used to calculate where business or related taxes are due.

Tax setup is very important as it links into the calculated price that you can charge your customers and also flows through into any related legal documents that are generated (eg Sales Order, Sales Invoice, Purchase Order etc).

Each country or region will have specific rules regarding what should or should not be taxed. There will also be very strict regulations on how taxable transactions should be recorded and tracked in the general ledger or chart of accounts.

Tax authority setup allows configuration of the following :

Income tax

Value Added Tax (VAT) / Goods and Services Tax (GST)

Import / Export tax /Custom and Excise Duty

State, City or County taxes

8.8.1. Tax Authorities management in User Interface
Help for Find Tax Authorities

The default screen displays a list of Tax Authorities that have been setup.

	You will need to create a party in Party Manager for the tax authority before you can add a new tax authority in the accounting / tax authorities screen.

Steps to create the party to be used for the tax authority are as follows:

Create New Party Group

Fill in basic details (eg name, address etc)

Once the party record is created then add the role of 'Tax Authority' to the party

Only when the tax authority party record is created can you continue.

How do I create a new tax authority?

Press the 'New Tax Authority' button

Select or enter the code for the country, state or region that is applicable for the 'Geo' field

Select or enter the party id of the Tax Authority party that has been created in Party Manager

Leave the 'Require Tax Id for Exemption' field at its default of 'Y'
(NOTE: This triggers tax not to be charged if a valid Tax Id is found!)

Leave 'Tax Id Format Pattern' blank
(NOTE: This specifies the format of the Tax Id so that it can be validated)

Fill in the 'Include Tax in the price' - the default is 'N'.
(NOTE: If prices need to include tax such as GST or VAT in the price then change this to 'Y')

Press the 'Update' button

	The above process creates the basic tax authority detail but there are further details that can be added via the other tax authority sub menus
How do I update a tax authority?

Select the 'Edit' button next to the tax authority that you wish to update

The 'Edit Tax Authority' screen is displayed

Update the details of the tax authority as required including any submenus

Press the 'Update' button

How do I delete / remove a tax authority?

Tax authorities cannot be deleted via the Tax Authority screens. If they need to be removed then it can be done via the Webtools and Entity Data maintenance.

	Be very careful removing tax authorities records unless you are completely certain that they have not been already used for transaction calculations.
Help for Edit Tax Authority

The 'Edit Tax Authority' sub menu is the first of six sub menus used in the creation or update of a Tax Authority. On the creation or update of a Tax Authority it is the default screen that is displayed.

It can be used for updating the basic details of a Tax Authority such as:

Changing whether a tax id or code is required for an exemption

Modifying the tax id or code format

Updating where or not to include the tax calculation as part of the product price

	An example of the Tax Id is as follows:
\d{2}\-\d{7}|\d{3}\-\d{2}\-\d{4} which translates to 99-9999999 or 999-99-9999
Help for Edit Tax Authority Categories

The Tax Authority Categories sub menu screen allows you link a tax authority to a specific catalog or product category.

It can be used to add product categories to a tax authority. This means that all products in this category will be taxed at the rate specified for the tax authority.

An example of this could be separating products into categories for export to different countries. A separate tax authority will be associated with each category so that the specific tax rate for each of them will be applied.

How do I add a new Tax Authority / Category mapping?

Enter or Lookup the 'Category Id' to be mapped

Press the 'Add' button

The new mapping will be displayed at the bottom of the screen

How do I update a Tax Authority / Category mapping?

A Tax Authority / Category mapping cannot be updated. If it needs to be changed then the entry must be deleted and then re-entered.

How do I remove a Tax Authority / Category mapping?

Locate the entry that needs to be removed

Press the 'Delete' button next to the entry

Help for Edit Tax Authority Associations

An association is a way of specifying how tax authorities can be linked to each other.

It can be used in the situation where the tax structure is hierarchical (eg city tax, plus county tax plus state tax).

Using associations allows tax rates from multiple authorities to be applied to a particular order at once.

How do I add a new association for a Tax Authority?

Enter or use the lookup to find the 'To Tax Auth Geo Id'

Enter of use the lookup to find the 'To Tax Auth Party Id'

Leave the 'From Date' blank (NOTE: It will default to the current date and time)

Leave the 'Thru Date' blank

Select the 'Type' from the dropdown or leave blank

Press the 'Add' button

The new tax authority association is displayed at the bottom of the screen.

How do I update an association for a Tax Authority?

Only two fields are available for update, these are the 'Thru Date' and 'Type'

Enter the changes required

Press the 'Update' button next to the entry updated

How do I remove an association for a Tax Authority?

Press the 'Delete' button next to the entry that needs to be deleted

Help for Edit Tax Authority GL Accounts

The GL Accounts sub menu screen allows you specify which general ledger account any tax calculated for this tax authority will be posted. This is done at at organisation level so the minimum requirement is that 'Company' is setup.

It is used to consolidate taxes for a specific tax authority into one general ledger account. It can be very useful if you need to track taxes for several tax authorities (eg different states or countries).

How do I add a new general ledger account for a Tax Authority?

Enter or use the lookup to select the 'Organisation Party Id'
(NOTE: Normally this would be 'Company')

Enter or use the lookup to select the 'GL Account'

Press the 'Add' button

	The GL account used must have already been created in the Global GL Settings and linked to the chart of accounts for 'Company'
How do I update a general ledger account for a Tax Authority?

The general ledger account can be updated by simply adding a new account to replace the existing entry.

Enter or use the lookup to select the 'Organisation Party Id'
(NOTE: Normally this would be 'Company')

Enter or use the lookup to select the updated 'GL Account'

Press the 'Add' button

The existing entry will be replaced by the updated GL Account

	Be careful when updating a general ledger account because some transactions may have already been posted to the existing account.
How do I delete a general ledger account for a Tax Authority?

Locate the entry required

Press the 'Delete' button next to the entry that needs to be deleted

The entry is removed

Help for Edit Tax Authority Product Rates

This screen allows the setup of tax rates and types. The rates or type can be assigned globally to a store (ie tax will be applied to all products at the same rate) or category (ie limited to products in a specific category).

Other parameters are available to allow the user to limit whether the tax is to be applied to all purchases / sales or only those which are above a certain threshold.

Tax associated with shipping charges or promotions can also be configured here.

How do I add a new product tax rate?

Use the drop down box to select the tax 'Type' (eg Sales Tax)

Use the lookup to select a 'Store Id' (or leave blank for all Stores)

If a category has been setup it will be available for selection in 'Category' field otherwise leave this blank

Leave 'Title Transfer' blank

Enter a value for the 'Minimum Price' for a product where the tax is to be applied
(NOTE: The Demo Data sets this as zero)

Enter a value for the 'Minimun Purchase' where the tax is to be applied
(NOTE: The Demo Data sets this as zero)

Use the drop down box to select whether 'Shipping Charges' will be taxable

Enter the tax rate in the 'Tax Percentage' field (eg 12.5)

Use the drop down box to select whether products on 'Promotion' will be taxable

Leave the 'From Date' and 'Thru Date' blank

Enter the name of the tax in the 'Description' field (eg VAT) as this will be displayed and printed on documents when the tax is applied

Press the 'Add' button

How do I update an existing product tax rate

Select the entry that needs to be updated

Make the changes required

Press the 'Update' button next to the entry that needs to be updated

How do I delete a product tax rate?

Press the 'Delete' button next to the entry that needs to be removed

	The deletion of tax rates may cause audit problems particularly if the rate has already been used as part of a transaction.
In this case it would be better to expire the old rate using the 'Thru Date' field and then enter the new rate.
Help for List Tax Authority Parties

This screen list any parties that have been associated with a tax authority and tax rate. To have any tax calculated for Sales Orders or Purchase Orders then an entry must exist for 'Company'.

Entries can also be created, updated or deleted.

How do I add a new Tax Authority Party Info?

Press the 'New Tax Authority Party Info' button

Enter or use the lookup to select the 'Party Id'

Leave the 'From Date' blank
(NOTE: Default will be current date and time)

Leave the 'Thru Date' blank

Enter the 'Party Tax Id' if required
(NOTE: This can be VAT or GST number)

Use the drop down box to select whether the party select is 'Tax Exempt'

Use the drop down box to select whether the party selected is 'Nexus' (See note below)

Press the 'Create' button

	'Nexus' is a term that refers to an agreement for between the tax authority and potential tax payer that the tax authority can impose the tax. This is usually for Sales Tax.
If you have a Sales Tax that is uniformly applied to a product or range of products then the 'Nexus' field can be set to 'Y'
How do I update a Tax Authority Party Info?

Press the 'Edit' button next to the entry that needs to be amended

Update the fields as required

Press the 'Update' button

How do I delete a Tax Authority Party Info?

Press the 'Delete' button next to the entry that needs to be deleted

Help for Edit Tax Authority Party Info

This screen is used to create or update details for a Tax Authority Party entry.

If a new entry is being created all fields are available to be entered.

If an existing entry is being updated only limited fields are available to be amended.

8.9. Global General Ledger Settings

The Global General Ledger Settings are master templates that we can use to setup up our chart of accounts, default transactions or other settings that can be applied across many OFBiz modules.

We need settings at a global level because OFBiz is an integrated system so certain areas like accounting are linked to many other modules. It also makes sense to have a central place to setup things that will be used globally.

At the time of writing, the following are available as part of the Global GL Settings:

Chart of Accounts - a comprehensive master template for a complete chart of accounts.

Custom Time Periods - a master list to display or setup financial periods

Costs - a master list of any cost calculations to be used for assets or tasks

Payment Method Type - a master list of the ways payments can be made (e.g. cash, credit card etc) and the default accounts to be used for each

Invoice Item Type - a master list of all the transaction line types that can occur on any invoice and the default account to be used for each

Rates - a list of rates (e.g. pay rates, overtime rates etc) that can be used for billing work,tasks or as part of salary calculations

Foreign Exchange Rates - a master list of exchange rates to be used and dates they are valid

GL Account Category - currently this is set to be a list of cost centres

Cost Centers - a way to specify how to process percentage allocations between cost centres for specific accounts

	Some of the configuration specified here can be over-ridden using the 'Organization GL Settings' tab
8.9.1. Master Template - Chart of Accounts

If you load the demo data, then by default over 450 accounts are included as part of the OFBiz global chart of accounts master template.

To setup a chart of accounts in OFBiz simply means that we need to select the accounts we want to use from the global chart of accounts master template.

All general ledger accounts must exist in the global template before they can be assigned to be used at the organisation level (e.g. Company)

Help Find Global GL Account

The default screen for the Global GL Settings tab is 'List Accounts'.

It is used to view or edit the details of the general ledger accounts in the global template and there are options to print or export the account details.

How do I view details for an account?

Locate the account required

Click on account id

The account details will be displayed

Help for Navigate GL Accounts

This screen is split into two areas:

one for navigating the general ledger accounts in the global template and;

the other for adding or editing the details of an account

This screen can also be used as follows:

To locate a particular account

To view the chart of account structure or hierarchy

To update the details of an existing account

To add a new account to the chart of accounts template

	When adding or creating an account it is important to understand the fields used in the chart of accounts hierarchy.

The following list tries to define these.

GL Account Id: A unique identifier used to identify the account. (NOTE: If using the demo data chart of accounts template then keep any new accounts within the same structure)

GL Account Type Id: This appears to be a way of translating a business transaction into an accounting transaction
(NOTE: In 'Organization GL Settings / Setup / GL Account Type Defaults' it is the GL Account Id that is used to specify which GL account that particular type of transaction will post to such as Accounts Payable, Accounts Receivable etc. When a payment is created thne based on the type of payment made such as 'Customer Deposit' then it will translate to a GL Account Type Id which in turn will map to an actual GL Account)

GL Account Class Id: This appears to be a classification system and hierarchy for reporting purposes.

GL Resource Type Id: This appears to be a way of specifying the type of account possibly for reporting (eg Services, Finished Goods, Labour, etc)

GL Xbrl Class Id: This appears to be indicate the which accounting standards are used. Current examples are as US Generally Accepted Accounting Principles (US GAAP) or International Accounting Standards (IAS)

Parent GL Account Id: The GL Account of an account that is the next level up in the chart of account hierarchy

Account Code: This is the same as the GL Accound Id…​not sure why???

Account Name: The name or description of the account

Description: A further or long description of the account or the details it will contain

Product Id: This may be for specifying that only details for a specific product can be posted to this account
…​Needs To be verified…​

Posted Balance: For the Global Template this cannot be updated and is zero

How do I add a new GL account?

Click on the 'Navigate Accounts' tab

The default display will be to add a new account

Enter the 'GL Account Id' for the new account
(NOTE:This must be entered)

Enter the 'GL Account Type' for the new account

Enter the 'GL Account Class Id' for the new account

Enter the 'GL Resource Type Id' for the new account

Enter the 'Parent GL Account Id' if required

Enter the 'Account Code' for the new account
(NOTE: This should be the same as the GL Account Id)

Enter the 'Account Name' for the new account

Press the 'Add' button

How do I update an existing GL account?

Use the 'Navigate Accounts' window to find the account required

Click on the Account Id and the details will be displayed in the lower part of the screen

Update the details required

Press the 'Update' button

Help for Assign GL Account

The chart of accounts for the default organisation is built up by selecting or 'assigning' accounts that you want to use from the global chart of accounts master template.
This means that if you want to create a new account then it needs to be created in the global chart of accounts before it can be assigned to be used.

How do I assign a GL account?

Click on the 'Assign GL Account' tab

Use the drop down box to select the 'GL Account Id' to required

Use the drop down box to select the 'Party Id' to assign the GL Account to
(NOTE: Only parties that have been setup under 'Organization GL Settings' will be displayed)

Press the 'Create Assignment' button

	All assignments for a party can be viewed under 'Organization GL Settings / Setup / Chart of Accounts' for the party required.
8.9.2. Custom Time Periods

Time periods are a defined period of time (usually a month, quarter or year) that is used to group business transactions. It is a key part of any general accounting setup. Time periods can be used for the definition of :

Company Financial Year

Fiscal / Tax Periods (weeks, months, quarters)

VAT / GST Periods

Sales Periods

8.9.3. Costs

A business is designed to be profi table. This means that you need to be able to track all the costs involved in your business to ensure that you are not losing money.

Some example costs that you may want to setup and track are as follows:

Raw Materials Costs

Labour Costs

Rental Costs

Electricity Costs

Quality Assurance or Regulatory Costs

Direct and Indirect Costs

Costs can also be broken down into “Direct” and “Indirect” costs. Direct costs are costs that are easily identifiable as directly related to what you do to produce and sell to your customers.

Indirect costs are costs that cannot easily be directly linked to what you on sell to your customers. Included in this would be rent, electricity or general administration costs.

Fixed and variable Costs

Variable costs are those that rise and fall based on the amount product you produce or sell. If you sell or produce a lot of products it will cost more than if you produce a smaller amount.

Fixed costs are ones that remain the same no matter how much is being produced or sold.

Before you can calculate costs you need to define a formula of how to do it and in OFBiz this is called a “Cost Component Calculation”.

8.9.4. Payment Method Type

A “Payment Method” is simply a way to define the ways in which payments can be made. Examples include:

Cash

Cheque

Electronic Funds Transfer

Billing Account

Paypal

Financial Account

Gift Certificate

Each payment method can be linked to a different General Ledger account in the Chart of Accounts. By doing this OFBiz will be able to help us create an accounting transaction based on how the payment wasmade. This is very useful if we want to automate the creation of accounting transactions.

8.9.5. Invoice Item Types

An “Invoice Item Type” is another way to describe the different type of individual line items that appear on an invoice. For example an invoice is usually made up of:

A header - which contains details of the supplier, customer, invoice date etc

Line items - which are the products, taxes, discounts etc on the invoice

A footer - which summarises the totals, taxes and discounts

Invoice item types can refer to any of these three areas on an invoice. They can also be broken down into specific categories that allow us to classify or report on the total or frequency of that type.

Some examples of Invoice Item Types are:

Type of Product (Standard, Digital, Service)

Shipping or Handling Charges

Promotions (Discounted Products, Free Products)

Discounts (Product Discount, Invoice Discount, Early Payment)

Returned Items (Faulty, Replacement)

OFBiz allows us to setup a code for each of the different line item types that can appear on an invoice. We can then link each item type to a specific General Ledger account. By doing this OFBiz will be able to help us create an accounting transactions based on the item types that appear on the invoice.

This is very useful if we want to automate the creation of accounting transactions.

8.9.6. Rates

Rates are used to create a “pay rate” or “charge amount” that can be used in the calculation of a task, employee salary or a service that involves people.

Rates are closely linked to the OFBiz Human Resources Manager application but are also used across multiple OFBiz applications (Manufacturing, Asset Maintenance, Project Tasks, Timesheet Entry etc) where person related work tasks are required.

8.9.7. Foreign Exchange Rates

Foreign exchange rates are used to convert from one currency to another. A business will usually want to work in one main currency (e.g. GBP) but will allow transactions in other currencies (e.g. EUR, USD). These currencies will need to be converted to the main currency in order to generate financial reports (e.g. Balance Sheet or Income Statement) and most importantly to adhere to Tax Authority regulations.

Help for View Foreign Exchange Rates

OFBiz currently allows you to input to 3 different rates for the same currency using the 'Purpose' field. With this you can specify whether the conversion is to be used internally, externally or leave the field blank. Also the start and end date for a conversion can be specified beforehand.

How do I add a new foreign exchange rate?

To add a new rate for US Dollars (USD) to Euro (EUR)

Using the drop down box on the 'From Currency' field, select 'American Dollar - USD'

Using the drop down box on the 'To Currency' field, select 'Euro - EUR'

The 'Purpose' field can be left blank or you can select 'Internal Conversion' or 'External Conversion' from the drop down list

Enter the exchange rate in the 'Rate' field (eg 0.72883)

Enter the 'From Date' (NOTE: If left blank then will default to the current date and time)

Leave the 'Thru Date' blank

Click the 'Update Foreign Currency Rates' button

The new foreign exchange rate will be displayed

How do I update an existing foreign exchange rate?
	Existing foreign exchange rates cannot be updated - instead the existing rate is expired and a new rate is created.

Currently up to 3 different exchange rates can be created by using the 'Purpose' field to distinguish them.

How do I delete a foreign exchange rate?

Foreign exchange rates cannot be deleted. Existing rates can be expired by entering a new exchange rate for the same currency and purpose.

8.9.8. GL Account Category

A “General Ledger Account Category” (or GL Account Category) is a generic term to describe the way you can segment or classify accounts. Categories can be setup and then linked to the required accounts.

Another way to think about it is that it is like adding an extra tag to an account so that you can easily retrieve that account to do any additional reporting or processing.

In OFBiz at the time of writing, the GL Account Category has been used to implement cost centre functionality for the Chart of Accounts.

8.9.9. Cost Centers

A cost centre is an area or part of an organisation where costs (direct or indirect) can be allocated .

By default OFBiz will allocate and post 100% of any accounting value to the specified General Ledger account. Setting up Cost Centres allows you to split the amount across different areas using a percentage calculation.

For example: You want to buy something that and three departments will contribute to buying it. If the product costs $90 then each department will pay $30 towards the cost.

OFBiz will allow you to setup the percentage that each cost centre will contribute so that you can view and track how much each department has contributed or spent.

8.10. Organization GL Settings.
8.10.1. Help for setting by domain
Help for Available Internal Organizations

The default screen shows a list of Party Groups that have the role of 'Internal Organization' associated with them.

If you have installed the demo data then the default company 'Company' as well as departments / business units and regional subsidiaries will be displayed.

For each 'Internal Organization' there is the ability to set the currency, fiscal periods and invoice prefixes.

Help for Accounting Preferences

Accounting Preferences are a set of configuration details that are related to a party. To appear on this screen the party must be setup with the role of 'Internal Organisation'. This means that you can add the internal organisation role to a party and they will be added to this screen and then can be configured.

The master default party is 'Company' but preferences can also be setup for internal departments. The demo data shows some examples of this (eg Marketing, Accounting, Sales, Development etc). Unless overridden then then all other parties appearing on this screen will take their default setup from 'Company'

	The majority of the configuration information displayed in Accounting Preferences are taken from the Enumeration entity.

It is used for setting specifying information related to the accounting setup for a specific organisation or parties that exist within an organisation such as business units, cost centres, departments ,subsidiaries etc.

Information that can be setup include the following:

The start date of the Time Periods and Fiscal or Accounting Year (eg 1st April, 1st January, 1st June etc)

Tax Return Form
(NOTE: Need TO CHECK how important this is and where it is used…​…​.possibly some kind of reporting???)

The method to be used for calculating Cost of Goods Sold (COGS)

Base Currency - eg USD, GBP, EUR etc
(NOTE: May have main company in USD but a subsidiary in EUR etc)

Invoice prefix, numbering and sequencing (eg you may want each business unit / subsidiary to have its own invoice numbering or sequence etc)

Quote prefix, number and sequencing

Method to be used for refunds (eg cheque, direct bank credit, voucher credit etc…​)

Specify which journal will be used to store error transactions

	Key things that are usually need to be amended include the base currency for the company, fiscal year information and invoice numbering prefix or sequencing.
How do I create or setup a new Accounting Preference?
	A party must be setup with the role of 'Internal Organisation' before it will appear on the Accounting Preferences screen so that it can be setup.

Select the 'Setup' button next to the party to be setup

The Accounting Preferences screen is displayed.
(IMPORTANT: The first time this screen is displayed all of the fields will be modifiable. Once this has been saved only certain fields will be modifiable!!)

The default entries will be based on (or inherited from) 'Company'

Enter any changes that are required (eg Invoice Prefix, Error Journal name; as you may want error transactions from separate departments to be handled differently…​)

Press the 'Add' button

How do I update an Accounting Preference?

Select the 'Setup' button next to the party to be setup

The Accounting Preferences screen is displayed but only certain fields will be modifiable

Enter any changes required

Press the 'Update' button

	If you need to change any of the fields that are not modifiable then it can be done via the Entity Data Maintenance on Webtools menu using the PartyAcctgPreference entity.
You will need to be careful in editing an existing preference especially if the configuration already been used for transactions.
How to I delete an Accounting Preference?

There is currently no delete option via the user interface but an Accounting Preference can be removed by deleting the role of 'Internal Organisation' from the party record.

	TO CHECK: Need to investigate the impact of using an accounting preference then removing it.
What happens to the transactions in process etc…​…​???
Help for Chart of Accounts

OFBiz comes with a master template for a very comprehensive chart of accounts. This can be found in 'Global GL Defaults' under the 'Accounting' tab.

A couple of points to note

you do not need to use all the accounts defined in this master template (but it may be simpler to look for the accounts that you can use or rename)

you can create your own additional accounts if you dont want to use the ones in the master template

The chart of accounts for the default organisation (Company) is built up by selecting the accounts that you want to use from the global chart of accounts master template.

This means that if you want to create a new account then you need to create it first in the Global Chart of Accounts and then link (or assign) it to the chart of accounts for Company.

Details of the Chart of Accounts can be exported as a CSV file or PDF using the buttons displayed.

	You need to be careful if you do decide to create your own accounts that they contain all the details required and that they are linked into the relevant configuation for the setup of the GL defaults.
This means that if you change an account (eg Inventory) to one of your own, you need to check the GL defaults setup and replace any reference to the Inventory account to the one you have created.

This Chart of Accounts screen is used to define the list of accounts (or chart) that will be actively used by the company. For example the Global chart of accounts may contain 100 different accounts but only 20 need to be used for your specific business. This means you need only to create assignments to the accounts that you actively want to use.

The Chart of Accounts is a mixture of business needs (ie being able to track the information you need for your business) and tax requirements (i.e. legal or government requirements necessary for operating a business). The type of Chart that you setup will be dependent of your business type.

How do I create a Chart of Accounts?

As mentioned above the chart of accounts for the default organisation (Company) is built up by selecting the accounts that you want to use from the global chart of accounts master template.
This means that if you want to create a new account then you need to create it first in the Global Chart of Accounts and then link (or assign) it to the chart of accounts for Company.

By creating an assignment to an account it is then added to the Chart of Accounts.

Select the account Gl Account Id that you need from the drop down box

Press the 'Create Assignment' button

The account is added to the Chart of Account

How do I update a Chart of Accounts?

Updating the Chart of Accounts will involve either creating a new assignment or removing an existing one.
A new assignment is created using the instructions above.

The added complication may be that the account that you need does not exist in the Global Chart of Accounts. As mentioned above it will need to be created and then linked.

See the instructions below to remove an existing account assignment.

	If a completely new account is required that does not already exist as part of the Global Chart of Accounts template then it will need to be created as part of the Global template first before it can be used as an assignment in the Organisation Chart of Accounts.
How do I delete a Chart of Accounts?

Accounts are not deleted from the Chart of Accounts - they are simply no longer selected to be used.

It is important that you do not remove accounts that are active and have already been used for transactions. Even if the net balance of the account is zero then from an audit perspective then you should not be removing accounts.

You should only be looking to remove accounts that have not been used. To un-link or un-assign accounts from the default company then use the Entity Data Maintenance from the Webtools menu. Look for the entity 'GlAccountOrganization' and delete the record to remove the link.

How do I update the details for an account in the Chart ofAccounts?

Details of the accounts that make up the Chart of Accounts can be accessed from this screen.

Click on the 'GL Account Id' of the account required

The 'Edit GL Account' screen is displayed showing the details of the account selected
(NOTE:This screen is also accessible via 'Global GL Settings / Chart of Account / Navigate Accounts '

Amend the fields required
(NOTE: The GL Account Id and Posted Balance fields cannot be amended)

Press the 'Update' button

Help for Journals

A journal is a detailed accounting transaction that is recorded (or posted) to the General Ledger. It is made up of a debit and a credit component.

	TO CHECK: Is this screen really about Journals or is it about Suspense Accounts…​..??????)
	By default in OFBIZ a journal called 'ERROR_JOURNAL' is created as part of the demo data installation.
This 'ERROR_JOURNAL' is referenced in the Accounting Preferences setup for 'Company'.
The 'ERROR_JOURNAL' is used to store details of any transaction that fails and cannot be posted to a general ledger account.
Transactions falling into error can be as the result of incomplete setup or an invalid transaction (eg a transaction that should never occur).
How do I create a journal?

Enter a journal name in the Gl Journal Name field (eg MY_JOURNAL)

Press the 'Submit' button

The journal is created and will appear in the journal list at the bottom of the screen
(Note that the Journal ID is automatically generated)

How do I update a journal?

Select the journal to be updated from the list of journals at the bottom of the screen

The journal details will be displayed on the screen

Update the Gl Journal Name (as this is currently the only field that can be updated)

Press the 'Submit' button

The updated journal will appear in the journal list at the bottom of the screen

How do I delete a journal?

Be careful if you need to remove an existing journal as it may have transactions associated with it.

Press the 'Remove' button next to the journal that you want to delete

The journal is deleted and the screen is redisplayed

Help for GL Account Type Defaults

The GL Account Defaults screens are are method to setup rules that are used to translate business transactions into accounting transactions. It currently is made up of 12 sub menus that can be used to map various transaction type codes to a specific general ledger account

Accounting transactions are made up of a Debit Entry and a Credit Entry. The GL Account defaults screens help map which accounts are to be used to generate a each part of the transaction. This means that certain mappings will be used to generate the Debit (or DR) entry part of the transaction and others used to generate the Credit (or CR) entry part of the transaction.

	Many of the accounting transactions are generated 'automatically' (or in the background) using the the accounting services SECAS / EECAS.

The GL Account Type is used to specify the default account that certain transactions (eg Accounts Payable, Accounts Receivable, etc) are posted to.

An accounting transaction (or journal entry) is made up of two parts - a Debit Entry and a Credit Entry that balance each other. The GL Account Type is used to translate one side of the journal entry.

GL Account Types are stored in Entity GLAccountType which can be viewed via Entity Data Maintenance in the Webtools menu. There are currently 57 different GL Account Types that are part of the OFBiz demo data but only 19 of these are setup as mappings

How the GL Account Type is used is best shown by an example.

A very simple description of an online Sales Order Process could be as follows:

Customer Orders a Product (and Creates a Sales Order)

Customer Pays for Product (via Credit Card, Internet Banking etc)

Vendor confirms Payment and Dispatches the Product to the Customer

Let’s focus on the first part step of 3 in more detail.

The vendor has checked their bank statement and seen that the customer has paid

In OFBiz Order Manager they will then look up the relevant Sales Order and then click the 'Receive Payment' button to log the payment in the system

The 'Receive Payment' button is a trigger for an 'automatic' accounting transaction

The transaction type that is triggered is called 'Incoming Payment'

The accounting entries generated are: DR 112000 Undeposited Funds , CR 120000 Accounts Receivable

The CR (or Credit) entry for the transaction is created by the GL Acccount Type mapping for 'Accounts Receivable' (which by using the demo data default will go the 120000 Accounts Receivable)

The DR (or Debit) entry for the transaction is created by a different GL Account default, the Payment Method Id / GL Account Id mapping (eg Cash is setup as 112000 Undeposited Receipts)

How do I create a new GL Account Type default mapping?

There are currently 57 different GL Account Types that come as part of the demo data with OFBiz. This should be enough to manage the vast majority of business transactions.

These instructions show how to add a mapping using the default data

Select the 'GL Account Type Id' from the drop down list

Select the 'GL Account' to map it to from the drop down list

Press the 'Save' button

The new GL Account Type mapping is displayed in the list at the bottom of the screen

	If none of the demo data GL Account Types are sufficient then new ones can be added using Entity Data Maintenance and the entity 'GLAccountType' in the Webtools menu.
How do I update a GL Account Type default mapping?

A GL Account Type mapping cannot be updated directly but needs to be removed then re-created. If you try to update an existing entry you will get an 'duplicate key' error message.

Press the 'Remove' button next to the entry that you want to update

The entry is removed from the list of entries displayed

Select the 'GL Account Type Id' from the drop down list

Select the updated 'GL Account' to map it to from the drop down list

Press the 'Save' button

The new GL Account mapping is displayed in the list at the bottom of the screen

How do I delete a GL Account Type default mapping?

Press the 'Remove' button next to the entry that you want to delete

The entry is removed from the list of entries displayed

Help for Product GL Account

The Product GL Account is used to specify the default account to be used for a specific Product' and 'Account Type' combination. This setup will translate to one side of the journal entry only.

	Duplicate functionality …​. This setup for the Product GL Account can also be setup using the 'Accounts' sub menu for the Product in Catalog Manager.
TO CHECK: Need to confirm whether this default work like a hierarchy…​.eg Product GL Defaults will override General Account defaults.

It is used for tracking product transactions at a more detailed level.

Examples could be as follows:

Tracking Accounts Receivable by Product in the General Ledger

Tracking Cost of Goods by product (or product variation) in the General Ledger

Tracking Commissions paid by Product in the General Ledger

How do I add a new Product / GL Account Type mapping?

By default there are no Product / GL Account Type mappings that are configured as part of the OFBiz demo data.

Select the 'Account Type' from the drop down list
(NOTE: In other screens this field is call the 'GL Account Type Id'…​..)

Select the ' GL Account' to map it to from the drop down list

Enter or look up the 'Product Id' to be used

Press the 'Add' button

The new mapping will be displayed in the list at the bottom of the screen

	This mapping can also be also be done via the 'Accounts' sub menu for the Product.
Any mapping created here will be displayed under the Product 'Accounts' sub menu. Alternatively any mapping created in the Product 'Accounts' sub menu will also be displayed here.
How do I update a Product / GL Account Type mapping?

A Product / GL Account Type mapping can be updated by modifying the GL Account only. If the product needs to be updated then the mapping will need to be deleted and then re-entered using the new product.

Locate the entry that needs to be updated in the list of Product / GL Account Type mappings

Modify the 'GL Account 'by using the drop down list next to the 'GL Account' field

Press the 'Update' button

The updated mapping will be displayed

How do I delete a Product / GL Account Type mapping?

Locate the entry that needs to be deleted in the list of Product / GL Account Type mappings

Press the 'Remove' button next to the entry

	This can also be done via the 'Accounts' sub menu for the Product using the 'Delete Link' button.
Help for Product Category GL Accounts

The Product Category GL Account is used to specify the default account to be used for a specific 'Product Category' and 'Account Type' combination. This setup will translate to one side of the journal entry only.

It is used for tracking product category transactions at a more detailed level.

Examples could be as follows:

Tracking Accounts Receivable by Product Category in the General Ledger

Tracking Cost of Goods by Product Category in the General Ledger

Tracking Commissions paid by Product Category in the General Ledger

The demo data gives an idea of the use of product categories to classify or separate different products streams. If specific accounting or management reporting is required at this level then the General Ledger can be setup to provide this detail.

How do I add a new Product Category / GL Account Type mapping?

By default there are no Product Category / GL Account Type mappings that are configured as part of the OFBiz demo data.

Select the 'Account Type' from the drop down list
(NOTE: In other screens this field is call the 'GL Account Type Id'…​..)

Select the ' GL Account' to map it to from the drop down list

Enter or look up the 'Product Category Id' to be used

Press the 'Add' button

The new mapping will be displayed in the list at the bottom of the screen

How do I update a Product Category / GL Account type mapping?

A Product Category / GL Account Type mapping can be updated by modifying the GL Account only. If the product category or the Account Type needs to be updated then the mapping will need to be deleted and then re-entered using the new product category or Account Type.

Locate the entry that needs to be updated in the list of Product Category / GL Account Type mappings

Modify the 'GL Account 'by using the drop down list next to the 'GL Account' field

Press the 'Update' button

The updated mapping will be displayed

How do I remove a Product Category / GL Account Type mapping?

Locate the entry that needs to be deleted in the list of Product Category / GL Account Type mappings

Press the 'Remove' button next to the entry

Help for Financial Account GL Account Type

The FinAccount Type GL Account (Financial Account Type / GL Account Type) is used to specify the default account to be used for a specific type of Financial Account.
This setup will translate to one side of the journal entry only.

	There is a limitation that only one account can be specified per Financial Account type.
Currently there are 6 types of Financial Account
(Bank, Deposit, Investment, Gift Certificate, Replenish, Service Credit)
so if you have more than one of these type of accounts that you need to track separately then there could be a problem.

This mapping is normally be triggered if something is paid or uses a Financial Account. Using the demo data this mapping is triggered when someone purchases a gift certificate, or pays money into a financial account.

How do I add a new Financial Account Type / GL Account mapping?

By default there are 4 Financial Account Type / GL Type mappings that are configured as part of the OFBiz demo data.

Select the 'FinAccount Type Id' from the drop down list

Select the ' GL Account' to map it to from the drop down list

Press the 'Add' button

The new mapping will be displayed in the list at the bottom of the screen

How do I update a Financial Account Type / GL Account mapping?

A Financial Account Type / GL Account Type mapping can be updated by modifying the GL Account only.
Unlike other screens in this area if the GL Account Type needs to be updated then it can be done by creating a new record with the correct GL Account type which will overwrite the existing record.

Locate the entry that needs to be updated in the list of Financial Account Type / GL Account Type mappings

Modify the 'GL Account 'by using the drop down list next to the GL Account field

Press the 'Update' button

The updated mapping will be displayed

How do I remove a Financial Account Type / GL Account mapping?

Locate the entry that needs to be deleted in the list of Financial Account Type / GL Account Type mappings

Press the 'Remove' button next to the entry

Help for Sales Invoice default account

The Sales Invoice sub menu is used to specify the default account to be used for the individual line items that appear on a Sales Invoice.

The items are identified by a line description which can be mapped to a specific general ledger account.

Sales invoices can be made up of a variety of items as well as the product that is being sold (eg discounts, promotions, work effort or labour costs etc). The majority of businesses will want to track these type of items separately in the general ledger and this screen will allow this type of setup.

This setup will translate to one side of the journal entry only.

A key mapping used is linked directly to the Product Type (eg Invoice Digital Good Item, Invoice Finished Good Item, Invoice Finished/Digital Good Item…​.). This controls where the sales revenue received from the sale of the product is stored in the general ledger

Only a limited number of general ledger accounts that are available to be mapped. Currently this is 7 and limited to the accounts that have been assigned to the organisation from the Global Chart of Accounts that have a 'GL Account Class Id' = 'Revenue'
(NOTE: You will see that Discounts on Sales is not available to be selected because it’s GL Account Class Id = 'Cost of Goods Sold Expense'. It appears as a default because it is setup in the Global GL settings that doesnt seem to have any limitations of the account.)

	This screen is one of the screens where the default entries that are displayed here are entered via the Global GL Settings under the sub menu 'Invoice Item Type'.
This screen allows users to override the global settings for the Sales Invoice item type.
An example of why this could be necessary could be that a company many want to isolate the sales reporting of a specific department or business unit separately (eg subledgers etc) but still have the option of a 'catch all' global general ledger account.

If an override account is added it will appear in the Override GL Account column on the screen.

The only mapping that seems a bit out of place here is Sales Tax. It is blank because Sales Tax is setup using Tax Authorities so dont know why you would want to override the Sales Tax account to a Sales Revenue Account.

	Also need to highlight that in the Global Settings it uses the ENUM description to select the item and there are duplicate descriptions between the Sales Invoice and the Purchase Invoice.
Not too much of a problem here but it does cause problems in Agreements when setting up things like Commissions based on line items as you cant tell the difference between the description of a Sales Invoice item called 'Invoice Adjustment' and a Purchase Invoice item called 'Invoice Adjustment' …​.. except by trial and error

How the Sales Invoice mappings are used is best shown by an example.

A very simple description of an online Sales Order Process could be as follows:

Customer Orders a Product (and Creates a Sales Order)

Customer Pays for Product (via Credit Card, Internet Banking etc)

Vendor confirms Payment and Dispatches the Product to the Customer

Let’s focus on the second part step of 3 in more detail.

The vendor has verified that the customer payment has been received

In OFBiz Order Manager they will then look up the relevant Sales Order and then click the 'Quick Ship Entire Order' button to log the dispatch of the order in the system

The 'Quick Ship Entire Order' button is a trigger for an 'automatic' accounting transaction

The transaction type that is triggered is called 'Sales Invoice'

Transaction Type: Sales Invoice DR 120000 Accounts Receivable, DR 410000 Discounts on Sales, DR 400000 Sales, CR 22????? Sales Tax Collected

DR Sales is used for item promotions where product cost is simply reversed.
Only order promotions are coded to Discounts.
The Sales Tax account will be dependent on your sales tax setup.
The demo data posts to tax accounts by US state.

One of the CR (or Credit) entries for the Sales Invoice transaction is created using the Sales mapping defined here in the Sales Invoice (and the other is created another GL Account default for 'Tax Authority GL Accounts')

All of the the DR (or Debit) entries for the Sales Invoice transaction (except for Accounts Receivable which is comes from the GL Account Type defaults) are created using the mappings defined here in the Sales Invoice

How do I add a Sales Invoice override mapping?

By default there are no Sales Invoice override mappings that are configured as part of the OFBiz demo data.

Select the 'Invoice Item Type' from the drop down list

Select the ' Override Revenue GL Account Id' to map it to from the drop down list

Press the 'Save' button

The new mapping will be displayed in the 'Override GL Account' column in the list at the bottom of the screen

How do I update a Sales Invoice override mapping?

An existing Sales Invoice override mapping cannot be updated but needs to be removed and a new mapping added. If you try to add an override to an item that already has an override you will get a duplicate record error message.

How do I remove a Sales Invoice override mapping?
	Only the override mapping can be deleted. The default mapping record cannot be deleted here (even though the Remove button is displayed next to it!)

Locate the entry that needs the override deleted in the list of Sales Invoice override mappings

Press the 'Remove' button next to the entry

he override mapping will be removed from the 'Override GL Account' column of the entry

Help for Purchase Invoice default account

The Purchase Invoice sub menu is used to specify the default account to be used for the individual line items that appear on a Purchase Invoice.

The items are identified by a line description which can be mapped to a specific general ledger account.

Purchase invoices can be made up of a variety of items as well as the product that is being bought (eg discounts, promotions, work effort or labour costs etc). The majority of businesses will want to track these type of items separately in the general ledger and this screen will allow this type of setup.

This setup will translate to one side of the journal entry only.

	This screen is one of the screens where the default entries that are displayed here are entered via the Global GL Settings under the sub menu 'Invoice Item Type'. This screen allows users to override the global settings for the Purchase Invoice item type.
An example of why this could be necessary could be that a company many want to isolate the sales reporting of a specific department or business unit separately (eg subledgers etc) but still have the option of a 'catch all' global general ledger account.
	TO CHECK: Need to do more investigation but the it looks like these Purchase Invoice mappings dont work when used as part of the Purchase Order to Purchase Invoice Process. (Have been doing some tests to try and get it to post to a different account than 'Uninvoiced Shipment Receipts' and 'Inventory' but hasnt worked so far.) We need to be able to specify things such as Sales Tax, Freight and any Purchase Order adjustments.

These override mappings do work if there is no Purchase Order just a Purchase Invoice as shown in the simple process below.

How the Purchase Invoice mappings are used is best shown by an example.

A very simple description of a Purchase Invoice Process could be as follows:

You have ordered something from a supplier (eg indirect purchasing such as stationery etc via phone)

The Supplier ships the products to you
(NOTE: as they are not stored in the Warehouse but in your offices - so dont need an Inventory Receive…​..????)

You receive the product and an invoice from the Supplier (Purchase Invoice)

You enter the Purchase Invoice pay the Supplier the amount invoiced

Let’s focus on step of 4 in more detail.

You have received the product from the supplier with an invoice

In OFBiz you enter the Purchase Invoice using 'Create New' in the 'Invoices' menu of Accounting Manager

Using the 'Items' sub menu you can create individual items on the Purchase Invoice (eg Paper, Pens, Sales Tax etc and they dont need to have a Product Id associated with them)

When you add a new invoice item to the Purchase Invoice it is the 'Invoice Item Type' that is affected by the Purchase Invoice override mappings

The Purchase Invoice can then be moved to various statuses (Approved, Received, Ready or Cancelled)

When the status is moved to 'Ready' this is a trigger for an 'automatic' accounting transaction

The transaction type generated is called 'Purchase Invoice' and it uses the Purchase Invoice override mappings

Transaction Type: Purchase Invoice, DR 516100 Purchase Order Adjustments , DR ????? Sales Tax, CR 210000 Accounts Payable

How do I add a new Purchase Invoice override mapping?

By default there are no Purchase Invoice override mappings that are configured as part of the OFBiz demo data.

Select the 'Invoice Purchase Item Type' from the drop down list

Select the ' Invoice Override Expense GL Account Id' to map it to from the drop down list

Press the 'Save' button

The new mapping will be displayed in the 'Invoice Override Expense GL Account' column in the list at the bottom of the screen

How do I update a Purchase Invoice override mapping?

An existing Purchase Invoice override mapping cannot be updated but needs to be removed and a new mapping added. If you try to add an override to an item that already has an override you will get a duplicate record error message.

How do I remove a Purchase Invoice override mapping?
	Only the override mapping can be deleted. The default mapping record cannot be deleted here (even though the Remove button is displayed next to it!)

Locate the entry that needs the override deleted in the list of Purchase Invoice override mappings

Press the 'Remove' button next to the entry

The override mapping will be removed from the 'Invoice Override Expense GL Account' column of the entry

Help for Payment Type GL Account Type

The Payment Type GL Account Type Id is used to translate (or map) the different payment types to a specific GL Account Type Id. The GL Account Type Id is then used via the 'GL Account Type Id' defaults to translate to one side of a journal entry.

	This GL Account default is used to link to another one of the GL Account defaults.

A Payment Type is just a way to categorize transactions.

Examples of Payment Types could be as follows:

Commission Payments

Customer Payments

Vendor (or Supplier) Payments

Customer Refunds

Customer Prepayments or Deposits

These payment types can then be mapped to the required account type in the Chart of Account.

Examples of these type of mappings could be as follows:

Customer Payments are mapped to Account Receivable

Vendor (or Supplier) Payment are mapped to Account Payable

Customer Refunds are mapped to Customer Credits

How do I add a Payment Type / GL Account Type Id mapping?

There are currently 14 different Payment Type / GL Account Types mappings that come as part of the demo data with OFBiz and should cover a good variety of payment related transactions.

Select the 'Payment Type Id' from the drop down list

Select the 'GL Account Type Id' to map it to from the drop down list

Press the 'Save' button

The new 'Payment Type / GL Account Type' mapping is displayed in the list at the bottom of the screen

How do I update a Payment Type / GL Account Type Id mapping?

A Payment Type / GL Account Type mapping cannot be updated directly but needs to be removed then re-created. If you try to update an existing entry you will get an 'duplicate key' error message.

Press the 'Remove' button next to the entry that you want to update

The entry is removed from the list of entries displayed

Select the 'Payment Type Id' from the drop down list

Select the updated 'GL Account Type Id' to map it to from the drop down list

Press the 'Save' button

The new 'Payment Type / GL Account Type' mapping is displayed in the list at the bottom of the screen

How do I remove a Payment Type / GL Account Type Id mapping?

Press the 'Remove' button next to the entry that you want to delete

The entry is removed from the list of entries displayed

Help for Payment Method GL Account Type

The Payment Method GL Account Type Id is used to map the different payment methods (eg Cash, Cheque etc) to a specific GL Account Type Id. This will translate to one side of a GL entry only.

A Payment Method is just a way to define the ways in which payments can be made.
Each payment method can be linked to a different account in the general ledger.
A main GL account used would be the one that represents the Company bank account.
In the demo data mappings Electronic Funds Transfer, Company Account, Financial Account are all linked to the Company bank account GL account.

OFBiz demo data defines 15 different payment methods as follows:

Cash

Certified Cheque

Company Account

Company Cheque

Electronic Funds Transfer
(NOTE TO CHECK: Problem with definition or terminology - is this a Direct Debit…​. ?? A direct debit is controlled by the payee and an automatic payment via bank account is controlled by the payer)

Billing Account

Cash on Delivery (COD)

eBay

Offline Payment
(NOTE: Is this ambiguous - since COD is an offline payment…​)

PayPal

WorldPay

Financial Account

Gift Certificate

Money Order

Personal Cheque

	A point to note is that these payment methods dont include Credit Cards…​.(which I think is on purpose…​). The majority of these payment methods are linked to 'Undeposited Receipts' but an additional accounting transaction may be needed once the funds have cleared and are available in the Company bank account.
How do I add a new Payment Method Id / GL Account Id mapping?

Select the 'Payment Method Type' from the drop down list

Select the 'GL Account Id' to map it to from the drop down list

Press the 'Save' button

The new Payment Method Type / GL Account Type mapping is displayed in the list at the bottom of the screen

How do I update a Payment Method Id / GL Account Id mapping?

A Payment Method Type / GL Account Type mapping cannot be updated directly but needs to be removed then re-created. If you try to update an existing entry you will get an 'duplicate key' error message

Press the 'Remove' button next to the entry that you want to update

The entry is removed from the list of entries displayed

Select the 'Payment Method Type' from the drop down list

Select the updated 'GL Account Type' to map it to from the drop down list

Press the 'Save' button

The new Payment Method Type / GL Account Type mapping is displayed in the list at the bottom of the screen

How do I remove a Payment Method Id / Gl Account Id mapping?

Press the 'Remove' button next to the entry that you want to delete

The entry is removed from the list of entries displayed

Help for Variance Reason GL Accounts

The Variance Reason / GL Account default is used for mapping any stock differences to a particular general ledger account. If there are variances in the number of products that are in stock then this affects the value of inventory in the general ledger. By using this GL default you can offset any differences in stock to the relevant general ledger account.

The number of products (or items) in stock can vary.
These differences can be caused by numerous reasons.
Some of these could be as follows:

Products have been damaged

Products were lost or stolen

Products were found

Under or over supply of a Product from a Supplier (eg. You have ordered 10 and 11 are delivered…​.)

Free samples or giveaways to potential clients

	These mappings are used in Catalog Manager when a manual inventory adjustment is done through the Inventory Item screens.
How do I add a new Variance Reason / GL Account mapping?

There are 6 mappings that come as part of the OFBiz demo data.

Select the 'Variance Reason Id' from the drop down list

Select the 'GL Account Type Id' to map it to from the drop down list

Press the 'Add' button

The new 'Variance Reason / GL Account Type' mapping is displayed in the list at the bottom of the screen

How do I update a Variance Reason / GL Account mapping?

Select the 'Variance Reason Id' from the drop down list

Select the updated 'GL Account Type Id' to map it to from the drop down list

Press the 'Add' button

The updated 'Variance Reason / GL Account Type' mapping is displayed in the list at the bottom of the screen

How do I remove a Variance Reason / GL Account mapping?

Press the 'Remove' button next to the entry that you want to delete

The entry is removed from the list of entries displayed

Help for Credit Card Type GL Accounts

The Credit Card Type / GL Account default is used to map different types of credit card to different general ledger accounts.

	This setup will affect one side of a journal entry only.

This type of mapping is useful if you need to track the amounts to be collected from different credit card agents.

The OFBiz demo data comes with some setup here

	TO CHECK The demo entries appear to be duplicated…​has something changed in ENUM for defining each credit card type…​..?????)

Examples are as follows:

American Express

Visa

Mastercard

Diners Club

How do I add a Credit Card Type GL Account mapping?

There are 10 mappings that come as part of the OFBiz demo data but they do appear to be duplicated for some reason.

Select the 'Card Type' from the drop down list

Select the 'GL Account Id' to map it to from the drop down list

Press the 'Add' button

The new 'Credit Card / GL Account Id' mapping is displayed in the list at the bottom of the screen

How do I update a Credit Card Type GL Account mapping?

Select the 'Card Type' from the drop down list

Select the updated 'GL Account Id' to map it to from the drop down list

Press the 'Add' button

The updated 'Credit Card Type / GL Account' mapping is displayed in the list at the bottom of the screen

	TO CHECK Used 'Visa' as an example to update and the 'CCT_VISA' was updated but the 'Visa' one was’nt. This is probably related to the duplication.
How do I remove a Credit Card Type GL Account mapping?

Press the 'Remove' button next to the entry that you want to delete

The entry is removed from the list of entries displayed

Help for Tax Authority GL Accounts

The Tax Authority / GL Account default is used to map different tax authorities to different general ledger accounts. This setup will affect one side of a journal entry only.

	A tax authority is legal body usually the state (country) that imposes a financial levy on business transactions.

Normal business rules require you will to keep track amounts collected or paid to different tax authorities separately. This mapping ensures that money collected or paid to various tax authorities (eg through Sales Orders, Purchase Orders etc) can be separated into specific accounts

The OFBiz demo data comes with 9 entries to show an example of how this can be setup using the some of the US states as separate tax authorities.

How do I add a Tax Authority / GL Account mapping?

Unlike the other GL Account defaults you cannot add a Tax Authority / GL mapping through these screens. It needs to be done via the 'GL Accounts' sub menu under the 'Tax Authorities' menu.

The method of how to add a mapping using the 'Tax Authorities' is shown below.

From the Accounting Manager / Tax Authorities Menu press the 'Edit' button next to the Tax Authority required

Select the sub menu 'GL Accounts'

Enter or Lookup the party for the 'Organisation Party Id' field (NOTE: Use 'Company' as default)

Enter or Lookup the GL Account to be mapped to

Press the 'Add' button

The mapping will be displayed at the bottom of the screen.

Return to the Tax Authority / GL Account default and this new mapping will be shown in the list

How do I update a Tax Authority / GL Account mapping?

Only the GL Account Id linked to the mapping can be updated.

Locate the Tax Authority / GL Account entry that needs to be updated

Select the new 'GL Account Id' from the drop down list next to the entry

Press the 'Update' button next to the entry

How do I remove a Tax Authority / GL Account mapping?

Locate the Tax Authority / GL Account entry that needs to be removed

Press the 'Delete' button next to the entry

Help for Party GL Account mapping

The Party / GL Account mapping allows the translation of different account types (eg Accounts Receivable, Accounts Payable etc) for a party to be mapped to a separate general ledger account.

The party role (eg Bill To Customer) is also used to define the mapping even further.

OFBiz demo data setup comes with no entries here.

It is used as a way of implementing subledger functionality in OFBiz. Subledger functionality is where a higher level account can be split into lower levels. In this case these lower levels can be by party.

An example could be that a business may want to use the general ledger to track the Accounts Receivable (AR) by customer so the chart of account would be setup something like as follows:

120000 Accounts Receivable

120010 Accounts Receivable - Customer A

120020 Accounts Receiviable - Customer B

120030 Accounts Receivalbe - Customer C

This has the main AR account is at the top of the hierarchy and 3 sub accounts below it.

Entries for Customers A, B and C would be setup with a role of 'Bill From Customer' as this is a role associated with the customer when the Sales Invoice is generated.When a transaction matching the criteria is processed in the system then these mappings will control where it is posted to.In the case of Customer A any AR transactions with role 'Bill To Customer' are posted to '120010' instead of the standard '120000

How do I add a new Party / GL Account mapping?

Enter or Lookup the party for the 'Party Id' field

Select the 'Role Type Id' from the drop down list
(NOTE: Be careful that you select the correct role for the transactions you want to track…​…​)

Select the 'GL Account Type Id' from the drop down list

Select the 'GL Account Id' from the drop down list

Press the 'Add' button

The new entry will be displayed at the bottom of the screen

How do I update a Party / GL Account mapping?

Only the GL Account Id linked to the mapping can be updated.

Locate the Party / GL Account entry that needs to be updated

Select the new 'GL Account Id' from the drop down list next to the entry

Press the 'Update' button next to the entry

How do I remove a Party / GL Account mapping?

Locate the Party / GL Account entry that needs to be removed

Press the 'Delete' button next to the entry

Help for Time Periods

Time periods are a defined period of time (usually a month, quarter or year) that is used to group business transactions. It is a key part of any general accounting setup.

Time periods can be used for the definition of :

Company Financial Year

Fiscal / Tax Periods (weeks, months, quarters)

VAT / GST Periods

Sales Periods

The screen is divided into 3 main areas. The first two show lists of the open and closed time periods. The area at the bottom allows you to define and enter a new time period.

How do I add a new Financial Year time period?

Using the area at the bottom of the screen labelled 'New'

Leave the Parent Period Id field blank
(NOTE: The financial year will be the parent of other time periods eg fiscal months or GST / VAT periods)

Select 'Fiscal Year' from the 'Period Type Id' drop down box

Enter '13' in the Period Num field
(NOTE: You can use any number that does not conflict with the other time periods you want to use. We plan to define 12 fiscal or tax months so will use 13 for the year)

Enter 'FY 2010-2011' in the Period Name field
(NOTE: You can use any name you want but make sure it makes sense. This example is an abbreviation for Fiscal Year 2010-2011)

Select '1st April 2010' using the calendar lookup in the 'From Date' field

Select '1st April 2011' using the calendar lookup in the 'Thru Date' field
(NOTE: Even though we want our financial year to end on 31st March 2011 the test used is based on less than not an equal to)

Leave the 'Is Closed' field at its default of 'No'

Press the 'Create' button

The new time period will now be displayed in the list of open time periods.

How do I add a new GST/ VAT time period?

Using the area at the bottom of the screen labelled 'New'

Select the previously created financial year 'FY 2010-2011' in the Parent Period Id field

Select 'Fiscal Month' from the 'Period Type Id' drop down box

Enter '1' in the Period Num field
(NOTE: This is the first of 12 periods that we want to define.)

Enter 'FM April 2010' in the Period Name field
(NOTE: You can use any name you want but make sure it makes sense. This example is an abbreviation for Fiscal Month April 2010)

Select '1st April 2010' using the calendar lookup in the 'From Date' field

Select '1st May 2010' using the calendar lookup in the 'Thru Date' field
(NOTE: Even though we want our fiscal month to end on 30th April 2010 the test is used is based on less than not an equal to)

Leave the Is Closed field at its default of 'No'

Press the 'Create' button

The new time period will now be displayed in the list of open time periods.

How do I update a time period?
	Time periods cannot be updated via the current time periods screen. If you need to amend time period details then it can be done via Entity Data Maintenance in the Webtools menu.
How do I close a time period?

To close a time period select the 'Close' button next to the time period.

The time period will be removed from the current open time periods area and re-displayed in the closed time periods section of the screen.

Closing a time period is a trigger for an automatic accounting transaction as follows:

Transaction Type: Period Closing

DR ?????? (based on the GL account type mapping for Profit Loss)

CR 336000 Retained Earnings (based on GL account type mapping for Retained Earnings)

	Both sides of this accounting transaction uses the same GL account type default mapping.
The account mapping for 'Profit Loss' is not setup as part of the demo data so this transaction will not automatically post to the general ledger but will instead be put in the ERROR_JOURNAL as an unposted transaction.
The transaction value is zero for both sides of journal…​Even if it does have a value do we want to move it from P&L to Equity during the financial year? Normally this is done once at the end of the financial year.
Accounting Glossary
Accounts Payable

These are the debts that your business owes to suppliers, usually in relation to goods or services, inventory, or supplies. It is also called 'A/P' for short or 'Creditors'.

Accounts Payable Invoice

AP invoice is a document raised by the customer and sent to the company with the details of the items sent, qty sent, price and other details. The company will enter this invoice details in the Payable module and then pay the customer according to the credit terms. This invoice may come along with the consignment or may be sent to the company separately.

Accounts Receivable

These are the outstanding debts that your customers owe to your business, for products and services delivered. It is also called 'A/R' for short or Debtors.

Accounts Receivable Invoice

AR Invoice is a document raised by the company and sent to the customer with the details of items sold, qty sold, price, tax and other details. Based on this invoice, the customer will send the payment in case of credit sales.

Account Type

A key that specifies the accounting area to which an account belongs. The account type is required in addition to the account number to identify an account, because the same account number can be used for each account type.

Accrual Based Accounting

This is a method where you record the income when the sale occurs and not necessarily when you receive the payment. Also you record an expense when you receive goods or services, even though you may not pay for them until later.

Acquisition

The process of identifying the requirement for a certain good or material item, ordering it, and paying for it.

Accrual Based Accounting

This is a method where you record the income when the sale occurs and not necessarily when you receive the payment. Also you record an expense when you receive goods or services, even though you may not pay for them until later.

Annual Revenue

Annual revenue is the amount of revenue for a group that is reported in the Party Group Information screenlet of the groups profile (visit Party Profile screen).

Assets

These are all of the non-inventory "things" that the enterprise owns.
These are items of value owned by the business.
There are different types of assets (fixed, current, intangible) In accounting assets are shown as balance sheet accounts.

	Examples: Furniture, computer or manufacturing equipment, vehicles, bank accounts, investments and goodwill.
Asset Maintenance

Any expense incurred during the process of maintaining an asset.
There is a application in OFBiz plugin to manage maintenance process of assets

	Example: Real Estate assessor fees, stock broker fees, vehicle maintenance costs
Balance Sheet

This is like a financial snapshot of your business at a certain point in time.
It lists your assets, liabilities and the difference between the two which is the net worth (or equity) of the business.
The balance sheet is also called the 'Statement of Financial Position'

Budget

A budget is used to track spending in the company for a future period of time. The company may have one or more budgets depending on the requirements (i.e. Operating Budget, Capital Budget).
A budget has a status, type and is composed of budget line items.

Budget Id

The unique identifier for a budget.

Budget Item

Describes an item in a budget. It may have a type, amount and purpose.

Capital

This is money invested in the business by the owners. It is also called equity.

Cash Based Accounting

This method is when you record income only when you receive the cash from your customers. You also only record an expense when you actually pay your suppliers

Chart of Account

This is a list or hierarchy of account descriptions that you use to keep the accounting records for your business

Closing balance

At the end of a financial period, the balance on all entries posted to an account.

Cost of Goods Sold

This is the amount it costs you to provide your product or services sold to your customers. It is often called and abbreviated to 'COGS'

Credits

One component of every accounting transaction (journal entry) is a credit. Credits increase liabilities and equity but decrease assets

Credit account

An account that allows buyers to obtain goods or services without paying for them until a later date.

Credit amount

An amount of money in someone’s favor.

Creditor

This is a company or an individual that you owe money to.

Current Assets

Normally these are things that the business owns that are in the form of cash or will generally be converted to cash or used up within a year.

	Examples: Accounts Receivable (because people owe you money that you expect will pay you); Inventory and money in your company bank account.
Current Liabilities

Normally these are debts that the business owes that are generally payable within a year, (i.e. Accounts Payable; Taxes and Payroll)

Debits

One component of every accounting transaction (journal entry) is a debit. Debits increase assets but decrease liabilities and equity.

Debtor

This is a company or an individual that owes you money.

Depreciation

This is a write-off of a portion of the cost of fixed assets, such as vehicles and equipment. It is usually done annually but can be done more frequently. Depreciation is also listed as part of the expenses on the 'Profit & Loss' or 'Income Statement'.

Double Entry Accounting

In this method every transaction has two entries: a debit and a credit (also called a journal entry). Debits must always equal credits. Most if not all accounting software use double entry accounting.

Equity

This is the net worth of your business. It is also called 'Capital' or 'Owner’s Equity. Equity is made up of investment in the business by the owners plus any profits that the business has made that has’nt been taken out.

End of Year Rollover

At the end of the financial year the Profit & Loss accounts totals are reset to zero and the balance sheet accounts totals are carried forward into the next financial year.

Fixed Assets

These are assets that are generally not going to be converted to cash within a year. (i.e. Manufacturing equipment; vehicles, building, …​)

General Ledger

This is a collection of different types of accounts (balance sheet, income, expense) that are used to keep the accounting records of a business. A general ledger works with double entry accounting and journal entries for each transaction.

Gross price

The price of one unit of an item, or a service, including tax.

Gross Profit

The positive difference between sales revenues and the costs of goods sold.

Income Accounts

These are the accounts that are used to keep track of your sources of income. (i.e. Sales, Consulting Income or Interest).

Income Statement

This is also called a Profit and Loss Statement' or a 'P&L'.
It lists the income, expenses, and net profit (or loss) for the business. The net profit (or loss) is equal to the total income minus the total expenses.

Intangible Asset

This is something of value that is owned by the business that cannot be touched physically. (i.e. a trademark; patent or goodwill)

Inventory Audit Report

An audit trail for the posted inventory transactions in the Chart of Accounts. This report compares the accounting view (inventory balance accounts) and the logistics view (inventory value displayed by the audit report).

Invoice Date

This is the date that the invoice was created.
Normally this will be based on when products were shipped or services were provided

Invoice Due Date

This is the last possible date that payments can be made or received for an invoice without triggering any late payment penalties

Journal

This is a detailed accounting transaction that is recorded (or posted) in the general ledger. It can also be referred to as a Journal Entry. It is made up of a debit and a credit component.

Journal Entry

This is a detailed accounting transaction that is recorded (or posted) in the general ledger. It can also be referred to as a Journal. It is made up of a debit and a credit component.

Liabilities

These are the debts that your business owes to its suppliers, banks or the government. (i.e. taxes or loans)

Long Term Liabilities

These are debts that a business owes to its suppliers that are not generally due to be paid off within a year (An example would be a mortgage payment).

Outstanding Amount

The amount of money that is owed by a debtor and has not yet been paid.

Outstanding Payment

The remaining amount of money that is due for goods or services.

Net Income

This is also called 'Profit' or 'Net Profit'. It is the total income minus the total expenses.

Passive Account

A bank account in which no transactions have taken place, neither deposits nor withdrawals, for a specified period of time (normally six months).

Payables

The total amount due to creditors. This information includes the type, the amount, and the due date of the debts. Payables may include amounts payable to banks and suppliers, as well as customer down payments.

Payment Method

A set of parameters and other details that determine how invoices are cleared when the Payment Wizard is used. It is possible to create as many payment methods as required. In addition, you can link specific payment methods to relevant business partners.

Payment Period

The period of time in which an outstanding debt has to be paid, for example a range of days or a certain month.

Payment Run

A process that clears A/R and A/P invoices, by generating the payments, posting the transactions and updating the system (by creating the bank transfer files).

Payment Terms

The conditions of payment agreed to between business partners with respect to goods supplied or services provided.

Profit and Loss Statement

A comparison of revenue and expense within a certain period. The purpose of the profit and loss statement is the establishing of profit made by an organization and the sources thereof. It is a compulsory part of year-end closing.

Retained Earning

These are profits from the business that have been kept or 'retained' in the business and not paid out to the owners.

Trial Balance

This is a list of the general ledger accounts showing the debits in one column and the credits in another.
The main objective of a trial balance is to ensure that the total credits and total debits balance (eg. total debits = total credits).
It also validates that the double entry accounting is working correctly.

9. Content Management

The Document Content Management System (DMS/CMS) is designed to store data once and then allow it to be reused in multiple arrangements.

9.1. Overview

The term 'content management' generally refers to a system for acquiring, storing and retrieving electronic data in varying formats - such as text, images or proprietary formats.

Content management systems (CMS) usually incorporate a rendering system to let the developer display the content in various formats.

While some CMSs are rigid in the manner in which content is entered and rendered, the content management module of OFBiz is more of a set of tools which can be used in a variety of situations.

In addition to HTML, the content can be rendered in non-Web modes, such as PDF or email newsletters.

The OFBiz CMS is designed to store data once and then allow it to be reused in multiple arrangements.

Hence, there are basically two aspects

the back-end storage subsystem, which is oriented around the DataResource entity,

and the front-end association subsystem, which revolves around the Content entity.

Note that the Content entity has a foreign key pointing to one and only one DataResource entity, but the same DataResource entity can be referenced by multiple Content entities.

It is a general rule that data can only be accessed via a Content entity, but one common exception is that images are typically served up using the DataResource primary key.

Content entities are related to other content via ContentAssoc entities. The ContentAssoc entity has a four part primary key and other fields that are used to relate content. The key specifies the 'to' Content and the 'from' Content, as well as the type of association and its effective date. See the discussion of the ContentAssoc entity for more information on how content is related.

9.2. Security

All services defined in the content component are safely secured. If you are in a safe environment, want to save more complex contents and get blocked by the security policy you might want to override the security only in the content component.

Typically when using content/control/WebSiteCms?webSiteId=CmsSite (ie "Edit[ing] WebSite CMS For: CMS Web Site [CmsSite]"), the service updateTextContent may prevent you to save contents with a message like

	The Following Errors Occurred: In field [textData] by our input policy, your input has not been accepted for security reason. Please check and modify accordingly, thanks.

To override the security you can change definitions of other content services by changing the security on field "textData" from "safe" to "any". That’s of course an example and you may find other similar cases.

You may also prefer to change the security policy at an upper level. See owasp.properties file.

9.3. Major CMS entities
9.3.1. DataResource

The DataResource entity acts as the gateway to actual content retrieval.
There are two important fields for determining the format and storage of a resource :

the 'mimeTypeId'

the 'dataResourceTypeId'.

mimeTypeId

The mime type is the standard Multipurpose Internet Mail Extension, of which, 'text/html' and 'image/gif' will be two of the more common examples.

The mimeTypeId indicates the format of the content as it is stored.

This must be compared to the desired output format to see if the rendering system can handle the request.

For example, if the DataResource.mimeTypeId equals, 'image/png', and the target output format is 'text/html', the rendering system could make the logical supposition that it should return an HTML "img…​/" tag. If the output format were 'application/pdf' then it will need to determine if it can convert the image to a PDF format.

dataResourceTypeId

The dataResourceTypeId field indicates the storage mechanism for the resource.
It could be of type ELECTRONIC_TEXT, which indicates that there is an entry in the ElectronicText table that is related to the DataResource by its primary key.

If the mimeTypeId is of type image, then the dataResourceId could be IMAGE_OBJECT (stored in the database ImageDataResource table), OFBIZ_FILE (stored in a file the path of which is relative to the OFBiz home directory) or URL_RESOURCE (could be accessed via HTTP protocol).

9.3.2. dataTemplateTypeId

One of the powerful concepts of the OFBiz CMS is that it can store templates that can be used to control the formatting of data.

In this case, the resource pointed to by the DataResource entity will not be rendered, itself; instead, it will be used as a template to format data that is associated with it.

The currently supported templating types are FreeMarker (FTL) and the OFBiz Screen Widget (SCREEN_COMBINED) format. If the value of dataTemplateTypeId is empty or equal to NONE, then the data pointed to by the dataResource entity is rendered directly.

9.3.3. objectInfo

If dataResourceTypeId is ELECTRONIC_TEXT or IMAGE_OBJECT, then objectInfo is not used, but for other types, it will contain the resource storage information.

If dataResourceTypeId is one of OFBIZ_FILE, CONTEXT_FILE, LOCAL_FILE or URL_RESOURCE; then objectInfo contains path info.

If dataResourceTypeId equals SHORT_TEXT, then objectInfo will contain the actual resource (short text) value.

ElectronicText

ElectronicText contains ASCII text data.
An ElectronicText entity can be associated with only one DataResource entity and vice-versa.
The mimeTypeId field of the DataResource entity must be checked to determine the format of the ElectronicText data.

ImageDataResource

ImageDataResource is the equivalent of ElectronicText for binary image data.
The DataResource.mimeTypeId must be checked to determine the format of the data.

9.4. Content

The Content entity determines how DataResources are rendered.

It does this on a 'local' level, in that it has a mimeTypeId, localeString and other fields that indicate to the rendering system how the DataResource should look, but it can also control the larger picture because it can act as a placeholder and head for other content.

The Content.dataResourceId does not need to point to anything, instead a Content entity can be related to other Content via ContentAssoc entities.

At some point, some of the child Content entities must point to DataResources, else nothing will ever be displayed.

9.4.1. dataResourceId

The dataResourceId points to a DataResource entity that represents content associated with the parent Content entity.

The related DataResource could be data that is rendered or it could be a template that indicates how child Content of the parent Content are rendered.

9.4.2. contentName

contentName is the field that is used to represent the Content entity in lists. The contentName field value must be less than 100 characters.

9.4.3. description

description is used in cases where a short summary or description of the Content is desired. The description field value must be less than 255 characters.

9.4.4. templateDateResourceId

The templateDataResourceId field points to a DataResource entity that is used to transform the data contained in the DataResource pointed to by the Content.dataResourceId field.

The dataTemplateTypeId of the DataResource pointed to by templateDataResourceId will be checked to determine what sort of transform will be applied.

9.5. ContentRole

The ContentRole entity is used to assign permission authority to a piece of content.

The ContentRole entity identifies the Content to which the authority is being attached and the Party that has that authority and what sort of authority (role) that party has.

The ContentRole also establishes the time frame (from/thruDate) for which that authority is valid.

9.6. ContentPurpose

The ContentPurpose entity adds extra information to a Content entity that is used to determine what permissions are required to access that Content.

9.7. ContentPurposeOperation

ContentPurposeOperation is used to setup permission validation rules.

9.8. ContentAssoc

ContentAssoc relates one Content entity to another.

A sense of direction is conveyed in the fact that one field is named contentIdTo (the from field is contentId).

9.8.1. contentId

This is the 'parent' Content in a Content-to-Content relationship.

9.8.2. contentIdTo

This field is the 'from' or 'child' field in a Content-to-Content relationship.

9.8.3. contentAssocTypeId

The contentAssocTypeId field is used to add information about the type of a Content-to-Content relationship. It is part of the primary key.

Two Content entities can be related by multiple ContentAssoc entities if the contentAssocTypeId field varies (or the fromDate is different).

9.8.4. fromDate

the fromDate field is part of the primary key.

10. Manufacturing

The OFBiz Manufacturing component is one of the core application components and has all of the functionality you need to manage the cycle of tasks involved in the making of products and ensuring that the material necessary for production is forecast to be available at the right time

It is well integrated with other components especially Catalog to manage product definition, whatever its stage of manufacture (raw material, supply, subassembly, service, …​) and Workeffort to manage all means of production.

10.1. About Manufacturing and MRP

OFBiz Manufacturing & MRP is a highly functional seamless application that contains everything you need to run an efficient and successful manufacturing business.

Key features include:

Bill of Materials

Manufacturing Routing and Tasks

Production Planning

Production Costing

Equipment Billing

Raw Materials Procurement

This guide gives you the basics you need to get up and running with OFBiz for Manufacturing & MRP.

It contains a quick overview of some common manufacturing concepts, a list of the setup required and an example for you to work through.

By the end of the document you should have the enough information to begin your own manufacturing setup in OFBiz.

10.1.1. What is Manufacturing?

Manufacturing is the “act of making something out of raw materials”. The 'something' that is manufactured is generally a product that can be on sold to customers.

Manufacturing is not only an industrial activity carried out in a factory, it can also be any range of tasks that result in an end product. So, even if you only assemble products you can still make use of OFBiz Manufacturing & MRP.

10.1.2. What is MRP?

MRP is a three-letter abbreviation that is always used in conjunction with manufacturing – so what exactly is it?

MRP stands for “Material Requirement Planning”. It’s a computer program that, when run regularly, helps a business to plan what to manufacture and when to manufacture it.

It also has the added benefit of letting you know when to buy raw materials to meet your manufacturing commitments.

The MRP tool comes with OFBiz ‘out of the box’.

10.2. JobShop, or ProductionRun

Jobshop is the generic term to manage Production Run

The JobShop is used to manage and track all the manufacturing or assembling work.
The work (or job) carried out in the JobShop is called a Production Run.

Production Runs can also be called Work Orders.

Production Runs are the work list of the manufacturing department and include details of:

the product to be manufactured

the raw materials or sub assemblies to use

the steps needed to make the finished product

“Production Runs” are the to do or work lists of the manufacturing department.
Each manufacturing job, batch, or run is done based on a production run.

In OFBiz Jobshop you can

Create a new ProductionRun

Manage ProductionRun

its tasks

the materials needed

fixedAsset need (machine)

Parties working

Associate ProductionRun

View cost associated

declare all actions done on a ProductionRun

JobShop menu is the default screen for manufacturing.

Productions Runs can be created manually or automatically.
To create one manually:

Click the "Create a Production Run" button

To locate an existing Production Run

Click "Find"

A list of any existing Production Runs will be displayed

Click the Production Run Id to view the Production Run details

Production Runs cannot be deleted but they can be cancelled instead.

10.2.1. ProductionRun management in UI
Find production run

In this screen you can search for existing production runs. You can also create new production runs by clicking 'Create new production run'

Create production run

In this screen you can create a new production run.

Select the product that needs to be manufactured.

Set the quantity to produce and the start date.

Subsequently set the warehouse and the routing ID.

Give the production run a name and optionally a description.

Set the field for 'Create dependent production runs' to yes if you want the system to automatically create the production runs of sub assemblies or components.

Click the button 'Submit' to save the changes.

Display production run

This screen provides the details of the production run.
It also provides overviews of related orders, tasks, material, equipment and notes.

Edit Production Run

This screen displays the details of a Production Run.
Through this screen you can:

Edit the basic details of the Production Run

Create tasks that will be performed as part of the Production Run by clicking 'Tasks'

Add materials that the Production Run will use to make the manufactured product by clicking 'Materials'

Associate equipment that will be used as part of Production by clicking 'Equipment'

View any associated (or dependent) Production Runs by clicking 'Assocs'

View any associated content by clicking 'Content'

View the actual cost of the Production Run by click 'Actual Costs'

Basic Production Run Details

This section displays the basic details of the Production Run.
This includes information about the Facility where the Production Run will take place, the quantity of product to be produced and the proposed start and completion date.

The majority of these fields are editable, the exception being the "Calculated completion date".

This section also allows you to change the Production Run status as follows:

"Cancel" - To cancel the Production Run.

"Quick Close" - To close the Production Run

"Quick complete" - To mark the Production Run as 'complete'

"Confirm" - To confirm the Production Run

"Schedule" -To schedule the Production Run in the calendar

"Print" - To create a pdf file of the Production Run

Order Items

This section displays an overview of associated order items if the Production Run will be used to fulfill an order.

Tasks

This section displays an overview of associated tasks that will be performed as part of the Production Run. These are also called "Routing Tasks"

Materials

This section displays an overview of the required materials that will be used during the Production Run. This information is taken from the Bill of Materials.

Equipment/Production Run Fixed Assets

This section displays the required equipment or machinery to be used in the Production Pun.

Notes

This section displays an overview of any associated Production Run notes.

Display production run tasks

This screen provides an overview of all routing tasks connected to the production run.
From here you can also add a new or modify an existing routing task to the production run.

Display production run materials

This screen provides an overview of materials connected to the production run.
From here you can also connect new materials to the production run.

Display production run equipment

This screen provides an overview of the equipment related to the production run.
From here you can also connect new equipment to the production run.

Display production run assocs

This screen provides overviews of mandatory and dependent associated production runs.

Display production run content

This screen provides an overview of all connected content to the production run.

Display production run costs

This screen provides overviews of the costs of routing tasks of the production run and the cost of routings of the production run.

10.3. Routing

Routing is used to Link the tasks (routingTask) together in the sequence they need to be performed to produce final product.

Routing is used, when a productionRun is created for a product, the default routing associated to the product is "duplicate" for the productionRun.
All its routing-tasks are "duplicated" in the productionRun.

10.3.1. Routing management in UI
Find routing

This screen displays an overview of all routings available.
When select one it’s possible to Edit it.
From here you can also create a new routing by clicking 'New routing'.

Create / Edit Routing

In this screen you can :

Create new a new Routing or;

Edit an existing Routing.

Create / edit route associated task

In this screen you can connect a task to a routing and modify an existing routing task.

Create / Edit Routing associated product-link

In this screen can you create a link to a product for the routing.

The product specified here will be linked to this routing.
This means that when a Production Run is created for this product, it will automatically use this routing by default.

You can also edit an existing product link.

An overview of the associated products is displayed in the lower section of the screen.

10.4. Routing Task

Routing Tasks are the individual steps or activities that are needed to turn the raw materials into a finished product. There are used in the manufacturing or assembling process of a product.

Examples include:

Weighing out Raw Materials

Assembling a Product

Machining or Processing Materials

It’s necessary to create the routing tasks before creating a Routing or a Production Run.

10.4.1. Routing Task management in UI
Find routing task

This screen displays an overview of all available routing tasks.
It’s possible to select one to edit it.
From here you can also create a new routing task.

Create / edit route task

In this screen you can create a new routing task and modify an existing Routing Task.

Create / edit route task cost

In this screen you can associate a cost component and the related calculation method to the routing task.
You can also remove an existing associated cost component.

Routing task deliverable products

This screen displays an overview of all associated products deliverable to the routing task.
From here you can also connect new products to the routing task.

Create / edit deliverable products

In this screen you can add deliverable products to the routing task and modify existing deliverable products.

Create / edit routing task equipment

In this screen you can associate equipment to the task.
In the lower part of the screen all associated equipment is displayed.

10.5. Calendar

To be able to do planification, it’s necessary to know when each resources (machine) are available.

Calendar help you to define each period with availability.

10.5.1. Calendar management in UI
Find calendars

This screen displays an overview of exisiting production calendars.
From this screen you can

select one to edit it

create a new calendar by clicking 'New Calendar'

Create/modify calendar

In this screen you can create new calendars and change existing calendars.

Find calendar weeks

This screen displays an overview all calendar weeks From here you can create new calendar weeks.

Create/edit calendar week

In this screen you can define a new calendar week and modify an existing calendar week.

For a new calendar week give it a name and a description.
Set for each day the start time and the capacity.

Calendar exception week

This screen displays a list of the exception weekks of the calendar.
In this screen you can also add a new exception week to the overview.

Calendar exception day

This screen displays a list of the exception days of the calendar.
In this screen you can also add a new exception day to the curent calendar.

10.6. Manage Cost Component Calc Entries

Cost component calc is used to be able to calculate routing task cost.
In routing task cost, it’s possible to associate it to a Cost Component Calc.

In this screen you can create new cost calculations and modify existing calculations.

10.6.1. Cost Component Calc management in UI
Modify cost calculation

The first part of the screen is to create a new cost calculation, or to modify an existing calculation.
Click the 'Submit'-button to save the changes.

Subsequently, the screen will be refreshed and the the modified details are shown in the lower part of the screen.

Click the ID of cost calculation to modify it.
Click the 'Delete'-button to remove a cost calculation.

10.7. Bill Of Material

The Bill of Materials is the list of raw materials or list of ingredients required to make our manufactured product.

When a product is created and it will be manufactured, we need to define the relationship between the product and its raw materials. This is done using the BOM.

For configurable product, or product with feature, it’s possible to define some "Manufacturing Rules" to have a BOM which that adjust according to the options / feature chosen.

10.7.1. Bill Of Material management in UI
Find BOM

This screen displays an overview of the BoM’s available, i.e. a list of product with components.

When one is selected in the list, the detail of its components are shown.

You can also click the button 'Create BOM' to create a new BoM.

Add/edit a BoM

In this screen you can create a new BOM (a Product association) or modify an existing BOM.

Usually BOM is understand as the product and its componants, in this screen there is the component list and it’s possible to add or edit each of association between the product and one of its component.

BOM Simulation

This screen shows the effects of a simulated BOM.

The parameters form

Select the product of the BOM you want to simulate.
Choose the BoM-type and set the quantity to simulate.

Set the simulation type and select the warehouse to get the QoH (Quantity on Hand).

Subsequently click the 'Submit'-button to execute the simulation. The output of the simulation is shown below the form.

The simulation overview

The simulation will be executed and an overview will be shown after the button has been pressed.

The first section will show the details of the BOM.
The second part will show the required quantities and costs of the components.

Manufacturing rules

This screen displays an overview of the manufacturing rules that are applicable to produce a product.
A manufacturing rule displays the replacements of a component.

In this screen you can also create new manufacturing rules.

Create/Edit new manufacturing rule

This form enables you to define replacing materials for the BoM components.
In the second part of the screen the overview of replacement rules is shown.

10.8. MRP

MRP stands for “Material Requirement Planning”. It’s a computer program that, when run regularly, helps a business to plan what to manufacture and when to manufacture it.

It also has the added benefit of letting you know when to buy raw materials to meet your manufacturing commitments.

Running MRP is multiple step :

“MRP” tab and run the MRP report

view the MRP results

use the requirement generated to buy order or run productionRun

10.8.1. MRP management in UI
Run MRP

This screen enables you to run an MRP

Reports

This screen enables you to get a report on an MRP.

MRP Log

This screen displays an overview of the MRPs that ran.
The second overview in this screen displays the MRPs that are scheduled to run. From here you can also search for MRPs

Shipment plans

This screen provides an overview of all shipment plans.

11. SFA

Sale Force Automation component.

11.1. Overview

The main purpose of the SFA application is to support the process of creating orders for leads.

The SFA application is for a specific user to list his leads, contacts accounts and opportunities.
He can create new parties or he can assign existing parties to himself.

It is very much based on the party application as its source.
Records from the party application are selected with only one basic reason: a possible sale in the future.
That also means that records in the party manager should be complete, especially the role is pretty important. Not All roles, but at least 'lead' 'contact' and 'Account' should be defined.

11.2. SFA in User Interface
11.2.1. Main screen

The SFA main screen allows the quick create of any new lead and/or contact which is available on any SFA screen. Further this screen is designed to provide an overview of this users activity.

11.2.2. SFA Accounts find/list screen

The Accounts screen will show you the list which you have created or which have been assigned to you.

11.2.3. SFA Contacts find/list screen

The Contact screen will show you the list which you have created.

11.2.4. SFA Leads find/list screen

The leads screen will show you the list which you have created or which have been assigned to you.

11.2.5. SFA SalesOpportunity find/list screen

The SalesOpportunity screen will show you the list which you have created.

12. Human Resources

The OFBiz Human Resources system is one of the core application components and has all of the functionality you need to manage your business employees process : organisational hierarchies, recruitment, training, evaluation, …​It is well integrated with other components especially Accounting to manage Payroll and any specific employee agreements.

The HR Application data design, like most of the OFBiz back office administration applications, was inspired by the data models in The Data Model Resource Books by Len Silverston [1]. The sections below introduces some of the concepts in HR App that were derived from the models.

In OFBiz Party is one of the core object, a party is a person (employee, end customer, sub-contractor, contact, …​) or an organization (group, department, company, …​).
One of the strengths of OFBiz is the rich set of features it has build up to manage information and relationships for parties. This makes OFBiz a great platform for HR services because managing people and organizations is a core OFBiz technology.

Important terms in the documentation are defined in a Glossary. In order to promote a consistent usage and understanding of terms, links to the Glossary definitions are placed throughout the document.

12.1. About Human Resources

The people who work for your company are human capital and are its most important asset. Selecting a software platform that increases the value of your companies human capital and delivers benefits, services and opportunities to your workforce, is critical to your companies success. That platform must be able to accurately and reliability process worker transactions, collect decision support information, and communicate between management, workers and outside resources.

The OFBiz Human Resource application (HR App) can provide a stable foundation for building that platform.

12.1.1. The Human Resources Main screen.

The Main window is the entry point into the Human Resources Application and displays the Company tree view for navigating to the main menu items.

This screen will display the organizational setup of your Company.
The top level Company is defined in a system setup file: general.properties.

The system will also list any divisions or departments that have been setup with the role "Internal organization" as defined in the party relationships as a "Group member".

The number of organizational levels can be as many as required.

Nodes In the Company Tree

There are three node types in the tree, each identified by a different icon.

The top of the tree represents your Company, the highest level in the organization.

The Company and departments under the Company can have sub departments or positions.

Under positions are the people who fulfill the position.

Usage

Contextual menu is with right-clic

Navigate the organization to view departments, positions and people

Add or remove a department

Add a person

Quickly open the profile of any item in the tree

If the item is a position you can add a person to fulfill the position

12.2. HR Processes

Human Resources Management can be divided into several distinct processes.

Organization, Job Position and Definition

Employee Training and Development

Performance Management and Employee Evaluation

Employee Salary and Benefits Administration

Recruitment, Candidate Selection and Hiring

12.2.1. Organization, Job Position and Definition

Many companies organize departments in a tree structure. There is no special meaning attached to the word department.
It is used to describe any sub-division of a business organization.

In each department there are some Employee positions (or Job position)
Generally Job positions are authorized by a budget and fulfilled by people. The person fulfilling the position may be a permanent employee, a temporary employee or a contractor.

Positions may be salary or hourly, full-time or part time.

Positions have responsibilities.

Positions are defined by a type of work.

Your Companies organizational tree is shown on the main page of the HR App, and you can manage each part of it (view, add, remove departments; assign job position to department or manage its employments)

If you need to define one or more department, you must create it in the Party component.
Create a Party-Group and associated to it the role type Internal Organization (INTERNAL_ORGANIZATIO). After that the department appear in the drop-down when you select "Add Internal Organization" in the contextual menu (click right) of the Companies organizational tree in HR component.

If you need to define one or more Job positions, you must create it in the Employee Position HR sub-component ( Main HR Menu, option Employee Position) and maybe previously create some Position Type in Global HR Settings HR sub-component.

12.2.2. Employee Salary and Benefits Administration

Being able to manage employee salaries and associated benefits is a key part of any Human Resources system.

Salary is not related to a Employee Positions (also named Job Position) because when a person which fulfill a Job Position change to an other, salary does’nt change in every time. Some organization are waiting person demonstrate his capabilities for the new Job Position to change salary.

Salary is not related only to a Person, because in some company there are multiple subsidiaries or affiliate company, so Salary (and associated benefits) is related to Employments (a subtype of Party Relationship).

In hightly structured company, Salary is organized with a pay schedule which have normally two level Grade and step.
In Apache OFBiz, you can manage salary (and other point) directly by amount or with Grade-Step or with a mix of them.

In the OFBiz Human Resources application you can:

Create Pay Grades and Salary Steps within each Pay Grade

Assign a Pay Grade and Salary Step to a Job Position Type

Manage Employment and

his Pay History

his associated Benefits

his Leaves (Holidays, ill, family event,..)

Calculate salaries and Generate Payslips

12.2.3. Employee Training and Development

Training and professional development is important for an organization because it ensures that your employees have the knowledge they need to perform their work. It can also help to fill any gaps in skills and improve their proficiency.

In the OFBiz Human Resources application you can:

Define and create training courses

Schedule courses on a global training calendar

Make course available (or unavailable) for enrollment

Review and approve requests from employees to attend

12.2.4. Performance Management and Employee Evaluation

Evaluating and managing the performance of employees is another main Human Resources function. Performance reviews can be created for an employee and used to evaluate the work that they have done in a particular job position. Comments and ratings can also be added.

In the OFBiz Human Resources application you can:

Create a new Performance Review for an employee

Add individual review items such as Attitude, Communication or Technical Skills

Add ratings or comments to each item

If an evaluation has gone well then the employee can be considered for promotion to another job position, or can be given other benefits such as a salary increase.

12.2.5. Recruitment, Candidate Selection and Hiring

Recruitment is about at attracting applicants that match the skills and experience you are looking for in a particular job position. Candidates can apply and after reviewing their details, those who are the best match in terms of qualifications and experience are short listed for interview. The final step is deciding upon the final candidate that you want to hire and the employment contract details that are related to that.

In the OFBiz Human Resources application you can:

Create a Requisition for new job positions

Create Internal Job Postings

Apply for job positions

Review Resumes / CVs

Arrange and Grade Interviews

(add a test to check if createEmployment works for not yet employee (ex: party which are before only candidat)

12.3. HR core object
12.3.1. Employee Positions

An employee position is also called a job position. It is a role that has been created to perform a specific task within the Company. This means that it has approved funding to pay it.
Generally positions are authorized by a budget and fulfilled by people. For the Company to engage one person to do a job. OFBiz handles positions in a flexible manner so you can think of a position as an authorization for a full-time equivalent (FTE)

Employee positions are defined by:

the work description and responsibilities

a pay structure (e.g. hourly wages, salary, contract etc)

full-time or part-time

the skills needed to fullfill the position

	An employee positions is not the same as a person fullfilling the role. A person fulfilling an employee position is called an employee

An employee position can be fullfilled (i.e. someone is currently working in the role) or it can be unfulfilled (i.e. a job vacancy).

	In some cases an employee position could also be considered a full-time equivalent (FTE) and can be assigned to more than one person (e.g. job sharing)

In the OFBiz Human Resources application

an employee position have

a type, defined in Global HR Settings, which describes the job and it’s pay rates.
Some examples types could be secretary, production worker, sales manager, executive vice president or OFBiz programmer.
If more then one person is needed for a type of job then a position must be created for each required person : i.e. If 10 secretaries are authorized for the Human Resource department then 10 positions are created with type secretary.

a reporting structure. Positions report to other positions and not the people who hold the position.
You can identify / manage

the position to reports to

the positions(s), the current position manages.

in matrix orgnaization when there are multiple positions to report, most of time only one is the primary for the day to day approval (like holidays). It’s the purpose of the flag primary

a status, it can be one of: Planned For, Active/Open, or Inactive/Closed.

you can:

Create employee positions

Fulfill employee positions

Define the responsibilities of an employee position

Define a tree reporting structure between employee positions

Track employment position fulfillments over time

Employee Position management in UI
List Employee Position

This screen displays a list of positions for an employee.

	Employee positions are created and managed in the 'Employee Position' menu option.

Details about the position are displayed including any related dates and whether the position is temporary or not.

Create or Edit Employee Position

This screen is used to create or edit and update an employee position.

In the main search screen it is opened in create mode by clicking the New Employee Position button or in update mode by clicking on the EmployeePosition Id column in Search Results.

An Employee Position is the authorization, typically from the budget of an internal organization, for the Company to engage someone to do a job.

This means that you can fill a position in a number of different ways.

You can fill a position with one full time person, change the assignment of a position from one person to another over time, or split a position across more then one person at the same a time.

Positions have a status. They can be one of:

Planned For,

Active/Open,

Inactive/Closed.

Positions have a type, defined in Global HR Settings, which describes the job and its pay rates.
Some examples of job types could be secretary, production worker, sales manager, executive vice president or OFBiz programmer.

If more then one person is needed for a type of job then a position must be created for each required person i.e.
If 10 secretaries are authorized for the Human Resource department then 10 positions are created with type secretary.

Positions have a reporting structure and report to other positions (and not the people who hold the position).

You can identify the position a position reports to and/or the positions(s) a position manages.

	Be careful because it is possible to create circular reporting structures.
Fields

Employee Position Id - Unique Id for the position. May be user entered or if empty the system will generate sequence number.

Status ID - One of Active/Open, Inactive/Closed or Planned For.

Party Id - The party id of the internal organization authorized to fill the position.

Budget Id - A user entered identifier for the budget authorizing the position.

Budget Item Seq Id - A user entered identifier for the budget item authorizing the position.

Empl Position Type Id - Select a name for the position type. Position types are defined in Global HR Settings .

Estimated From Date - Enter date the position is expected to be filled.

Estimated Thru Date - Enter date on which the positions budget authorization is expected to end.

Salary Flag - Enter Y if this is a salaried position else N.

Exempt Flag - Enter Y if this position exempt from a requirement else N

Fulltime Flag - Enter Y if this is a fulltime position else N

Temporary Flag - Enter Y if this is a temporary position else N

Actual From Date - Enter the date the position is filled.

Actual Thru Date - Enter the date the position is no longer authorized.

Click Create - to create the position.

View Employee Position

This screen displays summary details about an Employee Position including details about who currently holds the position, their responsibilities and the reporting structure.

12.3.2. Employees

An employee is an individual that works for a company either full-time or part-time under a formal employment contract. The company pays the employee wages or salary.

	Wages tend to be related to an hourly rate and can vary based on the hours worked whereas salary is a flat rate generally paid monthly.

The Employees feature manages information about people who have an employment relationship with your Company or one of its departments. Details that can be setup include an employee profile, a display of all employee related information in a single screen and facilities for managing employee skills, qualifications, training, leave and payroll history.

In OFBiz Human Resources you can

Create a new employee

Search for an existing employee

View the full list of existing employees

Employees management in UI

This includes an employee profile, a display of all employee related information in a single screen and facilities for managing employee skills, qualifications, training, leave and payroll history

Create New Employee

This screen allows you to create a new employee.

There are some mandatory fields required and these are indicated on the screen

To create a new employee

Click New Employee

Enter the Employee details (e.g Name, Organization, Address, Phone Number)

Click Save

The new employee will be created

Find Employees

In this screen you can create a new employee, search for an existing employee and view a list of employees.

Selecting an employee in the list opens the employee’s profile and other screens associated with the employee.

To find an employee enter the search criteria.

	Only Employees Are Found.If you want to locate people who are not employees then use the Party Manager application.

Fields

Party ID - Must be the id of a party who is an employee.

User Login - The identifier used to login to OFBiz. An employee may have zero or more user logins.

Last name - Employee last name

First name - Employee first name

Employee Profile

The Profile screen for an employee is a collection of screenlets each displaying information about a different aspect of the employee.

In this screen you can:

View summary information about an employee

Update employee personal information

View, create, update, and expire employee contact information

View and create a list of related accounts

View training records

View employment information

View, create, and update login id’s, update security group

View and create party attributes

Upload party content

View and create notes

Employee Skills

In this screen you can assign a skill to an employee.

Enter numeric values in 'Years Experience', 'Rating' and 'Skill Level' to provide objective criteria for managing resources with the same skill.

These attributes can be used to locate resources with a needed skill.

NOTE:Skills are managed in 'Global HR Settings' where new skill groups and skills can be created or existing ones can be amended.

Employee Qualifications

In this screen you can enter details of any qualifications an employee has, to a person which could help track their ability to perform a particular job.

Existing qualifications can also be updated and status codes can be used to help manage the process of verifying the validity of any qualifications entered.

Employee Training

This screen lists any training for an employee.
Details such as the type of training, date, time and also the person who needs to approve the training are displayed

	You cannot enter any training details in this screen. If you need to enter training for an employee it can be done under the 'Training' menu option.
Employee Leave

This screen is displays any leave requested by an employee.

Any user with Human Resource Employee permission can view and request leave for any other employee.

	Only users with Human Resource Approver permission can update or approve a leave request.

Leave requests are managed in the 'Leave' menu option where in addition to requesting leave, an approver may review and approve any requests assigned to them.

	Leave types and reasons are managed by the administrator in the Global HR Settings.
Payroll History

This screen displays a list of invoices for the employee.
Generally these are payroll or commission invoices.

	An employee payslip is the same as an OFBiz payroll invoice

The invoice life cycle from creation through payment is done in the Accounting application.

Fields

Invoice ID - The distance identifier of the invoice. This number can be used to find the invoice in the Accounting application.

Invoice Type - Identifies the type of invoice. This will typically be Payroll.

Invoice Date - Date the invoice was created.

Invoice Status - Status may be In-Processes (can be edited), Approved (has been reviewed, can not be edited), Ready (post to GL), Paid (post to GL)

Description - A user entered description of the invoice.

From Party - The employee identified by the party id . The invoice is in effect from the employee to the company.

To Party - The party the invoice is to. For payroll this will typically by your company identified by the party id.

Total - Amount paid. For a payroll invoice this will typically be less then the gross amount of the invoice due to deductions for taxes and benefits etc

Outstanding Amount - Any unpaid amount due on the invoice.

12.3.3. Employments

An employment is a relationship between a person and your Company. The Human Resources application tracks employment benefits, pay history, unemployment claims and employment agreements for each employed person.

When you create new employee, an employee relationship is created automatically (/!\ see CreateEmployee functional Bug).

	If a person was entered into the application by some other means then you will have to create the employee relationship manually in the Party Manager application.

The employment record includes the start and end date of the employment. When the employment ends you include the type of termination and a reason. For example, an employee may have been let go because of poor performance. (In this case the 'type' could be 'fired and the reason could be 'poor performance')

The Employments screen can be used to create an employment or search for existing employments.

To other explanation, look at the process Employee Salary and Benefits Administration introduction.
A Database diagram for main link with other entities exist in HR Data model - Employment

Employments management in UI
Create or Edit Employment

This screen allows you to create a new employment or edit an existing one.

To create a new employment relationship between Company and an employee

Select the Employee Party Id

Enter the start date for the employment (e.g. Hire Date)

Click Create

Once created the employment detail screen will be displayed where you can update a range of information related to the employment such as benefits, payment preferences and unemployment claims

12.3.4. List Employments

This screen displays a list of Employments for an employee.

NOTE:Usually a person will have only a single employment with an employer.

The employment details (e.g benefits, payroll preferences, etc) can be modified by clicking 'Edit'.

12.3.5. Performance Review

Performance review allows employees to post reviews that can be used by management in evaluating the performance of the individual employee.

The employee’s position is also captured with the review which allows the creation of reports that look at ratings for a review item by position.

Performance Review Item

Each review has a list of items that can be rated and commented on.

	Performance review item can be created or deleted but can not be changed.

In the OFBiz Human Resources application you can:

Create performance review

Search performance review

Update performance review

Add performance review item

Delete performance review item

12.3.6. Qualifications

Qualifications are a feature of the recruitment process that allows you to record the details of any qualifications held by job applicants or your existing employees.

During the job application process, you may want to ensure that applicants have a minimum set of qualifications as a requirement for a position. The details of the qualifications for each applicant will need to be captured and if necessary, verified.

For existing employees, details of qualifications during their employment with your organisation can be added at any time.

In the case where qualifications expire if not renewed, you can also add an expiry or renewal date.

12.3.7. Recruitment

Recruitment is an important function in any organisation. It is a set of processes that allow you to specify, search for candidates to fulfill the roles that you have available.

When you have a job position that needs to be fulfilled, you can create a Job Requisition. The job requisition identifies the skills, qualifications, experience and also the number of resources needed for a position.

	Currently the default assumption is that the Job Requisition is for an Internal Job posting

Once the requisition is created, you can then create Job Posting based on the requisition. For example if the requisition was for three (3) roles then three job postings can be created (each with different application deadlines) one to fulfill each of the positions.

People can then apply for the positions and send in their CVs or Resumes. You can track the progress of the the application and also create details about various types of job interviews needed (e.g. HR, Panel, Case Study /Practical Test etc) and link it to the requisition.

You can also track the status of people who have applied for a position.

In the OFBiz Human Resource application you can

Approve or reject job applications

Manage and book job interviews

Record the result of job interviews

12.3.8. Skills

Skills are the basic foundation of any Human Resources function as it is a key factor in identifying the suitability of someone to perform a specific task or job. They can often be divided into two types; general and specific, and are characterised by things such as years of experience, rating or level of expertise.

In OFBiz basic skills can be defined in Global HR Settings and then linked to actual individuals via the Skills menu option.

In the recruitment process, skills are specified as part of the job requisition for an employee (or job) position. This helps ensure that the recruiter can focus on finding applicants with the relevant skillset.

Your employees can also gain new skills as part of their employment and so OFBiz allows you to record and track their newly acquired skills. It may be that rather than start a new recruitment process, you may be able to find someone with the right skills from your existing employees.

In the OFBiz Human Resources application you can

Assign or link skills to job applicants (i.e. non employees)

Assign or link skills to existing employees

Search for existing employees that have the required skills for a job

12.3.9. Resumes

Resumes or Curriculum Vitae (CVs) are documents that job applicants use to apply for job positions. These documents summarise the applicant’s experience, qualifications, contact information and details about why they are suitable for a particular job position.

In OFBiz you can enter a resume as a document and then link it to a person. Each resume entry has a unique identifier (that currently needs to be manually entered!). This identifier links a person to an instance of their resume.

	The OFBiz Content Manager application is used for the linking of resumes because it was designed for managing, storing and retrieving electronic data in varying formats - such as text, images, MS Word, PDF or even web URL’s.
12.3.10. Training
Introduction

Training and professional development is important for an organisation because it can help to fill any gaps in skills and improve the proficiency of the existing workforce. The training section of the HR module includes a Training Calendar where new training classes or events can be scheduled for an organisation. Users that have HR administration permissions can create, assign and approve training classes. All other users can view the list of classes available, their training status and any requests they have made to enroll for training.

General Process Flow

Training classes are created in the Global HR Training Class Type screen

Training classes are scheduled and added to the training calendar

Employees can create a request to attend a training

The employee supervisor needs to approve or reject the employee training request

Employees can check the status of the training requests

Training Calendar

The main screen in the Training feature is the Training Calendar. This is where you add classes and class participants. You can navigate the calendar by clicking the navigation text for day, week and month views located in the calendar title bar.

Admin can schedule a training through training calender.

Admin can assign training to an employee(right half of calendar screen).

Employee with his login can request for Training to admin from the calendar.

Employee cannot request same training event again to same approver.

Add New Training Event

Training classes are created in the Training Calendar by clicking the Add New text command located in each calendar day cell. This action opens a small window above the calendar to enter the training class details.

	If you try to create a class and do not have correct User permissions, you will get an error. After a class is created a numeric class identifier and text identifier description appear in the calendar for the day of the class.
Request Training / Add a Training Participant

Participants can be added to a class by clicking on the class identifier. If you are the creator of the class the Participants window above and to the right of the calendar opens. You can add participants by entering their party id and clicking the Add button. The list of participants is displayed and updated. After a new participant is added to a training class or event, they are given the default status ‘Assigned’.

Approve Training

To approve a request for training, tor training administrator navigates to the Training Approvals screen and locates all requests with a status of "Assigned". They look up the person listed as the approver party. After checking with the approver they click update button to open the approval screen. In the approval screen the administrator sets the Approver Status and adds a reason for the decision. The user can see the status of their training schedule by clicking on the Training Status menu.

In "Training Approval" tab (in case of Employee login tab name would be "Training Status")

Admin can approve/reject the training requested to him

Admin can not change the training status once it is rejected.

Employee can check status of requested and assigned trainings.

	TO CHECK Something isn’t working correctly in 16.11. The there is no update button to click to approve a participant for training.
Simple Howto for Training UI
	TO CHECK for the moment, work in progress…​

Introduction: Trainings in HR module includes Training Calendar where we can create new schedules from trainings available in an organization.

Admin can assign trainings & employee can request for scheduled trainings.

Employee can also check status of their training requests & assignments.

Need of Trainings in HR:

Training and development of professionals fills up the skill gaps and further improve the levels of proficiency.

Training and development manages constantly changing business and industrial scenario and therefore, matches with the requirements or demands of changes on the organizations.

Creates a learning organization culture.

Organizational development:

Organization decides to use certain initiatives and wants to train and develop a good number of people in the entire organization or the people in certain chosen departments or projects on those initiatives.

Prepares the organization to meet the needs of legal/statutory requirements. Features of Trainings:

New Trainings can be added/modified.

Trainings can be scheduled in the calendar.

Employees can apply to supervisor for available scheduled trainings but, cannot request same training event again to same approver

Admin can assign trainings to Employees.

Admin can approve/reject the trainings requested to him but, once rejected cannot be approved again.

Employees can check the status of their training requests and Trainings assigned to them.

Road Ahead: Currently we have implemented Trainings under HR module.

We are working on the implementation of Training calendar in profile tab of Employee.

We are also planning to introduce trainer’s information in training calendar.

In "GlobalHRSetting"

Admin can create & manage the trainings provided by the organization.

12.3.11. Leave

Generally each of your employees will be allowed to take a certain amount of time off work on an annual basis. This time-off work can be called leave, holiday or vacation. The amount and type of leave they can take may depend on their job position or how long they have worked for you.

You may also allow your employees special leave such as days off when they are ill (sick leave), time off during pregnacy or birth of a child (maternity or paternity leave) or time off to attend a funeral (bereavement leave).

OFBiz allows you to setup a range of different leave types and categories to cover many situations.

In all cases the employee will need to request the date (or dates) they would like to take as leave. Next the manager of the employee will need to approve the leave request. Once approved the employee can then take the leave.

In the OFBiz Human Resources application:

Employees can schedule or a leave request

Managers can create leave requests on behalf of an employee

Managers can approve, reject or delete employee leave requests

	Users with Human Resource Approver permission can only approve a leave request. To update or delete a leave request, you will need to have Human Resources Administration permission.
12.3.12. Security

OFBiz has a security model that controls access to all aspects of teh system at a very detailed level. This means that it is possible to manage what each user has access to and what actions they can perform.

	Security can be so fine grained to the lowest level such as a view, or the creation, update or deletion of a single item of information

This section covers the security permissions that inlcuded as part of the Human Resources application and how an administrator can assign permissions to users using the Party Manager application.

	A person may have one or more OFBiz login id’s. Each login id can be assigned to it’s own set of Security Groups. This means that the id a user logs in with determines what applications the person can work in and what work can be done in the application.
Human Resource Permissions

In OFBiz a Security Group is collection of permissions that allow a members of the group to use the application and any resources. The Human Resources application has three special security groups that can be assigned Human Resources users. There are also other general administrative security groups that let managers and administrators work in the application.

You can use the Party Manager application to add users to one or more Security Groups.

The three special HR App Security Groups are named by role:

Employee Role - This is mandatory to be able to logon into the Human Resources application. This is true even if user has the the other Human Resources Approver and Administration Roles. The employee role has the most restrictions on what a user may view and the actions they can take.

Approver Role - The Approver role gives members of the group the ability to approve, training and employee leave requests. The approver has all of the permissions included in the Employee Role and can also view and update some additional screens that are not available to the Employee role.

Administrator Role - The Human Resources Administrator Role has permission to do most things in the Human Resources application. They are allowed full access to view, create, update and delete throughout the Human Resources application. Please see the note below for the additional permissions required to be able to do everything in Human Resources.

	A person with the Human Administrator Role must also belong to the following Security Groups (Work Effort User, My Portal Employee, My Portal Customer or Scrum Team) to be able to add Training classes in the Training feature.
General OFBiz Permissions

Some OFBiz users (from the demo data) may not have any of the Human Resource permissions but can still access the Human Resouces application to be able to perform general operations. These include:

Business Admin has permission for all operations in the Human Resources application

Flexible Admin has permission to create, update, delete and view operations in Human Resources

Full Admin has permission for all operations in Human Resources

Super has permission for all operations in the Human Resources

Viewadmin has permission for viewing details in Human Resources

Security Administration In Party Manager

A user must be granted permission to use the Human Resources application. This section describes how to do this using OFBiz Party Manager. It assumes the user has a user login and Party administration privileges.

Please do the following to grant permissions

Login to the Party application

User the search functionality to locate the user that you want to give Human Resources permissions to

When the search results are displayed, click on the Party ID column

In the User Name(s) screenlet click the Security Groups button for the User Login that will receive Human Resources permissions

In the Add User Login to Security Group screenlet select the HUMANRES_EMPLOYEE. from the Group drop-down-list.

Click the Add button to use the current date for the From Date or enter dates for From Date and Thru Date as needed then click Add

If the person is to be allowed to approve Training add the HUMANRES_APPROVER permission. As in the previous step enter dates as required

If the person is to be allowed all access then add the HUMANRES_ADMIN permission…​ As in the previous steps enter dates as required.

12.4. Global HR Settings

Global HR Settings are used to setup the basic reference data that is used throughout the Human Resources application. Many of the screens contain fields that have drop-down lists for selection and these drop-down list can be setup here.

	You need to have 'administrator' or 'create privileges' to update any of the Global HR Settings
12.4.1. Employee Leave Type

Used by Employee Leave management to detail why is employee request a leave.

In this menu option you could manage (create / modify / delete) Leave Type and Leave Reason.

For some example, look at the Tutorial Employment and Salary [_step_5_employee_leaves]

Reason Type

To create or request a leave an employee could give the type of leave and the reason.

12.4.2. Pay Grades

Useful to define a salary amount table for the company. With this table for each grade and a step you have a amount.

It’s used in structured entreprise to be more clear on salary definition or supplier cost.

Worksheet PayGrade - SalaryStep is not usable alone, when it’s used to define a Rates it’s associated with PeriodType (per year, per month, per week, per hour) and RateType (Standard, Average, Hightest, lowest, …​).
So sometine it’s needed to define multiple Grades if it will be use with a specifics periodType, ex: for developper, one Grade for using with «per month» and one Grade for using with «per hours»

Salary Steps

For each Grade, it possible to have multiple step. It’s possible to have overlap in step betwwen to grade.

For more detail, look at the Tutorial Employment and Salary [_step_1_pay_grade_and_salary_step]

12.4.3. Position Types

Employee Positions is associated with a Position Type to "pre-define" some informations about the Job Position.

Position Type can be use for legal purpose, like social classification or Union constrain to be able "classify" Job position.

Position Type Rate

When defining a Employee Position, Salary is one of the important point. Depending of company salary rules, most of time there is not a salary associated with a Position but a range and some indicators.

So it’s possible to associated to a position type some amount associated to a Rate Type (Standard, Average, Hightest, lowest, …​) and a PeriodType (per year, per month, per week, per hour).

It’s also used by WorkEffort Component to manage cost for subcontractor, for example.

Position Type Grade

If company is very structured on the salary management and so mange Salary by Grade-Step, it’s possible to associate a Position Type and a RateType a Grade-Step.

As business rules, it’s not possible to have for the same RateType a amount and a Grade-Step.

Valid Responsibilities

It’s possible to define some responsibilities for a Position Type, to constrain the responsibilities it is authorized to associate to a Employee Position (which is associated to this Position Type).

12.4.4. Skills Types

A skill type is used to define a skill group. Your employees, contractors and partners may have hundreds of different of skills so skill types allows you to organise these skills so they are manageable.

This is helpful for reporting on your companies skill inventory or searching for resources with the skill types needed for a job. You can search for skills types and assign skills to people and organisations in the Skills feature.

	You can manage the skills of an individual or an organisation in their profile in Party Manager uisng the Party Skills feature.
12.5. HR Data model

This chapter describe the main entities for the Human Resource Component.
The goal is to show :

overall view for each HR core object

link between entities

For each diagram, Main Entities (for this diagram) are in purple
Entities in Light Blue have not all fields (link, composition ) present.

12.5.1. Employee Position
Position and PositionType

This diagram explain Position and PositionType main informations.

Diagram associated

Position details

Party in Human Resources

Employment

Employment Appl

Qualification Skill training

Performance Review

Position details

This diagram show all Positions main informations / link.

Diagram associated

Position and PositionType

Party in Human Resources

Employment

Employment Appl

Qualification Skill training

Performance Review

12.5.2. Employment
Employment

This diagram explain Position and PositionType main informations.

Diagram associated

Position and PositionType

Position details

Party in Human Resources

Employment Appl

Qualification Skill training

Performance Review

Employment Appl

This diagram show all Positions main informations / link.

Diagram associated

Position and PositionType

Position details

Party in Human Resources

Employment

Qualification Skill training

Performance Review

12.5.3. Qualification, Skill, Review
Training

This diagram show all link between Party & PartyRole AND all HR entites.

Diagram associated

Position and PositionType

Position details

Party in Human Resources

Employment

Employment Appl

Performance Review

Performance Review

This diagram show all link between Party & PartyRole AND all HR entites.

Diagram associated

Position and PositionType

Position details

Party in Human Resources

Employment

Employment Appl

Qualification Skill training

12.5.4. HR App intra-application integration
Party in Human Resources

This diagram show all link between Party & PartyRole AND all HR entites.

Diagram associated

Position and PositionType

Position details

Employment

Employment Appl

Qualification Skill training

Performance Review

HR Glossary
Employment Benefits

Employment imply salary but not only, most of time, there are some benefit packages associated. Examples are vacation,health or life insurance, sick leave or retirement plan. Cost of these package may be partly or completely paid by the entreprise. Example can be see in [_step_4_employee_associated_benefits] in [_tutorial_employment_and_salary].

Employment

Employment defines the relationship between your Company and a person who is an employee. The employment relationship tracks employee benefits preferences, pay history, and unemployment claims and agreements.
For more detail see Employments chapter.

Employee

An employee is a person (and so a party) who has an employment relationship with your Company.
For more detail see Employees chapter.

Employee Position Type

Employee Position Type is a name that describes a position (Employee Positions). You can define your own position types in Global HR Settings > Position Types.

	Business Analyst, Programmer and System Administrator are examples of position types in the OFBiz demo data.
Exempt Flag

The exempt flag can be used to indicate if an employee position is exempt or non-exempt under the fair labor Standards Act (FLSA).

Fulfillment

A fulfillment associates a person with a position. A person can fulfill more than one position and a position can have more then one person.

Fulltime Flag

The fulltime flag can be used to indicate if an employee position is for a full or part time position.

HR App Menu

The main menu that opens the high level features of the HR App i.e. Employees, Employments, Employee Position etc.

Number of Employees

Number of employees that are reported in the Party Group Information screenlet of the groups profile (Visit Party Profile screen).

Qualifications

Qualifications for an individual person or organization are in the Employees Qualifications menu item. To find and update the qualifications of people and organizations visit Qualifications menu.

Party Qualification Type

Party qualifications define a person or organizations accomplishments that indicate their suitability to perform a job. Qualifications are organized into qualification groups for the purpose of managing and reporting.

Position

A Employee Position is a job that can be filled by more then one person over time or at the same time. Positions are defined by a type of work. For example there may be 20 positions in an organization for a secretary. Each position is related to a department in the organization.
For more details have a look at Employee Positions in HR core object chapter.

Rating

Rating is a user defined numeric rating for a skill. (See Skills Menu)

Responsibility

Responsibilities define duties assigned to a position. They are defined in Responsibility Types and assigned in Employee Position Responsibilities.

Salary Flag

The salary flag can be used to indicate if an employee position is salaried or paid hourly.

Skill

Skill is some ability or knowledge possessed by a person or organization that is needed to perform a job for the company. See Skills

Skill Level

Skill level is a user defined numeric rating a skill. It is up to the user to assign some meaning to the level. For example 1=Entry, 2=Intermediate, 3=Expert (See Skills Menu).

Skill Group

Skill goup is a name that describes a collection of skills that have common attributes (See Skills Menu).

Temporary Flag

A temporary flag can be used to indicate if an employee position is permanent or temporary.

Termination Reason

The termination reason is a name describing the cause related to a termination type e.g. Type: resigned for reason: found new job.

Termination Type

The termination type is a name for the kind of termination e.i. Resigned, fired, retired, layoff.

Appendix A: HR Data Model Resource Book Difference
PayHistory

it’s not really a difference, more a not explicit detail about fromDate field.
PayHistory is a detail of Employment entity (Composition in UML language) and Employment entity has a fromDate field (as one of the keyField), and we need fromDate field for information about PayHistory, so it’s needed to have one named emplFromDate (coming from Employment) and one classical fromDate to be able to have multiple PayHistory for one Employment.

PartyBenefit

It’s exactly the same problem or case than PayHistory, currently in Apache OFBiz entity is exactly the same as in Data Model Resource Book Difference (only one fromDate field), so it’s not possible to have a correct User Interface as an Employment subOption.
So correct solution should be to have one more field: emplFromDate (coming from Employment).

Resume

entity in Apache OFBiz is a simplification of the concept explain in the Book

Appendix B: HR Enhancement & Bug
12.B.1. Functional bug

This section explain current "Bug" which are waiting some developpment.

CreateEmployee

Currently create an employee should create a Party Relationship between Employer and Employee(cf documentation), it’s not working because a parameters if forgot in service but it’s not the major "Bug", and the main question is :
create an employee should create a Party Relationship or a Employment (which is a subtype of PartyRelationship) ?

If the create Employee screen is used from HR, it’s to use HR functions and for HR component, an employee has an Employment (which is a subtype of PartyRelationship), so create an Employee should create an Employment (and so the first PayHistory).
Screen and Service should corrected to do these points.

12.B.2. Functional Enhancement

This section explain which developpment should be done to add some features which should be in Apache OFBiz

Valid Responsibility

Entity ValidResponsibility exist in Apache OFBiz, associated controler screens, forms and services exists too, but there is no menu to use them !

Add a entry menu in Employee Position Type sub menu (in Global HR Setting)

Correction on screen definition to included GlobalHR decorator and button highlight

JIRA OFBIZ-11045 is for that.

Business Rule

It’s suggest in «the Data Model Resource Book» to have a check before adding some responsibilities to a job Position if Position Type has it (in ValidResposibility) with valid date.

Position Type Rate amount-and-grade

For a RateType, it should not be possible to have a amount AND a Grade-Step.

EmplPositionTypeClass

Entity exist but no screen management.

Same for EmplPositonClassType

BenefitType

Entity exist but no screen management.
It should be place in Global HR Settings

13. Marketing

The overall purpose of the Marketing application is the support to select leads from parties obtained from a certain source or marketing segment to convert to opportunities by contacting these parties via a contact-list related to a marketing campaign.
(contact-list generation support not yet implemented)

The marketing application is supporting you to create, select and follow sales opportunities in order to create sales orders for the company.

The first option of the marketing application is the definition of a datasource [DataSource], and connecting or loading party information to it [PartyDataSource]. In the party application a data source Id can be added to the party.

A second input to the marketing application is the Segment group and classification which again can be allocated to parties in the party component.

Now a marketing campaign can be created. A contact list can be created using the parties related to a dataSource or marketing segment classification and referring back to the marketing campaign

Contact lists are currently email mailinglists, the OFBiz system could be extended to include the support of calling by telephone and entering the results.
On the email sent via this lists tracking codes can be used to measure the response when the readers of the email mailing click on a link where a trackingcode is specified.
For more info look at the program: applications/marketing/src/org/apache/ofbiz/marketing/tracking/TrackingCodeEvents.java

Opportunities resulting from these actions can be entered in the SFA web application referring back to the marketing campaign.

13.1. Marketing in User Interface
13.1.1. Help for main screen

This page acts as an placeholder of the overview of the marketing activity in the company.

It can be customized to describe internal process.

13.2. Marketing Contact Lists.

A contactlist is currently an email mailing list to inform a certain number of parties via email.
The system however already has a provision to use this facility for calling list or to create mail and merge list for paper documents.

13.2.1. Contact Lists management in UI
Help for Find contact list screen

This is the initial screen to find an existing contactlist or create a new one.

Find selection fields.

ContactList Id : The unique id of the contact list

ContactList Name : The name of the contactlist

ContactList Type : The type of the contactlist

Contact Mech type : the contact type like email, postal address etc.

Campaign Name : The marketing campaign name

Edit a contact list.

This screen enables you to edit an existing contactlist or create a new one. Below an explanation of the fields

Contact list fields.

ContactList Id : The unique id of the contact list

ContactList Name : The name of the contactlist

ContactList Type : The type of the contactlist

Is Public ? :

Is Single Use ? : If set to 'Y' all parties of this contactlist will be deleted after sending the email.

Contact Mech type: the contact type like email, postal address etc.

Marketing Campaign Name : The marketing campaign name

Owner Party Id:

Verify Email From:

Verify Email Screen:

Verify Email Subject:

Verify Email WebSite Id:

Opt Out Screen:

Help for import contact list parties

This is the initial screen to find an existing parties and select them for import to the contact list.

Find selection fields.

Party Id : The unique id of the party

Party Type Id : The type of the party

Role Type : The role of the party

Contact Mech Type Id : the contact type according to the contact meth type’s ID of the contact list.
There is a sub form for this field according to the contact mech type’s ID.

Import the parties

Select the parties in the search result list.

Press the "Submit Query" button

13.3. Web tools

The Webtools application is the UI-gateway to all the framework functions.

13.3.1. Help for Webtools Main page.

This is the default screen for the Webtools application.
Several links are present on this page to access specific tool screens directly.
Using the application menu you can select the tool you need.

The Logging section is used to view and configure the OFBiz system logs.

The Cache & Debug section is used to monitor the OFBiz cache system status. You can even set or clear some cache content or force Garbage collection with this tool.

The Artifact Info section is used to navigate through all OFBiz artifact files. When accessing this section the complete OFBiz code base is scanned and a list of all artifacts is offered to the user to be navigated. Please note that the initial scan can take a while to be completed.

The Entity Engine section is used to interact with the entities defined in the system. You can view the entity structures, search for entity content, navigate though related entities, etc.

The Service Engine section is used to interact with the services defined in the system. You can view all services details, monitor the jobs that are running, the active threads. You can even manually run a service or schedule a periodic/delaied job execution.

The Import/Export section is used to transfer entity content from the OFBiz system to external systems and viceversa. Various import/export systems and formats are available.

The Configuration section is used to set parameters for the OFBiz system.

Apache OFBiz Plugins
The Apache OFBiz Project
14. Project Manager

Unresolved directive in plugins/projectmgr/src/docs/asciidoc/project-mgr.adoc - include::plugins/projectmgr/src/docs/asciidoc/_include/prjm_intro.adoc[leveloffset=+1]

14.1. ProjectMgr in UI
14.1.1. Main screen.

This is the startup screen of the project manager. It will show all active projects with some statistical data.

14.1.2. My tasks

This overview outlines all tasks the user has been assigned to.

14.1.3. My Timesheets

Here the user enters the hours worked on tasks.

It also provides an overview of all timesheets the user has filled out.
It also shows the status of the timesheets.

14.1.4. Find Projects

This screen provides an overview of all projects the user is participating in.

Unresolved directive in plugins/projectmgr/src/docs/asciidoc/project-mgr.adoc - include::plugins/projectmgr/src/docs/asciidoc/_include/prjm_project.adoc[leveloffset=+2]

14.1.5. Project - billing

This screen shows all hours registered to the various tasks in the project by all participants.

From here the Project Manager processes all time entries for further processing regarding invoicing and cost accounting.

14.1.6. Project - edit info

The Project Manager can edit various details regarding the project.

14.1.7. Project - orders

This screen provides an overview of all orders related to the project.

14.1.8. Project - phases

This screen provides an overview of the phases of the project.

The Project Manager can manage all phases in the project here, e.g. defining new phases.

14.1.9. Project - resources

This screen provides an overview of all participants in the project.

From here the Project Manager can add new resources to the project, or end the participation of existing project members.

14.1.10. Project - tasks

This screen provides an overview of all tasks associated to the project.

14.1.11. Project - Requests

This screen provides an overview of all customer request regarding projects.

14.1.12. Tasks

This screen provides an overview of all tasks in the module

14.1.13. Timesheets

This screen provides an overview of all timesheets registered with the application by all project participants.

15. My portal Plugin

Within the 'my portal' application it is possible to create a collection of screens for a specific type of user of the system.

Examples are a general employee, an account manager, a customer, a supplier etc…​

The system makes use of special portlets which can be arranged and selected/hidden by the logged on user.

The MyPortal application is an example of what it’s possible to do with OFBiz Portal technics (integrated in ofbiz framework)

15.1. Some Portlet in other components

Unresolved directive in plugins/myportal/src/docs/asciidoc/my-portal.adoc - include::plugins/myportal/src/docs/asciidoc/_include/portlet-system-info-notes.adoc[leveloffset=+2]

Unresolved directive in plugins/myportal/src/docs/asciidoc/my-portal.adoc - include::plugins/myportal/src/docs/asciidoc/_include/portlet-calendar.adoc[leveloffset=+2]

16. Asset Maintenance plugin

Assets are items of value that are owned by the business.

The Asset Maintenance application is used to schedule and trace all maintenance activities on assets.

17. The Scrum Component.
17.1. Introduction

The purpose of this component is to have a web based and ERP integrated access and recording for all information related to your Scrum project development.
The Scrum development methodology itself is described in any of the following documents:

Scrum guide (various languages)

Scrum in 30 seconds.

Scrum in 5 minutes

Below follows a list how the system should be used and at what time you have to update the information within the Scrum component.

17.2. Administration

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-timeSheet.adoc[leveloffset=+2]

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-default-tasks.adoc[leveloffset=+2]

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-members.adoc[leveloffset=+2]

17.3. Product Backlog.

Before anything can start a product backlog is required which will need a product to be created first. So create a product assign the it to a product owner which was created in the Scrum member section. Then go to the backlog and create the backlog items.

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-product.adoc[leveloffset=+2]

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-product-backlog-item.adoc[leveloffset=+2]

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-product-categories.adoc[leveloffset=+2]

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-project-sprint.adoc[]

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-my-work.adoc[leveloffset=+1]

17.4. Task

The view task show Task description.

17.4.1. View Task

New Task button : To create new task.

Task information.

Sprint Backlog Item Note.

Task Attachements.

Unresolved directive in plugins/scrum/src/docs/asciidoc/scrum.adoc - include::plugins/scrum/src/docs/asciidoc/_include/scrum-open-test.adoc[leveloffset=+1]

17.5. Sprint Demonstration and Evaluation meeting

At the end of a sprint demonstrate the system to the product owner and interested parties. The product owner will incorporate comments into the current backlog list. The team and Scrum master will evaluate the sprint so lessons can be learned for the next sprint.

Determine also which tasks were not completed and return them to the product backlog to be included in a next sprint.

The sprint will be repeated until the project is complete.

17.6. Security

In the Scrum component there are security roles to access in the Scrum component.

Product Owner can create product, project, and assign member in project.

Scrum Master can do anything on the project.

Scrum admin can do anything on Scrum component

Scrum team can assign task to yourself and view project.

18. Birt OFBiz® plugin

The Apache OFBiz Project

	

By default the Birt plugin is disabled for security reason, see the Birt ofbiz-component.xml file for more info.

The birt plugin is one of the OFBiz plugins.

18.1. OFBiz Flexible Reports

One of the functionalities of the birt plugin are the "OFBiz Flexible Reports"

There is an announce with some history in the OFBiz blog: Reporting in Apache OFBiz® and the OFBiz Flexible Reports

18.2. Technical Documentation
18.2.1. Report creation
Introduction

A flexible report is an OFBiz content of FLEXIBLE_REPORT type that allows a final user to make use of the reporting module to obtain flexible reports, ie reports which are created from an entity or view definition and even from a service. A flexible report is created from a Report Master (content REPORT_MASTER), and an optional XML override of the parent form.

Pre-requisite

OFBiz framework

The Birt plugin

The BIRT Report Designer: Using the Birt Report Designer

How to do

Get to Birt component in OFBiz 

Click on the "Flexible Report" menu (varies depending on themes)

Click on the "Generate report" button, you get to this screen:

Fill the form: 

The list "Choose report topic" will let you choose among predefined report masters your topic of interest.

The report name is a simple short name from which the file name will be generated.

The description is a short description which will allow you to recognise the report and its topic.

The box "Generate filters in design" will add in the design the visualisation of the filters filled in the filtering form.

Once the form is validated, OFBiz will show you the "Edit Report" screen.

Report information

This first panel allows you to change the report description and status. Actually it does not make sense changing the status to published before having downloaded the .rptdesign file (Birt Report Designer file) from the server (in database), edited and uploaded it back to the server. This is explained in the section below. Changing the status allows users to use your reports. But if you publish without any change the report will render as empty.

The .rptdesign report file: download, edit, upload and publish it

To really use the report you need to download the .rptdesign file from the server in a location from where you can edit it with the BIRT Report Designer. So you need to install first the BIRT Report Designer. Then you can edit the .rptdesign file in the BIRT Report Designer. For that refer to Using the Birt Report Designer.

Editing the downloaded file

Once you installed the BIRT Report Designer and have downloaded the .rptdesign file, you can edit it with the Birt Report Designer. When you have edited it suiting your needs you must upload it to the server for your changes to be taken into account by OFBiz.

This is when things begin to be really interesting. You can then test your report using the "Preview" panel. There you can temporarily filter the result, and use the export format you prefer, once done click "Send". You can then decide to change the report content in the Birt Report Designer again or keep your changes. Once done in the Birt Report Designer, simply select the changed file to upload, and upload it again. You can re-test your changes and continue until you really get what you want! You can then publish the report to allow users to select and use it. There are 2 ways to publish a report from the "Manage reports" screen or directly in the "Report information" panel. We will see the "Manage reports" screen below.

Filters Overriding

You may want to overide the default filters. You can then use the Xml "Override filters" panel to override and personnalize the form, once done click "Save". If you ignore that step, it will NOT prevent the report creation, it is already done, it will just be with the generic filtering form inherited from the master from.

	if no preview is available, it is usually due to a mistake in the master form code. You can edit it in the database.
Manage reports

The "Manage reports" button get you to a screen which allows to edit (get back to current page), publish or delete a report.

Use a report

Users can select and use any published report from that screen. When they select a report they then get the same "Preview" Panel and can do the same things than in the "Edit Report" screen. Refer users to

18.2.2. Using the Birt Report Designer
Introduction
	this feature will be officially available with the R17.12 branch first release

The creation of a flexible report goes through a design step of the initial flexible report output under the Birt Report Designer.

This document describes the simplest designs to connect to the data. It is not exhaustive, and simply attempts to cover basic needs. You will find much more documentation online. In our approach, the connection to the data is generated automatically by OFBiz, only the design part of the report will be discussed.

Installing the BIRT Report Designer

Installing the BIRT Report Designer is easy. If you use Eclipse, you can include it as a plugin. You can also install the whole BIRT Report Designer. I use Eclipse but I prefer the second way, to not mix things. So simply download and install the whole all-in-one thing. Or install the plugin if you prefer and use its "Report Design" view which allows to edit .rptdesign files.

	if you installed the BIRT Report Designer under say, a Birt directory, then by default the reports will be accessed from the Birt\workspace\Report Builder directly and this is where you should put the .rptdesign files when downloading them. Your mileage may wary…​
Different areas of the screen and their role
Navigator - Report Builder

This is where you should find the .rptdesign files you downloaded.

Data Explorer

The Data Explorer defaults to the right of your screen. It gives you access to two things. The data fields available for the report, and the filter fields that can be used for this report.

Palette

The palette provides the various tools you can insert in the report. Simple text, image, table of data, layout table, graph, aggregation, etc. All objects are added to the report by drag & drop.

Tabs

At the right bottom of the window is a series of five tabs.

We will use two:

Layout, which will allow most of the design.

Master Page, which will give access by its owners to standard parameters such as the orientation or size of the report.

The preview is not accessible because it can not be executed outside of OFBiz. Any changes to the scripts will be erased during the upload in OFBiz.

Simple design without break

The simplest possible design is to insert in a table (table in the palette), a part or all of the data set data fields. To do this, right-click on Data Set in the Data Explorer -> Insert in Layout, and then select the fields you want to see appear.

Simple design with break

A break is a collection of data made by Birt from the data. It permits to classify according to a field, and to give details for each category, then to aggregate certain fields, etc.

Insert a table (Table) in the report -> OK

Right-click on the table -> Edit Data Binding, select all fields

In the data set field, change "None" in "Data Set", validate

Right-click the table -> Insert Group. Configure your group, eg: 

Your table then has five lines:

A global title line

A title line of the group

A group detail line

A footer of the group

A global footer line

Then insert some elements in the design: in the global header, everything that does not depend on the group, for example the title of the report. In the header of the group, everything that is common to the whole group and that you want to see in its title. In the details, the fields that may appear for each group line. As in the image below, the fields might be inserted by Copy/Paste from the Data Set, and titles via a text element of the palette. You can add lines and columns by right clicking on the end of the line (gray rectangle when the table is selected), etc.

Construction of aggregation

The aggregations may be on the whole table, or only on a group. They are characterized by an expression to aggregate (made up of different data fields), a possible filter on the data lines, and an aggregation function, eg:

Expression builder

The fx (for expression and filter) buttons are used to open a complex expression construction window. It is possible to use predefined functions, Javascript, data fields, already built aggregations, and so on. This window can also be used by including a data element, which allows to construct non-aggregated data expressions.

Footer lines often allow you to place aggregations, such as sums on the group or table rows, eg

	any unused line must be deleted, otherwise it generates white spaces on the report.
Layout Management
General settings

Right button leads to Properties Editor tab at bottom. Then click on the Master Page tab, just above. In the Property Editor you will see a series of general properties that will allow you to modify the general form of the report.

Styles

By right-clicking on any item in the table, you have access to the menu of styles. From there they can be edited, applied, created. A style can be applied to the whole picture, to a row or column, to a cell, or to an element in that cell (text, data, …​).

18.2.3. Report master creation
Introduction
	this feature will be officially available with the R17.12 branch first release

A report master is an OFBiz content which allows a user to generate data reports. It defines data connexion, and a general filtering form for data. It can be based on an entity, a dedicated service, or in a wider sense on any shape a data connexion can take and return back a map.

Pre-requisite

OFBiz

Birt plugin

Report Master based on an entity/view

Create or choice a database entity or view

Create the general filtering form within the file plugins/birt/widget/birt/BirtMasterForms.xml. The only informations to be changed are entity-name and form name.

    <form name="CTNT_MASTER_EXAMPLE" type="single" extends="AbstractFlexibleReportSearchForm">
        <auto-fields-entity entity-name="Example" default-field-type="find"/>
    </form>

Add the informations about this Master in the database using the file plugins/birt/data/BirtMasterData.xml

    <DataResource dataResourceId="DR_MASTER_EXAMPLE" dataResourceTypeId="ELECTRONIC_TEXT" dataTemplateTypeId="FORM_COMBINED" />
    <ElectronicText dataResourceId="DR_MASTER_EXAMPLE">
        <textData><![CDATA[<!--default domain form-->
            <form name="${masterContentId}_${contentId}" type="single" extends="${masterContentId}" extends-    resource="component://birt/widget/birt/BirtMasterForms.xml">
            </form>]]>
        </textData>
    </ElectronicText>
    <Content contentId="CTNT_MASTER_EXAMPLE" contentTypeId="REPORT_MASTER"  dataResourceId="DR_MASTER_EXAMPLE" statusId="CTNT_PUBLISHED" contentName="Example" description="Master Content for Example" />
    <!-- Data retrieval will be done using perform find on entity Example-->
    <ContentAttribute contentId="CTNT_MASTER_EXAMPLE" attrName="Entity" attrValue="Example"/>

The form in the database is the form that will allow users to change form parameters. You can add any field you desire. Some field names are though reserved: reportContentId, overrideFilters, entityViewName, birtContentType.

Add in the file content/config/contentEntityLabels.xml the Property that will allow translation for your report master description.

    <property key="Content.description.CTNT_MASTER_EXAMPLE">
        <value xml:lang="en">Example</value>
        <value xml:lang="fr">Exemple</value>
    </property>

Your Report Master is created ! You can now create reports using it.

Report Master based on a service

In plugins/birt/src/main/java/org/apache/ofbiz/birt/flexible/BirtMasterReportServices.java there is 2 sets of dedicated services (see examples there)

In each set the first service, will return 4 items:

an object of type Map<String, String> called dataMap.

Keys: data field names.

Values: data types (OFBiz types).

an object of type Map<String, String> called fieldDisplayLabels.

Keys: data field names.

Values: the names displayed to the user.

This output is optional, should it be missing, the keys will be displayed.

an object of type Map<String, String> called filterMap.

Keys: data filtering field names (exact names used for the form fields).

Values: data type (OFBiz type).

This output is optional, if missing, filters can not be displayed on the report.

an object of type Map<String, String> called filterDisplayLabels.

Keys: data filtering field names (exact names used for the form fields).

Values: names to be displayed to the user.

This output is optional, should it be missing, the keys will be displayed.

The second service will actually get the data. It receives an object (Object type) called reportContext.
From this object, you can obtain the map parameters using the following code:

    Map<String, Object> parameters = UtilGenerics.checkMap(reportContext.getParameterValue("parameters"));

This Map will give access fields of the filtering form.
This service will return a list of type List<GenericValue>, containing the data.
A Map<String, Object> would also do.

Then,

create the parent form in the file plugins/birt/widget/birt/BirtMasterForms.xml. Field names created here must be the names used on the Map parameters of the previous service, and also corresponding to the map filterMap.

    <form name="CTNT_MASTER_TURNOVER" type="single" extends="AbstractFlexibleReportSearchForm">
        <field name="fromDate"><date-time type="date"/></field>
        <field name="thruDate"><date-time type="date"/></field>
        <field name="productCategoryId"><lookup target-form-name="LookupProductCategory"/></field>
        <field name="productStoreId"><lookup target-form-name="LookupProductStore"/></field>
    </form>

Create the master in database following.

    <CustomMethod customMethodId="CM_FB_TURNOVER" customMethodTypeId="FLEXIBLE_BIRT" customMethodName="flexibleReportTurnOver" description="service to resolve invoice for turnover report domain"/>
    <DataResource dataResourceId="DR_MASTER_TURNOVER" dataResourceTypeId="ELECTRONIC_TEXT" dataTemplateTypeId="FORM_COMBINED" />
    <ElectronicText dataResourceId="DR_MASTER_TURNOVER">
        <textData><![CDATA[<!--default domain form-->
            <form name="${masterContentId}_${contentId}" type="single" extends="${masterContentId}" extends-resource="component://birt/widget/birt/BirtMasterForms.xml">
            </form>]]>
        </textData>
    </ElectronicText>
    <Content contentId="CTNT_MASTER_TURNOVER" customMethodId="CM_FB_TURNOVER" contentTypeId="REPORT_MASTER" dataResourceId="DR_MASTER_TURNOVER" statusId="CTNT_PUBLISHED" contentName="Turnover" description="Master Content for TURNOVER domain" />
    <!-- Data retrieval will be done using two service calls. First the contentAttribute Service gives the service that will define which data and label will be retrieved,
    and which filter and label are supported by the report design (default value will call the second service with "prepareField" suffix).
    Second, the custom method gives the service to retrieve all data in the report design.
    Here : flexibleReportTurnOverPrepareFields (customMethodName + "prepareFields") then flexibleReportTurnOver-->
    <ContentAttribute contentId="CTNT_MASTER_TURNOVER" attrName="Service" attrValue="default"/>

The form in the database is the form that will allow users to change form parameters. You can add any field you desire. Some field names are reserved: reportContentId, overrideFilters, entityViewName, birtContentType.

Import these data in the base using Webtools XML import (or the longer "gradlew 'ofbiz -l readers=seed,ext' command).

Add in the file content/config/contentEntityLabels.xml the Property which will translate your report Master description.

    <property key="Content.description.CTNT_MASTER_TURNOVER">
        <value xml:lang="en">Turnover (product)</value>
        <value xml:lang="fr">Rotation (des stocks)</value>
    </property>
Entities diagram

The following diagram shows the Entities linked with Content to store report_master/report.

18.3. User documentation
18.3.1. Using a flexible report
Introduction
	this feature will be officially available with the R17.12 branch first release

A flexible report is an OFBiz content of FLEXIBLE_REPORT type which allows the final user to obtain reports using the Birt reporting module. It will be produced at a specific time of your choosing, with your chosen output format, filtering the data with a few parameters defined during report design creation.

Pre-requisite

OFBiz

The Birt plugin

Pre-published reports created from report masters

Using the report

go to the Birt component or to another page harboring reports.

In the Birt component, click "Use a report".

Select your report and hit "Send".

The next screen will allow you to filter your data through a set of pre-defined criteria. Should you leave it empty, you will retrieve unfiltered data.

Select the desired export format

Upon validation, your report is now loaded and can be saved.

18.4. BIRT in OFbiz User Interface

Welcome to OFBiz BIRT component.
The part installed within OFBiz allows you to run the reports which are prepared using Eclipse with the BIRT plugin installed.

This is a short document to help you get started using BIRT to make a report.

As a demo we have prepared a an example report.
Look at the Eclipse BIRT web site for more information.

There is also a new feature (2017) which allows you to dynamically create Birt reports, and allow your users to customise them: the OFBiz Flexible Reports.

18.4.1. PDF tab

When you click on this tab. It will render the example report in a PDF format

18.4.2. Send any format through Mail tab

When you click on this tab. It will show a form that can send the report per email.

18.4.3. Chart tab

When you click on this tab. An example chart will render in a PDF format

18.4.4. Examine the Example Report

The example report design that run in OFBiz is in the file component://birt/webapp/birt/report/example.rptdesign.

When you have started Eclipse BIRT, open this document.

This report show how a report receives data from OFBiz through Scripted Data Source using the OFBiz delegator.
This report has the scripted data source name "OFBiz" and the data set that use the script data source name is called "Product". Open the script editor for Product data set, it uses the delegator object query data from the Product entity. A report that runs on the OFBiz platform can use the delegator object, dispatcher object, security object and classpath of OFBiz environment in the script.

18.4.5. How do I send parameter to report?

If a report is to be rendered through a view map, you can send a parameter through attribute of the request object, the attribute’s name is "birtParameters" which is a map.

If a report is to be rendered through an e-mail, you can send the parameter through the service’s parameter name called birtParameters.

18.4.6. Which are the supported content types?

Excel (.xls)

Excel (.xlsx)

LibreOffice Calc (.ods)

LibreOffice Impress (.odp)

LibreOffice Writer (.odt)

Pdf (.pdf)

Postscript (.ps)

Powerpoint (.ppt)

Powerpoint (.pptx)

Text (.html)

Word (.doc)

Word (.docx)

19. The Ebay Component

The Ebay component provides an interface to the Ebay website.

It is possible to export products from your store into eBay category also import an orders from ebay.

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-intro.adoc[leveloffset=+1]

19.1. main Features

Ebay configurations for ofbiz intregrate with ebay.

Setup shipping methods.

Export products into ebay categories.

Export products into ebay categories.

Import transactions from ebay

Import orders from ebay

19.2. Ebay management in User Interface

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-configurations.adoc[leveloffset=+2]

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-search-product.adoc[leveloffset=+2]

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-filter-result-search-product.adoc[leveloffset=+2]

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-import-orders.adoc[leveloffset=+2]

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-import-single-transaction.adoc[leveloffset=+2]

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-export-to-ebay.adoc[leveloffset=+2]

Unresolved directive in plugins/ebay/src/docs/asciidoc/ebay.adoc - include::plugins/ebay/src/docs/asciidoc/_include/ebay-ShippingMethods.adoc[leveloffset=+2]

20. Ebay Store

The Ebay Store component provides an interface to the Ebay website.
It’s desactivate in the default configuration.

It is possible to export products from your store into eBay category also import an orders from ebay.

20.1. Ebay Store management in User Interface
20.1.1. Ebay Store main screen.

This screen allows the user to access to ebay store by using their account and you can set up and manage your ebay store in ofbiz.

Before you take action on this function, you should already have an ebay store and ebay account on the ebay site because ebay does not allow to create a store from third party site.

How to start ebay store in ofbiz?

Register with ebay developer site to obtain keys and certificate (eBayExport.devId,eBayExport.appId,eBayExport.cerId and eBayExport.token etc.) at Join with ebay developers

Press 'New Ebay Account' button to create your ebay account in ofbiz. After you have created ,the system will generate new product store in ofbiz which link to ebay store. (note :An ebay account in ofbiz use for access to your ebay store on the ebay site)

Put your keys in Ebay Configurations Tab.

How to connect to your ebay store?

Go to 'Ebay Accounts' section select your account then press 'submit' button,the system will show functions.

20.1.2. New Ebay Account.

This screen allows the user to add new ebay account for access to using their ebay store.

Fields Description :

Enter 'Salutation' (ex:Mr,miss,Missis)

Enter 'First Name' (ex:Demo)

Enter 'Middle Name'

Enter 'Last Name' (ex: DemoLastName)

Enter 'Gender'

Enter 'User Login Id' (ex:exbaySandBox123) which you registered on ebay

Enter 'Current Password' the same which you registered on ebay

Press the 'Create' button.

	Go to Party module → Search your party → then you can update your profiles
20.1.3. Ebay Store Detail screen.

This screen allows the user to manage store display setting (store detail, theme, and font color,logo etc.). You can setting in this screen and submit the system will sent your setting to your ebay store and store will update detail.

Fields Description :

Store Name(define 35 charactors)

Store Descrption(define 300 charactors)

Store Url

Store Logo Url(enter your company logo are located at the following URL..)

All of your Store’s pages will appear with the theme you choose, On ebay there are two basic types of themes to choose from.

Store Advanced Theme (This is predesigned themes offer professionally designed background graphics and color combinations.
Use one of these if you want to save time on creating an appealing, consistent look for your Store)

Store Advanced Theme Color

Store Basic Theme(Easily Customizable themes lend themselves to creating a more custom look.
Use one of these if you’d prefer to have more control over the colors in your store)

See example layout on ebay

Primary Color

Secondary Color

Accent Color

Store Name(Font,Size and Color)

Store Title(Font,Size and Color)

Store Description(Font,Size and Color)

Header Display


Select No, do not include additional information in the header,


Select Yes, include additional information in the header. (Enter in text area below))

Select the eBay header style

Item List Display

Item Sort

Store Merch Display

Subscription Level

Press 'submit' to submit data to your ebay store site

20.1.4. Export categories to ebay store screen.

The screen allow user to export categories and product to eBay store.

First you should select catalog and click on Export to eBay store button to complete function.
When you click Export to eBay store button, this function will add your categories that in catalog selected to eBay store also add product to categories too.

20.1.5. EBay Leave Feedback.

This screen have 3 tab button All, bought, sold.

"All" = bought and sold,

"bought" = this account is buyer,

"sold" = this account is seller.

All item in the list can leave message to buyer and seller multi action that mean each item is seperated.

If item is bought it have 3 options to select and then when select "Positive", "Neutral" and "Negative" a rating section appear:

add rating to seller, and comment,

if select "I’ll leave Feedback later" a rating section disappear.

If item is sold it have 2 options to select and then when select "Positive" a comment box appear to add comment text to buyer,
if select "I’ll leave Feedback later" this comment box will disappear.

	If you don’t add comment in text box, leave feedback don’t send.
20.1.6. EBay Feedback.
Items Awaiting Feedback

This section list Items, they are sold or bought and have link to Leave Feedback screen.

This list you can see itemId, title, user and link to leave feedback to buyer or seller. See more info

Recent Feedback

This section list recent feedback message from commentator (buyer) who do transaction with this account.

20.1.7. Ebay Store Auto-Setting

This section contains all Auto setting of specify Account.

20.1.8. Automation Re-list Items

Automation Re-list Items is setting when items are sold or quantity empty or don’t active and then auto re-listing those items.

Start Date have to start before today or finish date. Format: yyyy-MM-dd HH:mm:ss.SSS"

Finish Date have to is after start date. Format: yyyy-MM-dd HH:mm:ss.SSS"

	If you don’t set finish date Automation Re-list continue to do.
20.1.9. Handle Ebay Product Inventory.

This screen allows the user to manage reserve products from ofbiz inventory to their ebay store and then user can use this screen to upload that products into ebay product inventory on ebay site following an ebay account.

In this screen user can manage their ebay store inventory from ofbiz, the screen will show status of product on ebay product inventory (Product Avialabel to list, active, sold, unsold and scheduled

This function used for :

Handle ofbiz inventory and ebay product inventory follow an ebay account

Reserve product from ofbiz inventory

Upload product to ebay product inventory

Show status of product(QTY, Avialable to listing, scheduled, sold, unsold and active listing)

Show Quantity of product

How to go to reserve product?

Go to inventory Details section.

Press on "Reserve product inventory" button

The system will show reserve product screen

How to update inventoy and status on ebay site?

Go to inventory Details section.

Press on "Update to ebay inventory" button

The system will update product and qty to ebay inventory on ebay site

Fields Description :

ProductId (productId in ofbiz catalog)

ProductName (Name of product)

Qty Reserved (Quantity of product that user reserved from ofbiz inventory)

Available To Promise Listing (Quantity of product that user can use create listing)

Ebay Product Id
(this field used for keep productId from ebay inventory because Ebay site not allow user to create productId to their system)

Active Listing (Quantity of product that user can use create listing)

sold (Quantity of product that sold)

un Sold (Quantity of product that still un sold)

reserved date

Note: The user can not create ebay listing and sell product on ebay site greater than amount they made a reservation only.

Notes :

Please subscribed to Selling Manager Pro before you use this function because ebay product inventory will open when you start selling manager pro on ebay site

To subscribe for production site

To upgrade store level for sandbox site (The normal level for sandbox store is basic, the user should upgrade to premium when you want to use inventory function with ebay sandbox.)

How to upgrade sandbox store level?

Click on the link "To upgrade store level for sandbox site"

Go to "Selling Related links" section

Click on "Edit my eBay store"

Page Manage my eBay store will show up

Go to "Store Usage Information" section

Click upgrade at "Subscription level" then select "Premium Store" and "Selling Manager Pro" submit.

20.1.10. Reserve Product From Ofbiz Inventory.

This screen allows the user to reserve products from ofbiz inventory for create listing and sell on ebay site.

How to reserve product?

Go to Reserve Product section

Enter field productId (Click "look up" to find product or type in text the system will show list of product)

Enter quantity of product you want to reserve.

Press "" button

20.1.11. Block item that out of stock.

The screen allow user to block items that out of stock on eBay inventory.

First you should input your store id and click on Block out of stock button to complete this function.

When you click Block out of stock button, this function will block your items on inventory that quantity is zero.

21. Example Plugin

The Example application will allow you to discover the possibilities to create an application, with a lot of search boxes, lists and many more.

This application could be used to have an example of the bests practices in user interface development in Apache - OFBiz.

Look help for each example screen, help will explain which part of development is used in this case.

For example, if you want to see how you should do to add some help you can look to help files in src/docs/asciisoc/_include/ directory and src/docs/asciisoc/example.adoc both in example component.

21.1. Help file organization

Help is managed by using content component functionality.

Help can be for :

one component or sub-component, access is possible by navigation in help index tree and select it, contentId is associated to HELP_ROOT with contentAssocTypeId="TREE_CHILD" ;

one screen, access is done by help icon in screen (most of time on top), contentId is search on ContentAssoc.mapKey with a value (helpTopic) build with component webSite and uri used to show this screen ;

one portlet, access is done by a link on the portalPages (which contain this portlet) help, link is a showHelp (like for a screen) with helpTopic build with "HELP_" and portletId

one portal page, access is done by help icon if parameters.portalPageId is not empty, contentId is read on PortalPage (or originalPortalPage if exist) and is show on top of portlet list contain on it.

21.2. Development help sub-subject

To have the complete list you should click on index button and look to example tree option, but here is a list of main shortcut :

How is organize The Apache OFBiz documentation system documentation is coming soon.

Documentation / asciidoc guidelines

21.3. UI help for Example

Unresolved directive in plugins/example/src/docs/asciidoc/example.adoc - include::plugins/example/src/docs/asciidoc/_include/example_main.adoc[leveloffset=+2]

22. Apache OFBiz® plugin for REST

This initial implementation helps to expose existing or new OFBiz services as REST. To facilitate this, added a new "action" attribute to service elements that helps to determine how a particular service can be accessed via REST.

22.1. Important URLs

API https://localhost:8443/rest

WADL https://localhost:8443/rest/application.wadl

OpenAPI docs https://localhost:8443/docs/swagger-ui.html

22.2. Endpoints

Once deployed, following URLs can be accessed

GET /rest/services

GET /rest/services/{serviceName}?inParams=<URLEncodedJSON>

POST /rest/services/{serviceName} (For this endpoint, the service in parameters must be part of Request Body)

22.3. Authentication

API is protected by JWT tokens, although other forms of access tokens may be supported in future. An API client must first needs to authenticate itself using Basic Auth using username and password. Username is nothing but OFBiz 'userLogin'. Token can also be generated using Swagger UI.

curl -X POST "https://localhost:8443/rest/auth/token" -H "accept: application/json" -H "Authorization: Basic YWRtaW46b2ZiaXo="

If successfully validated, generated token should be received in response

{
  "statusCode": 200,
  "statusDescription": "OK",
  "successMessage": "Token granted.",
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyTG9naW5JZCI6ImFkbWluIiwiaXNzIjoiQXBhY2hlT0ZCaXoiLCJleHAiOjE1OTY3MDk4MjAsImlhdCI6MTU5NjcwODAyMH0.9Hj4pkkeQowAMxPLrI_To0WTohxxgVR6FoViyx5HoboTACQZ4iqDyqiIBodkuCVsZwOTPT1RSAQJ0L_oSVMqBA",
    "token_type": "Bearer",
    "expires_in": "1800"
  }
}

Subsequent API calls must use received token using Bearer Authentication scheme as shown below -

GET /rest/services HTTP/1.1
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyTG9naW5JZCI6ImFkbWluIiwiaXNzIjoiQXBhY2hlT0ZCaXoiLCJleHAiOjE1OTY3MDk4MjAsImlhdCI6MTU5NjcwODAyMH0.9Hj4pkkeQowAMxPLrI_To0WTohxxgVR6FoViyx5HoboTACQZ4iqDyqiIBodkuCVsZwOTPT1RSAQJ0L_oSVMqBA
22.4. Example

List All Services (export="true" and verb = "get|post")

GET /rest/services HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJBcGFjaGVPRkJpeiIsImlhdCI6MTU0NzczOTM0OCwiZXhwIjoxNjc5Mjc1MzQ4LCJhdWQiOiJ3d3cuZXhhbXBsZS5jb20iLCJzdWIiOiJqcm9ja2V0QGV4YW1wbGUuY29tIiwiR2l2ZW5OYW1lIjoiSm9obm55IiwiU3VybmFtZSI6IlJvY2tldCIsIkVtYWlsIjoianJvY2tldEBleGFtcGxlLmNvbSIsInVzZXJMb2dpbklkIjoiYWRtaW4iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.fwafgrgpodBJcXxNTQdZknKeWKb3sDOsQrcR2vcRw97FznD6mkE79p10Tu7cqpUx7LiXuROUAnXEgqDice-BSg

Response :

{
  "statusCode" : 200,
  "statusDescription" : "OK",
  "successMessage" : "OK",
  "data" : [ {
    "name" : "findProductById",
    "description" : "Finds productId(s) corresponding to a product reference, productId or a GoodIdentification idValue",
    "link" : {
      "href" : "https://localhost:8443/rest/services/findProductById",
      "rel" : "self",
      "type" : "get"
    }
  }, {
    "name" : "searchProductsByGoodIdentificationValue",
    "description" : "Search Products by Good Identification Value",
    "link" : {
      "href" : "https://localhost:8443/rest/services/searchProductsByGoodIdentificationValue",
      "rel" : "self",
      "type" : "post"
    }
  } ]
}

Call OFBiz service via GET(export="true" and verb = "get|post")

GET /rest/services/findProductById?inParams=%7B%22idToFind%22:%22GZ-1001%22%7D HTTP/1.1 +
Content-Type: application/json +
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJBcGFjaGVPRkJpeiIsImlhdCI6MTU0NzczOTM0OCwiZXhwIjoxNjc5Mjc1MzQ4LCJhdWQiOiJ3d3cuZXhhbXBsZS5jb20iLCJzdWIiOiJqcm9ja2V0QGV4YW1wbGUuY29tIiwiR2l2ZW5OYW1lIjoiSm9obm55IiwiU3VybmFtZSI6IlJvY2tldCIsIkVtYWlsIjoianJvY2tldEBleGFtcGxlLmNvbSIsInVzZXJMb2dpbklkIjoiYWRtaW4iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.fwafgrgpodBJcXxNTQdZknKeWKb3sDOsQrcR2vcRw97FznD6mkE79p10Tu7cqpUx7LiXuROUAnXEgqDice-BSg

Response :

{
  "statusCode" : 200,
  "statusDescription" : "OK",
  "data" : {
    "product" : {
      "createdStamp" : "2020-06-11T15:29:58.182+0000",
      "productName" : "Nan Gizmo",
      "createdByUserLogin" : "admin",
      "productId" : "GZ-1001",
      "taxable" : "Y",
      "primaryProductCategoryId" : "101",
      "createdTxStamp" : "2020-06-11T15:29:57.523+0000",
      "lastUpdatedTxStamp" : "2020-06-11T15:29:57.523+0000",
      "isVirtual" : "N",
      "autoCreateKeywords" : "Y",
      "description" : "Indian style Nan gizmo",
      "chargeShipping" : "Y",
      "internalName" : "Nan Gizmo",
      "lastModifiedByUserLogin" : "admin",
      "lastUpdatedStamp" : "2020-06-11T15:29:58.182+0000",
      "lastModifiedDate" : "2001-05-13T06:30:00.000+0000",
      "productTypeId" : "FINISHED_GOOD",
      "createdDate" : "2001-05-13T06:30:00.000+0000",
      "isVariant" : "N"
    }
  }
}

Call OFBiz Service via POST


POST rest/services/searchProductsByGoodIdentificationValue HTTP/1.1
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJBcGFjaGVPRkJpeiIsImlhdCI6MTU0NzczOTM0OCwiZXhwIjoxNjc5Mjc1MzQ4LCJhdWQiOiJ3d3cuZXhhbXBsZS5jb20iLCJzdWIiOiJqcm9ja2V0QGV4YW1wbGUuY29tIiwiR2l2ZW5OYW1lIjoiSm9obm55IiwiU3VybmFtZSI6IlJvY2tldCIsIkVtYWlsIjoianJvY2tldEBleGFtcGxlLmNvbSIsInVzZXJMb2dpbklkIjoiYWRtaW4iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.fwafgrgpodBJcXxNTQdZknKeWKb3sDOsQrcR2vcRw97FznD6mkE79p10Tu7cqpUx7LiXuROUAnXEgqDice-BSg
{
    "idFragment": "2644"
}

Response


{
  "statusCode" : 200,
  "statusDescription" : "OK",
  "data" : {
    "products" : [ {
      "internalName" : "Round Gizmo",
      "productId" : "GZ-2644",
      "primaryProductCategoryId" : "101",
      "isVariant" : "N",
      "goodIdentificationTypeId" : "INVOICE_EXPORT",
      "idValue" : "GZ-2644-replaced",
      "isVirtual" : "N"
    } ]
  }
}
22.5. Refresh Token Mechanism

The authentication system now supports a refresh token mechanism. This allows clients to obtain a new access_token using a previously issued refresh_token. This improves user experience by reducing frequent authentication prompts. It helps in maintaining seamless user sessions while minimising exposure of credentials, making authentication more efficient and secure.

	

Of course it’s not that simple on the security side. Because a refresh_token can be stolen! This is well explained by this auth0.com article.

To preserve security auth0 is using a rotation mechanism that sounds like a wise solution. This is not implement OOTB in OFBiz, so you might implement it or possibly use auth0 for that.

The idea is to have short term refresh tokens replaced each time a refresh token is called. Here is an Auth0 article excerpt:

	

With refresh token rotation enabled in the Auth0 Dashboard, every time an application exchanges a refresh token to get a new access token, a new refresh token is also returned. Therefore, you no longer have a long-lived refresh token that, if compromised, could provide illegitimate access to resources. As refresh tokens are continually exchanged and invalidated, the threat is reduced.

The complete process is explained simply but well here. A priori, this would be while calling AuthenticationResource::refreshToken. BTW this allows to store refresh tokens in local storage, which is quite safe.

22.5.1. Login API Enhancement

This said, upon successful login, the response includes both access_token and refresh_token.

Response Example
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "dGhpc19pc19hX3JlZnJlc2hfdG9rZW4..."
}
22.5.2. Get Access Token Using Refresh Token

A new endpoint has been introduced to obtain a new access_token using a valid refresh_token.

URL: POST https://localhost:8443/rest/auth/refresh-token

Request

The request should contain the refresh_token in the body.

Request Example
{
  "Refresh-Token": "dGhpc19pc19hX3JlZnJlc2hfdG9rZW4..."
}
Response

If the refresh token is valid, a new access_token is returned.

Response Example
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
Errors

401 Unauthorized: If the provided refresh token is missing, expired, or invalid.

General Glossary

This glossary is intended to help beginners with OFBiz terms and concepts.
Some of them come from the Data Model Resource Book some are OFBiz specific.

Application

for end users , an application is a top level menu entry, it’s for managing a business object: order, accounting GL, accounting AP, facility, project, …​.
An application can be dedicated for a specifics business and can use part of other applications.
With Apache OFBiz OOTB (Out Of The Box) you will find the main application (the Core Application) and with OFBIZ plugins you can find application more business specifics.

technicaly , an application is a part of Component beginning with the ~webapp directory.
A single component may contain several applications each mounted on a unique URL. Within each component, the "ofbiz-component.xml" file defines the available applications and how those applications shall be mounted on URLs.

Component

for end users , an OFBiz component, is an application or a group of applications.
Knowing which component is used by a application can be useful for "key users" to be able to set application parameters or modify configuration files.

technically , An OFBiz component is a directory used by the OFBiz framework to specify and load application server resources necessary to execute an OFBiz instance.
Each OFBiz component must have a unique name (typically the name of the root directory for the component) and a configuration file called: "ofbiz-component.xml".
Component resources may include, but are not limited to:

webapps,

Java source/classes,

classpath resources,

scripts, entity definitions,

entity data files,

service definitions,

service and entity ECA rules,

test suites,

encryption keystores.

A component contains applications and/or the lower level tools and definitions needed by applications.
A component can be used for self-contained extensions, including applications and logic/data modifications, to the suite of tools and applications that come with OFBiz.
For more detail look at developer-manual.

core application components

The core applications in Apache OFBiz are web applications that serve common business needs found in most enterprises.
They are included in the ofbiz-framework and each one has one (or more) menu entry.
Currently there are :

Accounting,
menu entries: Accounting, Accounting-AP, Accounting-AR

Catalog, to manage products, prices, promotion rules, categories, catalogs, stores and more.
menu entry: Catalog

Content Management,

Facility: Wharehouse management, to manage facilities, inventory, physical inventory, in and out shipment, and more.
menu entry: Facility

Human Resources management,
menu entry: HR

Manufacturing: Materials Resource Planning, define production schemas and tasks, Bill of Materials, Equipment allocation, Workers assignment, Job Shop

Marketing: Marketing Communications Management and Sales Force Automation
menu entry: Marketing, SFA

Order: Fully featured sales and purchase order management module, including

request

requirements

quote

order

statistics

Party, enables organizations to maintain parties (human and other legal entities), their roles and user accounts, and lots more.

Work Effort Management, to manage work efforts, tasks, calendar, maintenance assignments and more.

With these core applications multiple others can be build. In ofbiz-plugin you can find some.

CRM

Customer Relationship Management

Demo Data

Demo data are loaded with the command gradlew loadAll or gradlew "ofbiz --load-data readers=dDemo"

Demo data are present to help understanding ofbiz application process, most of the time it’s only the minimum of data, For a correct understanding, it’s necessary to create more data to have a full functionnal OFBiz.

E-Commerce

The buying and selling of goods or services over electronic systems.

Entity

An entity represents an important business concept that is stored as a record in the database. It is used in the document and OFBiz to generalize about the behavior of persistent information. For example employees and employments are important business concepts for HR application, stored in the database. We could refer to an action directly on a particular entity by saying "Create a new employee" or "Create a new employment". We could alternately describe a general create action by saying "Create a new entity".

Entity Data Maintenance

It’s a sub-application of WebTool application, it’s necessary to have specifics authorization to access it.
Use Entity Data Maintenance to search, look, create, update and delete entities data, most of time it’s really not the good solution to use it for other think that only looking data.
Exceptions are

when there was a bug and it’s necessary to manually do a data correction

manage entities, which have’nt a user interface, main example are for StatusType, Enumeration, but there are some type entities, like BenefitType for HR.


	For creation, as Primary keys must be entered manually apply the ID general advice.
In ID only standard characters and without space are authorized. ID length must be less than 20 characters.
Generally manual primary keys are all upper case with underscores between words and are a meaningful mnemonic i.e. A_PRIMARY_KEY.
ERP

An acronym for Enterprise Resource Planning, an ERP is basically a category of software used for managing a business. It is often a package containing several individual, but integrated, applications. Some of those applications might be Accounts Receivable, Accounts Payable, General Ledger, or Point of Sale.

	Example of ERP: Apache OFBiz, OpenBravo, Odoo
Internal Organization

An Internal organization is a special term in OFBiz that allows you to flag the main accounting company that is being setup.
It can also be used to highlight relationship between a party group (any of your departments, business units or subsidiaries.) and your company.
This relationship is used to filter party groups as being part of your company to distinguish them from other groups which are external. For example your marketing department is an internal organization while a suppliers sales department is not.

MRP

Material Requirements Planning

Party

User, person, organization or other entity (where entity is not an OFBiz "Entity" but rather entity in the legal sense) implied in at least one process modeled and implemented by OFBiz.
Party is a term used to simplify collecting information that used in a common manner by different people and things.
The most common party types are people and groups.
Both people and groups have contact information.
A party is identified by a unique Party Id. Using this Id OFBiz can collect and find contact (and other information and processes) for both people and groups in the same way. This is why you will often see Party Id as a field in a form or a filter as you work in OFBiz.

	Example of party: a administrator of the website; a company dealing goods and/or services via the website; an OFBiz customer assigned a unique party identifier, etc.
Party Id

The unique identifier for a party.
The id is stored as text so in some cases you will see an id that helps you identify the party it is linked to (e.g. Party Id DemoEmployee, or DemoSupplier).
In other cases the Id is created by OFBiz and is will be simply a number from a sequence(by default it starts from the sequence 10000).
In either case the Id is unique.

SCM

Supply Chain Management

1. silverston-data-model, Silverston Data Model Resource Companion Site
Version trunk
Last updated 2025-09-19 11:15:37 UTC
