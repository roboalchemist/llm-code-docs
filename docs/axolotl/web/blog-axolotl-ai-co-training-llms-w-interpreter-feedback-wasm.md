# Source: https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm

Title: Training Large Language Models with Interpreter Feedback using WebAssembly

URL Source: https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm

Markdown Content:
[Back to Articles](https://huggingface.co/blog)

[![Image 1: Salman Mohammadi's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/64e4d0707d26615b5d4bf775/c8EbVvgGvQW7fgHdKI6fh.jpeg)](https://huggingface.co/smohammadi)

[![Image 2: wing lian's avatar](https://cdn-avatars.huggingface.co/v1/production/uploads/641dfddf3bae5a77636817c5/2IwNwh9kK98eCHUmOGoWD.png)](https://huggingface.co/winglian)

* [Introduction](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#introduction "Introduction")

* [Training with Code Interpreter Feedback](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#training-with-code-interpreter-feedback "Training with Code Interpreter Feedback")

* [Reward functions](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#reward-functions "Reward functions")

* [Multiprocessing](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#multiprocessing "Multiprocessing")

* [Training](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#training "Training")
  * [Installation](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#installation "Installation")

  * [Training](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#training-1 "Training")

* [Evaluations](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#evaluations "Evaluations")

* [Next steps](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#next-steps "Next steps")

_A fast, local, and secure approach to training LLMs for code with WebAssembly and interpreter-based rewards_

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#introduction) Introduction

We’re excited to share an open-source tool for safe and entirely local training of code generation models in Python which builds upon on our recent work on supporting Group Relative Policy Optimization (GRPO) [in axolotl](https://axolotlai.substack.com/p/axolotl-update-v070-with-grpo). We make it easy to self-host a sandboxed code interpreter environment, so you can fine-tune with zero setup!

By utilizing [WebAssembly](https://webassembly.org/) we can execute untrusted code in an isolated and resource-constrained environment. On top of this, we’ve implemented multi-processing to minimize the overhead of executing the code interpreter, resulting in a robust and lightning-fast training procedure. To get up and running right away, check out our [grpo_code repository](https://github.com/axolotl-ai-cloud/grpo_code)!

[![Image 3: image/png](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/_Pk0d00VqEurOYe2F1yjU.png)](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/_Pk0d00VqEurOYe2F1yjU.png)

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#training-with-code-interpreter-feedback) Training with Code Interpreter Feedback

There has been significant effort to replicate the recent success of DeepSeek’s R1 training procedure, which eschews the typical supervised fine-tuning (SFT) stage for reinforcement learning by training on domains where the outputs of the model can be automatically verified, such as math problems and coding tasks. While verifying the correctness of math problems is relatively straightforward, verifying the correctness of code is non-trivial and requires executing the code in a safe and controlled environment.

The effectiveness of GRPO hinges on well-formed reward functions which reliably guide the model towards our desired behavior. In order to train a model on the output of a code interpreter, we need to translate the output of the interpreter into some form of success criterion. Fortunately, several coding datasets exist which provide test cases which can be used to verify the behavior of code at runtime.

Let’s take [TIGER-Lab/AceCode-87K](https://huggingface.co/datasets/TIGER-Lab/AceCode-87K) as an example of such a dataset. This dataset consists of a problem statement to implement a function or class in Python, along with executable assertions which verify the behavior of this functionality:

```
{
    "question": "Given a list of strings, implement a function `find_palindromes` that returns a new list containing only the strings that are palindromes. A palindrome is defined as a word that reads the same forward and backward, ignoring case and spaces. For example, if the input list is `['radar', 'hello', 'level', 'world', 'Anna']`, the function should return `['radar', 'level', 'Anna']`. Your function should handle empty strings and variations in case appropriately.",
    "test_cases": [
        "assert find_palindromes(['radar', 'hello', 'level', 'world', 'Anna']) == ['radar', 'level', 'Anna']",
        "assert find_palindromes(['racecar', 'civic', 'deified', 'hello', 'world']) == ['racecar', 'civic', 'deified']",
        "assert find_palindromes(['noon', 'test', 'rotor', 'python']) == ['noon', 'rotor']",
        "assert find_palindromes(['']) == ['']",
        "assert find_palindromes(['Able was I ere I saw Elba', 'Hello']) == ['Able was I ere I saw Elba']",
        "assert find_palindromes(['12321', '12345', '121']) == ['12321', '121']",
        "assert find_palindromes(['Madam', 'Hello World', 'noon']) == ['Madam', 'noon']",
        "assert find_palindromes(['123321', 'abcba', 'xyz']) == ['123321', 'abcba']",
        "assert find_palindromes(['']) == ['']",
        "assert find_palindromes(['level', 'Level', 'LEVEL']) == ['level', 'Level', 'LEVEL']",
        "assert find_palindromes(['abccba', 'abc', 'a']) == ['abccba', 'a']",
        "assert find_palindromes(['step on no pets', 'sample text']) == ['step on no pets']",
        "assert find_palindromes(['no lemon, no melon']) == ['no lemon, no melon']",
        "assert find_palindromes(['racecar', 'not a palindrome']) == ['racecar']",
        "assert find_palindromes(['']) == ['']",
        "assert find_palindromes(['Wow', 'wow', 'WOW']) == ['Wow', 'wow', 'WOW']",
        "assert find_palindromes(['abc', 'def', 'ghi']) == []"
    ]
}
```

Great! As long as we have a way to execute the code predicted by our model during training alongside each assertion in the associated list of test cases, we can provide a reward signal to optimize our model for maximizing accuracy across the test cases. However, we don’t want to arbitrarily execute LLM-generated code - while it’s unlikely that models will generate outright malicious code when training on competitive coding style datasets like AceCode-87K, we do wish to mitigate any unintended side-effects of executing untrusted code which could interfere with the training environment or consume large amounts of system resources.

There are existing solutions for sandboxing untrusted code. Cloud providers such as [E2B](https://e2b.dev/) offer support for executing untrusted code in a secure cloud environment, but require a paid subscription after limited use, and containerized solutions such as [piston](https://github.com/engineer-man/piston) and kernel-level sandboxes such as [isolate](https://github.com/ioi/isolate) are non-trivial to self-host and configure.

[WebAssembly](https://webassembly.org/) (Wasm) is a binary instruction format designed as a portable compilation target for programming languages. Wasm code runs in a secure, sandboxed virtual environment isolated from the host system and with well-defined resource constraints (which we refer to as “fuel”). Thanks to [VMware Labs](https://wasmlabs.dev/articles/python-wasm32-wasi/)’ pre-compiled Python 3.12.0 Wasm runtime binary, we can safely execute Python code in our local training environment with minimal setup and overhead. We adapted our Wasm runtime implementation from [Simon Wilson’s blogpost](https://til.simonwillison.net/webassembly/python-in-a-wasm-sandbox) on executing Python in a Wasm sandbox.

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#reward-functions) Reward functions

Let’s tie all this together by defining reward functions which utilise our secure Wasm runtime:

* `grpo_code.code_execution_reward_func` provides a reward signal for code completions which can successfully execute without errors.

* `grpo_code.answer_execution_reward_func` provides a reward signal based on the accuracy of the code completions against the provided test cases. Rather than simply using the percentage of test cases that pass, we apply a power law of 2 * (accuracy)^3 to provide substantially higher rewards for increasingly accurate code completions.

* `grpo_code.soft_format_reward_func` enforces a formatting constraint on the code completions - this was necessary to correctly extract the predicted code from the model’s output.

[![Image 4: image/png](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/rARg3-ZCTDX8plJMis4Bs.png)](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/rARg3-ZCTDX8plJMis4Bs.png)

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#multiprocessing) Multiprocessing

Utilizing multiprocessing to asynchronously execute environment updates is a common paradigm in reinforcement learning to minimize GPU idle time. We provide a simple multiprocessing implementation which uses a reusable process worker pool to asynchronously execute Wasm code - in our benchmarks we found this to result in almost 10x speedups in code execution time. You can configure the number of processes by setting the MAX_WORKERS environment variable - we recommend utilizing fewer workers than there are available cores on your machine and scaling workers as a function of your batch size, number of generations, and world size.

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#training) Training

To make it easy to get started, let’s follow the process of training a model on the AceCode-87K dataset - you can find our [trained model here](https://huggingface.co/axolotl-ai-co/qwen2-3b-instruct-code-grpo).

#### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#installation) Installation

```
git clone https://github.com/axolotl-ai-cloud/grpo_code
cd grpo_code
pip install -e .
pip install axolotl==0.8.0[vllm]
```

#### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#training-1) Training

The following environment variables can be used to modify the behavior of the reward functions during training.

`WASM_FUEL` - Controls the amount of fuel (computation resources) allocated to the Wasm environment (default: 10000000000). The fuel mechanism in WebAssembly counts the number of executed operations, and returns to the caller if the configured limit is exceeded.

`WASM_PATH` - Path to the Python Wasm runtime file (default: “./wasm/python-3.12.0.wasm”)

`TIMEOUT` - Maximum execution time in seconds for code evaluation (default: 1)

`MAX_WORKERS` - Number of parallel workers for multiprocessing reward functions. By default, multiprocessing is disabled. When training across multiple GPUs, MAX_WORKERS is divided by the total world size.

We trained our model on 4 A100 GPUs for ~16 hours. First, set up the vLLM server utilizing two of our four GPUs - ensure you’re using the last GPUs here by setting CUDA_VISIBLE_DEVICES :

```
CUDA_VISIBLE_DEVICES=2,3 axolotl vllm-serve r1_acecode.yaml
```

Then, in another terminal, run the training script:

```
CUDA_VISIBLE_DEVICES=0,1 MAX_WORKERS=64 axolotl train r1_acecode.yaml --num-processes 2
```

You should see the following training graphs showing stable convergence across all reward functions and a final test case accuracy reward of ~85%:

[![Image 5: image/png](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/iclLYI_q6qaCMfJsLJUoL.png)](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/iclLYI_q6qaCMfJsLJUoL.png)

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#evaluations) Evaluations

We’ve included an [example evaluation script](https://github.com/axolotl-ai-cloud/grpo_code/tree/main/eval_plus) in the `eval_plus` folder of our repo, which we adapted from the [Qwen2.5-Coder repository](https://github.com/QwenLM/Qwen2.5-Coder/tree/main/qwencoder-eval/instruct/eval_plus) with updated dependencies for better reproducibility.

To run the evaluation, first install the required packages. In a fresh Python environment, run:

```
cd eval_plus
pip install evalplus --upgrade
pip install -r requirements.txt
```

Then, run the evaluation script:, making sure you have the weights of the model you wish to evaluate available on your filesystem:

```
bash test.sh {path_to_your_local_model_checkpoint} {tensor_parallel_size} {output_dir}
```

You should see evaluation results for HumanEval and MBPP in the output_dir folder for your model. We’ve included the results for our trained model below, which we benchmarked against Qwen2.5-Coder-3B-Instruct and the base model for our training run, Qwen2.5-3B-Instruct:

[![Image 6: image/png](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/7McYCoEmaIAuivLY3EJUH.png)](https://cdn-uploads.huggingface.co/production/uploads/641dfddf3bae5a77636817c5/7McYCoEmaIAuivLY3EJUH.png)

We used Qwen2.5-3B-Instruct and Qwen2.5-Coder-3B-Instruct as baselines for our evaluations. Qwen2.5-3B-Instruct was used as the base model for our fine-tuning, and helps us measure the direct impact of fine-tuning using interpreter feedback.

Qwen2.5-Coder-3B-Instruct used Qwen2.5-3B (non-instruct) as a base model, and instead underwent significant coding-based continued pre-training (CPT), instruction supervised fine-tuning (SFT), and Direct Preference Optimization using code execution feedback. These training steps used vast amounts of data: 5.2 trillion tokens for coding-specific continued pre-training, and tens of millions of instruction samples. Evaluating against Qwen2.5-Coder-3B-Instruct helps us understand the relative performance improvements from extensive training using CPT, SFT, and alignment fine-tuning, versus using a comparatively tiny amount of reinforcement-learning based code-interpeter fine-tuning.

We observe a substantial improvement relative to our base model, Qwen2.5-3B-Instruct, and Qwen2.5-Coder-3B-Instruct, in the [Mostly Basic Python Programming](https://huggingface.co/datasets/google-research-datasets/mbpp) (MBPP) and [MBPP+](https://huggingface.co/datasets/evalplus/mbppplus) benchmarks which comprise entry-level programming problems solvable by using only standard library functions. We also found improvements over our base model on the [Human Eval](https://huggingface.co/datasets/openai/openai_humaneval) and [Human Eval+](https://huggingface.co/datasets/evalplus/humanevalplus) benchmarks. We think these results show huge potential for fine-tuning using reinforcement learning and code interpreter feedback for producing highly capable domain-specific models.

### [](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm#next-steps) Next steps

We've introduced a lightweight and extensible framework for training code generation models with interpreter feedback. We think this is a promising direction for training more reliable and robust code generation models, and are excited to see what the community will build on top of this work. This could include support for more challenging datasets on multiple coding tasks, cross-language support, or multi-task training across math and code datasets.

We’ve also recently added support for [sequence-parallel](https://axolotlai.substack.com/p/enabling-long-context-training-with) in axolotl - we think this could unlock long-context fine-tuning with GRPO to tackle complex coding tasks which would benefit from much longer reasoning traces.
