# Source: https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test

Title: test package - go.temporal.io/api/internal/protojson/testprotos/test - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test

Markdown Content:
*   [Constants](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#pkg-constants)
*   [Variables](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#pkg-variables)
*   [type FooRequest](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest)
*       *   [func (*FooRequest) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest.Descriptor)deprecated
    *   [func (*FooRequest) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest.ProtoMessage)
    *   [func (x *FooRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest.ProtoReflect)
    *   [func (x *FooRequest) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest.Reset)
    *   [func (x *FooRequest) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest.String)

*   [type FooResponse](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse)
*       *   [func (*FooResponse) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse.Descriptor)deprecated
    *   [func (*FooResponse) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse.ProtoMessage)
    *   [func (x *FooResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse.ProtoReflect)
    *   [func (x *FooResponse) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse.Reset)
    *   [func (x *FooResponse) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse.String)

*   [type ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)
*       *   [func (ForeignEnum) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.Descriptor)
    *   [func (x ForeignEnum) Enum() *ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.Enum)
    *   [func (ForeignEnum) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.EnumDescriptor)deprecated
    *   [func (x ForeignEnum) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.Number)
    *   [func (x ForeignEnum) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.String)
    *   [func (ForeignEnum) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.Type)
    *   [func (x *ForeignEnum) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum.UnmarshalJSON)deprecated

*   [type ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage)
*       *   [func (*ForeignMessage) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.Descriptor)deprecated
    *   [func (x *ForeignMessage) GetC() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.GetC)
    *   [func (x *ForeignMessage) GetD() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.GetD)
    *   [func (*ForeignMessage) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.ProtoMessage)
    *   [func (x *ForeignMessage) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.ProtoReflect)
    *   [func (x *ForeignMessage) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.Reset)
    *   [func (x *ForeignMessage) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage.String)

*   [type ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum)
*       *   [func (ImportEnum) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.Descriptor)
    *   [func (x ImportEnum) Enum() *ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.Enum)
    *   [func (ImportEnum) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.EnumDescriptor)deprecated
    *   [func (x ImportEnum) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.Number)
    *   [func (x ImportEnum) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.String)
    *   [func (ImportEnum) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.Type)
    *   [func (x *ImportEnum) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum.UnmarshalJSON)deprecated

*   [type ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage)
*       *   [func (*ImportMessage) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage.Descriptor)deprecated
    *   [func (*ImportMessage) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage.ProtoMessage)
    *   [func (x *ImportMessage) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage.ProtoReflect)
    *   [func (x *ImportMessage) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage.Reset)
    *   [func (x *ImportMessage) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage.String)

*   [type OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup)
*       *   [func (*OptionalGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.Descriptor)deprecated
    *   [func (x *OptionalGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.GetA)
    *   [func (x *OptionalGroup) GetOptionalNestedMessage() *TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.GetOptionalNestedMessage)
    *   [func (x *OptionalGroup) GetSameFieldNumber() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.GetSameFieldNumber)
    *   [func (*OptionalGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.ProtoMessage)
    *   [func (x *OptionalGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.ProtoReflect)
    *   [func (x *OptionalGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.Reset)
    *   [func (x *OptionalGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup.String)

*   [type PublicImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage)
*       *   [func (*PublicImportMessage) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage.Descriptor)deprecated
    *   [func (*PublicImportMessage) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage.ProtoMessage)
    *   [func (x *PublicImportMessage) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage.ProtoReflect)
    *   [func (x *PublicImportMessage) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage.Reset)
    *   [func (x *PublicImportMessage) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage.String)

*   [type RemoteDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault)
*       *   [func (*RemoteDefault) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.Descriptor)deprecated
    *   [func (x *RemoteDefault) GetDefault() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetDefault)
    *   [func (x *RemoteDefault) GetElevent() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetElevent)
    *   [func (x *RemoteDefault) GetNegative() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetNegative)
    *   [func (x *RemoteDefault) GetOne() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetOne)
    *   [func (x *RemoteDefault) GetSeventeen() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetSeventeen)
    *   [func (x *RemoteDefault) GetSixtyseven() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetSixtyseven)
    *   [func (x *RemoteDefault) GetThirtyseven() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetThirtyseven)
    *   [func (x *RemoteDefault) GetZero() enums.Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.GetZero)
    *   [func (*RemoteDefault) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.ProtoMessage)
    *   [func (x *RemoteDefault) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.ProtoReflect)
    *   [func (x *RemoteDefault) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.Reset)
    *   [func (x *RemoteDefault) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault.String)

*   [type RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup)
*       *   [func (*RepeatedGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.Descriptor)deprecated
    *   [func (x *RepeatedGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.GetA)
    *   [func (x *RepeatedGroup) GetOptionalNestedMessage() *TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.GetOptionalNestedMessage)
    *   [func (*RepeatedGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.ProtoMessage)
    *   [func (x *RepeatedGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.ProtoReflect)
    *   [func (x *RepeatedGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.Reset)
    *   [func (x *RepeatedGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup.String)

*   [type TestAllExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions)
*       *   [func (*TestAllExtensions) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions.Descriptor)deprecated
    *   [func (*TestAllExtensions) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions.ProtoMessage)
    *   [func (x *TestAllExtensions) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions.ProtoReflect)
    *   [func (x *TestAllExtensions) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions.Reset)
    *   [func (x *TestAllExtensions) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions.String)

*   [type TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage)
*       *   [func (*TestAllExtensions_NestedMessage) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.Descriptor)deprecated
    *   [func (x *TestAllExtensions_NestedMessage) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.GetA)
    *   [func (x *TestAllExtensions_NestedMessage) GetCorecursive() *TestAllExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.GetCorecursive)
    *   [func (*TestAllExtensions_NestedMessage) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.ProtoMessage)
    *   [func (x *TestAllExtensions_NestedMessage) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.ProtoReflect)
    *   [func (x *TestAllExtensions_NestedMessage) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.Reset)
    *   [func (x *TestAllExtensions_NestedMessage) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage.String)

*   [type TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)
*       *   [func (*TestAllTypes) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.Descriptor)deprecated
    *   [func (x *TestAllTypes) GetDefaultBool() bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultBool)
    *   [func (x *TestAllTypes) GetDefaultBytes() []byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultBytes)
    *   [func (x *TestAllTypes) GetDefaultDouble() float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultDouble)
    *   [func (x *TestAllTypes) GetDefaultFixed32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultFixed32)
    *   [func (x *TestAllTypes) GetDefaultFixed64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultFixed64)
    *   [func (x *TestAllTypes) GetDefaultFloat() float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultFloat)
    *   [func (x *TestAllTypes) GetDefaultForeignEnum() ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultForeignEnum)
    *   [func (x *TestAllTypes) GetDefaultInt32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultInt32)
    *   [func (x *TestAllTypes) GetDefaultInt64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultInt64)
    *   [func (x *TestAllTypes) GetDefaultNestedEnum() TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultNestedEnum)
    *   [func (x *TestAllTypes) GetDefaultSfixed32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultSfixed32)
    *   [func (x *TestAllTypes) GetDefaultSfixed64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultSfixed64)
    *   [func (x *TestAllTypes) GetDefaultSint32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultSint32)
    *   [func (x *TestAllTypes) GetDefaultSint64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultSint64)
    *   [func (x *TestAllTypes) GetDefaultString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultString)
    *   [func (x *TestAllTypes) GetDefaultUint32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultUint32)
    *   [func (x *TestAllTypes) GetDefaultUint64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetDefaultUint64)
    *   [func (x *TestAllTypes) GetMapBoolBool() map[bool]bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapBoolBool)
    *   [func (x *TestAllTypes) GetMapFixed32Fixed32() map[uint32]uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapFixed32Fixed32)
    *   [func (x *TestAllTypes) GetMapFixed64Fixed64() map[uint64]uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapFixed64Fixed64)
    *   [func (x *TestAllTypes) GetMapInt32Double() map[int32]float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapInt32Double)
    *   [func (x *TestAllTypes) GetMapInt32Float() map[int32]float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapInt32Float)
    *   [func (x *TestAllTypes) GetMapInt32Int32() map[int32]int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapInt32Int32)
    *   [func (x *TestAllTypes) GetMapInt64Int64() map[int64]int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapInt64Int64)
    *   [func (x *TestAllTypes) GetMapSfixed32Sfixed32() map[int32]int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapSfixed32Sfixed32)
    *   [func (x *TestAllTypes) GetMapSfixed64Sfixed64() map[int64]int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapSfixed64Sfixed64)
    *   [func (x *TestAllTypes) GetMapSint32Sint32() map[int32]int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapSint32Sint32)
    *   [func (x *TestAllTypes) GetMapSint64Sint64() map[int64]int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapSint64Sint64)
    *   [func (x *TestAllTypes) GetMapStringBytes() map[string][]byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapStringBytes)
    *   [func (x *TestAllTypes) GetMapStringNestedEnum() map[string]TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapStringNestedEnum)
    *   [func (x *TestAllTypes) GetMapStringNestedMessage() map[string]*TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapStringNestedMessage)
    *   [func (x *TestAllTypes) GetMapStringString() map[string]string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapStringString)
    *   [func (x *TestAllTypes) GetMapUint32Uint32() map[uint32]uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapUint32Uint32)
    *   [func (x *TestAllTypes) GetMapUint64Uint64() map[uint64]uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetMapUint64Uint64)
    *   [func (x *TestAllTypes) GetOneofBool() bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofBool)
    *   [func (x *TestAllTypes) GetOneofBytes() []byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofBytes)
    *   [func (x *TestAllTypes) GetOneofDouble() float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofDouble)
    *   [func (x *TestAllTypes) GetOneofEnum() TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofEnum)
    *   [func (x *TestAllTypes) GetOneofField() isTestAllTypes_OneofField](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofField)
    *   [func (x *TestAllTypes) GetOneofFloat() float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofFloat)
    *   [func (x *TestAllTypes) GetOneofNestedMessage() *TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofNestedMessage)
    *   [func (x *TestAllTypes) GetOneofOptional() isTestAllTypes_OneofOptional](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofOptional)
    *   [func (x *TestAllTypes) GetOneofOptionalUint32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofOptionalUint32)
    *   [func (x *TestAllTypes) GetOneofString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofString)
    *   [func (x *TestAllTypes) GetOneofUint32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofUint32)
    *   [func (x *TestAllTypes) GetOneofUint64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofUint64)
    *   [func (x *TestAllTypes) GetOneofgroup() *TestAllTypes_OneofGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOneofgroup)
    *   [func (x *TestAllTypes) GetOptionalBool() bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalBool)
    *   [func (x *TestAllTypes) GetOptionalBytes() []byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalBytes)
    *   [func (x *TestAllTypes) GetOptionalDouble() float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalDouble)
    *   [func (x *TestAllTypes) GetOptionalFixed32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalFixed32)
    *   [func (x *TestAllTypes) GetOptionalFixed64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalFixed64)
    *   [func (x *TestAllTypes) GetOptionalFloat() float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalFloat)
    *   [func (x *TestAllTypes) GetOptionalForeignEnum() ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalForeignEnum)
    *   [func (x *TestAllTypes) GetOptionalForeignMessage() *ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalForeignMessage)
    *   [func (x *TestAllTypes) GetOptionalImportEnum() ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalImportEnum)
    *   [func (x *TestAllTypes) GetOptionalImportMessage() *ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalImportMessage)
    *   [func (x *TestAllTypes) GetOptionalInt32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalInt32)
    *   [func (x *TestAllTypes) GetOptionalInt64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalInt64)
    *   [func (x *TestAllTypes) GetOptionalNestedEnum() TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalNestedEnum)
    *   [func (x *TestAllTypes) GetOptionalNestedMessage() *TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalNestedMessage)
    *   [func (x *TestAllTypes) GetOptionalSfixed32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalSfixed32)
    *   [func (x *TestAllTypes) GetOptionalSfixed64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalSfixed64)
    *   [func (x *TestAllTypes) GetOptionalSint32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalSint32)
    *   [func (x *TestAllTypes) GetOptionalSint64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalSint64)
    *   [func (x *TestAllTypes) GetOptionalString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalString)
    *   [func (x *TestAllTypes) GetOptionalUint32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalUint32)
    *   [func (x *TestAllTypes) GetOptionalUint64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalUint64)
    *   [func (x *TestAllTypes) GetOptionalgroup() *TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetOptionalgroup)
    *   [func (x *TestAllTypes) GetRepeatedBool() []bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedBool)
    *   [func (x *TestAllTypes) GetRepeatedBytes() [][]byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedBytes)
    *   [func (x *TestAllTypes) GetRepeatedDouble() []float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedDouble)
    *   [func (x *TestAllTypes) GetRepeatedFixed32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedFixed32)
    *   [func (x *TestAllTypes) GetRepeatedFixed64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedFixed64)
    *   [func (x *TestAllTypes) GetRepeatedFloat() []float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedFloat)
    *   [func (x *TestAllTypes) GetRepeatedForeignEnum() []ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedForeignEnum)
    *   [func (x *TestAllTypes) GetRepeatedForeignMessage() []*ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedForeignMessage)
    *   [func (x *TestAllTypes) GetRepeatedImportenum() []ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedImportenum)
    *   [func (x *TestAllTypes) GetRepeatedImportmessage() []*ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedImportmessage)
    *   [func (x *TestAllTypes) GetRepeatedInt32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedInt32)
    *   [func (x *TestAllTypes) GetRepeatedInt64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedInt64)
    *   [func (x *TestAllTypes) GetRepeatedNestedEnum() []TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedNestedEnum)
    *   [func (x *TestAllTypes) GetRepeatedNestedMessage() []*TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedNestedMessage)
    *   [func (x *TestAllTypes) GetRepeatedSfixed32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedSfixed32)
    *   [func (x *TestAllTypes) GetRepeatedSfixed64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedSfixed64)
    *   [func (x *TestAllTypes) GetRepeatedSint32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedSint32)
    *   [func (x *TestAllTypes) GetRepeatedSint64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedSint64)
    *   [func (x *TestAllTypes) GetRepeatedString() []string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedString)
    *   [func (x *TestAllTypes) GetRepeatedUint32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedUint32)
    *   [func (x *TestAllTypes) GetRepeatedUint64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedUint64)
    *   [func (x *TestAllTypes) GetRepeatedgroup() []*TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.GetRepeatedgroup)
    *   [func (*TestAllTypes) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.ProtoMessage)
    *   [func (x *TestAllTypes) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.ProtoReflect)
    *   [func (x *TestAllTypes) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.Reset)
    *   [func (x *TestAllTypes) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes.String)

*   [type TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum)
*       *   [func (TestAllTypes_NestedEnum) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.Descriptor)
    *   [func (x TestAllTypes_NestedEnum) Enum() *TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.Enum)
    *   [func (TestAllTypes_NestedEnum) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.EnumDescriptor)deprecated
    *   [func (x TestAllTypes_NestedEnum) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.Number)
    *   [func (x TestAllTypes_NestedEnum) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.String)
    *   [func (TestAllTypes_NestedEnum) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.Type)
    *   [func (x *TestAllTypes_NestedEnum) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum.UnmarshalJSON)deprecated

*   [type TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)
*       *   [func (*TestAllTypes_NestedMessage) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.Descriptor)deprecated
    *   [func (x *TestAllTypes_NestedMessage) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.GetA)
    *   [func (x *TestAllTypes_NestedMessage) GetCorecursive() *TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.GetCorecursive)
    *   [func (*TestAllTypes_NestedMessage) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.ProtoMessage)
    *   [func (x *TestAllTypes_NestedMessage) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.ProtoReflect)
    *   [func (x *TestAllTypes_NestedMessage) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.Reset)
    *   [func (x *TestAllTypes_NestedMessage) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage.String)

*   [type TestAllTypes_OneofBool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofBool)
*   [type TestAllTypes_OneofBytes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofBytes)
*   [type TestAllTypes_OneofDouble](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofDouble)
*   [type TestAllTypes_OneofEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofEnum)
*   [type TestAllTypes_OneofFloat](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofFloat)
*   [type TestAllTypes_OneofGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup)
*       *   [func (*TestAllTypes_OneofGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.Descriptor)deprecated
    *   [func (x *TestAllTypes_OneofGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.GetA)
    *   [func (x *TestAllTypes_OneofGroup) GetB() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.GetB)
    *   [func (*TestAllTypes_OneofGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.ProtoMessage)
    *   [func (x *TestAllTypes_OneofGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.ProtoReflect)
    *   [func (x *TestAllTypes_OneofGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.Reset)
    *   [func (x *TestAllTypes_OneofGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup.String)

*   [type TestAllTypes_OneofNestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofNestedMessage)
*   [type TestAllTypes_OneofOptionalUint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofOptionalUint32)
*   [type TestAllTypes_OneofString](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofString)
*   [type TestAllTypes_OneofUint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofUint32)
*   [type TestAllTypes_OneofUint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofUint64)
*   [type TestAllTypes_Oneofgroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_Oneofgroup)
*   [type TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup)
*       *   [func (*TestAllTypes_OptionalGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.Descriptor)deprecated
    *   [func (x *TestAllTypes_OptionalGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.GetA)
    *   [func (x *TestAllTypes_OptionalGroup) GetOptionalNestedMessage() *TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.GetOptionalNestedMessage)
    *   [func (x *TestAllTypes_OptionalGroup) GetSameFieldNumber() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.GetSameFieldNumber)
    *   [func (*TestAllTypes_OptionalGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.ProtoMessage)
    *   [func (x *TestAllTypes_OptionalGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.ProtoReflect)
    *   [func (x *TestAllTypes_OptionalGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.Reset)
    *   [func (x *TestAllTypes_OptionalGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup.String)

*   [type TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup)
*       *   [func (*TestAllTypes_RepeatedGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.Descriptor)deprecated
    *   [func (x *TestAllTypes_RepeatedGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.GetA)
    *   [func (x *TestAllTypes_RepeatedGroup) GetOptionalNestedMessage() *TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.GetOptionalNestedMessage)
    *   [func (*TestAllTypes_RepeatedGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.ProtoMessage)
    *   [func (x *TestAllTypes_RepeatedGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.ProtoReflect)
    *   [func (x *TestAllTypes_RepeatedGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.Reset)
    *   [func (x *TestAllTypes_RepeatedGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup.String)

*   [type TestDeprecatedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage)deprecated
*       *   [func (*TestDeprecatedMessage) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.Descriptor)deprecated
    *   [func (x *TestDeprecatedMessage) GetDeprecatedInt32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.GetDeprecatedInt32)deprecated
    *   [func (x *TestDeprecatedMessage) GetDeprecatedOneof() isTestDeprecatedMessage_DeprecatedOneof](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.GetDeprecatedOneof)
    *   [func (x *TestDeprecatedMessage) GetDeprecatedOneofField() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.GetDeprecatedOneofField)deprecated
    *   [func (*TestDeprecatedMessage) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.ProtoMessage)
    *   [func (x *TestDeprecatedMessage) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.ProtoReflect)
    *   [func (x *TestDeprecatedMessage) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.Reset)
    *   [func (x *TestDeprecatedMessage) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage.String)

*   [type TestDeprecatedMessage_DeprecatedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum)deprecated
*       *   [func (TestDeprecatedMessage_DeprecatedEnum) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.Descriptor)
    *   [func (x TestDeprecatedMessage_DeprecatedEnum) Enum() *TestDeprecatedMessage_DeprecatedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.Enum)
    *   [func (TestDeprecatedMessage_DeprecatedEnum) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.EnumDescriptor)deprecated
    *   [func (x TestDeprecatedMessage_DeprecatedEnum) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.Number)
    *   [func (x TestDeprecatedMessage_DeprecatedEnum) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.String)
    *   [func (TestDeprecatedMessage_DeprecatedEnum) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.Type)
    *   [func (x *TestDeprecatedMessage_DeprecatedEnum) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum.UnmarshalJSON)deprecated

*   [type TestDeprecatedMessage_DeprecatedOneofField](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedOneofField)
*   [type TestNestedExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension)
*       *   [func (*TestNestedExtension) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension.Descriptor)deprecated
    *   [func (*TestNestedExtension) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension.ProtoMessage)
    *   [func (x *TestNestedExtension) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension.ProtoReflect)
    *   [func (x *TestNestedExtension) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension.Reset)
    *   [func (x *TestNestedExtension) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension.String)

*   [type TestPackedExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions)
*       *   [func (*TestPackedExtensions) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions.Descriptor)deprecated
    *   [func (*TestPackedExtensions) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions.ProtoMessage)
    *   [func (x *TestPackedExtensions) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions.ProtoReflect)
    *   [func (x *TestPackedExtensions) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions.Reset)
    *   [func (x *TestPackedExtensions) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions.String)

*   [type TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)
*       *   [func (*TestPackedTypes) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.Descriptor)deprecated
    *   [func (x *TestPackedTypes) GetPackedBool() []bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedBool)
    *   [func (x *TestPackedTypes) GetPackedDouble() []float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedDouble)
    *   [func (x *TestPackedTypes) GetPackedEnum() []ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedEnum)
    *   [func (x *TestPackedTypes) GetPackedFixed32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedFixed32)
    *   [func (x *TestPackedTypes) GetPackedFixed64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedFixed64)
    *   [func (x *TestPackedTypes) GetPackedFloat() []float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedFloat)
    *   [func (x *TestPackedTypes) GetPackedInt32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedInt32)
    *   [func (x *TestPackedTypes) GetPackedInt64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedInt64)
    *   [func (x *TestPackedTypes) GetPackedSfixed32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedSfixed32)
    *   [func (x *TestPackedTypes) GetPackedSfixed64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedSfixed64)
    *   [func (x *TestPackedTypes) GetPackedSint32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedSint32)
    *   [func (x *TestPackedTypes) GetPackedSint64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedSint64)
    *   [func (x *TestPackedTypes) GetPackedUint32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedUint32)
    *   [func (x *TestPackedTypes) GetPackedUint64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.GetPackedUint64)
    *   [func (*TestPackedTypes) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.ProtoMessage)
    *   [func (x *TestPackedTypes) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.ProtoReflect)
    *   [func (x *TestPackedTypes) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.Reset)
    *   [func (x *TestPackedTypes) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes.String)

*   [type TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)
*       *   [func (*TestRequired) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired.Descriptor)deprecated
    *   [func (x *TestRequired) GetRequiredField() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired.GetRequiredField)
    *   [func (*TestRequired) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired.ProtoMessage)
    *   [func (x *TestRequired) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired.ProtoReflect)
    *   [func (x *TestRequired) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired.Reset)
    *   [func (x *TestRequired) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired.String)

*   [type TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)
*       *   [func (*TestRequiredForeign) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.Descriptor)deprecated
    *   [func (x *TestRequiredForeign) GetMapMessage() map[int32]*TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.GetMapMessage)
    *   [func (x *TestRequiredForeign) GetOneofField() isTestRequiredForeign_OneofField](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.GetOneofField)
    *   [func (x *TestRequiredForeign) GetOneofMessage() *TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.GetOneofMessage)
    *   [func (x *TestRequiredForeign) GetOptionalMessage() *TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.GetOptionalMessage)
    *   [func (x *TestRequiredForeign) GetRepeatedMessage() []*TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.GetRepeatedMessage)
    *   [func (*TestRequiredForeign) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.ProtoMessage)
    *   [func (x *TestRequiredForeign) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.ProtoReflect)
    *   [func (x *TestRequiredForeign) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.Reset)
    *   [func (x *TestRequiredForeign) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign.String)

*   [type TestRequiredForeign_OneofMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign_OneofMessage)
*   [type TestRequiredGroupFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields)
*       *   [func (*TestRequiredGroupFields) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.Descriptor)deprecated
    *   [func (x *TestRequiredGroupFields) GetOptionalgroup() *TestRequiredGroupFields_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.GetOptionalgroup)
    *   [func (x *TestRequiredGroupFields) GetRepeatedgroup() []*TestRequiredGroupFields_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.GetRepeatedgroup)
    *   [func (*TestRequiredGroupFields) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.ProtoMessage)
    *   [func (x *TestRequiredGroupFields) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.ProtoReflect)
    *   [func (x *TestRequiredGroupFields) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.Reset)
    *   [func (x *TestRequiredGroupFields) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields.String)

*   [type TestRequiredGroupFields_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup)
*       *   [func (*TestRequiredGroupFields_OptionalGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup.Descriptor)deprecated
    *   [func (x *TestRequiredGroupFields_OptionalGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup.GetA)
    *   [func (*TestRequiredGroupFields_OptionalGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup.ProtoMessage)
    *   [func (x *TestRequiredGroupFields_OptionalGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup.ProtoReflect)
    *   [func (x *TestRequiredGroupFields_OptionalGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup.Reset)
    *   [func (x *TestRequiredGroupFields_OptionalGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup.String)

*   [type TestRequiredGroupFields_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup)
*       *   [func (*TestRequiredGroupFields_RepeatedGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup.Descriptor)deprecated
    *   [func (x *TestRequiredGroupFields_RepeatedGroup) GetA() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup.GetA)
    *   [func (*TestRequiredGroupFields_RepeatedGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup.ProtoMessage)
    *   [func (x *TestRequiredGroupFields_RepeatedGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup.ProtoReflect)
    *   [func (x *TestRequiredGroupFields_RepeatedGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup.Reset)
    *   [func (x *TestRequiredGroupFields_RepeatedGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup.String)

*   [type TestReservedEnumFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields)
*       *   [func (TestReservedEnumFields) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.Descriptor)
    *   [func (x TestReservedEnumFields) Enum() *TestReservedEnumFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.Enum)
    *   [func (TestReservedEnumFields) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.EnumDescriptor)deprecated
    *   [func (x TestReservedEnumFields) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.Number)
    *   [func (x TestReservedEnumFields) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.String)
    *   [func (TestReservedEnumFields) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.Type)
    *   [func (x *TestReservedEnumFields) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields.UnmarshalJSON)deprecated

*   [type TestReservedFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields)
*       *   [func (*TestReservedFields) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields.Descriptor)deprecated
    *   [func (*TestReservedFields) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields.ProtoMessage)
    *   [func (x *TestReservedFields) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields.ProtoReflect)
    *   [func (x *TestReservedFields) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields.Reset)
    *   [func (x *TestReservedFields) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields.String)

*   [type TestUnpackedExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions)
*       *   [func (*TestUnpackedExtensions) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions.Descriptor)deprecated
    *   [func (*TestUnpackedExtensions) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions.ProtoMessage)
    *   [func (x *TestUnpackedExtensions) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions.ProtoReflect)
    *   [func (x *TestUnpackedExtensions) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions.Reset)
    *   [func (x *TestUnpackedExtensions) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions.String)

*   [type TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)
*       *   [func (*TestUnpackedTypes) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.Descriptor)deprecated
    *   [func (x *TestUnpackedTypes) GetUnpackedBool() []bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedBool)
    *   [func (x *TestUnpackedTypes) GetUnpackedDouble() []float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedDouble)
    *   [func (x *TestUnpackedTypes) GetUnpackedEnum() []ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedEnum)
    *   [func (x *TestUnpackedTypes) GetUnpackedFixed32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedFixed32)
    *   [func (x *TestUnpackedTypes) GetUnpackedFixed64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedFixed64)
    *   [func (x *TestUnpackedTypes) GetUnpackedFloat() []float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedFloat)
    *   [func (x *TestUnpackedTypes) GetUnpackedInt32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedInt32)
    *   [func (x *TestUnpackedTypes) GetUnpackedInt64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedInt64)
    *   [func (x *TestUnpackedTypes) GetUnpackedSfixed32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedSfixed32)
    *   [func (x *TestUnpackedTypes) GetUnpackedSfixed64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedSfixed64)
    *   [func (x *TestUnpackedTypes) GetUnpackedSint32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedSint32)
    *   [func (x *TestUnpackedTypes) GetUnpackedSint64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedSint64)
    *   [func (x *TestUnpackedTypes) GetUnpackedUint32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedUint32)
    *   [func (x *TestUnpackedTypes) GetUnpackedUint64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.GetUnpackedUint64)
    *   [func (*TestUnpackedTypes) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.ProtoMessage)
    *   [func (x *TestUnpackedTypes) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.ProtoReflect)
    *   [func (x *TestUnpackedTypes) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.Reset)
    *   [func (x *TestUnpackedTypes) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes.String)

*   [type TestWeak](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak)
*       *   [func (*TestWeak) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.Descriptor)deprecated
    *   [func (x *TestWeak) GetWeakMessage1() *weak1.WeakImportMessage1](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.GetWeakMessage1)
    *   [func (x *TestWeak) GetWeakMessage2() *weak2.WeakImportMessage2](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.GetWeakMessage2)
    *   [func (*TestWeak) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.ProtoMessage)
    *   [func (x *TestWeak) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.ProtoReflect)
    *   [func (x *TestWeak) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.Reset)
    *   [func (x *TestWeak) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak.String)

*   [type WeirdDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault)
*       *   [func (*WeirdDefault) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault.Descriptor)deprecated
    *   [func (x *WeirdDefault) GetWeirdDefault() []byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault.GetWeirdDefault)
    *   [func (*WeirdDefault) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault.ProtoMessage)
    *   [func (x *WeirdDefault) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault.ProtoReflect)
    *   [func (x *WeirdDefault) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault.Reset)
    *   [func (x *WeirdDefault) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault.String)

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L366)

const (
 Default_TestAllTypes_DefaultInt32 = [int32](https://pkg.go.dev/builtin#int32)(81)  Default_TestAllTypes_DefaultInt64 = [int64](https://pkg.go.dev/builtin#int64)(82)  Default_TestAllTypes_DefaultUint32 = [uint32](https://pkg.go.dev/builtin#uint32)(83)  Default_TestAllTypes_DefaultUint64 = [uint64](https://pkg.go.dev/builtin#uint64)(84)  Default_TestAllTypes_DefaultSint32 = [int32](https://pkg.go.dev/builtin#int32)(-85)  Default_TestAllTypes_DefaultSint64 = [int64](https://pkg.go.dev/builtin#int64)(86)  Default_TestAllTypes_DefaultFixed32 = [uint32](https://pkg.go.dev/builtin#uint32)(87)  Default_TestAllTypes_DefaultFixed64 = [uint64](https://pkg.go.dev/builtin#uint64)(88)  Default_TestAllTypes_DefaultSfixed32 = [int32](https://pkg.go.dev/builtin#int32)(89)  Default_TestAllTypes_DefaultSfixed64 = [int64](https://pkg.go.dev/builtin#int64)(-90)  Default_TestAllTypes_DefaultFloat = [float32](https://pkg.go.dev/builtin#float32)(91.5)  Default_TestAllTypes_DefaultDouble = [float64](https://pkg.go.dev/builtin#float64)(92000)  Default_TestAllTypes_DefaultBool = [bool](https://pkg.go.dev/builtin#bool)([true](https://pkg.go.dev/builtin#true))  Default_TestAllTypes_DefaultString = [string](https://pkg.go.dev/builtin#string)("hello")  Default_TestAllTypes_DefaultNestedEnum = [TestAllTypes_BAR](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_BAR) Default_TestAllTypes_DefaultForeignEnum = [ForeignEnum_FOREIGN_BAR](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum_FOREIGN_BAR))

Default values for TestAllTypes fields.

Default values for RemoteDefault fields.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L41)

var (
 ForeignEnum_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		4: "FOREIGN_FOO",
		5: "FOREIGN_BAR",
		6: "FOREIGN_BAZ",
	}
 ForeignEnum_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"FOREIGN_FOO": 4,
		"FOREIGN_BAR": 5,
		"FOREIGN_BAZ": 6,
	}
)

Enum value maps for ForeignEnum.

Enum value maps for TestReservedEnumFields.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L154)

var (
 TestAllTypes_NestedEnum_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0:  "FOO",
		1:  "BAR",
		2:  "BAZ",
		-1: "NEG",
	}
 TestAllTypes_NestedEnum_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"FOO": 0,
		"BAR": 1,
		"BAZ": 2,
		"NEG": -1,
	}
)

Enum value maps for TestAllTypes_NestedEnum.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L215)

var (
 TestDeprecatedMessage_DeprecatedEnum_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		0: "DEPRECATED",
	}
 TestDeprecatedMessage_DeprecatedEnum_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"DEPRECATED": 0,
	}
)

Enum value maps for TestDeprecatedMessage_DeprecatedEnum.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L3362)

var (
	E_OptionalInt32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[0]
	E_OptionalInt64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[1]
	E_OptionalUint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[2]
	E_OptionalUint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[3]
	E_OptionalSint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[4]
	E_OptionalSint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[5]
	E_OptionalFixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[6]
	E_OptionalFixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[7]
	E_OptionalSfixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[8]
	E_OptionalSfixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[9]
	E_OptionalFloat = &file_internal_protojson_testprotos_test_test_proto_extTypes[10]
	E_OptionalDouble = &file_internal_protojson_testprotos_test_test_proto_extTypes[11]
	E_OptionalBool = &file_internal_protojson_testprotos_test_test_proto_extTypes[12]
	E_OptionalString = &file_internal_protojson_testprotos_test_test_proto_extTypes[13]
	E_OptionalBytes = &file_internal_protojson_testprotos_test_test_proto_extTypes[14]
	E_Optionalgroup = &file_internal_protojson_testprotos_test_test_proto_extTypes[15]
	E_OptionalNestedMessage = &file_internal_protojson_testprotos_test_test_proto_extTypes[16]
	E_OptionalNestedEnum = &file_internal_protojson_testprotos_test_test_proto_extTypes[17]
	E_RepeatedInt32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[18]
	E_RepeatedInt64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[19]
	E_RepeatedUint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[20]
	E_RepeatedUint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[21]
	E_RepeatedSint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[22]
	E_RepeatedSint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[23]
	E_RepeatedFixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[24]
	E_RepeatedFixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[25]
	E_RepeatedSfixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[26]
	E_RepeatedSfixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[27]
	E_RepeatedFloat = &file_internal_protojson_testprotos_test_test_proto_extTypes[28]
	E_RepeatedDouble = &file_internal_protojson_testprotos_test_test_proto_extTypes[29]
	E_RepeatedBool = &file_internal_protojson_testprotos_test_test_proto_extTypes[30]
	E_RepeatedString = &file_internal_protojson_testprotos_test_test_proto_extTypes[31]
	E_RepeatedBytes = &file_internal_protojson_testprotos_test_test_proto_extTypes[32]
	E_Repeatedgroup = &file_internal_protojson_testprotos_test_test_proto_extTypes[33]
	E_RepeatedNestedMessage = &file_internal_protojson_testprotos_test_test_proto_extTypes[34]
	E_RepeatedNestedEnum = &file_internal_protojson_testprotos_test_test_proto_extTypes[35]
	E_DefaultInt32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[36]
	E_DefaultInt64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[37]
	E_DefaultUint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[38]
	E_DefaultUint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[39]
	E_DefaultSint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[40]
	E_DefaultSint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[41]
	E_DefaultFixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[42]
	E_DefaultFixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[43]
	E_DefaultSfixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[44]
	E_DefaultSfixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[45]
	E_DefaultFloat = &file_internal_protojson_testprotos_test_test_proto_extTypes[46]
	E_DefaultDouble = &file_internal_protojson_testprotos_test_test_proto_extTypes[47]
	E_DefaultBool = &file_internal_protojson_testprotos_test_test_proto_extTypes[48]
	E_DefaultString = &file_internal_protojson_testprotos_test_test_proto_extTypes[49]
	E_DefaultBytes = &file_internal_protojson_testprotos_test_test_proto_extTypes[50]
	E_TestNestedExtension_NestedStringExtension = &file_internal_protojson_testprotos_test_test_proto_extTypes[79]
	E_TestRequired_Single = &file_internal_protojson_testprotos_test_test_proto_extTypes[80]
	E_TestRequired_Multi = &file_internal_protojson_testprotos_test_test_proto_extTypes[81]
)

Extension fields to TestAllExtensions.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L3474)

var (
	E_PackedInt32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[51]
	E_PackedInt64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[52]
	E_PackedUint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[53]
	E_PackedUint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[54]
	E_PackedSint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[55]
	E_PackedSint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[56]
	E_PackedFixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[57]
	E_PackedFixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[58]
	E_PackedSfixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[59]
	E_PackedSfixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[60]
	E_PackedFloat = &file_internal_protojson_testprotos_test_test_proto_extTypes[61]
	E_PackedDouble = &file_internal_protojson_testprotos_test_test_proto_extTypes[62]
	E_PackedBool = &file_internal_protojson_testprotos_test_test_proto_extTypes[63]
	E_PackedEnum = &file_internal_protojson_testprotos_test_test_proto_extTypes[64]
)

Extension fields to TestPackedExtensions.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L3506)

var (
	E_UnpackedInt32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[65]
	E_UnpackedInt64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[66]
	E_UnpackedUint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[67]
	E_UnpackedUint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[68]
	E_UnpackedSint32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[69]
	E_UnpackedSint64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[70]
	E_UnpackedFixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[71]
	E_UnpackedFixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[72]
	E_UnpackedSfixed32 = &file_internal_protojson_testprotos_test_test_proto_extTypes[73]
	E_UnpackedSfixed64 = &file_internal_protojson_testprotos_test_test_proto_extTypes[74]
	E_UnpackedFloat = &file_internal_protojson_testprotos_test_test_proto_extTypes[75]
	E_UnpackedDouble = &file_internal_protojson_testprotos_test_test_proto_extTypes[76]
	E_UnpackedBool = &file_internal_protojson_testprotos_test_test_proto_extTypes[77]
	E_UnpackedEnum = &file_internal_protojson_testprotos_test_test_proto_extTypes[78]
)

Extension fields to TestUnpackedExtensions.

Enum value maps for ImportEnum.

Default values for TestAllTypes fields.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/test/test.pb.go#L2194)

var (
 Default_WeirdDefault_WeirdDefault = [][byte](https://pkg.go.dev/builtin#byte)("hello, \"world!\"\ndeadޭ\xbe\xefbeef`") )

Default values for WeirdDefault fields.

This section is empty.

type FooRequest struct {
	
}

Test that RPC services work.

Deprecated: Use FooRequest.ProtoReflect.Descriptor instead.

func (*[FooRequest](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest)) ProtoMessage()

func (x *[FooRequest](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooRequest)) Reset()

type FooResponse struct {
	
}

Deprecated: Use FooResponse.ProtoReflect.Descriptor instead.

func (*[FooResponse](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse)) ProtoMessage()

func (x *[FooResponse](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#FooResponse)) Reset()

const (
 ForeignEnum_FOREIGN_FOO [ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) = 4  ForeignEnum_FOREIGN_BAR [ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) = 5  ForeignEnum_FOREIGN_BAZ [ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) = 6 )

func (x [ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)) Enum() *[ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)

Deprecated: Use ForeignEnum.Descriptor instead.

Deprecated: Do not use.

type ForeignMessage struct {
 C *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=c" json:"c,omitempty"`  D *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=d" json:"d,omitempty"` 	
}

Deprecated: Use ForeignMessage.ProtoReflect.Descriptor instead.

func (*[ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage)) ProtoMessage()

func (x *[ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage)) Reset()

const (
 ImportEnum_IMPORT_ZERO [ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum) = 0 )

func (x [ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum)) Enum() *[ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum)

func ([ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum)) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use ImportEnum.Descriptor instead.

Deprecated: Do not use.

type ImportMessage struct {
	
}

Deprecated: Use ImportMessage.ProtoReflect.Descriptor instead.

func (*[ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage)) ProtoMessage()

func (x *[ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage)) Reset()

type OptionalGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,17,opt,name=a" json:"a,omitempty"`  SameFieldNumber *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,16,opt,name=same_field_number,json=sameFieldNumber" json:"same_field_number,omitempty"`  OptionalNestedMessage *[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage) `protobuf:"bytes,1000,opt,name=optional_nested_message,json=optionalNestedMessage" json:"optional_nested_message,omitempty"` 	
}

Deprecated: Use OptionalGroup.ProtoReflect.Descriptor instead.

func (x *[OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup)) GetOptionalNestedMessage() *[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage)

func (x *[OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup)) GetSameFieldNumber() [int32](https://pkg.go.dev/builtin#int32)

func (*[OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup)) ProtoMessage()

func (x *[OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#OptionalGroup)) Reset()

type PublicImportMessage struct {
	
}

Deprecated: Use PublicImportMessage.ProtoReflect.Descriptor instead.

func (*[PublicImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage)) ProtoMessage()

func (x *[PublicImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#PublicImportMessage)) Reset()

type RemoteDefault struct {
 Default *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,1,opt,name=default,enum=goproto.proto.enums.Enum" json:"default,omitempty"`  Zero *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,2,opt,name=zero,enum=goproto.proto.enums.Enum,def=0" json:"zero,omitempty"`  One *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,3,opt,name=one,enum=goproto.proto.enums.Enum,def=1" json:"one,omitempty"`  Elevent *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,4,opt,name=elevent,enum=goproto.proto.enums.Enum,def=11" json:"elevent,omitempty"`  Seventeen *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,5,opt,name=seventeen,enum=goproto.proto.enums.Enum,def=17" json:"seventeen,omitempty"`  Thirtyseven *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,6,opt,name=thirtyseven,enum=goproto.proto.enums.Enum,def=37" json:"thirtyseven,omitempty"`  Sixtyseven *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,7,opt,name=sixtyseven,enum=goproto.proto.enums.Enum,def=67" json:"sixtyseven,omitempty"`  Negative *[enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums).[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/enums#Enum) `protobuf:"varint,8,opt,name=negative,enum=goproto.proto.enums.Enum,def=-1" json:"negative,omitempty"` 	
}

Deprecated: Use RemoteDefault.ProtoReflect.Descriptor instead.

func (*[RemoteDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault)) ProtoMessage()

func (x *[RemoteDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RemoteDefault)) Reset()

type RepeatedGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,47,opt,name=a" json:"a,omitempty"`  OptionalNestedMessage *[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage) `protobuf:"bytes,1001,opt,name=optional_nested_message,json=optionalNestedMessage" json:"optional_nested_message,omitempty"` 	
}

Deprecated: Use RepeatedGroup.ProtoReflect.Descriptor instead.

func (x *[RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup)) GetOptionalNestedMessage() *[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage)

func (*[RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup)) ProtoMessage()

func (x *[RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#RepeatedGroup)) Reset()

type TestAllExtensions struct {
	
}

Deprecated: Use TestAllExtensions.ProtoReflect.Descriptor instead.

func (*[TestAllExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions)) ProtoMessage()

func (x *[TestAllExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions)) Reset()

type TestAllExtensions_NestedMessage struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=a" json:"a,omitempty"`  Corecursive *[TestAllExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions) `protobuf:"bytes,2,opt,name=corecursive" json:"corecursive,omitempty"` 	
}

Deprecated: Use TestAllExtensions_NestedMessage.ProtoReflect.Descriptor instead.

func (x *[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage)) GetCorecursive() *[TestAllExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions)

func (*[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage)) ProtoMessage()

func (x *[TestAllExtensions_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllExtensions_NestedMessage)) Reset()

type TestAllTypes struct {
 OptionalInt32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=optional_int32,json=optionalInt32" json:"optional_int32,omitempty"`  OptionalInt64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,2,opt,name=optional_int64,json=optionalInt64" json:"optional_int64,omitempty"`  OptionalUint32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,3,opt,name=optional_uint32,json=optionalUint32" json:"optional_uint32,omitempty"`  OptionalUint64 *[uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,4,opt,name=optional_uint64,json=optionalUint64" json:"optional_uint64,omitempty"`  OptionalSint32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"zigzag32,5,opt,name=optional_sint32,json=optionalSint32" json:"optional_sint32,omitempty"`  OptionalSint64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"zigzag64,6,opt,name=optional_sint64,json=optionalSint64" json:"optional_sint64,omitempty"`  OptionalFixed32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,7,opt,name=optional_fixed32,json=optionalFixed32" json:"optional_fixed32,omitempty"`  OptionalFixed64 *[uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,8,opt,name=optional_fixed64,json=optionalFixed64" json:"optional_fixed64,omitempty"`  OptionalSfixed32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"fixed32,9,opt,name=optional_sfixed32,json=optionalSfixed32" json:"optional_sfixed32,omitempty"`  OptionalSfixed64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,10,opt,name=optional_sfixed64,json=optionalSfixed64" json:"optional_sfixed64,omitempty"`  OptionalFloat *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,11,opt,name=optional_float,json=optionalFloat" json:"optional_float,omitempty"`  OptionalDouble *[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,12,opt,name=optional_double,json=optionalDouble" json:"optional_double,omitempty"`  OptionalBool *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,13,opt,name=optional_bool,json=optionalBool" json:"optional_bool,omitempty"`  OptionalString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,14,opt,name=optional_string,json=optionalString" json:"optional_string,omitempty"`  OptionalBytes [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,15,opt,name=optional_bytes,json=optionalBytes" json:"optional_bytes,omitempty"`  Optionalgroup *[TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup) `protobuf:"group,16,opt,name=OptionalGroup,json=optionalgroup" json:"optionalgroup,omitempty"`  OptionalNestedMessage *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage) `protobuf:"bytes,18,opt,name=optional_nested_message,json=optionalNestedMessage" json:"optional_nested_message,omitempty"`  OptionalForeignMessage *[ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage) `protobuf:"bytes,19,opt,name=optional_foreign_message,json=optionalForeignMessage" json:"optional_foreign_message,omitempty"`  OptionalImportMessage *[ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage) `protobuf:"bytes,20,opt,name=optional_import_message,json=optionalImportMessage" json:"optional_import_message,omitempty"`  OptionalNestedEnum *[TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) ``  OptionalForeignEnum *[ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) ``  OptionalImportEnum *[ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum) ``  RepeatedInt32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,31,rep,name=repeated_int32,json=repeatedInt32" json:"repeated_int32,omitempty"`  RepeatedInt64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,32,rep,name=repeated_int64,json=repeatedInt64" json:"repeated_int64,omitempty"`  RepeatedUint32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,33,rep,name=repeated_uint32,json=repeatedUint32" json:"repeated_uint32,omitempty"`  RepeatedUint64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,34,rep,name=repeated_uint64,json=repeatedUint64" json:"repeated_uint64,omitempty"`  RepeatedSint32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"zigzag32,35,rep,name=repeated_sint32,json=repeatedSint32" json:"repeated_sint32,omitempty"`  RepeatedSint64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"zigzag64,36,rep,name=repeated_sint64,json=repeatedSint64" json:"repeated_sint64,omitempty"`  RepeatedFixed32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,37,rep,name=repeated_fixed32,json=repeatedFixed32" json:"repeated_fixed32,omitempty"`  RepeatedFixed64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,38,rep,name=repeated_fixed64,json=repeatedFixed64" json:"repeated_fixed64,omitempty"`  RepeatedSfixed32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"fixed32,39,rep,name=repeated_sfixed32,json=repeatedSfixed32" json:"repeated_sfixed32,omitempty"`  RepeatedSfixed64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,40,rep,name=repeated_sfixed64,json=repeatedSfixed64" json:"repeated_sfixed64,omitempty"`  RepeatedFloat [][float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,41,rep,name=repeated_float,json=repeatedFloat" json:"repeated_float,omitempty"`  RepeatedDouble [][float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,42,rep,name=repeated_double,json=repeatedDouble" json:"repeated_double,omitempty"`  RepeatedBool [][bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,43,rep,name=repeated_bool,json=repeatedBool" json:"repeated_bool,omitempty"`  RepeatedString [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,44,rep,name=repeated_string,json=repeatedString" json:"repeated_string,omitempty"`  RepeatedBytes [][][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,45,rep,name=repeated_bytes,json=repeatedBytes" json:"repeated_bytes,omitempty"`  Repeatedgroup []*[TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup) `protobuf:"group,46,rep,name=RepeatedGroup,json=repeatedgroup" json:"repeatedgroup,omitempty"`  RepeatedNestedMessage []*[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage) `protobuf:"bytes,48,rep,name=repeated_nested_message,json=repeatedNestedMessage" json:"repeated_nested_message,omitempty"`  RepeatedForeignMessage []*[ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage) `protobuf:"bytes,49,rep,name=repeated_foreign_message,json=repeatedForeignMessage" json:"repeated_foreign_message,omitempty"`  RepeatedImportmessage []*[ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage) `protobuf:"bytes,50,rep,name=repeated_importmessage,json=repeatedImportmessage" json:"repeated_importmessage,omitempty"`  RepeatedNestedEnum [][TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) ``  RepeatedForeignEnum [][ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) ``  RepeatedImportenum [][ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum) ``  MapInt32Int32 map[[int32](https://pkg.go.dev/builtin#int32)][int32](https://pkg.go.dev/builtin#int32) ``  MapInt64Int64 map[[int64](https://pkg.go.dev/builtin#int64)][int64](https://pkg.go.dev/builtin#int64) ``  MapUint32Uint32 map[[uint32](https://pkg.go.dev/builtin#uint32)][uint32](https://pkg.go.dev/builtin#uint32) ``  MapUint64Uint64 map[[uint64](https://pkg.go.dev/builtin#uint64)][uint64](https://pkg.go.dev/builtin#uint64) ``  MapSint32Sint32 map[[int32](https://pkg.go.dev/builtin#int32)][int32](https://pkg.go.dev/builtin#int32) ``  MapSint64Sint64 map[[int64](https://pkg.go.dev/builtin#int64)][int64](https://pkg.go.dev/builtin#int64) ``  MapFixed32Fixed32 map[[uint32](https://pkg.go.dev/builtin#uint32)][uint32](https://pkg.go.dev/builtin#uint32) ``  MapFixed64Fixed64 map[[uint64](https://pkg.go.dev/builtin#uint64)][uint64](https://pkg.go.dev/builtin#uint64) ``  MapSfixed32Sfixed32 map[[int32](https://pkg.go.dev/builtin#int32)][int32](https://pkg.go.dev/builtin#int32) ``  MapSfixed64Sfixed64 map[[int64](https://pkg.go.dev/builtin#int64)][int64](https://pkg.go.dev/builtin#int64) ``  MapInt32Float map[[int32](https://pkg.go.dev/builtin#int32)][float32](https://pkg.go.dev/builtin#float32) ``  MapInt32Double map[[int32](https://pkg.go.dev/builtin#int32)][float64](https://pkg.go.dev/builtin#float64) ``  MapBoolBool map[[bool](https://pkg.go.dev/builtin#bool)][bool](https://pkg.go.dev/builtin#bool) ``  MapStringString map[[string](https://pkg.go.dev/builtin#string)][string](https://pkg.go.dev/builtin#string) ``  MapStringBytes map[[string](https://pkg.go.dev/builtin#string)][][byte](https://pkg.go.dev/builtin#byte) ``  MapStringNestedMessage map[[string](https://pkg.go.dev/builtin#string)]*[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage) ``  MapStringNestedEnum map[[string](https://pkg.go.dev/builtin#string)][TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) `` 	
 DefaultInt32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,81,opt,name=default_int32,json=defaultInt32,def=81" json:"default_int32,omitempty"`  DefaultInt64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,82,opt,name=default_int64,json=defaultInt64,def=82" json:"default_int64,omitempty"`  DefaultUint32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,83,opt,name=default_uint32,json=defaultUint32,def=83" json:"default_uint32,omitempty"`  DefaultUint64 *[uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,84,opt,name=default_uint64,json=defaultUint64,def=84" json:"default_uint64,omitempty"`  DefaultSint32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"zigzag32,85,opt,name=default_sint32,json=defaultSint32,def=-85" json:"default_sint32,omitempty"`  DefaultSint64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"zigzag64,86,opt,name=default_sint64,json=defaultSint64,def=86" json:"default_sint64,omitempty"`  DefaultFixed32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,87,opt,name=default_fixed32,json=defaultFixed32,def=87" json:"default_fixed32,omitempty"`  DefaultFixed64 *[uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,88,opt,name=default_fixed64,json=defaultFixed64,def=88" json:"default_fixed64,omitempty"`  DefaultSfixed32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"fixed32,89,opt,name=default_sfixed32,json=defaultSfixed32,def=89" json:"default_sfixed32,omitempty"`  DefaultSfixed64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,80,opt,name=default_sfixed64,json=defaultSfixed64,def=-90" json:"default_sfixed64,omitempty"`  DefaultFloat *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,91,opt,name=default_float,json=defaultFloat,def=91.5" json:"default_float,omitempty"`  DefaultDouble *[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,92,opt,name=default_double,json=defaultDouble,def=92000" json:"default_double,omitempty"`  DefaultBool *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,93,opt,name=default_bool,json=defaultBool,def=1" json:"default_bool,omitempty"`  DefaultString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,94,opt,name=default_string,json=defaultString,def=hello" json:"default_string,omitempty"`  DefaultBytes [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,95,opt,name=default_bytes,json=defaultBytes,def=world" json:"default_bytes,omitempty"`  DefaultNestedEnum *[TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) ``  DefaultForeignEnum *[ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) `` 	
	
	
	
	
	
	
	
	
	
	
	OneofField isTestAllTypes_OneofField `protobuf_oneof:"oneof_field"`
	
	
	
	
	OneofOptional isTestAllTypes_OneofOptional `protobuf_oneof:"oneof_optional"`
	
}

Deprecated: Use TestAllTypes.ProtoReflect.Descriptor instead.

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultBool() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultBytes() [][byte](https://pkg.go.dev/builtin#byte)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultFixed32() [uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultFixed64() [uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultForeignEnum() [ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultInt32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultInt64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultNestedEnum() [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultSfixed32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultSfixed64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultSint32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultSint64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultString() [string](https://pkg.go.dev/builtin#string)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultUint32() [uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetDefaultUint64() [uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetMapStringNestedMessage() map[[string](https://pkg.go.dev/builtin#string)]*[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofBool() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofBytes() [][byte](https://pkg.go.dev/builtin#byte)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofEnum() [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofField() isTestAllTypes_OneofField

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofNestedMessage() *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofOptional() isTestAllTypes_OneofOptional

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofOptionalUint32() [uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOneofgroup() *[TestAllTypes_OneofGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalBool() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalBytes() [][byte](https://pkg.go.dev/builtin#byte)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalFixed32() [uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalFixed64() [uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalForeignEnum() [ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalForeignMessage() *[ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalImportEnum() [ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalImportMessage() *[ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalInt32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalInt64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalNestedEnum() [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalNestedMessage() *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalSfixed32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalSfixed64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalSint32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalSint64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalString() [string](https://pkg.go.dev/builtin#string)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalUint32() [uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalUint64() [uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetOptionalgroup() *[TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedBool() [][bool](https://pkg.go.dev/builtin#bool)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedBytes() [][][byte](https://pkg.go.dev/builtin#byte)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedFixed32() [][uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedFixed64() [][uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedForeignEnum() [][ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedForeignMessage() []*[ForeignMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedImportenum() [][ImportEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedImportmessage() []*[ImportMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ImportMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedInt32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedInt64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedNestedEnum() [][TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedNestedMessage() []*[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedSfixed32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedSfixed64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedSint32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedSint64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedString() [][string](https://pkg.go.dev/builtin#string)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedUint32() [][uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedUint64() [][uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) GetRepeatedgroup() []*[TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup)

func (*[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) ProtoMessage()

func (x *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)) Reset()

type TestAllTypes_NestedEnum [int32](https://pkg.go.dev/builtin#int32)

const (
 TestAllTypes_FOO [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) = 0  TestAllTypes_BAR [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) = 1  TestAllTypes_BAZ [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) = 2  TestAllTypes_NEG [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) = -1 )

Deprecated: Use TestAllTypes_NestedEnum.Descriptor instead.

Deprecated: Do not use.

type TestAllTypes_NestedMessage struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=a" json:"a,omitempty"`  Corecursive *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes) `protobuf:"bytes,2,opt,name=corecursive" json:"corecursive,omitempty"` 	
}

Deprecated: Use TestAllTypes_NestedMessage.ProtoReflect.Descriptor instead.

func (x *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)) GetCorecursive() *[TestAllTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes)

func (*[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)) ProtoMessage()

func (x *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)) Reset()

type TestAllTypes_OneofBool struct {
 OneofBool [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,115,opt,name=oneof_bool,json=oneofBool,oneof"` }

type TestAllTypes_OneofBytes struct {
 OneofBytes [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,114,opt,name=oneof_bytes,json=oneofBytes,oneof"` }

type TestAllTypes_OneofDouble struct {
 OneofDouble [float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,118,opt,name=oneof_double,json=oneofDouble,oneof"` }

type TestAllTypes_OneofEnum struct {
 OneofEnum [TestAllTypes_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedEnum) `protobuf:"varint,119,opt,name=oneof_enum,json=oneofEnum,enum=goproto.proto.test.TestAllTypes_NestedEnum,oneof"` }

type TestAllTypes_OneofFloat struct {
 OneofFloat [float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,117,opt,name=oneof_float,json=oneofFloat,oneof"` }

type TestAllTypes_OneofGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=a" json:"a,omitempty"`  B *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=b" json:"b,omitempty"` 	
}

Deprecated: Use TestAllTypes_OneofGroup.ProtoReflect.Descriptor instead.

func (*[TestAllTypes_OneofGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup)) ProtoMessage()

func (x *[TestAllTypes_OneofGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup)) Reset()

type TestAllTypes_OneofNestedMessage struct {
 OneofNestedMessage *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage) `protobuf:"bytes,112,opt,name=oneof_nested_message,json=oneofNestedMessage,oneof"` }

type TestAllTypes_OneofOptionalUint32 struct {
 OneofOptionalUint32 [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,120,opt,name=oneof_optional_uint32,json=oneofOptionalUint32,oneof"` }

type TestAllTypes_OneofString struct {
 OneofString [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,113,opt,name=oneof_string,json=oneofString,oneof"` }

type TestAllTypes_OneofUint32 struct {
 OneofUint32 [uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,111,opt,name=oneof_uint32,json=oneofUint32,oneof"` }

type TestAllTypes_OneofUint64 struct {
 OneofUint64 [uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,116,opt,name=oneof_uint64,json=oneofUint64,oneof"` }

type TestAllTypes_Oneofgroup struct {
 Oneofgroup *[TestAllTypes_OneofGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OneofGroup) `protobuf:"group,121,opt,name=OneofGroup,json=oneofgroup,oneof"` }

type TestAllTypes_OptionalGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,17,opt,name=a" json:"a,omitempty"`  OptionalNestedMessage *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage) `protobuf:"bytes,1000,opt,name=optional_nested_message,json=optionalNestedMessage" json:"optional_nested_message,omitempty"`  SameFieldNumber *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,16,opt,name=same_field_number,json=sameFieldNumber" json:"same_field_number,omitempty"` 	
}

Deprecated: Use TestAllTypes_OptionalGroup.ProtoReflect.Descriptor instead.

func (x *[TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup)) GetOptionalNestedMessage() *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)

func (*[TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup)) ProtoMessage()

func (x *[TestAllTypes_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_OptionalGroup)) Reset()

type TestAllTypes_RepeatedGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,47,opt,name=a" json:"a,omitempty"`  OptionalNestedMessage *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage) `protobuf:"bytes,1001,opt,name=optional_nested_message,json=optionalNestedMessage" json:"optional_nested_message,omitempty"` 	
}

Deprecated: Use TestAllTypes_RepeatedGroup.ProtoReflect.Descriptor instead.

func (x *[TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup)) GetOptionalNestedMessage() *[TestAllTypes_NestedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_NestedMessage)

func (*[TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup)) ProtoMessage()

func (x *[TestAllTypes_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestAllTypes_RepeatedGroup)) Reset()

type TestDeprecatedMessage struct {

	DeprecatedInt32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=deprecated_int32,json=deprecatedInt32" json:"deprecated_int32,omitempty"`
	
	
	DeprecatedOneof isTestDeprecatedMessage_DeprecatedOneof `protobuf_oneof:"deprecated_oneof"`
	
}

Deprecated: Marked as deprecated in internal/protojson/testprotos/test/test.proto.

Deprecated: Use TestDeprecatedMessage.ProtoReflect.Descriptor instead.

func (x *[TestDeprecatedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage)) GetDeprecatedInt32() [int32](https://pkg.go.dev/builtin#int32)

Deprecated: Marked as deprecated in internal/protojson/testprotos/test/test.proto.

func (x *[TestDeprecatedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage)) GetDeprecatedOneof() isTestDeprecatedMessage_DeprecatedOneof

func (x *[TestDeprecatedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage)) GetDeprecatedOneofField() [int32](https://pkg.go.dev/builtin#int32)

Deprecated: Marked as deprecated in internal/protojson/testprotos/test/test.proto.

func (*[TestDeprecatedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage)) ProtoMessage()

func (x *[TestDeprecatedMessage](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage)) Reset()

type TestDeprecatedMessage_DeprecatedEnum [int32](https://pkg.go.dev/builtin#int32)

Deprecated: Marked as deprecated in internal/protojson/testprotos/test/test.proto.

const (
	TestDeprecatedMessage_DEPRECATED [TestDeprecatedMessage_DeprecatedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestDeprecatedMessage_DeprecatedEnum) = 0
)

Deprecated: Use TestDeprecatedMessage_DeprecatedEnum.Descriptor instead.

Deprecated: Do not use.

type TestDeprecatedMessage_DeprecatedOneofField struct {
	DeprecatedOneofField [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=deprecated_oneof_field,json=deprecatedOneofField,oneof"`
}

type TestNestedExtension struct {
	
}

Deprecated: Use TestNestedExtension.ProtoReflect.Descriptor instead.

func (*[TestNestedExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension)) ProtoMessage()

func (x *[TestNestedExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestNestedExtension)) Reset()

type TestPackedExtensions struct {
	
}

Deprecated: Use TestPackedExtensions.ProtoReflect.Descriptor instead.

func (*[TestPackedExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions)) ProtoMessage()

func (x *[TestPackedExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedExtensions)) Reset()

type TestPackedTypes struct {
 PackedInt32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,90,rep,packed,name=packed_int32,json=packedInt32" json:"packed_int32,omitempty"`  PackedInt64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,91,rep,packed,name=packed_int64,json=packedInt64" json:"packed_int64,omitempty"`  PackedUint32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,92,rep,packed,name=packed_uint32,json=packedUint32" json:"packed_uint32,omitempty"`  PackedUint64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,93,rep,packed,name=packed_uint64,json=packedUint64" json:"packed_uint64,omitempty"`  PackedSint32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"zigzag32,94,rep,packed,name=packed_sint32,json=packedSint32" json:"packed_sint32,omitempty"`  PackedSint64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"zigzag64,95,rep,packed,name=packed_sint64,json=packedSint64" json:"packed_sint64,omitempty"`  PackedFixed32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,96,rep,packed,name=packed_fixed32,json=packedFixed32" json:"packed_fixed32,omitempty"`  PackedFixed64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,97,rep,packed,name=packed_fixed64,json=packedFixed64" json:"packed_fixed64,omitempty"`  PackedSfixed32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"fixed32,98,rep,packed,name=packed_sfixed32,json=packedSfixed32" json:"packed_sfixed32,omitempty"`  PackedSfixed64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,99,rep,packed,name=packed_sfixed64,json=packedSfixed64" json:"packed_sfixed64,omitempty"`  PackedFloat [][float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,100,rep,packed,name=packed_float,json=packedFloat" json:"packed_float,omitempty"`  PackedDouble [][float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,101,rep,packed,name=packed_double,json=packedDouble" json:"packed_double,omitempty"`  PackedBool [][bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,102,rep,packed,name=packed_bool,json=packedBool" json:"packed_bool,omitempty"`  PackedEnum [][ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) `` 	
}

Deprecated: Use TestPackedTypes.ProtoReflect.Descriptor instead.

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedBool() [][bool](https://pkg.go.dev/builtin#bool)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedEnum() [][ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedFixed32() [][uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedFixed64() [][uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedInt32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedInt64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedSfixed32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedSfixed64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedSint32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) GetPackedSint64() [][int64](https://pkg.go.dev/builtin#int64)

func (*[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) ProtoMessage()

func (x *[TestPackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestPackedTypes)) Reset()

type TestRequired struct {
 RequiredField *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,req,name=required_field,json=requiredField" json:"required_field,omitempty"` 	
}

Deprecated: Use TestRequired.ProtoReflect.Descriptor instead.

func (x *[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)) GetRequiredField() [int32](https://pkg.go.dev/builtin#int32)

func (*[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)) ProtoMessage()

func (x *[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)) Reset()

type TestRequiredForeign struct {
 OptionalMessage *[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired) `protobuf:"bytes,1,opt,name=optional_message,json=optionalMessage" json:"optional_message,omitempty"`  RepeatedMessage []*[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired) `protobuf:"bytes,2,rep,name=repeated_message,json=repeatedMessage" json:"repeated_message,omitempty"`  MapMessage map[[int32](https://pkg.go.dev/builtin#int32)]*[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired) `` 	
	
	OneofField isTestRequiredForeign_OneofField `protobuf_oneof:"oneof_field"`
	
}

Deprecated: Use TestRequiredForeign.ProtoReflect.Descriptor instead.

func (x *[TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)) GetOneofField() isTestRequiredForeign_OneofField

func (x *[TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)) GetOneofMessage() *[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)

func (x *[TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)) GetOptionalMessage() *[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)

func (x *[TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)) GetRepeatedMessage() []*[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired)

func (*[TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)) ProtoMessage()

func (x *[TestRequiredForeign](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredForeign)) Reset()

type TestRequiredForeign_OneofMessage struct {
 OneofMessage *[TestRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequired) `protobuf:"bytes,4,opt,name=oneof_message,json=oneofMessage,oneof"` }

type TestRequiredGroupFields struct {
 Optionalgroup *[TestRequiredGroupFields_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup) `protobuf:"group,1,opt,name=OptionalGroup,json=optionalgroup" json:"optionalgroup,omitempty"`  Repeatedgroup []*[TestRequiredGroupFields_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup) `protobuf:"group,3,rep,name=RepeatedGroup,json=repeatedgroup" json:"repeatedgroup,omitempty"` 	
}

Deprecated: Use TestRequiredGroupFields.ProtoReflect.Descriptor instead.

func (x *[TestRequiredGroupFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields)) GetOptionalgroup() *[TestRequiredGroupFields_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup)

func (x *[TestRequiredGroupFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields)) GetRepeatedgroup() []*[TestRequiredGroupFields_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup)

func (*[TestRequiredGroupFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields)) ProtoMessage()

func (x *[TestRequiredGroupFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields)) Reset()

type TestRequiredGroupFields_OptionalGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,req,name=a" json:"a,omitempty"` 	
}

Deprecated: Use TestRequiredGroupFields_OptionalGroup.ProtoReflect.Descriptor instead.

func (*[TestRequiredGroupFields_OptionalGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_OptionalGroup)) ProtoMessage()

type TestRequiredGroupFields_RepeatedGroup struct {
 A *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,4,req,name=a" json:"a,omitempty"` 	
}

Deprecated: Use TestRequiredGroupFields_RepeatedGroup.ProtoReflect.Descriptor instead.

func (*[TestRequiredGroupFields_RepeatedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestRequiredGroupFields_RepeatedGroup)) ProtoMessage()

type TestReservedEnumFields [int32](https://pkg.go.dev/builtin#int32)

const (
 TestReservedEnumFields_RESERVED_ENUM [TestReservedEnumFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedEnumFields) = 0 )

Deprecated: Use TestReservedEnumFields.Descriptor instead.

Deprecated: Do not use.

type TestReservedFields struct {
	
}

Deprecated: Use TestReservedFields.ProtoReflect.Descriptor instead.

func (*[TestReservedFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields)) ProtoMessage()

func (x *[TestReservedFields](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestReservedFields)) Reset()

type TestUnpackedExtensions struct {
	
}

Deprecated: Use TestUnpackedExtensions.ProtoReflect.Descriptor instead.

func (*[TestUnpackedExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions)) ProtoMessage()

func (x *[TestUnpackedExtensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedExtensions)) Reset()

type TestUnpackedTypes struct {
 UnpackedInt32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,90,rep,name=unpacked_int32,json=unpackedInt32" json:"unpacked_int32,omitempty"`  UnpackedInt64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,91,rep,name=unpacked_int64,json=unpackedInt64" json:"unpacked_int64,omitempty"`  UnpackedUint32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,92,rep,name=unpacked_uint32,json=unpackedUint32" json:"unpacked_uint32,omitempty"`  UnpackedUint64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,93,rep,name=unpacked_uint64,json=unpackedUint64" json:"unpacked_uint64,omitempty"`  UnpackedSint32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"zigzag32,94,rep,name=unpacked_sint32,json=unpackedSint32" json:"unpacked_sint32,omitempty"`  UnpackedSint64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"zigzag64,95,rep,name=unpacked_sint64,json=unpackedSint64" json:"unpacked_sint64,omitempty"`  UnpackedFixed32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,96,rep,name=unpacked_fixed32,json=unpackedFixed32" json:"unpacked_fixed32,omitempty"`  UnpackedFixed64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,97,rep,name=unpacked_fixed64,json=unpackedFixed64" json:"unpacked_fixed64,omitempty"`  UnpackedSfixed32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"fixed32,98,rep,name=unpacked_sfixed32,json=unpackedSfixed32" json:"unpacked_sfixed32,omitempty"`  UnpackedSfixed64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,99,rep,name=unpacked_sfixed64,json=unpackedSfixed64" json:"unpacked_sfixed64,omitempty"`  UnpackedFloat [][float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,100,rep,name=unpacked_float,json=unpackedFloat" json:"unpacked_float,omitempty"`  UnpackedDouble [][float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,101,rep,name=unpacked_double,json=unpackedDouble" json:"unpacked_double,omitempty"`  UnpackedBool [][bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,102,rep,name=unpacked_bool,json=unpackedBool" json:"unpacked_bool,omitempty"`  UnpackedEnum [][ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum) `` 	
}

Deprecated: Use TestUnpackedTypes.ProtoReflect.Descriptor instead.

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedBool() [][bool](https://pkg.go.dev/builtin#bool)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedEnum() [][ForeignEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#ForeignEnum)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedFixed32() [][uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedFixed64() [][uint64](https://pkg.go.dev/builtin#uint64)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedInt32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedInt64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedSfixed32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedSfixed64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedSint32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedSint64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedUint32() [][uint32](https://pkg.go.dev/builtin#uint32)

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) GetUnpackedUint64() [][uint64](https://pkg.go.dev/builtin#uint64)

func (*[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) ProtoMessage()

func (x *[TestUnpackedTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestUnpackedTypes)) Reset()

type TestWeak struct {
 WeakMessage1 *[weak1](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test/weak1).[WeakImportMessage1](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test/weak1#WeakImportMessage1) `protobuf:"bytes,1,opt,name=weak_message1,json=weakMessage1" json:"weak_message1,omitempty"`  WeakMessage2 *[weak2](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test/weak2).[WeakImportMessage2](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test/weak2#WeakImportMessage2) `protobuf:"bytes,2,opt,name=weak_message2,json=weakMessage2" json:"weak_message2,omitempty"` 	
}

Deprecated: Use TestWeak.ProtoReflect.Descriptor instead.

func (*[TestWeak](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak)) ProtoMessage()

func (x *[TestWeak](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#TestWeak)) Reset()

type WeirdDefault struct {
 WeirdDefault [][byte](https://pkg.go.dev/builtin#byte) `` 	
}

Deprecated: Use WeirdDefault.ProtoReflect.Descriptor instead.

func (x *[WeirdDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault)) GetWeirdDefault() [][byte](https://pkg.go.dev/builtin#byte)

func (*[WeirdDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault)) ProtoMessage()

func (x *[WeirdDefault](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/test#WeirdDefault)) Reset()
