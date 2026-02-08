# Lambda Stack and recovery images -

Source: https://docs.lambda.ai/education/linux-usage/lambda-stack-and-recovery-images/

---

# Lambda Stack and recovery images [# ](#lambda-stack-and-recovery-images)

## Removing and reinstalling Lambda Stack [# ](#removing-and-reinstalling-lambda-stack)

To remove and reinstall [Lambda Stack ](https://lambda.ai/lambda-stack-deep-learning-software): 

Uninstall (purge) the existing Lambda Stack by running: 

```
`[](#__codelineno-0-1)sudo rm -f /etc/apt/sources.list.d/{graphics,nvidia,cuda}* && \
[](#__codelineno-0-2)dpkg -l | \
[](#__codelineno-0-3)awk '/cuda|lib(accinj64|cu(blas|dart|dnn|fft|inj|pti|rand|solver|sparse)|magma|nccl|npp|nv[^p])|nv(idia|ml)|tensor(flow|board)|torch/ { print $2 }' | \
[](#__codelineno-0-4)sudo xargs -or apt -y remove --purge
`
```
