# Source: https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/tests/example/v1

Title: examplev1 package - buf.build/go/protovalidate/internal/gen/tests/example/v1 - Go Packages

URL Source: https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/tests/example/v1

Markdown Content:
Skip to Main Content
Why Go
Learn
Docs
Packages
Community
Discover Packages
 
buf.build/go/protovalidate
 
internal
 
gen
 
tests
 
example
 
v1
examplev1
package
Version: v1.1.3 Latest 
Published: Feb 19, 2026 
License: Apache-2.0 
Imports: 10 
Imported by: 0
Details
 Valid go.mod file 
 Redistributable license 
 Tagged version 
 Stable version 
Learn more about best practices
Repository
github.com/bufbuild/protovalidate-go
Links
 Open Source Insights
Jump to ...
Documentation
Source Files
 Documentation ¶
Index ¶
Constants
Variables
type AllRuleTypes
func (x *AllRuleTypes) ClearOneofField()
func (x *AllRuleTypes) ClearRequiredOneof()
func (x *AllRuleTypes) GetField() int32
func (x *AllRuleTypes) GetOneofField() string
func (x *AllRuleTypes) GetRequiredOneof() isAllRuleTypes_RequiredOneof
func (x *AllRuleTypes) HasOneofField() bool
func (x *AllRuleTypes) HasRequiredOneof() bool
func (*AllRuleTypes) ProtoMessage()
func (x *AllRuleTypes) ProtoReflect() protoreflect.Message
func (x *AllRuleTypes) Reset()
func (x *AllRuleTypes) SetField(v int32)
func (x *AllRuleTypes) SetOneofField(v string)
func (x *AllRuleTypes) String() string
func (x *AllRuleTypes) WhichRequiredOneof() case_AllRuleTypes_RequiredOneof
type AllRuleTypes_OneofField
type AllRuleTypes_builder
func (b0 AllRuleTypes_builder) Build() *AllRuleTypes
type BenchComplexSchema
func (x *BenchComplexSchema) ClearChoice()
func (x *BenchComplexSchema) ClearNested()
func (x *BenchComplexSchema) ClearOneofI32()
func (x *BenchComplexSchema) ClearOneofMsg()
func (x *BenchComplexSchema) ClearOneofStr()
func (x *BenchComplexSchema) ClearSelfRef()
func (x *BenchComplexSchema) GetBl() bool
func (x *BenchComplexSchema) GetBy() []byte
func (x *BenchComplexSchema) GetChoice() isBenchComplexSchema_Choice
func (x *BenchComplexSchema) GetDb() float64
func (x *BenchComplexSchema) GetEnumField() BenchEnum
func (x *BenchComplexSchema) GetF32() uint32
func (x *BenchComplexSchema) GetF64() uint64
func (x *BenchComplexSchema) GetFl() float32
func (x *BenchComplexSchema) GetI32() int32
func (x *BenchComplexSchema) GetI64() int64
func (x *BenchComplexSchema) GetMapI32I64() map[int32]int64
func (x *BenchComplexSchema) GetMapI64Msg() map[int64]*BenchScalar
func (x *BenchComplexSchema) GetMapStrBytes() map[string][]byte
func (x *BenchComplexSchema) GetMapStrMsg() map[string]*BenchScalar
func (x *BenchComplexSchema) GetMapStrStr() map[string]string
func (x *BenchComplexSchema) GetMapU64Bool() map[uint64]bool
func (x *BenchComplexSchema) GetNested() *BenchScalar
func (x *BenchComplexSchema) GetOneofI32() int32
func (x *BenchComplexSchema) GetOneofMsg() *BenchScalar
func (x *BenchComplexSchema) GetOneofStr() string
func (x *BenchComplexSchema) GetRepBytes() [][]byte
func (x *BenchComplexSchema) GetRepI32() []int32
func (x *BenchComplexSchema) GetRepMsg() []*BenchScalar
func (x *BenchComplexSchema) GetRepStr() []string
func (x *BenchComplexSchema) GetS1() string
func (x *BenchComplexSchema) GetS2() string
func (x *BenchComplexSchema) GetSelfRef() *BenchComplexSchema
func (x *BenchComplexSchema) GetSf32() int32
func (x *BenchComplexSchema) GetSf64() int64
func (x *BenchComplexSchema) GetSi32() int32
func (x *BenchComplexSchema) GetSi64() int64
func (x *BenchComplexSchema) GetU32() uint32
func (x *BenchComplexSchema) GetU64() uint64
func (x *BenchComplexSchema) HasChoice() bool
func (x *BenchComplexSchema) HasNested() bool
func (x *BenchComplexSchema) HasOneofI32() bool
func (x *BenchComplexSchema) HasOneofMsg() bool
func (x *BenchComplexSchema) HasOneofStr() bool
func (x *BenchComplexSchema) HasSelfRef() bool
func (*BenchComplexSchema) ProtoMessage()
func (x *BenchComplexSchema) ProtoReflect() protoreflect.Message
func (x *BenchComplexSchema) Reset()
func (x *BenchComplexSchema) SetBl(v bool)
func (x *BenchComplexSchema) SetBy(v []byte)
func (x *BenchComplexSchema) SetDb(v float64)
func (x *BenchComplexSchema) SetEnumField(v BenchEnum)
func (x *BenchComplexSchema) SetF32(v uint32)
func (x *BenchComplexSchema) SetF64(v uint64)
func (x *BenchComplexSchema) SetFl(v float32)
func (x *BenchComplexSchema) SetI32(v int32)
func (x *BenchComplexSchema) SetI64(v int64)
func (x *BenchComplexSchema) SetMapI32I64(v map[int32]int64)
func (x *BenchComplexSchema) SetMapI64Msg(v map[int64]*BenchScalar)
func (x *BenchComplexSchema) SetMapStrBytes(v map[string][]byte)
func (x *BenchComplexSchema) SetMapStrMsg(v map[string]*BenchScalar)
func (x *BenchComplexSchema) SetMapStrStr(v map[string]string)
func (x *BenchComplexSchema) SetMapU64Bool(v map[uint64]bool)
func (x *BenchComplexSchema) SetNested(v *BenchScalar)
func (x *BenchComplexSchema) SetOneofI32(v int32)
func (x *BenchComplexSchema) SetOneofMsg(v *BenchScalar)
func (x *BenchComplexSchema) SetOneofStr(v string)
func (x *BenchComplexSchema) SetRepBytes(v [][]byte)
func (x *BenchComplexSchema) SetRepI32(v []int32)
func (x *BenchComplexSchema) SetRepMsg(v []*BenchScalar)
func (x *BenchComplexSchema) SetRepStr(v []string)
func (x *BenchComplexSchema) SetS1(v string)
func (x *BenchComplexSchema) SetS2(v string)
func (x *BenchComplexSchema) SetSelfRef(v *BenchComplexSchema)
func (x *BenchComplexSchema) SetSf32(v int32)
func (x *BenchComplexSchema) SetSf64(v int64)
func (x *BenchComplexSchema) SetSi32(v int32)
func (x *BenchComplexSchema) SetSi64(v int64)
func (x *BenchComplexSchema) SetU32(v uint32)
func (x *BenchComplexSchema) SetU64(v uint64)
func (x *BenchComplexSchema) String() string
func (x *BenchComplexSchema) WhichChoice() case_BenchComplexSchema_Choice
type BenchComplexSchema_OneofI32
type BenchComplexSchema_OneofMsg
type BenchComplexSchema_OneofStr
type BenchComplexSchema_builder
func (b0 BenchComplexSchema_builder) Build() *BenchComplexSchema
type BenchEnum
func (BenchEnum) Descriptor() protoreflect.EnumDescriptor
func (x BenchEnum) Enum() *BenchEnum
func (x BenchEnum) Number() protoreflect.EnumNumber
func (x BenchEnum) String() string
func (BenchEnum) Type() protoreflect.EnumType
type BenchMap
func (x *BenchMap) GetEntries() map[string]string
func (*BenchMap) ProtoMessage()
func (x *BenchMap) ProtoReflect() protoreflect.Message
func (x *BenchMap) Reset()
func (x *BenchMap) SetEntries(v map[string]string)
func (x *BenchMap) String() string
type BenchMap_builder
func (b0 BenchMap_builder) Build() *BenchMap
type BenchRepeatedBytesUnique
func (x *BenchRepeatedBytesUnique) GetX() [][]byte
func (*BenchRepeatedBytesUnique) ProtoMessage()
func (x *BenchRepeatedBytesUnique) ProtoReflect() protoreflect.Message
func (x *BenchRepeatedBytesUnique) Reset()
func (x *BenchRepeatedBytesUnique) SetX(v [][]byte)
func (x *BenchRepeatedBytesUnique) String() string
type BenchRepeatedBytesUnique_builder
func (b0 BenchRepeatedBytesUnique_builder) Build() *BenchRepeatedBytesUnique
type BenchRepeatedMessage
func (x *BenchRepeatedMessage) GetX() []*BenchScalar
func (*BenchRepeatedMessage) ProtoMessage()
func (x *BenchRepeatedMessage) ProtoReflect() protoreflect.Message
func (x *BenchRepeatedMessage) Reset()
func (x *BenchRepeatedMessage) SetX(v []*BenchScalar)
func (x *BenchRepeatedMessage) String() string
type BenchRepeatedMessage_builder
func (b0 BenchRepeatedMessage_builder) Build() *BenchRepeatedMessage
type BenchRepeatedScalar
func (x *BenchRepeatedScalar) GetX() []int32
func (*BenchRepeatedScalar) ProtoMessage()
func (x *BenchRepeatedScalar) ProtoReflect() protoreflect.Message
func (x *BenchRepeatedScalar) Reset()
func (x *BenchRepeatedScalar) SetX(v []int32)
func (x *BenchRepeatedScalar) String() string
type BenchRepeatedScalarUnique
func (x *BenchRepeatedScalarUnique) GetX() []float32
func (*BenchRepeatedScalarUnique) ProtoMessage()
func (x *BenchRepeatedScalarUnique) ProtoReflect() protoreflect.Message
func (x *BenchRepeatedScalarUnique) Reset()
func (x *BenchRepeatedScalarUnique) SetX(v []float32)
func (x *BenchRepeatedScalarUnique) String() string
type BenchRepeatedScalarUnique_builder
func (b0 BenchRepeatedScalarUnique_builder) Build() *BenchRepeatedScalarUnique
type BenchRepeatedScalar_builder
func (b0 BenchRepeatedScalar_builder) Build() *BenchRepeatedScalar
type BenchScalar
func (x *BenchScalar) GetX() int32
func (*BenchScalar) ProtoMessage()
func (x *BenchScalar) ProtoReflect() protoreflect.Message
func (x *BenchScalar) Reset()
func (x *BenchScalar) SetX(v int32)
func (x *BenchScalar) String() string
type BenchScalar_builder
func (b0 BenchScalar_builder) Build() *BenchScalar
type CelMapOnARepeated
func (x *CelMapOnARepeated) GetValues() []*CelMapOnARepeated_Value
func (*CelMapOnARepeated) ProtoMessage()
func (x *CelMapOnARepeated) ProtoReflect() protoreflect.Message
func (x *CelMapOnARepeated) Reset()
func (x *CelMapOnARepeated) SetValues(v []*CelMapOnARepeated_Value)
func (x *CelMapOnARepeated) String() string
type CelMapOnARepeated_Value
func (x *CelMapOnARepeated_Value) GetName() string
func (*CelMapOnARepeated_Value) ProtoMessage()
func (x *CelMapOnARepeated_Value) ProtoReflect() protoreflect.Message
func (x *CelMapOnARepeated_Value) Reset()
func (x *CelMapOnARepeated_Value) SetName(v string)
func (x *CelMapOnARepeated_Value) String() string
type CelMapOnARepeated_Value_builder
func (b0 CelMapOnARepeated_Value_builder) Build() *CelMapOnARepeated_Value
type CelMapOnARepeated_builder
func (b0 CelMapOnARepeated_builder) Build() *CelMapOnARepeated
type Coordinates
func (x *Coordinates) GetLat() float64
func (x *Coordinates) GetLng() float64
func (*Coordinates) ProtoMessage()
func (x *Coordinates) ProtoReflect() protoreflect.Message
func (x *Coordinates) Reset()
func (x *Coordinates) SetLat(v float64)
func (x *Coordinates) SetLng(v float64)
func (x *Coordinates) String() string
type Coordinates_builder
func (b0 Coordinates_builder) Build() *Coordinates
type F1
func (x *F1) ClearField()
func (x *F1) GetField() *FieldWithIssue
func (x *F1) GetNeedThis() string
func (x *F1) HasField() bool
func (*F1) ProtoMessage()
func (x *F1) ProtoReflect() protoreflect.Message
func (x *F1) Reset()
func (x *F1) SetField(v *FieldWithIssue)
func (x *F1) SetNeedThis(v string)
func (x *F1) String() string
type F1_builder
func (b0 F1_builder) Build() *F1
type F2
func (x *F2) ClearField()
func (x *F2) GetField() *FieldWithIssue
func (x *F2) HasField() bool
func (*F2) ProtoMessage()
func (x *F2) ProtoReflect() protoreflect.Message
func (x *F2) Reset()
func (x *F2) SetField(v *FieldWithIssue)
func (x *F2) String() string
type F2_builder
func (b0 F2_builder) Build() *F2
type FieldOfTypeAny
func (x *FieldOfTypeAny) ClearAny()
func (x *FieldOfTypeAny) GetAny() *anypb.Any
func (x *FieldOfTypeAny) HasAny() bool
func (*FieldOfTypeAny) ProtoMessage()
func (x *FieldOfTypeAny) ProtoReflect() protoreflect.Message
func (x *FieldOfTypeAny) Reset()
func (x *FieldOfTypeAny) SetAny(v *anypb.Any)
func (x *FieldOfTypeAny) String() string
type FieldOfTypeAny_builder
func (b0 FieldOfTypeAny_builder) Build() *FieldOfTypeAny
type FieldWithIssue
func (x *FieldWithIssue) ClearF1()
func (x *FieldWithIssue) GetF1() *F1
func (x *FieldWithIssue) GetName() string
func (x *FieldWithIssue) HasF1() bool
func (*FieldWithIssue) ProtoMessage()
func (x *FieldWithIssue) ProtoReflect() protoreflect.Message
func (x *FieldWithIssue) Reset()
func (x *FieldWithIssue) SetF1(v *F1)
func (x *FieldWithIssue) SetName(v string)
func (x *FieldWithIssue) String() string
type FieldWithIssue_builder
func (b0 FieldWithIssue_builder) Build() *FieldWithIssue
type HasMsgExprs
func (x *HasMsgExprs) GetX() int32
func (x *HasMsgExprs) GetY() int32
func (*HasMsgExprs) ProtoMessage()
func (x *HasMsgExprs) ProtoReflect() protoreflect.Message
func (x *HasMsgExprs) Reset()
func (x *HasMsgExprs) SetX(v int32)
func (x *HasMsgExprs) SetY(v int32)
func (x *HasMsgExprs) String() string
type HasMsgExprs_builder
func (b0 HasMsgExprs_builder) Build() *HasMsgExprs
type InvalidRules
func (x *InvalidRules) GetField() int32
func (*InvalidRules) ProtoMessage()
func (x *InvalidRules) ProtoReflect() protoreflect.Message
func (x *InvalidRules) Reset()
func (x *InvalidRules) SetField(v int32)
func (x *InvalidRules) String() string
type InvalidRules_builder
func (b0 InvalidRules_builder) Build() *InvalidRules
type Issue148
func (x *Issue148) ClearTest()
func (x *Issue148) GetTest() int32
func (x *Issue148) HasTest() bool
func (*Issue148) ProtoMessage()
func (x *Issue148) ProtoReflect() protoreflect.Message
func (x *Issue148) Reset()
func (x *Issue148) SetTest(v int32)
func (x *Issue148) String() string
type Issue148_builder
func (b0 Issue148_builder) Build() *Issue148
type Issue187
func (x *Issue187) ClearFalseField()
func (x *Issue187) ClearTrueField()
func (x *Issue187) GetFalseField() bool
func (x *Issue187) GetTrueField() bool
func (x *Issue187) HasFalseField() bool
func (x *Issue187) HasTrueField() bool
func (*Issue187) ProtoMessage()
func (x *Issue187) ProtoReflect() protoreflect.Message
func (x *Issue187) Reset()
func (x *Issue187) SetFalseField(v bool)
func (x *Issue187) SetTrueField(v bool)
func (x *Issue187) String() string
type Issue187_builder
func (b0 Issue187_builder) Build() *Issue187
type Issue211
func (x *Issue211) ClearValue()
func (x *Issue211) GetValue() *timestamppb.Timestamp
func (x *Issue211) HasValue() bool
func (*Issue211) ProtoMessage()
func (x *Issue211) ProtoReflect() protoreflect.Message
func (x *Issue211) Reset()
func (x *Issue211) SetValue(v *timestamppb.Timestamp)
func (x *Issue211) String() string
type Issue211_builder
func (b0 Issue211_builder) Build() *Issue211
type Issue296
func (x *Issue296) ClearFm()
func (x *Issue296) GetFm() *fieldmaskpb.FieldMask
func (x *Issue296) HasFm() bool
func (*Issue296) ProtoMessage()
func (x *Issue296) ProtoReflect() protoreflect.Message
func (x *Issue296) Reset()
func (x *Issue296) SetFm(v *fieldmaskpb.FieldMask)
func (x *Issue296) String() string
type Issue296_builder
func (b0 Issue296_builder) Build() *Issue296
type LoopRecursiveA
func (x *LoopRecursiveA) ClearB()
func (x *LoopRecursiveA) GetB() *LoopRecursiveB
func (x *LoopRecursiveA) HasB() bool
func (*LoopRecursiveA) ProtoMessage()
func (x *LoopRecursiveA) ProtoReflect() protoreflect.Message
func (x *LoopRecursiveA) Reset()
func (x *LoopRecursiveA) SetB(v *LoopRecursiveB)
func (x *LoopRecursiveA) String() string
type LoopRecursiveA_builder
func (b0 LoopRecursiveA_builder) Build() *LoopRecursiveA
type LoopRecursiveB
func (x *LoopRecursiveB) ClearA()
func (x *LoopRecursiveB) GetA() *LoopRecursiveA
func (x *LoopRecursiveB) HasA() bool
func (*LoopRecursiveB) ProtoMessage()
func (x *LoopRecursiveB) ProtoReflect() protoreflect.Message
func (x *LoopRecursiveB) Reset()
func (x *LoopRecursiveB) SetA(v *LoopRecursiveA)
func (x *LoopRecursiveB) String() string
type LoopRecursiveB_builder
func (b0 LoopRecursiveB_builder) Build() *LoopRecursiveB
type MismatchRules
func (x *MismatchRules) GetNoRule() bool
func (x *MismatchRules) GetStringFieldBoolRule() string
func (*MismatchRules) ProtoMessage()
func (x *MismatchRules) ProtoReflect() protoreflect.Message
func (x *MismatchRules) Reset()
func (x *MismatchRules) SetNoRule(v bool)
func (x *MismatchRules) SetStringFieldBoolRule(v string)
func (x *MismatchRules) String() string
type MismatchRules_builder
func (b0 MismatchRules_builder) Build() *MismatchRules
type MixedValidInvalidRules
func (x *MixedValidInvalidRules) GetStringFieldBoolRule() string
func (x *MixedValidInvalidRules) GetValidStringRule() string
func (*MixedValidInvalidRules) ProtoMessage()
func (x *MixedValidInvalidRules) ProtoReflect() protoreflect.Message
func (x *MixedValidInvalidRules) Reset()
func (x *MixedValidInvalidRules) SetStringFieldBoolRule(v string)
func (x *MixedValidInvalidRules) SetValidStringRule(v string)
func (x *MixedValidInvalidRules) String() string
type MixedValidInvalidRules_builder
func (b0 MixedValidInvalidRules_builder) Build() *MixedValidInvalidRules
type MsgHasMap
func (x *MsgHasMap) GetInt32Map() map[int32]int32
func (x *MsgHasMap) GetMessageMap() map[int64]*LoopRecursiveA
func (x *MsgHasMap) GetStringMap() map[string]string
func (*MsgHasMap) ProtoMessage()
func (x *MsgHasMap) ProtoReflect() protoreflect.Message
func (x *MsgHasMap) Reset()
func (x *MsgHasMap) SetInt32Map(v map[int32]int32)
func (x *MsgHasMap) SetMessageMap(v map[int64]*LoopRecursiveA)
func (x *MsgHasMap) SetStringMap(v map[string]string)
func (x *MsgHasMap) String() string
type MsgHasMap_builder
func (b0 MsgHasMap_builder) Build() *MsgHasMap
type MsgHasOneof
func (x *MsgHasOneof) ClearMsg()
func (x *MsgHasOneof) ClearO()
func (x *MsgHasOneof) ClearX()
func (x *MsgHasOneof) ClearY()
func (x *MsgHasOneof) GetMsg() *HasMsgExprs
func (x *MsgHasOneof) GetO() isMsgHasOneof_O
func (x *MsgHasOneof) GetX() string
func (x *MsgHasOneof) GetY() int32
func (x *MsgHasOneof) HasMsg() bool
func (x *MsgHasOneof) HasO() bool
func (x *MsgHasOneof) HasX() bool
func (x *MsgHasOneof) HasY() bool
func (*MsgHasOneof) ProtoMessage()
func (x *MsgHasOneof) ProtoReflect() protoreflect.Message
func (x *MsgHasOneof) Reset()
func (x *MsgHasOneof) SetMsg(v *HasMsgExprs)
func (x *MsgHasOneof) SetX(v string)
func (x *MsgHasOneof) SetY(v int32)
func (x *MsgHasOneof) String() string
func (x *MsgHasOneof) WhichO() case_MsgHasOneof_O
type MsgHasOneof_Msg
type MsgHasOneof_X
type MsgHasOneof_Y
type MsgHasOneof_builder
func (b0 MsgHasOneof_builder) Build() *MsgHasOneof
type MsgHasRepeated
func (x *MsgHasRepeated) GetX() []float32
func (x *MsgHasRepeated) GetY() []string
func (x *MsgHasRepeated) GetZ() []*HasMsgExprs
func (*MsgHasRepeated) ProtoMessage()
func (x *MsgHasRepeated) ProtoReflect() protoreflect.Message
func (x *MsgHasRepeated) Reset()
func (x *MsgHasRepeated) SetX(v []float32)
func (x *MsgHasRepeated) SetY(v []string)
func (x *MsgHasRepeated) SetZ(v []*HasMsgExprs)
func (x *MsgHasRepeated) String() string
type MsgHasRepeated_builder
func (b0 MsgHasRepeated_builder) Build() *MsgHasRepeated
type MultipleStepsTransitiveFieldRules
func (x *MultipleStepsTransitiveFieldRules) ClearApi()
func (x *MultipleStepsTransitiveFieldRules) GetApi() *apipb.Api
func (x *MultipleStepsTransitiveFieldRules) HasApi() bool
func (*MultipleStepsTransitiveFieldRules) ProtoMessage()
func (x *MultipleStepsTransitiveFieldRules) ProtoReflect() protoreflect.Message
func (x *MultipleStepsTransitiveFieldRules) Reset()
func (x *MultipleStepsTransitiveFieldRules) SetApi(v *apipb.Api)
func (x *MultipleStepsTransitiveFieldRules) String() string
type MultipleStepsTransitiveFieldRules_builder
func (b0 MultipleStepsTransitiveFieldRules_builder) Build() *MultipleStepsTransitiveFieldRules
type NestedRules
func (x *NestedRules) ClearField()
func (x *NestedRules) ClearOneofField()
func (x *NestedRules) ClearRequiredOneof()
func (x *NestedRules) GetField() *AllRuleTypes
func (x *NestedRules) GetField2() string
func (x *NestedRules) GetMapField() map[string]*AllRuleTypes
func (x *NestedRules) GetOneofField() string
func (x *NestedRules) GetRepeatedField() []*AllRuleTypes
func (x *NestedRules) GetRequiredOneof() isNestedRules_RequiredOneof
func (x *NestedRules) HasField() bool
func (x *NestedRules) HasOneofField() bool
func (x *NestedRules) HasRequiredOneof() bool
func (*NestedRules) ProtoMessage()
func (x *NestedRules) ProtoReflect() protoreflect.Message
func (x *NestedRules) Reset()
func (x *NestedRules) SetField(v *AllRuleTypes)
func (x *NestedRules) SetField2(v string)
func (x *NestedRules) SetMapField(v map[string]*AllRuleTypes)
func (x *NestedRules) SetOneofField(v string)
func (x *NestedRules) SetRepeatedField(v []*AllRuleTypes)
func (x *NestedRules) String() string
func (x *NestedRules) WhichRequiredOneof() case_NestedRules_RequiredOneof
type NestedRules_OneofField
type NestedRules_builder
func (b0 NestedRules_builder) Build() *NestedRules
type OneTwo
func (x *OneTwo) ClearField1()
func (x *OneTwo) ClearField2()
func (x *OneTwo) GetField1() *F1
func (x *OneTwo) GetField2() *F2
func (x *OneTwo) HasField1() bool
func (x *OneTwo) HasField2() bool
func (*OneTwo) ProtoMessage()
func (x *OneTwo) ProtoReflect() protoreflect.Message
func (x *OneTwo) Reset()
func (x *OneTwo) SetField1(v *F1)
func (x *OneTwo) SetField2(v *F2)
func (x *OneTwo) String() string
type OneTwo_builder
func (b0 OneTwo_builder) Build() *OneTwo
type Person
func (x *Person) ClearHome()
func (x *Person) GetEmail() string
func (x *Person) GetHome() *Coordinates
func (x *Person) GetId() uint64
func (x *Person) GetName() string
func (x *Person) HasHome() bool
func (*Person) ProtoMessage()
func (x *Person) ProtoReflect() protoreflect.Message
func (x *Person) Reset()
func (x *Person) SetEmail(v string)
func (x *Person) SetHome(v *Coordinates)
func (x *Person) SetId(v uint64)
func (x *Person) SetName(v string)
func (x *Person) String() string
type Person_builder
func (b0 Person_builder) Build() *Person
type Proto2Group
func (x *Proto2Group) ClearOptional()
func (x *Proto2Group) GetOptional() *Proto2Group_Optional
func (x *Proto2Group) HasOptional() bool
func (*Proto2Group) ProtoMessage()
func (x *Proto2Group) ProtoReflect() protoreflect.Message
func (x *Proto2Group) Reset()
func (x *Proto2Group) SetOptional(v *Proto2Group_Optional)
func (x *Proto2Group) String() string
type Proto2Group_Optional
func (x *Proto2Group_Optional) ClearValue()
func (x *Proto2Group_Optional) GetValue() int32
func (x *Proto2Group_Optional) HasValue() bool
func (*Proto2Group_Optional) ProtoMessage()
func (x *Proto2Group_Optional) ProtoReflect() protoreflect.Message
func (x *Proto2Group_Optional) Reset()
func (x *Proto2Group_Optional) SetValue(v int32)
func (x *Proto2Group_Optional) String() string
type Proto2Group_Optional_builder
func (b0 Proto2Group_Optional_builder) Build() *Proto2Group_Optional
type Proto2Group_builder
func (b0 Proto2Group_builder) Build() *Proto2Group
type RepeatedItemCel
func (x *RepeatedItemCel) GetPaths() []string
func (*RepeatedItemCel) ProtoMessage()
func (x *RepeatedItemCel) ProtoReflect() protoreflect.Message
func (x *RepeatedItemCel) Reset()
func (x *RepeatedItemCel) SetPaths(v []string)
func (x *RepeatedItemCel) String() string
type RepeatedItemCel_builder
func (b0 RepeatedItemCel_builder) Build() *RepeatedItemCel
type SelfRecursive
func (x *SelfRecursive) ClearTurtle()
func (x *SelfRecursive) GetTurtle() *SelfRecursive
func (x *SelfRecursive) GetX() int32
func (x *SelfRecursive) HasTurtle() bool
func (*SelfRecursive) ProtoMessage()
func (x *SelfRecursive) ProtoReflect() protoreflect.Message
func (x *SelfRecursive) Reset()
func (x *SelfRecursive) SetTurtle(v *SelfRecursive)
func (x *SelfRecursive) SetX(v int32)
func (x *SelfRecursive) String() string
type SelfRecursive_builder
func (b0 SelfRecursive_builder) Build() *SelfRecursive
type SelfReferentialMap
func (x *SelfReferentialMap) ClearName()
func (x *SelfReferentialMap) GetChildren() map[string]*SelfReferentialMap
func (x *SelfReferentialMap) GetName() string
func (x *SelfReferentialMap) HasName() bool
func (*SelfReferentialMap) ProtoMessage()
func (x *SelfReferentialMap) ProtoReflect() protoreflect.Message
func (x *SelfReferentialMap) Reset()
func (x *SelfReferentialMap) SetChildren(v map[string]*SelfReferentialMap)
func (x *SelfReferentialMap) SetName(v string)
func (x *SelfReferentialMap) String() string
type SelfReferentialMap_builder
func (b0 SelfReferentialMap_builder) Build() *SelfReferentialMap
type SelfReferentialRepeated
func (x *SelfReferentialRepeated) ClearName()
func (x *SelfReferentialRepeated) GetChildren() []*SelfReferentialRepeated
func (x *SelfReferentialRepeated) GetName() string
func (x *SelfReferentialRepeated) HasName() bool
func (*SelfReferentialRepeated) ProtoMessage()
func (x *SelfReferentialRepeated) ProtoReflect() protoreflect.Message
func (x *SelfReferentialRepeated) Reset()
func (x *SelfReferentialRepeated) SetChildren(v []*SelfReferentialRepeated)
func (x *SelfReferentialRepeated) SetName(v string)
func (x *SelfReferentialRepeated) String() string
type SelfReferentialRepeated_builder
func (b0 SelfReferentialRepeated_builder) Build() *SelfReferentialRepeated
type Simple
func (x *Simple) GetS() string
func (*Simple) ProtoMessage()
func (x *Simple) ProtoReflect() protoreflect.Message
func (x *Simple) Reset()
func (x *Simple) SetS(v string)
func (x *Simple) String() string
type Simple_builder
func (b0 Simple_builder) Build() *Simple
type TransitiveFieldRule
func (x *TransitiveFieldRule) ClearMask()
func (x *TransitiveFieldRule) GetMask() *fieldmaskpb.FieldMask
func (x *TransitiveFieldRule) HasMask() bool
func (*TransitiveFieldRule) ProtoMessage()
func (x *TransitiveFieldRule) ProtoReflect() protoreflect.Message
func (x *TransitiveFieldRule) Reset()
func (x *TransitiveFieldRule) SetMask(v *fieldmaskpb.FieldMask)
func (x *TransitiveFieldRule) String() string
type TransitiveFieldRule_builder
func (b0 TransitiveFieldRule_builder) Build() *TransitiveFieldRule
type TwoOne
func (x *TwoOne) ClearField1()
func (x *TwoOne) ClearField2()
func (x *TwoOne) GetField1() *F1
func (x *TwoOne) GetField2() *F2
func (x *TwoOne) HasField1() bool
func (x *TwoOne) HasField2() bool
func (*TwoOne) ProtoMessage()
func (x *TwoOne) ProtoReflect() protoreflect.Message
func (x *TwoOne) Reset()
func (x *TwoOne) SetField1(v *F1)
func (x *TwoOne) SetField2(v *F2)
func (x *TwoOne) String() string
type TwoOne_builder
func (b0 TwoOne_builder) Build() *TwoOne
Constants ¶
View Source
const AllRuleTypes_OneofField_case case_AllRuleTypes_RequiredOneof = 2
View Source
const AllRuleTypes_RequiredOneof_not_set_case case_AllRuleTypes_RequiredOneof = 0
View Source
const BenchComplexSchema_Choice_not_set_case case_BenchComplexSchema_Choice = 0
View Source
const BenchComplexSchema_OneofI32_case case_BenchComplexSchema_Choice = 31
View Source
const BenchComplexSchema_OneofMsg_case case_BenchComplexSchema_Choice = 32
View Source
const BenchComplexSchema_OneofStr_case case_BenchComplexSchema_Choice = 30
View Source
const MsgHasOneof_Msg_case case_MsgHasOneof_O = 3
View Source
const MsgHasOneof_O_not_set_case case_MsgHasOneof_O = 0
View Source
const MsgHasOneof_X_case case_MsgHasOneof_O = 1
View Source
const MsgHasOneof_Y_case case_MsgHasOneof_O = 2
View Source
const NestedRules_OneofField_case case_NestedRules_RequiredOneof = 5
View Source
const NestedRules_RequiredOneof_not_set_case case_NestedRules_RequiredOneof = 0
Variables ¶
View Source
var (
	BenchEnum_name = map[int32]string{
		0: "BENCH_ENUM_UNSPECIFIED",
		1: "BENCH_ENUM_ONE",
		2: "BENCH_ENUM_TWO",
	}
	BenchEnum_value = map[string]int32{
		"BENCH_ENUM_UNSPECIFIED": 0,
		"BENCH_ENUM_ONE":         1,
		"BENCH_ENUM_TWO":         2,
	}
)

Enum value maps for BenchEnum.

View Source
var (
	// repeated int32 abs_not_in = 1800;
	E_AbsNotIn = &file_tests_example_v1_predefined_proto_extTypes[0]
)

Extension fields to validate.Int32Rules.

View Source
var (
	// optional google.protobuf.FieldMask fm_rules_extension = 1801;
	E_FmRulesExtension = &file_tests_example_v1_predefined_proto_extTypes[2]
)

Extension fields to validate.FieldMaskRules.

View Source
var (
	// optional bool this_equals_rule = 1800;
	E_ThisEqualsRule = &file_tests_example_v1_predefined_proto_extTypes[1]
)

Extension fields to validate.BoolRules.

View Source
var File_tests_example_v1_bench_proto protoreflect.FileDescriptor
View Source
var File_tests_example_v1_compile_proto protoreflect.FileDescriptor
View Source
var File_tests_example_v1_example_proto protoreflect.FileDescriptor
View Source
var File_tests_example_v1_filter_proto protoreflect.FileDescriptor
View Source
var File_tests_example_v1_groups_proto2_proto protoreflect.FileDescriptor
View Source
var File_tests_example_v1_predefined_proto protoreflect.FileDescriptor
View Source
var File_tests_example_v1_validations_proto protoreflect.FileDescriptor
Functions ¶

This section is empty.

Types ¶
type AllRuleTypes ¶
type AllRuleTypes struct {
	Field int32 `protobuf:"varint,1,opt,name=field,proto3" json:"field,omitempty"`
	// Types that are valid to be assigned to RequiredOneof:
	//
	//	*AllRuleTypes_OneofField
	RequiredOneof isAllRuleTypes_RequiredOneof `protobuf_oneof:"required_oneof"`
	// contains filtered or unexported fields
}
func (*AllRuleTypes) ClearOneofField ¶
func (x *AllRuleTypes) ClearOneofField()
func (*AllRuleTypes) ClearRequiredOneof ¶
func (x *AllRuleTypes) ClearRequiredOneof()
func (*AllRuleTypes) GetField ¶
func (x *AllRuleTypes) GetField() int32
func (*AllRuleTypes) GetOneofField ¶
func (x *AllRuleTypes) GetOneofField() string
func (*AllRuleTypes) GetRequiredOneof ¶
func (x *AllRuleTypes) GetRequiredOneof() isAllRuleTypes_RequiredOneof
func (*AllRuleTypes) HasOneofField ¶
func (x *AllRuleTypes) HasOneofField() bool
func (*AllRuleTypes) HasRequiredOneof ¶
func (x *AllRuleTypes) HasRequiredOneof() bool
func (*AllRuleTypes) ProtoMessage ¶
func (*AllRuleTypes) ProtoMessage()
func (*AllRuleTypes) ProtoReflect ¶
func (x *AllRuleTypes) ProtoReflect() protoreflect.Message
func (*AllRuleTypes) Reset ¶
func (x *AllRuleTypes) Reset()
func (*AllRuleTypes) SetField ¶
func (x *AllRuleTypes) SetField(v int32)
func (*AllRuleTypes) SetOneofField ¶
func (x *AllRuleTypes) SetOneofField(v string)
func (*AllRuleTypes) String ¶
func (x *AllRuleTypes) String() string
func (*AllRuleTypes) WhichRequiredOneof ¶
func (x *AllRuleTypes) WhichRequiredOneof() case_AllRuleTypes_RequiredOneof
type AllRuleTypes_OneofField ¶
type AllRuleTypes_OneofField struct {
	OneofField string `protobuf:"bytes,2,opt,name=oneof_field,json=oneofField,proto3,oneof"`
}
type AllRuleTypes_builder ¶
type AllRuleTypes_builder struct {
	Field int32
	// Fields of oneof RequiredOneof:
	OneofField *string
	// contains filtered or unexported fields
}
func (AllRuleTypes_builder) Build ¶
func (b0 AllRuleTypes_builder) Build() *AllRuleTypes
type BenchComplexSchema ¶
added in v1.1.1
type BenchComplexSchema struct {

	// Scalars with various constraints
	S1   string  `protobuf:"bytes,1,opt,name=s1,proto3" json:"s1,omitempty"`
	S2   string  `protobuf:"bytes,2,opt,name=s2,proto3" json:"s2,omitempty"`
	I32  int32   `protobuf:"varint,3,opt,name=i32,proto3" json:"i32,omitempty"`
	I64  int64   `protobuf:"varint,4,opt,name=i64,proto3" json:"i64,omitempty"`
	U32  uint32  `protobuf:"varint,5,opt,name=u32,proto3" json:"u32,omitempty"`
	U64  uint64  `protobuf:"varint,6,opt,name=u64,proto3" json:"u64,omitempty"`
	Si32 int32   `protobuf:"zigzag32,7,opt,name=si32,proto3" json:"si32,omitempty"`
	Si64 int64   `protobuf:"zigzag64,8,opt,name=si64,proto3" json:"si64,omitempty"`
	F32  uint32  `protobuf:"fixed32,9,opt,name=f32,proto3" json:"f32,omitempty"`
	F64  uint64  `protobuf:"fixed64,10,opt,name=f64,proto3" json:"f64,omitempty"`
	Sf32 int32   `protobuf:"fixed32,11,opt,name=sf32,proto3" json:"sf32,omitempty"`
	Sf64 int64   `protobuf:"fixed64,12,opt,name=sf64,proto3" json:"sf64,omitempty"`
	Fl   float32 `protobuf:"fixed32,13,opt,name=fl,proto3" json:"fl,omitempty"`
	Db   float64 `protobuf:"fixed64,14,opt,name=db,proto3" json:"db,omitempty"`
	Bl   bool    `protobuf:"varint,15,opt,name=bl,proto3" json:"bl,omitempty"`
	By   []byte  `protobuf:"bytes,16,opt,name=by,proto3" json:"by,omitempty"`
	// Nested message
	Nested *BenchScalar `protobuf:"bytes,17,opt,name=nested,proto3" json:"nested,omitempty"`
	// Self-referential
	SelfRef *BenchComplexSchema `protobuf:"bytes,18,opt,name=self_ref,json=selfRef,proto3" json:"self_ref,omitempty"`
	// Repeated scalars
	RepStr   []string `protobuf:"bytes,19,rep,name=rep_str,json=repStr,proto3" json:"rep_str,omitempty"`
	RepI32   []int32  `protobuf:"varint,20,rep,packed,name=rep_i32,json=repI32,proto3" json:"rep_i32,omitempty"`
	RepBytes [][]byte `protobuf:"bytes,21,rep,name=rep_bytes,json=repBytes,proto3" json:"rep_bytes,omitempty"`
	// Repeated messages
	RepMsg []*BenchScalar `protobuf:"bytes,22,rep,name=rep_msg,json=repMsg,proto3" json:"rep_msg,omitempty"`
	// Maps with scalar keys and values
	MapStrStr   map[string]string `` /* 165-byte string literal not displayed */
	MapI32I64   map[int32]int64   `` /* 167-byte string literal not displayed */
	MapU64Bool  map[uint64]bool   `` /* 170-byte string literal not displayed */
	MapStrBytes map[string][]byte `` /* 171-byte string literal not displayed */
	// Maps with message values
	MapStrMsg map[string]*BenchScalar `` /* 165-byte string literal not displayed */
	MapI64Msg map[int64]*BenchScalar  `` /* 166-byte string literal not displayed */
	// Enum field
	EnumField BenchEnum `protobuf:"varint,29,opt,name=enum_field,json=enumField,proto3,enum=tests.example.v1.BenchEnum" json:"enum_field,omitempty"`
	// Oneof
	//
	// Types that are valid to be assigned to Choice:
	//
	//	*BenchComplexSchema_OneofStr
	//	*BenchComplexSchema_OneofI32
	//	*BenchComplexSchema_OneofMsg
	Choice isBenchComplexSchema_Choice `protobuf_oneof:"choice"`
	// contains filtered or unexported fields
}

Complex schema benchmark - tests compile-time registry copying overhead

func (*BenchComplexSchema) ClearChoice ¶
added in v1.1.1
func (x *BenchComplexSchema) ClearChoice()
func (*BenchComplexSchema) ClearNested ¶
added in v1.1.1
func (x *BenchComplexSchema) ClearNested()
func (*BenchComplexSchema) ClearOneofI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) ClearOneofI32()
func (*BenchComplexSchema) ClearOneofMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) ClearOneofMsg()
func (*BenchComplexSchema) ClearOneofStr ¶
added in v1.1.1
func (x *BenchComplexSchema) ClearOneofStr()
func (*BenchComplexSchema) ClearSelfRef ¶
added in v1.1.1
func (x *BenchComplexSchema) ClearSelfRef()
func (*BenchComplexSchema) GetBl ¶
added in v1.1.1
func (x *BenchComplexSchema) GetBl() bool
func (*BenchComplexSchema) GetBy ¶
added in v1.1.1
func (x *BenchComplexSchema) GetBy() []byte
func (*BenchComplexSchema) GetChoice ¶
added in v1.1.1
func (x *BenchComplexSchema) GetChoice() isBenchComplexSchema_Choice
func (*BenchComplexSchema) GetDb ¶
added in v1.1.1
func (x *BenchComplexSchema) GetDb() float64
func (*BenchComplexSchema) GetEnumField ¶
added in v1.1.1
func (x *BenchComplexSchema) GetEnumField() BenchEnum
func (*BenchComplexSchema) GetF32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetF32() uint32
func (*BenchComplexSchema) GetF64 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetF64() uint64
func (*BenchComplexSchema) GetFl ¶
added in v1.1.1
func (x *BenchComplexSchema) GetFl() float32
func (*BenchComplexSchema) GetI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetI32() int32
func (*BenchComplexSchema) GetI64 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetI64() int64
func (*BenchComplexSchema) GetMapI32I64 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetMapI32I64() map[int32]int64
func (*BenchComplexSchema) GetMapI64Msg ¶
added in v1.1.1
func (x *BenchComplexSchema) GetMapI64Msg() map[int64]*BenchScalar
func (*BenchComplexSchema) GetMapStrBytes ¶
added in v1.1.1
func (x *BenchComplexSchema) GetMapStrBytes() map[string][]byte
func (*BenchComplexSchema) GetMapStrMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) GetMapStrMsg() map[string]*BenchScalar
func (*BenchComplexSchema) GetMapStrStr ¶
added in v1.1.1
func (x *BenchComplexSchema) GetMapStrStr() map[string]string
func (*BenchComplexSchema) GetMapU64Bool ¶
added in v1.1.1
func (x *BenchComplexSchema) GetMapU64Bool() map[uint64]bool
func (*BenchComplexSchema) GetNested ¶
added in v1.1.1
func (x *BenchComplexSchema) GetNested() *BenchScalar
func (*BenchComplexSchema) GetOneofI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetOneofI32() int32
func (*BenchComplexSchema) GetOneofMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) GetOneofMsg() *BenchScalar
func (*BenchComplexSchema) GetOneofStr ¶
added in v1.1.1
func (x *BenchComplexSchema) GetOneofStr() string
func (*BenchComplexSchema) GetRepBytes ¶
added in v1.1.1
func (x *BenchComplexSchema) GetRepBytes() [][]byte
func (*BenchComplexSchema) GetRepI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetRepI32() []int32
func (*BenchComplexSchema) GetRepMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) GetRepMsg() []*BenchScalar
func (*BenchComplexSchema) GetRepStr ¶
added in v1.1.1
func (x *BenchComplexSchema) GetRepStr() []string
func (*BenchComplexSchema) GetS1 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetS1() string
func (*BenchComplexSchema) GetS2 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetS2() string
func (*BenchComplexSchema) GetSelfRef ¶
added in v1.1.1
func (x *BenchComplexSchema) GetSelfRef() *BenchComplexSchema
func (*BenchComplexSchema) GetSf32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetSf32() int32
func (*BenchComplexSchema) GetSf64 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetSf64() int64
func (*BenchComplexSchema) GetSi32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetSi32() int32
func (*BenchComplexSchema) GetSi64 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetSi64() int64
func (*BenchComplexSchema) GetU32 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetU32() uint32
func (*BenchComplexSchema) GetU64 ¶
added in v1.1.1
func (x *BenchComplexSchema) GetU64() uint64
func (*BenchComplexSchema) HasChoice ¶
added in v1.1.1
func (x *BenchComplexSchema) HasChoice() bool
func (*BenchComplexSchema) HasNested ¶
added in v1.1.1
func (x *BenchComplexSchema) HasNested() bool
func (*BenchComplexSchema) HasOneofI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) HasOneofI32() bool
func (*BenchComplexSchema) HasOneofMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) HasOneofMsg() bool
func (*BenchComplexSchema) HasOneofStr ¶
added in v1.1.1
func (x *BenchComplexSchema) HasOneofStr() bool
func (*BenchComplexSchema) HasSelfRef ¶
added in v1.1.1
func (x *BenchComplexSchema) HasSelfRef() bool
func (*BenchComplexSchema) ProtoMessage ¶
added in v1.1.1
func (*BenchComplexSchema) ProtoMessage()
func (*BenchComplexSchema) ProtoReflect ¶
added in v1.1.1
func (x *BenchComplexSchema) ProtoReflect() protoreflect.Message
func (*BenchComplexSchema) Reset ¶
added in v1.1.1
func (x *BenchComplexSchema) Reset()
func (*BenchComplexSchema) SetBl ¶
added in v1.1.1
func (x *BenchComplexSchema) SetBl(v bool)
func (*BenchComplexSchema) SetBy ¶
added in v1.1.1
func (x *BenchComplexSchema) SetBy(v []byte)
func (*BenchComplexSchema) SetDb ¶
added in v1.1.1
func (x *BenchComplexSchema) SetDb(v float64)
func (*BenchComplexSchema) SetEnumField ¶
added in v1.1.1
func (x *BenchComplexSchema) SetEnumField(v BenchEnum)
func (*BenchComplexSchema) SetF32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetF32(v uint32)
func (*BenchComplexSchema) SetF64 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetF64(v uint64)
func (*BenchComplexSchema) SetFl ¶
added in v1.1.1
func (x *BenchComplexSchema) SetFl(v float32)
func (*BenchComplexSchema) SetI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetI32(v int32)
func (*BenchComplexSchema) SetI64 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetI64(v int64)
func (*BenchComplexSchema) SetMapI32I64 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetMapI32I64(v map[int32]int64)
func (*BenchComplexSchema) SetMapI64Msg ¶
added in v1.1.1
func (x *BenchComplexSchema) SetMapI64Msg(v map[int64]*BenchScalar)
func (*BenchComplexSchema) SetMapStrBytes ¶
added in v1.1.1
func (x *BenchComplexSchema) SetMapStrBytes(v map[string][]byte)
func (*BenchComplexSchema) SetMapStrMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) SetMapStrMsg(v map[string]*BenchScalar)
func (*BenchComplexSchema) SetMapStrStr ¶
added in v1.1.1
func (x *BenchComplexSchema) SetMapStrStr(v map[string]string)
func (*BenchComplexSchema) SetMapU64Bool ¶
added in v1.1.1
func (x *BenchComplexSchema) SetMapU64Bool(v map[uint64]bool)
func (*BenchComplexSchema) SetNested ¶
added in v1.1.1
func (x *BenchComplexSchema) SetNested(v *BenchScalar)
func (*BenchComplexSchema) SetOneofI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetOneofI32(v int32)
func (*BenchComplexSchema) SetOneofMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) SetOneofMsg(v *BenchScalar)
func (*BenchComplexSchema) SetOneofStr ¶
added in v1.1.1
func (x *BenchComplexSchema) SetOneofStr(v string)
func (*BenchComplexSchema) SetRepBytes ¶
added in v1.1.1
func (x *BenchComplexSchema) SetRepBytes(v [][]byte)
func (*BenchComplexSchema) SetRepI32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetRepI32(v []int32)
func (*BenchComplexSchema) SetRepMsg ¶
added in v1.1.1
func (x *BenchComplexSchema) SetRepMsg(v []*BenchScalar)
func (*BenchComplexSchema) SetRepStr ¶
added in v1.1.1
func (x *BenchComplexSchema) SetRepStr(v []string)
func (*BenchComplexSchema) SetS1 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetS1(v string)
func (*BenchComplexSchema) SetS2 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetS2(v string)
func (*BenchComplexSchema) SetSelfRef ¶
added in v1.1.1
func (x *BenchComplexSchema) SetSelfRef(v *BenchComplexSchema)
func (*BenchComplexSchema) SetSf32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetSf32(v int32)
func (*BenchComplexSchema) SetSf64 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetSf64(v int64)
func (*BenchComplexSchema) SetSi32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetSi32(v int32)
func (*BenchComplexSchema) SetSi64 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetSi64(v int64)
func (*BenchComplexSchema) SetU32 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetU32(v uint32)
func (*BenchComplexSchema) SetU64 ¶
added in v1.1.1
func (x *BenchComplexSchema) SetU64(v uint64)
func (*BenchComplexSchema) String ¶
added in v1.1.1
func (x *BenchComplexSchema) String() string
func (*BenchComplexSchema) WhichChoice ¶
added in v1.1.1
func (x *BenchComplexSchema) WhichChoice() case_BenchComplexSchema_Choice
type BenchComplexSchema_OneofI32 ¶
added in v1.1.1
type BenchComplexSchema_OneofI32 struct {
	OneofI32 int32 `protobuf:"varint,31,opt,name=oneof_i32,json=oneofI32,proto3,oneof"`
}
type BenchComplexSchema_OneofMsg ¶
added in v1.1.1
type BenchComplexSchema_OneofMsg struct {
	OneofMsg *BenchScalar `protobuf:"bytes,32,opt,name=oneof_msg,json=oneofMsg,proto3,oneof"`
}
type BenchComplexSchema_OneofStr ¶
added in v1.1.1
type BenchComplexSchema_OneofStr struct {
	OneofStr string `protobuf:"bytes,30,opt,name=oneof_str,json=oneofStr,proto3,oneof"`
}
type BenchComplexSchema_builder ¶
added in v1.1.1
type BenchComplexSchema_builder struct {

	// Scalars with various constraints
	S1   string
	S2   string
	I32  int32
	I64  int64
	U32  uint32
	U64  uint64
	Si32 int32
	Si64 int64
	F32  uint32
	F64  uint64
	Sf32 int32
	Sf64 int64
	Fl   float32
	Db   float64
	Bl   bool
	By   []byte
	// Nested message
	Nested *BenchScalar
	// Self-referential
	SelfRef *BenchComplexSchema
	// Repeated scalars
	RepStr   []string
	RepI32   []int32
	RepBytes [][]byte
	// Repeated messages
	RepMsg []*BenchScalar
	// Maps with scalar keys and values
	MapStrStr   map[string]string
	MapI32I64   map[int32]int64
	MapU64Bool  map[uint64]bool
	MapStrBytes map[string][]byte
	// Maps with message values
	MapStrMsg map[string]*BenchScalar
	MapI64Msg map[int64]*BenchScalar
	// Enum field
	EnumField BenchEnum

	// Fields of oneof Choice:
	OneofStr *string
	OneofI32 *int32
	OneofMsg *BenchScalar
	// contains filtered or unexported fields
}
func (BenchComplexSchema_builder) Build ¶
added in v1.1.1
func (b0 BenchComplexSchema_builder) Build() *BenchComplexSchema
type BenchEnum ¶
added in v1.1.1
type BenchEnum int32
const (
	BenchEnum_BENCH_ENUM_UNSPECIFIED BenchEnum = 0
	BenchEnum_BENCH_ENUM_ONE         BenchEnum = 1
	BenchEnum_BENCH_ENUM_TWO         BenchEnum = 2
)
func (BenchEnum) Descriptor ¶
added in v1.1.1
func (BenchEnum) Descriptor() protoreflect.EnumDescriptor
func (BenchEnum) Enum ¶
added in v1.1.1
func (x BenchEnum) Enum() *BenchEnum
func (BenchEnum) Number ¶
added in v1.1.1
func (x BenchEnum) Number() protoreflect.EnumNumber
func (BenchEnum) String ¶
added in v1.1.1
func (x BenchEnum) String() string
func (BenchEnum) Type ¶
added in v1.1.1
func (BenchEnum) Type() protoreflect.EnumType
type BenchMap ¶
added in v1.1.1
type BenchMap struct {
	Entries map[string]string `` /* 141-byte string literal not displayed */
	// contains filtered or unexported fields
}

Map validation benchmark - tests thisToCel() map copying overhead

func (*BenchMap) GetEntries ¶
added in v1.1.1
func (x *BenchMap) GetEntries() map[string]string
func (*BenchMap) ProtoMessage ¶
added in v1.1.1
func (*BenchMap) ProtoMessage()
func (*BenchMap) ProtoReflect ¶
added in v1.1.1
func (x *BenchMap) ProtoReflect() protoreflect.Message
func (*BenchMap) Reset ¶
added in v1.1.1
func (x *BenchMap) Reset()
func (*BenchMap) SetEntries ¶
added in v1.1.1
func (x *BenchMap) SetEntries(v map[string]string)
func (*BenchMap) String ¶
added in v1.1.1
func (x *BenchMap) String() string
type BenchMap_builder ¶
added in v1.1.1
type BenchMap_builder struct {
	Entries map[string]string
	// contains filtered or unexported fields
}
func (BenchMap_builder) Build ¶
added in v1.1.1
func (b0 BenchMap_builder) Build() *BenchMap
type BenchRepeatedBytesUnique ¶
added in v1.0.1
type BenchRepeatedBytesUnique struct {
	X [][]byte `protobuf:"bytes,1,rep,name=x,proto3" json:"x,omitempty"`
	// contains filtered or unexported fields
}
func (*BenchRepeatedBytesUnique) GetX ¶
added in v1.0.1
func (x *BenchRepeatedBytesUnique) GetX() [][]byte
func (*BenchRepeatedBytesUnique) ProtoMessage ¶
added in v1.0.1
func (*BenchRepeatedBytesUnique) ProtoMessage()
func (*BenchRepeatedBytesUnique) ProtoReflect ¶
added in v1.0.1
func (x *BenchRepeatedBytesUnique) ProtoReflect() protoreflect.Message
func (*BenchRepeatedBytesUnique) Reset ¶
added in v1.0.1
func (x *BenchRepeatedBytesUnique) Reset()
func (*BenchRepeatedBytesUnique) SetX ¶
added in v1.0.1
func (x *BenchRepeatedBytesUnique) SetX(v [][]byte)
func (*BenchRepeatedBytesUnique) String ¶
added in v1.0.1
func (x *BenchRepeatedBytesUnique) String() string
type BenchRepeatedBytesUnique_builder ¶
added in v1.0.1
type BenchRepeatedBytesUnique_builder struct {
	X [][]byte
	// contains filtered or unexported fields
}
func (BenchRepeatedBytesUnique_builder) Build ¶
added in v1.0.1
func (b0 BenchRepeatedBytesUnique_builder) Build() *BenchRepeatedBytesUnique
type BenchRepeatedMessage ¶
added in v1.0.1
type BenchRepeatedMessage struct {
	X []*BenchScalar `protobuf:"bytes,1,rep,name=x,proto3" json:"x,omitempty"`
	// contains filtered or unexported fields
}
func (*BenchRepeatedMessage) GetX ¶
added in v1.0.1
func (x *BenchRepeatedMessage) GetX() []*BenchScalar
func (*BenchRepeatedMessage) ProtoMessage ¶
added in v1.0.1
func (*BenchRepeatedMessage) ProtoMessage()
func (*BenchRepeatedMessage) ProtoReflect ¶
added in v1.0.1
func (x *BenchRepeatedMessage) ProtoReflect() protoreflect.Message
func (*BenchRepeatedMessage) Reset ¶
added in v1.0.1
func (x *BenchRepeatedMessage) Reset()
func (*BenchRepeatedMessage) SetX ¶
added in v1.0.1
func (x *BenchRepeatedMessage) SetX(v []*BenchScalar)
func (*BenchRepeatedMessage) String ¶
added in v1.0.1
func (x *BenchRepeatedMessage) String() string
type BenchRepeatedMessage_builder ¶
added in v1.0.1
type BenchRepeatedMessage_builder struct {
	X []*BenchScalar
	// contains filtered or unexported fields
}
func (BenchRepeatedMessage_builder) Build ¶
added in v1.0.1
func (b0 BenchRepeatedMessage_builder) Build() *BenchRepeatedMessage
type BenchRepeatedScalar ¶
added in v1.0.1
type BenchRepeatedScalar struct {
	X []int32 `protobuf:"varint,1,rep,packed,name=x,proto3" json:"x,omitempty"`
	// contains filtered or unexported fields
}
func (*BenchRepeatedScalar) GetX ¶
added in v1.0.1
func (x *BenchRepeatedScalar) GetX() []int32
func (*BenchRepeatedScalar) ProtoMessage ¶
added in v1.0.1
func (*BenchRepeatedScalar) ProtoMessage()
func (*BenchRepeatedScalar) ProtoReflect ¶
added in v1.0.1
func (x *BenchRepeatedScalar) ProtoReflect() protoreflect.Message
func (*BenchRepeatedScalar) Reset ¶
added in v1.0.1
func (x *BenchRepeatedScalar) Reset()
func (*BenchRepeatedScalar) SetX ¶
added in v1.0.1
func (x *BenchRepeatedScalar) SetX(v []int32)
func (*BenchRepeatedScalar) String ¶
added in v1.0.1
func (x *BenchRepeatedScalar) String() string
type BenchRepeatedScalarUnique ¶
added in v1.0.1
type BenchRepeatedScalarUnique struct {
	X []float32 `protobuf:"fixed32,1,rep,packed,name=x,proto3" json:"x,omitempty"`
	// contains filtered or unexported fields
}
func (*BenchRepeatedScalarUnique) GetX ¶
added in v1.0.1
func (x *BenchRepeatedScalarUnique) GetX() []float32
func (*BenchRepeatedScalarUnique) ProtoMessage ¶
added in v1.0.1
func (*BenchRepeatedScalarUnique) ProtoMessage()
func (*BenchRepeatedScalarUnique) ProtoReflect ¶
added in v1.0.1
func (x *BenchRepeatedScalarUnique) ProtoReflect() protoreflect.Message
func (*BenchRepeatedScalarUnique) Reset ¶
added in v1.0.1
func (x *BenchRepeatedScalarUnique) Reset()
func (*BenchRepeatedScalarUnique) SetX ¶
added in v1.0.1
func (x *BenchRepeatedScalarUnique) SetX(v []float32)
func (*BenchRepeatedScalarUnique) String ¶
added in v1.0.1
func (x *BenchRepeatedScalarUnique) String() string
type BenchRepeatedScalarUnique_builder ¶
added in v1.0.1
type BenchRepeatedScalarUnique_builder struct {
	X []float32
	// contains filtered or unexported fields
}
func (BenchRepeatedScalarUnique_builder) Build ¶
added in v1.0.1
func (b0 BenchRepeatedScalarUnique_builder) Build() *BenchRepeatedScalarUnique
type BenchRepeatedScalar_builder ¶
added in v1.0.1
type BenchRepeatedScalar_builder struct {
	X []int32
	// contains filtered or unexported fields
}
func (BenchRepeatedScalar_builder) Build ¶
added in v1.0.1
func (b0 BenchRepeatedScalar_builder) Build() *BenchRepeatedScalar
type BenchScalar ¶
added in v1.0.1
type BenchScalar struct {
	X int32 `protobuf:"varint,1,opt,name=x,proto3" json:"x,omitempty"`
	// contains filtered or unexported fields
}
func (*BenchScalar) GetX ¶
added in v1.0.1
func (x *BenchScalar) GetX() int32
func (*BenchScalar) ProtoMessage ¶
added in v1.0.1
func (*BenchScalar) ProtoMessage()
func (*BenchScalar) ProtoReflect ¶
added in v1.0.1
func (x *BenchScalar) ProtoReflect() protoreflect.Message
func (*BenchScalar) Reset ¶
added in v1.0.1
func (x *BenchScalar) Reset()
func (*BenchScalar) SetX ¶
added in v1.0.1
func (x *BenchScalar) SetX(v int32)
func (*BenchScalar) String ¶
added in v1.0.1
func (x *BenchScalar) String() string
type BenchScalar_builder ¶
added in v1.0.1
type BenchScalar_builder struct {
	X int32
	// contains filtered or unexported fields
}
func (BenchScalar_builder) Build ¶
added in v1.0.1
func (b0 BenchScalar_builder) Build() *BenchScalar
type CelMapOnARepeated ¶
type CelMapOnARepeated struct {
	Values []*CelMapOnARepeated_Value `protobuf:"bytes,1,rep,name=values,proto3" json:"values,omitempty"`
	// contains filtered or unexported fields
}

https://github.com/bufbuild/protovalidate/issues/92

func (*CelMapOnARepeated) GetValues ¶
func (x *CelMapOnARepeated) GetValues() []*CelMapOnARepeated_Value
func (*CelMapOnARepeated) ProtoMessage ¶
func (*CelMapOnARepeated) ProtoMessage()
func (*CelMapOnARepeated) ProtoReflect ¶
func (x *CelMapOnARepeated) ProtoReflect() protoreflect.Message
func (*CelMapOnARepeated) Reset ¶
func (x *CelMapOnARepeated) Reset()
func (*CelMapOnARepeated) SetValues ¶
func (x *CelMapOnARepeated) SetValues(v []*CelMapOnARepeated_Value)
func (*CelMapOnARepeated) String ¶
func (x *CelMapOnARepeated) String() string
type CelMapOnARepeated_Value ¶
type CelMapOnARepeated_Value struct {
	Name string `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	// contains filtered or unexported fields
}
func (*CelMapOnARepeated_Value) GetName ¶
func (x *CelMapOnARepeated_Value) GetName() string
func (*CelMapOnARepeated_Value) ProtoMessage ¶
func (*CelMapOnARepeated_Value) ProtoMessage()
func (*CelMapOnARepeated_Value) ProtoReflect ¶
func (x *CelMapOnARepeated_Value) ProtoReflect() protoreflect.Message
func (*CelMapOnARepeated_Value) Reset ¶
func (x *CelMapOnARepeated_Value) Reset()
func (*CelMapOnARepeated_Value) SetName ¶
func (x *CelMapOnARepeated_Value) SetName(v string)
func (*CelMapOnARepeated_Value) String ¶
func (x *CelMapOnARepeated_Value) String() string
type CelMapOnARepeated_Value_builder ¶
type CelMapOnARepeated_Value_builder struct {
	Name string
	// contains filtered or unexported fields
}
func (CelMapOnARepeated_Value_builder) Build ¶
func (b0 CelMapOnARepeated_Value_builder) Build() *CelMapOnARepeated_Value
type CelMapOnARepeated_builder ¶
type CelMapOnARepeated_builder struct {
	Values []*CelMapOnARepeated_Value
	// contains filtered or unexported fields
}
func (CelMapOnARepeated_builder) Build ¶
func (b0 CelMapOnARepeated_builder) Build() *CelMapOnARepeated
type Coordinates ¶
type Coordinates struct {
	Lat float64 `protobuf:"fixed64,1,opt,name=lat,proto3" json:"lat,omitempty"`
	Lng float64 `protobuf:"fixed64,2,opt,name=lng,proto3" json:"lng,omitempty"`
	// contains filtered or unexported fields
}
func (*Coordinates) GetLat ¶
func (x *Coordinates) GetLat() float64
func (*Coordinates) GetLng ¶
func (x *Coordinates) GetLng() float64
func (*Coordinates) ProtoMessage ¶
func (*Coordinates) ProtoMessage()
func (*Coordinates) ProtoReflect ¶
func (x *Coordinates) ProtoReflect() protoreflect.Message
func (*Coordinates) Reset ¶
func (x *Coordinates) Reset()
func (*Coordinates) SetLat ¶
func (x *Coordinates) SetLat(v float64)
func (*Coordinates) SetLng ¶
func (x *Coordinates) SetLng(v float64)
func (*Coordinates) String ¶
func (x *Coordinates) String() string
type Coordinates_builder ¶
type Coordinates_builder struct {
	Lat float64
	Lng float64
	// contains filtered or unexported fields
}
func (Coordinates_builder) Build ¶
func (b0 Coordinates_builder) Build() *Coordinates
type F1 ¶
type F1 struct {
	NeedThis string          `protobuf:"bytes,1,opt,name=need_this,json=needThis,proto3" json:"need_this,omitempty"`
	Field    *FieldWithIssue `protobuf:"bytes,2,opt,name=field,proto3" json:"field,omitempty"`
	// contains filtered or unexported fields
}
func (*F1) ClearField ¶
func (x *F1) ClearField()
func (*F1) GetField ¶
func (x *F1) GetField() *FieldWithIssue
func (*F1) GetNeedThis ¶
func (x *F1) GetNeedThis() string
func (*F1) HasField ¶
func (x *F1) HasField() bool
func (*F1) ProtoMessage ¶
func (*F1) ProtoMessage()
func (*F1) ProtoReflect ¶
func (x *F1) ProtoReflect() protoreflect.Message
func (*F1) Reset ¶
func (x *F1) Reset()
func (*F1) SetField ¶
func (x *F1) SetField(v *FieldWithIssue)
func (*F1) SetNeedThis ¶
func (x *F1) SetNeedThis(v string)
func (*F1) String ¶
func (x *F1) String() string
type F1_builder ¶
type F1_builder struct {
	NeedThis string
	Field    *FieldWithIssue
	// contains filtered or unexported fields
}
func (F1_builder) Build ¶
func (b0 F1_builder) Build() *F1
type F2 ¶
type F2 struct {
	Field *FieldWithIssue `protobuf:"bytes,1,opt,name=field,proto3" json:"field,omitempty"`
	// contains filtered or unexported fields
}
func (*F2) ClearField ¶
func (x *F2) ClearField()
func (*F2) GetField ¶
func (x *F2) GetField() *FieldWithIssue
func (*F2) HasField ¶
func (x *F2) HasField() bool
func (*F2) ProtoMessage ¶
func (*F2) ProtoMessage()
func (*F2) ProtoReflect ¶
func (x *F2) ProtoReflect() protoreflect.Message
func (*F2) Reset ¶
func (x *F2) Reset()
func (*F2) SetField ¶
func (x *F2) SetField(v *FieldWithIssue)
func (*F2) String ¶
func (x *F2) String() string
type F2_builder ¶
type F2_builder struct {
	Field *FieldWithIssue
	// contains filtered or unexported fields
}
func (F2_builder) Build ¶
func (b0 F2_builder) Build() *F2
type FieldOfTypeAny ¶
type FieldOfTypeAny struct {
	Any *anypb.Any `protobuf:"bytes,1,opt,name=any,proto3" json:"any,omitempty"`
	// contains filtered or unexported fields
}
func (*FieldOfTypeAny) ClearAny ¶
func (x *FieldOfTypeAny) ClearAny()
func (*FieldOfTypeAny) GetAny ¶
func (x *FieldOfTypeAny) GetAny() *anypb.Any
func (*FieldOfTypeAny) HasAny ¶
func (x *FieldOfTypeAny) HasAny() bool
func (*FieldOfTypeAny) ProtoMessage ¶
func (*FieldOfTypeAny) ProtoMessage()
func (*FieldOfTypeAny) ProtoReflect ¶
func (x *FieldOfTypeAny) ProtoReflect() protoreflect.Message
func (*FieldOfTypeAny) Reset ¶
func (x *FieldOfTypeAny) Reset()
func (*FieldOfTypeAny) SetAny ¶
func (x *FieldOfTypeAny) SetAny(v *anypb.Any)
func (*FieldOfTypeAny) String ¶
func (x *FieldOfTypeAny) String() string
type FieldOfTypeAny_builder ¶
type FieldOfTypeAny_builder struct {
	Any *anypb.Any
	// contains filtered or unexported fields
}
func (FieldOfTypeAny_builder) Build ¶
func (b0 FieldOfTypeAny_builder) Build() *FieldOfTypeAny
type FieldWithIssue ¶
type FieldWithIssue struct {
	F1   *F1    `protobuf:"bytes,1,opt,name=f1,proto3" json:"f1,omitempty"`
	Name string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	// contains filtered or unexported fields
}
func (*FieldWithIssue) ClearF1 ¶
func (x *FieldWithIssue) ClearF1()
func (*FieldWithIssue) GetF1 ¶
func (x *FieldWithIssue) GetF1() *F1
func (*FieldWithIssue) GetName ¶
func (x *FieldWithIssue) GetName() string
func (*FieldWithIssue) HasF1 ¶
func (x *FieldWithIssue) HasF1() bool
func (*FieldWithIssue) ProtoMessage ¶
func (*FieldWithIssue) ProtoMessage()
func (*FieldWithIssue) ProtoReflect ¶
func (x *FieldWithIssue) ProtoReflect() protoreflect.Message
func (*FieldWithIssue) Reset ¶
func (x *FieldWithIssue) Reset()
func (*FieldWithIssue) SetF1 ¶
func (x *FieldWithIssue) SetF1(v *F1)
func (*FieldWithIssue) SetName ¶
func (x *FieldWithIssue) SetName(v string)
func (*FieldWithIssue) String ¶
func (x *FieldWithIssue) String() string
type FieldWithIssue_builder ¶
type FieldWithIssue_builder struct {
	F1   *F1
	Name string
	// contains filtered or unexported fields
}
func (FieldWithIssue_builder) Build ¶
func (b0 FieldWithIssue_builder) Build() *FieldWithIssue
type HasMsgExprs ¶
type HasMsgExprs struct {
	X int32 `protobuf:"varint,1,opt,name=x,proto3" json:"x,omitempty"`
	Y int32 `protobuf:"varint,2,opt,name=y,proto3" json:"y,omitempty"`
	// contains filtered or unexported fields
}
func (*HasMsgExprs) GetX ¶
func (x *HasMsgExprs) GetX() int32
func (*HasMsgExprs) GetY ¶
func (x *HasMsgExprs) GetY() int32
func (*HasMsgExprs) ProtoMessage ¶
func (*HasMsgExprs) ProtoMessage()
func (*HasMsgExprs) ProtoReflect ¶
func (x *HasMsgExprs) ProtoReflect() protoreflect.Message
func (*HasMsgExprs) Reset ¶
func (x *HasMsgExprs) Reset()
func (*HasMsgExprs) SetX ¶
func (x *HasMsgExprs) SetX(v int32)
func (*HasMsgExprs) SetY ¶
func (x *HasMsgExprs) SetY(v int32)
func (*HasMsgExprs) String ¶
func (x *HasMsgExprs) String() string
type HasMsgExprs_builder ¶
type HasMsgExprs_builder struct {
	X int32
	Y int32
	// contains filtered or unexported fields
}
func (HasMsgExprs_builder) Build ¶
func (b0 HasMsgExprs_builder) Build() *HasMsgExprs
type InvalidRules ¶
type InvalidRules struct {
	Field int32 `protobuf:"varint,1,opt,name=field,proto3" json:"field,omitempty"`
	// contains filtered or unexported fields
}
func (*InvalidRules) GetField ¶
func (x *InvalidRules) GetField() int32
func (*InvalidRules) ProtoMessage ¶
func (*InvalidRules) ProtoMessage()
func (*InvalidRules) ProtoReflect ¶
func (x *InvalidRules) ProtoReflect() protoreflect.Message
func (*InvalidRules) Reset ¶
func (x *InvalidRules) Reset()
func (*InvalidRules) SetField ¶
func (x *InvalidRules) SetField(v int32)
func (*InvalidRules) String ¶
func (x *InvalidRules) String() string
type InvalidRules_builder ¶
type InvalidRules_builder struct {
	Field int32
	// contains filtered or unexported fields
}
func (InvalidRules_builder) Build ¶
func (b0 InvalidRules_builder) Build() *InvalidRules
type Issue148 ¶
type Issue148 struct {
	Test *int32 `protobuf:"varint,1,opt,name=test" json:"test,omitempty"`
	// contains filtered or unexported fields
}

https://github.com/bufbuild/protovalidate-go/issues/148

func (*Issue148) ClearTest ¶
func (x *Issue148) ClearTest()
func (*Issue148) GetTest ¶
func (x *Issue148) GetTest() int32
func (*Issue148) HasTest ¶
func (x *Issue148) HasTest() bool
func (*Issue148) ProtoMessage ¶
func (*Issue148) ProtoMessage()
func (*Issue148) ProtoReflect ¶
func (x *Issue148) ProtoReflect() protoreflect.Message
func (*Issue148) Reset ¶
func (x *Issue148) Reset()
func (*Issue148) SetTest ¶
func (x *Issue148) SetTest(v int32)
func (*Issue148) String ¶
func (x *Issue148) String() string
type Issue148_builder ¶
type Issue148_builder struct {
	Test *int32
	// contains filtered or unexported fields
}
func (Issue148_builder) Build ¶
func (b0 Issue148_builder) Build() *Issue148
type Issue187 ¶
type Issue187 struct {
	FalseField *bool `protobuf:"varint,1,opt,name=false_field,json=falseField" json:"false_field,omitempty"`
	TrueField  *bool `protobuf:"varint,2,opt,name=true_field,json=trueField" json:"true_field,omitempty"`
	// contains filtered or unexported fields
}

https://github.com/bufbuild/protovalidate-go/issues/187

func (*Issue187) ClearFalseField ¶
func (x *Issue187) ClearFalseField()
func (*Issue187) ClearTrueField ¶
func (x *Issue187) ClearTrueField()
func (*Issue187) GetFalseField ¶
func (x *Issue187) GetFalseField() bool
func (*Issue187) GetTrueField ¶
func (x *Issue187) GetTrueField() bool
func (*Issue187) HasFalseField ¶
func (x *Issue187) HasFalseField() bool
func (*Issue187) HasTrueField ¶
func (x *Issue187) HasTrueField() bool
func (*Issue187) ProtoMessage ¶
func (*Issue187) ProtoMessage()
func (*Issue187) ProtoReflect ¶
func (x *Issue187) ProtoReflect() protoreflect.Message
func (*Issue187) Reset ¶
func (x *Issue187) Reset()
func (*Issue187) SetFalseField ¶
func (x *Issue187) SetFalseField(v bool)
func (*Issue187) SetTrueField ¶
func (x *Issue187) SetTrueField(v bool)
func (*Issue187) String ¶
func (x *Issue187) String() string
type Issue187_builder ¶
type Issue187_builder struct {
	FalseField *bool
	TrueField  *bool
	// contains filtered or unexported fields
}
func (Issue187_builder) Build ¶
func (b0 Issue187_builder) Build() *Issue187
type Issue211 ¶
type Issue211 struct {
	Value *timestamppb.Timestamp `protobuf:"bytes,1,opt,name=value,proto3" json:"value,omitempty"`
	// contains filtered or unexported fields
}
func (*Issue211) ClearValue ¶
func (x *Issue211) ClearValue()
func (*Issue211) GetValue ¶
func (x *Issue211) GetValue() *timestamppb.Timestamp
func (*Issue211) HasValue ¶
func (x *Issue211) HasValue() bool
func (*Issue211) ProtoMessage ¶
func (*Issue211) ProtoMessage()
func (*Issue211) ProtoReflect ¶
func (x *Issue211) ProtoReflect() protoreflect.Message
func (*Issue211) Reset ¶
func (x *Issue211) Reset()
func (*Issue211) SetValue ¶
func (x *Issue211) SetValue(v *timestamppb.Timestamp)
func (*Issue211) String ¶
func (x *Issue211) String() string
type Issue211_builder ¶
type Issue211_builder struct {
	Value *timestamppb.Timestamp
	// contains filtered or unexported fields
}
func (Issue211_builder) Build ¶
func (b0 Issue211_builder) Build() *Issue211
type Issue296 ¶
added in v1.1.1
type Issue296 struct {
	Fm *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=fm" json:"fm,omitempty"`
	// contains filtered or unexported fields
}

https://github.com/bufbuild/protovalidate-go/issues/296

func (*Issue296) ClearFm ¶
added in v1.1.1
func (x *Issue296) ClearFm()
func (*Issue296) GetFm ¶
added in v1.1.1
func (x *Issue296) GetFm() *fieldmaskpb.FieldMask
func (*Issue296) HasFm ¶
added in v1.1.1
func (x *Issue296) HasFm() bool
func (*Issue296) ProtoMessage ¶
added in v1.1.1
func (*Issue296) ProtoMessage()
func (*Issue296) ProtoReflect ¶
added in v1.1.1
func (x *Issue296) ProtoReflect() protoreflect.Message
func (*Issue296) Reset ¶
added in v1.1.1
func (x *Issue296) Reset()
func (*Issue296) SetFm ¶
added in v1.1.1
func (x *Issue296) SetFm(v *fieldmaskpb.FieldMask)
func (*Issue296) String ¶
added in v1.1.1
func (x *Issue296) String() string
type Issue296_builder ¶
added in v1.1.1
type Issue296_builder struct {
	Fm *fieldmaskpb.FieldMask
	// contains filtered or unexported fields
}
func (Issue296_builder) Build ¶
added in v1.1.1
func (b0 Issue296_builder) Build() *Issue296
type LoopRecursiveA ¶
type LoopRecursiveA struct {
	B *LoopRecursiveB `protobuf:"bytes,1,opt,name=b,proto3" json:"b,omitempty"`
	// contains filtered or unexported fields
}
func (*LoopRecursiveA) ClearB ¶
func (x *LoopRecursiveA) ClearB()
func (*LoopRecursiveA) GetB ¶
func (x *LoopRecursiveA) GetB() *LoopRecursiveB
func (*LoopRecursiveA) HasB ¶
func (x *LoopRecursiveA) HasB() bool
func (*LoopRecursiveA) ProtoMessage ¶
func (*LoopRecursiveA) ProtoMessage()
func (*LoopRecursiveA) ProtoReflect ¶
func (x *LoopRecursiveA) ProtoReflect() protoreflect.Message
func (*LoopRecursiveA) Reset ¶
func (x *LoopRecursiveA) Reset()
func (*LoopRecursiveA) SetB ¶
func (x *LoopRecursiveA) SetB(v *LoopRecursiveB)
func (*LoopRecursiveA) String ¶
func (x *LoopRecursiveA) String() string
type LoopRecursiveA_builder ¶
type LoopRecursiveA_builder struct {
	B *LoopRecursiveB
	// contains filtered or unexported fields
}
func (LoopRecursiveA_builder) Build ¶
func (b0 LoopRecursiveA_builder) Build() *LoopRecursiveA
type LoopRecursiveB ¶
type LoopRecursiveB struct {
	A *LoopRecursiveA `protobuf:"bytes,1,opt,name=a,proto3" json:"a,omitempty"`
	// contains filtered or unexported fields
}
func (*LoopRecursiveB) ClearA ¶
func (x *LoopRecursiveB) ClearA()
func (*LoopRecursiveB) GetA ¶
func (x *LoopRecursiveB) GetA() *LoopRecursiveA
func (*LoopRecursiveB) HasA ¶
func (x *LoopRecursiveB) HasA() bool
func (*LoopRecursiveB) ProtoMessage ¶
func (*LoopRecursiveB) ProtoMessage()
func (*LoopRecursiveB) ProtoReflect ¶
func (x *LoopRecursiveB) ProtoReflect() protoreflect.Message
func (*LoopRecursiveB) Reset ¶
func (x *LoopRecursiveB) Reset()
func (*LoopRecursiveB) SetA ¶
func (x *LoopRecursiveB) SetA(v *LoopRecursiveA)
func (*LoopRecursiveB) String ¶
func (x *LoopRecursiveB) String() string
type LoopRecursiveB_builder ¶
type LoopRecursiveB_builder struct {
	A *LoopRecursiveA
	// contains filtered or unexported fields
}
func (LoopRecursiveB_builder) Build ¶
func (b0 LoopRecursiveB_builder) Build() *LoopRecursiveB
type MismatchRules ¶
type MismatchRules struct {
	NoRule              bool   `protobuf:"varint,1,opt,name=no_rule,json=noRule,proto3" json:"no_rule,omitempty"`
	StringFieldBoolRule string `protobuf:"bytes,2,opt,name=string_field_bool_rule,json=stringFieldBoolRule,proto3" json:"string_field_bool_rule,omitempty"`
	// contains filtered or unexported fields
}
func (*MismatchRules) GetNoRule ¶
func (x *MismatchRules) GetNoRule() bool
func (*MismatchRules) GetStringFieldBoolRule ¶
func (x *MismatchRules) GetStringFieldBoolRule() string
func (*MismatchRules) ProtoMessage ¶
func (*MismatchRules) ProtoMessage()
func (*MismatchRules) ProtoReflect ¶
func (x *MismatchRules) ProtoReflect() protoreflect.Message
func (*MismatchRules) Reset ¶
func (x *MismatchRules) Reset()
func (*MismatchRules) SetNoRule ¶
func (x *MismatchRules) SetNoRule(v bool)
func (*MismatchRules) SetStringFieldBoolRule ¶
func (x *MismatchRules) SetStringFieldBoolRule(v string)
func (*MismatchRules) String ¶
func (x *MismatchRules) String() string
type MismatchRules_builder ¶
type MismatchRules_builder struct {
	NoRule              bool
	StringFieldBoolRule string
	// contains filtered or unexported fields
}
func (MismatchRules_builder) Build ¶
func (b0 MismatchRules_builder) Build() *MismatchRules
type MixedValidInvalidRules ¶
type MixedValidInvalidRules struct {
	StringFieldBoolRule string `protobuf:"bytes,1,opt,name=string_field_bool_rule,json=stringFieldBoolRule,proto3" json:"string_field_bool_rule,omitempty"`
	ValidStringRule     string `protobuf:"bytes,2,opt,name=valid_string_rule,json=validStringRule,proto3" json:"valid_string_rule,omitempty"`
	// contains filtered or unexported fields
}
func (*MixedValidInvalidRules) GetStringFieldBoolRule ¶
func (x *MixedValidInvalidRules) GetStringFieldBoolRule() string
func (*MixedValidInvalidRules) GetValidStringRule ¶
func (x *MixedValidInvalidRules) GetValidStringRule() string
func (*MixedValidInvalidRules) ProtoMessage ¶
func (*MixedValidInvalidRules) ProtoMessage()
func (*MixedValidInvalidRules) ProtoReflect ¶
func (x *MixedValidInvalidRules) ProtoReflect() protoreflect.Message
func (*MixedValidInvalidRules) Reset ¶
func (x *MixedValidInvalidRules) Reset()
func (*MixedValidInvalidRules) SetStringFieldBoolRule ¶
func (x *MixedValidInvalidRules) SetStringFieldBoolRule(v string)
func (*MixedValidInvalidRules) SetValidStringRule ¶
func (x *MixedValidInvalidRules) SetValidStringRule(v string)
func (*MixedValidInvalidRules) String ¶
func (x *MixedValidInvalidRules) String() string
type MixedValidInvalidRules_builder ¶
type MixedValidInvalidRules_builder struct {
	StringFieldBoolRule string
	ValidStringRule     string
	// contains filtered or unexported fields
}
func (MixedValidInvalidRules_builder) Build ¶
func (b0 MixedValidInvalidRules_builder) Build() *MixedValidInvalidRules
type MsgHasMap ¶
type MsgHasMap struct {
	Int32Map   map[int32]int32           `` /* 145-byte string literal not displayed */
	StringMap  map[string]string         `` /* 162-byte string literal not displayed */
	MessageMap map[int64]*LoopRecursiveA `` /* 166-byte string literal not displayed */
	// contains filtered or unexported fields
}
func (*MsgHasMap) GetInt32Map ¶
func (x *MsgHasMap) GetInt32Map() map[int32]int32
func (*MsgHasMap) GetMessageMap ¶
func (x *MsgHasMap) GetMessageMap() map[int64]*LoopRecursiveA
func (*MsgHasMap) GetStringMap ¶
func (x *MsgHasMap) GetStringMap() map[string]string
func (*MsgHasMap) ProtoMessage ¶
func (*MsgHasMap) ProtoMessage()
func (*MsgHasMap) ProtoReflect ¶
func (x *MsgHasMap) ProtoReflect() protoreflect.Message
func (*MsgHasMap) Reset ¶
func (x *MsgHasMap) Reset()
func (*MsgHasMap) SetInt32Map ¶
func (x *MsgHasMap) SetInt32Map(v map[int32]int32)
func (*MsgHasMap) SetMessageMap ¶
func (x *MsgHasMap) SetMessageMap(v map[int64]*LoopRecursiveA)
func (*MsgHasMap) SetStringMap ¶
func (x *MsgHasMap) SetStringMap(v map[string]string)
func (*MsgHasMap) String ¶
func (x *MsgHasMap) String() string
type MsgHasMap_builder ¶
type MsgHasMap_builder struct {
	Int32Map   map[int32]int32
	StringMap  map[string]string
	MessageMap map[int64]*LoopRecursiveA
	// contains filtered or unexported fields
}
func (MsgHasMap_builder) Build ¶
func (b0 MsgHasMap_builder) Build() *MsgHasMap
type MsgHasOneof ¶
type MsgHasOneof struct {

	// Types that are valid to be assigned to O:
	//
	//	*MsgHasOneof_X
	//	*MsgHasOneof_Y
	//	*MsgHasOneof_Msg
	O isMsgHasOneof_O `protobuf_oneof:"o"`
	// contains filtered or unexported fields
}
func (*MsgHasOneof) ClearMsg ¶
func (x *MsgHasOneof) ClearMsg()
func (*MsgHasOneof) ClearO ¶
func (x *MsgHasOneof) ClearO()
func (*MsgHasOneof) ClearX ¶
func (x *MsgHasOneof) ClearX()
func (*MsgHasOneof) ClearY ¶
func (x *MsgHasOneof) ClearY()
func (*MsgHasOneof) GetMsg ¶
func (x *MsgHasOneof) GetMsg() *HasMsgExprs
func (*MsgHasOneof) GetO ¶
func (x *MsgHasOneof) GetO() isMsgHasOneof_O
func (*MsgHasOneof) GetX ¶
func (x *MsgHasOneof) GetX() string
func (*MsgHasOneof) GetY ¶
func (x *MsgHasOneof) GetY() int32
func (*MsgHasOneof) HasMsg ¶
func (x *MsgHasOneof) HasMsg() bool
func (*MsgHasOneof) HasO ¶
func (x *MsgHasOneof) HasO() bool
func (*MsgHasOneof) HasX ¶
func (x *MsgHasOneof) HasX() bool
func (*MsgHasOneof) HasY ¶
func (x *MsgHasOneof) HasY() bool
func (*MsgHasOneof) ProtoMessage ¶
func (*MsgHasOneof) ProtoMessage()
func (*MsgHasOneof) ProtoReflect ¶
func (x *MsgHasOneof) ProtoReflect() protoreflect.Message
func (*MsgHasOneof) Reset ¶
func (x *MsgHasOneof) Reset()
func (*MsgHasOneof) SetMsg ¶
func (x *MsgHasOneof) SetMsg(v *HasMsgExprs)
func (*MsgHasOneof) SetX ¶
func (x *MsgHasOneof) SetX(v string)
func (*MsgHasOneof) SetY ¶
func (x *MsgHasOneof) SetY(v int32)
func (*MsgHasOneof) String ¶
func (x *MsgHasOneof) String() string
func (*MsgHasOneof) WhichO ¶
func (x *MsgHasOneof) WhichO() case_MsgHasOneof_O
type MsgHasOneof_Msg ¶
type MsgHasOneof_Msg struct {
	Msg *HasMsgExprs `protobuf:"bytes,3,opt,name=msg,proto3,oneof"`
}
type MsgHasOneof_X ¶
type MsgHasOneof_X struct {
	X string `protobuf:"bytes,1,opt,name=x,proto3,oneof"`
}
type MsgHasOneof_Y ¶
type MsgHasOneof_Y struct {
	Y int32 `protobuf:"varint,2,opt,name=y,proto3,oneof"`
}
type MsgHasOneof_builder ¶
type MsgHasOneof_builder struct {

	// Fields of oneof O:
	X   *string
	Y   *int32
	Msg *HasMsgExprs
	// contains filtered or unexported fields
}
func (MsgHasOneof_builder) Build ¶
func (b0 MsgHasOneof_builder) Build() *MsgHasOneof
type MsgHasRepeated ¶
type MsgHasRepeated struct {
	X []float32      `protobuf:"fixed32,1,rep,packed,name=x,proto3" json:"x,omitempty"`
	Y []string       `protobuf:"bytes,2,rep,name=y,proto3" json:"y,omitempty"`
	Z []*HasMsgExprs `protobuf:"bytes,3,rep,name=z,proto3" json:"z,omitempty"`
	// contains filtered or unexported fields
}
func (*MsgHasRepeated) GetX ¶
func (x *MsgHasRepeated) GetX() []float32
func (*MsgHasRepeated) GetY ¶
func (x *MsgHasRepeated) GetY() []string
func (*MsgHasRepeated) GetZ ¶
func (x *MsgHasRepeated) GetZ() []*HasMsgExprs
func (*MsgHasRepeated) ProtoMessage ¶
func (*MsgHasRepeated) ProtoMessage()
func (*MsgHasRepeated) ProtoReflect ¶
func (x *MsgHasRepeated) ProtoReflect() protoreflect.Message
func (*MsgHasRepeated) Reset ¶
func (x *MsgHasRepeated) Reset()
func (*MsgHasRepeated) SetX ¶
func (x *MsgHasRepeated) SetX(v []float32)
func (*MsgHasRepeated) SetY ¶
func (x *MsgHasRepeated) SetY(v []string)
func (*MsgHasRepeated) SetZ ¶
func (x *MsgHasRepeated) SetZ(v []*HasMsgExprs)
func (*MsgHasRepeated) String ¶
func (x *MsgHasRepeated) String() string
type MsgHasRepeated_builder ¶
type MsgHasRepeated_builder struct {
	X []float32
	Y []string
	Z []*HasMsgExprs
	// contains filtered or unexported fields
}
func (MsgHasRepeated_builder) Build ¶
func (b0 MsgHasRepeated_builder) Build() *MsgHasRepeated
type MultipleStepsTransitiveFieldRules ¶
type MultipleStepsTransitiveFieldRules struct {
	Api *apipb.Api `protobuf:"bytes,1,opt,name=api,proto3" json:"api,omitempty"`
	// contains filtered or unexported fields
}
func (*MultipleStepsTransitiveFieldRules) ClearApi ¶
func (x *MultipleStepsTransitiveFieldRules) ClearApi()
func (*MultipleStepsTransitiveFieldRules) GetApi ¶
func (x *MultipleStepsTransitiveFieldRules) GetApi() *apipb.Api
func (*MultipleStepsTransitiveFieldRules) HasApi ¶
func (x *MultipleStepsTransitiveFieldRules) HasApi() bool
func (*MultipleStepsTransitiveFieldRules) ProtoMessage ¶
func (*MultipleStepsTransitiveFieldRules) ProtoMessage()
func (*MultipleStepsTransitiveFieldRules) ProtoReflect ¶
func (x *MultipleStepsTransitiveFieldRules) ProtoReflect() protoreflect.Message
func (*MultipleStepsTransitiveFieldRules) Reset ¶
func (x *MultipleStepsTransitiveFieldRules) Reset()
func (*MultipleStepsTransitiveFieldRules) SetApi ¶
func (x *MultipleStepsTransitiveFieldRules) SetApi(v *apipb.Api)
func (*MultipleStepsTransitiveFieldRules) String ¶
func (x *MultipleStepsTransitiveFieldRules) String() string
type MultipleStepsTransitiveFieldRules_builder ¶
type MultipleStepsTransitiveFieldRules_builder struct {
	Api *apipb.Api
	// contains filtered or unexported fields
}
func (MultipleStepsTransitiveFieldRules_builder) Build ¶
func (b0 MultipleStepsTransitiveFieldRules_builder) Build() *MultipleStepsTransitiveFieldRules
type NestedRules ¶
type NestedRules struct {
	Field         *AllRuleTypes            `protobuf:"bytes,1,opt,name=field,proto3" json:"field,omitempty"`
	Field2        string                   `protobuf:"bytes,2,opt,name=field2,proto3" json:"field2,omitempty"`
	RepeatedField []*AllRuleTypes          `protobuf:"bytes,3,rep,name=repeated_field,json=repeatedField,proto3" json:"repeated_field,omitempty"`
	MapField      map[string]*AllRuleTypes `` /* 159-byte string literal not displayed */
	// Types that are valid to be assigned to RequiredOneof:
	//
	//	*NestedRules_OneofField
	RequiredOneof isNestedRules_RequiredOneof `protobuf_oneof:"required_oneof"`
	// contains filtered or unexported fields
}
func (*NestedRules) ClearField ¶
func (x *NestedRules) ClearField()
func (*NestedRules) ClearOneofField ¶
func (x *NestedRules) ClearOneofField()
func (*NestedRules) ClearRequiredOneof ¶
func (x *NestedRules) ClearRequiredOneof()
func (*NestedRules) GetField ¶
func (x *NestedRules) GetField() *AllRuleTypes
func (*NestedRules) GetField2 ¶
func (x *NestedRules) GetField2() string
func (*NestedRules) GetMapField ¶
func (x *NestedRules) GetMapField() map[string]*AllRuleTypes
func (*NestedRules) GetOneofField ¶
func (x *NestedRules) GetOneofField() string
func (*NestedRules) GetRepeatedField ¶
func (x *NestedRules) GetRepeatedField() []*AllRuleTypes
func (*NestedRules) GetRequiredOneof ¶
func (x *NestedRules) GetRequiredOneof() isNestedRules_RequiredOneof
func (*NestedRules) HasField ¶
func (x *NestedRules) HasField() bool
func (*NestedRules) HasOneofField ¶
func (x *NestedRules) HasOneofField() bool
func (*NestedRules) HasRequiredOneof ¶
func (x *NestedRules) HasRequiredOneof() bool
func (*NestedRules) ProtoMessage ¶
func (*NestedRules) ProtoMessage()
func (*NestedRules) ProtoReflect ¶
func (x *NestedRules) ProtoReflect() protoreflect.Message
func (*NestedRules) Reset ¶
func (x *NestedRules) Reset()
func (*NestedRules) SetField ¶
func (x *NestedRules) SetField(v *AllRuleTypes)
func (*NestedRules) SetField2 ¶
func (x *NestedRules) SetField2(v string)
func (*NestedRules) SetMapField ¶
func (x *NestedRules) SetMapField(v map[string]*AllRuleTypes)
func (*NestedRules) SetOneofField ¶
func (x *NestedRules) SetOneofField(v string)
func (*NestedRules) SetRepeatedField ¶
func (x *NestedRules) SetRepeatedField(v []*AllRuleTypes)
func (*NestedRules) String ¶
func (x *NestedRules) String() string
func (*NestedRules) WhichRequiredOneof ¶
func (x *NestedRules) WhichRequiredOneof() case_NestedRules_RequiredOneof
type NestedRules_OneofField ¶
type NestedRules_OneofField struct {
	OneofField string `protobuf:"bytes,5,opt,name=oneof_field,json=oneofField,proto3,oneof"`
}
type NestedRules_builder ¶
type NestedRules_builder struct {
	Field         *AllRuleTypes
	Field2        string
	RepeatedField []*AllRuleTypes
	MapField      map[string]*AllRuleTypes
	// Fields of oneof RequiredOneof:
	OneofField *string
	// contains filtered or unexported fields
}
func (NestedRules_builder) Build ¶
func (b0 NestedRules_builder) Build() *NestedRules
type OneTwo ¶
type OneTwo struct {
	Field1 *F1 `protobuf:"bytes,1,opt,name=field1,proto3" json:"field1,omitempty"`
	Field2 *F2 `protobuf:"bytes,2,opt,name=field2,proto3" json:"field2,omitempty"`
	// contains filtered or unexported fields
}
func (*OneTwo) ClearField1 ¶
func (x *OneTwo) ClearField1()
func (*OneTwo) ClearField2 ¶
func (x *OneTwo) ClearField2()
func (*OneTwo) GetField1 ¶
func (x *OneTwo) GetField1() *F1
func (*OneTwo) GetField2 ¶
func (x *OneTwo) GetField2() *F2
func (*OneTwo) HasField1 ¶
func (x *OneTwo) HasField1() bool
func (*OneTwo) HasField2 ¶
func (x *OneTwo) HasField2() bool
func (*OneTwo) ProtoMessage ¶
func (*OneTwo) ProtoMessage()
func (*OneTwo) ProtoReflect ¶
func (x *OneTwo) ProtoReflect() protoreflect.Message
func (*OneTwo) Reset ¶
func (x *OneTwo) Reset()
func (*OneTwo) SetField1 ¶
func (x *OneTwo) SetField1(v *F1)
func (*OneTwo) SetField2 ¶
func (x *OneTwo) SetField2(v *F2)
func (*OneTwo) String ¶
func (x *OneTwo) String() string
type OneTwo_builder ¶
type OneTwo_builder struct {
	Field1 *F1
	Field2 *F2
	// contains filtered or unexported fields
}
func (OneTwo_builder) Build ¶
func (b0 OneTwo_builder) Build() *OneTwo
type Person ¶
type Person struct {
	Id    uint64       `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Email string       `protobuf:"bytes,2,opt,name=email,proto3" json:"email,omitempty"`
	Name  string       `protobuf:"bytes,3,opt,name=name,proto3" json:"name,omitempty"`
	Home  *Coordinates `protobuf:"bytes,4,opt,name=home,proto3" json:"home,omitempty"`
	// contains filtered or unexported fields
}
func (*Person) ClearHome ¶
func (x *Person) ClearHome()
func (*Person) GetEmail ¶
func (x *Person) GetEmail() string
func (*Person) GetHome ¶
func (x *Person) GetHome() *Coordinates
func (*Person) GetId ¶
func (x *Person) GetId() uint64
func (*Person) GetName ¶
func (x *Person) GetName() string
func (*Person) HasHome ¶
func (x *Person) HasHome() bool
func (*Person) ProtoMessage ¶
func (*Person) ProtoMessage()
func (*Person) ProtoReflect ¶
func (x *Person) ProtoReflect() protoreflect.Message
func (*Person) Reset ¶
func (x *Person) Reset()
func (*Person) SetEmail ¶
func (x *Person) SetEmail(v string)
func (*Person) SetHome ¶
func (x *Person) SetHome(v *Coordinates)
func (*Person) SetId ¶
func (x *Person) SetId(v uint64)
func (*Person) SetName ¶
func (x *Person) SetName(v string)
func (*Person) String ¶
func (x *Person) String() string
type Person_builder ¶
type Person_builder struct {
	Id    uint64
	Email string
	Name  string
	Home  *Coordinates
	// contains filtered or unexported fields
}
func (Person_builder) Build ¶
func (b0 Person_builder) Build() *Person
type Proto2Group ¶
added in v1.1.0
type Proto2Group struct {
	Optional *Proto2Group_Optional `protobuf:"group,1,opt,name=Optional,json=optional" json:"optional,omitempty"`
	// contains filtered or unexported fields
}
func (*Proto2Group) ClearOptional ¶
added in v1.1.0
func (x *Proto2Group) ClearOptional()
func (*Proto2Group) GetOptional ¶
added in v1.1.0
func (x *Proto2Group) GetOptional() *Proto2Group_Optional
func (*Proto2Group) HasOptional ¶
added in v1.1.0
func (x *Proto2Group) HasOptional() bool
func (*Proto2Group) ProtoMessage ¶
added in v1.1.0
func (*Proto2Group) ProtoMessage()
func (*Proto2Group) ProtoReflect ¶
added in v1.1.0
func (x *Proto2Group) ProtoReflect() protoreflect.Message
func (*Proto2Group) Reset ¶
added in v1.1.0
func (x *Proto2Group) Reset()
func (*Proto2Group) SetOptional ¶
added in v1.1.0
func (x *Proto2Group) SetOptional(v *Proto2Group_Optional)
func (*Proto2Group) String ¶
added in v1.1.0
func (x *Proto2Group) String() string
type Proto2Group_Optional ¶
added in v1.1.0
type Proto2Group_Optional struct {
	Value *int32 `protobuf:"varint,1,opt,name=value" json:"value,omitempty"`
	// contains filtered or unexported fields
}
func (*Proto2Group_Optional) ClearValue ¶
added in v1.1.0
func (x *Proto2Group_Optional) ClearValue()
func (*Proto2Group_Optional) GetValue ¶
added in v1.1.0
func (x *Proto2Group_Optional) GetValue() int32
func (*Proto2Group_Optional) HasValue ¶
added in v1.1.0
func (x *Proto2Group_Optional) HasValue() bool
func (*Proto2Group_Optional) ProtoMessage ¶
added in v1.1.0
func (*Proto2Group_Optional) ProtoMessage()
func (*Proto2Group_Optional) ProtoReflect ¶
added in v1.1.0
func (x *Proto2Group_Optional) ProtoReflect() protoreflect.Message
func (*Proto2Group_Optional) Reset ¶
added in v1.1.0
func (x *Proto2Group_Optional) Reset()
func (*Proto2Group_Optional) SetValue ¶
added in v1.1.0
func (x *Proto2Group_Optional) SetValue(v int32)
func (*Proto2Group_Optional) String ¶
added in v1.1.0
func (x *Proto2Group_Optional) String() string
type Proto2Group_Optional_builder ¶
added in v1.1.0
type Proto2Group_Optional_builder struct {
	Value *int32
	// contains filtered or unexported fields
}
func (Proto2Group_Optional_builder) Build ¶
added in v1.1.0
func (b0 Proto2Group_Optional_builder) Build() *Proto2Group_Optional
type Proto2Group_builder ¶
added in v1.1.0
type Proto2Group_builder struct {
	Optional *Proto2Group_Optional
	// contains filtered or unexported fields
}
func (Proto2Group_builder) Build ¶
added in v1.1.0
func (b0 Proto2Group_builder) Build() *Proto2Group
type RepeatedItemCel ¶
type RepeatedItemCel struct {
	Paths []string `protobuf:"bytes,1,rep,name=paths,proto3" json:"paths,omitempty"`
	// contains filtered or unexported fields
}
func (*RepeatedItemCel) GetPaths ¶
func (x *RepeatedItemCel) GetPaths() []string
func (*RepeatedItemCel) ProtoMessage ¶
func (*RepeatedItemCel) ProtoMessage()
func (*RepeatedItemCel) ProtoReflect ¶
func (x *RepeatedItemCel) ProtoReflect() protoreflect.Message
func (*RepeatedItemCel) Reset ¶
func (x *RepeatedItemCel) Reset()
func (*RepeatedItemCel) SetPaths ¶
func (x *RepeatedItemCel) SetPaths(v []string)
func (*RepeatedItemCel) String ¶
func (x *RepeatedItemCel) String() string
type RepeatedItemCel_builder ¶
type RepeatedItemCel_builder struct {
	Paths []string
	// contains filtered or unexported fields
}
func (RepeatedItemCel_builder) Build ¶
func (b0 RepeatedItemCel_builder) Build() *RepeatedItemCel
type SelfRecursive ¶
type SelfRecursive struct {
	X      int32          `protobuf:"varint,1,opt,name=x,proto3" json:"x,omitempty"`
	Turtle *SelfRecursive `protobuf:"bytes,2,opt,name=turtle,proto3" json:"turtle,omitempty"`
	// contains filtered or unexported fields
}
func (*SelfRecursive) ClearTurtle ¶
func (x *SelfRecursive) ClearTurtle()
func (*SelfRecursive) GetTurtle ¶
func (x *SelfRecursive) GetTurtle() *SelfRecursive
func (*SelfRecursive) GetX ¶
func (x *SelfRecursive) GetX() int32
func (*SelfRecursive) HasTurtle ¶
func (x *SelfRecursive) HasTurtle() bool
func (*SelfRecursive) ProtoMessage ¶
func (*SelfRecursive) ProtoMessage()
func (*SelfRecursive) ProtoReflect ¶
func (x *SelfRecursive) ProtoReflect() protoreflect.Message
func (*SelfRecursive) Reset ¶
func (x *SelfRecursive) Reset()
func (*SelfRecursive) SetTurtle ¶
func (x *SelfRecursive) SetTurtle(v *SelfRecursive)
func (*SelfRecursive) SetX ¶
func (x *SelfRecursive) SetX(v int32)
func (*SelfRecursive) String ¶
func (x *SelfRecursive) String() string
type SelfRecursive_builder ¶
type SelfRecursive_builder struct {
	X      int32
	Turtle *SelfRecursive
	// contains filtered or unexported fields
}
func (SelfRecursive_builder) Build ¶
func (b0 SelfRecursive_builder) Build() *SelfRecursive
type SelfReferentialMap ¶
added in v1.1.3
type SelfReferentialMap struct {
	Children map[string]*SelfReferentialMap `` /* 143-byte string literal not displayed */
	Name     *string                        `protobuf:"bytes,2,opt,name=name,proto3,oneof" json:"name,omitempty"`
	// contains filtered or unexported fields
}

https://github.com/bufbuild/protovalidate-go/issues/307

func (*SelfReferentialMap) ClearName ¶
added in v1.1.3
func (x *SelfReferentialMap) ClearName()
func (*SelfReferentialMap) GetChildren ¶
added in v1.1.3
func (x *SelfReferentialMap) GetChildren() map[string]*SelfReferentialMap
func (*SelfReferentialMap) GetName ¶
added in v1.1.3
func (x *SelfReferentialMap) GetName() string
func (*SelfReferentialMap) HasName ¶
added in v1.1.3
func (x *SelfReferentialMap) HasName() bool
func (*SelfReferentialMap) ProtoMessage ¶
added in v1.1.3
func (*SelfReferentialMap) ProtoMessage()
func (*SelfReferentialMap) ProtoReflect ¶
added in v1.1.3
func (x *SelfReferentialMap) ProtoReflect() protoreflect.Message
func (*SelfReferentialMap) Reset ¶
added in v1.1.3
func (x *SelfReferentialMap) Reset()
func (*SelfReferentialMap) SetChildren ¶
added in v1.1.3
func (x *SelfReferentialMap) SetChildren(v map[string]*SelfReferentialMap)
func (*SelfReferentialMap) SetName ¶
added in v1.1.3
func (x *SelfReferentialMap) SetName(v string)
func (*SelfReferentialMap) String ¶
added in v1.1.3
func (x *SelfReferentialMap) String() string
type SelfReferentialMap_builder ¶
added in v1.1.3
type SelfReferentialMap_builder struct {
	Children map[string]*SelfReferentialMap
	Name     *string
	// contains filtered or unexported fields
}
func (SelfReferentialMap_builder) Build ¶
added in v1.1.3
func (b0 SelfReferentialMap_builder) Build() *SelfReferentialMap
type SelfReferentialRepeated ¶
added in v1.1.3
type SelfReferentialRepeated struct {
	Children []*SelfReferentialRepeated `protobuf:"bytes,1,rep,name=children,proto3" json:"children,omitempty"`
	Name     *string                    `protobuf:"bytes,2,opt,name=name,proto3,oneof" json:"name,omitempty"`
	// contains filtered or unexported fields
}

https://github.com/bufbuild/protovalidate-go/issues/307

func (*SelfReferentialRepeated) ClearName ¶
added in v1.1.3
func (x *SelfReferentialRepeated) ClearName()
func (*SelfReferentialRepeated) GetChildren ¶
added in v1.1.3
func (x *SelfReferentialRepeated) GetChildren() []*SelfReferentialRepeated
func (*SelfReferentialRepeated) GetName ¶
added in v1.1.3
func (x *SelfReferentialRepeated) GetName() string
func (*SelfReferentialRepeated) HasName ¶
added in v1.1.3
func (x *SelfReferentialRepeated) HasName() bool
func (*SelfReferentialRepeated) ProtoMessage ¶
added in v1.1.3
func (*SelfReferentialRepeated) ProtoMessage()
func (*SelfReferentialRepeated) ProtoReflect ¶
added in v1.1.3
func (x *SelfReferentialRepeated) ProtoReflect() protoreflect.Message
func (*SelfReferentialRepeated) Reset ¶
added in v1.1.3
func (x *SelfReferentialRepeated) Reset()
func (*SelfReferentialRepeated) SetChildren ¶
added in v1.1.3
func (x *SelfReferentialRepeated) SetChildren(v []*SelfReferentialRepeated)
func (*SelfReferentialRepeated) SetName ¶
added in v1.1.3
func (x *SelfReferentialRepeated) SetName(v string)
func (*SelfReferentialRepeated) String ¶
added in v1.1.3
func (x *SelfReferentialRepeated) String() string
type SelfReferentialRepeated_builder ¶
added in v1.1.3
type SelfReferentialRepeated_builder struct {
	Children []*SelfReferentialRepeated
	Name     *string
	// contains filtered or unexported fields
}
func (SelfReferentialRepeated_builder) Build ¶
added in v1.1.3
func (b0 SelfReferentialRepeated_builder) Build() *SelfReferentialRepeated
type Simple ¶
type Simple struct {
	S string `protobuf:"bytes,1,opt,name=s,proto3" json:"s,omitempty"`
	// contains filtered or unexported fields
}
func (*Simple) GetS ¶
func (x *Simple) GetS() string
func (*Simple) ProtoMessage ¶
func (*Simple) ProtoMessage()
func (*Simple) ProtoReflect ¶
func (x *Simple) ProtoReflect() protoreflect.Message
func (*Simple) Reset ¶
func (x *Simple) Reset()
func (*Simple) SetS ¶
func (x *Simple) SetS(v string)
func (*Simple) String ¶
func (x *Simple) String() string
type Simple_builder ¶
type Simple_builder struct {
	S string
	// contains filtered or unexported fields
}
func (Simple_builder) Build ¶
func (b0 Simple_builder) Build() *Simple
type TransitiveFieldRule ¶
type TransitiveFieldRule struct {
	Mask *fieldmaskpb.FieldMask `protobuf:"bytes,1,opt,name=mask,proto3" json:"mask,omitempty"`
	// contains filtered or unexported fields
}
func (*TransitiveFieldRule) ClearMask ¶
func (x *TransitiveFieldRule) ClearMask()
func (*TransitiveFieldRule) GetMask ¶
func (x *TransitiveFieldRule) GetMask() *fieldmaskpb.FieldMask
func (*TransitiveFieldRule) HasMask ¶
func (x *TransitiveFieldRule) HasMask() bool
func (*TransitiveFieldRule) ProtoMessage ¶
func (*TransitiveFieldRule) ProtoMessage()
func (*TransitiveFieldRule) ProtoReflect ¶
func (x *TransitiveFieldRule) ProtoReflect() protoreflect.Message
func (*TransitiveFieldRule) Reset ¶
func (x *TransitiveFieldRule) Reset()
func (*TransitiveFieldRule) SetMask ¶
func (x *TransitiveFieldRule) SetMask(v *fieldmaskpb.FieldMask)
func (*TransitiveFieldRule) String ¶
func (x *TransitiveFieldRule) String() string
type TransitiveFieldRule_builder ¶
type TransitiveFieldRule_builder struct {
	Mask *fieldmaskpb.FieldMask
	// contains filtered or unexported fields
}
func (TransitiveFieldRule_builder) Build ¶
func (b0 TransitiveFieldRule_builder) Build() *TransitiveFieldRule
type TwoOne ¶
type TwoOne struct {
	Field2 *F2 `protobuf:"bytes,1,opt,name=field2,proto3" json:"field2,omitempty"`
	Field1 *F1 `protobuf:"bytes,2,opt,name=field1,proto3" json:"field1,omitempty"`
	// contains filtered or unexported fields
}
func (*TwoOne) ClearField1 ¶
func (x *TwoOne) ClearField1()
func (*TwoOne) ClearField2 ¶
func (x *TwoOne) ClearField2()
func (*TwoOne) GetField1 ¶
func (x *TwoOne) GetField1() *F1
func (*TwoOne) GetField2 ¶
func (x *TwoOne) GetField2() *F2
func (*TwoOne) HasField1 ¶
func (x *TwoOne) HasField1() bool
func (*TwoOne) HasField2 ¶
func (x *TwoOne) HasField2() bool
func (*TwoOne) ProtoMessage ¶
func (*TwoOne) ProtoMessage()
func (*TwoOne) ProtoReflect ¶
func (x *TwoOne) ProtoReflect() protoreflect.Message
func (*TwoOne) Reset ¶
func (x *TwoOne) Reset()
func (*TwoOne) SetField1 ¶
func (x *TwoOne) SetField1(v *F1)
func (*TwoOne) SetField2 ¶
func (x *TwoOne) SetField2(v *F2)
func (*TwoOne) String ¶
func (x *TwoOne) String() string
type TwoOne_builder ¶
type TwoOne_builder struct {
	Field2 *F2
	Field1 *F1
	// contains filtered or unexported fields
}
func (TwoOne_builder) Build ¶
func (b0 TwoOne_builder) Build() *TwoOne
 Source Files ¶
View all Source files
bench.pb.go
compile.pb.go
example.pb.go
filter.pb.go
groups_proto2.pb.go
predefined.pb.go
validations.pb.go
Why Go
Use Cases
Case Studies
Get Started
Playground
Tour
Stack Overflow
Help
Packages
Standard Library
Sub-repositories
About Go Packages
About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct
Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly
Copyright
Terms of Service
Privacy Policy
Report an Issue

Theme Toggle

Shortcuts Modal
