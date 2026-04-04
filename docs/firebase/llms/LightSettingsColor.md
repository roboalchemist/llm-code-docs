# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor.md.txt

# LightSettingsColor

public final class **LightSettingsColor** extends Object  
A class representing color in LightSettings.  

### Public Constructor Summary

|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor#LightSettingsColor(float, float, float, float))(float red, float green, float blue, float alpha) Creates a new [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) using the given red, green, blue, and alpha values. |

### Public Method Summary

|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) | [fromString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor#fromString(java.lang.String))(String rrggbb) Creates a new [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) with a string. |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Constructors

#### public
**LightSettingsColor**
(float red, float green, float blue, float alpha)

Creates a new [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) using the given red, green, blue, and
alpha values.  

##### Parameters

|  red  |  The red component.  |
| green | The green component. |
| blue  | The blue component.  |
| alpha | The alpha component. |
|-------|----------------------|

## Public Methods

#### public static [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor)
**fromString**
(String rrggbb)

Creates a new [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) with a string. Alpha of the color will be
set to 1.  

##### Parameters

| rrggbb | LightSettingsColor specified in the `#rrggbb` format. |
|--------|-------------------------------------------------------|

##### Returns

- A [LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) instance.