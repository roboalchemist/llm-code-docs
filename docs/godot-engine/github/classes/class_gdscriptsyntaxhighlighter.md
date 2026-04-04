:github_url: hide



# GDScriptSyntaxHighlighter

**Inherits:** [EditorSyntaxHighlighter<class_EditorSyntaxHighlighter>] **<** [SyntaxHighlighter<class_SyntaxHighlighter>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A GDScript syntax highlighter that can be used with [TextEdit<class_TextEdit>] and [CodeEdit<class_CodeEdit>] nodes.


## Description

**Note:** This class can only be used for editor plugins because it relies on editor settings.


> **TABS**
>

    var code_preview = TextEdit.new()
    var highlighter = GDScriptSyntaxHighlighter.new()
    code_preview.syntax_highlighter = highlighter


    var codePreview = new TextEdit();
    var highlighter = new GDScriptSyntaxHighlighter();
    codePreview.SyntaxHighlighter = highlighter;



