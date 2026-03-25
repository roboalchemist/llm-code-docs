# Source: https://docs.kubearmor.io/kubearmor/documentation/network_security_policy_examples.md

# Network Policy Examples for Nodes/VMs

Here, we demonstrate how to define network security policies.

* DNS lookup restriction
  * Block outgoing DNS traffic ([nsp-egress-block-dns.yaml](https://github.com/kubearmor/KubeArmor/blob/main/examples/network-security-policies/nsp-egress-block-dns.yaml))

    ```
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorNetworkPolicy
    metadata:
      name: nsp-egress-block-dns
    spec:
      nodeSelector:
        matchLabels:
          kubernetes.io/hostname: "kubearmor-dev"
      egress:
      - to:
        - ipBlock:
            cidr: "8.8.8.8/32"
        ports:
        - port: "dns"
          protocol: "UDP"
      severity: 5
      action: Block
    ```

    * Explanation: The purpose of this policy is to audit the outgoing DNS packets (UDP) to 8.8.8.8 in a host whose host name is 'kubearmor-dev'. For this, we define 'kubernetes.io/hostname: kubearmor-dev' in nodeSelector -> matchLabels and the specific address ('8.8.8.8') in egress -> to and port + protocol ('dns' and 'UDP') egress -> ports. Also, we put 'Block' as the action of this policy.
    * Verification: After applying this policy, please open a new terminal (or connect to the host with a new session) and run `nc -uvz -w 2 8.8.8.8 53`. You will see that it runs without an output and an alert is generated.

    **NOTE**

    The given policy works with almost every linux distribution. If it is not working in your case, check if nftables is enabled on your system.
* Ingress alerting

  * Alert for incoming SSH connections

  ```
  apiVersion: security.kubearmor.com/v1
  kind: KubeArmorNetworkPolicy
  metadata:
    name: nsp-ingress-audit-ssh
  spec:
    nodeSelector:
      matchLabels:
        kubearmor.io/hostname: "ubuntu"
    ingress:
    - from:
      - ipBlock:
          cidr: "192.168.29.0/24"
      ports:
      - port: "ssh"
    message: "New SSH connection!"
    severity: 5
    action: Audit
  ```
