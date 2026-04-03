# Class reference primer in English

# Class reference primer
This page explains how to write the class reference. You will learn where to
write new descriptions for the classes, methods, and properties for Godot's
built-in node types.
See also
To learn to submit your changes to the Godot project using the Git version
control system, seeClass reference contribution documentation.
The reference for each class is contained in an XML file like the one below:
```
<class name="Node2D" inherits="CanvasItem" version="4.0">
    <brief_description>
        A 2D game object, inherited by all 2D-related nodes. Has a position, rotation, scale, and Z index.
    </brief_description>
    <description>
        A 2D game object, with a transform (position, rotation, and scale). All 2D nodes, including physics objects and sprites, inherit from Node2D. Use Node2D as a parent node to move, scale and rotate children in a 2D project. Also gives control of the node's render order.
    </description>
    <tutorials>
        <link title="Custom drawing in 2D">https://docs.godotengine.org/en/latest/tutorials/2d/custom_drawing_in_2d.html</link>
        <link title="All 2D Demos">https://github.com/godotengine/godot-demo-projects/tree/master/2d</link>
    </tutorials>
    <methods>
        <method name="apply_scale">
            <return type="void">
            </return>
            <argument index="0" name="ratio" type="Vector2">
            </argument>
            <description>
                Multiplies the current scale by the [code]ratio[/code] vector.
            </description>
        </method>
        [...]
        <method name="translate">
            <return type="void">
            </return>
            <argument index="0" name="offset" type="Vector2">
            </argument>
            <description>
                Translates the node by the given [code]offset[/code] in local coordinates.
            </description>
        </method>
    </methods>
    <members>
        <member name="global_position" type="Vector2" setter="set_global_position" getter="get_global_position">
            Global position.
        </member>
        [...]
        <member name="z_index" type="int" setter="set_z_index" getter="get_z_index" default="0">
            Z index. Controls the order in which the nodes render. A node with a higher Z index will display in front of others.
        </member>
    </members>
    <constants>
    </constants>
</class>
```
It starts with brief and long descriptions. In the generated docs, the brief
description is always at the top of the page, while the long description lies
below the list of methods, variables, and constants. You can find methods,
member variables, constants, and signals in separate XML nodes.
For each, you want to learn how they work in Godot's source code. Then, fill
their documentation by completing or improving the text in these tags:
- <brief_description>
<brief_description>
- <description>
<description>
- <constant>
<constant>
- <method>(in its<description>tag; return types and arguments don't take separate
documentation strings)
<method>(in its<description>tag; return types and arguments don't take separate
documentation strings)
- <member>
<member>
- <signal>(in its<description>tag; arguments don't take separate documentation strings)
<signal>(in its<description>tag; arguments don't take separate documentation strings)
- <constant>
<constant>
Write in a clear and simple language. Always follow thewriting guidelinesto keep your descriptions short and easy to read.Do not leave empty linesin the descriptions: each line in the XML file will
result in a new paragraph, even if it is empty.

## How to edit class XML
Edit the file for your chosen class indoc/classes/to update the class
reference. The folder contains an XML file for each class. The XML lists the
constants and methods you will find in the class reference. Godot generates and
updates the XML automatically.
Note
For some modules in the engine's source code, you'll find the XML
files in themodules/<module_name>/doc_classes/directory instead.
Edit it using your favorite text editor. If you use a code editor, make sure
that it doesn't change the indent style: you should use tabs for the XML and
four spaces inside BBCode-style blocks. More on that below.
To check that the modifications you've made are correct in the generated
documentation, navigate to thedoc/folder and run the commandmakerst.
This will convert the XML files to the online documentation's format and output
errors if anything's wrong.
Alternatively, you can build Godot and open the modified page in the built-in
code reference. To learn how to compile the engine, read thecompilation
guide.
We recommend using a code editor that supports XML files like Vim, Atom, Visual Studio Code,
Notepad++, or another to comfortably edit the file. You can also use their
search feature to find classes and properties quickly.
If you use Visual Studio Code, you can install thevscode-xml extensionto get linting for class reference XML files.

### Improve formatting with BBCode style tags
Godot's XML class reference supports BBCode-like tags for linking as well as formatting text and code.
In the tables below you can find the available tags, usage examples and the results after conversion to reStructuredText.

#### Linking
Whenever you link to a member of another class, you need to specify the class name.
For links to the same class, the class name is optional and can be omitted.

| Tag and Description | Example | Result |
|---|---|---|
| [Class]Link to class | Movethe[Sprite2D]. | Move theSprite2D. |
| [annotationClass.name]Link to annotation | See[annotation@GDScript.@rpc]. | See@GDScript.@rpc. |
| [constantClass.name]Link to constant | See[constantColor.RED]. | SeeColor.RED. |
| [enumClass.name]Link to enum | See[enumMesh.ArrayType]. | SeeMesh.ArrayType. |
| [memberClass.name]Link to member | Get[memberNode2D.scale]. | GetNode2D.scale. |
| [methodClass.name]Link to method | Call[methodNode3D.hide]. | CallNode3D.hide(). |
| [constructorClass.name]Link to built-in constructor | Use[constructorColor.Color]. | UseColor.Color. |
| [operatorClass.name]Link to built-in operator | Use[operatorColor.operator*]. | UseColor.operator *. |
| [signalClass.name]Link to signal | Emit[signalNode.renamed]. | EmitNode.renamed. |
| [theme_itemClass.name]Link to theme item | See[theme_itemLabel.font]. | SeeLabel.font. |
| [paramname]Parameter name (as code) | Takes[paramsize]forthesize. | Takessizefor the size. |

Tag and Description
Example
Result
Movethe[Sprite2D].
Move theSprite2D.
See[annotation@GDScript.@rpc].
See@GDScript.@rpc.
See[constantColor.RED].
SeeColor.RED.
See[enumMesh.ArrayType].
SeeMesh.ArrayType.
Get[memberNode2D.scale].
GetNode2D.scale.
Call[methodNode3D.hide].
CallNode3D.hide().
Use[constructorColor.Color].
UseColor.Color.
Use[operatorColor.operator*].
UseColor.operator *.
Emit[signalNode.renamed].
EmitNode.renamed.
See[theme_itemLabel.font].
SeeLabel.font.
Takes[paramsize]forthesize.
Takessizefor the size.
Note
Currently only@GDScripthas annotations.

#### Formatting text

| Tag and Description | Example | Result |
|---|---|---|
| [br]Line break | Line1.[br]Line2. | Line 1.Line 2. |
| [lb][rb][and]respectively | [lb]b[rb]text[lb]/b[rb] | [b]text[/b] |
| [b][/b]Bold | Do[b]not[/b]callthismethod. | Donotcall this method. |
| [i][/i]Italic | Returnsthe[i]global[/i]position. | Returns theglobalposition. |
| [u][/u]Underline | [u]Always[/u]usethismethod. | Alwaysuse this method. |
| [s][/s]Strikethrough | [s]Outdatedinformation.[/s] | Outdated information. |
| [url][/url]Hyperlink | [url]https://example.com[/url][url=https://example.com]Website[/url] | https://example.comWebsite |
| [center][/center]Horizontal centering | [center]2+2=4[/center] | 2 + 2 = 4 |
| [kbd][/kbd]Keyboard/mouse shortcut | Press[kbd]Ctrl+C[/kbd]. | PressCtrl+C. |
| [code][/code]Inline code fragment | Returns[code]true[/code]. | Returnstrue. |

Tag and Description
Example
Result
[lb]b[rb]text[lb]/b[rb]
[b]text[/b]
Do[b]not[/b]callthismethod.
Donotcall this method.
Returnsthe[i]global[/i]position.
Returns theglobalposition.
[u]Always[/u]usethismethod.
[s]Outdatedinformation.[/s]
[center]2+2=4[/center]
Press[kbd]Ctrl+C[/kbd].
PressCtrl+C.
Returns[code]true[/code].
Returnstrue.
Note
- Some supported tags like[color]and[font]are not listed here because they are not recommended in the engine documentation.
Some supported tags like[color]and[font]are not listed here because they are not recommended in the engine documentation.
- [kbd]disables BBCode until the parser encounters[/kbd].
[kbd]disables BBCode until the parser encounters[/kbd].
- [code]disables BBCode until the parser encounters[/code].
[code]disables BBCode until the parser encounters[/code].

#### Formatting code blocks
There are two options for formatting code blocks:
- Use[codeblock]if you want to add an example for a specific language.
Use[codeblock]if you want to add an example for a specific language.
- Use[codeblocks],[gdscript], and[csharp]if you want to add the same example for both languages, GDScript and C#.
Use[codeblocks],[gdscript], and[csharp]if you want to add the same example for both languages, GDScript and C#.
By default,[codeblock]highlights GDScript syntax. You can change it using
thelangattribute. Currently supported options are:
- [codeblocklang=text]disables syntax highlighting;
[codeblocklang=text]disables syntax highlighting;
- [codeblocklang=gdscript]highlights GDScript syntax;
[codeblocklang=gdscript]highlights GDScript syntax;
- [codeblocklang=csharp]highlights C# syntax (only in .NET version).
[codeblocklang=csharp]highlights C# syntax (only in .NET version).
Note
[codeblock]disables BBCode until the parser encounters[/codeblock].
Warning
Use[codeblock]for pre-formatted code blocks. Since Godot 4.5,tabsshould be used for indentation.
For example:
```
[codeblock]
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
[/codeblock]
```
Will display as:
```
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
```
If you need to have different code version in GDScript and C#, use[codeblocks]instead. If you use[codeblocks], you also need to have at
least one of the language-specific tags,[gdscript]and[csharp].
Always write GDScript code examples first! You can use thisexperimental code
translation toolto speed up your
workflow.
```
[codeblocks]
[gdscript]
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
[/gdscript]
[csharp]
public override void _Ready()
{
    var sprite = GetNode("Sprite2D");
    GD.Print(sprite.GetPos());
}
[/csharp]
[/codeblocks]
```
The above will display as:
```
func _ready():
    var sprite = get_node("Sprite2D")
    print(sprite.get_pos())
```
```
public override void _Ready()
{
    var sprite = GetNode("Sprite2D");
    GD.Print(sprite.GetPos());
}
```

#### Formatting notes and warnings
To denote important information, add a paragraph starting with "[b]Note:[/b]" at
the end of the description:
```
[b]Note:[/b] Only available when using the Forward+ renderer.
```
To denote crucial information that could cause security issues or loss of data
if not followed carefully, add a paragraph starting with "[b]Warning:[/b]" at
the end of the description:
```
[b]Warning:[/b] If this property is set to [code]true[/code], it allows clients to execute arbitrary code on the server.
```
In all the paragraphs described above, make sure the punctuation is part of the
BBCode tags for consistency.

### Marking API as deprecated/experimental
To mark an API as deprecated or experimental, you need to add the corresponding XML attribute. The attribute value must be a message
explaining why the API is not recommended (BBCode markup is supported) or an empty string (the default message will be used).
If an API element is marked as deprecated/experimental, then it is considered documented even if the description is empty.
```
<class name="Parallax2D" inherits="Node2D" experimental="This node is meant to replace [ParallaxBackground] and [ParallaxLayer]. The implementation may change in the future." xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="../class.xsd">
    [...]
</class>

<constant name="RESPONSE_USE_PROXY" value="305" enum="ResponseCode" deprecated="Many clients ignore this response code for security reasons. It is also deprecated by the HTTP standard.">
    HTTP status code [code]305 Use Proxy[/code].
</constant>

<member name="auto_translate" type="bool" setter="set_auto_translate" getter="is_auto_translating" deprecated="Use [member Node.auto_translate_mode] instead.">
    Toggles if any text should automatically change to its translated version depending on the current locale.
</member>

<method name="get_method_call_mode" qualifiers="const" deprecated="Use [member AnimationMixer.callback_mode_method] instead.">
    <return type="int" enum="AnimationPlayer.AnimationMethodCallMode" />
    <description>
        Returns the call mode used for "Call Method" tracks.
    </description>
</method>
```

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.