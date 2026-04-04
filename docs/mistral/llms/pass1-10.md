# {'pass@1': 1.0}
```

</details>

## LLM-based Evaluation
Using a Large Language Model (LLM) to evaluate or judge the output of another LLM is a common practice in situations especially when labeled data and golden answers are not available or insufficient. The [MT Bench paper](https://arxiv.org/pdf/2306.05685) explored the effectiveness of LLM-as-a-judge and revealed that strong LLMs can perform similarly to humans. LLMs can process and evaluate large amounts of data in a relatively short time, making it highly scalable and efficient compared to human evaluation, which often requires substantial time and resources. 

There are several approaches to using LLMs as judges, including single-point grading, reference-based grading, and pairwise grading.
- **Single-point grading**: LLM assigns a single score to a generated output based on its quality or accuracy. This score is typically given according to specific grading instructions. Single-point grading is a straightforward and efficient approach, but it may not always capture the nuances of various complex outputs.
- **Reference-based grading**: LLM compares a generated output to one or more reference outputs and assigns a score based on their similarity. This approach is often used in machine translation tasks, where there may be multiple valid translations for a given input. However, reference-based grading requires the availability of a golden answer, which may not always be available.
- **Pairwise grading**: LLM compares two generated outputs and assigns a score based on their relative quality or accuracy. This approach is often used in tasks such as dialogue generation, where there may be multiple valid responses to a given query. By comparing pairs of responses, the LLM can determine which one is more relevant or coherent, and assign a score accordingly.

It is also essential to recognize the potential limitations and challenges. For example, LLMs may exhibit inherent biases. LLMs developed by one company tends to favor answers that models of the same company generate. It is difficult to ensure a fair and accurate evaluation. In our experience, Mistral Large exhibits relatively little favoritism.

<details>
<summary><b> Example 3: evaluate summary generation with LLM</b></summary>

### Example 3: evaluate summary generation with LLM

#### Evaluation data
In this example, we generate news summaries and use LLM single-point grading to evaluate the quality of the summary. To carry out the evaluation, let's use a sample news article that we plan to summarize. 

```py
news = (
    "BRUSSELS (Reuters) - Theresa May looked despondent , with deep rings under her eyes, EU chief executive Jean-Claude Juncker told aides after dining with the British prime minister last week, a German newspaper said on Sunday. The report by a Frankfurter Allgemeine Zeitung correspondent whose leaked account of a Juncker-May dinner in April caused upset in London, said Juncker thought her marked by battles over Brexit with her own Conservative ministers as she asked for EU help to create more room for maneuver at home. No immediate comment was available from Juncker s office, which has a policy of not commenting on reports of meetings. The FAZ said May, who flew in for a hastily announced dinner in Brussels with the European Commission president last Monday ahead of an EU summit, seemed to Juncker anxious, despondent and disheartened , a woman who trusts hardly anyone but is also not ready for a clear-out to free herself . As she later did over dinner on Thursday with fellow EU leaders, May asked for help to overcome British divisions. She indicated that back home friend and foe are at her back plotting to bring her down, the paper said. May said she had no room left to maneuver. The Europeans have to create it for her. May s face and appearance spoke volumes, Juncker later told his colleagues, the FAZ added. She has deep rings under her eyes. She looks like someone who can t sleep a wink. She smiles for the cameras, it went on, but it looks forced , unlike in the past, when she could shake with laughter. Now she needs all her strength not to lose her poise. As with the April dinner at 10 Downing Street, when the FAZ reported that Juncker thought May in another galaxy in terms of Brexit expectations, both sides issued statements after last week s meeting saying talks were constructive and friendly . They said they agreed negotiations should be accelerated . May dismissed the dinner leak six months ago as Brussels gossip , though officials on both sides said the report in the FAZ did little to foster an atmosphere of trust which they agree will be important to reach a deal. German Chancellor Angela Merkel was also reported to have been irritated by that leak. Although the summit on Thursday and Friday rejected May s call for an immediate start to talks on the future relationship, leaders made a gesture to speed up the process and voiced hopes of opening a new phase in December. Some said they understood May s difficulties in forging consensus in London.",
)
```

#### How to evaluate? 
- Step 1: Generate summary for the given news

First, let's use a smaller model, `open-mistral-7b', to generate a summary for the provided news article. If you have additional news articles to summarize, please generate a summary for each one. For the sake of simplicity in this example, we will only demonstrate one news sample.

```py

from mistralai import Mistral

def run_mistral(user_message, model="open-mistral-7b", is_json=False):
    client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
    messages = [{"role":"user", "content":user_message}]

    if is_json:
        chat_response = client.chat.complete(
            model=model, messages=messages, response_format={"type": "json_object"}
        )
    else:
        chat_response = client.chat.complete(model=model, messages=messages)

    return chat_response.choices[0].message.content

summary_prompt = f"""
Summarize the following news. Write the summary based on the following criteria: relevancy and readability. Consider the sources cited, the quality of evidence provided, and any potential biases or misinformation. 

## News: 
{news}
"""

summary = run_mistral(summary_prompt)
```

- Step 2: Define evaluation metrics and rubrics

To accurately evaluate the quality of the generated summaries, we need to establish clear and well-defined evaluation metrics and rubrics. These guidelines play a pivotal role in directing the LLM in its evaluation process. Feel free to incorporate various metrics and create rubrics tailored to your specific needs.

```py
eval_rubrics = [
    {
        "metric": "relevancy", 
        "rubrics": """
        Score 1: The summary is not relevant to the original text. 
        Score 2: The summary is somewhat relevant to the original text, but has significant flaws.
        Score 3: The summary is mostly relevant to the original text, and effectively conveys its main ideas and arguments.
        Score 4: The summary is highly relevant to the original text, and provides additional value or insight.
        """
    },
    {
        "metric": "readability", 
        "rubrics": """
        Score 1: The summary is difficult to read and understand.
        Score 2: The summary is somewhat readable, but has significant flaws.
        Score 3: The summary is mostly readable and easy to understand.
        Score 4: The summary is highly readable and engaging.
        """
    },
    
]
```

- Step 3: Employ a more powerful LLM (e.g., Mistral Large) as a judge

It's beneficial to use a more powerful LLM such as Mistral Large as a judge to ensure a more accurate and comprehensive evaluation of the generated summaries. In the prompt, we provide the specific evaluation metrics, associated rubrics, the original news article, and the generated summary. This information enables the LLM to evaluate the summary based on the predefined criteria systematically. In this example, we assess each metric separately to gain a better understanding of the summarization model's performance in different aspects. However, you can also choose to combine all metrics for a more general evaluation.

```py
scoring_prompt = """
Please read the provided news article and its corresponding summary. Based on the specified evaluation metric and rubrics, assign an integer score between 1 and 4 to the summary. Then, return a JSON object with the metric as the key and the evaluation score as the value.