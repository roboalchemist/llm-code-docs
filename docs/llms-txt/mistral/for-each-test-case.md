# for each test case
for name in prompts:

    # define user message
    user_message = prompt_template.format(medical_notes=prompts[name]["medical_notes"])

    # run LLM
    response = json.loads(run_mistral(user_message))

    # calculate accuracy rate for this test case
    accuracy_rates.append(
        compare_json_objects(response, prompts[name]["golden_answer"])
    )