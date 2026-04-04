:github_url: hide



# Expression

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A class that stores an expression you can execute.


## Description

An expression can be made of any arithmetic operation, built-in math function call, method call of a passed instance, or built-in type construction call.

An example expression text using the built-in math functions could be `sqrt(pow(3, 2) + pow(4, 2))`.

In the following example we use a [LineEdit<class_LineEdit>] node to write our expression and show the result.


> **TABS**
>

    var expression = Expression.new()

    func _ready():
        $LineEdit.text_submitted.connect(self._on_text_submitted)

    func _on_text_submitted(command):
        var error = expression.parse(command)
        if error != OK:
            print(expression.get_error_text())
            return
        var result = expression.execute()
        if not expression.has_execute_failed():
            $LineEdit.text = str(result)


    private Expression _expression = new Expression();

    public override void _Ready()
    {
        GetNode<LineEdit>("LineEdit").TextSubmitted += OnTextEntered;
    }

    private void OnTextEntered(string command)
    {
        Error error = _expression.Parse(command);
        if (error != Error.Ok)
        {
            GD.Print(_expression.GetErrorText());
            return;
        }
        Variant result = _expression.Execute();
        if (!_expression.HasExecuteFailed())
        {
            GetNode<LineEdit>("LineEdit").Text = result.ToString();
## }




## Tutorials

- [../tutorials/scripting/evaluating_expressions](Evaluating Expressions .md)


## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`         | :ref:`execute<class_Expression_method_execute>`\ (\ inputs\: :ref:`Array<class_Array>` = [], base_instance\: :ref:`Object<class_Object>` = null, show_error\: :ref:`bool<class_bool>` = true, const_calls_only\: :ref:`bool<class_bool>` = false\ ) |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_error_text<class_Expression_method_get_error_text>`\ (\ ) |const|                                                                                                                                                                         |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`               | :ref:`has_execute_failed<class_Expression_method_has_execute_failed>`\ (\ ) |const|                                                                                                                                                                 |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`parse<class_Expression_method_parse>`\ (\ expression\: :ref:`String<class_String>`, input_names\: :ref:`PackedStringArray<class_PackedStringArray>` = PackedStringArray()\ )                                                                  |
> +---------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Variant<class_Variant>] **execute**\ (\ inputs\: [Array<class_Array>] = [], base_instance\: [Object<class_Object>] = null, show_error\: [bool<class_bool>] = true, const_calls_only\: [bool<class_bool>] = false\ ) [🔗<class_Expression_method_execute>]

Executes the expression that was previously parsed by [parse()<class_Expression_method_parse>] and returns the result. Before you use the returned object, you should check if the method failed by calling [has_execute_failed()<class_Expression_method_has_execute_failed>].

If you defined input variables in [parse()<class_Expression_method_parse>], you can specify their values in the inputs array, in the same order.


----



[String<class_String>] **get_error_text**\ (\ ) |const| [🔗<class_Expression_method_get_error_text>]

Returns the error text if [parse()<class_Expression_method_parse>] or [execute()<class_Expression_method_execute>] has failed.


----



[bool<class_bool>] **has_execute_failed**\ (\ ) |const| [🔗<class_Expression_method_has_execute_failed>]

Returns `true` if [execute()<class_Expression_method_execute>] has failed.


----



[Error<enum_@GlobalScope_Error>] **parse**\ (\ expression\: [String<class_String>], input_names\: [PackedStringArray<class_PackedStringArray>] = PackedStringArray()\ ) [🔗<class_Expression_method_parse>]

Parses the expression and returns an [Error<enum_@GlobalScope_Error>] code.

You can optionally specify names of variables that may appear in the expression with `input_names`, so that you can bind them when it gets executed.

