# Source: https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil

Title: boil package - github.com/volatiletech/sqlboiler/v4/boil - Go Packages

URL Source: https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil

Markdown Content:
*   [Variables](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#pkg-variables)
*   [func BeginTx(ctx context.Context, opts *sql.TxOptions) (*sql.Tx, error)](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#BeginTx)
*   [func DebugWriterFrom(ctx context.Context) io.Writer](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#DebugWriterFrom)
*   [func GetLocation() *time.Location](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#GetLocation)
*   [func HooksAreSkipped(ctx context.Context) bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#HooksAreSkipped)
*   [func IsBoilErr(err error) bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#IsBoilErr)
*   [func IsDebug(ctx context.Context) bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#IsDebug)
*   [func SetDB(db Executor)](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#SetDB)
*   [func SetLocation(loc *time.Location)](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#SetLocation)
*   [func SkipHooks(ctx context.Context) context.Context](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#SkipHooks)
*   [func SkipTimestamps(ctx context.Context) context.Context](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#SkipTimestamps)
*   [func TimestampsAreSkipped(ctx context.Context) bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#TimestampsAreSkipped)
*   [func WithDebug(ctx context.Context, debug bool) context.Context](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#WithDebug)
*   [func WithDebugWriter(ctx context.Context, writer io.Writer) context.Context](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#WithDebugWriter)
*   [func WrapErr(err error) error](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#WrapErr)
*   [type Beginner](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Beginner)
*   [type Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)
*       *   [func Blacklist(columns ...string) Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Blacklist)
    *   [func Greylist(columns ...string) Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Greylist)
    *   [func Infer() Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Infer)
    *   [func None() Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#None)
    *   [func Whitelist(columns ...string) Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Whitelist)

*       *   [func (c Columns) InsertColumnSet(cols, defaults, noDefaults, nonZeroDefaults []string) ([]string, []string)](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.InsertColumnSet)
    *   [func (c Columns) IsBlacklist() bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsBlacklist)
    *   [func (c Columns) IsGreylist() bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsGreylist)
    *   [func (c Columns) IsInfer() bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsInfer)
    *   [func (c Columns) IsNone() bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsNone)
    *   [func (c Columns) IsWhitelist() bool](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsWhitelist)
    *   [func (c Columns) UpdateColumnSet(allColumns, pkeyCols []string) []string](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.UpdateColumnSet)

*   [type ContextBeginner](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#ContextBeginner)
*   [type ContextExecutor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#ContextExecutor)
*       *   [func GetContextDB() ContextExecutor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#GetContextDB)

*   [type ContextTransactor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#ContextTransactor)
*   [type Executor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Executor)
*       *   [func GetDB() Executor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#GetDB)

*   [type HookPoint](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#HookPoint)
*   [type Transactor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Transactor)
*       *   [func Begin() (Transactor, error)](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Begin)

This section is empty.

DebugMode is a flag controlling whether generated sql statements and debug information is outputted to the DebugWriter handle

NOTE: This should be disabled in production to avoid leaking sensitive data

DebugWriter is where the debug output will be sent if DebugMode is true

BeginTx begins a transaction with the current global database handle.

DebugWriterFrom returns the debug writer for the context, or DebugWriter if not set.

GetLocation retrieves the global timestamp Location. This is the timezone used by the generated package for the automated setting of created_at and updated_at columns if the package was not generated with the --no-auto-timestamps flag.

HooksAreSkipped returns true if the context skips hooks

IsBoilErr checks if err is a boilErr

IsDebug returns true if the context has debugging enabled, or the value of DebugMode if not set.

SetDB initializes the database handle for all template db interactions

SetLocation sets the global timestamp Location. This is the timezone used by the generated package for the automated setting of created_at and updated_at columns. If the package was generated with the --no-auto-timestamps flag then this function has no effect.

SkipHooks modifies a context to prevent hooks from running for any query it encounters.

SkipTimestamps modifies a context to prevent hooks from running for any query it encounters.

TimestampsAreSkipped returns true if the context skips hooks

WithDebug modifies a context to configure debug writing. If true, all queries made using this context will be outputted to the io.Writer returned by DebugWriterFrom.

WithDebugWriter modifies a context to configure the writer written to when debugging is enabled.

WrapErr wraps err in a boilErr

type Beginner interface {
 Begin() (*[sql](https://pkg.go.dev/database/sql).[Tx](https://pkg.go.dev/database/sql#Tx), [error](https://pkg.go.dev/builtin#error)) }

Beginner begins transactions.

#### type [Columns](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L25)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns "Go to Columns")

type Columns struct {
 Kind [int](https://pkg.go.dev/builtin#int) Cols [][string](https://pkg.go.dev/builtin#string)}

Columns is a list of columns and a kind of list. Each kind interacts differently with non-zero and default column inference to produce a final list of columns for a given query. (Typically insert/updates).

func Blacklist(columns ...[string](https://pkg.go.dev/builtin#string)) [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)

Blacklist creates a list that overrides column inference choices by excluding a column from the inferred list. In essence, inference creates the list of columns, and blacklisted columns are removed from that list to produce the final list.

Greylist creates a list that adds to the inferred column choices. The final list is composed of both inferred columns and greylisted columns.

Infer is a placeholder that means there is no other list, simply infer the final list of columns for insert/update etc.

None creates an empty column list.

func Whitelist(columns ...[string](https://pkg.go.dev/builtin#string)) [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)

Whitelist creates a list that completely overrides column inference. It becomes the final list for the insert/update etc.

#### func (Columns) [InsertColumnSet](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L132)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.InsertColumnSet "Go to Columns.InsertColumnSet")

func (c [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)) InsertColumnSet(cols, defaults, noDefaults, nonZeroDefaults [][string](https://pkg.go.dev/builtin#string)) ([][string](https://pkg.go.dev/builtin#string), [][string](https://pkg.go.dev/builtin#string))

InsertColumnSet generates the set of columns to insert and return for an insert statement. The return columns are used to get values that are assigned within the database during the insert to keep the struct in sync with what's in the db. The various interactions with the different types of Columns list are outlined below.

Note that a default column's zero value is based on the Go type and does not take into account the default value in the database.

None:
 insert: empty
 return: empty

Infer:
 insert: columns-without-default + non-zero-default-columns
 return: columns-with-defaults - insert

Whitelist:
 insert: whitelist
 return: columns-with-defaults - whitelist

Blacklist:
  insert: columns-without-default + non-zero-default-columns - blacklist
  return: columns-with-defaults - insert

Greylist:
  insert: columns-without-default + non-zero-default-columns + greylist
  return: columns-with-defaults - insert

#### func (Columns) [IsBlacklist](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L85)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsBlacklist "Go to Columns.IsBlacklist")

func (c [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)) IsBlacklist() [bool](https://pkg.go.dev/builtin#bool)

IsBlacklist checks to see if these columns should be inferred. This method is here simply to not have to export the columns types.

#### func (Columns) [IsGreylist](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L100)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsGreylist "Go to Columns.IsGreylist")

func (c [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)) IsGreylist() [bool](https://pkg.go.dev/builtin#bool)

IsGreylist checks to see if these columns should be inferred. This method is here simply to not have to export the columns types.

#### func (Columns) [IsInfer](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L53)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsInfer "Go to Columns.IsInfer")

func (c [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)) IsInfer() [bool](https://pkg.go.dev/builtin#bool)

IsInfer checks to see if these columns should be inferred. This method is here simply to not have to export the columns types.

#### func (Columns) [IsNone](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L39)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsNone "Go to Columns.IsNone")added in v4.3.0

IsNone checks to see if no columns should be inferred. This method is here simply to not have to export the columns types.

#### func (Columns) [IsWhitelist](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L68)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.IsWhitelist "Go to Columns.IsWhitelist")

func (c [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)) IsWhitelist() [bool](https://pkg.go.dev/builtin#bool)

IsWhitelist checks to see if these columns should be inferred. This method is here simply to not have to export the columns types.

#### func (Columns) [UpdateColumnSet](https://github.com/volatiletech/sqlboiler/blob/v4.19.1/boil/columns.go#L181)[¶](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns.UpdateColumnSet "Go to Columns.UpdateColumnSet")

func (c [Columns](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Columns)) UpdateColumnSet(allColumns, pkeyCols [][string](https://pkg.go.dev/builtin#string)) [][string](https://pkg.go.dev/builtin#string)

UpdateColumnSet generates the set of columns to update for an update statement. The various interactions with the different types of Columns list are outlined below. In the case of greylist you can only add pkeys, which isn't useful in an update since then you can't find the original record you were trying to update.

None:      empty
Infer:     all - pkey-columns
whitelist: whitelist
blacklist: all - pkeys - blacklist
greylist:  all - pkeys + greylist

ContextBeginner allows creation of context aware transactions with options.

ContextExecutor can perform SQL queries with context

func GetContextDB() [ContextExecutor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#ContextExecutor)

GetContextDB retrieves the global state database handle as a context executor

type ContextTransactor interface {
 Commit() [error](https://pkg.go.dev/builtin#error) Rollback() [error](https://pkg.go.dev/builtin#error)
	[ContextExecutor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#ContextExecutor)
}

ContextTransactor can commit and rollback, on top of being able to execute context-aware queries.

Executor can perform SQL queries.

GetDB retrieves the global state database handle

HookPoint is the point in time at which we hook

const (
 BeforeInsertHook [HookPoint](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#HookPoint) = [iota](https://pkg.go.dev/builtin#iota) + 1  BeforeUpdateHook  BeforeDeleteHook  BeforeUpsertHook  AfterInsertHook  AfterSelectHook  AfterUpdateHook  AfterDeleteHook  AfterUpsertHook )

the hook point constants

type Transactor interface {
 Commit() [error](https://pkg.go.dev/builtin#error) Rollback() [error](https://pkg.go.dev/builtin#error)
	[Executor](https://pkg.go.dev/github.com/volatiletech/sqlboiler/v4/boil#Executor)
}

Transactor can commit and rollback, on top of being able to execute queries.

Begin a transaction with the current global database handle.
