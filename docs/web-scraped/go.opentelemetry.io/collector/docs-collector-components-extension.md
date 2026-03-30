# Source: https://opentelemetry.io/docs/collector/components/extension/

Title: Extensions

URL Source: https://opentelemetry.io/docs/collector/components/extension/

Markdown Content:
List of available OpenTelemetry Collector extensions

Extensions provide additional capabilities like health checks and service discovery. For more information on how to configure extensions, see the [Collector configuration documentation](https://opentelemetry.io/docs/collector/configuration/#extensions).

Extensions[](https://opentelemetry.io/docs/collector/components/extension/#extensions)
--------------------------------------------------------------------------------------

| Name | Distributions[1](https://opentelemetry.io/docs/collector/components/extension/#fn:1) | Stability[2](https://opentelemetry.io/docs/collector/components/extension/#fn:2) |
| --- | --- | --- |
| [ackextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/ackextension) | contrib, K8s | alpha |
| [asapauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/asapauthextension) | contrib | beta |
| [awsproxy](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/awsproxy) | contrib | beta |
| [azureauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/azureauthextension) | contrib | alpha |
| [basicauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/basicauthextension) | contrib, K8s | beta |
| [bearertokenauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/bearertokenauthextension) | contrib, K8s | beta |
| [cgroupruntimeextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/cgroupruntimeextension) | contrib | alpha |
| [datadogextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/datadogextension) | contrib | alpha |
| [googleclientauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/googleclientauthextension) | contrib | beta |
| [headerssetterextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/headerssetterextension) | contrib, K8s | alpha |
| [healthcheckextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/healthcheckextension) | contrib, core, K8s | alpha |
| [healthcheckv2extension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/healthcheckv2extension) | contrib | development |
| [httpforwarderextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/httpforwarderextension) | contrib, K8s | beta |
| [jaegerremotesampling](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/jaegerremotesampling) | contrib | alpha |
| [k8sleaderelector](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/k8sleaderelector) | contrib, K8s | alpha |
| [memorylimiterextension](https://github.com/open-telemetry/opentelemetry-collector/tree/main/extension/memorylimiterextension) | contrib | development |
| [oauth2clientauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/oauth2clientauthextension) | contrib, K8s | beta |
| [oidcauthextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/oidcauthextension) | contrib, K8s | beta |
| [opampextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/opampextension) | contrib, K8s | alpha |
| [pprofextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/pprofextension) | contrib, core, K8s | beta |
| [remotetapextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/remotetapextension) | contrib | development |
| [sigv4authextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/sigv4authextension) | contrib | beta |
| [solarwindsapmsettingsextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/solarwindsapmsettingsextension) | contrib | development |
| [sumologicextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/sumologicextension) | contrib | alpha |
| [zpagesextension](https://github.com/open-telemetry/opentelemetry-collector/tree/main/extension/zpagesextension) | contrib, core, K8s | beta |

Encoding Extensions[](https://opentelemetry.io/docs/collector/components/extension/#encoding-extensions)
--------------------------------------------------------------------------------------------------------

| Name | Distributions[1](https://opentelemetry.io/docs/collector/components/extension/#fn:1) | Stability[2](https://opentelemetry.io/docs/collector/components/extension/#fn:2) |
| --- | --- | --- |
| [avrologencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/avrologencodingextension) | contrib | development |
| [awscloudwatchmetricstreamsencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/awscloudwatchmetricstreamsencodingextension) | contrib | alpha |
| [awslogsencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/awslogsencodingextension) | contrib | alpha |
| [azureencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/azureencodingextension) | contrib | development |
| [googlecloudlogentryencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/googlecloudlogentryencodingextension) | contrib | alpha |
| [jaegerencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/jaegerencodingextension) | contrib | alpha |
| [jsonlogencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/jsonlogencodingextension) | contrib | alpha |
| [otlpencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/otlpencodingextension) | contrib | beta |
| [skywalkingencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/skywalkingencodingextension) | contrib | alpha |
| [textencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/textencodingextension) | contrib | beta |
| [zipkinencodingextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/encoding/zipkinencodingextension) | contrib | alpha |

Observer Extensions[](https://opentelemetry.io/docs/collector/components/extension/#observer-extensions)
--------------------------------------------------------------------------------------------------------

| Name | Distributions[1](https://opentelemetry.io/docs/collector/components/extension/#fn:1) | Stability[2](https://opentelemetry.io/docs/collector/components/extension/#fn:2) |
| --- | --- | --- |
| [cfgardenobserver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/cfgardenobserver) | contrib | alpha |
| [dockerobserver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/dockerobserver) | contrib | beta |
| [ecsobserver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/ecsobserver) | contrib | beta |
| [endpointswatcher](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/endpointswatcher) | contrib | N/A |
| [hostobserver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/hostobserver) | contrib, K8s | beta |
| [k8sobserver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/k8sobserver) | contrib, K8s | alpha |
| [kafkatopicsobserver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/observer/kafkatopicsobserver) | contrib | alpha |

Storage Extensions[](https://opentelemetry.io/docs/collector/components/extension/#storage-extensions)
------------------------------------------------------------------------------------------------------

| Name | Distributions[1](https://opentelemetry.io/docs/collector/components/extension/#fn:1) | Stability[2](https://opentelemetry.io/docs/collector/components/extension/#fn:2) |
| --- | --- | --- |
| [dbstorage](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/storage/dbstorage) | contrib | alpha |
| [filestorage](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/storage/filestorage) | contrib, K8s | beta |
| [redisstorageextension](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/extension/storage/redisstorageextension) | contrib | alpha |

* * *

1.   Shows which [distributions](https://opentelemetry.io/docs/collector/distributions/) (core, contrib, K8s, etc.) include this component.[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref:1)[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref1:1)[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref2:1)[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref3:1)

2.   For details about component stability levels, see the [OpenTelemetry Collector component stability definitions](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/component-stability.md).[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref:2)[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref1:2)[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref2:2)[↩︎](https://opentelemetry.io/docs/collector/components/extension/#fnref3:2)

Feedback
--------

Was this page helpful?

Thank you. Your feedback is appreciated!

Please let us know [how we can improve this page](https://github.com/open-telemetry/opentelemetry.io/issues/new?template=PAGE_FEEDBACK.yml&title=[Page+feedback]%3A+ADD+A+SUMMARY+OF+YOUR+FEEDBACK+HERE). Your feedback is appreciated!
