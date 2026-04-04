# Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FRichTextDecorator

Title: FRichTextDecorator | Unreal Engine 5.7 Documentation | Epic Developer Community

URL Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FRichTextDecorator

Markdown Content:
Navigation
----------

[API](https://dev.epicgames.com/documentation/en-us/unreal-engine/API)>[API/Runtime](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime)>[API/Runtime/UMG](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG)

|  |  |
| --- | --- |
| _Name_ | FRichTextDecorator |
| _Type_ | class |
| _Header File_ | /Engine/Source/Runtime/UMG/Public/Components/RichTextBlockDecorator.h |
| _Include Path_ | #include "Components/RichTextBlockDecorator.h" |

Syntax
------

```
class FRichTextDecorator : public ITextDecorator
```

Implements Interfaces
---------------------

* [ITextDecorator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ITextDecorator)

Constructors
------------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| FRichTextDecorator ( [URichTextBlock](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/URichTextBlock)* InOwner ) |  | Components/RichTextBlockDecorator.h |  |

Destructors
-----------

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual ~FRichTextDecorator() |  | Components/RichTextBlockDecorator.h |  |

Functions
---------

### Public

#### Overridden from [ITextDecorator](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ITextDecorator)

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[ISlateRun](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/ISlateRun)> Create ( const [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)< class [FTextLayout](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/FTextLayout)>& TextLayout, const [FTextRunParseResults](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/FTextRunParseResults)& RunParseResult, const [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)& OriginalText, const [TSharedRef](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedRef)<[FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)>& InOutModelText, const [ISlateStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/ISlateStyle)* Style ) |  | Components/RichTextBlockDecorator.h |  |
| virtual bool Supports ( const [FTextRunParseResults](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/FTextRunParseResults)& RunParseResult, const [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)& Text ) const | Override this function to specify which types of tags are handled by this decorator | Components/RichTextBlockDecorator.h |  |

### Protected

| Name | Remarks | Include Path | [Unreal Specifiers](https://dev.epicgames.com/documentation/unreal-engine/ufunctions-in-unreal-engine#functionspecifiers) |
| --- | --- | --- | --- |
| virtual void [CreateDecoratorText](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/UMG/FRichTextDecorator/CreateDecoratorText) ( const [FTextRunInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/FTextRunInfo)& RunInfo, [FTextBlockStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FTextBlockStyle)& InOutTextStyle, [FString](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FString)& InOutString ) const | Override this function if you want to dynamically generate text, optionally changing the style. | Components/RichTextBlockDecorator.h |  |
| virtual [TSharedPtr](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/TSharedPtr)<[SWidget](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/SWidget)> CreateDecoratorWidget ( const [FTextRunInfo](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Slate/FTextRunInfo)& RunInfo, const [FTextBlockStyle](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/SlateCore/FTextBlockStyle)& DefaultTextStyle ) const | Override this function if you want to create a unique widget like an image | Components/RichTextBlockDecorator.h |  |
