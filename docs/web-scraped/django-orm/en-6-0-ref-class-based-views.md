# Source: https://docs.djangoproject.com/en/6.0/ref/class-based-views/

Title: Built-in class-based views API | Django documentation

URL Source: https://docs.djangoproject.com/en/6.0/ref/class-based-views/

Markdown Content:
Class-based views API reference. For introductory material, see the [Class-based views](https://docs.djangoproject.com/en/6.0/topics/class-based-views/) topic guide.

*   [Base views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/)
    *   [`View`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#view)
    *   [`TemplateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#templateview)
    *   [`RedirectView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#redirectview)

*   [Generic display views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/)
    *   [`DetailView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/#detailview)
    *   [`ListView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-display/#listview)

*   [Generic editing views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-editing/)
    *   [`FormView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-editing/#formview)
    *   [`CreateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-editing/#createview)
    *   [`UpdateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-editing/#updateview)
    *   [`DeleteView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-editing/#deleteview)

*   [Generic date views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/)
    *   [`ArchiveIndexView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#archiveindexview)
    *   [`YearArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#yeararchiveview)
    *   [`MonthArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#montharchiveview)
    *   [`WeekArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#weekarchiveview)
    *   [`DayArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#dayarchiveview)
    *   [`TodayArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#todayarchiveview)
    *   [`DateDetailView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/generic-date-based/#datedetailview)

*   [Class-based views mixins](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins/)
    *   [Simple mixins](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/)
        *   [`ContextMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#contextmixin)
        *   [`TemplateResponseMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-simple/#templateresponsemixin)

    *   [Single object mixins](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/)
        *   [`SingleObjectMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#singleobjectmixin)
        *   [`SingleObjectTemplateResponseMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-single-object/#singleobjecttemplateresponsemixin)

    *   [Multiple object mixins](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/)
        *   [`MultipleObjectMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#multipleobjectmixin)
        *   [`MultipleObjectTemplateResponseMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-multiple-object/#multipleobjecttemplateresponsemixin)

    *   [Editing mixins](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/)
        *   [`FormMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#formmixin)
        *   [`ModelFormMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#modelformmixin)
        *   [`ProcessFormView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#processformview)
        *   [`DeletionMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-editing/#deletionmixin)

    *   [Date-based mixins](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/)
        *   [`YearMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#yearmixin)
        *   [`MonthMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#monthmixin)
        *   [`DayMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#daymixin)
        *   [`WeekMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#weekmixin)
        *   [`DateMixin`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#datemixin)
        *   [`BaseDateListView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/mixins-date-based/#basedatelistview)

*   [Class-based generic views - flattened index](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/)
    *   [Simple generic views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#simple-generic-views)
        *   [`View`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#view)
        *   [`TemplateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#templateview)
        *   [`RedirectView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#redirectview)

    *   [Detail Views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#detail-views)
        *   [`DetailView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#detailview)

    *   [List Views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#list-views)
        *   [`ListView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#listview)

    *   [Editing views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#editing-views)
        *   [`FormView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#formview)
        *   [`CreateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#createview)
        *   [`UpdateView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#updateview)
        *   [`DeleteView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#deleteview)

    *   [Date-based views](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#date-based-views)
        *   [`ArchiveIndexView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#archiveindexview)
        *   [`YearArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#yeararchiveview)
        *   [`MonthArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#montharchiveview)
        *   [`WeekArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#weekarchiveview)
        *   [`DayArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#dayarchiveview)
        *   [`TodayArchiveView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#todayarchiveview)
        *   [`DateDetailView`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/flattened-index/#datedetailview)

Specification[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/#specification "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Each request served by a class-based view has an independent state; therefore, it is safe to store state variables on the instance (i.e., `self.foo = 3` is a thread-safe operation).

A class-based view is deployed into a URL pattern using the [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") classmethod:

urlpatterns = [
    path("view/", MyView.as_view(size=42)),
]

Thread safety with view arguments

Arguments passed to a view are shared between every instance of a view. This means that you shouldn’t use a list, dictionary, or any other mutable object as an argument to a view. If you do and the shared object is modified, the actions of one user visiting your view could have an effect on subsequent users visiting the same view.

Arguments passed into [`as_view()`](https://docs.djangoproject.com/en/6.0/ref/class-based-views/base/#django.views.generic.base.View.as_view "django.views.generic.base.View.as_view") will be assigned onto the instance that is used to service a request. Using the previous example, this means that every request on `MyView` is able to use `self.size`. Arguments must correspond to attributes that already exist on the class (return `True` on a `hasattr` check).

Base vs Generic views[¶](https://docs.djangoproject.com/en/6.0/ref/class-based-views/#base-vs-generic-views "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

Base class-based views can be thought of as _parent_ views, which can be used by themselves or inherited from. They may not provide all the capabilities required for projects, in which case there are Mixins which extend what base views can do.

Django’s generic views are built off of those base views, and were developed as a shortcut for common usage patterns such as displaying the details of an object. They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to repeat yourself.

Most generic views require the `queryset` key, which is a `QuerySet` instance; see [Making queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/) for more information about `QuerySet` objects.
