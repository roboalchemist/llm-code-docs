# Source: https://docs.curator.interworks.com/embedding_using_analytics/data_manager/creating_a_form.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating a Form

> Build custom data collection forms using Data Manager to gather structured information from users.

First before you continue - take a look at our [Data Manager Basics](/embedding_using_analytics/data_manager/data_manager_basics)
to get familiar with terms and how Data Manager works generally.  Once you've perused that page, check out all the
flexible ways you can add forms and gather important feedback in your Curator site.

## Building your Form

To create a form, simply map all the Attributes you would like your Group to include.  If you're not sure which field
types you'd like your form to contain refer to the "Available Fields" section below.  Once you've created your
attributes, simply collect them into your Data Manager Group to begin placing your form throughout your site.  For
details on how to make your form accessible, refer to the "Accessing the Data Manager Form" section below.

## Available Fields

There are many ways to build a form using Curator's Data manager. Below, you'll find an outline of each field and what
it's used for.

### User-populated fields

There are many flexible options when building a form, and your users may want flexible free-text input or pre-selected
date or dropdown options:

* **Short Text**: A standard user-input text field, typically used for things like first name, last name, and email.

* **Long Text**: A free-form text entry allowing for lengthy input, primarily used when your users will be entering
  one or more sentences into the form.

* **Number**: Short Text input that limits entry to numbers (whole or decimal).

* **URL**: Short Text input that limits the format to a URL.

* **Dropdown**: Create a pre-set list of options for users to select from.

* **Date**: A calendar-date picker allowing users to select a given day.

* **Password**: Short Text input that hides the input for secure browsing (however, the password will not be encrypted
  in the database once stored).

* **Markdown**: A markdown field - renders a markdown text-editor on the backend when inputting new data.  This is
  primarily used when creating documentation.

### Fields populated from other sources

Some other sources within Curator may contain the data you want to populate your form with.  For these
more complex scenarios, you can leverage the following fields:

* **Lookup**: A dropdown that allows you to retrieve the selected options from another data manager group's input.

* **Read-only Field**: Short Text input that users cannot interact with - for use when populating an input using custom
  code.

### Fields populated from other sources: *Tableau mark-commenting only*

When selecting a data-point on a Tableau Dashboard, you can leverage that Dashboard's underlying data to pre-populate the
form that renders in the pop-up modal.  To learn ore about this, refer to the
[Mark Commenting](/embedding_using_analytics/data_manager/mark_commenting)
details.  To utilize the data that resides in your Dashboard to pre-fill dropdown options use these two fields:

* **Tableau Field**: A dropdown field that retrieves the data from the Tableau mark-selection for a given field name and
  populates the possible options when the form is rendered.

* **Tableau Parameter**: A dropdown field that retrieves the data from the Tableau mark-selection for a given parameter
  and populates the possible options when the form is rendered.

## Accessing the Data Manager Form

Once your Data Manager Group has been created, you will need to share the form so users can access it and start adding
their own data in to Curator's data manager storage.  There are four possible ways to access the form you've created
through your Group.

### Default Data Manager Form

Once a Data Manager Group has been created, Curator provides you with a templated page that contains your Data Manager
form - along with an option view of the data depending on the settings you've enabled for your group.

### Adding a Data Manager form to a page

Using Curator's page builder system, you can add a form - with a few different options for layout types - to a page.
Refer to the [Forms](/site_content_design/pages/forms) documentation on how to
add a form to a Page.

### Mark Commenting Pop-up Form

When interacting with a Dashboard, you can show your users a form after they click on a given Tableau data-point.
To learn ore about this, refer to the
[Mark Commenting](/embedding_using_analytics/data_manager/mark_commenting)
document.

### Dashboard Feedback

Curious what your users think about your dashboards?  You can add a single form to incorporate their feedback, gathering
the Dashboard URL automatically and tying it to their form-submission.  For details on Dashboard Feedback
[check out this outline](/embedding_using_analytics/data_manager/dashboard_feedback).
