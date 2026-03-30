# Source: https://docs.startree.ai/corecapabilities/visualize_data/connect-tableau-to-startree-cloud.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Tableau to StarTree Cloud

> Connect either Tableau Desktop or Tableau Server to your StarTree Cloud instance.

## Prerequisites

* JDBC driver (JAR file)
* Tableau connector (TACO file)
* An API Token (see [Generating an API Token](../security/manage-api-tokens#generating-an-api-token))

## Install the Apache Pinot Driver

1. Build or download the **JDBC driver**.\
   You can build the driver from the [source code](https://github.com/apache/pinot/tree/master/pinot-clients/pinot-jdbc-client) or you can [download](https://repo1.maven.org/maven2/org/apache/pinot/pinot-jdbc-client/) one that is already built. In either case, you must use the shaded jar, which will have a filename that includes `shaded`, as in `pinot-jdbc-client-1.0.0-shaded.jar`.
2. Copy the JDBC driver JAR to the Tableau drivers directory.
   * On Mac: `~/Library/Tableau/Drivers/`
   * On Windows: `C:\Program Files\Tableau\Drivers`
3. Download the **StarTree Tableau Connector** TACO file from the [Tableau Exchange](https://exchange.tableau.com/products/1033), and copy it to the connectors directory.
   * On Mac: `/Users/[user]/Documents/My Tableau Repository/Connectors`
   * On Windows: `C:\Users\[user]\Documents\My Tableau Repository\Connectors`

<Info>
  You can skip this step if the `Apache Pinot by Startree` connector is already installed (see step 2 below).
</Info>

1. Launch Tableau.

## Connect Tableau to Apache Pinot

1. On the left side panel, under the **To a Server** section, click the **More...** button.
2. Click on the Apache Pinot by StarTree connector.
   <img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/visualize_data/images/tableau_connector_ui.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=59d70c8003f7e68f9eba9eb289d0385f" alt="Tableau Connectors" width="2358" height="1940" data-path="corecapabilities/visualize_data/images/tableau_connector_ui.png" />
3. Configure the connection to Pinot:\
   a. **Controller Host:** Enter the URL to your Pinot cluster, in the form of `pinot.<env-id>.<org-id>.startree.cloud`\
   b. **Port:** This would typically be `9000` or `443`\
   c. **Authentication:** Leave this set to `None` (we will handle authentication in the ‘Advanced’ tab).

   <img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/visualize_data/images/tableau_connector_dialog.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=27e942547cc5df8ae21c12e057043d2a" alt="Apache Pinot Connection Dialog" className="mx-auto" style={{ width:"73%" }} width="502" height="409" data-path="corecapabilities/visualize_data/images/tableau_connector_dialog.png" />

   d. Click on the **Advanced** tab.\
   e. Set the **Scheme** to HTTPS.\
   f. Enable TLS for Controller and Brokers.\
   g. Using the API token that you obtained in the prerequisites, enter `headers.Authorization=Bearer <your token>` in the **Additional Properties** text box (e.g. `headers.Authorization=Bearer st-N5zM7kPqW8xR3aVb-H1gJ4fD6sA9zX2cC5vB8nL0kM7pQ2wE4rT6`).

   <img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/visualize_data/images/tableau_connector_dialog_advanced.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=965533083e0cbc69762d44d0ec67c212" alt="Apache Pinot Connection Dialog" className="mx-auto" style={{ width:"78%" }} width="501" height="459" data-path="corecapabilities/visualize_data/images/tableau_connector_dialog_advanced.png" />

   h. click **Sign In**.
4. Once you are connected, you will be able to see the data from your data source and can begin to query.
   <img src="https://mintcdn.com/startree/xe5mTwlEdZc68KYh/corecapabilities/visualize_data/images/tableau_tables_ui.png?fit=max&auto=format&n=xe5mTwlEdZc68KYh&q=85&s=ce58c37874ac5728c1cbf95bede1eb46" alt="Fetch data from Pinot" width="3548" height="2110" data-path="corecapabilities/visualize_data/images/tableau_tables_ui.png" />

Built with [Mintlify](https://mintlify.com).
