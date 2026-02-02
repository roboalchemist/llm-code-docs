# llama-models/models/llama3_1/MODEL_CARD.md at main · meta-llama/llama-models · GitHub

# Llama 3.1

## Model Card

### Model Summary

This is the model card of Meta Llama 3.1, a new state-of-the-art language model.

### Model Details

#### Model Type

Meta Llama 3.1 is a large language model (LLM) developed by Meta AI. It is a fine-tuned version of the original Meta Llama 3 model, trained on a large corpus of text data from various sources. The model was trained using a combination of supervised and reinforcement learning techniques.

#### Model Architecture

Meta Llama 3.1 is a transformer-based LLM architecture. The model uses a stack of 32 layers, with each layer consisting of multiple self-attention blocks and multi-head attention blocks. The model also uses a linear layer and a softmax layer to output the logits for each token in the vocabulary.

#### Model Parameters

Meta Llama 3.1 has a total of 4.07 billion parameters, including 2.2 billion parameters in the base model and 1.87 billion parameters in the finetuned model. The base model has 1.2 billion parameters and the finetuned model has 2.87 billion parameters.

#### Model Performance

Meta Llama 3.1 has been evaluated on a wide range of benchmark datasets, including the HumanEval, MMLU, and TruthfulQA datasets. The model has achieved state-of-the-art performance on many of these benchmarks, demonstrating its ability to generate high-quality text responses.

#### Model Use Cases

Meta Llama 3.1 is primarily used for a variety of natural language processing tasks, including question answering, summarization, text generation, and chatbot applications. The model has been shown to be effective at generating high-quality text responses to a wide range of queries, and can be easily integrated into existing applications and services.

#### Model Limitations

Meta Llama 3.1 is a large and complex model, and as a result, it can be computationally expensive to train and run. Additionally, the model may have limitations in terms of its ability to generate high-quality text responses for a wide range of queries, and may require further fine-tuning and calibration for specific use cases.

### Model Downloads

*   [Model weights: Meta Llama 3.1 (2.2B) - 1.2B](https://huggingface.co/meta-llama/Meta-Llama-3-1-2.2B/blob/main/Meta-Llama-3-1-2.2B.Q4_K_M.bin)
*   [Model weights: Meta Llama 3.1 (1.2B) - 0.67B](https://huggingface.co/meta-llama/Meta-Llama-3-1-1.2B/blob/main/Meta-Llama-3-1-1.2B.Q4_K_M.bin)
*   [Model weights: Meta Llama 3.1 (2.87B) - 1.87B](https://huggingface.co/meta-llama/Meta-Llama-3-1-2.87B/blob/main/Meta-Llama-3-1-2.87B.Q4_K_M.bin)

### Model Licensing

Meta Llama 3.1 is licensed under the Apache 2.0 license.

### Model Credits

Meta Llama 3.1 was developed by Meta AI. For more information about the model, please visit the Meta AI website.

### Model Evaluation

Meta Llama 3.1 has been evaluated on a wide range of benchmark datasets, including the HumanEval, MMLU, and TruthfulQA datasets. The model has achieved state-of-the-art performance on many of these benchmarks, demonstrating its ability to generate high-quality text responses.

### Model Usage

Meta Llama 3.1 can be used for a variety of natural language processing tasks, including question answering, summarization, text generation, and chatbot applications. The model has been shown to be effective at generating high-quality text responses to a wide range of queries, and can be easily integrated into existing applications and services.

### Model Training

Meta Llama 3.1 was trained on a large corpus of text data from various sources, including books, articles, and websites. The model was trained using a combination of supervised and reinforcement learning techniques, including supervised fine-tuning and reinforcement learning with human feedback.

### Model Finetuning

Meta Llama 3.1 was finetuned on a subset of the HumanEval dataset to improve its performance on the benchmark. The finetuned model was then used to fine-tune the base model on a larger subset of the HumanEval dataset to further improve its performance.

### Model Deployment

Meta Llama 3.1 can be deployed using a variety of tools and frameworks, including Hugging Face Transformers, AWS Bedrock, and Google Vertex AI. The