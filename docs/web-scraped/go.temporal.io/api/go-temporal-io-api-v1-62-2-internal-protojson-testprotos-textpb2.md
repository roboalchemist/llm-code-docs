# Source: https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2

Title: textpb2 package - go.temporal.io/api/internal/protojson/testprotos/textpb2 - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2

Markdown Content:
*   [Variables](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#pkg-variables)
*   [type Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)
*       *   [func (Enum) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.Descriptor)
    *   [func (x Enum) Enum() *Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.Enum)
    *   [func (Enum) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.EnumDescriptor)deprecated
    *   [func (x Enum) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.Number)
    *   [func (x Enum) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.String)
    *   [func (Enum) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.Type)
    *   [func (x *Enum) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum.UnmarshalJSON)deprecated

*   [type Enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums)
*       *   [func (*Enums) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.Descriptor)deprecated
    *   [func (x *Enums) GetOptEnum() Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.GetOptEnum)
    *   [func (x *Enums) GetOptNestedEnum() Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.GetOptNestedEnum)
    *   [func (x *Enums) GetRptEnum() []Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.GetRptEnum)
    *   [func (x *Enums) GetRptNestedEnum() []Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.GetRptNestedEnum)
    *   [func (*Enums) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.ProtoMessage)
    *   [func (x *Enums) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.ProtoReflect)
    *   [func (x *Enums) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.Reset)
    *   [func (x *Enums) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums.String)

*   [type Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum)
*       *   [func (Enums_NestedEnum) Descriptor() protoreflect.EnumDescriptor](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.Descriptor)
    *   [func (x Enums_NestedEnum) Enum() *Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.Enum)
    *   [func (Enums_NestedEnum) EnumDescriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.EnumDescriptor)deprecated
    *   [func (x Enums_NestedEnum) Number() protoreflect.EnumNumber](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.Number)
    *   [func (x Enums_NestedEnum) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.String)
    *   [func (Enums_NestedEnum) Type() protoreflect.EnumType](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.Type)
    *   [func (x *Enums_NestedEnum) UnmarshalJSON(b []byte) error](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum.UnmarshalJSON)deprecated

*   [type Extensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions)
*       *   [func (*Extensions) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.Descriptor)deprecated
    *   [func (x *Extensions) GetOptBool() bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.GetOptBool)
    *   [func (x *Extensions) GetOptInt32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.GetOptInt32)
    *   [func (x *Extensions) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.GetOptString)
    *   [func (*Extensions) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.ProtoMessage)
    *   [func (x *Extensions) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.ProtoReflect)
    *   [func (x *Extensions) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.Reset)
    *   [func (x *Extensions) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions.String)

*   [type ExtensionsContainer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer)
*       *   [func (*ExtensionsContainer) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer.Descriptor)deprecated
    *   [func (*ExtensionsContainer) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer.ProtoMessage)
    *   [func (x *ExtensionsContainer) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer.ProtoReflect)
    *   [func (x *ExtensionsContainer) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer.Reset)
    *   [func (x *ExtensionsContainer) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer.String)

*   [type FakeMessageSet](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet)
*       *   [func (*FakeMessageSet) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet.Descriptor)deprecated
    *   [func (*FakeMessageSet) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet.ProtoMessage)
    *   [func (x *FakeMessageSet) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet.ProtoReflect)
    *   [func (x *FakeMessageSet) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet.Reset)
    *   [func (x *FakeMessageSet) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet.String)

*   [type FakeMessageSetExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension)
*       *   [func (*FakeMessageSetExtension) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension.Descriptor)deprecated
    *   [func (x *FakeMessageSetExtension) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension.GetOptString)
    *   [func (*FakeMessageSetExtension) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension.ProtoMessage)
    *   [func (x *FakeMessageSetExtension) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension.ProtoReflect)
    *   [func (x *FakeMessageSetExtension) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension.Reset)
    *   [func (x *FakeMessageSetExtension) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension.String)

*   [type IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)
*       *   [func (*IndirectRequired) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.Descriptor)deprecated
    *   [func (x *IndirectRequired) GetOneofNested() *NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.GetOneofNested)
    *   [func (x *IndirectRequired) GetOptNested() *NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.GetOptNested)
    *   [func (x *IndirectRequired) GetRptNested() []*NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.GetRptNested)
    *   [func (x *IndirectRequired) GetStrToNested() map[string]*NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.GetStrToNested)
    *   [func (m *IndirectRequired) GetUnion() isIndirectRequired_Union](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.GetUnion)
    *   [func (*IndirectRequired) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.ProtoMessage)
    *   [func (x *IndirectRequired) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.ProtoReflect)
    *   [func (x *IndirectRequired) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.Reset)
    *   [func (x *IndirectRequired) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired.String)

*   [type IndirectRequired_OneofNested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired_OneofNested)
*   [type KnownTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes)
*       *   [func (*KnownTypes) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.Descriptor)deprecated
    *   [func (x *KnownTypes) GetOptAny() *anypb.Any](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptAny)
    *   [func (x *KnownTypes) GetOptBool() *wrapperspb.BoolValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptBool)
    *   [func (x *KnownTypes) GetOptBytes() *wrapperspb.BytesValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptBytes)
    *   [func (x *KnownTypes) GetOptDouble() *wrapperspb.DoubleValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptDouble)
    *   [func (x *KnownTypes) GetOptDuration() *durationpb.Duration](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptDuration)
    *   [func (x *KnownTypes) GetOptEmpty() *emptypb.Empty](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptEmpty)
    *   [func (x *KnownTypes) GetOptFieldmask() *fieldmaskpb.FieldMask](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptFieldmask)
    *   [func (x *KnownTypes) GetOptFloat() *wrapperspb.FloatValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptFloat)
    *   [func (x *KnownTypes) GetOptInt32() *wrapperspb.Int32Value](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptInt32)
    *   [func (x *KnownTypes) GetOptInt64() *wrapperspb.Int64Value](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptInt64)
    *   [func (x *KnownTypes) GetOptList() *structpb.ListValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptList)
    *   [func (x *KnownTypes) GetOptNull() structpb.NullValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptNull)
    *   [func (x *KnownTypes) GetOptString() *wrapperspb.StringValue](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptString)
    *   [func (x *KnownTypes) GetOptStruct() *structpb.Struct](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptStruct)
    *   [func (x *KnownTypes) GetOptTimestamp() *timestamppb.Timestamp](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptTimestamp)
    *   [func (x *KnownTypes) GetOptUint32() *wrapperspb.UInt32Value](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptUint32)
    *   [func (x *KnownTypes) GetOptUint64() *wrapperspb.UInt64Value](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptUint64)
    *   [func (x *KnownTypes) GetOptValue() *structpb.Value](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.GetOptValue)
    *   [func (*KnownTypes) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.ProtoMessage)
    *   [func (x *KnownTypes) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.ProtoReflect)
    *   [func (x *KnownTypes) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.Reset)
    *   [func (x *KnownTypes) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes.String)

*   [type Maps](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps)
*       *   [func (*Maps) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.Descriptor)deprecated
    *   [func (x *Maps) GetInt32ToStr() map[int32]string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.GetInt32ToStr)
    *   [func (x *Maps) GetStrToNested() map[string]*Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.GetStrToNested)
    *   [func (*Maps) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.ProtoMessage)
    *   [func (x *Maps) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.ProtoReflect)
    *   [func (x *Maps) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.Reset)
    *   [func (x *Maps) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps.String)

*   [type MessageSet](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet)
*       *   [func (*MessageSet) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet.Descriptor)deprecated
    *   [func (*MessageSet) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet.ProtoMessage)
    *   [func (x *MessageSet) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet.ProtoReflect)
    *   [func (x *MessageSet) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet.Reset)
    *   [func (x *MessageSet) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet.String)

*   [type MessageSetExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension)
*       *   [func (*MessageSetExtension) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension.Descriptor)deprecated
    *   [func (x *MessageSetExtension) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension.GetOptString)
    *   [func (*MessageSetExtension) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension.ProtoMessage)
    *   [func (x *MessageSetExtension) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension.ProtoReflect)
    *   [func (x *MessageSetExtension) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension.Reset)
    *   [func (x *MessageSetExtension) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension.String)

*   [type Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)
*       *   [func (*Nested) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.Descriptor)deprecated
    *   [func (x *Nested) GetOptNested() *Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.GetOptNested)
    *   [func (x *Nested) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.GetOptString)
    *   [func (*Nested) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.ProtoMessage)
    *   [func (x *Nested) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.ProtoReflect)
    *   [func (x *Nested) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.Reset)
    *   [func (x *Nested) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested.String)

*   [type NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired)
*       *   [func (*NestedWithRequired) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired.Descriptor)deprecated
    *   [func (x *NestedWithRequired) GetReqString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired.GetReqString)
    *   [func (*NestedWithRequired) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired.ProtoMessage)
    *   [func (x *NestedWithRequired) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired.ProtoReflect)
    *   [func (x *NestedWithRequired) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired.Reset)
    *   [func (x *NestedWithRequired) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired.String)

*   [type Nests](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests)
*       *   [func (*Nests) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.Descriptor)deprecated
    *   [func (x *Nests) GetOptNested() *Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.GetOptNested)
    *   [func (x *Nests) GetOptgroup() *Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.GetOptgroup)
    *   [func (x *Nests) GetRptNested() []*Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.GetRptNested)
    *   [func (x *Nests) GetRptgroup() []*Nests_RptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.GetRptgroup)
    *   [func (*Nests) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.ProtoMessage)
    *   [func (x *Nests) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.ProtoReflect)
    *   [func (x *Nests) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.Reset)
    *   [func (x *Nests) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests.String)

*   [type Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup)
*       *   [func (*Nests_OptGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.Descriptor)deprecated
    *   [func (x *Nests_OptGroup) GetOptNested() *Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.GetOptNested)
    *   [func (x *Nests_OptGroup) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.GetOptString)
    *   [func (x *Nests_OptGroup) GetOptnestedgroup() *Nests_OptGroup_OptNestedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.GetOptnestedgroup)
    *   [func (*Nests_OptGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.ProtoMessage)
    *   [func (x *Nests_OptGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.ProtoReflect)
    *   [func (x *Nests_OptGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.Reset)
    *   [func (x *Nests_OptGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup.String)

*   [type Nests_OptGroup_OptNestedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup)
*       *   [func (*Nests_OptGroup_OptNestedGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup.Descriptor)deprecated
    *   [func (x *Nests_OptGroup_OptNestedGroup) GetOptFixed32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup.GetOptFixed32)
    *   [func (*Nests_OptGroup_OptNestedGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup.ProtoMessage)
    *   [func (x *Nests_OptGroup_OptNestedGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup.ProtoReflect)
    *   [func (x *Nests_OptGroup_OptNestedGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup.Reset)
    *   [func (x *Nests_OptGroup_OptNestedGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup.String)

*   [type Nests_RptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup)
*       *   [func (*Nests_RptGroup) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup.Descriptor)deprecated
    *   [func (x *Nests_RptGroup) GetRptString() []string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup.GetRptString)
    *   [func (*Nests_RptGroup) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup.ProtoMessage)
    *   [func (x *Nests_RptGroup) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup.ProtoReflect)
    *   [func (x *Nests_RptGroup) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup.Reset)
    *   [func (x *Nests_RptGroup) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup.String)

*   [type PartialRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired)
*       *   [func (*PartialRequired) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.Descriptor)deprecated
    *   [func (x *PartialRequired) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.GetOptString)
    *   [func (x *PartialRequired) GetReqString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.GetReqString)
    *   [func (*PartialRequired) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.ProtoMessage)
    *   [func (x *PartialRequired) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.ProtoReflect)
    *   [func (x *PartialRequired) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.Reset)
    *   [func (x *PartialRequired) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired.String)

*   [type Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)
*       *   [func (*Repeats) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.Descriptor)deprecated
    *   [func (x *Repeats) GetRptBool() []bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptBool)
    *   [func (x *Repeats) GetRptBytes() [][]byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptBytes)
    *   [func (x *Repeats) GetRptDouble() []float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptDouble)
    *   [func (x *Repeats) GetRptFloat() []float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptFloat)
    *   [func (x *Repeats) GetRptInt32() []int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptInt32)
    *   [func (x *Repeats) GetRptInt64() []int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptInt64)
    *   [func (x *Repeats) GetRptString() []string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptString)
    *   [func (x *Repeats) GetRptUint32() []uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptUint32)
    *   [func (x *Repeats) GetRptUint64() []uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.GetRptUint64)
    *   [func (*Repeats) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.ProtoMessage)
    *   [func (x *Repeats) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.ProtoReflect)
    *   [func (x *Repeats) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.Reset)
    *   [func (x *Repeats) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats.String)

*   [type Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)
*       *   [func (*Requireds) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.Descriptor)deprecated
    *   [func (x *Requireds) GetReqBool() bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.GetReqBool)
    *   [func (x *Requireds) GetReqDouble() float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.GetReqDouble)
    *   [func (x *Requireds) GetReqEnum() Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.GetReqEnum)
    *   [func (x *Requireds) GetReqNested() *Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.GetReqNested)
    *   [func (x *Requireds) GetReqSfixed64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.GetReqSfixed64)
    *   [func (x *Requireds) GetReqString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.GetReqString)
    *   [func (*Requireds) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.ProtoMessage)
    *   [func (x *Requireds) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.ProtoReflect)
    *   [func (x *Requireds) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.Reset)
    *   [func (x *Requireds) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds.String)

*   [type Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)
*       *   [func (*Scalars) Descriptor() ([]byte, []int)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.Descriptor)deprecated
    *   [func (x *Scalars) GetOptBool() bool](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptBool)
    *   [func (x *Scalars) GetOptBytes() []byte](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptBytes)
    *   [func (x *Scalars) GetOptDouble() float64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptDouble)
    *   [func (x *Scalars) GetOptFixed32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptFixed32)
    *   [func (x *Scalars) GetOptFixed64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptFixed64)
    *   [func (x *Scalars) GetOptFloat() float32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptFloat)
    *   [func (x *Scalars) GetOptInt32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptInt32)
    *   [func (x *Scalars) GetOptInt64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptInt64)
    *   [func (x *Scalars) GetOptSfixed32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptSfixed32)
    *   [func (x *Scalars) GetOptSfixed64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptSfixed64)
    *   [func (x *Scalars) GetOptSint32() int32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptSint32)
    *   [func (x *Scalars) GetOptSint64() int64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptSint64)
    *   [func (x *Scalars) GetOptString() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptString)
    *   [func (x *Scalars) GetOptUint32() uint32](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptUint32)
    *   [func (x *Scalars) GetOptUint64() uint64](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.GetOptUint64)
    *   [func (*Scalars) ProtoMessage()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.ProtoMessage)
    *   [func (x *Scalars) ProtoReflect() protoreflect.Message](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.ProtoReflect)
    *   [func (x *Scalars) Reset()](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.Reset)
    *   [func (x *Scalars) String() string](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars.String)

This section is empty.

Enum value maps for Enum.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/textpb2/test.pb.go#L106)

var (
 Enums_NestedEnum_name = map[[int32](https://pkg.go.dev/builtin#int32)][string](https://pkg.go.dev/builtin#string){ 		1:  "UNO",
		2:  "DOS",
		10: "DIEZ",
	}
 Enums_NestedEnum_value = map[[string](https://pkg.go.dev/builtin#string)][int32](https://pkg.go.dev/builtin#int32){ 		"UNO":  1,
		"DOS":  2,
		"DIEZ": 10,
	}
)

Enum value maps for Enums_NestedEnum.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/textpb2/test.pb.go#L1763)

var (
	E_OptExtBool = &file_internal_testprotos_textpb2_test_proto_extTypes[0]
	E_OptExtString = &file_internal_testprotos_textpb2_test_proto_extTypes[1]
	E_OptExtEnum = &file_internal_testprotos_textpb2_test_proto_extTypes[2]
	E_OptExtNested = &file_internal_testprotos_textpb2_test_proto_extTypes[3]
	E_OptExtPartial = &file_internal_testprotos_textpb2_test_proto_extTypes[4]
	E_RptExtFixed32 = &file_internal_testprotos_textpb2_test_proto_extTypes[5]
	E_RptExtEnum = &file_internal_testprotos_textpb2_test_proto_extTypes[6]
	E_RptExtNested = &file_internal_testprotos_textpb2_test_proto_extTypes[7]
	E_ExtensionsContainer_OptExtBool = &file_internal_testprotos_textpb2_test_proto_extTypes[9]
	E_ExtensionsContainer_OptExtString = &file_internal_testprotos_textpb2_test_proto_extTypes[10]
	E_ExtensionsContainer_OptExtEnum = &file_internal_testprotos_textpb2_test_proto_extTypes[11]
	E_ExtensionsContainer_OptExtNested = &file_internal_testprotos_textpb2_test_proto_extTypes[12]
	E_ExtensionsContainer_OptExtPartial = &file_internal_testprotos_textpb2_test_proto_extTypes[13]
	E_ExtensionsContainer_RptExtString = &file_internal_testprotos_textpb2_test_proto_extTypes[14]
	E_ExtensionsContainer_RptExtEnum = &file_internal_testprotos_textpb2_test_proto_extTypes[15]
	E_ExtensionsContainer_RptExtNested = &file_internal_testprotos_textpb2_test_proto_extTypes[16]
)

Extension fields to Extensions.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/textpb2/test.pb.go#L1799)

var (
	E_MessageSetExtension = &file_internal_testprotos_textpb2_test_proto_extTypes[8]
	E_MessageSetExtension_MessageSetExtension = &file_internal_testprotos_textpb2_test_proto_extTypes[17]
	E_MessageSetExtension_NotMessageSetExtension = &file_internal_testprotos_textpb2_test_proto_extTypes[18]
	E_MessageSetExtension_ExtNested = &file_internal_testprotos_textpb2_test_proto_extTypes[19]
)

Extension fields to MessageSet.

[View Source](https://github.com/temporalio/api-go/blob/v1.62.2/internal/protojson/testprotos/textpb2/test.pb.go#L1811)

var (
	E_FakeMessageSetExtension_MessageSetExtension = &file_internal_testprotos_textpb2_test_proto_extTypes[20]
)

Extension fields to FakeMessageSet.

This section is empty.

const (
 Enum_ONE [Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum) = 1  Enum_TWO [Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum) = 2  Enum_TEN [Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum) = 10 )

func (x [Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)) Enum() *[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)

func ([Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)) EnumDescriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Enum.Descriptor instead.

Deprecated: Do not use.

type Enums struct {
 OptEnum *[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum) `protobuf:"varint,1,opt,name=opt_enum,json=optEnum,enum=pb2.Enum" json:"opt_enum,omitempty"`  RptEnum [][Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum) `protobuf:"varint,2,rep,name=rpt_enum,json=rptEnum,enum=pb2.Enum" json:"rpt_enum,omitempty"`  OptNestedEnum *[Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum) `protobuf:"varint,3,opt,name=opt_nested_enum,json=optNestedEnum,enum=pb2.Enums_NestedEnum" json:"opt_nested_enum,omitempty"`  RptNestedEnum [][Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum) `protobuf:"varint,4,rep,name=rpt_nested_enum,json=rptNestedEnum,enum=pb2.Enums_NestedEnum" json:"rpt_nested_enum,omitempty"` 	
}

Message contains enum fields.

Deprecated: Use Enums.ProtoReflect.Descriptor instead.

func (x *[Enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums)) GetOptEnum() [Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)

func (x *[Enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums)) GetOptNestedEnum() [Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum)

func (x *[Enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums)) GetRptEnum() [][Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)

func (x *[Enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums)) GetRptNestedEnum() [][Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum)

func (*[Enums](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums)) ProtoMessage()

type Enums_NestedEnum [int32](https://pkg.go.dev/builtin#int32)

const (
 Enums_UNO [Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum) = 1  Enums_DOS [Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum) = 2  Enums_DIEZ [Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum) = 10 )

func (x [Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum)) Enum() *[Enums_NestedEnum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enums_NestedEnum)

Deprecated: Use Enums_NestedEnum.Descriptor instead.

Deprecated: Do not use.

type Extensions struct {
 OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=opt_string,json=optString" json:"opt_string,omitempty"`  OptBool *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,101,opt,name=opt_bool,json=optBool" json:"opt_bool,omitempty"`  OptInt32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=opt_int32,json=optInt32" json:"opt_int32,omitempty"` 	
}

Deprecated: Use Extensions.ProtoReflect.Descriptor instead.

func (x *[Extensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions)) GetOptBool() [bool](https://pkg.go.dev/builtin#bool)

func (x *[Extensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions)) GetOptInt32() [int32](https://pkg.go.dev/builtin#int32)

func (*[Extensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions)) ProtoMessage()

func (x *[Extensions](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Extensions)) Reset()

type ExtensionsContainer struct {
	
}

Deprecated: Use ExtensionsContainer.ProtoReflect.Descriptor instead.

func (*[ExtensionsContainer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer)) ProtoMessage()

func (x *[ExtensionsContainer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#ExtensionsContainer)) Reset()

type FakeMessageSet struct {
	
}

Deprecated: Use FakeMessageSet.ProtoReflect.Descriptor instead.

func (*[FakeMessageSet](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet)) ProtoMessage()

func (x *[FakeMessageSet](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSet)) Reset()

type FakeMessageSetExtension struct {
 OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=opt_string,json=optString" json:"opt_string,omitempty"` 	
}

Deprecated: Use FakeMessageSetExtension.ProtoReflect.Descriptor instead.

func (*[FakeMessageSetExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension)) ProtoMessage()

func (x *[FakeMessageSetExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#FakeMessageSetExtension)) Reset()

type IndirectRequired struct {
 OptNested *[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired) `protobuf:"bytes,1,opt,name=opt_nested,json=optNested" json:"opt_nested,omitempty"`  RptNested []*[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired) `protobuf:"bytes,2,rep,name=rpt_nested,json=rptNested" json:"rpt_nested,omitempty"`  StrToNested map[[string](https://pkg.go.dev/builtin#string)]*[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired) `` 	
	
	Union isIndirectRequired_Union `protobuf_oneof:"union"`
	
}

Deprecated: Use IndirectRequired.ProtoReflect.Descriptor instead.

func (x *[IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)) GetOneofNested() *[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired)

func (x *[IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)) GetOptNested() *[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired)

func (x *[IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)) GetRptNested() []*[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired)

func (m *[IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)) GetUnion() isIndirectRequired_Union

func (*[IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)) ProtoMessage()

func (x *[IndirectRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#IndirectRequired)) Reset()

type IndirectRequired_OneofNested struct {
 OneofNested *[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired) `protobuf:"bytes,4,opt,name=oneof_nested,json=oneofNested,oneof"` }

type KnownTypes struct {
 OptBool *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[BoolValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#BoolValue) `protobuf:"bytes,1,opt,name=opt_bool,json=optBool" json:"opt_bool,omitempty"`  OptInt32 *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[Int32Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#Int32Value) `protobuf:"bytes,2,opt,name=opt_int32,json=optInt32" json:"opt_int32,omitempty"`  OptInt64 *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[Int64Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#Int64Value) `protobuf:"bytes,3,opt,name=opt_int64,json=optInt64" json:"opt_int64,omitempty"`  OptUint32 *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[UInt32Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#UInt32Value) `protobuf:"bytes,4,opt,name=opt_uint32,json=optUint32" json:"opt_uint32,omitempty"`  OptUint64 *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[UInt64Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#UInt64Value) `protobuf:"bytes,5,opt,name=opt_uint64,json=optUint64" json:"opt_uint64,omitempty"`  OptFloat *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[FloatValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#FloatValue) `protobuf:"bytes,6,opt,name=opt_float,json=optFloat" json:"opt_float,omitempty"`  OptDouble *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[DoubleValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#DoubleValue) `protobuf:"bytes,7,opt,name=opt_double,json=optDouble" json:"opt_double,omitempty"`  OptString *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[StringValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#StringValue) `protobuf:"bytes,8,opt,name=opt_string,json=optString" json:"opt_string,omitempty"`  OptBytes *[wrapperspb](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb).[BytesValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/wrapperspb#BytesValue) `protobuf:"bytes,9,opt,name=opt_bytes,json=optBytes" json:"opt_bytes,omitempty"`  OptDuration *[durationpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb).[Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb#Duration) `protobuf:"bytes,20,opt,name=opt_duration,json=optDuration" json:"opt_duration,omitempty"`  OptTimestamp *[timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[Timestamp](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#Timestamp) `protobuf:"bytes,21,opt,name=opt_timestamp,json=optTimestamp" json:"opt_timestamp,omitempty"`  OptStruct *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Struct](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Struct) `protobuf:"bytes,25,opt,name=opt_struct,json=optStruct" json:"opt_struct,omitempty"`  OptList *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[ListValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#ListValue) `protobuf:"bytes,26,opt,name=opt_list,json=optList" json:"opt_list,omitempty"`  OptValue *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[Value](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#Value) `protobuf:"bytes,27,opt,name=opt_value,json=optValue" json:"opt_value,omitempty"`  OptNull *[structpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb).[NullValue](https://pkg.go.dev/google.golang.org/protobuf/types/known/structpb#NullValue) `protobuf:"varint,28,opt,name=opt_null,json=optNull,enum=google.protobuf.NullValue" json:"opt_null,omitempty"`  OptEmpty *[emptypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb).[Empty](https://pkg.go.dev/google.golang.org/protobuf/types/known/emptypb#Empty) `protobuf:"bytes,30,opt,name=opt_empty,json=optEmpty" json:"opt_empty,omitempty"`  OptAny *[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any) `protobuf:"bytes,32,opt,name=opt_any,json=optAny" json:"opt_any,omitempty"`  OptFieldmask *[fieldmaskpb](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb).[FieldMask](https://pkg.go.dev/google.golang.org/protobuf/types/known/fieldmaskpb#FieldMask) `protobuf:"bytes,40,opt,name=opt_fieldmask,json=optFieldmask" json:"opt_fieldmask,omitempty"` 	
}

Message contains well-known type fields.

Deprecated: Use KnownTypes.ProtoReflect.Descriptor instead.

func (*[KnownTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes)) ProtoMessage()

func (x *[KnownTypes](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#KnownTypes)) Reset()

Message contains map fields.

func (*[Maps](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps)) Descriptor() ([][byte](https://pkg.go.dev/builtin#byte), [][int](https://pkg.go.dev/builtin#int))

Deprecated: Use Maps.ProtoReflect.Descriptor instead.

func (x *[Maps](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps)) GetStrToNested() map[[string](https://pkg.go.dev/builtin#string)]*[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)

func (*[Maps](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Maps)) ProtoMessage()

type MessageSet struct {
	
}

Deprecated: Use MessageSet.ProtoReflect.Descriptor instead.

func (*[MessageSet](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet)) ProtoMessage()

func (x *[MessageSet](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSet)) Reset()

type MessageSetExtension struct {
 OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=opt_string,json=optString" json:"opt_string,omitempty"` 	
}

Deprecated: Use MessageSetExtension.ProtoReflect.Descriptor instead.

func (*[MessageSetExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension)) ProtoMessage()

func (x *[MessageSetExtension](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#MessageSetExtension)) Reset()

type Nested struct {
 OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=opt_string,json=optString" json:"opt_string,omitempty"`  OptNested *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested) `protobuf:"bytes,2,opt,name=opt_nested,json=optNested" json:"opt_nested,omitempty"` 	
}

Message type used as submessage.

Deprecated: Use Nested.ProtoReflect.Descriptor instead.

func (x *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)) GetOptNested() *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)

func (*[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)) ProtoMessage()

type NestedWithRequired struct {
 ReqString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,req,name=req_string,json=reqString" json:"req_string,omitempty"` 	
}

Deprecated: Use NestedWithRequired.ProtoReflect.Descriptor instead.

func (*[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired)) ProtoMessage()

func (x *[NestedWithRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#NestedWithRequired)) Reset()

type Nests struct {
 OptNested *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested) `protobuf:"bytes,1,opt,name=opt_nested,json=optNested" json:"opt_nested,omitempty"`  Optgroup *[Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup) `protobuf:"group,2,opt,name=OptGroup,json=optgroup" json:"optgroup,omitempty"`  RptNested []*[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested) `protobuf:"bytes,4,rep,name=rpt_nested,json=rptNested" json:"rpt_nested,omitempty"`  Rptgroup []*[Nests_RptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup) `protobuf:"group,5,rep,name=RptGroup,json=rptgroup" json:"rptgroup,omitempty"` 	
}

Message contains message and group fields.

Deprecated: Use Nests.ProtoReflect.Descriptor instead.

func (x *[Nests](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests)) GetOptNested() *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)

func (x *[Nests](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests)) GetOptgroup() *[Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup)

func (x *[Nests](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests)) GetRptNested() []*[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)

func (x *[Nests](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests)) GetRptgroup() []*[Nests_RptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup)

func (*[Nests](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests)) ProtoMessage()

type Nests_OptGroup struct {
 OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=opt_string,json=optString" json:"opt_string,omitempty"`  OptNested *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested) `protobuf:"bytes,2,opt,name=opt_nested,json=optNested" json:"opt_nested,omitempty"`  Optnestedgroup *[Nests_OptGroup_OptNestedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup) `protobuf:"group,3,opt,name=OptNestedGroup,json=optnestedgroup" json:"optnestedgroup,omitempty"` 	
}

Deprecated: Use Nests_OptGroup.ProtoReflect.Descriptor instead.

func (x *[Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup)) GetOptNested() *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)

func (x *[Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup)) GetOptnestedgroup() *[Nests_OptGroup_OptNestedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup)

func (*[Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup)) ProtoMessage()

func (x *[Nests_OptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup)) Reset()

type Nests_OptGroup_OptNestedGroup struct {
 OptFixed32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,1,opt,name=opt_fixed32,json=optFixed32" json:"opt_fixed32,omitempty"` 	
}

Deprecated: Use Nests_OptGroup_OptNestedGroup.ProtoReflect.Descriptor instead.

func (*[Nests_OptGroup_OptNestedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup)) ProtoMessage()

func (x *[Nests_OptGroup_OptNestedGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_OptGroup_OptNestedGroup)) Reset()

type Nests_RptGroup struct {
 RptString [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,rep,name=rpt_string,json=rptString" json:"rpt_string,omitempty"` 	
}

Deprecated: Use Nests_RptGroup.ProtoReflect.Descriptor instead.

func (*[Nests_RptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup)) ProtoMessage()

func (x *[Nests_RptGroup](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nests_RptGroup)) Reset()

type PartialRequired struct {
 ReqString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,req,name=req_string,json=reqString" json:"req_string,omitempty"`  OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=opt_string,json=optString" json:"opt_string,omitempty"` 	
}

Message contains both required and optional fields.

Deprecated: Use PartialRequired.ProtoReflect.Descriptor instead.

func (*[PartialRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired)) ProtoMessage()

func (x *[PartialRequired](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#PartialRequired)) Reset()

type Repeats struct {
 RptBool [][bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,rep,name=rpt_bool,json=rptBool" json:"rpt_bool,omitempty"`  RptInt32 [][int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,rep,name=rpt_int32,json=rptInt32" json:"rpt_int32,omitempty"`  RptInt64 [][int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,rep,name=rpt_int64,json=rptInt64" json:"rpt_int64,omitempty"`  RptUint32 [][uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,4,rep,name=rpt_uint32,json=rptUint32" json:"rpt_uint32,omitempty"`  RptUint64 [][uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,5,rep,name=rpt_uint64,json=rptUint64" json:"rpt_uint64,omitempty"`  RptFloat [][float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,6,rep,name=rpt_float,json=rptFloat" json:"rpt_float,omitempty"`  RptDouble [][float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,7,rep,name=rpt_double,json=rptDouble" json:"rpt_double,omitempty"`  RptString [][string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,8,rep,name=rpt_string,json=rptString" json:"rpt_string,omitempty"`  RptBytes [][][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,9,rep,name=rpt_bytes,json=rptBytes" json:"rpt_bytes,omitempty"` 	
}

Message contains repeated fields.

Deprecated: Use Repeats.ProtoReflect.Descriptor instead.

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptBool() [][bool](https://pkg.go.dev/builtin#bool)

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptBytes() [][][byte](https://pkg.go.dev/builtin#byte)

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptInt32() [][int32](https://pkg.go.dev/builtin#int32)

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptInt64() [][int64](https://pkg.go.dev/builtin#int64)

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptString() [][string](https://pkg.go.dev/builtin#string)

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptUint32() [][uint32](https://pkg.go.dev/builtin#uint32)

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) GetRptUint64() [][uint64](https://pkg.go.dev/builtin#uint64)

func (*[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) ProtoMessage()

func (x *[Repeats](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Repeats)) Reset()

type Requireds struct {
 ReqBool *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,req,name=req_bool,json=reqBool" json:"req_bool,omitempty"`  ReqSfixed64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,2,req,name=req_sfixed64,json=reqSfixed64" json:"req_sfixed64,omitempty"`  ReqDouble *[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,3,req,name=req_double,json=reqDouble" json:"req_double,omitempty"`  ReqString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,req,name=req_string,json=reqString" json:"req_string,omitempty"`  ReqEnum *[Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum) `protobuf:"varint,5,req,name=req_enum,json=reqEnum,enum=pb2.Enum" json:"req_enum,omitempty"`  ReqNested *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested) `protobuf:"bytes,6,req,name=req_nested,json=reqNested" json:"req_nested,omitempty"` 	
}

Message contains required fields.

Deprecated: Use Requireds.ProtoReflect.Descriptor instead.

func (x *[Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)) GetReqBool() [bool](https://pkg.go.dev/builtin#bool)

func (x *[Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)) GetReqEnum() [Enum](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Enum)

func (x *[Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)) GetReqNested() *[Nested](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Nested)

func (x *[Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)) GetReqSfixed64() [int64](https://pkg.go.dev/builtin#int64)

func (*[Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)) ProtoMessage()

func (x *[Requireds](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Requireds)) Reset()

type Scalars struct {
 OptBool *[bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=opt_bool,json=optBool" json:"opt_bool,omitempty"`  OptInt32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=opt_int32,json=optInt32" json:"opt_int32,omitempty"`  OptInt64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"varint,3,opt,name=opt_int64,json=optInt64" json:"opt_int64,omitempty"`  OptUint32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"varint,4,opt,name=opt_uint32,json=optUint32" json:"opt_uint32,omitempty"`  OptUint64 *[uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"varint,5,opt,name=opt_uint64,json=optUint64" json:"opt_uint64,omitempty"`  OptSint32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"zigzag32,6,opt,name=opt_sint32,json=optSint32" json:"opt_sint32,omitempty"`  OptSint64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"zigzag64,7,opt,name=opt_sint64,json=optSint64" json:"opt_sint64,omitempty"`  OptFixed32 *[uint32](https://pkg.go.dev/builtin#uint32) `protobuf:"fixed32,8,opt,name=opt_fixed32,json=optFixed32" json:"opt_fixed32,omitempty"`  OptFixed64 *[uint64](https://pkg.go.dev/builtin#uint64) `protobuf:"fixed64,9,opt,name=opt_fixed64,json=optFixed64" json:"opt_fixed64,omitempty"`  OptSfixed32 *[int32](https://pkg.go.dev/builtin#int32) `protobuf:"fixed32,10,opt,name=opt_sfixed32,json=optSfixed32" json:"opt_sfixed32,omitempty"`  OptSfixed64 *[int64](https://pkg.go.dev/builtin#int64) `protobuf:"fixed64,11,opt,name=opt_sfixed64,json=optSfixed64" json:"opt_sfixed64,omitempty"`  OptFloat *[float32](https://pkg.go.dev/builtin#float32) `protobuf:"fixed32,20,opt,name=opt_float,json=optFloat" json:"opt_float,omitempty"`  OptDouble *[float64](https://pkg.go.dev/builtin#float64) `protobuf:"fixed64,21,opt,name=opt_double,json=optDouble" json:"opt_double,omitempty"`  OptBytes [][byte](https://pkg.go.dev/builtin#byte) `protobuf:"bytes,14,opt,name=opt_bytes,json=optBytes" json:"opt_bytes,omitempty"`  OptString *[string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,13,opt,name=opt_string,json=optString" json:"opt_string,omitempty"` 	
}

Scalars contains optional scalar fields.

Deprecated: Use Scalars.ProtoReflect.Descriptor instead.

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptBool() [bool](https://pkg.go.dev/builtin#bool)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptBytes() [][byte](https://pkg.go.dev/builtin#byte)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptInt32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptInt64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptSfixed32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptSfixed64() [int64](https://pkg.go.dev/builtin#int64)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptSint32() [int32](https://pkg.go.dev/builtin#int32)

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) GetOptSint64() [int64](https://pkg.go.dev/builtin#int64)

func (*[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) ProtoMessage()

func (x *[Scalars](https://pkg.go.dev/go.temporal.io/api@v1.62.2/internal/protojson/testprotos/textpb2#Scalars)) Reset()
