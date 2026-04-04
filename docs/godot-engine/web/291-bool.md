# bool

# bool
A built-in boolean type.

## Description
Theboolis a built-inVarianttype that may only store one of two values:trueorfalse. You can imagine it as a switch that can be either turned on or off, or as a binary digit that can either be 1 or 0.
Booleans can be directly used inif, and other conditional statements:
```
var can_shoot = true
if can_shoot:
    launch_bullet()
```
```
bool canShoot = true;
if (canShoot)
{
    LaunchBullet();
}
```
All comparison operators return booleans (==,>,<=, etc.). As such, it is not necessary to compare booleans themselves. You do not need to add==trueor==false.
Booleans can be combined with the logical operatorsand,or,notto create complex conditions:
```
if bullets > 0 and not is_reloading():
    launch_bullet()

if bullets == 0 or is_reloading():
    play_clack_sound()
```
```
if (bullets > 0 && !IsReloading())
{
    LaunchBullet();
}

if (bullets == 0 || IsReloading())
{
    PlayClackSound();
}
```
Note:In modern programming languages, logical operators are evaluated in order. All remaining conditions are skipped if their result would have no effect on the final value. This concept is known asshort-circuit evaluationand can be useful to avoid evaluating expensive conditions in some performance-critical cases.
Note:By convention, built-in methods and properties that return booleans are usually defined as yes-no questions, single adjectives, or similar (String.is_empty(),Node.can_process(),Camera2D.enabled, etc.).

## Constructors

| bool | bool() |
|---|---|
| bool | bool(from:bool) |
| bool | bool(from:float) |
| bool | bool(from:int) |

bool
bool()
bool
bool(from:bool)
bool
bool(from:float)
bool
bool(from:int)

## Operators

| bool | operator !=(right:bool) |
|---|---|
| bool | operator <(right:bool) |
| bool | operator ==(right:bool) |
| bool | operator >(right:bool) |

bool
operator !=(right:bool)
bool
operator <(right:bool)
bool
operator ==(right:bool)
bool
operator >(right:bool)

## Constructor Descriptions
boolbool()🔗
Constructs aboolset tofalse.
boolbool(from:bool)
Constructs aboolas a copy of the givenbool.
boolbool(from:float)
Cast afloatvalue to a boolean value. Returnsfalseiffromis equal to0.0(including-0.0), andtruefor all other values (including@GDScript.INFand@GDScript.NAN).
boolbool(from:int)
Cast anintvalue to a boolean value. Returnsfalseiffromis equal to0, andtruefor all other values.

## Operator Descriptions
booloperator !=(right:bool)🔗
Returnstrueif the two booleans are not equal. That is, one istrueand the other isfalse. This operation can be seen as a logical XOR.
booloperator <(right:bool)🔗
Returnstrueif the left operand isfalseand the right operand istrue.
booloperator ==(right:bool)🔗
Returnstrueif the two booleans are equal. That is, both aretrueor both arefalse. This operation can be seen as a logical EQ or XNOR.
booloperator >(right:bool)🔗
Returnstrueif the left operand istrueand the right operand isfalse.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.