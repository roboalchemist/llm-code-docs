# Source: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/gguf.py

## API Reference

```python
class TokenType(IntEnum):
class GGMLFileType(IntEnum):
class HfVocab:
    def __init__(
    def hf_tokens(self) -> Iterable[Tuple[bytes, float, TokenType]]:
    def get_token_type(
    def get_token_score(self, token_id: int) -> float:
    def added_tokens(self) -> Iterable[Tuple[bytes, float, TokenType]]:
    def has_newline_token(self):
    def all_tokens(self) -> Iterable[Tuple[bytes, float, TokenType]]:
    def __repr__(self) -> str:
    def load(path: Path) -> "HfVocab":
def translate_weight_names(name):
def permute_weights(weights, n_head, n_head_kv=None):
def prepare_metadata(config, vocab):
def convert_to_gguf(
```
