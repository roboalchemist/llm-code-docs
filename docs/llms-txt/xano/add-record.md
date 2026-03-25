# Source: https://docs.xano.com/the-function-stack/functions/database-requests/add-record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Record

Add Record allows you to add a new record to an existing table.

<Frame>
  <iframe src="https://demo.arcade.software/4tLbIYlynMcDDSpqRvb5?embed" title="https://demo.arcade.software/4tLbIYlynMcDDSpqRvb5?embed" allowFullScreen allow="clipboard-write" class="contentkit-webframe" width="1000" height="500" />
</Frame>

<Tabs>
  <Tab title="Filter">
    In this section, you will specify the data to be added to the record.

    Click <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/30e379e4-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=d137380875c9d694db46eedadbf997a9" className="inline m-0" width="25" height="22" data-path="images/30e379e4-image.jpeg" /> to quickly enable or disable all fields.

    Hover over each field name and click <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/df467d0a-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=9f0f2c45a97c5d404f08d8d9c2ec0ce6" className="inline m-0" width="24" height="21" data-path="images/df467d0a-image.jpeg" /> to disable that field — this means that no data will be written, or the default value in the database will be used instead, if set.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/ccb79742-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=91cebbe206fe1af3b234f1b8314f4c84" width="266" height="132" data-path="images/ccb79742-image.jpeg" />
    </Frame>

    If you have an object that already contains all of the data to use in the add record step, click <img src="https://mintcdn.com/xano-997cb9ee/_FyaEhYRFYQZinJ0/images/d9d03ea1-image.jpeg?fit=max&auto=format&n=_FyaEhYRFYQZinJ0&q=85&s=2b9eecbdabcbab3c6e913b11495952dd" className="inline m-0" width="267" height="41" data-path="images/d9d03ea1-image.jpeg" />
    to auto-fill from that variable.

    <Warning>
      You are able to manually specify a record ID, but proceed with caution. If you have workflows that rely on sequential IDs, or multiple requests try and add records with the same ID simultaneously, you might run into problems. By default, Xano will auto-increment the ID for you, which is usually best practice.
    </Warning>
  </Tab>

  <Tab title="Output">
    ### Customizing the return

    Click <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/af34b8b7-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=635c91dca96497f3f23bb1360f0a218b" className="inline m-0" width="105" height="39" data-path="images/af34b8b7-image.jpeg" /> to edit the fields returned in the query.

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