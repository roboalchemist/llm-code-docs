# Class: FeatureAPI

Controls the availability of features within the Creative Editor SDK.

The FeatureAPI allows you to enable or disable specific functionality within the editor based on custom conditions or user permissions.

## Understanding the Feature System[#](#understanding-the-feature-system)

The feature system uses a **predicate chain** to determine if a feature is enabled. There are two types of predicates:

1.  **Boolean predicates** (e.g., `true` or `false`) - These are **always terminal** and immediately return their value.
2.  **Function predicates** - The implementation decides whether to call `isPreviousEnable()` (continue chain) or return directly (end chain).

### Evaluation Order[#](#evaluation-order)

  

Predicates are evaluated in this order:

1.  **`set()` predicates** (most recent first) - Evaluated **FIRST**
2.  **`enable()`/`disable()` state** - Evaluated **LAST**

This means **`set()` can override `enable()` and `disable()`**.

## Common Use Cases and Expected Outcomes[#](#common-use-cases-and-expected-outcomes)

### Use Case 1: Simple Enable/Disable[#](#use-case-1-simple-enabledisable)

```
// Enable a feature with its default behaviorcesdk.feature.enable('ly.img.delete');// isEnabled: true
// Disable itcesdk.feature.disable('ly.img.delete');// isEnabled: false
// Re-enable itcesdk.feature.enable('ly.img.delete');// isEnabled: true
```

**Expected outcome:** `enable()` and `disable()` work together to toggle features on/off.

### Use Case 2: Custom Conditions with `set()`[#](#use-case-2-custom-conditions-with-set)

```
// Enable delete only when something is selectedcesdk.feature.set('ly.img.delete', ({ engine }) => {  return engine.block.findAllSelected().length > 0;});// isEnabled: depends on selection
// Now calling disable() won't work because set() is evaluated first!cesdk.feature.disable('ly.img.delete');// isEnabled: still depends on selection (disable is ignored)
```

**Expected outcome:** `set()` function predicates are evaluated before `disable()`, so `disable()` has no effect when a `set()` predicate exists.

### Use Case 3: Terminal Boolean Predicates[#](#use-case-3-terminal-boolean-predicates)

```
cesdk.feature.enable('ly.img.delete'); // Default predicate: truecesdk.feature.set('ly.img.delete', false); // Adds false to front// Chain: [set(false), enable(true)]// Evaluation: false (stops here, never reaches enable)// isEnabled: false
cesdk.feature.set('ly.img.delete', true); // Adds true to front// Chain: [set(true), set(false), enable(true)]// Evaluation: true (stops here, never reaches the rest)// isEnabled: true
```

**Expected outcome:** The most recent `set()` call with a boolean wins because boolean predicates are terminal.

### Use Case 4: Layering Conditions with Functions[#](#use-case-4-layering-conditions-with-functions)

```
// Base: Feature enabled by defaultcesdk.feature.enable('ly.img.delete');
// Layer 1: Add selection requirementcesdk.feature.set('ly.img.delete', ({ isPreviousEnable, engine }) => {  const baseEnabled = isPreviousEnable(); // Checks enable(true)  const hasSelection = engine.block.findAllSelected().length > 0;  return baseEnabled && hasSelection;});// isEnabled: true only if enabled AND has selection
// Layer 2: Add mode requirementcesdk.feature.set('ly.img.delete', ({ isPreviousEnable, engine }) => {  const previousEnabled = isPreviousEnable(); // Checks Layer 1  const isDesignMode = engine.scene.getMode() === 'Design';  return previousEnabled && isDesignMode;});// isEnabled: true only if all conditions met (mode + selection + enabled)
```

**Expected outcome:** Each `set()` call with a function can build on previous conditions by calling `isPreviousEnable()`.

### Use Case 5: Overriding with `set()`[#](#use-case-5-overriding-with-set)

```
cesdk.feature.enable('ly.img.delete');cesdk.feature.disable('ly.img.delete');// isEnabled: false (disable overrides enable)
// But set() overrides both:cesdk.feature.set('ly.img.delete', true);// Chain: [set(true), disable(false)]// isEnabled: true (set is terminal, disable never evaluated)
```

**Expected outcome:** `set()` with a boolean always wins because it’s evaluated first and is terminal.

### Use Case 6: Glob Patterns for Bulk Operations[#](#use-case-6-glob-patterns-for-bulk-operations)

```
// Enable all video features at oncecesdk.feature.enable('ly.img.video.*');
// Disable all crop featurescesdk.feature.disable('ly.img.crop.*');
// Set custom predicate for all navigation featurescesdk.feature.set('ly.img.navigation.*', ({ engine }) => {  return engine.scene.getMode() === 'Design';});
// Check if all video features are enabledconst allVideoEnabled = cesdk.feature.isEnabled('ly.img.video.*');// Returns true only if ALL matching features are enabled
```

**Expected outcome:** Glob patterns match multiple features. `isEnabled()` with a glob returns `true` only if **all** matching features are enabled.

### Use Case 7: Role-Based Access Control[#](#use-case-7-role-based-access-control)

```
const userRole = 'editor'; // Could be 'viewer', 'editor', 'admin'
cesdk.feature.set('ly.img.delete', () => {  return userRole === 'editor' || userRole === 'admin';});
cesdk.feature.set('ly.img.settings', () => {  return userRole === 'admin';});
```

**Expected outcome:** Features are enabled based on user roles, with predicates evaluated on every check.

## Key Principles[#](#key-principles)

1.  **Use `enable()` for simple on/off** - Works with default predicates
2.  **Use `disable()` to turn off enabled features** - Only works if no `set()` predicates exist
3.  **Use `set()` for custom logic** - Overrides `enable()`/`disable()`
4.  **Boolean predicates are terminal** - Stop evaluation immediately
5.  **Function predicates can chain** - Call `isPreviousEnable()` to continue
6.  **Most recent `set()` wins** - Evaluated in LIFO order (most recent first)
7.  **Glob patterns affect multiple features** - Use `*` as wildcard

## Constructors[#](#constructors)

### Constructor[#](#constructor)

  

`FeatureAPI`

## Feature Control[#](#feature-control)

Methods for enabling and checking the status of editor features based on custom predicates.

### enable()[#](#enable)

  

Enables one or more features using their default predicates.

This is the recommended way to enable features. Each feature has a sensible default predicate that determines when it should be available in the UI. To customize the behavior, use the `set()` method instead.

Supports glob patterns (e.g., ‘ly.img.video.\*’) to enable multiple features at once. Use `*` as a wildcard to match any sequence of characters.

##### Parameters[#](#parameters)

| Parameter | Type | Description |
| --- | --- | --- |
| `featureId` |  | [`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) |

##### Returns[#](#returns)

`void`

##### Examples[#](#examples)

Enable single feature with its default predicate:

```
cesdk.feature.enable('ly.img.delete');
```

Enable multiple features at once:

```
cesdk.feature.enable(['ly.img.delete', 'ly.img.duplicate']);
```

Enable all video features using a glob pattern:

```
cesdk.feature.enable('ly.img.video.*');
```

Enable all navigation features:

```
cesdk.feature.enable('ly.img.navigation.*');
```

#### Call Signature[#](#call-signature)

```
enable(featureId, predicate): void;
```

##### Parameters[#](#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `featureId` |  | [`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) |
| `predicate` | [`FeaturePredicate`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featurepredicate/) | The condition that determines if the feature is enabled. |

##### Returns[#](#returns-1)

`void`

##### Deprecated[#](#deprecated)

Use `cesdk.feature.set(featureId, predicate)` instead. This overload will be removed in a future version.

Enables one or more features based on the provided predicate.

#### Signatures[#](#signatures)

```
enable(featureId: FeatureId | FeatureId[]): void
```

```
enable(featureId: FeatureId | FeatureId[], predicate: FeaturePredicate): void
```

* * *

### disable()[#](#disable)

  

Disables one or more features.

This is a convenience method that adds a `false` predicate to the feature’s predicate chain, effectively disabling the feature. Disabled features will not be shown in the UI.

Supports glob patterns (e.g., ‘ly.img.video.\*’) to disable multiple features at once. Use `*` as a wildcard to match any sequence of characters.

#### Parameters[#](#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `featureId` |  | [`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) |

#### Returns[#](#returns-2)

`void`

#### Examples[#](#examples-1)

Disable a single feature:

```
cesdk.feature.disable('ly.img.delete');
```

Disable multiple features at once:

```
cesdk.feature.disable([  'ly.img.delete',  'ly.img.duplicate',  'ly.img.group']);
```

Disable all video features using a glob pattern:

```
cesdk.feature.disable('ly.img.video.*');
```

Disable all crop features:

```
cesdk.feature.disable('ly.img.crop.*');
```

#### Signature[#](#signature)

```
disable(featureId: FeatureId | FeatureId[]): void
```

* * *

### set()[#](#set)

  

Sets a feature’s enabled state, replacing any existing predicates.

This method provides a unified way to enable or disable features. When setting to `true`, the feature’s default predicate is used. When setting to `false`, the feature is explicitly disabled. You can also provide a custom predicate function for advanced control.

Supports glob patterns (e.g., ‘ly.img.video.\*’) to set multiple features at once. Use `*` as a wildcard to match any sequence of characters.

#### Parameters[#](#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `featureId` | [`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) | The feature ID or glob pattern to set. |
| `enabled` | [`FeaturePredicate`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featurepredicate/) | Boolean to enable/disable, or a predicate function for custom logic. |

#### Returns[#](#returns-3)

`void`

#### Examples[#](#examples-2)

Enable a feature using its default predicate:

```
cesdk.feature.set('ly.img.delete', true);
```

Disable a feature:

```
cesdk.feature.set('ly.img.delete', false);
```

Set a feature with a custom predicate:

```
cesdk.feature.set('ly.img.delete', ({ engine }) => {  return engine.block.findAllSelected().length > 0;});
```

Disable all video features using a glob pattern:

```
cesdk.feature.set('ly.img.video.*', false);
```

Enable all filter features with a custom predicate:

```
cesdk.feature.set('ly.img.filter.*', ({ engine }) => {  // Only enable filters for images  const selected = engine.block.findAllSelected();  return selected.some(id => engine.block.getType(id) === '//ly.img.ubq/graphic');});
```

#### Signature[#](#signature-1)

```
set(featureId: FeatureId, enabled: FeaturePredicate): void
```

* * *

### list()[#](#list)

  

Lists all registered feature IDs, optionally filtered by a pattern.

This method is useful for debugging and discovering which features are currently registered in the editor. You can provide a glob-style pattern to filter the results.

#### Parameters[#](#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `options?` | { `matcher?`: `string`; } | Optional configuration object with a `matcher` property for glob-style pattern filtering (e.g., ‘ly.img.video.\*’). |
| `options.matcher?` | `string` | \- |

#### Returns[#](#returns-4)

[`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/)\[\]

An array of feature IDs sorted alphabetically.

#### Examples[#](#examples-3)

List all registered features:

```
const allFeatures = cesdk.feature.list();console.log(allFeatures); // ['ly.img.delete', 'ly.img.duplicate', ...]
```

List features matching a pattern:

```
const videoFeatures = cesdk.feature.list({ matcher: 'ly.img.video.*' });console.log(videoFeatures); // ['ly.img.video.timeline', 'ly.img.video.clips', ...]
```

List navigation features:

```
const navFeatures = cesdk.feature.list({ matcher: 'ly.img.navigation.*' });
```

#### Signature[#](#signature-2)

```
list(options?: object): FeatureId[]
```

* * *

### get()[#](#get)

  

Gets the predicate chain for a specific feature.

This method returns the array of predicates currently registered for a feature, allowing you to inspect the feature’s configuration. Returns `undefined` if the feature is not registered.

#### Parameters[#](#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `featureId` | [`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) | The feature ID to query. |

#### Returns[#](#returns-5)

[`FeaturePredicate`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featurepredicate/)\[\]

The array of predicates for the feature, or undefined if not registered.

#### Examples[#](#examples-4)

Get predicates for a feature:

```
const predicates = cesdk.feature.get('ly.img.delete');if (predicates) {  console.log(`Feature has ${predicates.length} predicates`);}
```

Check if a feature is registered:

```
const isRegistered = cesdk.feature.get('ly.img.delete') !== undefined;
```

#### Signature[#](#signature-3)

```
get(featureId: FeatureId): FeaturePredicate[]
```

* * *

### isEnabled()[#](#isenabled)

  

Checks if one or more features are currently enabled.

Supports glob patterns (e.g., ‘ly.img.video.\*’) to check multiple features at once. When a glob pattern is used, returns `true` only if **all** matching features are enabled.

#### Parameters[#](#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `featureId` | [`FeatureId`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/featureid/) | The feature ID or glob pattern to check. |
| `context?` | [`IsEnabledFeatureContext`](https://img.ly/docs/cesdk/vue/api/cesdk-js/type-aliases/isenabledfeaturecontext/) | The context object containing a reference to the underlying engine. |

#### Returns[#](#returns-6)

`boolean`

True if the feature (or all matching features for glob patterns) is enabled, false otherwise.

#### Examples[#](#examples-5)

Check if a single feature is enabled:

```
const isDeleteEnabled = cesdk.feature.isEnabled('ly.img.delete');
```

Check if all video features are enabled:

```
const allVideoFeaturesEnabled = cesdk.feature.isEnabled('ly.img.video.*');
```

Check with custom context (useful in predicates):

```
cesdk.feature.set('ly.img.delete', ({ engine }) => {  return cesdk.feature.isEnabled('ly.img.duplicate', { engine });});
```

#### Signature[#](#signature-4)

```
isEnabled(featureId: FeatureId, context?: IsEnabledFeatureContext): boolean
```

---



[Source](https:/img.ly/docs/cesdk/vue/api/cesdk-js/classes/eventapi)