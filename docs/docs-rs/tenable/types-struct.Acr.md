tenable::types
# Struct Acr 
Source 

```
pub struct Acr {
    pub acr_score: u64,
    pub reason: Option<Vec<AcrUpdateReason>>,
    pub note: Option<String>,
    pub asset: Vec<AcrAsset>,
}
```

## Fields§
§`acr_score: u64`

The ACR score you want to assign to the asset. The ACR must be an integer from 1 to 10.
§`reason: Option<Vec<AcrUpdateReason>>`

The reasons you are updating the ACR for the assets. Supported values include:\n\n - Business Critical\n - In Scope For Compliance\n - Existing Mitigation Control\n - Dev only \n - Key drivers does not match \n - Other\n\nThis parameter corresponds to the **Overwrite Reasoning** parameter when editing an ACR in the Tenable.io Lumin user interface. For more information, see Edit an ACR.
§`note: Option<String>`

Any notes you want to add to clarify the circumstances behind the update. This parameter corresponds to the **Note** parameter when editing an ACR in the Tenable.io Lumin user interface. For more information, see Edit an ACR.
§`asset: Vec<AcrAsset>`

The identifiers of the assets to update to the specified ACR. At least one asset object is required in this array.

## Trait Implementations§