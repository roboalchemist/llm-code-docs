# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/api-link-metrics.md

# Link Metrics

This module includes functions that control the Link Metrics protocol.

## Modules

[otLinkMetricsValues](ot-link-metrics-values)

[otLinkMetricsSeriesFlags](ot-link-metrics-series-flags)

## Enumerations

### otLinkMetricsEnhAckFlags

```c
enum otLinkMetricsEnhAckFlags {
    OT_LINK_METRICS_ENH_ACK_CLEAR = 0
    OT_LINK_METRICS_ENH_ACK_REGISTER = 1
}
```

**Description:**

Enhanced-ACK Flags.

**Details:**

These are used in Enhanced-ACK Based Probing to indicate whether to register or clear the probing.

**Enumerator:**

|   |   |
|---|---|
|OT_LINK_METRICS_ENH_ACK_CLEAR|Clear.|
|OT_LINK_METRICS_ENH_ACK_REGISTER|Register.|

### otLinkMetricsStatus

```c
enum otLinkMetricsStatus {
    OT_LINK_METRICS_STATUS_SUCCESS = 0
    OT_LINK_METRICS_STATUS_CANNOT_SUPPORT_NEW_SERIES = 1
    OT_LINK_METRICS_STATUS_SERIESID_ALREADY_REGISTERED = 2
    OT_LINK_METRICS_STATUS_SERIESID_NOT_RECOGNIZED = 3
    OT_LINK_METRICS_STATUS_NO_MATCHING_FRAMES_RECEIVED = 4
    OT_LINK_METRICS_STATUS_OTHER_ERROR = 254
}
```

**Description:**

Link Metrics Status values.

**Enumerator:**

|   |   |
|---|---|
|OT_LINK_METRICS_STATUS_SUCCESS||
|OT_LINK_METRICS_STATUS_CANNOT_SUPPORT_NEW_SERIES||
|OT_LINK_METRICS_STATUS_SERIESID_ALREADY_REGISTERED||
|OT_LINK_METRICS_STATUS_SERIESID_NOT_RECOGNIZED||
|OT_LINK_METRICS_STATUS_NO_MATCHING_FRAMES_RECEIVED||
|OT_LINK_METRICS_STATUS_OTHER_ERROR||

## Typedefs

### otLinkMetricsValues

`typedef struct otLinkMetricsValues otLinkMetricsValues`

**Description:**

Represents the result (value) for a Link Metrics query.

### otLinkMetricsSeriesFlags

`typedef struct otLinkMetricsSeriesFlags otLinkMetricsSeriesFlags`

**Description:**

Represents which frames are accounted in a Forward Tracking Series.

### otLinkMetricsEnhAckFlags (Typedefs)

`typedef enum otLinkMetricsEnhAckFlags otLinkMetricsEnhAckFlags`

**Description:**

Enhanced-ACK Flags.

**Details:**

These are used in Enhanced-ACK Based Probing to indicate whether to register or clear the probing.

### otLinkMetricsStatus (Typedefs)

`typedef enum otLinkMetricsStatus otLinkMetricsStatus`

**Description:**

Link Metrics Status values.

### otLinkMetricsReportCallback

`typedef void(* otLinkMetricsReportCallback) (const otIp6Address *aSource, const otLinkMetricsValues *aMetricsValues, otLinkMetricsStatus aStatus, void *aContext)`

**Description:**

Pointer is called when a Link Metrics report is received.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aSource|A pointer to the source address.|
||[in]|aMetricsValues|A pointer to the Link Metrics values (the query result).|
||[in]|aStatus|The status code in the report (only useful when `aMetricsValues` is NULL).|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otLinkMetricsMgmtResponseCallback

`typedef void(* otLinkMetricsMgmtResponseCallback) (const otIp6Address *aSource, otLinkMetricsStatus aStatus, void *aContext)`

**Description:**

Pointer is called when a Link Metrics Management Response is received.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aSource|A pointer to the source address.|
||[in]|aStatus|The status code in the response.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

### otLinkMetricsEnhAckProbingIeReportCallback

`typedef void(* otLinkMetricsEnhAckProbingIeReportCallback) (otShortAddress aShortAddress, const otExtAddress *aExtAddress, const otLinkMetricsValues *aMetricsValues, void *aContext)`

**Description:**

Pointer is called when Enh-ACK Probing IE is received.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
||[in]|aShortAddress|The Mac short address of the Probing Subject.|
||[in]|aExtAddress|A pointer to the Mac extended address of the Probing Subject.|
||[in]|aMetricsValues|A pointer to the Link Metrics values obtained from the IE.|
||[in]|aContext|A pointer to application-specific context.|

**Details:**

## Functions

### otLinkMetricsQuery

`otError otLinkMetricsQuery(otInstance *aInstance, const otIp6Address *aDestination, uint8_t aSeriesId, const otLinkMetrics *aLinkMetricsFlags, otLinkMetricsReportCallback aCallback, void *aCallbackContext)`

**Description:** Sends an MLE Data Request to query Link Metrics.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aDestination|A pointer to the destination address.|
|uint8_t|[in]|aSeriesId|The Series ID to query about, 0 for Single Probe.|
|const [otLinkMetrics](ot-link-metrics) *|[in]|aLinkMetricsFlags|A pointer to flags specifying what metrics to query.|
|[otLinkMetricsReportCallback](api-link-metrics#ot-link-metrics-report-callback)|[in]|aCallback|A pointer to a function that is called when Link Metrics report is received.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

It could be either Single Probe or Forward Tracking Series.

### otLinkMetricsConfigForwardTrackingSeries

`otError otLinkMetricsConfigForwardTrackingSeries(otInstance *aInstance, const otIp6Address *aDestination, uint8_t aSeriesId, otLinkMetricsSeriesFlags aSeriesFlags, const otLinkMetrics *aLinkMetricsFlags, otLinkMetricsMgmtResponseCallback aCallback, void *aCallbackContext)`

**Description:** Sends an MLE Link Metrics Management Request to configure or clear a Forward Tracking Series.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aDestination|A pointer to the destination address.|
|uint8_t|[in]|aSeriesId|The Series ID to operate with.|
|[otLinkMetricsSeriesFlags](ot-link-metrics-series-flags)|[in]|aSeriesFlags|The Series Flags that specifies which frames are to be accounted.|
|const [otLinkMetrics](ot-link-metrics) *|[in]|aLinkMetricsFlags|A pointer to flags specifying what metrics to query. Should be `NULL` when `aSeriesFlags` is `0`.|
|[otLinkMetricsMgmtResponseCallback](api-link-metrics#ot-link-metrics-mgmt-response-callback)|[in]|aCallback|A pointer to a function that is called when Link Metrics Management Response is received.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|

### otLinkMetricsConfigEnhAckProbing

`otError otLinkMetricsConfigEnhAckProbing(otInstance *aInstance, const otIp6Address *aDestination, otLinkMetricsEnhAckFlags aEnhAckFlags, const otLinkMetrics *aLinkMetricsFlags, otLinkMetricsMgmtResponseCallback aCallback, void *aCallbackContext, otLinkMetricsEnhAckProbingIeReportCallback aEnhAckCallback, void *aEnhAckCallbackContext)`

**Description:** Sends an MLE Link Metrics Management Request to configure/clear an Enhanced-ACK Based Probing.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aDestination|A pointer to the destination address.|
|[otLinkMetricsEnhAckFlags](api-link-metrics#ot-link-metrics-enh-ack-flags)|[in]|aEnhAckFlags|Enh-ACK Flags to indicate whether to register or clear the probing. `0` to clear and `1` to register. Other values are reserved.|
|const [otLinkMetrics](ot-link-metrics) *|[in]|aLinkMetricsFlags|A pointer to flags specifying what metrics to query. Should be `NULL` when `aEnhAckFlags` is `0`.|
|[otLinkMetricsMgmtResponseCallback](api-link-metrics#ot-link-metrics-mgmt-response-callback)|[in]|aCallback|A pointer to a function that is called when an Enhanced Ack with Link Metrics is received.|
|void *|[in]|aCallbackContext|A pointer to application-specific context.|
|[otLinkMetricsEnhAckProbingIeReportCallback](api-link-metrics#ot-link-metrics-enh-ack-probing-ie-report-callback)|N/A|aEnhAckCallback||
|void *|N/A|aEnhAckCallbackContext||

This functionality requires OT_LINK_METRICS_INITIATOR feature enabled.

### otLinkMetricsSendLinkProbe

`otError otLinkMetricsSendLinkProbe(otInstance *aInstance, const otIp6Address *aDestination, uint8_t aSeriesId, uint8_t aLength)`

**Description:** Sends an MLE Link Probe message.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otIp6Address](ot-ip6-address) *|[in]|aDestination|A pointer to the destination address.|
|uint8_t|[in]|aSeriesId|The Series ID [1, 254] which the Probe message aims at.|
|uint8_t|[in]|aLength|The length of the data payload in Link Probe TLV, [0, 64] (per Thread 1.2 spec, 4.4.37).|

### otLinkMetricsManagerIsEnabled

`bool otLinkMetricsManagerIsEnabled(otInstance *aInstance)`

**Description:** If Link Metrics Manager is enabled.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|

### otLinkMetricsManagerSetEnabled

`void otLinkMetricsManagerSetEnabled(otInstance *aInstance, bool aEnable)`

**Description:** Enable or disable Link Metrics Manager.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|bool|[in]|aEnable|A boolean indicating to enable or disable.|

### otLinkMetricsManagerGetMetricsValueByExtAddr

`otError otLinkMetricsManagerGetMetricsValueByExtAddr(otInstance *aInstance, const otExtAddress *aExtAddress, otLinkMetricsValues *aLinkMetricsValues)`

**Description:** Get Link Metrics data of a neighbor by its extended address.

**Parameters:**

|Type|Direction|Argument Name|Description|
|----|---------|-------------|-----------|
|[otInstance](api-instance#ot-instance) *|[in]|aInstance|A pointer to an OpenThread instance.|
|const [otExtAddress](ot-ext-address) *|[in]|aExtAddress|A pointer to the Mac extended address of the Probing Subject.|
|[otLinkMetricsValues](ot-link-metrics-values) *|[out]|aLinkMetricsValues|A pointer to the Link Metrics values of the subject.|
