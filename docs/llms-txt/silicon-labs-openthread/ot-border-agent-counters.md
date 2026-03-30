# Source: https://docs.silabs.com/openthread/3.0.0/openthread-api/ot-border-agent-counters.md

Defines Border Agent counters. 

The `mEpskc` related counters require `OPENTHREAD_CONFIG_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`. 

## Public Attributes

### mEpskcActivations

```
uint32_t otBorderAgentCounters::mEpskcActivations
```

**Description:** The number of ePSKc activations.

### mEpskcDeactivationClears

```
uint32_t otBorderAgentCounters::mEpskcDeactivationClears
```

**Description:** The number of ePSKc deactivations via API.

### mEpskcDeactivationTimeouts

```
uint32_t otBorderAgentCounters::mEpskcDeactivationTimeouts
```

**Description:** The number of ePSKc deactivations due to timeout.

### mEpskcDeactivationMaxAttempts

```
uint32_t otBorderAgentCounters::mEpskcDeactivationMaxAttempts
```

**Description:** The number of ePSKc deactivations due to reached max attempts.

### mEpskcDeactivationDisconnects

```
uint32_t otBorderAgentCounters::mEpskcDeactivationDisconnects
```

**Description:** The number of ePSKc deactivations due to commissioner disconnected.

### mEpskcInvalidBaStateErrors

```
uint32_t otBorderAgentCounters::mEpskcInvalidBaStateErrors
```

**Description:** The number of invalid border agent state errors at ePSKc activation.

### mEpskcInvalidArgsErrors

```
uint32_t otBorderAgentCounters::mEpskcInvalidArgsErrors
```

**Description:** The number of invalid args errors at ePSKc activation.

### mEpskcStartSecureSessionErrors

```
uint32_t otBorderAgentCounters::mEpskcStartSecureSessionErrors
```

**Description:** The number of start secure session errors at ePSKc activation.

### mEpskcSecureSessionSuccesses

```
uint32_t otBorderAgentCounters::mEpskcSecureSessionSuccesses
```

**Description:** The number of established secure sessions with ePSKc.

### mEpskcSecureSessionFailures

```
uint32_t otBorderAgentCounters::mEpskcSecureSessionFailures
```

**Description:** The number of failed secure sessions with ePSKc.

### mEpskcCommissionerPetitions

```
uint32_t otBorderAgentCounters::mEpskcCommissionerPetitions
```

**Description:** The number of successful commissioner petitions with ePSKc.

### mPskcSecureSessionSuccesses

```
uint32_t otBorderAgentCounters::mPskcSecureSessionSuccesses
```

**Description:** The number of established secure sessions with PSKc.

### mPskcSecureSessionFailures

```
uint32_t otBorderAgentCounters::mPskcSecureSessionFailures
```

**Description:** The number of failed secure sessions with PSKc.

### mPskcCommissionerPetitions

```
uint32_t otBorderAgentCounters::mPskcCommissionerPetitions
```

**Description:** The number of successful commissioner petitions with PSKc.

### mMgmtActiveGets

```
uint32_t otBorderAgentCounters::mMgmtActiveGets
```

**Description:** The number of MGMT_ACTIVE_GET.req sent over secure sessions.

### mMgmtPendingGets

```
uint32_t otBorderAgentCounters::mMgmtPendingGets
```

**Description:** The number of MGMT_PENDING_GET.req sent over secure sessions.