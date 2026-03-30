# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-message-settings.md

Represents a message settings. 

## Public Attributes

### mLinkSecurityEnabled

```
bool otMessageSettings::mLinkSecurityEnabled
```

**Description:** TRUE if the message should be secured at Layer 2.

### mPriority

```
uint8_t otMessageSettings::mPriority
```

**Description:** Priority level (MUST be a `OT_MESSAGE_PRIORITY_*` from `otMessagePriority`).