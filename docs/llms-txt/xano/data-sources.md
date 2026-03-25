# Source: https://docs.xano.com/the-database/database-basics/data-sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Sources

<Info>
  **Quick Summary**

  Data sources are like separate versions of tables that contain different data sets — typically, they are separated into **live** or **production** data, and **test** data. The advantage to using separate data sources is so when you are building or iterating on your backend functionality, your actual live data stays safe. All data sources share the same database schema. They only differ by allowing different copies of the database records.
</Info>

In Xano, data sources are essentially different sets of tables within your application's database. These data sources are crucial because they provide a way to separate the actual, live data that your business relies on from the data you use for testing or development purposes. This separation is beneficial as it ensures that any changes you make while testing new features do not affect the actual operational data.

Data sources typically have two main variants: **live data** and **test data**. You can have as many data sources as you'd like if additional separation makes sense for your backend. Live data is what your application uses in real-time—it’s the actual data that reflects real-world activities. In contrast, test data is used for experimentation and development, allowing developers to try out new features or changes without risking the integrity of the live data. By keeping these data sources distinct, Xano enables businesses to safely innovate and enhance their backend functionality without compromising the data they depend on every day.

## Creating Data Sources

<Steps>
  <Step title="Access your data sources from the left-side navigation menu">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f0e002df-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=db2e11245691b96328148f229afd6739" alt="" width="408" height="206" data-path="images/f0e002df-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Add a new data source from the panel that opens">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/3f0d339f-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=294bb2fa57c1b6a0a9a458cf67ed55b7" alt="" width="508" height="228" data-path="images/3f0d339f-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Customize the new data source">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/cfb50a9d-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=5a2a1893df2f39107eb7bf2882c243aa" alt="" width="508" height="228" data-path="images/cfb50a9d-image.jpeg" />
    </Frame>

    Give it a name, and choose a distinct color to assign to the data source. The color assigned is important, as it is used throughout the Xano interface to remind you of the currently selected data source.

    When you're done, click **Add Data Source**
  </Step>
</Steps>

## Using Data Sources

### Switching Data Sources

When you switch data sources, any action you take in Xano such as running and debugging a function stack will target the selected data source. It is recommended to use a test data source whenever possible to avoid accidentally impacting live application data.

Switch your data source at any time by clicking the data source indicator in the left-side navigation.

<Info>
  This **does not** impact your live application; only the work you are performing inside of Xano.
</Info>

### Setting a Data Source as Active

If you want your backend to use a different data source by default, select it from the data sources panel and choose **Set As Active Data Source**. All future activity, unless otherwise specified using one of the alternative methods below, will use the active data source.

<Warning>
  Proceed with caution. Changing the active data source can have unintended consequences on your live application. You do not need to change the **active data source** to work with other data sources in Xano.
</Warning>

### Targeting Specific Data Sources

When running function stacks in Xano or calling them externally, you can target a specific data source a number of ways. If you do not specify a data source, Xano will use the

<Steps>
  <Step title="Use the Set Data Source function">
    The **Set Data Source** function, located under **Utility Functions**, allows you to manually set a data source at any time. Any future database operations, such as reads and writes, will use the defined data source.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5a6e4cf2-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=38d97a6f40a8a31d312100c16f2d9a36" alt="" width="475" height="228" data-path="images/5a6e4cf2-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Send a data source header in your request">
    If you're calling one of your Xano APIs externally, you can specify the data source to use in the request headers.

    The header to send is as follows. Replace 'test' with the name of the data source you wish to target.

    ```bash  theme={null}
    X-Data-Source: test
    ```
  </Step>

  <Step title="Send a URL argument in your request">
    If you don't have the ability to modify the request headers but still want to specify the data source in an external request, you can use a URL argument.

    ```
    https://x1xx-abcd-efgh.a1.xano.io/api:x123abc/user?x-data-source=test
    ```
  </Step>

  <Step title="Change the settings of the function stack">
    In some function stack types, such as background tasks, you can set the data source to target if you would like it to be different from the live data source.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/kUGpIho8LJSMl5Gv/images/3c3ec9ae-image.jpeg?fit=max&auto=format&n=kUGpIho8LJSMl5Gv&q=85&s=a4bafa3f204643869833d09d7c7dcda5" alt="" width="525" height="225" data-path="images/3c3ec9ae-image.jpeg" />
    </Frame>
  </Step>
</Steps>

### Migrating Data Between Data Sources

<Frame>
  <iframe src="https://demo.arcade.software/OfK50mi7hWjjYeFmvDQC?embed" title="https://demo.arcade.software/OfK50mi7hWjjYeFmvDQC?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" />
</Frame>

<Steps>
  <Step title="Access the Migration panel">
    Click the data sources indicator and choose⚙️\*\* Manage Data Sources\*\*. In the panel that opens, click Migrate.
  </Step>

  <Step title="Select the source and destination data source.">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f398582c-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=6dd3b4874b7e26299584c46bb6c5353c" alt="" width="435" height="214" data-path="images/f398582c-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Select the tables to migrate.">
    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/219d9bbe-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=d5fd524cc8f878b007c239a02a019900" alt="" width="438" height="248" data-path="images/219d9bbe-image.jpeg" />
    </Frame>
  </Step>

  <Step title="Confirm your changes to begin the migration.">
    You can check the progress of the migration via the indicator in the left-hand navigation. You'll also see a banner at the top of the screen once the migration has completed.

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/417a672d-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=0ac2be2bb4574f35e3446832a25a8c00" alt="" width="275" height="138" data-path="images/417a672d-image.jpeg" />
    </Frame>

    <Frame>
            <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d7e074a3-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=3336a2ae2c97a85ebf369143bfba03f6" alt="" width="754" height="131" data-path="images/d7e074a3-image.jpeg" />
    </Frame>
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).