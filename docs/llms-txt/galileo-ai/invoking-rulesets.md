# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-protect/how-to/invoking-rulesets.md

# Invoking Rulesets

> Invoke rulesets in Galileo Protect to apply AI safeguards effectively, with comprehensive guidance on ruleset usage, configuration, and execution.

You'll need to *invoke* Protect whenever there's an input or output you want to validate.

You might choose to run multiple validations on different *stages* of your workflow (e.g. once when you get the query from your user, another time once the model has generated a response for the given task).

<Tabs>
  <Tab title="Python">
    ## Projects and Stages

    Before invoking Protect, you need to create a project and a stage. This will be used to associate your invocations and organize them.

    To create a new project:

    ```py
    import galileo_protect as gp

    gp.create_project("<project_name>")

    ```

    And to create a new stage thereafter:

    ```py
    stage = gp.create_stage(name="<stage_name>")
    stage_id = stage.id
    ```

    If you want to add a stage to a pre-existing project, please also specify the project ID alongwith your stage creation request:

    ```py
    stage = gp.create_stage(name="<stage_name>", project_id="<project_id>")
    stage_id = stage.id
    ```

    ## Invocations

    At invocation time, you can either pass the project ID and stage name or the stage ID directly. These can be set as environment variables or passed directly to the `invoke` method as below.

    ```py
    response = gp.invoke(
        payload=gp.Payload(output="here is my SSN 123-45-6789"),
        prioritized_rulesets=[
            gp.Ruleset(
                rules=[
                    gp.Rule(
                        metric=gp.RuleMetrics.pii,
                        operator=gp.RuleOperator.contains,
                        target_value="ssn",
                    )
                ],
                action=gp.OverrideAction(
                    choices=["Sorry, I cannot answer that question."]
                ),
            )
        ],
        stage_id=stage_id,
    )

    response.text

    ```
  </Tab>

  <Tab title="REST API with Javascript">
    To invoke Protect using the REST API, simply make a `POST` request to the `/v1/protect/invoke` endpoint with your [Rules](/galileo/gen-ai-studio-products/galileo-protect/concepts/rule) and [Actions](/galileo/gen-ai-studio-products/galileo-protect/concepts/action).

    If the project or stage name don't exist, a project + stage will be created for you for convenience.

    ```javascript
    const body = {
      prioritized_rulesets: [
        {
          rules: [
            {
              metric: "pii",
              operator: "contains",
              target_value: "ssn",
            },
          ],
          action: {
            type: "OVERRIDE",
            choices: ["Sorry, I cannot answer that question."],
          },
        },
      ],
      payload: {
        output: "here is my SSN 123-45-6789",
      },
      project_name: "<string>",
      stage_name: "<string>",
    };

    const options = {
      method: "POST",
      headers: {
        "Galileo-API-Key": "<api-key>",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    };

    fetch("https://api.your.galileo.cluster.com/v1/protect/invoke", options)
      .then((response) => response.json())
      .then((response) => console.log(response))
      .catch((err) => console.error(err));
    ```
  </Tab>
</Tabs>

For more information on how to define Rules and Actions, see [Rules](/galileo/gen-ai-studio-products/galileo-protect/concepts/rule) and [Actions](/galileo/gen-ai-studio-products/galileo-protect/concepts/action).
