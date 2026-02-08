# Importing and exporting data -

Source: https://docs.lambda.ai/public-cloud/importing-exporting-data/

---

[1-click clusters ](../../tags/#tag:1-click-clusters)[on-demand cloud ](../../tags/#tag:on-demand-cloud)
# Importing and exporting data [# ](#importing-and-exporting-data)

This document outlines common solutions for importing data into your Lambda On-Demand Cloud (ODC) instances and 1-Click Clusters (1CCs). The document also provides guidance on backing up your data so that it persists beyond the life of your instance or 1CC. 

## Importing data [# ](#importing-data)

You can use `rsync`to copy data to and from your Lambda instances and their attached filesystems. `rsync`allows you to copy files from your local environment to your ODC instance, between ODC instances, from instances to 1CCs, and more. If you need to import data from AWS S3 or an S3-compatible object storage service like Cloudflare R2, Google Cloud Storage, or Minio, you can use `s5cmd`or `rclone`. 

### Importing data from your local environment [# ](#importing-data-from-your-local-environment)

To copy files from your local environment to a Lambda Cloud instance or cluster, run the following `rsync`command from your local terminal. Replace the variables as follows: 

- Replace `<FILES>`with the files or directories you want to copy to the remote instance. If you're copying multiple files or directories, separate them using spaces—for example, `foo.md bar/ baz/`. 
- Replace `<USERNAME>`with your username on the remote instance. 
- Replace `<SERVER-IP>`with the IP address of the remote instance. 
- Replace `<REMOTE-PATH>`with the directory into which you want to copy files. 
```
`[](#__codelineno-0-1)rsync -av --info=progress2 <FILES> <USERNAME>@<SERVER-IP>:<REMOTE-PATH>
`
```
