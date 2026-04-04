:github_url: hide



# Tweener

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [CallbackTweener<class_CallbackTweener>], [IntervalTweener<class_IntervalTweener>], [MethodTweener<class_MethodTweener>], [PropertyTweener<class_PropertyTweener>], [SubtweenTweener<class_SubtweenTweener>]

Abstract class for all Tweeners used by [Tween<class_Tween>].


## Description

Tweeners are objects that perform a specific animating task, e.g. interpolating a property or calling a method at a given time. A **Tweener** can't be created manually, you need to use a dedicated method from [Tween<class_Tween>].


----


## Signals



**finished**\ (\ ) [🔗<class_Tweener_signal_finished>]

Emitted when the **Tweener** has just finished its job or became invalid (e.g. due to a freed object).

