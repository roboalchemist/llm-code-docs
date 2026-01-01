{{ fullname \| escape \| underline }}

::: currentmodule
{{ module }}
:::

{% if objtype in \[\'class\'\] %}

{% else %} .. auto{{ objtype }}:: {{ objname }}

{% endif %}

{% if objtype in \[\'class\', \'method\', \'function\'\] %} {% if
objname in \[\'AxesGrid\', \'Scalable\', \'HostAxes\', \'FloatingAxes\',
\'ParasiteAxesAuxTrans\', \'ParasiteAxes\'\] %}

{% else %}

::: {.minigallery add-heading=""}
{{module}}.{{objname}}
:::

{% endif %} {% endif %}
