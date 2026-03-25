# luigi.mypy

Plugin that provides support for luigi.Task

This Code reuses the code from mypy.plugins.dataclasses
https://github.com/python/mypy/blob/0753e2a82dad35034e000609b6e8daa37238bfaa/mypy/plugins/dataclasses.py

Functions

`plugin`(version)

Classes

`TaskAttribute`(name, has_default, line, ...)

`TaskPlugin`(*args, **kwargs)

`TaskTransformer`(cls, reason, api, task_plugin)

Implement the behavior of gokart.Task.

class luigi.mypy.TaskPlugin(**args: Any*, ***kwargs: Any*)

get_base_class_hook(*fullname: str*) → Callable[[mypy.plugin.ClassDefContext], None] | None

get_function_hook(*fullname: str*) → Callable[[mypy.plugin.FunctionContext], mypy.types.Type] | None

Adjust the return type of the Parameters function.

check_parameter(*fullname*)

class luigi.mypy.TaskAttribute(*name: str*, *has_default: bool*, *line: int*, *column: int*, *type: Type | None*, *info: TypeInfo*, *api: SemanticAnalyzerPluginInterface*)

to_argument(*current_info: mypy.nodes.TypeInfo*, ***, *of: Literal['__init__']*) → mypy.nodes.Argument

expand_type(*current_info: TypeInfo*) → Type | None

to_var(*current_info: mypy.nodes.TypeInfo*) → mypy.nodes.Var

serialize() → mypy.nodes.JsonDict

classmethod deserialize(*info: mypy.nodes.TypeInfo*, *data: mypy.nodes.JsonDict*, *api: mypy.plugin.SemanticAnalyzerPluginInterface*) → TaskAttribute

expand_typevar_from_subtype(*sub_type: mypy.nodes.TypeInfo*) → None

Expands type vars in the context of a subtype when an attribute is inherited
from a generic super type.

class luigi.mypy.TaskTransformer(*cls: ClassDef*, *reason: Expression | Statement*, *api: SemanticAnalyzerPluginInterface*, *task_plugin: TaskPlugin*)

Implement the behavior of gokart.Task.

transform() → bool

Apply all the necessary transformations to the underlying gokart.Task

collect_attributes() → List[TaskAttribute] | None

Collect all attributes declared in the task and its parents.

All assignments of the form

a: SomeType
b: SomeOtherType = …