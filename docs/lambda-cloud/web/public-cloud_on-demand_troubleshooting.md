# Troubleshooting -

Source: https://docs.lambda.ai/public-cloud/on-demand/troubleshooting/

---

[on-demand cloud ](../../../tags/#tag:on-demand-cloud)
# Troubleshooting [# ](#troubleshooting)

## apt full-upgrade fails on Lambda Stack 24.04 and GPU Base 24.04 images [# ](#apt-full-upgrade-fails-on-lambda-stack-2404-and-gpu-base-2404-images)

As of December 2025, running `sudo apt full-upgrade`or `sudo apt dist-upgrade`on the Lambda Stack 24.04 or GPU Base 24.04 base images produces an error: 

```
`[](#__codelineno-0-1)Error! Bad return status for module build on kernel: 6.14.0-1013-nvidia (x86_64)
[](#__codelineno-0-2)Consult /var/lib/dkms/mlnx-ofed-kernel/24.10.OFED.24.10.3.2.5.1/build/make.log for more information.
`
```
