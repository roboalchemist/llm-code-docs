# Source: https://docs.silabs.com/openthread/3.0.0/configuring-openthread-apps-for-thread-1-3/01-including-thread-1-3-features-in-soc-applications.md

# Including Thread 1.3 features in SoC Applications

Silicon Labs provides a number of sample SoC OpenThread applications. You can modify these to include Thread 1.3 features (some of which are enabled by default). This chapter assumes you are familiar with creating and modifying OpenThread projects in Simplicity Studio. If you need more information, see the Simplicity Studio User’s Guide and the [OpenThread Quick Start Guide](/openthread/{build-docspace-version}/openthread-quick-start-guide).

As an example, the following procedure shows how to configure 1.3 features:

1. Create a project based on the example: **OpenThread – SoC CLI (FTD)**.
2. On the **SOFTWARE COMPONENTS** tab, search for and select the **Stack (FTD)** entry. Depending on your application, you may have to do this on a **Stack (MTD)** or **Stack (RCP)** component (this example is for an FTD application).  
   ![Software Components tab](/configuring-openthread-apps-for-thread-1-3/0.1/images/sld862-image1.png)
3. Configure the various compile-time settings. The options are explained in the OpenThread documentation.  
   ![compile-time settings](/configuring-openthread-apps-for-thread-1-3/0.1/images/sld862-image2.png)

**For Thread 1.3 features**, the following flags are required. The description for each flag indicates whether it is mandatory, optional, or recommended. **Do not enable** these flags for a Thread 1.1 application.

- **Thread Stack Protocol Version**: Set to Thread 1.3 (mandatory).
- **DNS Client** (mandatory): Required for Thread 1.3 compliance.
- **DNS-SD Server** (recommended): FTDs only. Required for Thread 1.3 compliance on Thread Border Routers. Optional otherwise.
- **SRP Client** (mandatory): Required for Thread 1.3 compliance.
- **SRP Server** (recommended): FTDs only. Required for Thread 1.3 compliance on Thread Border Routers. Optional otherwise.
- **TCP features**: For more information, see [TCP in Thread 1.3](#tcp-in-thread-13).  
  - **TCP** (recommended): Recommended for Thread 1.3 compliance. Declarative support required for Thread 1.3 component certification.  
  - **DNS Client over TCP**: Recommended for Thread 1.3 compliance. Declarative support required for Thread 1.3 component certification.
- **Thread over Infrastructure** (recommended): NCPs only. Required for Thread 1.3 compliance on Thread Border Routers (and enabled by default for the border router POSIX stack). For sample applications on EFR platforms, this applies only to NCPs, and as such is an untested feature, as Silicon Labs does not support full-featured NCP FTD/MTD applications.

Additional information about these features is included in the following table.

<table>
    <thead>
        <tr>
            <th>Flag</th>
            <th>Note</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>DNS Client<br>(OPENTHREAD_CONFIG_DNS_CLIENT_ENABLE)</td>
            <td>
                Must always be turned on for Thread 1.3 conformance. Enables support for DNS client. Enables sending DNS queries for AAAA (IPv6) records.
            </td>
        </tr>
        <tr>
            <td>DNS-SD Server<br>(OPENTHREAD_CONFIG_DNSSD_SERVER_ENABLE)</td>
            <td>
                Enables support for DNS-SD server. Service information from a local SRP server is used to resolve DNS-SD queries.<br>
                A DNS server should implement the following features:
                <ul>
                    <li>DNS recursive resolver to answer queries for all valid DNS record types including, for example, host name records. DNS type "A" and "AAAA" address records.</li>
                    <li>DNS authoritative server that answers authoritatively for DNS-Based Service Discovery [RFC 6763] records and any other DNS records registered with the Thread Service Registry by clients using the Service Registration Protocol.</li>
                    <li>DNS Update Server: A server that accepts properly authenticated client requests to update authoritative DNS data.</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td>SRP Client<br>(OPENTHREAD_CONFIG_SRP_CLIENT_ENABLE)</td>
            <td>
                Must always be turned on for Thread 1.3 conformance. Enables support for SRP (Service Registration Protocol) client. An SRP client Thread Device registers services with the SRP server, communicates with the corresponding DNS-SD authoritative server for queries, and uses the DNS recursive resolver for DNS resolution as defined by the respective IETF specifications.<br>
                For more information, see:<br>
                <a href="https://github.com/openthread/openthread/blob/main/src/cli/README_SRP_CLIENT.md">https://github.com/openthread/openthread/blob/main/src/cli/README_SRP_CLIENT.md</a>
            </td>
        </tr>
        <tr>
            <td>SRP Server<br>(OPENTHREAD_CONFIG_SRP_SERVER_ENABLE)</td>
            <td>
                Enables support for SRP (Service Registration Protocol) server. An SRP server supports the DNS Update Server functions, plus additional public key cryptography for security and some other minor enhancements to better support constrained clients. For more information, see:<br>
                <a href="https://github.com/openthread/openthread/blob/main/src/cli/README_SRP.md">https://github.com/openthread/openthread/blob/main/src/cli/README_SRP.md</a>
            </td>
        </tr>
        <tr>
            <td>TCP API<br>(OPENTHREAD_CONFIG_TCP_ENABLE)</td>
            <td>
                Enables low-power TCP APIs.<br>
                For more information, see:<br>
                <a href="https://github.com/openthread/openthread/blob/main/src/cli/README_TCP.md">https://github.com/openthread/openthread/blob/main/src/cli/README_TCP.md</a>
            </td>
        </tr>
        <tr>
            <td>DNS Client over TCP<br>(OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE)</td>
            <td>
                Enables sending DNS queries over TCP.<br>
                For more information, see:<br>
                <a href="https://github.com/openthread/openthread/blob/main/src/cli/README.md#dns-config">https://github.com/openthread/openthread/blob/main/src/cli/README.md#dns-config</a>
            </td>
        </tr>
        <tr>
            <td>Thread over Infrastructure<br>(OPENTHREAD_CONFIG_RADIO_LINK_TREL_ENABLE)</td>
            <td>
                Must always be turned on for Thread 1.3 conformance. Enables TREL radio link for Thread over Infrastructure feature.<br> For sample applications, this is applicable to NCPs only, which are currently not supported by Silicon Labs. See the next section for information on how this applies to border router POSIX platforms.
            </td>
        </tr>
        <tr>
            <td>Delay Aware Queue Management<br>(OPENTHREAD_CONFIG_DELAY_AWARE_QUEUE_MANAGEMENT_ENABLE)</td>
            <td>
                Must always be turned on for Thread 1.3 conformance. Devices will monitor time-in-queue of messages in the direct tx queue and if the wait time is larger than specified thresholds it may update ECN flag (if message indicates it is ECN-capable) or drop the message.
            </td>
        </tr>
    </tbody>
</table>

## TCP in Thread 1.3

Thread 1.3 component certification requires declarative support for TCP, which means the TCP APIs (OPENTHREAD_CONFIG_TCP_ENABLE and  OPENTHREAD_CONFIG_DNS_CLIENT_OVER_TCP_ENABLE) must be enabled for conformance. However, if one chooses to not include TCP, then the third-party TCPlp implementation can be stubbed out using the “**TCPlp stubs for OpenThread TCP API**” component. If this component is installed, TCPlp implementation will be stubbed for an FTD / MTD application. Otherwise, the TCPlp implementation is included by default.

![TCPlp](/configuring-openthread-apps-for-thread-1-3/0.1/images/sld862-image3.png)

It is recommended to enable TCP for Thread 1.3 conformance so that OpenThread border routers using DNS can make use of well-known DNS-over-TCP queries and responses.

> **Note**: TCP is supported in SoC and POSIX host (OTBR) applications. It is not required on RCP applications, and can be supported on NCP applications, but Silicon Labs does not yet provide support for full-featured NCP FTD/MTD applications.