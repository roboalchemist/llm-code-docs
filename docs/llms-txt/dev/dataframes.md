# Source: https://dev.writer.com/agent-builder/dataframes.md

# Build data tables with DataFrames

The [**DataFrame** component](/components/dataframe) lets you display structured data in a table format with built-in features like sorting, searching, and downloading. It's designed to work with [Pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) or [PyArrow tables](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html).

## Overview

DataFrames allow you to present data in a grid format. They provide an interface with built-in features like sorting, searching, and downloading. They work well for displaying lists of records, reports, or any tabular data that you've processed with Python.

### When to use DataFrames

DataFrames are useful for:

* **Data analysis results** from pandas operations
* **CSV file uploads** that need to be displayed as tables
* **Database query results** formatted as DataFrames
* **Any data that benefits from sorting and filtering**
* **Reports that users might want to download as CSV**

## Example: Display a sales report

This example creates a sales report from hardcoded data. It processes data with pandas and displays it in a DataFrame.

<Steps>
  <Step title="Open the Code tab and edit the main.py file">
    Open the **Code** tab at the bottom of the agent's interface and navigate to the `main.py` file.

    Add the following code to the `main.py` file. It creates a pandas DataFrame with the sales data and sets it in the state as `sales_report`.

    ```python  theme={null}
    import pandas as pd
    import writer as wf

    # Sample sales data
    sales_data = [
        {"rep_name": "Sarah Chen", "region": "West", "product": "Software License", "amount": 15000, "quarter": "Q3 2024"},
        {"rep_name": "Mike Rodriguez", "region": "East", "product": "Consulting", "amount": 8500, "quarter": "Q3 2024"},
        {"rep_name": "Alex Johnson", "region": "Central", "product": "Software License", "amount": 22000, "quarter": "Q3 2024"},
        {"rep_name": "Sarah Chen", "region": "West", "product": "Support Package", "amount": 5000, "quarter": "Q3 2024"},
        {"rep_name": "Lisa Park", "region": "East", "product": "Software License", "amount": 18000, "quarter": "Q3 2024"},
        {"rep_name": "Mike Rodriguez", "region": "East", "product": "Consulting", "amount": 12000, "quarter": "Q3 2024"}
    ]

    # Create pandas DataFrame
    df = pd.DataFrame(sales_data)

    # Set the DataFrame in state
    initial_state = wf.init_state({
     "sales_report": df
    })
    ```
  </Step>

  <Step title="Add a DataFrame component to the agent's interface">
    Navigate to the **Interface** tab to build the agent's interface.

    Add a **DataFrame** component to your page. Update the following settings:

    * **Data**: `@{sales_report}`. This is the state variable that contains the sales report data.

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3c6408ed45bdfc6f0c951b4e6bb3a745" alt="" data-og-width="3456" width="3456" data-og-height="1810" height="1810" data-path="images/agent-builder/dataframe-component.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=010957aa52d37b7d880c406f20233c2d 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ab70fa9b7a571c42a5fe686484b8765e 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=2806348ed5a90a6d2eb19f8a185c40b9 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d8dc687b3794e93206d74b14cf87efeb 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=aac70b54a159ea00a201fe1f5fe1d457 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-component.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=3e28c7795a1b68d30d76991aa1eec0e5 2500w" />
  </Step>
</Steps>

### Preview the DataFrame

Navigate to the **Preview** tab to see the DataFrame in action.

You should see a table with columns for sales rep, region, product, amount, and quarter.

Try clicking column headers to sort by amount or region.

### Enable advanced features

Navigate back to the **Interface** tab to click on the DataFrame component. There, you can enable more features, like search, download, and editing or adding records.

1. **Enable Search**: In the DataFrame component settings, set **Enable search** to `yes`
2. **Enable Download**: Set **Enable download** to `yes`
3. **Optionally enable editing**: Set **Enable adding a record** and **Enable updating a record** to `yes` if you want users to modify data
4. **Test the enhanced features**:
   * Search for specific sales reps or regions
   * Sort by amount to see top performers
   * Download the data as CSV for further analysis

## Example: CSV file upload and processing

This example shows how to upload a CSV file and process the data with pandas to then display it in a DataFrame.

The example assumes you have a CSV file with the following columns:

* `product_category`
* `product_name`
* `quantity`
* `unit_price`
* `sales_rep`
* `date`
* `region`

It processes the data to calculate the total revenue for each product category and displays the data in a DataFrame.

Below is an example of the CSV file that you can use to test the agent:

```csv  theme={null}
product_category,product_name,quantity,unit_price,sales_rep,date,region
Software,CRM Pro,2,5000,Sarah Chen,2024-07-15,West
Hardware,Server Rack,1,8000,Mike Rodriguez,2024-07-18,East
Software,Analytics Suite,3,3000,Alex Johnson,2024-07-22,Central
Consulting,Implementation Service,5,1200,Sarah Chen,2024-07-25,West
Hardware,Network Switch,4,2500,Lisa Park,2024-08-02,East
Software,CRM Pro,1,5000,Mike Rodriguez,2024-08-05,East
Consulting,Training Package,8,800,Alex Johnson,2024-08-10,Central
Software,Analytics Suite,2,3000,Sarah Chen,2024-08-12,West
Hardware,Server Rack,2,8000,Lisa Park,2024-08-15,East
Consulting,Implementation Service,3,1200,Mike Rodriguez,2024-08-20,East
Software,CRM Pro,4,5000,Alex Johnson,2024-08-22,Central
Hardware,Network Switch,2,2500,Sarah Chen,2024-08-25,West
```

### Build the interface

Navigate to the **Interface** tab to build the agent's interface.

<Steps>
  <Step title="Add a File input component to allow users to upload the CSV file">
    Add a **File input** component to your page. Update the following settings:

    * **Label**: `Upload CSV`
    * **Allowed file types**: `.csv`
    * **Link variable** under **Binding**: `input_file`
  </Step>

  <Step title="Add a Button component to trigger the file upload">
    Add a **Button** component to your page. Update the following settings:

    * **Label**: `Process CSV`
  </Step>

  <Step title="Add a DataFrame component">
    Add a **DataFrame** component to your page. Update the following settings:

    * **Data**: `@{processed_data}`. This is the state variable that will contain the processed data after you build the blueprint.
  </Step>
</Steps>

The interface should look like this:

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=51f0391060921fd82b873218b1fa4beb" alt="" data-og-width="3456" width="3456" data-og-height="988" height="988" data-path="images/agent-builder/dataframe-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e77b25238e87c8367712aa77ac259212 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=05140d87292349924a26e014472d1699 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=12619ab7007c6c29cdc828b6bca08066 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=2896a253f1ede8101c7f6190a62c5fd9 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b6f705d5bf49b508e2585245a4ac04d9 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-ui.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=60ddcfbce3e9345854bab0fe50f9cb78 2500w" />

### Build the blueprint

Open the **Blueprint** tab to build the agent's blueprint. The blueprint contains:

* A **UI Trigger** that triggers blueprint execution when the user clicks the **Upload CSV** button.
* A **Python** block that processes the uploaded file and stores the data in a state variable.

<Steps>
  <Step title="Add a UI Trigger">
    Add a **UI Trigger** to the blueprint. Update the following settings:

    * **Component Id**: Select the **Process CSV** button you added to the interface.
    * **Event type**: `wf-click`
  </Step>

  <Step title="Add a Python code block">
    Add a **Python code** block to the blueprint. Then paste the following code into the block. The code reads the uploaded file, processes the data, and stores the processed data in a state variable.

    ```python  theme={null}
    import io
    import pandas as pd
    import writer as wf

    if "input_file" in state:
        # Read the uploaded file into a buffer
        file_buffer = io.BytesIO(state["input_file"][0]["data"])
        # Read buffer into pandas DataFrame
        df = pd.read_csv(file_buffer)
        
        # Process the data to calculate the total revenue for each product category
        df['total_revenue'] = df['quantity'] * df['unit_price']
        df = df.groupby('product_category').agg({
            'total_revenue': 'sum',
            'quantity': 'sum'
        }).reset_index()
        
        # Set processed DataFrame in state
        state["processed_data"] = df
    ```
  </Step>
</Steps>

The blueprint should look like this, with the Python block containing the code to process the uploaded file and store the processed data in a state variable.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c1830d131ad072995749c39250a07ad8" alt="" data-og-width="3456" width="3456" data-og-height="1806" height="1806" data-path="images/agent-builder/dataframe-blueprint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=d05b7c047e730d7dd0029302524a0411 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=80b089aeb965d86f4f2cf28a4624cdd8 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=dc9306f0b008242abce5f1ae7e59a0a7 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=e69729aa4263186876f9c555352d4588 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=629d2d4135ed3cbb226cc90e2f3b8b3f 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-blueprint.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c31872f2d5b1cdb4fc3cce4000572992 2500w" />

### Preview the agent

Navigate to the **Preview** tab to see the agent in action. You should see a button to upload a CSV file and a table to display the processed data.

Upload a CSV file; see the [beginning of this example](#example%3A-csv-file-upload-and-processing) for a sample CSV file.

Once you click the **Process CSV** button, the agent processes the data and displays it in the DataFrame component.

<img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7dd43ba5e826d82f79cd737e89d75c3c" alt="" data-og-width="3456" width="3456" data-og-height="1180" height="1180" data-path="images/agent-builder/dataframe-preview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0e2634c88834ed9eff977a1ce02bb19c 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=cd8b6341950431d2a1a82da40f0d5747 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=c4badb0b6901f9305adb84397c22ca18 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=7bd590eb9430ff54a771c4f05030bd51 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=21fce990ddc4973a947dcad675b33c35 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/dataframe-preview.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5990658355f226e0dbe475c537531cd8 2500w" />

## Best practices

1. **Use pandas for data processing**: Clean, aggregate, and transform data before display
2. **Keep DataFrames reasonably sized**: Use "Display row count" to control how many rows show simultaneously
3. **Enable appropriate features**: Only enable editing if users should modify data
4. **Consider text wrapping**: Toggle "Wrap text" based on your data content
5. **Use meaningful column names**: Pandas column names become the table headers

## Next steps

Try extending this example by:

* Adding more sophisticated pandas operations such as `groupby` and `pivot_tables`
* Connecting to real databases or APIs
* Creating calculated columns based on business rules
* Styling the component with custom CSS classes
