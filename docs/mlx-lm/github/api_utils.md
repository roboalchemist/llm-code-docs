# Source: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/utils.py

## API Reference

```python
def _unpack_awq_weights(qweight: mx.array) -> mx.array:
def _transform_awq_weights(
def _get_classes(config: dict):
    """
    Retrieve the model and model args classes based on the configuration.

    Args:
        config (dict): The model configuration.

    Returns:
        A tuple containing the Model class and the ModelArgs class.
def get_total_parameters(model):
    def nparams(m):
def compute_bits_per_weight(model):
def _download(
    """
    Ensures the model is available locally. If the path does not exist locally,
    it is downloaded from the Hugging Face Hub.

    Args:
        path_or_hf_repo (str): The local path or Hugging Face repository ID of the model.
        revision (str, optional): A revision id which can be a branch name, a tag, or a commit hash.

    Returns:
        Path: The local file path.
def hf_repo_to_path(hf_repo):
def load_config(model_path: Path) -> dict:
def load_model(
    """
    Load and initialize the model from a given path.

    Args:
        model_path (Path): The path to load the model from.
        lazy (bool): If False eval the model parameters to make sure they are
            loaded in memory before returning, otherwise they will be loaded
            when needed. Default: ``False``
        strict (bool): Whether or not to raise an exception if weights don't
            match. Default: ``True``
        model_config (dict, optional): Optional configuration parameters for the
            model. Defaults to an empty dictionary.
        get_model_classes (Callable[[dict], Tuple[Type[nn.Module], Type]], optional):
            A function that returns the model class and model args class given a config.
            Defaults to the ``_get_classes`` function.

    Returns:
        Tuple[nn.Module, dict[str, Any]]: The loaded and initialized model and config.

    Raises:
        FileNotFoundError: If the weight files (.safetensors) are not found.
        ValueError: If the model class or args class are not found or cannot be instantiated.
    def _quantize(quantization):
        def class_predicate(p, m):
def load_adapters(model: nn.Module, adapter_path: str) -> nn.Module:
def load_tokenizer(model_path, tokenizer_config_extra=None, eos_token_ids=None):
    """Load a huggingface tokenizer and try to infer the type of streaming
    detokenizer to use.
def load(
    """
    Load the model and tokenizer from a given path or a huggingface repository.

    Args:
        path_or_hf_repo (Path): The path or the huggingface repository to load the model from.
        tokenizer_config (dict, optional): Configuration parameters specifically for the tokenizer.
            Defaults to an empty dictionary.
        model_config(dict, optional): Configuration parameters specifically for the model.
            Defaults to an empty dictionary.
        adapter_path (str, optional): Path to the LoRA adapters. If provided, applies LoRA layers
            to the model. Default: ``None``.
        lazy (bool): If ``False`` eval the model parameters to make sure they are
            loaded in memory before returning, otherwise they will be loaded
            when needed. Default: ``False``
        return_config (bool: If ``True`` return the model config as the last item..
        revision (str, optional): A revision id which can be a branch name, a tag, or a commit hash.
    Returns:
        Union[Tuple[nn.Module, TokenizerWrapper], Tuple[nn.Module, TokenizerWrapper, Dict[str, Any]]]:
            A tuple containing the loaded model, tokenizer and, if requested, the model config.

    Raises:
        FileNotFoundError: If config file or safetensors are not found.
        ValueError: If model class or args class are not found.
def sharded_load(
def pipeline_load(repo, return_config=False):
def make_shards(weights: dict, max_file_size_gb: int = MAX_FILE_SIZE_GB) -> list:
    """
    Splits the weights into smaller shards.

    Args:
        weights (dict): Model weights.
        max_file_size_gb (int): Maximum size of each shard in gigabytes.

    Returns:
        list: List of weight shards.
def create_model_card(path: Union[str, Path], hf_path: Union[str, Path, None]):
    """
    Uploads the model to Hugging Face hub.

    Args:
        path (Union[str, Path]): Local path to the model.
        hf_path (Union[str, Path, None]): Path to the original Hugging Face model.
def upload_to_hub(path: str, upload_repo: str):
```
