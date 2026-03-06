# Source: https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/run-ollama.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Ollama

*Last Updated: September 24, 2024*

Ollama is a toolkit for deploying and service Large Language Models (LLMs). Ollama enables local operation of
open-source large language models like Llama 2, simplifying setup and configuration, including GPU usage, and providing
a library of supported models.

[Learn More Here](https://ollama.com/)

## Ollama API

Ollama can be used as an API that can:

* Generate text completions using different language models and tags.
* Stream responses in JSON format or receive them as single objects.
* Include optional parameters such as images, formatting options, and system messages.
* Maintain conversational memory using the context parameter.
* Control response streaming and model memory retention.

For detailed instructions and examples, refer to the
[Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)

# Deploying Ollama on Salad

## Container

Ollama provides a pre-built docker available via the Docker Container registry :
[https://hub.docker.com/r/ollama/ollama](https://hub.docker.com/r/ollama/ollama)

In order to deploy the container on Salad, you will need to specify the image:

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=af859d86712d7b7aaabfa34cd5ca018e" data-og-width="506" width="506" data-og-height="467" height="467" data-path="container-engine/images/a48be4d-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c3a80920c26df9c9f418b008dd6a7113 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2c0e3e71c2d4dd6c6b660f2ba481839f 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=482d7223bd3c4cde58ec74cce71fee34 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c187e274255f2556b74d812d539ece21 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=eafceae3e40f7d31f19d50ea16a86b5c 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/a48be4d-image.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=59ccc55c957e3fdb929261bff2e92df9 2500w" />

All the other options can be specified using api requests.

## Required - Container Gateway Setup

In addition you need to specify the port your api will be available through. Default port for Ollama is 11434

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=9a36c1e9c5607a3da189ad75b25c4cb1" data-og-width="529" width="529" data-og-height="498" height="498" data-path="container-engine/images/af91390-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=07ec4308d5d1e68c0ebaeb4a777d24e1 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=8147224555c09b529c873401fa8611ec 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5fa2923d1da898ec98fea43947e2cc3b 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e99afce25268f49d4c9915441eb4ddc3 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=274bef852891f12e5a02150c668155a4 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/af91390-image.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=981e3a3277a14dc3bbd4f5315c74afc2 2500w" />
