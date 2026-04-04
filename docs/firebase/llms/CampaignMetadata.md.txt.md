# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata.md.txt

# CampaignMetadata

# CampaignMetadata


```
public class CampaignMetadata
```

<br />

*** ** * ** ***

Provides the following about any message:

- Campaign ID
- Campaign Name
- Campaign Test Message State

## Summary

| ### Public fields |
|---|---|
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata#campaignId()` |
| `final https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata#campaignName()` |
| `final boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata#isTestMessage()` |

| ### Public methods |
|---|---|
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata#getCampaignId()()` Gets the campaign id associated with this message |
| `@https://developer.android.com/reference/kotlin/androidx/annotation/NonNull.html https://developer.android.com/reference/kotlin/java/lang/String.html` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata#getCampaignName()()` Gets the campaign name associated with this message |
| `boolean` | `https://firebase.google.com/docs/reference/android/com/google/firebase/inappmessaging/model/CampaignMetadata#getIsTestMessage()()` Returns true if the message is a test message |

## Public fields

### campaignId

```
public final String campaignId
```

### campaignName

```
public final String campaignName
```

### isTestMessage

```
public final boolean isTestMessage
```

## Public methods

### getCampaignId

```
public @NonNull String getCampaignId()
```

Gets the campaign id associated with this message

### getCampaignName

```
public @NonNull String getCampaignName()
```

Gets the campaign name associated with this message

### getIsTestMessage

```
public boolean getIsTestMessage()
```

Returns true if the message is a test message