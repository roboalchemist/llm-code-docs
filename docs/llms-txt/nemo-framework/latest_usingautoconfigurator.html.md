# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md

Title: Use Auto Configurator to Find the Optimal Configuration#

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html

Published Time: Fri, 18 Jul 2025 19:29:23 GMT

Markdown Content:
Auto Configurator searches for hyperparameters (HPs) that achieve the maximum highest training throughput when working with Large Language Models (LLMs) utilizing the NeMo Framework.

Note

Auto Configurator is supported for Bert, T5, and GPT-based models: GPT3, LLama, Mixtral, Mistral, Gemma, Nemotron, Starcoder, and Qwen.

Auto Configurator Capabilities[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#auto-configurator-capabilities "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Auto Configurator is intended to iterate over different model configurations quickly and find the best configuration, that is, the configuration that minimizes both time and financial expenditure. It offers a range of features to facilitate this, as detailed in the list below.

*   Model size recommendation: finds the optimal model size if the parameter is not specified.

*   Training time estimation: estimates model training time based on input parameters.

*   Hyperparameters recommendation: finds the optimal list of hyperparameters to be trained.

*   Optimal configuration recommendation: calculates the performance after a short training of candidate configurations and finds the optimal model configuration.

Note

Auto Configurator supports model size and hyperparameters recommendations only for pretrain mode. For finetune mode, the user is expected to specify lists of model parallelism parameters.

### Model Size Recommendation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#model-size-recommendation "Link to this heading")

If you have not decided what model size you want to train, Auto Configurator can recommend a model size for your use case. If you know the number of GPUs, TFLOPS per GPU, the maximum time to train, and the number of tokens to train for, it can recommend a model size that can be trained with the specified hardware and time constraints.

For example, if you had 20 NVIDIA DGX nodes available (in 80 GB GPU memory), and wanted to train a GPT model for a maximum of 5 days, Auto Configurator would recommend using a 5B parameter GPT model.

### Training Time Estimation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#training-time-estimation "Link to this heading")

Auto Configurator calculates the estimated training time for your model. It provides a projection of the training time in days, based on the input dataset and parameters you provide.

### Hyperparameters Recommendation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#hyperparameters-recommendation "Link to this heading")

After Auto Configurator generates the base configuration, it searches over four critical hyperparameters that have a great impact on training throughput but do not affect model convergence. These hyperparameters include Tensor Parallelism (TP), Pipeline Parallelism (PP), Context Parallelism (CP), Expert Parallelism (EP), Micro Batch Size (MBS), and Activation Checkpointing Layers (ActCkpt). Auto Configurator will also provide optimal Global Batch Size (GBS) if it’s not specified.

Auto Configurator initially applies heuristics to identify suitable candidates for the four key parameters, subsequently generating a grid of candidate configurations. It returns all of the candidate configurations in NeMo 2.0 format.

Note

Some of the candidate configurations may not work due to high-memory usage or other issues.

Once the candidate configurations are generated, you can use NeMo Framework to launch the most promising candidates.

When running the candidates on the cluster, you can limit job time and job max steps by using `max_minutes_per_run` and `max_steps_per_run` parameters. During this search, the jobs will run with the number of nodes specified in the configuration files, using the `num_nodes` parameter. Once all of the jobs have finished running, you’ll need to run compare_throughput.py to get a .csv table with performance results for each succeeded job.

### Optimal Configuration Recommendation[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#optimal-configuration-recommendation "Link to this heading")

After all of the candidate jobs are done, Auto Configurator calculates performance parameters for each of the candidates. Auto Configurator generates two .csv files: one detailing the performance measures of the candidates and another listing the candidates that failed due to out-of-memory errors.

### Configurations Generation Example[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#configurations-generation-example "Link to this heading")

The following list shows the required input parameters for the Auto Configurator runner:

*   `recipe`: model recipe based on NeMo 2.0.

*   `path_to_logs`: path to the directory where the logs will be stored.

The following list shows the optional parameters for the Auto Configurator runner:

*   `mode`: a string, `pretrain` or `finetune` mode.

*   `tensor_parallel_sizes`: a list, such as `[1, 2, 4]`.

*   `pipeline_parallel_sizes`: a list, such as `[1, 2, 4]`.

*   `context_parallel_sizes`: a list, such as `[1, 2, 4]`.

*   `expert_parallel_sizes`: a list, such as `[1, 2, 4]`.

*   `micro_batch_sizes`: a list, such as `[1, 2, 4]`.

*   `min_model_parallel_size`: a value for the minimum desired parallelism.

*   `max_model_parallel_size`: a value for the maximum desired parallelism.

For each of the optional parameters, Auto Configurator will find the optimal value if the parameter is not specified. To view the full list of parameters, please visit [this page](https://github.com/NVIDIA/NeMo/blob/main/nemo/collections/llm/tools/auto_configurator/runner.py.md#L68).

We provide an example below on how to generate configurations by a given **pretrain** recipe:

from functools import partial
from nemo.collections import llm
from nemo.collections.llm.tools.auto_configurator import AutoConfigurator, generate_configs

# Import recipe and change needed parameters
recipe = partial(llm.llama3_8b.pretrain_recipe, num_nodes=128, num_gpus_per_node=8)()
recipe.model.config.seq_length = recipe.data.seq_length = 8192
recipe.data.global_batch_size = 512

# Set this value to True if you want Auto Configurator
# to calculate size for your model based on given parameters.
# Auto Configurator will also change num_layers, num_attention_heads, hidden_size, ffn_hidden_size
# for given recipe in respect to calculated model size.
calculate_model_size = False

# Initialize Auto Configurator runner
runner = AutoConfigurator(
   recipe=recipe,
   path_to_logs="/path/to/save/logs",
   gpu_memory_gb=80,
   tensor_parallel_sizes=[1,2],
   pipeline_parallel_sizes="auto",
   context_parallel_sizes=[1,2],
   micro_batch_sizes="auto",
   max_model_parallel_size=4,
   min_model_parallel_size=1,
   max_training_days=7,
   max_steps_per_run=50,
   max_minutes_per_run=20,
   num_tokens_in_b=840,
   vocab_size=32000,
   calculate_model_size=calculate_model_size,
)

# Generate configs (NeMo 2.0 reicpes) with different model parallelism.
base_config, configs = generate_configs(runner)

Example output of the above script:

You can train a 8B parameter model in 4.34 days using 1024 GPUs. This result assumes you are training to 840B tokens, and each GPU achieves 140 TFLOPS.
Valid config: SeqLen=8192, GBS=512, MBS=1, TP=1, PP=2, CP=1, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=1, TP=1, PP=2, CP=2, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=1, TP=2, PP=1, CP=1, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=1, TP=2, PP=1, CP=2, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=1, TP=2, PP=2, CP=1, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=2, TP=2, PP=2, CP=1, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=1, TP=2, PP=2, CP=2, EP=1, VP=None. Adding to directory.
Valid config: SeqLen=8192, GBS=512, MBS=2, TP=2, PP=2, CP=2, EP=1, VP=None. Adding to directory.

All candidate configurations created correctly. Total number of configs: 8.

We also provide an example on how to generate configurations by a given **finetune** recipe:

from functools import partial
from nemo.collections import llm
from nemo.collections.llm.tools.auto_configurator import AutoConfigurator, generate_configs

# Import recipe and change needed parameters
recipe = partial(
   llm.llama3_8b.finetune_recipe,
   num_nodes=16,
   num_gpus_per_node=8,
   dir='/path/to/pretrained/model',
   scheme='lora',
)()
recipe.model.config.seq_length = recipe.data.seq_length = 4096
recipe.data.global_batch_size = 128

# Initialize Auto Configurator runner.
# Please, make sure you specified all the model parallelism parameters
# since 'finetune' mode doesn't support auto selection.
runner = AutoConfigurator(
   recipe=recipe,
   path_to_logs="/path/to/save/logs",
   mode="finetune",
   gpu_memory_gb=80,
   tensor_parallel_sizes=[1,2,4],
   pipeline_parallel_sizes=[1,2],
   context_parallel_sizes=[1,2],
   micro_batch_sizes=[1,2,4],
   max_model_parallel_size=8,
   min_model_parallel_size=1,
   max_steps_per_run=25,
   max_minutes_per_run=20,
   num_tokens_in_b=140,
   vocab_size=32000,
)

# Generate configs (NeMo 2.0 reicpes) with different model parallelism.
base_config, configs = generate_configs(runner)

### Calculate Performance[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#calculate-performance "Link to this heading")

We provide an example below on how to calculate the performance and get the optimal configuration after all the generated recipes were trained:

from nemo.collections.llm.tools.auto_configurator import get_results

# Generate results
# The results will be saved in .csv format
get_results(
   base_config=base_config, # base_config which was given by generate_configs function
   runner=runner, # runner which was used for config generation
   path_to_save="/path/to/save/results" # Path where to save the results
   output_top_n=10, # Print out top n configurations
   log_file_prefix="log", # Prefix of the logs file
)

Example output of the above script:

All candidate configurations created correctly. Total number of configs: 3.

Top 3 configs sorted from fastest to slowest:
Config 1: 53.62 TFLOPS per GPU with 0.5400s per global step.
Config 2: 50.79 TFLOPS per GPU with 0.5700s per global step.
Config 3: 46.7 TFLOPS per GPU with 0.6200s per global step.

==================================================
Optimal config: llama_0.145b_1nodes_tp_1_pp_1_cp_1_ep_1_mbs_4_vp_None with 0.5400s per global step.
==================================================

The results were successfully saved to /home/llama_auto_conf.

### End-To-End Example[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#end-to-end-example "Link to this heading")

To view an end-to-end example of how to generate candidate configs, train them, and calculate the performance using Auto Configurator with NeMo Framework, please visit [this page](https://github.com/NVIDIA/NeMo/blob/main/examples/llm/auto_configurator/auto_config.py.md).

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/usingautoconfigurator.html.md#end-to-end-example)
- [this page](https://github.com/NVIDIA/NeMo/blob/main/examples/llm/auto_configurator/auto_config.py.md)
