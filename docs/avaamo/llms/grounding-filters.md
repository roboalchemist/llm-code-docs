# Source: https://docs.avaamo.com/user-guide/llamb/llamb-filters/grounding-filters.md

# Grounding filters

Grounding filters ensure the quality, accuracy, and relevance of the generated output, and help to "ground" the models in the context of the specific use case to obtain accurate and relevant output.

### How does it work? <a href="#ode7hqmo4s9a" id="ode7hqmo4s9a"></a>

Grounding filters in LLaMB work on two primary metrics:

* **Answer relevancy:** This metric calculates the degree to which the generated response accurately and appropriately addresses the given input or query. It measures how well the generated answer matches the given prompt. Answers with incomplete or unnecessary information get lower scores, while more relevant answers get higher scores. The score is determined using the question, the context, and the answer.
* **Context relevancy:** Context relevancy metrics calculate the degree to which the generated response accurately addresses and aligns with the context provided by the input. It gauges the relevancy of the retrieved context, calculated based on both the question and contexts. LLaMB uses techniques like transformers and attention mechanisms to better capture and understand the context. Embeddings help the model retain and relate to contextual information effectively.

### Examples <a href="#eez8v044rayd" id="eez8v044rayd"></a>

The following example illustrates an example LLaMB agent and how grounding filters help in generating accurate responses with relevant context:

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fd3RxUyDvZkzeDN06F7RI%2F3.png?alt=media" alt="" width="375"></div>
