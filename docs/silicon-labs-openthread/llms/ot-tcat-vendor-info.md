# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-tcat-vendor-info.md

This structure represents a TCAT vendor information. 

The content of this structure MUST persist and remain unchanged while a TCAT session is running. 

## Public Attributes

### mProvisioningUrl

```
const char* otTcatVendorInfo::mProvisioningUrl
```

**Description:** Provisioning URL path string.

### mVendorName

```
const char* otTcatVendorInfo::mVendorName
```

**Description:** Vendor name string.

### mVendorModel

```
const char* otTcatVendorInfo::mVendorModel
```

**Description:** Vendor model string.

### mVendorSwVersion

```
const char* otTcatVendorInfo::mVendorSwVersion
```

**Description:** Vendor software version string.

### mVendorData

```
const char* otTcatVendorInfo::mVendorData
```

**Description:** Vendor specific data string.

### mPskdString

```
const char* otTcatVendorInfo::mPskdString
```

**Description:** Vendor managed pre-shared key for device.

### mInstallCode

```
const char* otTcatVendorInfo::mInstallCode
```

**Description:** Vendor managed install code string.

### mAdvertisedDeviceIds

```
const otTcatAdvertisedDeviceId* otTcatVendorInfo::mAdvertisedDeviceIds
```

### mGeneralDeviceId

```
const otTcatGeneralDeviceId* otTcatVendorInfo::mGeneralDeviceId
```

**Description:** Vendor managed advertised device ID array.

**Details:** Array is terminated like C string with OT_TCAT_DEVICE_ID_EMPTY

### mApplicationServiceName

```
const char* otTcatVendorInfo::mApplicationServiceName[OT_TCAT_APPLICATION_LAYER_MAX_COUNT]
```

**Description:** Vendor managed general device ID array.

**Details:** (if NULL: device ID is set to EUI-64 in binary format)

### mApplicationServiceIsTcp

```
bool otTcatVendorInfo::mApplicationServiceIsTcp[OT_TCAT_APPLICATION_LAYER_MAX_COUNT]
```

**Description:** Array with application service names as C string with maximum length OT_TCAT_SERVICE_NAME_MAX_LENGTH or NULL if not supported.