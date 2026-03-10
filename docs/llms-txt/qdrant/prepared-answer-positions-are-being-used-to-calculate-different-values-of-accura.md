# Prepared answer positions are being used to calculate different values of accuracy@k
for k in range(1, k_max + 1):
    correct_answers = len(
        list(
            filter(lambda x: 0 <= x < k, answer_positions)
        )
    )
    print(f"accuracy@{k} =", correct_answers / len(dataset["train"]))

```

Here are the values of the top-k accuracy for different values of k:

| **metric** | **value** |
| --- | --- |
| accuracy@1 | 0.877 |
| accuracy@2 | 0.921 |
| accuracy@3 | 0.942 |
| accuracy@4 | 0.950 |
| accuracy@5 | 0.956 |
| accuracy@6 | 0.960 |
| accuracy@7 | 0.964 |
| accuracy@8 | 0.971 |
| accuracy@9 | 0.976 |
| accuracy@10 | 0.977 |

It seems like our system worked pretty well even if we consider just the first result, with the lowest distance.
We failed with around 12% of questions. But numbers become better with the higher values of k. It might be also
valuable to check out what questions our system failed to answer, their perfect match and our guesses.

We managed to implement a working Question Answering system within just a few lines of code. If you are fine
with the results achieved, then you can start using it right away. Still, if you feel you need a slight improvement,
then fine-tuning the model is a way to go. If you want to check out the full source code,
it is available on [Google Colab](https://colab.research.google.com/drive/1YOYq5PbRhQ_cjhi6k4t1FnWgQm8jZ6hm?usp=sharing).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qa-with-cohere-and-qdrant.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/articles/qa-with-cohere-and-qdrant.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-177-lllmstxt|>
## geo-polygon-filter-gsoc
- [Articles](https://qdrant.tech/articles/)
- Google Summer of Code 2023 - Polygon Geo Filter for Qdrant Vector Database

[Back to Qdrant Internals](https://qdrant.tech/articles/qdrant-internals/)