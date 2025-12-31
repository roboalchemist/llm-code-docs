# Source: https://docs.vllm.ai/en/stable/examples/online_serving/utils/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/examples/online_serving/utils.md "Edit this page")

# Utils[¶](#utils "Permanent link")

Source <https://github.com/vllm-project/vllm/blob/main/examples/online_serving/utils.py>.

    # SPDX-License-Identifier: Apache-2.0
    # SPDX-FileCopyrightText: Copyright contributors to the vLLM project
    from openai import APIConnectionError, OpenAI
    from openai.pagination import SyncPage
    from openai.types.model import Model

    def get_first_model(client: OpenAI) -> str:
        """
        Get the first model from the vLLM server.
        """
        try:
            models: SyncPage[Model] = client.models.list()
        except APIConnectionError as e:
            raise RuntimeError(
                "Failed to get the list of models from the vLLM server at "
                f" with API key . Check\n"
                "1. the server is running\n"
                "2. the server URL is correct\n"
                "3. the API key is correct"
            ) from e

        if len(models.data) == 0:
            raise RuntimeError(f"No models found on the vLLM server at ")

        return models.data[0].id