# How to contribute

Thank you for your interest in contributing to Mistral AI. We welcome everyone who wishes to contribute and we appreciate your time and effort!

## Join our Ambassador Program

:::tip[ ]
Head to [Ambassador Program](../ambassador/) to learn more and apply! 
:::


## Contributing to the official documentation

If you are interested in contributing to our [official docs](https://docs.mistral.ai/), please submit a PR at [https://github.com/mistralai/platform-docs-public](https://github.com/mistralai/platform-docs-public). 

You can easily help by:
- fix a typo
- clarify a section
- document an underdocumented feature
- update a section that should have been updated
- ... 

## Contributing to the code clients

### Python client
Submit a PR to improve our Python client: [https://github.com/mistralai/client-python](https://github.com/mistralai/client-python). 

The easiest way to get started is to take a look at the [issue list](https://github.com/mistralai/client-python/issues) and see which one you might be interested in helping.  


### JavaScript client
Submit a PR to improve our JavaScript client: [https://github.com/mistralai/client-js](https://github.com/mistralai/client-js)

The easiest way to get started is to take a look at the [issue list](https://github.com/mistralai/client-js/issues) and see which one you might be interested in helping.  


## Contributing to the community 

### Mistral Cookbook
If you have cool examples showcasing Mistral models, whether you are using Mistral API or open-weight models, feel free to share them by submitting a PR to our [cookbook repo](https://github.com/mistralai/cookbook). 

### Discord

We are grateful to anyone who shares resources and assists us in addressing questions on our [Discord](https://discord.gg/mistralai) community.

### Community outreach
A valuable way to support Mistral AI is by engaging in active communication in the community. This can include activities like sharing on social media, writing blog articles, creating tutorial videos demonstrating your work using Mistral AI API or models. Feel free to tag us on social media, and we'll be there to support you!


[Evaluation]
Source: https://docs.mistral.ai/docs/guides/evaluation

<a target="_blank" href="https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/evaluation/evaluation.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Many companies face the challenge of evaluating whether a Large Language Model (LLM) is suitable for their specific use cases and determining which LLMs offer the best performance. It is essential to assess whether one model can effectively replace another and ensure that the chosen LLM meets the companies’ unique requirements. However, the process of evaluating LLMs can be complex and confusing. This guide provides a comprehensive approach to evaluating LLMs for various applications. We will start by discussing the goal of evaluation, the creation of evaluation datasets, and then we will dive into three primary evaluation methods with detailed Python code walkthroughs in notebooks. 

- What exact task do you want to solve?
- How to create an evaluation dataset?
- How to evaluate?  
    - Metrics-based evaluation
    - LLM-based evaluation
    - Human-based evaluation 

## What is your task? 
Before we get started with the evaluation process, it is important to think about what exact task you want to solve with the LLM. It is crucial that the task is precisely defined.

Some bad examples:
- Be a helpful assistant (What does “helpful” mean in your context?)
- Convert the text into code (What type of text and code?)
- Improve the quality of the documents (What is high vs. low quality?)

Some good examples:
- Be an assistant for customer complaints. Make sure to answer complaints in a polite and helpful way and give concise answers that don’t exceed 3 sentences. 
- Make sure to notify the user if you do not know the answer.
- Convert pseudo code into Python code 
- Rephrase the documents by improving all spelling and grammatical errors and give the text a more professional tone
- Extract all relevant information from medical records (which use case would be subject to specific applicable regulations)
- Summarize various types of documents, such as legal agreements, news articles, or scientific papers

Different goals and use cases may require different evaluation strategies. Some use cases may prioritize accuracy, while others may emphasize brevity and helpfulness. Therefore, it is crucial to know exactly what task you want to solve before starting an evaluation process.

## How to create an evaluation dataset?
There are numerous public benchmarks available for evaluating Large Language Models (LLMs) such as MMLU, GSMK8, and others. The first question to consider is whether these existing benchmarks can be used for your specific use cases. If applicable, then start with the existing benchmark dataset. 

However, we often observe that existing benchmarks are academic in nature and may not cover real-world customer use cases or only address a limited scope. Therefore, it is often preferable to create your own evaluation dataset. 

Once you have established your goals and determined whether existing benchmarks are suitable, you can proceed to create custom evaluation datasets tailored to your specific use cases. 

### Labeled data 

In many cases, it is important to create labeled data. For example, if your task is to use an LLM to extract information from medical records subject to specific applicable regulations, you can use human annotation to label the data and get the golden answer including all the information you would like to extract, e.g.,  `{"age": 60, "gender": "male", "diagnosis": "diabetes", "weight": 210, "smoking": "yes"}`. 

How much data annotation do you need? It depends on the task. You should always prioritize quality over quantity. If you have high quality data, 100 test cases can be enough to provide a meaningful signal.  

Additionally, It is recommended to have a discriminative benchmark, meaning that it’s neither too easy, nor too hard. If every model being tested achieves over 90% accuracy, the differences between them might not be meaningful, indicating the need for a better benchmark.  The goal is to create data that can differentiate models effectively. Creating discriminative data can be challenging, so focus on your specific task. Potentially multiple models perform well enough for your needs. A good evaluation dataset should lead to performances that are in agreement with model sizes, ie, larger models perform on par or better than smaller counterparts (unless the smaller models have been specifically trained for your purposes). 

Here are some examples of various prompts and golden answers across different capabilities:

| Task               | Prompt/Context| Golden Answer/Criteria|
|--------------------|:--------------------|:--------------------|
| Information extraction                | A 60-year-old male patient, Mr. Johnson, presented with symptoms of increased thirst, frequent urination, fatigue, and unexplained weight loss. Upon evaluation, he was diagnosed with diabetes, confirmed by elevated blood sugar levels. Mr. Johnson's weight is 210 lbs. He has been prescribed Metformin to be taken twice daily with meals. It was noted during the consultation that the patient is a current smoker.| `{"age": 60, "gender": "male", "diagnosis": "diabetes", "weight": 210, "smoking": "yes"}` |
|Python code generation|Write a python function to check whether the given number is odd or not using bitwise operator.|`assert is_odd(5) == True` |
|Summarization| Summarize the following into a short paragraph for 3rd graders: "Water is a chemical compound composed of two hydrogen atoms bonded to one oxygen atom, with the chemical formula H2O. The hydrogen atoms are bonded to the oxygen atom via polar covalent bonds, which means that the electrons in the bond are not shared equally between the atoms, resulting in a slight negative charge on the oxygen atom and a slight positive charge on the hydrogen atoms. This gives water molecules a bent, or V-shaped, structure, and allows them to form hydrogen bonds with other water molecules, which are responsible for many of water's unique properties, such as its high boiling point and surface tension." |Water is a special substance that is made up of two tiny parts called atoms, specifically, two hydrogen atoms and one oxygen atom. These atoms are stuck together in a way that creates a bent shape, which makes water have some amazing properties. For example, water can stick to itself, which helps it stay together as a liquid and not just turn into a gas. This also makes water have a high boiling point, which means it needs a lot of heat to turn into a gas. Water's unique properties make it an important part of our lives and our planet.|
|Multilingual|Translate this college homework assignment into advanced Spanish for an advanced writing course: "Write a personal essay of 500 words about a crucial moment in your family, describing the event, its impact on family relationships, and the emotions and thoughts that surrounded it. Your essay should have a clear structure, with an introduction, body, and conclusion, and use expressive and precise language. It will be evaluated based on clarity, coherence, depth, and originality."|Escriba un ensayo personal de 500 palabras sobre un momento crucial en su familia, describiendo el evento, su impacto en las relaciones familiares, y las emociones y pensamientos que lo rodearon. Su ensayo debe tener una estructura clara, con una introducción, un cuerpo y una conclusión, y utilizar un lenguaje expresivo y preciso. Será evaluado sobre la base de claridad, coherencia, profundidad y originalidad.|
|Chat|You are an 8th grade tutor for a Latin class, your job is to help students memorize their weekly word list test. You don’t give the answers to your students but instead help them get to the answer themselves. Begin your tutoring session by asking your student what word list do they need help memorizing. Remember to be encouraging and ask students to "show their work" i.e. articulate how they came up with that answer.|Hello there! I hope you're having a great day. As your Latin tutor, I'm here to help you with your weekly word list test. So, let's get started! Could you please tell me which word list you need help memorizing this week? Remember, the goal is not just to remember the words, but also to understand their meanings and how to use them in context. <br/> Once you've chosen a word, I'd like you to try to recall its meaning or use it in a sentence. Then, I'd love for you to "show your work" by explaining how you came up with that answer. This will help reinforce your understanding and make it easier to remember. Does that sound good? Let's dive in!


### Unlabeled data:

In some cases, you may not be able to create labeled data easily. You may use an LLM to generate the necessary data. For example, you may ask an LLM to generate questions and answers based on a given text. Here are two prompt templates for generating questions and answers:

- Prompt template for generating questions based on the context: 
```
Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge. Generate {num_questions_per_chunk} questions based on the context. The questions should be diverse in nature across the document. Restrict the questions to the context information provided.
```

- Prompt template for generating answers based on the context and the generated question from the previous prompt template: 
```
Context information is below
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge,
answer the query.
Query: {generated_query_str}
Answer: 
```

However, LLM-generated data usually requires further refinement and filtering. It is preferable to have questions derived from real-world sources, especially from experts. Nevertheless, LLM-generated data can still be helpful when real data is difficult to obtain or scarce. 

## How to evaluate

## Metrics-based evaluation
Metrics-based evaluation is the standard approach in many public benchmark evaluations. There are a number of metrics that can be used to evaluate and compare the model-generated answers with the golden answers. The most popular ones are exact match accuracy rate, recall, precision, F1 score.
- **Exact Match Accuracy Rate**: This metric measures the proportion of model-generated answers that perfectly match the golden answers. It offers a strict evaluation of the model's ability to generate precise responses.
- **Recall**: Recall calculates the fraction of relevant information from the golden answers that is successfully retrieved by the model-generated answers. A higher recall indicates that the model can capture more relevant information.
- **Precision**: Precision assesses the fraction of relevant information in the model-generated answers. A higher precision means that the model generates more accurate and relevant responses.
- **F1 Score**: The F1 score is the harmonic mean of recall and precision, providing a balanced evaluation of the model's performance in terms of both metrics.

Apart from these popular metrics, there are other NLP evaluation metrics such as BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation). BLEU is primarily used for machine translation tasks, while ROUGE is commonly applied for text summarization. However, due to concerns regarding their reliability and the potential for misleading results, we do not recommend.

<details>
<summary><b> Example 1: evaluate information extraction with accuracy rate</b></summary>

### Example 1: evaluate information extraction with accuracy rate

#### Evaluation data

This first example involves extracting patient information from medical notes. To perform the evaluation, both the medical notes and the correct/expected answer (referred to as the "golden answer") are required in the evaluation data. Here are two example test cases: 

```py
prompts = {
    "Johnson": {
        "medical_notes": "A 60-year-old male patient, Mr. Johnson, presented with symptoms of increased thirst, frequent urination, fatigue, and unexplained weight loss. Upon evaluation, he was diagnosed with diabetes, confirmed by elevated blood sugar levels. Mr. Johnson's weight is 210 lbs. He has been prescribed Metformin to be taken twice daily with meals. It was noted during the consultation that the patient is a current smoker. ",
        "golden_answer": {
            "age": 60,
            "gender": "male",
            "diagnosis": "diabetes",
            "weight": 210,
            "smoking": "yes",
        },
    },
    "Smith": {
        "medical_notes": "Mr. Smith, a 55-year-old male patient, presented with severe joint pain and stiffness in his knees and hands, along with swelling and limited range of motion. After a thorough examination and diagnostic tests, he was diagnosed with arthritis. It is important for Mr. Smith to maintain a healthy weight (currently at 150 lbs) and quit smoking, as these factors can exacerbate symptoms of arthritis and contribute to joint damage.",
        "golden_answer": {
            "age": 55,
            "gender": "male",
            "diagnosis": "arthritis",
            "weight": 150,
            "smoking": "yes",
        },
    },
}
```

#### How to evaluate?

- Step 1: Define prompt template

We have designed a prompt that incorporates the medical notes as context. Additionally, we expect the model to provide output in a JSON format following a predefined JSON schema, ensuring that the model produces the desired output accurately. It is worth noting that when calling our models, we specified the response format as `{"type": "json_object"}` to ensure consistent JSON output.


```py

from mistralai import Mistral

def run_mistral(user_message, model="mistral-large-latest"):
    client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
    messages = [{"role": "user", "content": user_message}]
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
        response_format={"type": "json_object"},
    )
    return chat_response.choices[0].message.content