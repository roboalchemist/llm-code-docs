# Source: https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/

Title: Class-based generic views - flattened index | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/

Markdown Content:
This index provides an alternate organization of the reference documentation for class-based views. For each view, the effective attributes and methods from the class tree are represented under that view. For the reference documentation organized by the class which defines the behavior, see [Class-based views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/).

See also

[Classy Class-Based Views](https://ccbv.co.uk/) provides a nice interface to navigate the class hierarchy of the built-in class-based views.

Simple generic views[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#simple-generic-views "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

### `View`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#view "Link to this heading")

_class_ View[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#View "Link to this definition")
**Attributes** (with optional accessor):

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `TemplateView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#templateview "Link to this heading")

_class_ TemplateView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#TemplateView "Link to this definition")
**Attributes** (with optional accessor):

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.get_context_data "django.views.generic.base.ContextMixin.get_context_data")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `RedirectView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#redirectview "Link to this heading")

_class_ RedirectView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#RedirectView "Link to this definition")
**Attributes** (with optional accessor):

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`pattern_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.RedirectView.pattern_name "django.views.generic.base.RedirectView.pattern_name")

*   [`permanent`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.RedirectView.permanent "django.views.generic.base.RedirectView.permanent")

*   [`query_string`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.RedirectView.query_string "django.views.generic.base.RedirectView.query_string")

*   [`url`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.RedirectView.url "django.views.generic.base.RedirectView.url") [[`get_redirect_url()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.RedirectView.get_redirect_url "django.views.generic.base.RedirectView.get_redirect_url")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   `delete()`

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   `options()`

*   `post()`

*   `put()`

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

Detail Views[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#detail-views "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

### `DetailView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#detailview "Link to this heading")

_class_ DetailView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#DetailView "Link to this definition")
**Attributes** (with optional accessor):

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.context_object_name "django.views.generic.detail.SingleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_object_name "django.views.generic.detail.SingleObjectMixin.get_context_object_name")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.model "django.views.generic.detail.SingleObjectMixin.model")

*   [`pk_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.pk_url_kwarg "django.views.generic.detail.SingleObjectMixin.pk_url_kwarg")

*   [`query_pk_and_slug`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.query_pk_and_slug "django.views.generic.detail.SingleObjectMixin.query_pk_and_slug")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset "django.views.generic.detail.SingleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_queryset "django.views.generic.detail.SingleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`slug_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_field "django.views.generic.detail.SingleObjectMixin.slug_field") [[`get_slug_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_slug_field "django.views.generic.detail.SingleObjectMixin.get_slug_field")]

*   [`slug_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_url_kwarg "django.views.generic.detail.SingleObjectMixin.slug_url_kwarg")

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field")

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   [`get()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/#django.views.generic.detail.BaseDetailView.get "django.views.generic.detail.BaseDetailView.get")

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data "django.views.generic.detail.SingleObjectMixin.get_context_data")

*   [`get_object()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

List Views[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#list-views "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

### `ListView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#listview "Link to this heading")

_class_ ListView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#ListView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   [`get()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/#django.views.generic.list.BaseListView.get "django.views.generic.list.BaseListView.get")

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

Editing views[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#editing-views "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

### `FormView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#formview "Link to this heading")

_class_ FormView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#FormView "Link to this definition")
**Attributes** (with optional accessor):

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`form_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class "django.views.generic.edit.FormMixin.form_class") [[`get_form_class()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form_class "django.views.generic.edit.FormMixin.get_form_class")]

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`initial`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.initial "django.views.generic.edit.FormMixin.initial") [[`get_initial()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_initial "django.views.generic.edit.FormMixin.get_initial")]

*   [`prefix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.prefix "django.views.generic.edit.FormMixin.prefix") [[`get_prefix()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_prefix "django.views.generic.edit.FormMixin.get_prefix")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`success_url`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.success_url "django.views.generic.edit.FormMixin.success_url") [[`get_success_url()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_success_url "django.views.generic.edit.FormMixin.get_success_url")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   [`form_invalid()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_invalid "django.views.generic.edit.FormMixin.form_invalid")

*   [`form_valid()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_valid "django.views.generic.edit.FormMixin.form_valid")

*   [`get()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.get "django.views.generic.edit.ProcessFormView.get")

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_context_data "django.views.generic.edit.FormMixin.get_context_data")

*   [`get_form()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form "django.views.generic.edit.FormMixin.get_form")

*   [`get_form_kwargs()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form_kwargs "django.views.generic.edit.FormMixin.get_form_kwargs")

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`post()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.post "django.views.generic.edit.ProcessFormView.post")

*   [`put()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.put "django.views.generic.edit.ProcessFormView.put")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `CreateView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#createview "Link to this heading")

_class_ CreateView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#CreateView "Link to this definition")
**Attributes** (with optional accessor):

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.context_object_name "django.views.generic.detail.SingleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_object_name "django.views.generic.detail.SingleObjectMixin.get_context_object_name")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`fields`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.fields "django.views.generic.edit.ModelFormMixin.fields")

*   [`form_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class "django.views.generic.edit.FormMixin.form_class") [[`get_form_class()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.get_form_class "django.views.generic.edit.ModelFormMixin.get_form_class")]

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`initial`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.initial "django.views.generic.edit.FormMixin.initial") [[`get_initial()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_initial "django.views.generic.edit.FormMixin.get_initial")]

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.model "django.views.generic.detail.SingleObjectMixin.model")

*   [`pk_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.pk_url_kwarg "django.views.generic.detail.SingleObjectMixin.pk_url_kwarg")

*   [`prefix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.prefix "django.views.generic.edit.FormMixin.prefix") [[`get_prefix()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_prefix "django.views.generic.edit.FormMixin.get_prefix")]

*   [`query_pk_and_slug`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.query_pk_and_slug "django.views.generic.detail.SingleObjectMixin.query_pk_and_slug")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset "django.views.generic.detail.SingleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_queryset "django.views.generic.detail.SingleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`slug_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_field "django.views.generic.detail.SingleObjectMixin.slug_field") [[`get_slug_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_slug_field "django.views.generic.detail.SingleObjectMixin.get_slug_field")]

*   [`slug_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_url_kwarg "django.views.generic.detail.SingleObjectMixin.slug_url_kwarg")

*   [`success_url`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.success_url "django.views.generic.edit.FormMixin.success_url") [[`get_success_url()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.get_success_url "django.views.generic.edit.ModelFormMixin.get_success_url")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field")

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   [`form_invalid()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_invalid "django.views.generic.edit.FormMixin.form_invalid")

*   [`form_valid()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid "django.views.generic.edit.ModelFormMixin.form_valid")

*   [`get()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.get "django.views.generic.edit.ProcessFormView.get")

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_context_data "django.views.generic.edit.FormMixin.get_context_data")

*   [`get_form()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form "django.views.generic.edit.FormMixin.get_form")

*   [`get_form_kwargs()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.get_form_kwargs "django.views.generic.edit.ModelFormMixin.get_form_kwargs")

*   [`get_object()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`post()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.post "django.views.generic.edit.ProcessFormView.post")

*   `put()`

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `UpdateView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#updateview "Link to this heading")

_class_ UpdateView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#UpdateView "Link to this definition")
**Attributes** (with optional accessor):

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.context_object_name "django.views.generic.detail.SingleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_object_name "django.views.generic.detail.SingleObjectMixin.get_context_object_name")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`fields`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.fields "django.views.generic.edit.ModelFormMixin.fields")

*   [`form_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_class "django.views.generic.edit.FormMixin.form_class") [[`get_form_class()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.get_form_class "django.views.generic.edit.ModelFormMixin.get_form_class")]

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`initial`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.initial "django.views.generic.edit.FormMixin.initial") [[`get_initial()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_initial "django.views.generic.edit.FormMixin.get_initial")]

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.model "django.views.generic.detail.SingleObjectMixin.model")

*   [`pk_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.pk_url_kwarg "django.views.generic.detail.SingleObjectMixin.pk_url_kwarg")

*   [`prefix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.prefix "django.views.generic.edit.FormMixin.prefix") [[`get_prefix()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_prefix "django.views.generic.edit.FormMixin.get_prefix")]

*   [`query_pk_and_slug`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.query_pk_and_slug "django.views.generic.detail.SingleObjectMixin.query_pk_and_slug")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset "django.views.generic.detail.SingleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_queryset "django.views.generic.detail.SingleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`slug_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_field "django.views.generic.detail.SingleObjectMixin.slug_field") [[`get_slug_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_slug_field "django.views.generic.detail.SingleObjectMixin.get_slug_field")]

*   [`slug_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_url_kwarg "django.views.generic.detail.SingleObjectMixin.slug_url_kwarg")

*   [`success_url`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.success_url "django.views.generic.edit.FormMixin.success_url") [[`get_success_url()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.get_success_url "django.views.generic.edit.ModelFormMixin.get_success_url")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field")

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   [`form_invalid()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.form_invalid "django.views.generic.edit.FormMixin.form_invalid")

*   [`form_valid()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.form_valid "django.views.generic.edit.ModelFormMixin.form_valid")

*   [`get()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.get "django.views.generic.edit.ProcessFormView.get")

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_context_data "django.views.generic.edit.FormMixin.get_context_data")

*   [`get_form()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.FormMixin.get_form "django.views.generic.edit.FormMixin.get_form")

*   [`get_form_kwargs()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ModelFormMixin.get_form_kwargs "django.views.generic.edit.ModelFormMixin.get_form_kwargs")

*   [`get_object()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`post()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.ProcessFormView.post "django.views.generic.edit.ProcessFormView.post")

*   `put()`

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `DeleteView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#deleteview "Link to this heading")

_class_ DeleteView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#DeleteView "Link to this definition")
**Attributes** (with optional accessor):

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.context_object_name "django.views.generic.detail.SingleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_object_name "django.views.generic.detail.SingleObjectMixin.get_context_object_name")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.model "django.views.generic.detail.SingleObjectMixin.model")

*   [`pk_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.pk_url_kwarg "django.views.generic.detail.SingleObjectMixin.pk_url_kwarg")

*   [`query_pk_and_slug`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.query_pk_and_slug "django.views.generic.detail.SingleObjectMixin.query_pk_and_slug")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset "django.views.generic.detail.SingleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_queryset "django.views.generic.detail.SingleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`slug_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_field "django.views.generic.detail.SingleObjectMixin.slug_field") [[`get_slug_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_slug_field "django.views.generic.detail.SingleObjectMixin.get_slug_field")]

*   [`slug_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_url_kwarg "django.views.generic.detail.SingleObjectMixin.slug_url_kwarg")

*   [`success_url`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.DeletionMixin.success_url "django.views.generic.edit.DeletionMixin.success_url") [[`get_success_url()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#django.views.generic.edit.DeletionMixin.get_success_url "django.views.generic.edit.DeletionMixin.get_success_url")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field")

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   `delete()`

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data "django.views.generic.detail.SingleObjectMixin.get_context_data")

*   [`get_object()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   `post()`

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

Date-based views[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#date-based-views "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

### `ArchiveIndexView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#archiveindexview "Link to this heading")

_class_ ArchiveIndexView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#ArchiveIndexView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_date_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_date_list "django.views.generic.dates.BaseDateListView.get_date_list")

*   [`get_dated_items()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_items "django.views.generic.dates.BaseDateListView.get_dated_items")

*   [`get_dated_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_queryset "django.views.generic.dates.BaseDateListView.get_dated_queryset")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `YearArchiveView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#yeararchiveview "Link to this heading")

_class_ YearArchiveView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#YearArchiveView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`make_object_list`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#django.views.generic.dates.YearArchiveView.make_object_list "django.views.generic.dates.YearArchiveView.make_object_list") [[`get_make_object_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#django.views.generic.dates.YearArchiveView.get_make_object_list "django.views.generic.dates.YearArchiveView.get_make_object_list")]

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

*   [`year`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year "django.views.generic.dates.YearMixin.year") [[`get_year()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year "django.views.generic.dates.YearMixin.get_year")]

*   [`year_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year_format "django.views.generic.dates.YearMixin.year_format") [[`get_year_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year_format "django.views.generic.dates.YearMixin.get_year_format")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_date_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_date_list "django.views.generic.dates.BaseDateListView.get_date_list")

*   [`get_dated_items()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_items "django.views.generic.dates.BaseDateListView.get_dated_items")

*   [`get_dated_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_queryset "django.views.generic.dates.BaseDateListView.get_dated_queryset")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `MonthArchiveView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#montharchiveview "Link to this heading")

_class_ MonthArchiveView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#MonthArchiveView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`month`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month "django.views.generic.dates.MonthMixin.month") [[`get_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month "django.views.generic.dates.MonthMixin.get_month")]

*   [`month_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month_format "django.views.generic.dates.MonthMixin.month_format") [[`get_month_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month_format "django.views.generic.dates.MonthMixin.get_month_format")]

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

*   [`year`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year "django.views.generic.dates.YearMixin.year") [[`get_year()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year "django.views.generic.dates.YearMixin.get_year")]

*   [`year_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year_format "django.views.generic.dates.YearMixin.year_format") [[`get_year_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year_format "django.views.generic.dates.YearMixin.get_year_format")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_date_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_date_list "django.views.generic.dates.BaseDateListView.get_date_list")

*   [`get_dated_items()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_items "django.views.generic.dates.BaseDateListView.get_dated_items")

*   [`get_dated_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_queryset "django.views.generic.dates.BaseDateListView.get_dated_queryset")

*   [`get_next_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_next_month "django.views.generic.dates.MonthMixin.get_next_month")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   [`get_previous_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_previous_month "django.views.generic.dates.MonthMixin.get_previous_month")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `WeekArchiveView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#weekarchiveview "Link to this heading")

_class_ WeekArchiveView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#WeekArchiveView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

*   [`week`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.WeekMixin.week "django.views.generic.dates.WeekMixin.week") [[`get_week()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.WeekMixin.get_week "django.views.generic.dates.WeekMixin.get_week")]

*   [`week_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.WeekMixin.week_format "django.views.generic.dates.WeekMixin.week_format") [[`get_week_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.WeekMixin.get_week_format "django.views.generic.dates.WeekMixin.get_week_format")]

*   [`year`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year "django.views.generic.dates.YearMixin.year") [[`get_year()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year "django.views.generic.dates.YearMixin.get_year")]

*   [`year_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year_format "django.views.generic.dates.YearMixin.year_format") [[`get_year_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year_format "django.views.generic.dates.YearMixin.get_year_format")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_date_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_date_list "django.views.generic.dates.BaseDateListView.get_date_list")

*   [`get_dated_items()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_items "django.views.generic.dates.BaseDateListView.get_dated_items")

*   [`get_dated_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_queryset "django.views.generic.dates.BaseDateListView.get_dated_queryset")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `DayArchiveView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#dayarchiveview "Link to this heading")

_class_ DayArchiveView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#DayArchiveView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`day`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.day "django.views.generic.dates.DayMixin.day") [[`get_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_day "django.views.generic.dates.DayMixin.get_day")]

*   [`day_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.day_format "django.views.generic.dates.DayMixin.day_format") [[`get_day_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_day_format "django.views.generic.dates.DayMixin.get_day_format")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`month`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month "django.views.generic.dates.MonthMixin.month") [[`get_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month "django.views.generic.dates.MonthMixin.get_month")]

*   [`month_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month_format "django.views.generic.dates.MonthMixin.month_format") [[`get_month_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month_format "django.views.generic.dates.MonthMixin.get_month_format")]

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

*   [`year`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year "django.views.generic.dates.YearMixin.year") [[`get_year()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year "django.views.generic.dates.YearMixin.get_year")]

*   [`year_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year_format "django.views.generic.dates.YearMixin.year_format") [[`get_year_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year_format "django.views.generic.dates.YearMixin.get_year_format")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_date_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_date_list "django.views.generic.dates.BaseDateListView.get_date_list")

*   [`get_dated_items()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_items "django.views.generic.dates.BaseDateListView.get_dated_items")

*   [`get_dated_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_queryset "django.views.generic.dates.BaseDateListView.get_dated_queryset")

*   [`get_next_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_next_day "django.views.generic.dates.DayMixin.get_next_day")

*   [`get_next_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_next_month "django.views.generic.dates.MonthMixin.get_next_month")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   [`get_previous_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_previous_day "django.views.generic.dates.DayMixin.get_previous_day")

*   [`get_previous_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_previous_month "django.views.generic.dates.MonthMixin.get_previous_month")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `TodayArchiveView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#todayarchiveview "Link to this heading")

_class_ TodayArchiveView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#TodayArchiveView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_empty`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.allow_empty "django.views.generic.list.MultipleObjectMixin.allow_empty") [[`get_allow_empty()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_allow_empty "django.views.generic.list.MultipleObjectMixin.get_allow_empty")]

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.context_object_name "django.views.generic.list.MultipleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_object_name "django.views.generic.list.MultipleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`day`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.day "django.views.generic.dates.DayMixin.day") [[`get_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_day "django.views.generic.dates.DayMixin.get_day")]

*   [`day_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.day_format "django.views.generic.dates.DayMixin.day_format") [[`get_day_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_day_format "django.views.generic.dates.DayMixin.get_day_format")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.model "django.views.generic.list.MultipleObjectMixin.model")

*   [`month`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month "django.views.generic.dates.MonthMixin.month") [[`get_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month "django.views.generic.dates.MonthMixin.get_month")]

*   [`month_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month_format "django.views.generic.dates.MonthMixin.month_format") [[`get_month_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month_format "django.views.generic.dates.MonthMixin.get_month_format")]

*   [`ordering`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.ordering "django.views.generic.list.MultipleObjectMixin.ordering") [[`get_ordering()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_ordering "django.views.generic.list.MultipleObjectMixin.get_ordering")]

*   [`paginate_by`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_by "django.views.generic.list.MultipleObjectMixin.paginate_by") [[`get_paginate_by()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_by "django.views.generic.list.MultipleObjectMixin.get_paginate_by")]

*   [`paginate_orphans`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_orphans "django.views.generic.list.MultipleObjectMixin.paginate_orphans") [[`get_paginate_orphans()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginate_orphans "django.views.generic.list.MultipleObjectMixin.get_paginate_orphans")]

*   [`paginator_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginator_class "django.views.generic.list.MultipleObjectMixin.paginator_class")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.queryset "django.views.generic.list.MultipleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_queryset "django.views.generic.list.MultipleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.list.MultipleObjectTemplateResponseMixin.template_name_suffix")

*   [`year`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year "django.views.generic.dates.YearMixin.year") [[`get_year()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year "django.views.generic.dates.YearMixin.get_year")]

*   [`year_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year_format "django.views.generic.dates.YearMixin.year_format") [[`get_year_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year_format "django.views.generic.dates.YearMixin.get_year_format")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data "django.views.generic.list.MultipleObjectMixin.get_context_data")

*   [`get_date_list()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_date_list "django.views.generic.dates.BaseDateListView.get_date_list")

*   [`get_dated_items()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_items "django.views.generic.dates.BaseDateListView.get_dated_items")

*   [`get_dated_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.BaseDateListView.get_dated_queryset "django.views.generic.dates.BaseDateListView.get_dated_queryset")

*   [`get_next_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_next_day "django.views.generic.dates.DayMixin.get_next_day")

*   [`get_next_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_next_month "django.views.generic.dates.MonthMixin.get_next_month")

*   [`get_paginator()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_paginator "django.views.generic.list.MultipleObjectMixin.get_paginator")

*   [`get_previous_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_previous_day "django.views.generic.dates.DayMixin.get_previous_day")

*   [`get_previous_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_previous_month "django.views.generic.dates.MonthMixin.get_previous_month")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`paginate_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.paginate_queryset "django.views.generic.list.MultipleObjectMixin.paginate_queryset")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")

### `DateDetailView`[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#datedetailview "Link to this heading")

_class_ DateDetailView[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#DateDetailView "Link to this definition")
**Attributes** (with optional accessor):

*   [`allow_future`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.allow_future "django.views.generic.dates.DateMixin.allow_future") [[`get_allow_future()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_allow_future "django.views.generic.dates.DateMixin.get_allow_future")]

*   [`content_type`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.content_type "django.views.generic.base.TemplateResponseMixin.content_type")

*   [`context_object_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.context_object_name "django.views.generic.detail.SingleObjectMixin.context_object_name") [[`get_context_object_name()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_object_name "django.views.generic.detail.SingleObjectMixin.get_context_object_name")]

*   [`date_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.date_field "django.views.generic.dates.DateMixin.date_field") [[`get_date_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DateMixin.get_date_field "django.views.generic.dates.DateMixin.get_date_field")]

*   [`day`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.day "django.views.generic.dates.DayMixin.day") [[`get_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_day "django.views.generic.dates.DayMixin.get_day")]

*   [`day_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.day_format "django.views.generic.dates.DayMixin.day_format") [[`get_day_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_day_format "django.views.generic.dates.DayMixin.get_day_format")]

*   [`extra_context`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.ContextMixin.extra_context "django.views.generic.base.ContextMixin.extra_context")

*   [`http_method_names`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_names "django.views.generic.base.View.http_method_names")

*   [`model`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.model "django.views.generic.detail.SingleObjectMixin.model")

*   [`month`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month "django.views.generic.dates.MonthMixin.month") [[`get_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month "django.views.generic.dates.MonthMixin.get_month")]

*   [`month_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.month_format "django.views.generic.dates.MonthMixin.month_format") [[`get_month_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_month_format "django.views.generic.dates.MonthMixin.get_month_format")]

*   [`pk_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.pk_url_kwarg "django.views.generic.detail.SingleObjectMixin.pk_url_kwarg")

*   [`query_pk_and_slug`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.query_pk_and_slug "django.views.generic.detail.SingleObjectMixin.query_pk_and_slug")

*   [`queryset`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset "django.views.generic.detail.SingleObjectMixin.queryset") [[`get_queryset()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_queryset "django.views.generic.detail.SingleObjectMixin.get_queryset")]

*   [`response_class`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.response_class "django.views.generic.base.TemplateResponseMixin.response_class") [[`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")]

*   [`slug_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_field "django.views.generic.detail.SingleObjectMixin.slug_field") [[`get_slug_field()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_slug_field "django.views.generic.detail.SingleObjectMixin.get_slug_field")]

*   [`slug_url_kwarg`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.slug_url_kwarg "django.views.generic.detail.SingleObjectMixin.slug_url_kwarg")

*   [`template_engine`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_engine "django.views.generic.base.TemplateResponseMixin.template_engine")

*   [`template_name`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.template_name "django.views.generic.base.TemplateResponseMixin.template_name") [[`get_template_names()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.get_template_names "django.views.generic.base.TemplateResponseMixin.get_template_names")]

*   [`template_name_field`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_field")

*   [`template_name_suffix`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix "django.views.generic.detail.SingleObjectTemplateResponseMixin.template_name_suffix")

*   [`year`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year "django.views.generic.dates.YearMixin.year") [[`get_year()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year "django.views.generic.dates.YearMixin.get_year")]

*   [`year_format`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.year_format "django.views.generic.dates.YearMixin.year_format") [[`get_year_format()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.YearMixin.get_year_format "django.views.generic.dates.YearMixin.get_year_format")]

**Methods**

*   [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view")

*   [`dispatch()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch "django.views.generic.base.View.dispatch")

*   `get()`

*   [`get_context_data()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_context_data "django.views.generic.detail.SingleObjectMixin.get_context_data")

*   [`get_next_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_next_day "django.views.generic.dates.DayMixin.get_next_day")

*   [`get_next_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_next_month "django.views.generic.dates.MonthMixin.get_next_month")

*   [`get_object()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.get_object "django.views.generic.detail.SingleObjectMixin.get_object")

*   [`get_previous_day()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.DayMixin.get_previous_day "django.views.generic.dates.DayMixin.get_previous_day")

*   [`get_previous_month()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#django.views.generic.dates.MonthMixin.get_previous_month "django.views.generic.dates.MonthMixin.get_previous_month")

*   `head()`

*   [`http_method_not_allowed()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.http_method_not_allowed "django.views.generic.base.View.http_method_not_allowed")

*   [`render_to_response()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#django.views.generic.base.TemplateResponseMixin.render_to_response "django.views.generic.base.TemplateResponseMixin.render_to_response")

*   [`setup()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.setup "django.views.generic.base.View.setup")
