# Source: https://docs.axonius.com/docs/oracle-vm.md

# Oracle VM

Oracle VM's server virtualization products support x86 and SPARC architectures and a variety of workloads such as Linux, Windows and Oracle Solaris.

## Parameters

1. **Oracle VM Domain** *(required)* - The hostname or IP address of the Oracle VM server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Oracle VM Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Oracle VM Domain** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Oracle VM Domain** will not be verified against the CA database inside of Axonius.
4. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1023\)\(800\).png)

## APIs

Axonius uses the [Oracle VM Manager REST API](https://docs.oracle.com/cd/E50245_01/E50253/html/vmapi-intro.html).