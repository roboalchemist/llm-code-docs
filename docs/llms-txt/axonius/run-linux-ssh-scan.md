# Source: https://docs.axonius.com/docs/run-linux-ssh-scan.md

# Axonius - Run Linux SSH Scan

**Axonius - Run Linux SSH Scan**  runs an SSH scan on each of the query results, which are endpoint Linux machines.
The scan retrieves important information about the device, including:

* Hostname
* Network Interfaces - including MAC addresses, IP addresses and subnets
* Operating system, kernel version and distribution
* A list of installed software
* Users and admin users
* Hard drives and file systems
* Services
* Listening ports
* CPUs and RAM
* Hardware details, including serials
* and more...

Most of the Linux SSH scan information is also displayed under the various asset aggregated data tables.<br />
For more details, see [Asset Profile page](/docs/asset-profile-page).

Refer to [Connecting Linux SSH Adapter](/docs/linux-ssh) for full information about Linux commands used.

<Callout icon="📘" theme="info">
  Note

  The **Linux SSH** adapter is a 'read only' adapter. The adapter only gathers information about the endpoint Linux machine and does not change it.

  It is safe to use the adapter to fetch information from production environments.

  For details on the list of used commands and read files, see [Connecting Linux SSH Adapter](/docs/linux-ssh).
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

1. **User Name** *(required)* - The SSH user name to connect with.

2. **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.
Refer to [Connecting Linux SSH Adapter](/docs/linux-ssh) for further details about these configuration options

1. **Password**   - A password for the SSH user.

<Callout icon="📘" theme="info">
  Note

  For authentication, you must specify at least password or private key, but you can also specify both.
</Callout>

2. **Private Key** *(optional)* - A private key for the SSH user.

3. **Private Key Passphrase** *(optional, default: empty)* - Specify a private key passphrase if the private key is protected by a passphrase.

4. **SSH Port** *(optional, default: 22)* - The SSH port.

5. **Sudoer** *(required, default: True)* - Select this if the user is listed as a sudoer and can execute privileged commands (by using the *sudo* command).

   Hardware information such as serials, CPUs and bios versions are fetched only when the specified user can run *dmidecode* command.

* If enabled, this adapter connection will try to run *sudo dmidecode* command. The user password will be used, if required.
* If disabled, this adapter connection will usually fail to run that command (unless the specified user is the superuser). Therefore, the hardware information will not be fetched.

6. **Sudo Path** - Specify an absolute path (/path/to/sudo) of a binary to use for sudo'ing to the root user.
   * If supplied, when the command line is executed it will be prefixed with the value supplied
   * If not supplied, when the command line is executed it will be prefixed with "sudo".
7. **Verify Fingerprint** - Enter a fingerprint. If entered then ssh connections verify that this fingerprint matches the fingerprint of the host's public key. The value can be usually found in \~/.ssh/known\_hosts. If missing then no confirmation is done upon connection attempts.

<Callout icon="📘" theme="info">
  Note

  If you are using multi-nodes, choose the Axonius node to use to interact with the adapter when executing the enforcement action.
</Callout>

8. **Connectivity Timeout** - Set the connectivity timeout. The default is 30 seconds.
9. **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).