# Type Alias: Scope

```
type Scope =  | "text/edit"  | "text/character"  | "fill/change"  | "fill/changeType"  | "stroke/change"  | "shape/change"  | "layer/move"  | "layer/resize"  | "layer/rotate"  | "layer/flip"  | "layer/crop"  | "layer/opacity"  | "layer/blendMode"  | "layer/visibility"  | "layer/clipping"  | "appearance/adjustments"  | "appearance/filter"  | "appearance/effect"  | "appearance/blur"  | "appearance/shadow"  | "appearance/animation"  | "lifecycle/destroy"  | "lifecycle/duplicate"  | "editor/add"  | "editor/select";
```

Represents the various scopes that define the capabilities and permissions within the Creative Editor SDK. Each scope corresponds to a specific functionality or action that can be performed within the editor.

The `Scope` type is used to control access to different features and operations, allowing for fine-grained control over what actions are permitted.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/type-aliases/scenemode)