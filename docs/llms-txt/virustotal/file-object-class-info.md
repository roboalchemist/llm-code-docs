# Source: https://virustotal.readme.io/reference/file-object-class-info.md

# class_info

information about Java .class bytecode files.

`class_info` gives information about Java bytecode files.

* `constants`: <*list of strings*> used constants in this class.
* `extends`: <*string*> class that this one inherits.
* `implements`: <*list of strings*> implemented interfaces.
* `methods`: <*list of strings*> methods belonging to the class.
* `name`: <*string*> class name.
* `platform`: <*string*> platform as a string, derived from major and minor version number.
* `provides`: <*list of strings*> provided classes, fields and methods.
* `requires`: <*list of strings*> required classes, fields and methods.

```json
{
  "data": {
		...
    "attributes" : {
      ...
      "class_info": {
        "constants": ["<strings>"],
        "extends": "<string>",
        "implements": ["<strings>"],
        "methods": ["<strings>"],
        "name": "<string>",
        "platform": "<string>",
        "provides": ["<strings>"],
        "requires": ["<strings>"]
      }
    }
  }
}
```
```json
{
    "data": {
        "attributes": {
            "class_info": {
                "constants": [
                    "StackMap",
                    "equals",
                    "getCurrent",
                    "getTime",
                    "java/lang/Exception",
                    "java/lang/Object",
                    "java/util/Date",
                    "javax/microedition/lcdui/Command",
                    "jimm/Jimm",
                    "setTime",
                    "toString"
                ],
                "extends": "java.lang.Object",
                "implements": [
                    "javax.blabla.blabla.CommandListener"
                ],
                "methods": [
                    "<init>",
                    "a",
                    "a",
                    "commandAction"
                ],
                "name": "al",
                "platform": "1.0.2",
                "provides": [
                    "al.a",
                    "al.commandAction",
                    "al.<init>",
                    "al.a"
                ],
                "requires": [
                    "java.lang.StringBuffer.<init>():void",
                    "java.lang.StringBuffer.toString():java.lang.String",
                    "java.util.Date.<init>():void",
                    "v.a():void",
                    "bz.a(java.lang.String):java.lang.String",
                    "cg",
                    "bb.a(int):java.lang.String",
                    "bb.b:int"
                ]
            }
        }
    }
}
```