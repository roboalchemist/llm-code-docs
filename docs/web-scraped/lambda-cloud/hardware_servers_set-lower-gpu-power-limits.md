# Set lower power limits (TDPs) for NVIDIA GPUs -

Source: https://docs.lambda.ai/hardware/servers/set-lower-gpu-power-limits/

---

# Set lower power limits (TDPs) for NVIDIA GPUs [# ](#set-lower-power-limits-tdps-for-nvidia-gpus)

You can set lower power limits (TDPs) for your NVIDIA GPUs using `nvidia-smi`and a simple script. You can configure the script to run automatically at boot using a systemd service. 

Lowering power limits can reduce power usage and heat output, which is helpful for thermally constrained systems or energy-aware environments. 

- 
**Check your GPU's minimum power limit. **Run: 

```
`[](#__codelineno-0-1)nvidia-smi -q -d POWER
`
```
