# Configuring Software RAID -

Source: https://docs.lambda.ai/education/linux-usage/configuring-software-raid/

---

# Configuring Software RAID [# ](#configuring-software-raid)

Software RAID (redundant array of independent disks) provides fast and resilient storage for your machine learning data. This document shows you how to configure software RAID in your cluster using [`mdadm`](https://linux.die.net/man/8/mdadm). 

- Install new drives as needed, then power on the machine. 
- Check that the drives are present with `lsblk`. Your output should look similar to the following: 
```
`[](#__codelineno-0-1)ubuntu@ubuntu:~$ lsblk
[](#__codelineno-0-2)NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
[](#__codelineno-0-3)nvme1n1  259:1   0 1.8T  0 disk
[](#__codelineno-0-4)nvme3n1  259:2   0 1.8T  0 disk
[](#__codelineno-0-5)nvme2n1  259:3   0 1.8T  0 disk
[](#__codelineno-0-6)...
`
```
