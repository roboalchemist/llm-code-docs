# Install other ML libraries
pip install transformers peft accelerate
```

#### For CPU-Only Environments

```bash
pip install torch transformers peft accelerate
```

#### Package Requirements

| Package | Minimum Version | Purpose |
|---------|-----------------|---------|
| `torch` | >= 2.0 | Deep learning framework |
| `transformers` | >= 4.40.0 | Model loading and inference |
| `peft` | >= 0.10.0 | LoRA adapter support |
| `accelerate` | >= 0.27.0 | Device management |

:::tip Verify GPU Support
After installation, verify that PyTorch can detect your GPU:
```bash
python3 -c "import torch; print('PyTorch version:', torch.__version__); print('CUDA available:', torch.cuda.is_available())"
```
If `CUDA available: False`, you may need to reinstall PyTorch with the correct CUDA version.
:::

### Account Management

For comprehensive account management, including viewing balances, managing sub-accounts, and handling refunds, see [Account Management](./account-management).

Quick CLI commands:
```bash