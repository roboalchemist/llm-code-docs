# Source: https://braintrust.dev/docs/guides/views.md

# Views

You'll often want to create a view that shows data organized and visualized a certain way on the same underlying data. Views are saved table configurations that preserve filters, sorts, column order and column visibility. All table-based layouts, including logs, experiments, datasets and projects support configured views.

<img src="https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=5e3a5c7fd7a904a4e9dfec6cbc7394d1" alt="Views" data-og-width="2822" width="2822" data-og-height="1334" height="1334" data-path="images/guides/views.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?w=280&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=0d72db951893fd587bf9d765fe6a9ce1 280w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?w=560&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=c830cc795cc9dc5bbf9c88f2c088710a 560w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?w=840&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=1e4e2c05d72773a8bbfe8f3aba20d41c 840w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?w=1100&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=dd6883f18003141034add2802edba5f0 1100w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?w=1650&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=8bed707dc93bd0fb0974e4a8c3fb7296 1650w, https://mintcdn.com/braintrust/LWrAGXabOsN4v6gt/images/guides/views.png?w=2500&fit=max&auto=format&n=LWrAGXabOsN4v6gt&q=85&s=a2f95b7a56d9d2396f4a9f956549fa23 2500w" />

## Default locked views

Some table layouts include default views for convenience. These views are locked and cannot be modified or deleted.

* **All rows** corresponds to all of the records in a given table. This is the default, unfiltered view.

On experiment and logs pages:

* **Non-errors** corresponds to all of the records in a given table that do not contain errors.
* **Errors** corresponds to all of the records in a given table that contain errors.

On experiment pages:

* **Unreviewed** hides items that have already been human-reviewed.

## Create and manage custom views

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To create a custom view, start by applying the filters, sorts, and columns that you would like to have visible in your view. Then, navigate to the **Views** dropdown and select **Create view**.

    <video className="border rounded-md" loop autoPlay playsInline muted poster="/images/reference/views/views-poster.png">
      <source src="https://mintcdn.com/braintrust/d9paHuGG6xUYaUiZ/images/reference/views/views.mp4?fit=max&auto=format&n=d9paHuGG6xUYaUiZ&q=85&s=bbc6fe0e7121794e87b1344b7db40ea1" type="video/mp4" data-path="images/reference/views/views.mp4" />
    </video>

    After entering a view, select **Save view** in the view dropdown menu to save any changes you make to the filters, sorts, and columns.

    To rename, duplicate, delete, or set as default, use the **Manage view** submenu in the view dropdown.

        <img src="https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=eb3ae1e4dcbda3e7501267943536b701" alt="Views menu" data-og-width="2328" width="2328" data-og-height="1208" height="1208" data-path="images/guides/views-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?w=280&fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=e4e39644e21b97440c74d7e024995a26 280w, https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?w=560&fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=08721dc55a8234100adab63ba7f92462 560w, https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?w=840&fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=b9ad919966b6e2fea8cfb851a97d9471 840w, https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?w=1100&fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=4e7167431c538ff3ede2e9558449506f 1100w, https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?w=1650&fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=ec560ee3a18f67eafaaae867dd5eb20d 1650w, https://mintcdn.com/braintrust/bLQQx4p_F7jEe4BM/images/guides/views-menu.png?w=2500&fit=max&auto=format&n=bLQQx4p_F7jEe4BM&q=85&s=422b580b1d18a588689fed1eb6a513bf 2500w" />
  </Tab>

  <Tab title="API" icon="terminal">
    Views can be created and managed programmatically [via the API](/api-reference/views/list-views).
  </Tab>
</Tabs>

## Access

Views are accessible and configurable by any member of the organization.

## Best practices

Use views when:

* You frequently reapply the same filters.
* You want to standardize what your team sees.
* You want to review only a subset of records.

Make sure to use clear, descriptive names so your team can quickly understand the purpose of each view. Some example views might be:

* "Logs with Factuality \< 50%"
* "Unreviewed high-priority traces"
* "Failing test cases"
* "Tagged with 'Customer Support'"
* "Lisa's test cases"

### Using views with custom columns

If you regularly filter by complex or nested JSON queries or metadata, consider creating [custom columns](/core/experiments/interpret#create-custom-columns). Custom columns let you surface frequently-used or computed values directly as columns, simplifying repetitive filtering tasks. Custom columns are also rendered in trace spans, with their own span field view type (for example, JSON, Markdown, or HTML).

For example, you can analyze data across multiple models within a single experiment view:

* First, define a custom column extracting the model name from your metadata.
* Then, apply the custom column, sort, and any additional standard filters, then save this configuration as a view.
* Lastly, use the filter dropdown to quickly toggle between models.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt