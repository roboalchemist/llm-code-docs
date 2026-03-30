# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/data_manager_basics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Manager Basics

> Introduction to Data Manager functionality for creating forms, capturing dashboard interactions and managing user-submitted data.

Data Manager allows you to create forms for users to fill out, and to store that data for retrieval later.  These forms
can even retrieve data-points that users click on in a Tableau Dashboard to be stored alongside the form they submit.
The data from these forms are then stored in Curator's database, where you can later retrieve that data for use in other
dashboards, or even for the same Dashboard itself, providing immediate feedback!

## Data Manager Terminology

When starting with the data manger, it's important to understand core concepts, and thankfully we've made it pretty
simple for you.  Here's a quick mapping to understand the Data Manager components when building a form:

* Data Attribute = Individual Field/Input
* Data Group = Entire Form

or another way to view these is from how the data will be stored in the database:

* Data Attribute = Column
* Data Group = Table

## Enabling Data Manager

If you do not see "Data Manager" as a top-level menu option on the left-hand nav on the backend of Curator, you can
enable it by following these steps:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab
4. In the "Functionality" section ensure the toggle for "Data Manager" is enabled and click the "Save" button.

That's it!  Curious what's under the "Manage Data" section on the left-hand nav?  That's where you can create or edit
existing rows in your Data Groups once they've already been added.

### Creating a Data Attribute

To create a data attribute, you can

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Data Manager** > **Data Attributes** section from the left-hand menu.
3. Click on the **New Attribute** button
4. Fill out the form keeping in mind how you'd like your end user to interact with this field, then click "Save".

#### Creating a Data Group

Once you have created all the data attributes you need for your user form, you can group them all together into a
Data Group for use with Data Manager features like
[Mark Commenting](/embedding_using_analytics/data_manager/mark_commenting).
To create a data group:

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Data Manager** > **Data Groups** section from the left-hand menu.
3. Click on the **New Group** button
4. Check all of the boxes next to the Data Attributes you wish to add to your Data Group then click "Create" or "Save".

## Migrating Data to another Database

If you would like to use a different database to store this data, we recommend using your preferred ETL process to
extract the data out of Curator's MySQL database.  Curator does not support any other databases beyond MySQL.

## Styling Data Manager Forms in Curator

If you would like to customize the background, text, or highlight colors for your data manager forms, you can do update
the colors in **Settings** > **Curator** > **Themes** section from the left-hand menu under the "Pages" tab.
