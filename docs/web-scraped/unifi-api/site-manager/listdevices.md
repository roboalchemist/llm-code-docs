# listdevices

Source: https://developer.ui.com/site-manager/v1.0.0/listdevices

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Devices

GET`/v1/devices`

Retrieves a list of UniFi devices managed by hosts where the UI account making the API call is the owner or a super admin.

**Note**: The structure of the `devices.uidb` field may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

query Parameters

## Responses

200400401429500502

Response Schema: application/json