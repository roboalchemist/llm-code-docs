# Source: https://docs.asapp.com/generativeagent/configuring/tasks-and-functions/conditional-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Conditional Templates

Conditional Templates allow you to use saved values from API calls to change the instructions for a given task.

GenerativeAgent uses the conditional templates to render API and Prompt instructions based on the conditions and values in each template.

<Note>
  Conditional Templates must be referenced in Jinja2 templating language conditional statements.
  Head to the [Jinja Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/) to dive further into Conditional Statements
</Note>

## Write Conditional Templates

Conditional templating supports rendering based on the presence of data in an API Response Model Action.

The system pulls this data at run-time from the input model context (list of ModelActions) and stores it in reference variables that you can use in Jinja2 conditional statements.

<Note>
  If you want to render based on ModelActions that are not API Responses, it will require further help from your ASAPP Team.
</Note>

Write a Conditional Template:

1. Identify the Function and the keypath to the value from the API response you want to use for conditional rendering.
2. Add a reference variable to the list of reference\_vars for the Function in the company's functions.yaml.
   It should include name and response\_keypath at minimum, with the response\_keypath format being response.\<your\_keypath>.
   You can optionally define a transform expression with val as the keypath value to be transformed. Note that these reference variables are used across the company's Tasks, so the name parameter must be unique.
3. Use the conditional in two places by referencing vars.get("my\_reference\_var\_name"):
   * In a Task, add Jinja2 conditional statements in the prompt\_instructions and define conditions for each TaskFunction so they only render when the condition evaluates to True.
   * Conditions on TaskFunctions are optional, and functions will always render in the final prompt if no conditions are provided.
   * In a Function, add Jinja2 conditional statements to the Function's description.

## Available Variables

The following variables are available to use in the conditional templates:

| Variable             | Description                                                                                                                                                                                   | Example                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `vars`               | A dictionary of [reference variables](/generativeagent/configuring/tasks-and-functions/reference-variables).                                                                                  | `vars.get("my_reference_var_name")`                   |
| `input_vars`         | A dictionary of [input variables](/generativeagent/configuring/tasks-and-functions/input-variables).                                                                                          | `input_vars.get("my_input_var_name")`                 |
| `function_responses` | A dictionary where keys are function names and values are the corresponding function response data. If the system finds no function responses in the actions, it returns an empty dictionary. | `function_responses.get("my_function_response_name")` |
| `current_datetime`   | The current date and time.                                                                                                                                                                    | `current_datetime`                                    |
| `channel_type`       | The type of channel the conversation is on. Can be either `voice` or `messaging`.                                                                                                             | `channel_type`                                        |
| `queue_status`       | A dictionary of queues and a boolean of whether the queue is open.                                                                                                                            | `queue_status.get("general_queue")`                   |

## Use Case Example - Mobile Bill

This use case example makes GenerativeAgent behave as follows:

* If CPNI compliance is unknown, only render the identity API without its description about checking the response field "data\['cpniCompliance']", and render in the prompt\_instructions that tell the LLM it must first confirm the customer is CPNI compliant.
* If a customer is not CPNI compliant, only render the identity API with its description about checking the response field "data\['cpniCompliance']", and do not render in the prompt\_instructions that tell the LLM it must first confirm the customer is CPNI compliant.
* If a customer is CPNI compliant, do not render the identity API and render the APIs that require CPNI compliance instead, and do not render in the prompt\_instructions that tell the LLM it must first confirm the customer is CPNI compliant.

```json  theme={null}
identity:
  name: identity
  lexicon_name: identity-genagent
  lexicon_type: entity
  description: |:-
    Use this API call to determine whether you can discuss billing or account information with the customer. 
    {%- if not vars.get("compliance_unknown") and not vars.get("is_compliant") %}
    - If the data['cpniCompliance'] does not return "COMPLIANT", you cannot discuss account or billing information with the customer.
    {%- endif %}
  message_before: Give me a few seconds while I pull up your account.
  reference_vars:
    - name: is_compliant # this variable to be used in conditions
      response_keypath: response.cpniCompliance # keypath to the value from the response
      transform: val == "COMPLIANT" # val is passed in from the keypath for the transform
    - name: compliance_unknown
      response_keypath: response.cpniCompliance
      transform: val == None
```

```json  theme={null}
dname: MobileBill
selector_description: For Mobile billing inquiries only, see the current billing situation and status of your Spectrum mobile account(s), including dues, balances, important dates and more.
prompt_instructions: |:-
  - If the customer expresses anything about their question not being answered (EXAMPLES: "That didn't answer my question" "My question wasn't answered"), *before doing anything else* ask them for more details
  - The APIs in these instructions and the information they return MUST only be used to answer basic questions about a mobile bill or statements.
  - They MUST NOT be used to answer any out-of-scope concerns like the following:
  - - To answer questions related to cable (internet, TV, landline), use the command `APICALL change_task(task_name="CableBill")` to switch to the CableBill flow.
  - - concerns about why services are not working
  - - concerns about when service will be restored
  - - inquiries about where bills are being sent, or sending confirmation emails
  - - updating billing address
  {%- if vars.get("compliance_unknown") %}
  - You must confirm that a customer is CPNI compliant before telling them anything about their account or billing info. The only way to do this is via the identity() api as described below.
  - -  Note: Authentication is not the same as being CPNI compliant. You still need to use the identity() api to confirm that a customer is CPNI compliant if they are authenticated.
  {%- endif %}
  - Mobile services are billed seperately from Cable (Internet, TV, and Home phone) services.
functions:
  - name: identity
    conditions: not vars.get("is_compliant")
  - name: mobile_current_balance
    conditions: vars.get("is_compliant")
    instructions: |:-
      - Anytime you call `mobile_current_balance`, you should also call `mobile_current_statement`
  - name: mobile_current_statement
    conditions: vars.get("is_compliant")
  - name: mobile_statements
    conditions: vars.get("is_compliant")
    instructions: |:-
      - When describing payments, your response to the customer must not imply that you know the purpose or reason for any payment or how it will affect the account.
      - If you think you have found a payment the customer is referring to, ask the customer if it's the right payment, but do not say anything to confirm the customer's impression of the payment or what it is for.
  - name: mobile_specific_statement
    conditions: vars.get("is_compliant")
```
