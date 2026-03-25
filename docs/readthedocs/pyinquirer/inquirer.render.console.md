# inquirer.render.console package

## Submodules

## inquirer.render.console.base module

*class *inquirer.render.console.base.BaseConsoleRender(*question*, *theme=None*, *terminal=None*, *show_default=False*, **args*, ***kwargs*)

Bases: `object`

get_current_value()

get_header()

get_options()

handle_validation_error(*error*)

process_input(*pressed*)

title_inline* = False*

## Module contents

*class *inquirer.render.console.ConsoleRender(*event_generator=None*, *theme=None*, **args*, ***kwargs*)

Bases: `object`

clear_bottombar()

clear_eos()

*property *height

print_line(*base*, *lf=True*, ***kwargs*)

print_str(*base*, *lf=False*, ***kwargs*)

render(*question*, *answers=None*)

render_error(*message*)

render_factory(*question_type*)

render_in_bottombar(*message*)

*property *width