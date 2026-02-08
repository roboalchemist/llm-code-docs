# Using the nvidia-bug-report.log file to troubleshoot your system -

Source: https://docs.lambda.ai/education/linux-usage/using-the-nvidia-bug-report.log-file-to-troubleshoot-your-system/

---

# Using the nvidia-bug-report.log file to troubleshoot your system [# ](#using-the-nvidia-bug-reportlog-file-to-troubleshoot-your-system)

NVIDIA provides a script that generates a log file that you can use to troubleshoot issues with NVIDIA GPUs. This log file has comprehensive information about your system, including information about individual devices, configuration of NVIDIA drivers, system journals, and more. 

## Generate the log file [# ](#generate-the-log-file)

To generate the log file, log in as the root user or use `sudo`, then run the following command: 

```
`[](#__codelineno-0-1)sudo nvidia-bug-report.sh
`
```
