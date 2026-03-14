# Source: https://docs.acceldata.io/documentation/quick-start-guide.md

# Integrate your First Data Source

## Sign Up

Click **Verify Email** in your ADOC Welcome Email -**&gt;** Copy and Enter the **Verification Code** to Set Your Password **-&gt;** **Sign In** to ADOC.

## Connect Data Source

Let’s connect your first data source. Here, we use **Snowflake** to get started with Data Reliability monitoring.

1. From the left main navigation menu, navigate to **Register** -&gt; **Add Data Source -&gt;** select **Snowflake** from the list.

![](https://uploads.developerhub.io/prod/Yoq2/vmwnlj9x0s1adatvky52r31kzxatovn0gvhkk9fx0suhd0wkmy3fhix1zk8kgui3.png)

2. On the **Data Source Basic Details** page, fill in the following:
    1. **Data Source name**: A valid name. For example: `My_Production_Snowflake`.
    2. **Description**: A brief description. For example: `This consists of Snowflake related assets.`
    3. **Enable Data Reliability**: Turn on the **Data Reliability** toggle, and select your data plane.
    4. Click **Next**.

3. On the **Snowflake Connection Details** page that appears, provide your Snowflake user credentials that ADOC can use to monitor your account.
4. Click **Test Connection**. A `Connected` message will appear. In the next window, enter the required warehouse and **databases** available in your Snowflake account. Click **Submit**.
5. In the next window that appears, click '**Start Crawler & Go to Data Sources**'. It will take a few minutes for your data to crawl. After this, you will redirected to **Register** page.

**Congratulations**! You've connected and crawled your data to ADOC.