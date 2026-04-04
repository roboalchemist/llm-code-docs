#  'instruction_template_cls': 'NoneType'}}

```

Running the evaluations as :

```python
experiment_5 = run_eval(eval_df,
                        collection_name=COLLECTION_NAME,
                        recipe_id=recipe_gpt['id'],
                        num_docs=num_docs,
                        path=f"{COLLECTION_NAME}_{num_docs}_gpt.csv")

```

We observe :

![experiment5_eval.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/experiment5_eval.png)

and comparing all the 5 experiments as below :

![graph_exp1_exp2_exp3_exp4_exp5.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/graph_exp1_exp2_exp3_exp4_exp5.png)

**GPT-3.5 surpassed Mistral-7B in all metrics**! Notably, Experiment 5 exhibited the **lowest occurrence of hallucination**.

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#conclusions) Conclusions

Let’s take a look at our results from all 5 experiments above

![overall_eval_results.png](https://qdrant.tech/articles_data/rapid-rag-optimization-with-qdrant-and-quotient/overall_eval_results.png)

We still have a long way to go in improving the retrieval performance of RAG, as indicated by our generally poor results thus far. It might be beneficial to **explore alternative embedding models** or **different retrieval strategies** to address this issue.

The significant variations in _Context Relevance_ suggest that **certain questions may necessitate retrieving more documents than others**. Therefore, investigating a **dynamic retrieval strategy** could be worthwhile.

Furthermore, there’s ongoing **exploration required on the generative aspect** of RAG.
Modifying LLMs or prompts can substantially impact the overall quality of responses.

This iterative process demonstrates how, starting from scratch, continual evaluation and adjustments throughout experimentation can lead to the development of an enhanced RAG system.

## [Anchor](https://qdrant.tech/articles/rapid-rag-optimization-with-qdrant-and-quotient/\#watch-this-workshop-on-youtube) Watch this workshop on YouTube

> A workshop version of this article is [available on YouTube](https://www.youtube.com/watch?v=3MEMPZR1aZA). Follow along using our [GitHub notebook](https://github.com/qdrant/qdrant-rag-eval/tree/master/workshop-rag-eval-qdrant-quotient).

Rapid RAG Optimization with Qdrant and Quotient - YouTube

[Photo image of Qdrant - Vector Database & Search Engine](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA?embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

Qdrant - Vector Database & Search Engine

8.12K subscribers

[Rapid RAG Optimization with Qdrant and Quotient](https://www.youtube.com/watch?v=3MEMPZR1aZA)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Watch on](https://www.youtube.com/watch?v=3MEMPZR1aZA&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

0:00

0:00 / 51:40
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=3MEMPZR1aZA "Watch on YouTube")

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/rapid-rag-optimization-with-qdrant-and-quotient.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/rapid-rag-optimization-with-qdrant-and-quotient.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-92-lllmstxt|>
## hybrid-queries
- [Documentation](https://qdrant.tech/documentation/)
- [Concepts](https://qdrant.tech/documentation/concepts/)
- Hybrid Queries