# we’ll use question and long_answer.
dataset = load_dataset("pubmed_qa", "pqa_labeled")

```

| **pubid** | **question** | **context** | **long\_answer** | **final\_decision** |
| --- | --- | --- | --- | --- |
| 18802997 | Can calprotectin predict relapse risk in infla… | … | Measuring calprotectin may help to identify UC… | maybe |
| 20538207 | Should temperature be monitorized during kidne… | … | The new storage can affords more stable temper… | no |
| 25521278 | Is plate clearing a risk factor for obesity? | … | The tendency to clear one’s plate when eating … | yes |
| 17595200 | Is there an intrauterine influence on obesity? | … | Comparison of mother-offspring and father-offs.. | no |
| 15280782 | Is unsafe sexual behaviour increasing among HI… | … | There was no evidence of a trend in unsafe sex… | no |

### [Anchor](https://qdrant.tech/articles/qa-with-cohere-and-qdrant/\#using-cohere-and-qdrant-to-build-the-answers-database) Using Cohere and Qdrant to build the answers database

In order to start generating the embeddings, you need to [create a Cohere account](https://dashboard.cohere.ai/welcome/register).
That will start your trial period, so you’ll be able to vectorize the texts for free. Once logged in, your default API key will
be available in [Settings](https://dashboard.cohere.ai/api-keys). We’ll need it to call the co.embed API. with the official python package.

```python
import cohere

cohere_client = cohere.Client(COHERE_API_KEY)