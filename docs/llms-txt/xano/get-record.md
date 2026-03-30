# Source: https://docs.xano.com/the-function-stack/functions/database-requests/get-record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Record

Get Record allows you to retrieve a single record from a database table using a single field to search by.

<Frame>
  <iframe src="https://demo.arcade.software/lZOuWcUumARAVBkZLcb7?embed" title="https://demo.arcade.software/lZOuWcUumARAVBkZLcb7?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

<Tabs>
  <Tab title="Filter">
    In Get Record, you'll provide the name of the field to search inside of, and the value to search for. These can come from inputs, variables, or you can manually specify a value.

    **field\_name** is the name of the field to look inside of. For example, if we wanted to search for a record with a specific ID, we'd type `id` here.

    **field\_value** is the value to search for in the provided field. Assuming we are searching in the `id` field, we would put the ID to search for here.

    <Info>
      If you need to find a record based on multiple fields, use [Query All Records](/the-function-stack/functions/database-requests/query-all-records) instead.
    </Info>

    You can also choose to enable a lock on the returned records here. Locking the records as part of a [database transaction](/the-function-stack/functions/database-requests/database-transaction) will prevent other function stacks from modifying the data until the lock has been released.
  </Tab>

  <Tab title="Output">
    ### Customizing the return

    Click <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/af34b8b7-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=635c91dca96497f3f23bb1360f0a218b" width="105" height="39" data-path="images/af34b8b7-image.jpeg" /> to edit the fields returned in the query.

    <Info>
      Note that customizing to reduce the fields returned will not have an impact on query speed, but may help with other performance issues in your function stacks. It is always good practice to only return the fields necessary.
    </Info>

    ### Return As

    Change the variable name that this function will output to.

    <Info>
      If you're using conditional steps, you can use the same variable name in multiple steps to make satisfying the conditional or outputting data in the response easier.

      For example, if we are sending a specific response based on if a variable is true or false, we can set both of those outputs to the same variable, making building our response easier.
    </Info>
  </Tab>

  <Tab title="Settings">
    Give this function a description for easy understanding of what this function achieves.

    This description will appear in the function stack, giving you easier readability for complex logic.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b191952c-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=5c8fab23febcc368a987398fdcf1fd8f" width="709" height="282" data-path="images/b191952c-image.jpeg" />
    </Frame>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).