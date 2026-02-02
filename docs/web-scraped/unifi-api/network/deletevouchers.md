# deletevouchers

Source: https://developer.ui.com/network/v10.1.68/deletevouchers

UniFi APIEndpoints combined into Ansible Modules for customized workflows.Delete VouchersDELETE/v1/sites/{siteId}/hotspot/vouchersRemove Hotspot vouchers based on the specified filter criteria.
Filterable properties (click to expand)NameTypeAllowed functionsidUUIDeq ne in notIncreatedAtTIMESTAMPeq ne gt ge lt lenameSTRINGeq ne in notIn likecodeSTRINGeq ne in notInauthorizedGuestLimitINTEGERisNull isNotNull eq ne gt ge lt leauthorizedGuestCountINTEGEReq ne gt ge lt leactivatedAtTIMESTAMPeq ne gt ge lt leexpiresAtTIMESTAMPeq ne gt ge lt leexpiredBOOLEANeq netimeLimitMinutesINTEGEReq ne gt ge lt ledataUsageLimitMBytesINTEGERisNull isNotNull eq ne gt ge lt lerxRateLimitKbpsINTEGERisNull isNotNull eq ne gt ge lt letxRateLimitKbpsINTEGERisNull isNotNull eq ne gt ge lt lepath Parametersquery ParametersResponses200Response Schema: application/json