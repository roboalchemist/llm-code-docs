# Tips for responding to user requests

1. Start by analyzing the task and identifying which API's should be used;

2. If multiple API's are required, outline the purpose of each API;

3. Write the code for calling each API as a separate function, and correctly handle any possible errors;
It is important to write reusable code, so that the user can reap the most benefits out of your response.
```python
def read(url):
	...
	
def main():
	...
```
Note: make sure you parse the response of each API correctly so that it can be used in the code.
For example, if you want to read the content of the page, you should extract the content from the response of the reader API like `content = reader_response["data"]["content"]`.
Another example, if you want to extract all the URL from a page, you can use the reader API with the "X-With-Links-Summary: true" header and then you can extract the links like `links = reader_response["data"]["links"]`.

4. Write the complete code, including input loading, calling the API functions, and saving/printing results;
Remember to use variables for required API keys, and point out to the user that they need to correctly set these variables.

5. Finally, Jina AI API endpoints rate limits:
Embedding & Reranker APIs (api.jina.ai/v1/embeddings, /rerank): 500 RPM & 1M TPM with API key; 2k RPM & 5M TPM with premium key
Reader APIs:
 - r.jina.ai: 500 RPM, 5k RPM premium
 - s.jina.ai: 100 RPM, 1000 RPM premium
DeepSearch API (deepsearch.jina.ai): 50 RPM, 500 RPM premium
VLM API (api-beta-vlm.jina.ai): Note that cold starts may take 30-60 seconds
Classifier APIs (api.jina.ai/v1/classify):
 - 20 RPM & 200k TPM; 60 RPM & 1M TPM premium
Segmenter API (segment.jina.ai): 200 RPM, 1k RPM premium

Approach your task step by step.