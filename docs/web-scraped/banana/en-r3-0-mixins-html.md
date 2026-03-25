# Source: https://banana.readthedocs.io/en/r3.0/mixins.html

Title: Banana specific Django View Mixins — Banana 2.0 documentation

URL Source: https://banana.readthedocs.io/en/r3.0/mixins.html

Markdown Content:
To fit our specific requirements we created Django View Mixins that extend the default behavior. They are used in various views in the banana app.

The mixins[¶](https://banana.readthedocs.io/en/r3.0/mixins.html#module-banana.views.mixins "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------

_class_`banana.views.mixins.``DatasetMixin`[[source]](https://banana.readthedocs.io/en/r3.0/_modules/banana/views/mixins.html#DatasetMixin)[¶](https://banana.readthedocs.io/en/r3.0/mixins.html#banana.views.mixins.DatasetMixin "Permalink to this definition")
Mixin view that adds the ‘dataset’ request variable to the context.

_class_`banana.views.mixins.``FluxViewMixin`[[source]](https://banana.readthedocs.io/en/r3.0/_modules/banana/views/mixins.html#FluxViewMixin)[¶](https://banana.readthedocs.io/en/r3.0/mixins.html#banana.views.mixins.FluxViewMixin "Permalink to this definition")
Mixin view that adds the ‘flux_prefix’ request variable to the context.

_class_`banana.views.mixins.``HybridTemplateMixin`[[source]](https://banana.readthedocs.io/en/r3.0/_modules/banana/views/mixins.html#HybridTemplateMixin)[¶](https://banana.readthedocs.io/en/r3.0/mixins.html#banana.views.mixins.HybridTemplateMixin "Permalink to this definition")
Assigns a default `template_name`, and checks the request for a format.

If the format specified in the querystring is json or csv, this will change the `content_type` and `template_name` accordingly.

If template name is not explicitly set, we assign one based on the object or model in the view. We derive the template path as:

> <app_label>/<object_name.lower()><template_name_suffix><extension>

where `template_name_suffix` is something like ‘_list’ or ‘_detail’ (inherited from the Django standard class views) e.g.:

> banana/extractedsource_list.html
> 
> 
> banana/extractedsource_detail.html

_class_`banana.views.mixins.``SortListMixin`[[source]](https://banana.readthedocs.io/en/r3.0/_modules/banana/views/mixins.html#SortListMixin)[¶](https://banana.readthedocs.io/en/r3.0/mixins.html#banana.views.mixins.SortListMixin "Permalink to this definition")
View mixin which provides sorting for ListView.

![Image 1](https://server.ethicalads.io/proxy/view/10084/019cdf31-05bf-7f12-a8b4-744c44657a74/)
