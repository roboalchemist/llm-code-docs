# Source: https://docs.datafold.com/data-monitoring/monitors/data-test-monitors.md

# Data Test Monitors

> Data Tests validate your data against off-the-shelf checks or custom business rules.

Data Test monitors allow you to validate your data using off-the-shelf checks for non-null or unique values, numeric ranges, accepted values, referential integrity, and more. Custom tests let you write custom SQL queries to validate your own business rules.

Think of Data Tests as pass/fail—either a test returns no records (pass) or it returns at least one record (fail). Failed records are viewable in the app, materialized to a temporary table in your warehouse, and can even be [attached to notifications as a CSV](/data-monitoring/monitors/data-test-monitors#attach-csvs-to-notifications).

## Create a Data Test monitor

There are two ways to create a Data Test monitor:

1. Open the **Monitors** page, select **Create new monitor**, and then choose **Data Test**.
2. Clone an existing Data Test monitor by clicking **Actions** and then **Clone**. This will pre-fill the form with the existing monitor configuration.

## Set up your monitor

Select your data connection, then choose whether you'd like to use a [Standard](/data-monitoring/monitors/data-test-monitors#standard-data-tests) or [Custom](/data-monitoring/monitors/data-test-monitors#custom-data-tests) test.

### Standard Data Tests

Standard tests allow you to validate your data against off-the-shelf checks for non-null or unique values, numeric ranges, accepted values, referential integrity, and more.

After choosing your data connection, select **Standard** and the specific test that you'd like to run. If you don't see the test you're looking for, you can always write a [Custom test](/data-monitoring/monitors/data-test-monitors#custom-data-tests).

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=6b3e4ff63c23d378a1afa1b9f5333e12" data-og-width="1182" width="1182" data-og-height="646" height="646" data-path="images/monitors/standard_data_test_types.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a346f265b2fb277ccb5a81594e066b2b 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=16a80272596a95655accea963760bec0 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d423caaacff78f3591f7b641fec1773e 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=d82c4d294e0289df2ee4b63bc3955e34 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f417b36d008c59024b1cbe4f7e7f6c20 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/standard_data_test_types.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=462eb1ef1287f983e137e231b64933a0 2500w" />
</Frame>

#### Quoting variables

Some test types (e.g. accepted values) require you to provide one or more values, which you may want to have quoted in the final SQL. The **Quote** flag, which is enabled by default, allows you to control this behavior. Here's an example.

Quoting **enabled** for `EXAMPLE_VALUE` (default):

```sql  theme={null}
SELECT *
FROM DB.SCHEMA.TABLE1
WHERE "COLUMN1" < 'EXAMPLE_VALUE';
```

Quoting **disabled** for `EXAMPLE_VALUE`:

```sql  theme={null}
SELECT *
FROM DB.SCHEMA.TABLE1
WHERE "COLUMN1" < EXAMPLE_VALUE;
```

### Custom Data Tests

When you need to test something that's not available in our [Standard tests](/data-monitoring/monitors/data-test-monitors#standard-data-tests), you can write a Custom test. Select your data connection, choose **Custom**, then write your SQL query.

Importantly, keep in mind that your query should return records that *fail* the test. Here are some examples to illustrate this.

**Custom business rule**

Say your company defines active users as individuals who have signed into your application at least 3 times in the past week. You could write a test that validates this logic by checking for users marked as active who *haven't* reached this threshold:

```sql  theme={null}
SELECT *
FROM users
WHERE status = 'active'
    AND signins_last_7d < 3;
```

**Data formatting**

If you wanted to validate that all phone numbers in your contacts table are 10 digits and only contain numbers, you'd return records that are not 10 digits or use non-numeric characters:

```sql  theme={null}
SELECT *
FROM contacts
WHERE LENGTH(phone_number) != 10
    OR phone_number REGEXP '[^0-9]';
```

## Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

## Add notifications

Receive notifications via Slack or email when at least one record fails your test:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## Attach CSVs to notifications

Datafold allows attaching a CSV of failed records to Slack and email notifications. This is useful if, for example, you have business users who don't have a Datafold license but need to know about records that fail your tests.

This option is configured separately per notification destination as shown here:

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=622b524bab2bb9ef79c263ec2f46ea87" alt="Attach CSVs to Data Tests notifications" data-og-width="1180" width="1180" data-og-height="742" height="742" data-path="images/data-test-csv-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=7876e84a312785296030b43008f2c1c9 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=d605241e8d8717b8dc79ab185eb303d1 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=98936a7b2311a8ef3e0dff84c78b0ca9 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=6ebe2a07c4573a310491353e536663c6 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=1432625f83e7ed5e73086b6f012201d0 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-1.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=dff2347dfe87444ad794488769039c7a 2500w" />

<Note>
  CSV attachments are limited to the lesser of 1,000 rows or 1 MB in file size.
</Note>

### Attaching CSVs in Slack

In order to attach CSVs to Slack notifications, you need to complete 1-2 additional steps:

1. If you installed the Datafold Slack app prior to October 2024, you'll need to reinstall the app by visiting Settings > Integrations > Notifications, selecting your Slack integration, then **Reinstall Slack integration**.
2. Invite the Datafold app to the channel you wish to send notifications to using the `/invite` command shown below:

<img src="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=0442451287ed6a89c1c9c680ae6a32d2" alt="Invite Datafold app to Slack channel" data-og-width="1068" width="1068" data-og-height="666" height="666" data-path="images/data-test-csv-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=280&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=f6e7b2a1da58a51aff55d6a884840a9a 280w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=560&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=21996a48dce46a32b0f97130d545a373 560w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=840&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c1c34e7b106bd225191ac63bb3404603 840w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=1100&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=16b04f6cdf970298e1ee84c3faaf74d1 1100w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=1650&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=c4a74cdac2ddd9875608fe87dcf0e2af 1650w, https://mintcdn.com/datafold/hQ4DukKOuaj6vjhH/images/data-test-csv-2.png?w=2500&fit=max&auto=format&n=hQ4DukKOuaj6vjhH&q=85&s=650487221f06e815f762b7dc13adaf01 2500w" />

## Run Tests in CI

Standard Data Tests run on a schedule against your production data. But often it's useful to test data before it gets to production as part of your deployment workflow. For this reason, Datafold supports running tests in CI.

Data Tests in CI work very similarly to our [Monitors as Code](/data-monitoring/monitors-as-code) feature, in the sense that you define your tests in a version-controled YAML file. You then use the Datafold SDK to execute those tests as part of your CI workflow.

### Write your tests

First, create a new file (e.g. `tests.yaml`) in the root of your repository. Then write your tests use the same format described in our [Monitors as Code](/data-monitoring/monitors-as-code) docs with two exceptions:

1. Add a `run_in_ci` flag to each test and set it to `true` (assuming you'd like to run the test)
2. (Optional) Add placeholders for variables that you'd like to populate dynamically when executing your tests

Here's an example:

```yaml  theme={null}
monitors:
  null_pk_test:
    type: test
    name: No NULL pk in the users table
    run_in_ci: true
    connection_id: 8
    query: select * from {{ schema }}.USERS where id is null

  duplicate_pk_test:
    type: test
    name: No duplicate pk in the users table
    run_in_ci: true
    connection_id: 8
    query: |
        select *
        from {{ schema }}.USERS
        where id in (
            select id
            from {{ schema }}.USERS
            group by id
            having count(*) > 1
        );
```

### Execute your tests

<Note>
  **INFO**

  This section describes how to get started with GitHub Actions, but the same concepts apply to other hosted version control platforms like GitLab and Bitbucket. Contact us if you need help getting started.
</Note>

If you're using GitHub Actions, create a new YAML file under `.github/workflows/` using the following template. Be sure to tailor it to your particular setup:

```yaml  theme={null}
  on:
    push:
      branches:
        - main
    pull_request:
  jobs:
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/checkout@v2
          with:
            token: ${{ secrets.GH_TOKEN }}
            repository: datafold/datafold-sdk
            path: datafold-sdk
            ref: data-tests-in-ci-demo
        - uses: actions/setup-python@v2
          with:
            python-version: '3.12'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Set schema env var in PR
          run: |
            echo "SCHEMA=ANALYTICS.PR" >> $GITHUB_ENV
          if: github.event_name == 'pull_request'
        - name: Set schema env var in main
          run: |
            echo "SCHEMA=ANALYTICS.CORE" >> $GITHUB_ENV
          if: github.event_name == 'push'
        - name: Run tests
          run: |
            datafold tests run --var schema:$SCHEMA --ci-config-id 1 tests.yaml # use the correct file name/path
          env:
            DATAFOLD_HOST: https://app.datafold.com # different for dedicated deployments
            DATAFOLD_API_KEY: ${{ secrets.DATAFOLD_API_KEY }} # remember to add to secrets
```

### View the results

When your CI workflow is triggered (e.g. by a pull request), you can view the terminal output for your test results:

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8343173f20f186775988ed8edc5e7f07" data-og-width="1498" width="1498" data-og-height="812" height="812" data-path="images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=9fc0a8d51af0d5bd0e39a2b43685269f 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fe3e2e88ba833cb4dd8f5599a360adca 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=61f7f849fe901b4a9230ea6f647f6138 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=fcb782b280969c750172fd1b9fc8f19d 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1cc0fbc6734157601122b1c62a2111b2 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_tests_in_ci_output-9be8c97e4d32734e71edee4f201e0ffc.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=184d1348cbf54c03144147559c32a356 2500w" />
</Frame>

## Need help?

If you have any questions about how to use Data Test monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
