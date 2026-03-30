# Source: https://docs.pinot.apache.org/release-0.9.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Source: https://docs.pinot.apache.org/basics/getting-started/frequent-questions/pinot-on-kubernetes-faq.md

# Pinot On Kubernetes FAQ

{% hint style="info" %}
This is a list of questions frequently asked in our troubleshooting channel on Slack. To contribute additional questions and answers, [make a pull request](https://docs.pinot.apache.org/contributing/contributing).
{% endhint %}

## How to increase server disk size on AWS

The following is an example using Amazon Elastic Kubernetes Service (Amazon EKS).

### 1. Update Storage Class

In the Kubernetes (k8s) cluster, check the storage class: in Amazon EKS, it should be `gp2`.

![](https://lh6.googleusercontent.com/-_s9xgJoO_jchVj0n424Phq8LZFLbkvlrEix_XvHpHeT6fugJeZbq7yzuwrLs_US9qqFGJeN2OJr2XeHLd4p6rDQ1BXaIkIpcNw3404AQ7JQUpenu_et83jra9BLBedTbc7kE2LY)

Then update StorageClass to ensure:

```bash
allowVolumeExpansion: true
```

Once StorageClass is updated, it should look like this:

![](https://lh6.googleusercontent.com/aYF44E1KGU6dFoM3E9M_lOSzsJ7gsCLy4oL0EJvfKMpMS0AdLOuL0dx58dcmiXCPcODgV285qrjkEg4laIT9XCNd1HoLGJRkGmsQI8lQRpzvlpwcpsLr6EDSSmhT3iLmQG0dccIU)

### 2. Update PVC

Once the storage class is updated, then we can update the PersistentVolumeClaim (PVC) for the server disk size.

Now we want to double the disk size for `pinot-server-3`.

The following is an example of current disks:

![](https://lh3.googleusercontent.com/s3tBb8hyQBWKwQ-fc3p4EjP1rBsScauHCGlCTU5T9uvGIZ53_i7RyRMv8NgcjviUkDztXytJ9LPExmvCxnz_rcEdIhI_B79VQoGD12uwLxjYeHnogiDdPl9PFcTs1MNK47ByY0EW)

The following is the output of `data-pinot-server-3`:

![PVC data-pinot-server-3](https://lh4.googleusercontent.com/yyIaKpAK5xOjbnw3zWKMhi5ybamZxppPKdzwVCsowZuKEPqE8sT5MpssVpZzAdxTNw-2D5u08bsLUIYgdmkwJRzOxzex96lkNq9e_0tTyNcFzP3Z5zs0arQW0IfZtXnScL2_yqhf)

Now, let's change the PVC size to `2T` by editing the server PVC.

```bash
kubectl edit pvc data-pinot-server-3 -n pinot
```

Once updated, the specification's PVC size is updated to `2T`, but the status's PVC size is still `1T`.

![](https://lh4.googleusercontent.com/OBIEE2GFsUKNa_bInkrjjMh1fouEsdd3U_S8TiVsFymcAAH7WXBxxPyz_9zEFfTRrPbQm0ComaxLeIOa9NIcggIWMjBnv5swR6UfBMErbWp7KG64GcjO03atsfkVrUGO7dwaw50B)

### 3. Restart pod to let it reflect

Restart the `pinot-server-3` pod:

![](https://lh5.googleusercontent.com/uglBVfhh1_dNF1bVrbpAsWQwbB0qZ34X3MgTMBVa5BIDxZg6UgQX6OO3z-YQrE4asnSBHWruiyPhI3s6_u4OfBZjicGttqhe4hcC30yVLaS5mXlkOsZWIjFJVcxSfpLSxv2_BwFK)

Recheck the PVC size:

![](https://lh4.googleusercontent.com/GNyz66IhVZFpW4RTxGWxGCAty716x1joQxXVCX-9T5BBUf3FqHNFA1VRjXjYgNjUH6bv3YmCewJgJpiA_cOGB8nY8O9jp-_J_D40uYPZbRL9PgPT8JW2di9_TYs8UW3Lfvtsz62b)

![](https://lh6.googleusercontent.com/QXkSPfwoxnVD2HOkyMlbvlI_2xXL7u1VIWZO9MZrKu4S5hCTXrH0vqVNoXAkQmB_B1rS7SoWWZvjk-giA1LZEwyLhI67myrQhYVMsexegVMecFQ1s5SZiyQJZNP0uioqo2nXh6Xh)

![](https://lh5.googleusercontent.com/SdanllIsXUnK6DedaxxhaJ1rvpn6vS5lJg4YSDmi-wLFnfZHzwqMpMfeYR-RE6CNUbkSA2UvNjQdz8PuwOGSlyqDVvK2HAqsDS7JX1brN31sTqGkIEZGFGWU_rwyz4pz-nNF-Ss3)
