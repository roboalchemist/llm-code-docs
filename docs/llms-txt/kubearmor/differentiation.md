# Source: https://docs.kubearmor.io/kubearmor/quick-links/differentiation.md

# Differentiation

![KubeArmor Differentiation](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-c3e30cca3b3c624b0ba5dfdb316d44c8b6b37afe%2Fdifferentiation.png?alt=media\&token=659b58da-da79-4982-99d2-65817623aae1)

## Significance of Inline Mitigation

KubeArmor supports attack prevention, not just observability and monitoring.\
More importantly, the prevention is handled inline: even before a process is spawned, a rule can deny execution of a process.\
Most other systems typically employ "post-attack mitigation" that kills a process/pod after malicious intent is observed, allowing an attacker to execute code on the target environment.\
Essentially KubeArmor uses inline mitigation to reduce the attack surface of a pod/container/VM.\
KubeArmor leverages best of breed Linux Security Modules (LSMs) such as AppArmor, BPF-LSM, and SELinux (only for host protection) for inline mitigation.\
LSMs have several advantages over other techniques:

* KubeArmor does not change anything with the pod/container.
* KubeArmor does not require any changes at the host level or at the CRI (Container Runtime Interface) level to enforce blocking rules. KubeArmor deploys as a non-privileged DaemonSet with certain capabilities that allows it to monitor other pods/containers and the host.
* A given cluster can have multiple nodes utilizing different LSMs. KubeArmor abstracts away complexities of LSMs and provides an easy way to enforce policies. KubeArmor manages complexity of LSMs under-the-hood.

### Post-Attack Mitigation and its flaws

![Post Attack Mitigation](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e08f90eb2bf3d31637ce0e29cb7fec849df52443%2Fpost-attack-mitigation.png?alt=media\&token=bd4ac092-7159-4071-bec8-1edeb6b70dfd)

* Post-exploit Mitigation works by killing a suspicious process in response to an alert indicating malicious intent.
* Attacker is allowed to execute a binary. Attacker could disable security controls, access logs, etc to circumvent attack detection.
* By the time a malicious process is killed, sensitive contents could have already been deleted, encrypted, or transmitted.
* [Quoting Grsecurity](https://grsecurity.net/tetragone_a_lesson_in_security_fundamentals), “post-exploitation detection/mitigation is at the mercy of an exploit writer putting little to no effort into avoiding tripping these detection mechanisms.”

## Problems with k8s native Pod Security Context

[Pod Security Context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) allows one to specify [native AppArmor](https://kubernetes.io/docs/tutorials/security/apparmor/) or [native SELinux](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#assign-selinux-labels-to-a-container) policies.

![Pod Security Context](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-a52231d4ee36e97c9ed4d214ef7260c7e5acffcb%2Fpod%20security%20context.png?alt=media\&token=d69855c1-217e-4e7b-a8a4-4a0db89fa024)

This approach has multiple problems:

1. It is often difficult to predict which LSM (AppArmor or SELinux) would be available on the target node.
2. BPF-LSM is not supported by Pod Security Context.
3. It is difficult to manually specify an AppArmor or SELinux policy. Changing default AppArmor or SELinux policies might result in more security holes since it is difficult to decipher the implications of the changes and can be counter-productive.

### Problems with multi-cloud deployment

Different managed cloud providers use different default distributions.\
Google GKE COS uses AppArmor by default, AWS Bottlerocket uses BPF-LSM and SELinux, and AWS Amazon Linux 2 uses only SELinux by default.\
Thus it is challenging to use Pod Security Context in multi-cloud deployments.

![Multi Cloud issues with LSMs](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-e720ae9b6d4e049162c2270c1b9e7bf033e92c57%2Fmulti-cloud.png?alt=media\&token=03fe5c22-381a-4879-8e80-287a9d1af63e)

## Use of BPF-LSM

![BPF-LSM with KubeArmor](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-7f8b390d0f4342b9171ab8aa27572e3d1a79d0c5%2Fbpf-lsm.png?alt=media\&token=2b7f01f9-b246-460b-a5d7-f8d9777cfe48)

References:

* [Armoring Cloud Native Workloads with BPF-LSM](https://www.youtube.com/watch?v=uYVaiIX7QC0\&ab_channel=CNCF%5BCloudNativeComputingFoundation%5D)
* [Securing Bottlerocket deployments on Amazon EKS with KubeArmor](https://aws.amazon.com/blogs/containers/secure-bottlerocket-deployments-on-amazon-eks-with-kubearmor/)
