# Source: https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/server.py

## API Reference

```python
def get_system_fingerprint():
class StopCondition(NamedTuple):
def stopping_criteria(
    """
    Determines whether the token generation should stop based on predefined
    conditions.

    Args:
        tokens (List[int]): The current sequence of generated tokens.
        eos_token_ids (set): The token IDs that represents the
          end-of-sequence. If the last token in ``tokens`` is in the set,
          the generation should stop.
        stop_id_sequences (List[List[[int]]): A list of integer lists, each
          representing a sequence of token IDs. If the end of the `tokens`
          list matches any of these sequences, the generation should stop.
        stop_words (List[str]): The stop words that correspond to the
            ``stop_id_sequences``.

    Returns:
        StopCondition: A named tuple indicating whether the stop condition has
          been met (`stop_met`) and how many tokens should be trimmed from the
          end if it has (`trim_length`) as well as the text that should be
          trimmed.
def sequence_overlap(s1: Sequence, s2: Sequence) -> bool:
    """
    Checks if a suffix of s1 has overlap with a prefix of s2

    Args:
        s1 (Sequence): The first sequence
        s2 (Sequence): The second sequence

    Returns:
        bool: If the two sequences have overlap
def convert_chat(messages: List[dict], role_mapping: Optional[dict] = None):
def process_message_content(messages):
    """
    Convert message content to a format suitable for `apply_chat_template`.

    The function operates on messages in place. It converts the 'content' field
    to a string instead of a list of text fragments.

    Args:
        message_list (list): A list of dictionaries, where each dictionary may
          have a 'content' key containing a list of dictionaries with 'type' and
          'text' keys.

    Raises:
        ValueError: If the 'content' type is not supported or if 'text' is missing.

class LRUPromptCache:
    class CacheEntry:
    class SearchResult:
    def __init__(self, max_size: int = 10):
    def _search(self, model, tokens):
        """Search the cache for a prompt cache. Return exact or close match."""
        if model not in self._cache:
            return self.SearchResult(model, None, None, None, 0)

        current = self._cache[model]
        last_cache_index = -1
        index = 0

        while index < len(tokens) and tokens[index] in current:
            current = current[tokens[index]]
            if "cache" in current:
                last_cache_index = index
            index += 1

        # Exact match no need to search for longer or shorter caches
        if last_cache_index == len(tokens) - 1:
            return self.SearchResult(model, tokens, None, None, 0)

        # Find the shorter cache
        shorter = None
        if last_cache_index > 0:
            shorter = tokens[: last_cache_index + 1]

        # Check for caches that are longer
        longer = None
        common_prefix = index
        if index > 0 and last_cache_index <= 0:
            best = None
            stack = [(current, [])]
            while stack:
                current, extra = stack.pop()
                if "cache" in current:
                    if best is None or len(extra) < len(best):
                        best = extra
                else:
                    for tok in current:
                        stack.append((current[tok], extra + [tok]))
            longer = tokens[:index] + best
        return self.SearchResult(model, None, shorter, longer, common_prefix)

    def _get(self, model, tokens):
        current = self._cache[model]
        for tok in tokens:
            current = current[tok]
        return current["cache"]

```
