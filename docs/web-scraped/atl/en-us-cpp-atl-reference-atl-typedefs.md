# Source: https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170

Title: ATL Typedefs

URL Source: https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170

Markdown Content:
Note

The Active Template Library (ATL) continues to be supported. However, we're no longer adding features or updating the documentation.

The Active Template Library includes the following typedefs.

| Typedef | Description |
| --- | --- |
| [_ATL_BASE_MODULE](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#_atl_base_module) | Defined as a typedef based on [_ATL_BASE_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-base-module70-structure?view=msvc-170). |
| [_ATL_COM_MODULE](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#_atl_com_module) | Defined as a typedef based on [_ATL_COM_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-com-module70-structure?view=msvc-170). |
| [_ATL_MODULE](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#_atl_module) | Defined as a typedef based on [_ATL_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-module70-structure?view=msvc-170). |
| [_ATL_WIN_MODULE](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#_atl_win_module) | Defined as a typedef based on [_ATL_WIN_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-win-module70-structure?view=msvc-170) |
| [ATL_URL_PORT](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#atl_url_port) | The type used by [CUrl](https://learn.microsoft.com/en-us/cpp/atl/reference/curl-class?view=msvc-170) for specifying a port number. |
| [CComDispatchDriver](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#ccomdispatchdriver) | This class manages COM interface pointers. |
| [CComGlobalsThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#ccomglobalsthreadmodel) | Calls the appropriate thread model methods, regardless of the threading model being used. |
| [CComObjectThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#ccomobjectthreadmodel) | Calls the appropriate thread model methods, regardless of the threading model being used. |
| [CContainedWindow](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#ccontainedwindow) | This class is a specialization of `CContainedWindowT`. |
| [CPath](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#cpath) | A specialization of [CPathT](https://learn.microsoft.com/en-us/cpp/atl/reference/cpatht-class?view=msvc-170) using `CString`. |
| [CPathA](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#cpatha) | A specialization of [CPathT](https://learn.microsoft.com/en-us/cpp/atl/reference/cpatht-class?view=msvc-170) using `CStringA`. |
| [CPathW](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#cpathw) | A specialization of [CPathT](https://learn.microsoft.com/en-us/cpp/atl/reference/cpatht-class?view=msvc-170) using `CStringW`. |
| [CSimpleValArray](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#csimplevalarray) | Represents an array for storing simple types. |
| [DefaultThreadTraits](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#defaultthreadtraits) | The default thread traits class. |
| [LPCURL](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#lpcurl) | A pointer to a constant [CUrl](https://learn.microsoft.com/en-us/cpp/atl/reference/curl-class?view=msvc-170) object. |
| [LPURL](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#lpurl) | A pointer to a [CUrl](https://learn.microsoft.com/en-us/cpp/atl/reference/curl-class?view=msvc-170) object. |

Defined as a typedef based on _ATL_BASE_MODULE70.

```
typedef ATL::_ATL_BASE_MODULE70 _ATL_BASE_MODULE;
```

Used in every ATL project. Based on [_ATL_BASE_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-base-module70-structure?view=msvc-170).

Classes that are part of the ATL 7.0 Module Classes derive from the _ATL_BASE_MODULE structure. For more information on ATL Module Classes, refer to [COM Modules Classes](https://learn.microsoft.com/en-us/cpp/atl/com-modules-classes?view=msvc-170).

**Header:** atlcore.h

Defined as a typedef based on _ATL_COM_MODULE70.

```
typedef ATL::_ATL_COM_MODULE70 _ATL_COM_MODULE;
```

Used by ATL projects which use COM features. Based on [_ATL_COM_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-com-module70-structure?view=msvc-170).

**Header:** atlbase.h

Defined as a typedef based on _ATL_MODULE70.

```
typedef ATL::_ATL_MODULE70 _ATL_MODULE;
```

**Header:**

Based on [_ATL_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-module70-structure?view=msvc-170).

Defined as a typedef based on _ATL_WIN_MODULE70.

```
typedef ATL::_ATL_WIN_MODULE70 _ATL_WIN_MODULE;
```

Used by any ATL projects which use windowing features. Based on [_ATL_WIN_MODULE70](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-win-module70-structure?view=msvc-170).

**Header:** atlbase.h

The type used by [CUrl](https://learn.microsoft.com/en-us/cpp/atl/reference/curl-class?view=msvc-170) for specifying a port number.

```
typedef WORD ATL_URL_PORT;
```

**Header:** atlutil.h

This class manages COM interface pointers.

```
typedef CComQIPtr<IDispatch, &__uuidof(IDispatch)> CComDispatchDriver;
```

**Header:** atlbase.h

Calls the appropriate thread model methods, regardless of the threading model being used.

```
#if defined(_ATL_SINGLE_THREADED)
typedef CComSingleThreadModel CComGlobalsThreadModel;
#elif defined(_ATL_APARTMENT_THREADED)
typedef CComMultiThreadModel CComGlobalsThreadModel;
#elif defined(_ATL_FREE_THREADED)
typedef CComMultiThreadModel CComGlobalsThreadModel;
#else
#pragma message ("No global threading model defined")
#endif
```

Depending on the threading model used by your application, the **`typedef`** name `CComGlobalsThreadModel` references either [CComSingleThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/ccomsinglethreadmodel-class?view=msvc-170) or [CComMultiThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/ccommultithreadmodel-class?view=msvc-170). These classes provide additional **`typedef`** names to reference a critical section class.

Using `CComGlobalsThreadModel` frees you from specifying a particular threading model class. Regardless of the threading model being used, the appropriate methods will be called.

In addition to `CComGlobalsThreadModel`, ATL provides the **`typedef`** name [CComObjectThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#ccomobjectthreadmodel). The class referenced by each **`typedef`** depends on the threading model used, as shown in the following table:

| typedef | Single threading | Apartment threading | Free threading |
| --- | --- | --- | --- |
| `CComObjectThreadModel` | S | S | M |
| `CComGlobalsThreadModel` | S | M | M |

S= `CComSingleThreadModel`; M= `CComMultiThreadModel`

Use `CComObjectThreadModel` within a single object class. Use `CComGlobalsThreadModel` in an object that is globally available to your program, or when you want to protect module resources across multiple threads.

**Header:** atlbase.h

Calls the appropriate thread model methods, regardless of the threading model being used.

```
#if defined(_ATL_SINGLE_THREADED)
typedef CComSingleThreadModel CComObjectThreadModel;
#elif defined(_ATL_APARTMENT_THREADED)
typedef CComSingleThreadModel CComObjectThreadModel;
#elif defined(_ATL_FREE_THREADED)
typedef CComMultiThreadModel CComObjectThreadModel;
#else
#pragma message ("No global threading model defined")
#endif
```

Depending on the threading model used by your application, the **`typedef`** name `CComObjectThreadModel` references either [CComSingleThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/ccomsinglethreadmodel-class?view=msvc-170) or [CComMultiThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/ccommultithreadmodel-class?view=msvc-170). These classes provide additional **`typedef`** names to reference a critical section class.

Using `CComObjectThreadModel` frees you from specifying a particular threading model class. Regardless of the threading model being used, the appropriate methods will be called.

In addition to `CComObjectThreadModel`, ATL provides the **`typedef`** name [CComGlobalsThreadModel](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-typedefs?view=msvc-170#ccomglobalsthreadmodel). The class referenced by each **`typedef`** depends on the threading model used, as shown in the following table:

| typedef | Single threading | Apartment threading | Free threading |
| --- | --- | --- | --- |
| `CComObjectThreadModel` | S | S | M |
| `CComGlobalsThreadModel` | S | M | M |

S= `CComSingleThreadModel`; M= `CComMultiThreadModel`

Use `CComObjectThreadModel` within a single object class. Use `CComGlobalsThreadModel` in an object that is either globally available to your program, or when you want to protect module resources across multiple threads.

**Header:** atlbase.h

This class is a specialization of `CContainedWindowT`.

```
typedef CContainedWindowT<CWindow> CContainedWindow;
```

**Header:** atlwin.h

`CContainedWindow` is a specialization of [CContainedWindowT](https://learn.microsoft.com/en-us/cpp/atl/reference/ccontainedwindowt-class?view=msvc-170). If you want to change the base class or traits, use `CContainedWindowT` directly.

A specialization of [CPathT](https://learn.microsoft.com/en-us/cpp/atl/reference/cpatht-class?view=msvc-170) using `CString`.

```
typedef CPathT<CString> CPath;
```

**Header:** atlpath.h

A specialization of [CPathT](https://learn.microsoft.com/en-us/cpp/atl/reference/cpatht-class?view=msvc-170) using `CStringA`.

```
typedef CPathT<CStringA> CPathA;
```

**Header:** atlpath.h

A specialization of [CPathT](https://learn.microsoft.com/en-us/cpp/atl/reference/cpatht-class?view=msvc-170) using `CStringW`.

```
typedef ATL::CPathT<CStringW> CPathW;
```

**Header:** atlpath.h

Represents an array for storing simple types.

```
#define CSimpleValArray CSimpleArray
```

`CSimpleValArray` is provided for creating and managing arrays containing simple data types. It is a simple #define of [CSimpleArray](https://learn.microsoft.com/en-us/cpp/atl/reference/csimplearray-class?view=msvc-170).

**Header:** atlsimpcoll.h

A pointer to a constant [CUrl](https://learn.microsoft.com/en-us/cpp/atl/reference/curl-class?view=msvc-170) object.

```
typedef const CUrl* LPCURL;
```

**Header:** atlutil.h

The default thread traits class.

```
#if defined(_MT)
   typedef CRTThreadTraits DefaultThreadTraits;
#else
   typedef Win32ThreadTraits DefaultThreadTraits;
#endif
```

If the current project uses the multithreaded CRT, DefaultThreadTraits is defined as CRTThreadTraits. Otherwise, Win32ThreadTraits is used.

**Header:** atlbase.h

A pointer to a [CUrl](https://learn.microsoft.com/en-us/cpp/atl/reference/curl-class?view=msvc-170) object.

```
typedef CUrl* LPURL;
```

**Header:** atlutil.h

[ATL COM Desktop Components](https://learn.microsoft.com/en-us/cpp/atl/atl-com-desktop-components?view=msvc-170)

[Functions](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-functions?view=msvc-170)

[Global Variables](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-global-variables?view=msvc-170)

[Classes and structs](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-classes?view=msvc-170)

[Macros](https://learn.microsoft.com/en-us/cpp/atl/reference/atl-macros?view=msvc-170)
