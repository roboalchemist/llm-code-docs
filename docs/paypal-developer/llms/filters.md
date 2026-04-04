# Create and set up filters

Filters are the rules that decide whether Fraud Protection Advanced (FPA) approves, rejects, or puts a transaction into a review queue.

The **Filters** tab displays customized filters that you can choose to enable or adjust, or you can create your own. You'll also see simulations based on your current filter settings applied to your historical data for a selected time period.

![Create Setup Filter](https://www.paypalobjects.com/devdoc/Create_setup_filter.png)

## Create a new filter

To add a new filter, use the following steps:

1. Select **Add Filter** on the **Filters** tab. A popup window will open.
2. Enter the **Filter Name** and provide a **Description** for the filter. The **Decision Label** will automatically be set to one of the following options based on the type of filter you create: **Approve**, **Reject**, or **Review**.
   ![Create Filter](https://www.paypalobjects.com/devdoc/img/docs/Setup_Filters_Create.png)
3. To add conditions to the filter, select **+Condition** and specify the desired fields. For example, you can specify conditions on transaction attributes or risk scores.
4. Select **Add**. The popup window will close. To apply the filter, you **must** click **Test** and **Save**, else the filter changes will not be saved.
   ![Edit Filter](https://www.paypalobjects.com/devdoc/img/docs/Setup_Filters_CreateTestAndSave.png)

## Enable customized filters

To enable customized filters, use the following steps:

1. On the **Filters** tab, locate the filter you want to enable, then select the pencil icon in the **Actions** column. This will open the filter configuration in a popup window for editing.
   ![Enable Custom Filters](https://www.paypalobjects.com/devdoc/Enable_Cust_Filters.png)
2. Toggle the Status to **On** then select **Change** button. The popup window will close. To apply the change, you **must** select **Save** and then confirm your changes.
   ![Edit Custom Filters](https://www.paypalobjects.com/devdoc/img/docs/Setup_Filters_EditFilter.png)
   ![Confirm Custom Filters](https://www.paypalobjects.com/devdoc/img/docs/Setup_Filters_EditTestAndSave.png)

## Edit filters

- Select the pencil icon available in the **Actions** column for each filter. The filter configuration will open in a popup window, where you can make changes to the filter. Once done, select **Change**. The pop-up window will close.
   ![Edit Filter](https://www.paypalobjects.com/devdoc/img/docs/Edit_filter.png)
- To apply the change, you **must** select **Save** and then confirm your changes. If you don’t select **Save**, your changes will not be saved as indicated in the message shown in the following screenshot.
   ![Email Address Filter](https://www.paypalobjects.com/devdoc/img/docs/Email_address_filter.png)
   ![Confirm Filter](https://www.paypalobjects.com/devdoc/img/docs/Confirm_filter.png)