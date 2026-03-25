# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp/analyzer-action-codes-and-usages-pentaho-analyzer-external-javascript-api.md

# Analyzer Action Codes and Usages

Analyzer actions map to codes called action codes. Each action code can be used to trigger an action through the `onActionEvent` call. Action events require an action context along with the action code. This context can be different for each of the actions codes. Each action code listed below includes the action context passed along with the action code and one or more use case examples.

The following action codes and action contexts are passed along to identify specific action events.

## actionAddLevel

This action code adds a level to a gembar when passed through `onActionEvent`. The action context passed along with the `actionAddLevel` code is a JSON object. The key is formula and the value is the level's MDX.

The following is a use case example of executing listener code each time the `actionAddLevel` is triggered.

```javascript
// actionCtx = { formula : "[Measures].[Quantity]" };
cv.api.event.registerActionEventListener(function(e, cv, actionCode, actionCtx) {
  if(actionCode == "actionAddMeasure") {
    // Execute listener code
  }
});

```

## actionAddMeasure

This action code adds a measure to a gembar when passed through `onActionEvent`. The action context passed along with the `actionAddMeasure` code is a JSON object. The key is formula and the value is the level's MDX.

The following is a use case example of executing listener code each time `actionAddMeasure` is triggered.

```javascript
// actionCtx = { formula : "[Measures].[Quantity]" };
cv.api.event.registerActionEventListener(function(e, cv, actionCode, actionCtx) {
  if(actionCode == "actionAddMeasure") {
    // Execute listener code
  }
});

```

## actionMoveLevel

This action code moves levels between gembars when passed through `onActionEvent`. The action context passed along with the actionMoveLevel code is a JSON object. The key is formula and the value is the level's MDX.

The following is a use case example of executing listener code each time `actionMoveLevel` is triggered.

```javascript
// actionCtx = { formula : "[Markets].[State]" };
cv.api.event.registerActionEventListener(function(e, cv, actionCode, actionCtx) {
  if(actionCode == "actionMoveLevel") {
    // Execute listener code
  }
});

```

## actionMoveMeasure

This action code moves measures between gembars when passed through `onActionEvent`. The action context passed along with the `actionAddMeasure` code is a JSON object. The key is formula and the value is the level's MDX.

The following is a use case example of executing listener code each time the `actionMoveMeasure` is triggered.

```javascript
// actionCtx = { formula : "[Measures].[Quantity]" };
cv.api.event.registerActionEventListener(function(e, cv, actionCode, actionCtx) {
  if(actionCode == "actionMoveMeasure") {
    // Execute listener code
  }
});

```

## actionRemoveLevel

This action code removes a level from a gembar when passed through `onActionEvent`. The action context passed along with the `actionRemoveLevel` code is a JSON object. The key is formula and the value is the level's MDX.

The following is a use case example of executing some listener code each time `actionRemoveLevel` is triggered.

```javascript
// actionCtx = { formula : "[Markets].[State]" };
cv.api.event.registerActionEventListener(function(e, cv, actionCode, actionCtx) {
  if(actionCode == "actionRemoveLevel") {
    // Execute listener code
  }
});

```

## actionRemoveMeasure

This action code removes a measure from a gembar when passed through `onActionEvent`. The action context passed along with the `actionRemoveMeasure` code is a JSON object. The key is formula and the value is the level's MDX.

The following is a use case example of executing some listener code each time `actionRemoveMeasure` is triggered.

```javascript
// actionCtx = { formula : "[Measures].[Quantity]" };
cv.api.event.registerActionEventListener(function(e, cv, actionCode, actionCtx) {
  if(actionCode == "actionRemoveMeasure") {
    // Execute listener code
  }
});

```
