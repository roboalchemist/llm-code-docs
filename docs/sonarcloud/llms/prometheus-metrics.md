# Source: https://docs.sonarsource.com/sonarqube-community-build/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/setup-and-update/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/setup-and-upgrade/deploy-on-kubernetes/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md

# Source: https://docs.sonarsource.com/sonarqube-server/server-installation/on-kubernetes-or-openshift/set-up-monitoring/prometheus-metrics.md

# List of Prometheus metrics

### Metrics exposed by the Web API <a href="#web-api" id="web-api"></a>

<table><thead><tr><th width="257.928955078125">Metric name</th><th width="97">Type</th><th width="117.453125">Unit</th><th>Description</th></tr></thead><tbody><tr><td><code>SonarQube_Database_PoolMaxConnections</code></td><td>Untyped</td><td>Connections</td><td>Maximum number of connections to the Database pool.</td></tr><tr><td><code>SonarQube_AsyncExecution_LargestWorkerCount</code></td><td>Untyped</td><td>n/a</td><td>Maximum number of asynchronous workers.</td></tr><tr><td><code>SonarQube_Database_PoolMinIdleConnections</code></td><td>Untyped</td><td>Connections</td><td>Minimum number of idle connections to the Database pool.</td></tr><tr><td><code>SonarQube_AsyncExecution_QueueSize</code></td><td>Untyped</td><td>n/a</td><td>Queue size for asynchronous jobs.</td></tr><tr><td><code>SonarQube_Database_PoolTotalConnections</code></td><td>Untyped</td><td>Connections</td><td>Total number of connections to the Database pool.</td></tr><tr><td><code>SonarQube_AsyncExecution_WorkerCount</code></td><td>Untyped</td><td>Workers</td><td>Total number of asynchronous job workers.</td></tr><tr><td><code>SonarQube_Database_PoolMaxLifeTimeMillis</code></td><td>Untyped</td><td>Milliseconds</td><td>Maximum time a connection can stay in the alive in the Database pool.</td></tr><tr><td><code>SonarQube_Database_PoolActiveConnections</code></td><td>Untyped</td><td>Connections</td><td>Maximum number of active connections in the Database pool.</td></tr><tr><td><code>SonarQube_Database_PoolMaxWaitMillis</code></td><td>Untyped</td><td>Milliseconds</td><td>Maximum time a connection can keep waiting in the Database pool.</td></tr><tr><td><code>SonarQube_Database_PoolIdleConnections</code></td><td>Untyped</td><td><br></td><td>Maximum number of idle connections in the Database pool.</td></tr></tbody></table>

### JMX metrics <a href="#jmx-metrics" id="jmx-metrics"></a>

#### Main SonarQube Server process <a href="#main-sonarqube-server-process" id="main-sonarqube-server-process"></a>

The metrics coming from the main Java process are listed below.

<table><thead><tr><th width="256">Metric name</th><th width="92">Type</th><th width="96">Unit</th><th>Description</th></tr></thead><tbody><tr><td><code>process_cpu_seconds_total</code></td><td>Counter</td><td>Seconds</td><td>Total user and system CPU time spent in seconds.</td></tr><tr><td><code>process_start_time_seconds</code></td><td>Gauge</td><td>Seconds</td><td>Start time of the process since Unix epoch in seconds.</td></tr><tr><td><code>process_open_fds</code></td><td>Gauge</td><td>n/a</td><td>Number of open file descriptors.</td></tr><tr><td><code>process_max_fds</code></td><td>Gauge</td><td>n/a</td><td>Maximum number of open file descriptors.</td></tr><tr><td><code>process_virtual_memory_bytes</code></td><td>Gauge</td><td>Bytes</td><td>Virtual memory size in bytes.</td></tr><tr><td><code>process_resident_memory_bytes</code></td><td>Gauge</td><td>Bytes</td><td>Resident memory size in bytes.</td></tr></tbody></table>

#### Tomcat <a href="#tomcat" id="tomcat"></a>

The metrics coming from Tomcat are listed below. All metrics are untyped.

<details>

<summary>Connector</summary>

<table><thead><tr><th width="299.2073974609375">Metric name</th><th>Description</th></tr></thead><tbody><tr><td><code>Tomcat_Connector_portOffset</code></td><td>The offset that will be applied to the port to determine the actual port number used.</td></tr><tr><td><code>Tomcat_Connector_maxThreads</code></td><td>The maximum number of request processing threads to be created for the internal Executor. -1 indicates an external Executor is being used.</td></tr><tr><td><code>Tomcat_Connector_tcpNoDelay</code></td><td>Should we use TCP no delay?</td></tr><tr><td><code>Tomcat_Connector_maxParameterCount</code></td><td>The maximum number of parameters (GET plus POST) that will be automatically parsed by the container. 10000 by default. The default Tomcat server.xml configures a lower default of 1000. A value of less than 0 means no limit.</td></tr><tr><td><code>Tomcat_Connector_maxHeaderCount</code></td><td>The maximum number of headers that are allowed by the container. 100 by default. A value of less than 0 means no limit.</td></tr><tr><td><code>Tomcat_Connector_maxKeepAliveRequests</code></td><td>Maximum number of Keep-Alive requests to honor per connection.</td></tr><tr><td><code>Tomcat_Connector_allowTrace</code></td><td>Allow disabling TRACE method.</td></tr><tr><td><code>Tomcat_Connector_enableLookups</code></td><td>The ‘enable DNS lookups’ flag for this Connector.</td></tr><tr><td><code>Tomcat_Connector_localPort</code></td><td>The port number on which this connector is listening to requests. If the special value for port of zero is used then this method will report the actual port bound.</td></tr><tr><td><code>Tomcat_Connector_threadPriority</code></td><td>The thread priority for processors using the internal Executor. -1 indicates an external Executor is being used.</td></tr><tr><td><code>Tomcat_Connector_processorCache</code></td><td>The processor cache size.</td></tr><tr><td><code>Tomcat_Connector_xpoweredBy</code></td><td>Is generation of X-Powered-By response header enabled/disabled?</td></tr><tr><td><code>Tomcat_Connector_useIPVHosts</code></td><td>Should IP-based virtual hosting be used?</td></tr><tr><td><code>Tomcat_Connector_port</code></td><td>The port number (excluding any offset) on which this connector is configured to listen for requests. The special value of 0 means select a random free port when the socket is bound.</td></tr><tr><td><code>Tomcat_Connector_redirectPort</code></td><td>The redirect port (excluding any offset) for non-SSL to SSL redirects.</td></tr><tr><td><code>Tomcat_Connector_proxyPort</code></td><td>The Server port to which we should pretend requests to this Connector.</td></tr><tr><td><code>Tomcat_Connector_acceptCount</code></td><td>The accept count for this Connector.</td></tr><tr><td><code>Tomcat_Connector_maxSwallowSize</code></td><td>The maximum number of request body bytes to be swallowed by Tomcat for an aborted upload.</td></tr><tr><td><code>Tomcat_Connector_portWithOffset</code></td><td>The actual port number (including any offset) on which this connector is configured to listen for requests.</td></tr><tr><td><code>Tomcat_Connector_maxPostSize</code></td><td>Maximum size in bytes of a POST which will be handled by the servlet API provided features.</td></tr><tr><td><code>Tomcat_Connector_connectionTimeout</code></td><td>Timeout value on the incoming connection.</td></tr><tr><td><code>Tomcat_Connector_connectionLinger</code></td><td>Linger value on the incoming connection.</td></tr></tbody></table>

</details>

<details>

<summary>Engine</summary>

| Metric name                              | Description                                                          |
| ---------------------------------------- | -------------------------------------------------------------------- |
| `Tomcat_Engine_backgroundProcessorDelay` | The processor delay for this component.                              |
| `Tomcat_Engine_startChildren`            | Will children be started automatically when they are added?          |
| `Tomcat_Engine_startStopThreads`         | The number of threads to use when starting and stopping child Hosts. |

</details>

<details>

<summary>GlobalRequestProcessor</summary>

| Metric name                                    | Description                                                  |
| ---------------------------------------------- | ------------------------------------------------------------ |
| `Tomcat_GlobalRequestProcessor_bytesReceived`  | Amount of data received, in bytes.                           |
| `Tomcat_GlobalRequestProcessor_bytesSent`      | Amount of data sent, in bytes.                               |
| `Tomcat_GlobalRequestProcessor_errorCount`     | Number of errors for the GlobalRequestProcessor.             |
| `Tomcat_GlobalRequestProcessor_maxTime`        | Maximum time to process a request.                           |
| `Tomcat_GlobalRequestProcessor_processingTime` | Total time to process the requests.                          |
| `Tomcat_GlobalRequestProcessor_requestCount`   | Number of requests processed for the GlobalRequestProcessor. |

</details>

<details>

<summary>Host</summary>

| Metric name                            | Description                                                                                                                                                        |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Tomcat_Host_autoDeploy`               | The auto deploy flag for this Host.                                                                                                                                |
| `Tomcat_Host_backgroundProcessorDelay` | The processor delay for this component.                                                                                                                            |
| `Tomcat_Host_copyXML`                  | Should XML files be copied to $CATALINA\_BASE/conf/{engine}/{host} by default when a web application is deployed?                                                  |
| `Tomcat_Host_createDirs`               | Should we create directories upon startup for appBase and xmlBase?                                                                                                 |
| `Tomcat_Host_deployOnStartup`          | The deploy on startup flag for this Host.                                                                                                                          |
| `Tomcat_Host_deployXML`                | Deploy Context XML config files property.                                                                                                                          |
| `Tomcat_Host_startChildren`            | Will children be started automatically when they are added?                                                                                                        |
| `Tomcat_Host_startStopThreads`         | The number of threads to use when starting, stopping, and deploying child Contexts.                                                                                |
| `Tomcat_Host_undeployOldVersions`      | Determines if old versions of applications deployed using parallel deployment are automatically undeployed when no longer used. Requires autoDeploy to be enabled. |
| `Tomcat_Host_unpackWARs`               | Unpack WARs property.                                                                                                                                              |

</details>

<details>

<summary>Manager</summary>

| Metric name                                          | Description                                                                                                                                       |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Tomcat_Manager_activeSessions`                      | Number of active sessions at this moment.                                                                                                         |
| `Tomcat_Manager_duplicates`                          | Number of duplicated session ids generated.                                                                                                       |
| `Tomcat_Manager_expiredSessions`                     | Number of sessions that expired (doesn’t include explicit invalidations).                                                                         |
| `Tomcat_Manager_maxActive`                           | Maximum number of active sessions so far.                                                                                                         |
| `Tomcat_Manager_maxActiveSessions`                   | The maximum number of active Sessions allowed, or -1 for no limit.                                                                                |
| `Tomcat_Manager_persistAuthentication`               | Indicates whether sessions shall persist authentication information when being persisted (e.g. across application restarts).                      |
| `Tomcat_Manager_processExpiresFrequency`             | The frequency of the manager checks (expiration and passivation).                                                                                 |
| `Tomcat_Manager_processingTime`                      | Time spent doing housekeeping and expiration.                                                                                                     |
| `Tomcat_Manager_rejectedSessions`                    | Number of sessions we rejected due to maxActive being reached.                                                                                    |
| `Tomcat_Manager_sessionAverageAliveTime`             | Average time an expired session had been alive.                                                                                                   |
| `Tomcat_Manager_sessionCounter`                      | Total number of sessions created by this manager.                                                                                                 |
| `Tomcat_Manager_sessionCreateRate`                   | Session creation rate in sessions per minute.                                                                                                     |
| `Tomcat_Manager_sessionExpireRate`                   | Session expiration rate in sessions per minute.                                                                                                   |
| `Tomcat_Manager_sessionMaxAliveTime`                 | Longest time an expired session had been alive.                                                                                                   |
| `Tomcat_Manager_warnOnSessionAttributeFilterFailure` | Should a WARN level log message be generated if a session attribute fails to match sessionAttributeNameFilter or sessionAttributeClassNameFilter? |

</details>

<details>

<summary>ProtocolHandler</summary>

| Metric name                                            | Description                                           |
| ------------------------------------------------------ | ----------------------------------------------------- |
| `Tomcat_ProtocolHandler_acceptCount`                   | Introspected attribute acceptCount.                   |
| `Tomcat_ProtocolHandler_acceptorThreadCount`           | Introspected attribute acceptorThreadCount.           |
| `Tomcat_ProtocolHandler_acceptorThreadPriority`        | Introspected attribute acceptorThreadPriority.        |
| `Tomcat_ProtocolHandler_allowHostHeaderMismatch`       | Introspected attribute allowHostHeaderMismatch.       |
| `Tomcat_ProtocolHandler_aprRequired`                   | Introspected attribute aprRequired.                   |
| `Tomcat_ProtocolHandler_compressionMinSize`            | Introspected attribute compressionMinSize.            |
| `Tomcat_ProtocolHandler_connectionCount`               | Introspected attribute connectionCount.               |
| `Tomcat_ProtocolHandler_connectionLinger`              | Introspected attribute connectionLinger.              |
| `Tomcat_ProtocolHandler_connectionTimeout`             | Introspected attribute connectionTimeout.             |
| `Tomcat_ProtocolHandler_connectionUploadTimeout`       | Introspected attribute connectionUploadTimeout.       |
| `Tomcat_ProtocolHandler_desiredBufferSize`             | Introspected attribute desiredBufferSize.             |
| `Tomcat_ProtocolHandler_disableUploadTimeout`          | Introspected attribute disableUploadTimeout.          |
| `Tomcat_ProtocolHandler_keepAliveTimeout`              | Introspected attribute keepAliveTimeout.              |
| `Tomcat_ProtocolHandler_localPort`                     | Introspected attribute localPort.                     |
| `Tomcat_ProtocolHandler_maxConnections`                | Introspected attribute maxConnections.                |
| `Tomcat_ProtocolHandler_maxExtensionSize`              | Introspected attribute maxExtensionSize.              |
| `Tomcat_ProtocolHandler_maxHeaderCount`                | Introspected attribute maxHeaderCount.                |
| `Tomcat_ProtocolHandler_maxHttpHeaderSize`             | Introspected attribute maxHttpHeaderSize.             |
| `Tomcat_ProtocolHandler_maxHttpRequestHeaderSize`      | Introspected attribute maxHttpRequestHeaderSize.      |
| `Tomcat_ProtocolHandler_maxHttpResponseHeaderSize`     | Introspected attribute maxHttpResponseHeaderSize.     |
| `Tomcat_ProtocolHandler_maxKeepAliveRequests`          | Introspected attribute maxKeepAliveRequests.          |
| `Tomcat_ProtocolHandler_maxSavePostSize`               | Introspected attribute maxSavePostSize.               |
| `Tomcat_ProtocolHandler_maxSwallowSize`                | Introspected attribute maxSwallowSize.                |
| `Tomcat_ProtocolHandler_maxThreads`                    | Introspected attribute maxThreads.                    |
| Tomcat\*\_ProtocolHandler\_\*maxTrailerSize            | Introspected attribute maxTrailerSize.                |
| `Tomcat_ProtocolHandler_minSpareThreads`               | Introspected attribute minSpareThreads.               |
| `Tomcat_ProtocolHandler_nameIndex`                     | Introspected attribute nameIndex.                     |
| `Tomcat_ProtocolHandler_noCompressionStrongETag`       | Introspected attribute noCompressionStrongETag.       |
| `Tomcat_ProtocolHandler_paused`                        | Introspected attribute paused.                        |
| `Tomcat_ProtocolHandler_pollerThreadCount`             | Introspected attribute pollerThreadCount.             |
| `Tomcat_ProtocolHandler_pollerThreadPriority`          | Introspected attribute pollerThreadPriority.          |
| `Tomcat_ProtocolHandler_port`                          | Introspected attribute port.                          |
| `Tomcat_ProtocolHandler_portOffset`                    | Introspected attribute portOffset.                    |
| `Tomcat_ProtocolHandler_portWithOffset`                | Introspected attribute portWithOffset.                |
| `Tomcat_ProtocolHandler_processorCache`                | Introspected attribute processorCache.                |
| `Tomcat_ProtocolHandler_rejectIllegalHeader`           | Introspected attribute rejectIllegalHeader.           |
| `Tomcat_ProtocolHandler_rejectIllegalHeaderName`       | Introspected attribute rejectIllegalHeaderName.       |
| `Tomcat_ProtocolHandler_secure`                        | Introspected attribute secure.                        |
| `Tomcat_ProtocolHandler_selectorTimeout`               | Introspected attribute selectorTimeout.               |
| `Tomcat_ProtocolHandler_sendfileSupported`             | Introspected attribute sendfileSupported.             |
| `Tomcat_ProtocolHandler_serverRemoveAppProvidedValues` | Introspected attribute serverRemoveAppProvidedValues. |
| `Tomcat_ProtocolHandler_sessionCacheSize`              | Introspected attribute sessionCacheSize.              |
| `Tomcat_ProtocolHandler_sessionTimeout`                | Introspected attribute sessionTimeout.                |
| `Tomcat_ProtocolHandler_sniParseLimit`                 | Introspected attribute sniParseLimit.                 |
| `Tomcat_ProtocolHandler_sSLDisableCompression`         | Introspected attribute sSLDisableCompression.         |
| `Tomcat_ProtocolHandler_sSLDisableSessionTickets`      | Introspected attribute sSLDisableSessionTickets.      |
| `Tomcat_ProtocolHandler_sSLEnabled`                    | Introspected attribute sSLEnabled.                    |
| `Tomcat_ProtocolHandler_sSLHonorCipherOrder`           | Introspected attribute sSLHonorCipherOrder.           |
| `Tomcat_ProtocolHandler_sSLVerifyDepth`                | Introspected attribute sSLVerifyDepth.                |
| `Tomcat_ProtocolHandler_tcpNoDelay`                    | Introspected attribute tcpNoDelay.                    |
| `Tomcat_ProtocolHandler_threadPriority`                | Introspected attribute threadPriority.                |
| `Tomcat_ProtocolHandler_trustMaxCertLength`            | Introspected attribute trustMaxCertLength.            |
| `Tomcat_ProtocolHandler_useKeepAliveResponseHeader`    | Introspected attribute useKeepAliveResponseHeader.    |
| `Tomcat_ProtocolHandler_useSendfile`                   | Introspected attribute useSendfile.                   |
| `Tomcat_ProtocolHandler_useServerCipherSuitesOrder`    | Introspected attribute useServerCipherSuitesOrder.    |
| `Tomcat_ProtocolHandler_waitingProcessorCount`         | Introspected attribute waitingProcessorCount.         |

</details>

<details>

<summary>Realm</summary>

| Metric name                                     | Description                                              |
| ----------------------------------------------- | -------------------------------------------------------- |
| `Tomcat_Realm_available`                        | Introspected attribute available.                        |
| `Tomcat_Realm_stripRealmForGss`                 | Introspected attribute stripRealmForGss.                 |
| `Tomcat_Realm_throwOnFailure`                   | Introspected attribute throwOnFailure.                   |
| `Tomcat_Realm_transportGuaranteeRedirectStatus` | Introspected attribute transportGuaranteeRedirectStatus. |
| `Tomcat_Realm_validate`                         | Introspected attribute validate.                         |

</details>

<details>

<summary>RequestProcessor</summary>

| Metric name                                         | Description                                       |
| --------------------------------------------------- | ------------------------------------------------- |
| `Tomcat_RequestProcessor_bytesReceived`             | Introspected attribute bytesReceived.             |
| `Tomcat_RequestProcessor_bytesSent`                 | Introspected attribute bytesSent.                 |
| `Tomcat_RequestProcessor_contentLength`             | Introspected attribute contentLength.             |
| `Tomcat_RequestProcessor_errorCount`                | Introspected attribute errorCount.                |
| `Tomcat_RequestProcessor_lastRequestProcessingTime` | Introspected attribute lastRequestProcessingTime. |
| `Tomcat_RequestProcessor_maxTime`                   | Introspected attribute maxTime.                   |
| `Tomcat_RequestProcessor_processingTime`            | Introspected attribute processingTime.            |
| `Tomcat_RequestProcessor_requestBytesReceived`      | Introspected attribute requestBytesReceived.      |
| `Tomcat_RequestProcessor_requestBytesSent`          | Introspected attribute requestBytesSent.          |
| `Tomcat_RequestProcessor_requestCount`              | Introspected attribute requestCount.              |
| `Tomcat_RequestProcessor_requestProcessingTime`     | Introspected attribute requestProcessingTime.     |
| `Tomcat_RequestProcessor_serverPort`                | Introspected attribute serverPort.                |
| `Tomcat_RequestProcessor_stage`                     | Introspected attribute stage.                     |

</details>

<details>

<summary>Server</summary>

| Metric name                    | Description                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------- |
| `Tomcat_Server_port`           | TCP port (excluding any offset) for shutdown messages.                          |
| `Tomcat_Server_portOffset`     | The offset applied to port and to the port attributes of any nested connectors. |
| `Tomcat_Server_portWithOffset` | Actual TCP port (including any offset) for shutdown messages.                   |

</details>

<details>

<summary>Servlet</summary>

| Metric name                               | Description                                                                                                                                                                                                                             |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Tomcat_Servlet_available`                | The date and time at which this servlet will become available (in milliseconds since the epoch), or zero if the servlet is available. If this value equals Long.MAX\_VALUE, the unavailability of this servlet is considered permanent. |
| `Tomcat_Servlet_asyncSupported`           | Async support.                                                                                                                                                                                                                          |
| `Tomcat_Servlet_backgroundProcessorDelay` | The processor delay for this component.                                                                                                                                                                                                 |
| `Tomcat_Servlet_classLoadTime`            | Time taken to load the Servlet class.                                                                                                                                                                                                   |
| `Tomcat_Servlet_countAllocated`           | The count of allocations that are currently active (even if they are for the same instance, as will be true on a non-STM servlet).                                                                                                      |
| `Tomcat_Servlet_errorCount`               | Error count.                                                                                                                                                                                                                            |
| `Tomcat_Servlet_loadOnStartup`            | The load-on-startup order value (negative value means load on first call) for this servlet.                                                                                                                                             |
| `Tomcat_Servlet_loadTime`                 | Time taken to load and initialize the Servlet.                                                                                                                                                                                          |
| `Tomcat_Servlet_maxInstances`             | Deprecated. Will be removed in Tomcat 10.1 onwards. Maximum number of STM instances.                                                                                                                                                    |
| `Tomcat_Servlet_maxTime`                  | Maximum processing time of a request.                                                                                                                                                                                                   |
| `Tomcat_Servlet_minTime`                  | Minimum processing time of a request.                                                                                                                                                                                                   |
| `Tomcat_Servlet_processingTime`           | Total execution time of the servlet’s service method.                                                                                                                                                                                   |
| `Tomcat_Servlet_requestCount`             | Number of requests processed by this wrapper.                                                                                                                                                                                           |
| `Tomcat_Servlet_singleThreadModel`        | Deprecated. Will be removed in Tomcat 10.1 onwards. Does this servlet implement the SingleThreadModel interface?                                                                                                                        |

</details>

<details>

<summary>SSLHostConfig</summary>

| Metric name                                                   | Description                                                    |
| ------------------------------------------------------------- | -------------------------------------------------------------- |
| `Tomcat_SSLHostConfig_certificateVerificationDepth`           | Introspected attribute certificateVerificationDepth.           |
| `Tomcat_SSLHostConfig_certificateVerificationDepthConfigured` | Introspected attribute certificateVerificationDepthConfigured. |
| `Tomcat_SSLHostConfig_disableCompression`                     | Introspected attribute disableCompression.                     |
| `Tomcat_SSLHostConfig_disableSessionTickets`                  | Introspected attribute disableSessionTickets.                  |
| `Tomcat_SSLHostConfig_honorCipherOrder`                       | Introspected attribute honorCipherOrder.                       |
| `Tomcat_SSLHostConfig_insecureRenegotiation`                  | Introspected attribute insecureRenegotiation.                  |
| `Tomcat_SSLHostConfig_openSslConfContext`                     | Introspected attribute openSslConfContext.                     |
| `Tomcat_SSLHostConfig_openSslContext`                         | Introspected attribute openSslContext.                         |
| `Tomcat_SSLHostConfig_revocationEnabled`                      | Introspected attribute revocationEnabled.                      |
| `Tomcat_SSLHostConfig_sessionCacheSize`                       | Introspected attribute sessionCacheSize.                       |
| `Tomcat_SSLHostConfig_sessionTimeout`                         | Introspected attribute sessionTimeout.                         |
| `Tomcat_SSLHostConfig_tls13RenegotiationAvailable`            | Introspected attribute tls13RenegotiationAvailable.            |

</details>

<details>

<summary>SocketProperties</summary>

| Metric name                                | Description                              |
| ------------------------------------------ | ---------------------------------------- |
| `Tomcat_SocketProperties_appReadBufSize`   | Introspected attribute appReadBufSize.   |
| `Tomcat_SocketProperties_appWriteBufSize`  | Introspected attribute appWriteBufSize.  |
| `Tomcat_SocketProperties_bufferPool`       | Introspected attribute bufferPool.       |
| `Tomcat_SocketProperties_bufferPoolSize`   | Introspected attribute bufferPoolSize.   |
| `Tomcat_SocketProperties_directBuffer`     | Introspected attribute directBuffer.     |
| `Tomcat_SocketProperties_directBufferPool` | Introspected attribute directBufferPool. |
| `Tomcat_SocketProperties_directSslBuffer`  | Introspected attribute directSslBuffer.  |
| `Tomcat_SocketProperties_eventCache`       | Introspected attribute eventCache.       |
| `Tomcat_SocketProperties_processorCache`   | Introspected attribute processorCache.   |
| `Tomcat_SocketProperties_soLingerOn`       | Introspected attribute soLingerOn.       |
| `Tomcat_SocketProperties_soLingerTime`     | Introspected attribute soLingerTime.     |
| `Tomcat_SocketProperties_soReuseAddress`   | Introspected attribute soReuseAddress.   |
| `Tomcat_SocketProperties_soTimeout`        | Introspected attribute soTimeout.        |
| `Tomcat_SocketProperties_tcpNoDelay`       | Introspected attribute tcpNoDelay.       |
| `Tomcat_SocketProperties_timeoutInterval`  | Introspected attribute timeoutInterval.  |
| `Tomcat_SocketProperties_unlockTimeout`    | Introspected attribute unlockTimeout.    |

</details>

<details>

<summary>StringCache</summary>

| Metric name                         | Description                            |
| ----------------------------------- | -------------------------------------- |
| `Tomcat_StringCache_accessCount`    | Introspected attribute accessCount.    |
| `Tomcat_StringCache_byteEnabled`    | Introspected attribute byteEnabled.    |
| `Tomcat_StringCache_cacheSize`      | Introspected attribute cacheSize.      |
| `Tomcat_StringCache_charEnabled`    | Introspected attribute charEnabled.    |
| `Tomcat_StringCache_hitCount`       | Introspected attribute hitCount.       |
| `Tomcat_StringCache_trainThreshold` | Introspected attribute trainThreshold. |

</details>

<details>

<summary>ThreadPool</summary>

| Metric name                                          | Description                                                                                    |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Tomcat_ThreadPool_acceptCount`                      | Tomcat ThreadPool acceptCount.                                                                 |
| `Tomcat_ThreadPool_acceptorThreadCount`              | Tomcat ThreadPool acceptorThreadCount.                                                         |
| `Tomcat_ThreadPool_acceptorThreadPriority`           | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=acceptorThreadPriority           |
| `Tomcat_ThreadPool_alpnSupported`                    | Tomcat ThreadPool alpnSupported.                                                               |
| `Tomcat_ThreadPool_bindOnInit`                       | Tomcat ThreadPool bindOnInit.                                                                  |
| `Tomcat_ThreadPool_connectionCount`                  | Tomcat ThreadPool connectionCount.                                                             |
| `Tomcat_ThreadPool_connectionLinger`                 | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=connectionLinger                 |
| `Tomcat_ThreadPool_connectionTimeout`                | Tomcat ThreadPool connection timeout.                                                          |
| `Tomcat_ThreadPool_currentThreadCount`               | Tomcat ThreadPool currentThreadCount.                                                          |
| `Tomcat_ThreadPool_currentThreadsBusy`               | The number of currently busy threads in the ThreadPool.                                        |
| `Tomcat_ThreadPool_daemon`                           | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=daemon                           |
| `Tomcat_ThreadPool_deferAccept`                      | Tomcat ThreadPool deferAccept.                                                                 |
| `Tomcat_ThreadPool_executorTerminationTimeoutMillis` | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=executorTerminationTimeoutMillis |
| `Tomcat_ThreadPool_keepAliveCount`                   | Tomcat ThreadPool keepAliveCount.                                                              |
| `Tomcat_ThreadPool_keepAliveTimeout`                 | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=keepAliveTimeout                 |
| `Tomcat_ThreadPool_localPort`                        | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=localPort                        |
| `Tomcat_ThreadPool_maxConnections`                   | Tomcat ThreadPool maxConnections.                                                              |
| `Tomcat_ThreadPool_maxKeepAliveRequests`             | Tomcat ThreadPool maxKeepAliveRequests.                                                        |
| `Tomcat_ThreadPool_maxThreads`                       | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=maxThreads                       |
| `Tomcat_ThreadPool_minSpareThreads`                  | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=minSpareThreads                  |
| `Tomcat_ThreadPool_paused`                           | Tomcat ThreadPool paused.                                                                      |
| `Tomcat_ThreadPool_pollerThreadCount`                | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=pollerThreadCount                |
| `Tomcat_ThreadPool_pollerThreadPriority`             | Tomcat ThreadPool pollerThreadPriority.                                                        |
| `Tomcat_ThreadPool_port`                             | Tomcat ThreadPool port.                                                                        |
| `Tomcat_ThreadPool_portOffset`                       | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=portOffset                       |
| `Tomcat_ThreadPool_portWithOffset`                   | Tomcat ThreadPool portWithOffset.                                                              |
| `Tomcat_ThreadPool_running`                          | Tomcat ThreadPool running.                                                                     |
| `Tomcat_ThreadPool_selectorTimeout`                  | Introspected attribute selectorTimeout.                                                        |
| `Tomcat_ThreadPool_sniParseLimit`                    | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=sniParseLimit                    |
| `Tomcat_ThreadPool_sSLEnabled`                       | Tomcat ThreadPool sSLEnabled.                                                                  |
| `Tomcat_ThreadPool_tcpNoDelay`                       | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=tcpNoDelay                       |
| `Tomcat_ThreadPool_threadPriority`                   | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=threadPriority                   |
| `Tomcat_ThreadPool_useInheritedChannel`              | Tomcat ThreadPool useInheritedChannel.                                                         |
| `Tomcat_ThreadPool_useSendfile`                      | Tomcat:name="http-nio-0.0.0.0-9000",type=ThreadPool,attribute=useSendfile                      |

</details>

<details>

<summary>UtilityExecutor</summary>

| Metric name                                                               | Description                                                              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `Tomcat_UtilityExecutor_activeCount`                                      | Introspected attribute activeCount.                                      |
| `Tomcat_UtilityExecutor_completedTaskCount`                               | Introspected attribute completedTaskCount.                               |
| `Tomcat_UtilityExecutor_continueExistingPeriodicTasksAfterShutdownPolicy` | Introspected attribute continueExistingPeriodicTasksAfterShutdownPolicy. |
| `Tomcat_UtilityExecutor_corePoolSize`                                     | Introspected attribute corePoolSize.                                     |
| `Tomcat_UtilityExecutor_executeExistingDelayedTasksAfterShutdownPolicy`   | Introspected attribute executeExistingDelayedTasksAfterShutdownPolicy.   |
| `Tomcat_UtilityExecutor_largestPoolSize`                                  | Introspected attribute largestPoolSize.                                  |
| `Tomcat_UtilityExecutor_maximumPoolSize`                                  | Introspected attribute maximumPoolSize.                                  |
| `Tomcat_UtilityExecutor_poolSize`                                         | Introspected attribute poolSize.                                         |
| `Tomcat_UtilityExecutor_removeOnCancelPolicy`                             | Introspected attribute removeOnCancelPolicy.                             |
| `Tomcat_UtilityExecutor_shutdown`                                         | Introspected attribute shutdown.                                         |
| `Tomcat_UtilityExecutor_taskCount`                                        | Introspected attribute taskCount.                                        |
| `Tomcat_UtilityExecutor_terminated`                                       | Introspected attribute terminated.                                       |
| `Tomcat_UtilityExecutor_terminating`                                      | Introspected attribute terminating.                                      |

</details>

<details>

<summary>Valve</summary>

| Metric name                                    | Description                                                                                           |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `Tomcat_Valve_asyncSupported`                  | Does this valve support async reporting?                                                              |
| `Tomcat_Valve_birthTime`                       | Introspected attribute birthTime.                                                                     |
| `Tomcat_Valve_cache`                           | Should we cache authenticated Principals if the request is part of an HTTP session?                   |
| `Tomcat_Valve_changeSessionIdOnAuthentication` | Controls if the session ID is changed if a session exists at the point where users are authenticated. |
| `Tomcat_Valve_disableProxyCaching`             | Controls the caching of pages that are protected by security constraints.                             |
| `Tomcat_Valve_quiet`                           | Introspected attribute quiet.                                                                         |
| `Tomcat_Valve_securePagesWithPragma`           | Controls the caching of pages that are protected by security constraints.                             |
| `Tomcat_Valve_showReport`                      | Enables/Disables full error reports.                                                                  |
| `Tomcat_Valve_showServerInfo`                  | Enables/Disables server info on error pages.                                                          |
| `Tomcat_Valve_started`                         | Introspected attribute started.                                                                       |
| `Tomcat_Valve_throwOnFailure`                  | Introspected attribute throwOnFailure.                                                                |

</details>

<details>

<summary>WebModule</summary>

| Metric name                                         | Description                                                                                                                                            |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Tomcat_WebModule_antiResourceLocking`              | Take care not to lock resources.                                                                                                                       |
| `Tomcat_WebModule_clearReferencesRmiTargets`        | Should Tomcat look for memory leaks in RMI Targets and clear them if found as a workaround for application coding errors?                              |
| `Tomcat_WebModule_clearReferencesStopTimerThreads`  | Should Tomcat attempt to terminate TimerThreads that have been started by the web application? Advisable to be used only in a development environment. |
| `Tomcat_WebModule_clearReferencesStopThreads`       | Should Tomcat attempt to terminate threads that have been started by the web application? Advisable to be used only in a development environment.      |
| `Tomcat_WebModule_clearReferencesThreadLocals`      | Should Tomcat attempt to clear ThreadLocal variables that have been populated with classes loaded by the web application?                              |
| `Tomcat_WebModule_configured`                       | The correctly configured flag for this Context.                                                                                                        |
| `Tomcat_WebModule_cookies`                          | Should we attempt to use cookies for session id communication?                                                                                         |
| `Tomcat_WebModule_crossContext`                     | Should we allow the ServletContext.getContext() method to access the context of other web applications in this server?                                 |
| `Tomcat_WebModule_delegate`                         | Tomcat WebModule delegate.                                                                                                                             |
| `Tomcat_WebModule_distributable`                    | The distributable flag for this web application.                                                                                                       |
| `Tomcat_WebModule_errorCount`                       | Cumulative error count of all servlets in this context.                                                                                                |
| `Tomcat_WebModule_ignoreAnnotations`                | Ignore annotations flag.                                                                                                                               |
| `Tomcat_WebModule_logEffectiveWebXml`               | Should the effective web.xml be logged when the context starts?                                                                                        |
| `Tomcat_WebModule_mapperContextRootRedirectEnabled` | Should the Mapper be used for context root redirects?                                                                                                  |
| `Tomcat_WebModule_mapperDirectoryRedirectEnabled`   | Should the Mapper be used for directory redirects?                                                                                                     |
| `Tomcat_WebModule_maxTime`                          | Maximum execution time of all servlets in this context.                                                                                                |
| `Tomcat_WebModule_minTime`                          | Minimum execution time of all servlets in this context.                                                                                                |
| `Tomcat_WebModule_override`                         | The default context.xml override flag for this web application.                                                                                        |
| `Tomcat_WebModule_parallelAnnotationScanning`       | The parallel annotation scanning flag.                                                                                                                 |
| `Tomcat_WebModule_paused`                           | The request processing pause flag (while reloading occurs).                                                                                            |
| `Tomcat_WebModule_privileged`                       | Access to Tomcat internals.                                                                                                                            |
| `Tomcat_WebModule_processingTime`                   | Cumulative execution times of all servlets in this context.                                                                                            |
| `Tomcat_WebModule_reloadable`                       | The reloadable flag for this web application.                                                                                                          |
| `Tomcat_WebModule_renewThreadsWhenStoppingContext`  | Should Tomcat renew the threads of the thread pool when the application is stopped to avoid memory leaks because of uncleaned ThreadLocal variables?   |
| `Tomcat_WebModule_requestCount`                     | Cumulative request count of all servlets in this context.                                                                                              |
| `Tomcat_WebModule_sessionTimeout`                   | The session timeout (in minutes) for this web application.                                                                                             |
| `Tomcat_WebModule_startTime`                        | Time (in milliseconds since January 1, 1970, 00:00:00) when this context was started.                                                                  |
| `Tomcat_WebModule_startupTime`                      | Time (in milliseconds) it took to start this context.                                                                                                  |
| `Tomcat_WebModule_swallowOutput`                    | Flag to set to cause the system.out and system.err to be redirected to the logger when executing a servlet.                                            |
| `Tomcat_WebModule_tldScanTime`                      | Time spent scanning jars for TLDs for this context.                                                                                                    |
| `Tomcat_WebModule_tldValidation`                    | Should the parsing of \*.tld files be performed by a validating parser?                                                                                |
|                                                     | Amount of ms that the container will wait for servlets to unload.                                                                                      |
| `Tomcat_WebModule_unpackWAR`                        | Unpack WAR property.                                                                                                                                   |
| `Tomcat_WebModule_useBloomFilterForArchives`        | DEPRECATED: Use a bloom filter for archives lookups.                                                                                                   |
| `Tomcat_WebModule_useHttpOnly`                      | Indicates that session cookies should use HttpOnly.                                                                                                    |
| `Tomcat_WebModule_useNaming`                        | Create a JNDI naming context for this application?                                                                                                     |
| `Tomcat_WebModule_useRelativeRedirects`             | When generating location headers for 302 responses, should a relative URI be used?                                                                     |
| `Tomcat_WebModule_xmlNamespaceAware`                | Should the parsing of web.xml and web-fragment.xml files be performed by a namespace-aware parser?                                                     |
| `Tomcat_WebModule_xmlValidation`                    | Should the parsing of web.xml and web-fragment.xml files be performed by a validating parser?                                                          |

</details>

<details>

<summary>WebResourceRoot</summary>

| Metric name                               | Description                                                           |
| ----------------------------------------- | --------------------------------------------------------------------- |
| `Tomcat_WebResourceRoot_allowLinking`     | Does this resources implementation allow the use of symbolic links?   |
| `Tomcat_WebResourceRoot_cachingAllowed`   | Is in-memory caching of resource content and metadata enabled?        |
| `Tomcat_WebResourceRoot_hitCount`         | The number of requests for resources that were served from the cache. |
| `Tomcat_WebResourceRoot_lookupCount`      | The number of requests for resources in the WebResourceRoot.          |
| `Tomcat_WebResourceRoot_maxSize`          | The maximum permitted size of the cache in kB.                        |
| `Tomcat_WebResourceRoot_objectMaxSize`    | The maximum permitted size for a single object in the cache in kB.    |
| `Tomcat_WebResourceRoot_size`             | The current estimate of the cache size in kB.                         |
| `Tomcat_WebResourceRoot_trackLockedFiles` | Does this resources implementation track requests that lock files?    |
| `Tomcat_WebResourceRoot_ttl`              | The time-to-live for cache entries in milliseconds.                   |

</details>
