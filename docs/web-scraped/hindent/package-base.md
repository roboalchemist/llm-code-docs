# Source: https://hackage.haskell.org/package/base

Title: base

URL Source: https://hackage.haskell.org/package/base

Markdown Content:
base: Core data structures and operations
===============

[Hackage :: [Package]](https://hackage.haskell.org/)
*   Search
*   [Browse](https://hackage.haskell.org/packages/browse)
*   [What's new](https://hackage.haskell.org/packages/recent)
*   [Upload](https://hackage.haskell.org/upload)
*   [User accounts](https://hackage.haskell.org/accounts)

[base](https://hackage.haskell.org/package/base): Core data structures and operations
=====================================================================================

 [ [bsd3](https://hackage.haskell.org/packages/tag/bsd3), [library](https://hackage.haskell.org/packages/tag/library), [prelude](https://hackage.haskell.org/packages/tag/prelude) ] [ [Propose Tags](https://hackage.haskell.org/package/base/tags/edit) ] [ [Report a vulnerability](https://github.com/haskell/security-advisories/blob/main/CONTRIBUTING.md) ] 

Haskell's base library provides, among other things, core types (e.g. [Data.Bool](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bool.html) and [Data.Int](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Int.html)), data structures (e.g. [Data.List](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-List.html), [Data.Tuple](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Tuple.html) and [Data.Maybe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Maybe.html)), the [Control.Exception](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Exception.html) mechanism, and the [System.IO](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-IO.html)&[Control.Concurrent](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Concurrent.html) operations. The [Prelude](https://hackage.haskell.org/package/base-4.22.0.0/docs/Prelude.html) module, which is imported by default, exposes a curated set of types and functions from other modules.

Other data structures like [Map](https://hackage.haskell.org/package/containers/docs/Data-Map.html), [Set](https://hackage.haskell.org/package/containers/docs/Data-Set.html) are available in the [containers](https://hackage.haskell.org/package/containers) library. To work with textual data, use the [text](https://hackage.haskell.org/package/text/docs/Data-Text.html) library.

[![Image 1](https://img.shields.io/static/v1?label=Build&message=PlanningFailed&color=critical)](https://hackage.haskell.org/package/base-4.22.0.0/reports/2)![Image 2](https://img.shields.io/static/v1?label=Documentation&message=Available&color=success)

Modules
-------

[[Index](https://hackage.haskell.org/package/base-4.22.0.0/docs/doc-index.html)] [[Quick Jump](https://hackage.haskell.org/package/base-4.22.0.0/#)]

*   _Control_
    *   [Control.Applicative](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Applicative.html)
    *   [Control.Arrow](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Arrow.html)
    *   [Control.Category](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Category.html)
    *   [Control.Concurrent](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Concurrent.html)
        *   [Control.Concurrent.Chan](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Concurrent-Chan.html)
        *   [Control.Concurrent.MVar](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Concurrent-MVar.html)
        *   [Control.Concurrent.QSem](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Concurrent-QSem.html)
        *   [Control.Concurrent.QSemN](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Concurrent-QSemN.html)

    *   [Control.Exception](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Exception.html)
        *   [Control.Exception.Annotation](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Exception-Annotation.html)
        *   [Control.Exception.Backtrace](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Exception-Backtrace.html)
        *   [Control.Exception.Base](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Exception-Base.html)
        *   [Control.Exception.Context](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Exception-Context.html)

    *   [Control.Monad](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad.html)
        *   [Control.Monad.Fail](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-Fail.html)
        *   [Control.Monad.Fix](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-Fix.html)
        *   _IO_
            *   [Control.Monad.IO.Class](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-IO-Class.html)

        *   [Control.Monad.Instances](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-Instances.html)
        *   [Control.Monad.ST](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST.html)
            *   [Control.Monad.ST.Lazy](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST-Lazy.html)
                *   [Control.Monad.ST.Lazy.Safe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST-Lazy-Safe.html)
                *   [Control.Monad.ST.Lazy.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST-Lazy-Unsafe.html)

            *   [Control.Monad.ST.Safe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST-Safe.html)
            *   [Control.Monad.ST.Strict](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST-Strict.html)
            *   [Control.Monad.ST.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-ST-Unsafe.html)

        *   [Control.Monad.Zip](https://hackage.haskell.org/package/base-4.22.0.0/docs/Control-Monad-Zip.html)

*   _Data_
    *   _Array_
        *   [Data.Array.Byte](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Array-Byte.html)

    *   [Data.Bifoldable](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bifoldable.html)
    *   [Data.Bifoldable1](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bifoldable1.html)
    *   [Data.Bifunctor](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bifunctor.html)
    *   [Data.Bitraversable](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bitraversable.html)
    *   [Data.Bits](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bits.html)
    *   [Data.Bool](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bool.html)
    *   [Data.Bounded](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Bounded.html)
    *   [Data.Char](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Char.html)
    *   [Data.Coerce](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Coerce.html)
    *   [Data.Complex](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Complex.html)
    *   [Data.Data](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Data.html)
    *   [Data.Dynamic](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Dynamic.html)
    *   [Data.Either](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Either.html)
    *   [Data.Enum](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Enum.html)
    *   [Data.Eq](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Eq.html)
    *   [Data.Fixed](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Fixed.html)
    *   [Data.Foldable](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Foldable.html)
    *   [Data.Foldable1](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Foldable1.html)
    *   [Data.Function](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Function.html)
    *   [Data.Functor](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor.html)
        *   [Data.Functor.Classes](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Classes.html)
        *   [Data.Functor.Compose](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Compose.html)
        *   [Data.Functor.Const](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Const.html)
        *   [Data.Functor.Contravariant](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Contravariant.html)
        *   [Data.Functor.Identity](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Identity.html)
        *   [Data.Functor.Product](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Product.html)
        *   [Data.Functor.Sum](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Functor-Sum.html)

    *   [Data.IORef](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-IORef.html)
    *   [Data.Int](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Int.html)
    *   [Data.Ix](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Ix.html)
    *   [Data.Kind](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Kind.html)
    *   [Data.List](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-List.html)
        *   [Data.List.NonEmpty](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-List-NonEmpty.html)

    *   [Data.Maybe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Maybe.html)
    *   [Data.Monoid](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Monoid.html)
    *   [Data.Ord](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Ord.html)
    *   [Data.Proxy](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Proxy.html)
    *   [Data.Ratio](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Ratio.html)
    *   [Data.STRef](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-STRef.html)
        *   [Data.STRef.Lazy](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-STRef-Lazy.html)
        *   [Data.STRef.Strict](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-STRef-Strict.html)

    *   [Data.Semigroup](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Semigroup.html)
    *   [Data.String](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-String.html)
    *   [Data.Traversable](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Traversable.html)
    *   [Data.Tuple](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Tuple.html)
    *   _Type_
        *   [Data.Type.Bool](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Type-Bool.html)
        *   [Data.Type.Coercion](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Type-Coercion.html)
        *   [Data.Type.Equality](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Type-Equality.html)
        *   [Data.Type.Ord](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Type-Ord.html)

    *   [Data.Typeable](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Typeable.html)
    *   [Data.Unique](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Unique.html)
    *   [Data.Version](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Version.html)
    *   [Data.Void](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Void.html)
    *   [Data.Word](https://hackage.haskell.org/package/base-4.22.0.0/docs/Data-Word.html)

*   _Debug_
    *   [Debug.Trace](https://hackage.haskell.org/package/base-4.22.0.0/docs/Debug-Trace.html)

*   [Foreign](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign.html)
    *   [Foreign.C](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-C.html)
        *   [Foreign.C.ConstPtr](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-C-ConstPtr.html)
        *   [Foreign.C.Error](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-C-Error.html)
        *   [Foreign.C.String](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-C-String.html)
        *   [Foreign.C.Types](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-C-Types.html)

    *   [Foreign.Concurrent](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Concurrent.html)
    *   [Foreign.ForeignPtr](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-ForeignPtr.html)
        *   [Foreign.ForeignPtr.Safe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-ForeignPtr-Safe.html)
        *   [Foreign.ForeignPtr.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-ForeignPtr-Unsafe.html)

    *   [Foreign.Marshal](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal.html)
        *   [Foreign.Marshal.Alloc](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Alloc.html)
        *   [Foreign.Marshal.Array](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Array.html)
        *   [Foreign.Marshal.Error](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Error.html)
        *   [Foreign.Marshal.Pool](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Pool.html)
        *   [Foreign.Marshal.Safe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Safe.html)
        *   [Foreign.Marshal.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Unsafe.html)
        *   [Foreign.Marshal.Utils](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Marshal-Utils.html)

    *   [Foreign.Ptr](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Ptr.html)
    *   [Foreign.Safe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Safe.html)
    *   [Foreign.StablePtr](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-StablePtr.html)
    *   [Foreign.Storable](https://hackage.haskell.org/package/base-4.22.0.0/docs/Foreign-Storable.html)

*   _GHC_
    *   [GHC.Arr](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Arr.html)
    *   [GHC.ArrayArray](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ArrayArray.html)
    *   [GHC.Base](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Base.html)
    *   [GHC.Bits](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Bits.html)
    *   [GHC.ByteOrder](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ByteOrder.html)
    *   [GHC.Char](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Char.html)
    *   [GHC.Clock](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Clock.html)
    *   [GHC.Conc](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Conc.html)
        *   [GHC.Conc.IO](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Conc-IO.html)
        *   GHC.Conc.POSIX
            *   GHC.Conc.POSIX.Const

        *   [GHC.Conc.Signal](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Conc-Signal.html)
        *   [GHC.Conc.Sync](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Conc-Sync.html)
        *   GHC.Conc.WinIO
        *   GHC.Conc.Windows

    *   [GHC.ConsoleHandler](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ConsoleHandler.html)
    *   [GHC.Constants](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Constants.html)
    *   [GHC.Desugar](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Desugar.html)
    *   _Encoding_
        *   [GHC.Encoding.UTF8](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Encoding-UTF8.html)

    *   [GHC.Enum](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Enum.html)
    *   [GHC.Environment](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Environment.html)
    *   [GHC.Err](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Err.html)
    *   [GHC.Event](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Event.html)
        *   [GHC.Event.TimeOut](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Event-TimeOut.html)
        *   GHC.Event.Windows
            *   GHC.Event.Windows.Clock
            *   GHC.Event.Windows.ConsoleEvent
            *   GHC.Event.Windows.FFI
            *   GHC.Event.Windows.ManagedThreadPool
            *   GHC.Event.Windows.Thread

    *   [GHC.Exception](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Exception.html)
        *   [GHC.Exception.Type](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Exception-Type.html)

    *   [GHC.ExecutionStack](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ExecutionStack.html)
    *   [GHC.Exts](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Exts.html)
    *   [GHC.Fingerprint](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Fingerprint.html)
        *   [GHC.Fingerprint.Type](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Fingerprint-Type.html)

    *   [GHC.Float](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Float.html)
        *   [GHC.Float.ConversionUtils](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Float-ConversionUtils.html)
        *   [GHC.Float.RealFracMethods](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Float-RealFracMethods.html)

    *   [GHC.Foreign](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Foreign.html)
    *   [GHC.ForeignPtr](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ForeignPtr.html)
    *   [GHC.GHCi](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-GHCi.html)
        *   [GHC.GHCi.Helpers](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-GHCi-Helpers.html)

    *   [GHC.Generics](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Generics.html)
    *   [GHC.IO](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO.html)
        *   [GHC.IO.Buffer](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Buffer.html)
        *   [GHC.IO.BufferedIO](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-BufferedIO.html)
        *   [GHC.IO.Device](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Device.html)
        *   [GHC.IO.Encoding](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding.html)
            *   [GHC.IO.Encoding.CodePage](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-CodePage.html)
                *   GHC.IO.Encoding.CodePage.API
                *   GHC.IO.Encoding.CodePage.Table

            *   [GHC.IO.Encoding.Failure](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-Failure.html)
            *   [GHC.IO.Encoding.Iconv](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-Iconv.html)
            *   [GHC.IO.Encoding.Latin1](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-Latin1.html)
            *   [GHC.IO.Encoding.Types](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-Types.html)
            *   [GHC.IO.Encoding.UTF16](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-UTF16.html)
            *   [GHC.IO.Encoding.UTF32](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-UTF32.html)
            *   [GHC.IO.Encoding.UTF8](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Encoding-UTF8.html)

        *   [GHC.IO.Exception](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Exception.html)
        *   [GHC.IO.FD](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-FD.html)
        *   [GHC.IO.Handle](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Handle.html)
            *   [GHC.IO.Handle.FD](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Handle-FD.html)
            *   [GHC.IO.Handle.Internals](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Handle-Internals.html)
            *   [GHC.IO.Handle.Lock](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Handle-Lock.html)
            *   [GHC.IO.Handle.Text](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Handle-Text.html)
            *   [GHC.IO.Handle.Types](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Handle-Types.html)
            *   GHC.IO.Handle.Windows

        *   [GHC.IO.IOMode](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-IOMode.html)
        *   [GHC.IO.StdHandles](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-StdHandles.html)
        *   [GHC.IO.SubSystem](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-SubSystem.html)
        *   [GHC.IO.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IO-Unsafe.html)
        *   _Windows_
            *   GHC.IO.Windows.Encoding
            *   GHC.IO.Windows.Handle
            *   GHC.IO.Windows.Paths

    *   [GHC.IOArray](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IOArray.html)
    *   [GHC.IORef](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IORef.html)
    *   [GHC.InfoProv](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-InfoProv.html)
    *   [GHC.Int](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Int.html)
    *   [GHC.Integer](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Integer.html)
        *   [GHC.Integer.Logarithms](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Integer-Logarithms.html)

    *   [GHC.IsList](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-IsList.html)
    *   [GHC.Ix](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Ix.html)
    *   _JS_
        *   _Foreign_
            *   GHC.JS.Foreign.Callback

        *   GHC.JS.Prim
            *   GHC.JS.Prim.Internal
                *   GHC.JS.Prim.Internal.Build

    *   [GHC.List](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-List.html)
    *   [GHC.MVar](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-MVar.html)
    *   [GHC.Maybe](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Maybe.html)
    *   [GHC.Natural](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Natural.html)
    *   [GHC.Num](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Num.html)
        *   [GHC.Num.BigNat](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Num-BigNat.html)
        *   [GHC.Num.Integer](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Num-Integer.html)
        *   [GHC.Num.Natural](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Num-Natural.html)

    *   [GHC.OldList](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-OldList.html)
    *   [GHC.OverloadedLabels](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-OverloadedLabels.html)
    *   [GHC.Profiling](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Profiling.html)
    *   [GHC.Ptr](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Ptr.html)
    *   _RTS_
        *   [GHC.RTS.Flags](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-RTS-Flags.html)

    *   [GHC.Read](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Read.html)
    *   [GHC.Real](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Real.html)
    *   [GHC.Records](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Records.html)
    *   [GHC.ResponseFile](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ResponseFile.html)
    *   [GHC.ST](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-ST.html)
    *   [GHC.STRef](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-STRef.html)
    *   [GHC.Show](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Show.html)
    *   [GHC.Stable](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Stable.html)
    *   [GHC.StableName](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-StableName.html)
    *   [GHC.Stack](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Stack.html)
        *   [GHC.Stack.CCS](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Stack-CCS.html)
        *   [GHC.Stack.CloneStack](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Stack-CloneStack.html)
        *   [GHC.Stack.Types](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Stack-Types.html)

    *   [GHC.StaticPtr](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-StaticPtr.html)
    *   [GHC.Stats](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Stats.html)
    *   [GHC.Storable](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Storable.html)
    *   [GHC.TopHandler](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-TopHandler.html)
    *   [GHC.TypeError](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-TypeError.html)
    *   [GHC.TypeLits](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-TypeLits.html)
    *   [GHC.TypeNats](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-TypeNats.html)
    *   [GHC.Unicode](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Unicode.html)
    *   [GHC.Weak](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Weak.html)
        *   [GHC.Weak.Finalize](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Weak-Finalize.html)

    *   GHC.Windows
    *   [GHC.Word](https://hackage.haskell.org/package/base-4.22.0.0/docs/GHC-Word.html)

*   [Numeric](https://hackage.haskell.org/package/base-4.22.0.0/docs/Numeric.html)
    *   [Numeric.Natural](https://hackage.haskell.org/package/base-4.22.0.0/docs/Numeric-Natural.html)

*   [Prelude](https://hackage.haskell.org/package/base-4.22.0.0/docs/Prelude.html)
*   _System_
    *   [System.CPUTime](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-CPUTime.html)
    *   _Console_
        *   [System.Console.GetOpt](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Console-GetOpt.html)

    *   [System.Environment](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Environment.html)
        *   [System.Environment.Blank](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Environment-Blank.html)

    *   [System.Exit](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Exit.html)
    *   [System.IO](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-IO.html)
        *   [System.IO.Error](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-IO-Error.html)
        *   [System.IO.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-IO-Unsafe.html)

    *   [System.Info](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Info.html)
    *   [System.Mem](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Mem.html)
        *   [System.Mem.StableName](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Mem-StableName.html)
        *   [System.Mem.Weak](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Mem-Weak.html)

    *   _Posix_
        *   [System.Posix.Internals](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Posix-Internals.html)
        *   [System.Posix.Types](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Posix-Types.html)

    *   [System.Timeout](https://hackage.haskell.org/package/base-4.22.0.0/docs/System-Timeout.html)

*   _Text_
    *   _ParserCombinators_
        *   [Text.ParserCombinators.ReadP](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-ParserCombinators-ReadP.html)
        *   [Text.ParserCombinators.ReadPrec](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-ParserCombinators-ReadPrec.html)

    *   [Text.Printf](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-Printf.html)
    *   [Text.Read](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-Read.html)
        *   [Text.Read.Lex](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-Read-Lex.html)

    *   [Text.Show](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-Show.html)
        *   [Text.Show.Functions](https://hackage.haskell.org/package/base-4.22.0.0/docs/Text-Show-Functions.html)

*   _Type_
    *   [Type.Reflection](https://hackage.haskell.org/package/base-4.22.0.0/docs/Type-Reflection.html)
        *   [Type.Reflection.Unsafe](https://hackage.haskell.org/package/base-4.22.0.0/docs/Type-Reflection-Unsafe.html)

*   _Unsafe_
    *   [Unsafe.Coerce](https://hackage.haskell.org/package/base-4.22.0.0/docs/Unsafe-Coerce.html)

Downloads
---------

*   [base-4.22.0.0.tar.gz](https://hackage.haskell.org/package/base-4.22.0.0/base-4.22.0.0.tar.gz) [[browse](https://hackage.haskell.org/package/base-4.22.0.0/src/)] (Cabal source package)
*   [Package description](https://hackage.haskell.org/package/base-4.22.0.0/base.cabal) (as included in the package)

#### Maintainer's Corner

[Package maintainers](https://hackage.haskell.org/package/base/maintainers)

*   [AustinSeipp](https://hackage.haskell.org/user/AustinSeipp), [BenGamari](https://hackage.haskell.org/user/BenGamari), [HerbertValerioRiedel](https://hackage.haskell.org/user/HerbertValerioRiedel), [IanLynagh](https://hackage.haskell.org/user/IanLynagh), [LuiteStegeman](https://hackage.haskell.org/user/LuiteStegeman), [PaoloCapriotti](https://hackage.haskell.org/user/PaoloCapriotti), [wz1000](https://hackage.haskell.org/user/wz1000)

For package maintainers and hackage trustees

*   [edit package information](https://hackage.haskell.org/package/base/maintain)

Candidates

*   [4.14.3.0](https://hackage.haskell.org/package/base-4.14.3.0/candidate), [4.15.1.0](https://hackage.haskell.org/package/base-4.15.1.0/candidate), [4.16.0.0](https://hackage.haskell.org/package/base-4.16.0.0/candidate), [4.16.1.0](https://hackage.haskell.org/package/base-4.16.1.0/candidate), [4.16.2.0](https://hackage.haskell.org/package/base-4.16.2.0/candidate), [4.16.3.0](https://hackage.haskell.org/package/base-4.16.3.0/candidate), [4.16.4.0](https://hackage.haskell.org/package/base-4.16.4.0/candidate), [4.17.0.0](https://hackage.haskell.org/package/base-4.17.0.0/candidate), [4.18.0.0](https://hackage.haskell.org/package/base-4.18.0.0/candidate), [4.18.1.0](https://hackage.haskell.org/package/base-4.18.1.0/candidate), [4.18.3.0](https://hackage.haskell.org/package/base-4.18.3.0/candidate), [4.19.0.0](https://hackage.haskell.org/package/base-4.19.0.0/candidate), [4.19.2.0](https://hackage.haskell.org/package/base-4.19.2.0/candidate), [4.20.0.0](https://hackage.haskell.org/package/base-4.20.0.0/candidate)

| Versions [[RSS](https://hackage.haskell.org/package/base.rss)] | [3.0.3.1](https://hackage.haskell.org/package/base-3.0.3.1), [3.0.3.2](https://hackage.haskell.org/package/base-3.0.3.2), [4.0.0.0](https://hackage.haskell.org/package/base-4.0.0.0), [4.1.0.0](https://hackage.haskell.org/package/base-4.1.0.0), [4.2.0.0](https://hackage.haskell.org/package/base-4.2.0.0), [4.2.0.1](https://hackage.haskell.org/package/base-4.2.0.1), [4.2.0.2](https://hackage.haskell.org/package/base-4.2.0.2), [4.3.0.0](https://hackage.haskell.org/package/base-4.3.0.0), [4.3.1.0](https://hackage.haskell.org/package/base-4.3.1.0), [4.4.0.0](https://hackage.haskell.org/package/base-4.4.0.0), [4.4.1.0](https://hackage.haskell.org/package/base-4.4.1.0), [4.5.0.0](https://hackage.haskell.org/package/base-4.5.0.0), [4.5.1.0](https://hackage.haskell.org/package/base-4.5.1.0), [4.6.0.0](https://hackage.haskell.org/package/base-4.6.0.0), [4.6.0.1](https://hackage.haskell.org/package/base-4.6.0.1), [4.7.0.0](https://hackage.haskell.org/package/base-4.7.0.0), [4.7.0.1](https://hackage.haskell.org/package/base-4.7.0.1), [4.7.0.2](https://hackage.haskell.org/package/base-4.7.0.2), [4.8.0.0](https://hackage.haskell.org/package/base-4.8.0.0), [4.8.1.0](https://hackage.haskell.org/package/base-4.8.1.0), [4.8.2.0](https://hackage.haskell.org/package/base-4.8.2.0), [4.9.0.0](https://hackage.haskell.org/package/base-4.9.0.0), [4.9.1.0](https://hackage.haskell.org/package/base-4.9.1.0), [4.10.0.0](https://hackage.haskell.org/package/base-4.10.0.0), [4.10.1.0](https://hackage.haskell.org/package/base-4.10.1.0), [4.11.0.0](https://hackage.haskell.org/package/base-4.11.0.0), [4.11.1.0](https://hackage.haskell.org/package/base-4.11.1.0), [4.12.0.0](https://hackage.haskell.org/package/base-4.12.0.0), [4.13.0.0](https://hackage.haskell.org/package/base-4.13.0.0), [4.14.0.0](https://hackage.haskell.org/package/base-4.14.0.0), [4.14.1.0](https://hackage.haskell.org/package/base-4.14.1.0), [4.14.2.0](https://hackage.haskell.org/package/base-4.14.2.0), [4.14.3.0](https://hackage.haskell.org/package/base-4.14.3.0), [4.15.0.0](https://hackage.haskell.org/package/base-4.15.0.0), [4.15.1.0](https://hackage.haskell.org/package/base-4.15.1.0), [4.16.0.0](https://hackage.haskell.org/package/base-4.16.0.0), [4.16.1.0](https://hackage.haskell.org/package/base-4.16.1.0), [4.16.2.0](https://hackage.haskell.org/package/base-4.16.2.0), [4.16.3.0](https://hackage.haskell.org/package/base-4.16.3.0), [4.16.4.0](https://hackage.haskell.org/package/base-4.16.4.0), [4.17.0.0](https://hackage.haskell.org/package/base-4.17.0.0), [4.17.1.0](https://hackage.haskell.org/package/base-4.17.1.0), [4.17.2.0](https://hackage.haskell.org/package/base-4.17.2.0), [4.17.2.1](https://hackage.haskell.org/package/base-4.17.2.1), [4.18.0.0](https://hackage.haskell.org/package/base-4.18.0.0), [4.18.1.0](https://hackage.haskell.org/package/base-4.18.1.0), [4.18.2.0](https://hackage.haskell.org/package/base-4.18.2.0), [4.18.2.1](https://hackage.haskell.org/package/base-4.18.2.1), [4.18.3.0](https://hackage.haskell.org/package/base-4.18.3.0), [4.19.0.0](https://hackage.haskell.org/package/base-4.19.0.0), [4.19.1.0](https://hackage.haskell.org/package/base-4.19.1.0), [4.19.2.0](https://hackage.haskell.org/package/base-4.19.2.0), [4.20.0.0](https://hackage.haskell.org/package/base-4.20.0.0), [4.20.0.1](https://hackage.haskell.org/package/base-4.20.0.1), [4.20.1.0](https://hackage.haskell.org/package/base-4.20.1.0), [4.20.2.0](https://hackage.haskell.org/package/base-4.20.2.0), [4.21.0.0](https://hackage.haskell.org/package/base-4.21.0.0), [4.21.1.0](https://hackage.haskell.org/package/base-4.21.1.0), **4.22.0.0** |
| --- |
| Change log | [changelog.md](https://hackage.haskell.org/package/base-4.22.0.0/changelog) |
| Dependencies | [ghc-internal](https://hackage.haskell.org/package/ghc-internal) (>=9.1401 &&<9.1402), [ghc-prim](https://hackage.haskell.org/package/ghc-prim) [[details](https://hackage.haskell.org/package/base-4.22.0.0/dependencies)] |
| License | [BSD-3-Clause](https://hackage.haskell.org/package/base-4.22.0.0/src/LICENSE) |
| Author |  |
| Maintainer | Core Libraries Committee <core-libraries-committee@haskell.org> |
| Uploaded | by [wz1000](https://hackage.haskell.org/user/wz1000) at 2025-12-19T11:52:34Z |
| Category | [Prelude](https://hackage.haskell.org/packages/#cat:Prelude) |
| Bug tracker | [https://github.com/haskell/core-libraries-committee/issues](https://github.com/haskell/core-libraries-committee/issues) |
| Distributions | Arch:[4.18.2.1](https://archlinux.org/packages/extra/x86_64/ghc), Fedora:[4.20.2.0](https://src.fedoraproject.org/rpms/ghc) |
| Reverse Dependencies | 17356 direct, 74 indirect [[details](https://hackage.haskell.org/package/base-4.22.0.0/)] |
| Downloads | 69279 total (162 in the last 30 days) |
| Rating | 2.75 (votes: 38) [estimated by [Bayesian average](https://en.wikipedia.org/wiki/Bayesian_average)] |
| Your Rating | * λ * λ * λ |
| Status | Docs uploaded by user [[build log](https://hackage.haskell.org/package/base-4.22.0.0/reports/2)] All reported builds failed as of 2025-12-19 [[all 2 reports](https://hackage.haskell.org/package/base-4.22.0.0/reports/)] |

Produced by [hackage](https://hackage.haskell.org/) and [Cabal](http://haskell.org/cabal/) 3.16.1.0.

You can find any exported type, constructor, class, function or pattern defined in this package by (approximate) name.

| Key | Shortcut |
| --- | --- |
| s | Open this search box |
| esc | Close this search box |
| ↓,ctrl + j | Move down in search results |
| ↑,ctrl + k | Move up in search results |
| ↵ | Go to active search result |
