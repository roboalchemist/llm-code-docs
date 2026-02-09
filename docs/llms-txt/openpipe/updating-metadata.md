# Source: https://docs.openpipe.ai/features/updating-metadata.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Updating Metadata Tags

You may want to update the metadata tags on a request log after it's already been reported. For instance, if you notice that a certain completion from your fine-tuned model was flawed,
you can mark it to be imported into one of your datasets and relabeled with GPT-4 for future training.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    import os
    from openpipe import OpenPipe, OpenAI
    from openpipe.client import UpdateLogTagsRequestFiltersItem

    # Find the config values in "Installing the SDK"
    client = OpenAI()
    op_client = OpenPipe(
        # defaults to os.environ["OPENPIPE_API_KEY"]
        api_key="YOUR_API_KEY"
    )

    completion = client.chat.completions.create(
        model="openpipe:your-fine-tuned-model-id",
        messages=[{"role": "system", "content": "count to 10"}],
        metadata={"prompt_id": "counting", "tag_to_remove": "some value"},
    )

    resp = op_client.update_log_metadata(
        filters=[
            UpdateLogTagsRequestFiltersItem(
                field="completionId",
                equals=completion.id,
            ),
            # completionId is the only filter necessary in this case, but let's add a couple more examples
            UpdateLogTagsRequestFiltersItem(
                field="model",
                equals="openpipe:your-fine-tuned-model-id",
            ),
            UpdateLogTagsRequestFiltersItem(
                field="metadata.prompt_id",
                equals="counting",
            ),
        ],
        metadata={
            "relabel": "true",
            "tag_to_remove": None # this will remove the tag_to_remove tag from the request log we just created
        },
    )

    assert resp.matched_logs == 1
    ```
  </Tab>

  <Tab title="NodeJS">
    ```typescript  theme={null}
    import OpenAI from "openpipe/openai";
    import OpenPipe from "openpipe/client";

    // Find the config values in "Installing the SDK"
    const client = OpenAI();
    const opClient = OpenPipe({
      // defaults to process.env.OPENPIPE_API_KEY
      apiKey: "YOUR_API_KEY",
    });

    const completion = await client.chat.completions.create({
      model: "openpipe:your-fine-tuned-model-id",
      messages: [{ role: "user", content: "Count to 10" }],
      metadata: {
        prompt_id: "counting",
        tag_to_remove: "some value",
      },
    });

    const resp = await opClient.updateLogTags({
      filters: [
        { field: "completionId", equals: completion.id },
        // completionId is the only filter necessary in this case, but let's add a couple more examples
        { field: "model", equals: "openpipe:your-fine-tuned-model-id" },
        { field: "metadata.prompt_id", equals: "counting" },
      ],
      metadata: {
        relabel: "true",
        tag_to_remove: null, // this will remove the tag_to_remove tag from the request log we just created
      },
    });

    expect(resp.matchedLogs).toEqual(1);
    ```
  </Tab>
</Tabs>

To update your metadata, you'll need to provide two fields: `filters` and `metadata`.

### Filters

Use filters to determine which request logs should be updated. Each filter contains two fields, `field` and `equals`.

* **`field`: Required** - Indicates the field on a request log that should be checked. Valid options include `model`, `completionId`, and `tags.your_tag_name`.
* **`equals`: Required** - The value that the field should equal.

Keep in mind that filters are cumulative, so only request logs that match all of the filters you provide will be updated.

### Metadata

Provide one or more metadata tags in a json object. The key should be the name of the tag you'd like to add, update, or delete. The value should be the new value of the tag.
If you'd like to delete a tag, provide a value of `None` or `null`.

Updated metadata tags will be searchable in the [Request Logs](/features/request-logs) panel.
