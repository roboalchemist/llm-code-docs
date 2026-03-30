# Source: https://pkg.go.dev/gopkg.in/ini.v1

Title: ini package - gopkg.in/ini.v1 - Go Packages

URL Source: https://pkg.go.dev/gopkg.in/ini.v1

Markdown Content:
Package ini provides INI file read and write functionality in Go.

*   [Variables](https://pkg.go.dev/gopkg.in/ini.v1#pkg-variables)
*   [func IsErrDelimiterNotFound(err error) bool](https://pkg.go.dev/gopkg.in/ini.v1#IsErrDelimiterNotFound)
*   [func IsErrEmptyKeyName(err error) bool](https://pkg.go.dev/gopkg.in/ini.v1#IsErrEmptyKeyName)
*   [func MapTo(v, source interface{}, others ...interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#MapTo)
*   [func MapToWithMapper(v interface{}, mapper NameMapper, source interface{}, others ...interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#MapToWithMapper)
*   [func ReflectFrom(cfg *File, v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#ReflectFrom)
*   [func ReflectFromWithMapper(cfg *File, v interface{}, mapper NameMapper) error](https://pkg.go.dev/gopkg.in/ini.v1#ReflectFromWithMapper)
*   [func StrictMapTo(v, source interface{}, others ...interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#StrictMapTo)
*   [func StrictMapToWithMapper(v interface{}, mapper NameMapper, source interface{}, others ...interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#StrictMapToWithMapper)
*   [type DebugFunc](https://pkg.go.dev/gopkg.in/ini.v1#DebugFunc)
*   [type ErrDelimiterNotFound](https://pkg.go.dev/gopkg.in/ini.v1#ErrDelimiterNotFound)
*       *   [func (err ErrDelimiterNotFound) Error() string](https://pkg.go.dev/gopkg.in/ini.v1#ErrDelimiterNotFound.Error)

*   [type ErrEmptyKeyName](https://pkg.go.dev/gopkg.in/ini.v1#ErrEmptyKeyName)
*       *   [func (err ErrEmptyKeyName) Error() string](https://pkg.go.dev/gopkg.in/ini.v1#ErrEmptyKeyName.Error)

*   [type File](https://pkg.go.dev/gopkg.in/ini.v1#File)
*       *   [func Empty(opts ...LoadOptions) *File](https://pkg.go.dev/gopkg.in/ini.v1#Empty)
    *   [func InsensitiveLoad(source interface{}, others ...interface{}) (*File, error)](https://pkg.go.dev/gopkg.in/ini.v1#InsensitiveLoad)
    *   [func Load(source interface{}, others ...interface{}) (*File, error)](https://pkg.go.dev/gopkg.in/ini.v1#Load)
    *   [func LoadSources(opts LoadOptions, source interface{}, others ...interface{}) (_ *File, err error)](https://pkg.go.dev/gopkg.in/ini.v1#LoadSources)
    *   [func LooseLoad(source interface{}, others ...interface{}) (*File, error)](https://pkg.go.dev/gopkg.in/ini.v1#LooseLoad)
    *   [func ShadowLoad(source interface{}, others ...interface{}) (*File, error)](https://pkg.go.dev/gopkg.in/ini.v1#ShadowLoad)

*       *   [func (f *File) Append(source interface{}, others ...interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#File.Append)
    *   [func (f *File) ChildSections(name string) []*Section](https://pkg.go.dev/gopkg.in/ini.v1#File.ChildSections)
    *   [func (f *File) DeleteSection(name string)](https://pkg.go.dev/gopkg.in/ini.v1#File.DeleteSection)
    *   [func (f *File) DeleteSectionWithIndex(name string, index int) error](https://pkg.go.dev/gopkg.in/ini.v1#File.DeleteSectionWithIndex)
    *   [func (f *File) GetSection(name string) (*Section, error)](https://pkg.go.dev/gopkg.in/ini.v1#File.GetSection)
    *   [func (f *File) HasSection(name string) bool](https://pkg.go.dev/gopkg.in/ini.v1#File.HasSection)
    *   [func (f *File) MapTo(v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#File.MapTo)
    *   [func (f *File) NewRawSection(name, body string) (*Section, error)](https://pkg.go.dev/gopkg.in/ini.v1#File.NewRawSection)
    *   [func (f *File) NewSection(name string) (*Section, error)](https://pkg.go.dev/gopkg.in/ini.v1#File.NewSection)
    *   [func (f *File) NewSections(names ...string) (err error)](https://pkg.go.dev/gopkg.in/ini.v1#File.NewSections)
    *   [func (f *File) ReflectFrom(v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#File.ReflectFrom)
    *   [func (f *File) Reload() (err error)](https://pkg.go.dev/gopkg.in/ini.v1#File.Reload)
    *   [func (f *File) SaveTo(filename string) error](https://pkg.go.dev/gopkg.in/ini.v1#File.SaveTo)
    *   [func (f *File) SaveToIndent(filename, indent string) error](https://pkg.go.dev/gopkg.in/ini.v1#File.SaveToIndent)
    *   [func (f *File) Section(name string) *Section](https://pkg.go.dev/gopkg.in/ini.v1#File.Section)
    *   [func (f *File) SectionStrings() []string](https://pkg.go.dev/gopkg.in/ini.v1#File.SectionStrings)
    *   [func (f *File) SectionWithIndex(name string, index int) *Section](https://pkg.go.dev/gopkg.in/ini.v1#File.SectionWithIndex)
    *   [func (f *File) Sections() []*Section](https://pkg.go.dev/gopkg.in/ini.v1#File.Sections)
    *   [func (f *File) SectionsByName(name string) ([]*Section, error)](https://pkg.go.dev/gopkg.in/ini.v1#File.SectionsByName)
    *   [func (f *File) StrictMapTo(v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#File.StrictMapTo)
    *   [func (f *File) WriteTo(w io.Writer) (int64, error)](https://pkg.go.dev/gopkg.in/ini.v1#File.WriteTo)
    *   [func (f *File) WriteToIndent(w io.Writer, indent string) (int64, error)](https://pkg.go.dev/gopkg.in/ini.v1#File.WriteToIndent)

*   [type Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)
*       *   [func (k *Key) AddNestedValue(val string) error](https://pkg.go.dev/gopkg.in/ini.v1#Key.AddNestedValue)
    *   [func (k *Key) AddShadow(val string) error](https://pkg.go.dev/gopkg.in/ini.v1#Key.AddShadow)
    *   [func (k *Key) Bool() (bool, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Bool)
    *   [func (k *Key) Bools(delim string) []bool](https://pkg.go.dev/gopkg.in/ini.v1#Key.Bools)
    *   [func (k *Key) Duration() (time.Duration, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Duration)
    *   [func (k *Key) Float64() (float64, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Float64)
    *   [func (k *Key) Float64s(delim string) []float64](https://pkg.go.dev/gopkg.in/ini.v1#Key.Float64s)
    *   [func (k *Key) In(defaultVal string, candidates []string) string](https://pkg.go.dev/gopkg.in/ini.v1#Key.In)
    *   [func (k *Key) InFloat64(defaultVal float64, candidates []float64) float64](https://pkg.go.dev/gopkg.in/ini.v1#Key.InFloat64)
    *   [func (k *Key) InInt(defaultVal int, candidates []int) int](https://pkg.go.dev/gopkg.in/ini.v1#Key.InInt)
    *   [func (k *Key) InInt64(defaultVal int64, candidates []int64) int64](https://pkg.go.dev/gopkg.in/ini.v1#Key.InInt64)
    *   [func (k *Key) InTime(defaultVal time.Time, candidates []time.Time) time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.InTime)
    *   [func (k *Key) InTimeFormat(format string, defaultVal time.Time, candidates []time.Time) time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.InTimeFormat)
    *   [func (k *Key) InUint(defaultVal uint, candidates []uint) uint](https://pkg.go.dev/gopkg.in/ini.v1#Key.InUint)
    *   [func (k *Key) InUint64(defaultVal uint64, candidates []uint64) uint64](https://pkg.go.dev/gopkg.in/ini.v1#Key.InUint64)
    *   [func (k *Key) Int() (int, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Int)
    *   [func (k *Key) Int64() (int64, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Int64)
    *   [func (k *Key) Int64s(delim string) []int64](https://pkg.go.dev/gopkg.in/ini.v1#Key.Int64s)
    *   [func (k *Key) Ints(delim string) []int](https://pkg.go.dev/gopkg.in/ini.v1#Key.Ints)
    *   [func (k *Key) MustBool(defaultVal ...bool) bool](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustBool)
    *   [func (k *Key) MustDuration(defaultVal ...time.Duration) time.Duration](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustDuration)
    *   [func (k *Key) MustFloat64(defaultVal ...float64) float64](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustFloat64)
    *   [func (k *Key) MustInt(defaultVal ...int) int](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustInt)
    *   [func (k *Key) MustInt64(defaultVal ...int64) int64](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustInt64)
    *   [func (k *Key) MustString(defaultVal string) string](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustString)
    *   [func (k *Key) MustTime(defaultVal ...time.Time) time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustTime)
    *   [func (k *Key) MustTimeFormat(format string, defaultVal ...time.Time) time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustTimeFormat)
    *   [func (k *Key) MustUint(defaultVal ...uint) uint](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustUint)
    *   [func (k *Key) MustUint64(defaultVal ...uint64) uint64](https://pkg.go.dev/gopkg.in/ini.v1#Key.MustUint64)
    *   [func (k *Key) Name() string](https://pkg.go.dev/gopkg.in/ini.v1#Key.Name)
    *   [func (k *Key) NestedValues() []string](https://pkg.go.dev/gopkg.in/ini.v1#Key.NestedValues)
    *   [func (k *Key) RangeFloat64(defaultVal, min, max float64) float64](https://pkg.go.dev/gopkg.in/ini.v1#Key.RangeFloat64)
    *   [func (k *Key) RangeInt(defaultVal, min, max int) int](https://pkg.go.dev/gopkg.in/ini.v1#Key.RangeInt)
    *   [func (k *Key) RangeInt64(defaultVal, min, max int64) int64](https://pkg.go.dev/gopkg.in/ini.v1#Key.RangeInt64)
    *   [func (k *Key) RangeTime(defaultVal, min, max time.Time) time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.RangeTime)
    *   [func (k *Key) RangeTimeFormat(format string, defaultVal, min, max time.Time) time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.RangeTimeFormat)
    *   [func (k *Key) SetValue(v string)](https://pkg.go.dev/gopkg.in/ini.v1#Key.SetValue)
    *   [func (k *Key) StrictBools(delim string) ([]bool, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictBools)
    *   [func (k *Key) StrictFloat64s(delim string) ([]float64, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictFloat64s)
    *   [func (k *Key) StrictInt64s(delim string) ([]int64, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictInt64s)
    *   [func (k *Key) StrictInts(delim string) ([]int, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictInts)
    *   [func (k *Key) StrictTimes(delim string) ([]time.Time, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictTimes)
    *   [func (k *Key) StrictTimesFormat(format, delim string) ([]time.Time, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictTimesFormat)
    *   [func (k *Key) StrictUint64s(delim string) ([]uint64, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictUint64s)
    *   [func (k *Key) StrictUints(delim string) ([]uint, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.StrictUints)
    *   [func (k *Key) String() string](https://pkg.go.dev/gopkg.in/ini.v1#Key.String)
    *   [func (k *Key) Strings(delim string) []string](https://pkg.go.dev/gopkg.in/ini.v1#Key.Strings)
    *   [func (k *Key) StringsWithShadows(delim string) []string](https://pkg.go.dev/gopkg.in/ini.v1#Key.StringsWithShadows)
    *   [func (k *Key) Time() (time.Time, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Time)
    *   [func (k *Key) TimeFormat(format string) (time.Time, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.TimeFormat)
    *   [func (k *Key) Times(delim string) []time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.Times)
    *   [func (k *Key) TimesFormat(format, delim string) []time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.TimesFormat)
    *   [func (k *Key) Uint() (uint, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Uint)
    *   [func (k *Key) Uint64() (uint64, error)](https://pkg.go.dev/gopkg.in/ini.v1#Key.Uint64)
    *   [func (k *Key) Uint64s(delim string) []uint64](https://pkg.go.dev/gopkg.in/ini.v1#Key.Uint64s)
    *   [func (k *Key) Uints(delim string) []uint](https://pkg.go.dev/gopkg.in/ini.v1#Key.Uints)
    *   [func (k *Key) ValidBools(delim string) []bool](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidBools)
    *   [func (k *Key) ValidFloat64s(delim string) []float64](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidFloat64s)
    *   [func (k *Key) ValidInt64s(delim string) []int64](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidInt64s)
    *   [func (k *Key) ValidInts(delim string) []int](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidInts)
    *   [func (k *Key) ValidTimes(delim string) []time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidTimes)
    *   [func (k *Key) ValidTimesFormat(format, delim string) []time.Time](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidTimesFormat)
    *   [func (k *Key) ValidUint64s(delim string) []uint64](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidUint64s)
    *   [func (k *Key) ValidUints(delim string) []uint](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValidUints)
    *   [func (k *Key) Validate(fn func(string) string) string](https://pkg.go.dev/gopkg.in/ini.v1#Key.Validate)
    *   [func (k *Key) Value() string](https://pkg.go.dev/gopkg.in/ini.v1#Key.Value)
    *   [func (k *Key) ValueWithShadows() []string](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValueWithShadows)

*   [type LoadOptions](https://pkg.go.dev/gopkg.in/ini.v1#LoadOptions)
*   [type NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper)
*   [type Parser](https://pkg.go.dev/gopkg.in/ini.v1#Parser)
*   [type Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)
*       *   [func (s *Section) Body() string](https://pkg.go.dev/gopkg.in/ini.v1#Section.Body)
    *   [func (s *Section) ChildSections() []*Section](https://pkg.go.dev/gopkg.in/ini.v1#Section.ChildSections)
    *   [func (s *Section) DeleteKey(name string)](https://pkg.go.dev/gopkg.in/ini.v1#Section.DeleteKey)
    *   [func (s *Section) GetKey(name string) (*Key, error)](https://pkg.go.dev/gopkg.in/ini.v1#Section.GetKey)
    *   [func (s *Section) HasKey(name string) bool](https://pkg.go.dev/gopkg.in/ini.v1#Section.HasKey)
    *   [func (s *Section) HasValue(value string) bool](https://pkg.go.dev/gopkg.in/ini.v1#Section.HasValue)
    *   [func (s *Section) Haskey(name string) bool](https://pkg.go.dev/gopkg.in/ini.v1#Section.Haskey)deprecated
    *   [func (s *Section) Key(name string) *Key](https://pkg.go.dev/gopkg.in/ini.v1#Section.Key)
    *   [func (s *Section) KeyStrings() []string](https://pkg.go.dev/gopkg.in/ini.v1#Section.KeyStrings)
    *   [func (s *Section) Keys() []*Key](https://pkg.go.dev/gopkg.in/ini.v1#Section.Keys)
    *   [func (s *Section) KeysHash() map[string]string](https://pkg.go.dev/gopkg.in/ini.v1#Section.KeysHash)
    *   [func (s *Section) MapTo(v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#Section.MapTo)
    *   [func (s *Section) Name() string](https://pkg.go.dev/gopkg.in/ini.v1#Section.Name)
    *   [func (s *Section) NewBooleanKey(name string) (*Key, error)](https://pkg.go.dev/gopkg.in/ini.v1#Section.NewBooleanKey)
    *   [func (s *Section) NewKey(name, val string) (*Key, error)](https://pkg.go.dev/gopkg.in/ini.v1#Section.NewKey)
    *   [func (s *Section) ParentKeys() []*Key](https://pkg.go.dev/gopkg.in/ini.v1#Section.ParentKeys)
    *   [func (s *Section) ReflectFrom(v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#Section.ReflectFrom)
    *   [func (s *Section) SetBody(body string)](https://pkg.go.dev/gopkg.in/ini.v1#Section.SetBody)
    *   [func (s *Section) StrictMapTo(v interface{}) error](https://pkg.go.dev/gopkg.in/ini.v1#Section.StrictMapTo)

*   [type StructReflector](https://pkg.go.dev/gopkg.in/ini.v1#StructReflector)
*   [type ValueMapper](https://pkg.go.dev/gopkg.in/ini.v1#ValueMapper)

This section is empty.

[View Source](https://github.com/go-ini/ini/blob/v1.67.1/ini.go#L30)

var (
	
	DefaultSection = "DEFAULT"

	
	LineBreak = "\n"

	DefaultHeader = [false](https://pkg.go.dev/builtin#false)

	PrettySection = [true](https://pkg.go.dev/builtin#true)
	
	PrettyFormat = [true](https://pkg.go.dev/builtin#true)
	PrettyEqual = [false](https://pkg.go.dev/builtin#false)
	DefaultFormatLeft = ""
	DefaultFormatRight = ""
)

IsErrDelimiterNotFound returns true if the given error is an instance of ErrDelimiterNotFound.

IsErrEmptyKeyName returns true if the given error is an instance of ErrEmptyKeyName.

func MapTo(v, source interface{}, others ...interface{}) [error](https://pkg.go.dev/builtin#error)

MapTo maps data sources to given struct.

func MapToWithMapper(v interface{}, mapper [NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper), source interface{}, others ...interface{}) [error](https://pkg.go.dev/builtin#error)

MapToWithMapper maps data sources to given struct with name mapper.

func ReflectFrom(cfg *[File](https://pkg.go.dev/gopkg.in/ini.v1#File), v interface{}) [error](https://pkg.go.dev/builtin#error)

ReflectFrom reflects data sources from given struct.

func ReflectFromWithMapper(cfg *[File](https://pkg.go.dev/gopkg.in/ini.v1#File), v interface{}, mapper [NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper)) [error](https://pkg.go.dev/builtin#error)

ReflectFromWithMapper reflects data sources from given struct with name mapper.

func StrictMapTo(v, source interface{}, others ...interface{}) [error](https://pkg.go.dev/builtin#error)

StrictMapTo maps data sources to given struct in strict mode, which returns all possible error including value parsing error.

func StrictMapToWithMapper(v interface{}, mapper [NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper), source interface{}, others ...interface{}) [error](https://pkg.go.dev/builtin#error)

StrictMapToWithMapper maps data sources to given struct with name mapper in strict mode, which returns all possible error including value parsing error.

type DebugFunc func(message [string](https://pkg.go.dev/builtin#string))

DebugFunc is the type of function called to log parse events.

type ErrDelimiterNotFound struct {
 Line [string](https://pkg.go.dev/builtin#string)}

ErrDelimiterNotFound indicates the error type of no delimiter is found which there should be one.

type ErrEmptyKeyName struct {
 Line [string](https://pkg.go.dev/builtin#string)}

ErrEmptyKeyName indicates the error type of no key name is found which there should be one.

type File struct {

	BlockMode [bool](https://pkg.go.dev/builtin#bool)

[NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper)[ValueMapper](https://pkg.go.dev/gopkg.in/ini.v1#ValueMapper)	
}

File represents a combination of one or more INI files in memory.

func Empty(opts ...[LoadOptions](https://pkg.go.dev/gopkg.in/ini.v1#LoadOptions)) *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)

Empty returns an empty file object.

func InsensitiveLoad(source interface{}, others ...interface{}) (*[File](https://pkg.go.dev/gopkg.in/ini.v1#File), [error](https://pkg.go.dev/builtin#error))

InsensitiveLoad has exactly same functionality as Load function except it forces all section and key names to be lowercased.

func Load(source interface{}, others ...interface{}) (*[File](https://pkg.go.dev/gopkg.in/ini.v1#File), [error](https://pkg.go.dev/builtin#error))

Load loads and parses from INI data sources. Arguments can be mixed of file name with string type, or raw data in []byte. It will return error if list contains nonexistent files.

func LoadSources(opts [LoadOptions](https://pkg.go.dev/gopkg.in/ini.v1#LoadOptions), source interface{}, others ...interface{}) (_ *[File](https://pkg.go.dev/gopkg.in/ini.v1#File), err [error](https://pkg.go.dev/builtin#error))

LoadSources allows caller to apply customized options for loading from data source(s).

func LooseLoad(source interface{}, others ...interface{}) (*[File](https://pkg.go.dev/gopkg.in/ini.v1#File), [error](https://pkg.go.dev/builtin#error))

LooseLoad has exactly same functionality as Load function except it ignores nonexistent files instead of returning error.

#### func [ShadowLoad](https://github.com/go-ini/ini/blob/v1.67.1/ini.go#L174)[¶](https://pkg.go.dev/gopkg.in/ini.v1#ShadowLoad "Go to ShadowLoad")added in v1.25.2

func ShadowLoad(source interface{}, others ...interface{}) (*[File](https://pkg.go.dev/gopkg.in/ini.v1#File), [error](https://pkg.go.dev/builtin#error))

ShadowLoad has exactly same functionality as Load function except it allows have shadow keys.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) Append(source interface{}, others ...interface{}) [error](https://pkg.go.dev/builtin#error)

Append appends one or more data sources and reloads automatically.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) ChildSections(name [string](https://pkg.go.dev/builtin#string)) []*[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)

ChildSections returns a list of child sections of given section name.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) DeleteSection(name [string](https://pkg.go.dev/builtin#string))

DeleteSection deletes a section or all sections with given name.

DeleteSectionWithIndex deletes a section with given name and index.

GetSection returns section by given name.

HasSection returns true if the file contains a section with given name.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) MapTo(v interface{}) [error](https://pkg.go.dev/builtin#error)

MapTo maps file to given struct.

NewRawSection creates a new section with an unparseable body.

NewSection creates a new section.

NewSections creates a list of sections.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) ReflectFrom(v interface{}) [error](https://pkg.go.dev/builtin#error)

ReflectFrom reflects file from given struct.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) Reload() (err [error](https://pkg.go.dev/builtin#error))

Reload reloads and parses all data sources.

SaveTo writes content to file system.

SaveToIndent writes content to file system with given value indention.

Section assumes named section exists and returns a zero-value when not.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) SectionStrings() [][string](https://pkg.go.dev/builtin#string)

SectionStrings returns list of section names.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) SectionWithIndex(name [string](https://pkg.go.dev/builtin#string), index [int](https://pkg.go.dev/builtin#int)) *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)

SectionWithIndex assumes named section exists and returns a new section when not.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) Sections() []*[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)

Sections returns a list of Section stored in the current instance.

SectionsByName returns all sections with given name.

func (f *[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) StrictMapTo(v interface{}) [error](https://pkg.go.dev/builtin#error)

StrictMapTo maps file to given struct in strict mode, which returns all possible error including value parsing error.

WriteTo writes file content into io.Writer.

WriteToIndent writes content into io.Writer with given indention. If PrettyFormat has been set to be true, it will align "=" sign with spaces under each section.

type Key struct {
	
}

Key represents a key under a section.

AddNestedValue adds a nested value to the key.

#### func (*Key) [AddShadow](https://github.com/go-ini/ini/blob/v1.67.1/key.go#L76)[¶](https://pkg.go.dev/gopkg.in/ini.v1#Key.AddShadow "Go to Key.AddShadow")added in v1.25.0

AddShadow adds a new shadow key to itself.

Bool returns bool type value.

Bools returns list of bool divided by given delimiter. Any invalid input will be treated as zero value.

Duration returns time.Duration type value.

Float64 returns float64 type value.

Float64s returns list of float64 divided by given delimiter. Any invalid input will be treated as zero value.

In always returns value without error, it returns default value if error occurs or doesn't fit into candidates.

InFloat64 always returns value without error, it returns default value if error occurs or doesn't fit into candidates.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) InInt(defaultVal [int](https://pkg.go.dev/builtin#int), candidates [][int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

InInt always returns value without error, it returns default value if error occurs or doesn't fit into candidates.

InInt64 always returns value without error, it returns default value if error occurs or doesn't fit into candidates.

InTime always parses with RFC3339 format and returns value without error, it returns default value if error occurs or doesn't fit into candidates.

InTimeFormat always parses with given format and returns value without error, it returns default value if error occurs or doesn't fit into candidates.

InUint always returns value without error, it returns default value if error occurs or doesn't fit into candidates.

InUint64 always returns value without error, it returns default value if error occurs or doesn't fit into candidates.

Int returns int type value.

Int64 returns int64 type value.

Int64s returns list of int64 divided by given delimiter. Any invalid input will be treated as zero value.

Ints returns list of int divided by given delimiter. Any invalid input will be treated as zero value.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) MustBool(defaultVal ...[bool](https://pkg.go.dev/builtin#bool)) [bool](https://pkg.go.dev/builtin#bool)

MustBool always returns value without error, it returns false if error occurs.

MustDuration always returns value without error, it returns zero value if error occurs.

MustFloat64 always returns value without error, it returns 0.0 if error occurs.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) MustInt(defaultVal ...[int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

MustInt always returns value without error, it returns 0 if error occurs.

MustInt64 always returns value without error, it returns 0 if error occurs.

MustString returns default value if key value is empty.

MustTime always parses with RFC3339 format and returns value without error, it returns zero value if error occurs.

MustTimeFormat always parses with given format and returns value without error, it returns zero value if error occurs.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) MustUint(defaultVal ...[uint](https://pkg.go.dev/builtin#uint)) [uint](https://pkg.go.dev/builtin#uint)

MustUint always returns value without error, it returns 0 if error occurs.

MustUint64 always returns value without error, it returns 0 if error occurs.

Name returns name of key.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) NestedValues() [][string](https://pkg.go.dev/builtin#string)

NestedValues returns nested values stored in the key. It is possible returned value is nil if no nested values stored in the key.

RangeFloat64 checks if value is in given range inclusively, and returns default value if it's not.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) RangeInt(defaultVal, min, max [int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

RangeInt checks if value is in given range inclusively, and returns default value if it's not.

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) RangeInt64(defaultVal, min, max [int64](https://pkg.go.dev/builtin#int64)) [int64](https://pkg.go.dev/builtin#int64)

RangeInt64 checks if value is in given range inclusively, and returns default value if it's not.

RangeTime checks if value with RFC3339 format is in given range inclusively, and returns default value if it's not.

RangeTimeFormat checks if value with given format is in given range inclusively, and returns default value if it's not.

SetValue changes key value.

StrictBools returns list of bool divided by given delimiter or error on first invalid input.

StrictFloat64s returns list of float64 divided by given delimiter or error on first invalid input.

StrictInt64s returns list of int64 divided by given delimiter or error on first invalid input.

StrictInts returns list of int divided by given delimiter or error on first invalid input.

StrictTimes parses with RFC3339 format and returns list of time.Time divided by given delimiter or error on first invalid input.

StrictTimesFormat parses with given format and returns list of time.Time divided by given delimiter or error on first invalid input.

StrictUint64s returns list of uint64 divided by given delimiter or error on first invalid input.

StrictUints returns list of uint divided by given delimiter or error on first invalid input.

String returns string representation of value.

Strings returns list of string divided by given delimiter.

#### func (*Key) [StringsWithShadows](https://github.com/go-ini/ini/blob/v1.67.1/key.go#L536)[¶](https://pkg.go.dev/gopkg.in/ini.v1#Key.StringsWithShadows "Go to Key.StringsWithShadows")added in v1.25.3

StringsWithShadows returns list of string divided by given delimiter. Shadows will also be appended if any.

Time parses with RFC3339 format and returns time.Time type value.

TimeFormat parses with given format and returns time.Time type value.

Times parses with RFC3339 format and returns list of time.Time divided by given delimiter. Any invalid input will be treated as zero value (0001-01-01 00:00:00 +0000 UTC).

TimesFormat parses with given format and returns list of time.Time divided by given delimiter. Any invalid input will be treated as zero value (0001-01-01 00:00:00 +0000 UTC).

Uint returns uint type valued.

Uint64 returns uint64 type value.

Uint64s returns list of uint64 divided by given delimiter. Any invalid input will be treated as zero value.

Uints returns list of uint divided by given delimiter. Any invalid input will be treated as zero value.

ValidBools returns list of bool divided by given delimiter. If some value is not 64-bit unsigned integer, then it will not be included to result list.

ValidFloat64s returns list of float64 divided by given delimiter. If some value is not float, then it will not be included to result list.

ValidInt64s returns list of int64 divided by given delimiter. If some value is not 64-bit integer, then it will not be included to result list.

ValidInts returns list of int divided by given delimiter. If some value is not integer, then it will not be included to result list.

ValidTimes parses with RFC3339 format and returns list of time.Time divided by given delimiter.

ValidTimesFormat parses with given format and returns list of time.Time divided by given delimiter.

ValidUint64s returns list of uint64 divided by given delimiter. If some value is not 64-bit unsigned integer, then it will not be included to result list.

ValidUints returns list of uint divided by given delimiter. If some value is not unsigned integer, then it will not be included to result list.

Validate accepts a validate function which can return modifed result as key value.

Value returns raw value of key for performance purpose.

#### func (*Key) [ValueWithShadows](https://github.com/go-ini/ini/blob/v1.67.1/key.go#L115)[¶](https://pkg.go.dev/gopkg.in/ini.v1#Key.ValueWithShadows "Go to Key.ValueWithShadows")added in v1.25.0

func (k *[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)) ValueWithShadows() [][string](https://pkg.go.dev/builtin#string)

ValueWithShadows returns raw values of key and its shadows if any. Shadow keys with empty values are ignored from the returned list.

type LoadOptions struct {
	Loose [bool](https://pkg.go.dev/builtin#bool)
	Insensitive [bool](https://pkg.go.dev/builtin#bool)
	InsensitiveSections [bool](https://pkg.go.dev/builtin#bool)
	InsensitiveKeys [bool](https://pkg.go.dev/builtin#bool)
	IgnoreContinuation [bool](https://pkg.go.dev/builtin#bool)
	IgnoreInlineComment [bool](https://pkg.go.dev/builtin#bool)
	SkipUnrecognizableLines [bool](https://pkg.go.dev/builtin#bool)
	ShortCircuit [bool](https://pkg.go.dev/builtin#bool)
	
	AllowBooleanKeys [bool](https://pkg.go.dev/builtin#bool)
	AllowShadows [bool](https://pkg.go.dev/builtin#bool)
	
	AllowNestedValues [bool](https://pkg.go.dev/builtin#bool)
	
	
	
	AllowPythonMultilineValues [bool](https://pkg.go.dev/builtin#bool)
	
	
	
	SpaceBeforeInlineComment [bool](https://pkg.go.dev/builtin#bool)
	
	UnescapeValueDoubleQuotes [bool](https://pkg.go.dev/builtin#bool)
	
	
	UnescapeValueCommentSymbols [bool](https://pkg.go.dev/builtin#bool)
	
	UnparseableSections [][string](https://pkg.go.dev/builtin#string)
	KeyValueDelimiters [string](https://pkg.go.dev/builtin#string)
	KeyValueDelimiterOnWrite [string](https://pkg.go.dev/builtin#string)
	ChildSectionDelimiter [string](https://pkg.go.dev/builtin#string)
	PreserveSurroundedQuote [bool](https://pkg.go.dev/builtin#bool)
	DebugFunc [DebugFunc](https://pkg.go.dev/gopkg.in/ini.v1#DebugFunc)
	ReaderBufferSize [int](https://pkg.go.dev/builtin#int)
	AllowNonUniqueSections [bool](https://pkg.go.dev/builtin#bool)
	AllowDuplicateShadowValues [bool](https://pkg.go.dev/builtin#bool)
}

LoadOptions contains all customized options used for load data source(s).

NameMapper represents a ini tag name mapper.

var (
	SnackCase [NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper) = func(raw [string](https://pkg.go.dev/builtin#string)) [string](https://pkg.go.dev/builtin#string) {
		newstr := [make](https://pkg.go.dev/builtin#make)([][rune](https://pkg.go.dev/builtin#rune), 0, [len](https://pkg.go.dev/builtin#len)(raw))
		for i, chr := range raw {
			if isUpper := 'A' <= chr && chr <= 'Z'; isUpper {
				if i > 0 {
					newstr = [append](https://pkg.go.dev/builtin#append)(newstr, '_')
				}
			}
			newstr = [append](https://pkg.go.dev/builtin#append)(newstr, [unicode](https://pkg.go.dev/unicode).[ToUpper](https://pkg.go.dev/unicode#ToUpper)(chr))
		}
		return [string](https://pkg.go.dev/builtin#string)(newstr)
	}
	TitleUnderscore [NameMapper](https://pkg.go.dev/gopkg.in/ini.v1#NameMapper) = func(raw [string](https://pkg.go.dev/builtin#string)) [string](https://pkg.go.dev/builtin#string) {
		newstr := [make](https://pkg.go.dev/builtin#make)([][rune](https://pkg.go.dev/builtin#rune), 0, [len](https://pkg.go.dev/builtin#len)(raw))
		for i, chr := range raw {
			if isUpper := 'A' <= chr && chr <= 'Z'; isUpper {
				if i > 0 {
					newstr = [append](https://pkg.go.dev/builtin#append)(newstr, '_')
				}
				chr -= 'A' - 'a'
			}
			newstr = [append](https://pkg.go.dev/builtin#append)(newstr, chr)
		}
		return [string](https://pkg.go.dev/builtin#string)(newstr)
	}
)

Built-in name getters.

type Section struct {
	
}

Section represents a config section.

#### func (*Section) [Body](https://github.com/go-ini/ini/blob/v1.67.1/section.go#L53)[¶](https://pkg.go.dev/gopkg.in/ini.v1#Section.Body "Go to Section.Body")added in v1.22.0

Body returns rawBody of Section if the section was marked as unparseable. It still follows the other rules of the INI format surrounding leading/trailing whitespace.

func (s *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)) ChildSections() []*[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)

ChildSections returns a list of child sections of current section. For example, "[parent.child1]" and "[parent.child12]" are child sections of section "[parent]".

DeleteKey deletes a key from section.

GetKey returns key in section by given name.

HasKey returns true if section contains a key with given name.

HasValue returns true if section contains given raw value.

Deprecated: Use "HasKey" instead.

Key assumes named Key exists in section and returns a zero-value when not.

KeyStrings returns list of key names of section.

func (s *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)) Keys() []*[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)

Keys returns list of keys of section.

KeysHash returns keys hash consisting of names and values.

func (s *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)) MapTo(v interface{}) [error](https://pkg.go.dev/builtin#error)

MapTo maps section to given struct.

Name returns name of Section.

NewBooleanKey creates a new boolean type key to given section.

NewKey creates a new key to given section.

func (s *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)) ParentKeys() []*[Key](https://pkg.go.dev/gopkg.in/ini.v1#Key)

ParentKeys returns list of keys of parent section.

func (s *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)) ReflectFrom(v interface{}) [error](https://pkg.go.dev/builtin#error)

ReflectFrom reflects section from given struct. It overwrites existing ones.

#### func (*Section) [SetBody](https://github.com/go-ini/ini/blob/v1.67.1/section.go#L58)[¶](https://pkg.go.dev/gopkg.in/ini.v1#Section.SetBody "Go to Section.SetBody")added in v1.30.3

SetBody updates body content only if section is raw.

func (s *[Section](https://pkg.go.dev/gopkg.in/ini.v1#Section)) StrictMapTo(v interface{}) [error](https://pkg.go.dev/builtin#error)

StrictMapTo maps section to given struct in strict mode, which returns all possible error including value parsing error.

type StructReflector interface {
 ReflectINIStruct(*[File](https://pkg.go.dev/gopkg.in/ini.v1#File)) [error](https://pkg.go.dev/builtin#error)}

StructReflector is the interface implemented by struct types that can extract themselves into INI objects.

ValueMapper represents a mapping function for values, e.g. os.ExpandEnv
