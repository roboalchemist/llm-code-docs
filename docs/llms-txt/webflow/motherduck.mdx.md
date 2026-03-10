# Source: https://developers.webflow.com/browser/data-exports/destinations/motherduck.mdx

***

title: MotherDuck
slug: data-exports/destinations/motherduck
description: Configure MotherDuck as a destination for Data Exports
-------------------------------------------------------------------

This guide walks you through configuring MotherDuck as a destination for your Webflow Analyze and Optimize data export.

## Configuration steps

<Steps>
  ### Create a database

  Create a new database for data writing. Skip this step if you already have a database prepared.

  1. Log in to the MotherDuck account.
  2. Click the plus icon next to "Attached Databases".
  3. Enter the desired name of your database.

  ### Create an access token

  Collect connection information and create an access token for the data transfer service.

  1. In the navigation dropdown, select **Settings**.

     ![](https://storage.googleapis.com/prequel_docs/images/motherduck-endpoints-navigation.png "navigation.png")

  2. Click the **Create token** button to create an **access token**.

     ![](https://storage.googleapis.com/prequel_docs/images/motherduck-endpoints-settings.png "settings.png")

  3. Name the token with a descriptive comment and assign the token lifetime. A longer lifetime will ensure you do not have to update the token as often. Ensure that the **Token Type** is set to "Read/Write Token". Click **Generate**.

     ![](https://storage.googleapis.com/prequel_docs/images/motherduck-endpoints-create-token.png "create-token.png")

  4. In the pop up that follows, **copy the token** and securely save the token.

  ### Add your destination

  Use the following details to complete the connection setup: **database**, your chosen **schema name**, and **access token**.

  * Instructions for [Analyze / Optimize for Webflow sites](https://help.webflow.com/hc/en-us/articles/49268475823763)
  * Instructions for [Optimize for non-Webflow sites](https://help-optimize.webflow.com/hc/en-us/articles/49271018634899)
</Steps>
