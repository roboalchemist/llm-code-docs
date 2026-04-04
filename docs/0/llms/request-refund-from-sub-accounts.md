# Request refund from sub-accounts
0g-compute-cli retrieve-fund
```

### Other Commands

#### Upload Dataset Separately

You can upload a dataset to 0G Storage before creating a task:

```bash
0g-compute-cli fine-tuning upload --data-path <PATH_TO_DATASET>
```

#### Download Data

You can download previously uploaded datasets from 0G Storage:

```bash
0g-compute-cli fine-tuning download --data-path <PATH_TO_SAVE_DATASET> --data-root <DATASET_ROOT_HASH>
```

#### View Task List

You can view the list of tasks submitted to a specific provider using the following command:

```bash
0g-compute-cli fine-tuning list-tasks  --provider <PROVIDER_ADDRESS>
```

#### Cancel a Task

You can cancel a task before it starts running using the following command:

```bash
0g-compute-cli fine-tuning cancel-task --provider <PROVIDER_ADDRESS> --task <TASK_ID>
```

**Note:** Tasks that are already in progress or completed cannot be canceled.

## Troubleshooting

<details>
<summary>Error: MinimumDepositRequired</summary>

This means the provider's fine-tuning sub-account has insufficient funds. Make sure to include `--service fine-tuning` when transferring funds:

```bash
0g-compute-cli transfer-fund --provider <PROVIDER_ADDRESS> --amount 2 --service fine-tuning
```

</details>

<details>
<summary>Error: Provider busy</summary>

The provider is processing another task. Options:
1. Wait and retry later
2. Use a different provider: `0g-compute-cli fine-tuning list-providers`
3. Queue your task (you'll be prompted)
</details>

<details>
<summary>Error: Insufficient balance</summary>

Add more funds:
```bash
0g-compute-cli deposit --amount 3
0g-compute-cli transfer-fund --provider <PROVIDER_ADDRESS> --amount 2 --service fine-tuning
```
</details>

<details>
<summary>Error: "second arg must be public key" when decrypting</summary>

This means the provider hasn't finished settlement yet. Wait about 1 minute after `acknowledge-model`, then check the task status:

```bash
0g-compute-cli fine-tuning get-task --provider <PROVIDER_ADDRESS> --task <TASK_ID>
```

When `Progress` shows `Finished`, retry the `decrypt-model` command.
</details>

<details>
<summary>Error: "Unexpected non-whitespace character after JSON" when creating task</summary>

Check your training configuration JSON file:
- Ensure valid JSON format
- Use decimal notation for numbers (e.g., `0.0002` instead of `2e-4`)
- Verify no trailing commas
</details>

---

## Inference Provider

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';