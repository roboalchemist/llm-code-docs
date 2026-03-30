# Summary
{summary}

"""
for i in eval_rubrics:
    eval_output = run_mistral(
        scoring_prompt.format(
            news=news, summary=summary, metric=i["metric"], rubrics=i["rubrics"]
        ),
        model="mistral-large-latest",
        is_json=True,
    )
    print(eval_output)