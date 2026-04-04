# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.md.txt

# AppDistributionRelease

# AppDistributionRelease


```
interface AppDistributionRelease
```

<br />

*** ** * ** ***

The release information returned by `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/FirebaseAppDistribution#checkForNewRelease()` when a new version is available for the signed in tester.

## Summary

| ### Public functions |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#getBinaryType()()` Returns the binary type for this build. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#getDisplayVersion()()` Returns the short bundle version of this build (example: 1.0.0). |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#getReleaseNotes()()` Returns the release notes for this build. |
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#getVersionCode()()` Returns the version code of this build (example: 123). |

| ### Extension functions |
|---|---|
| `operator https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component1()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide binaryType. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component2()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide displayVersion. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component3()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide versionCode. |
| `operator https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease.https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease#(com.google.firebase.appdistribution.AppDistributionRelease).component4()()` Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide releaseNotes. |

## Public functions

### getBinaryType

```
fun getBinaryType(): BinaryType
```

Returns the binary type for this build.

### getDisplayVersion

```
fun getDisplayVersion(): String
```

Returns the short bundle version of this build (example: 1.0.0).

### getReleaseNotes

```
fun getReleaseNotes(): String?
```

Returns the release notes for this build.

### getVersionCode

```
fun getVersionCode(): Long
```

Returns the version code of this build (example: 123).

## Extension functions

### component1

```
operator fun AppDistributionRelease.component1(): BinaryType
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide binaryType.

| Returns |
|---|---|
| `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/BinaryType` | the binaryType of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

### component2

```
operator fun AppDistributionRelease.component2(): String
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide displayVersion.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html` | the displayVersion of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

### component3

```
operator fun AppDistributionRelease.component3(): Long
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide versionCode.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-long/index.html` | the versionCode of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |

### component4

```
operator fun AppDistributionRelease.component4(): String?
```

Destructuring declaration for `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` to provide releaseNotes.

| Returns |
|---|---|
| `https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-string/index.html?` | the releaseNotes of the `https://firebase.google.com/docs/reference/kotlin/com/google/firebase/appdistribution/AppDistributionRelease` |