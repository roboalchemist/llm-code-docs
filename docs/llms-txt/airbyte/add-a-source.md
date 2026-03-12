# Source: https://docs.airbyte.com/platform/using-airbyte/getting-started/add-a-source.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/getting-started/add-a-source.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/getting-started/add-a-source.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/getting-started/add-a-source.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/getting-started/add-a-source.md

# Add a Source

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Setting up a new source in Airbyte is a quick and simple process! When viewing the Airbyte UI, you'll see the main navigation bar on the left side of your screen. Click the **Sources** tab to bring up a list of all available sources.

[Getting Started (Source)](https://demo.arcade.software/k63e0sDIzPWtM0wQjNSC?embed)

You can use the provided search bar, or simply scroll down the list to find the source you want to replicate data from. Let's use a demo source, Faker, as an example. Clicking on the **Sample Data (Faker)** card will bring us to its setup page.

![](/assets/images/getting-started-faker-source-87b415fca0834e51b8f5b6639a6bfdc1.png)

The left half of the page contains a set of fields that you will have to fill out. In the **Source name** field, you can enter a name of your choosing to help you identify this instance of the connector. By default, this will be set to the name of the source (ie, `Sample Data (Faker)`).

Each connector in Airbyte will have its own set of authentication methods and configurable parameters. In the case of Sample Data (Faker), you can adjust the number of records you want returned in your `Users` data, and optionally adjust additional configuration settings. You can always refer to your source's provided setup guide for specific instructions on filling out each field.

info

Some sources will have an **Optional Fields** tab. You can open this tab to view and configure any additional optional parameters that exist for the source, but you do not have to do so to successfully set up the connector.

Once you've filled out all the required fields, click the **Set up source** button and Airbyte will run a check to verify the connection. If you're using the [API](https://reference.airbyte.com/reference/createsource#/) or [Terraform](/platform/1.6/terraform-documentation.md) to manage your infrastructure, click the **Copy JSON** button to copy your configuration as a JSON string that you can paste into your code.

Happy replicating!

Can't find the connectors that you want? Try your hand at easily building one yourself using our [Connector Builder](/platform/1.6/connector-development/connector-builder-ui/overview.md)!
