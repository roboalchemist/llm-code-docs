# VisualShaderNodeFloatParameter

# VisualShaderNodeFloatParameter

Inherits:VisualShaderNodeParameter<VisualShaderNode<Resource<RefCounted<Object
A scalar float parameter to be used within the visual shader graph.

## Description

Translated touniformfloatin the shader language.

## Properties

| float | default_value | 0.0 |
|---|---|---|
| bool | default_value_enabled | false |
| Hint | hint | 0 |
| float | max | 1.0 |
| float | min | 0.0 |
| float | step | 0.1 |

float
default_value
bool
default_value_enabled
false
Hint
hint
float
float
float
step

## Enumerations

enumHint:🔗
HintHINT_NONE=0
No hint used.
HintHINT_RANGE=1
A range hint for scalar value, which limits possible input values betweenminandmax. Translated tohint_range(min,max)in shader code.
HintHINT_RANGE_STEP=2
A range hint for scalar value with step, which limits possible input values betweenminandmax, with a step (increment) ofstep). Translated tohint_range(min,max,step)in shader code.
HintHINT_MAX=3
Represents the size of theHintenum.

## Property Descriptions

floatdefault_value=0.0🔗

- voidset_default_value(value:float)
voidset_default_value(value:float)
- floatget_default_value()
floatget_default_value()
A default value to be assigned within the shader.
booldefault_value_enabled=false🔗
- voidset_default_value_enabled(value:bool)
voidset_default_value_enabled(value:bool)
- boolis_default_value_enabled()
boolis_default_value_enabled()
Enables usage of thedefault_value.
Hinthint=0🔗
- voidset_hint(value:Hint)
voidset_hint(value:Hint)
- Hintget_hint()
Hintget_hint()
A hint applied to the uniform, which controls the values it can take when set through the Inspector.
floatmax=1.0🔗
- voidset_max(value:float)
voidset_max(value:float)
- floatget_max()
floatget_max()
Minimum value for range hints. Used ifhintis set toHINT_RANGEorHINT_RANGE_STEP.
floatmin=0.0🔗
- voidset_min(value:float)
voidset_min(value:float)
- floatget_min()
floatget_min()
Maximum value for range hints. Used ifhintis set toHINT_RANGEorHINT_RANGE_STEP.
floatstep=0.1🔗
- voidset_step(value:float)
voidset_step(value:float)
- floatget_step()
floatget_step()
Step (increment) value for the range hint with step. Used ifhintis set toHINT_RANGE_STEP.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
