wundergraph::query_builder::selection
# Trait LoadingHandler 
Source 

```
pub trait LoadingHandler<DB, Ctx>: HasTable + Sizedwhere
    DB: Backend + ApplyOffset + 'static,{
    type Columns: BuildOrder<Self::Table, DB> + BuildSelect<Self::Table, DB, SqlTypeOfPlaceholder<Self::FieldList, DB, Self::PrimaryKeyIndex, Self::Table, Ctx>>;
    type FieldList: WundergraphFieldList<DB, Self::PrimaryKeyIndex, Self::Table, Ctx>;
    type PrimaryKeyIndex: Default + IsPrimaryKeyIndex;
    type Filter: InnerFilter + BuildFilter<DB> + 'static;

    const FIELD_NAMES: &'static [&'static str];
    const TYPE_NAME: &'static str;
    const TYPE_DESCRIPTION: Option<&'static str> = None;

    // Provided methods
    fn load<'a>(
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
        query: BoxedQuery<'a, Self, DB, Ctx>,
    ) -> Result<Vec<Value<WundergraphScalarValue>>>
       where DB: HasSqlType<SqlTypeOfPlaceholder<Self::FieldList, DB, Self::PrimaryKeyIndex, Self::Table, Ctx>>,
             Ctx: WundergraphContext + QueryModifier<Self, DB>,
             Ctx::Connection: Connection<Backend = DB>,
             DB::QueryBuilder: Default,
             <Self::Table as QuerySource>::FromClause: QueryFragment<DB> { ... }
    fn load_by_primary_key<'a>(
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
        selection: Option<&[Selection<'_, WundergraphScalarValue>]>,
        executor: &Executor<'_, Ctx, WundergraphScalarValue>,
        query: BoxedQuery<'a, Self, DB, Ctx>,
    ) -> Result<Option<Value<WundergraphScalarValue>>>
       where Self: 'static,
             &'static Self: Identifiable,
             Ctx: WundergraphContext + QueryModifier<Self, DB>,
             Ctx::Connection: Connection<Backend = DB>,
             <&'static Self as Identifiable>::Id: UnRef<'static>,
             <Self::Table as Table>::PrimaryKey: EqAll<<<&'static Self as Identifiable>::Id as UnRef<'static>>::UnRefed> + Default,
             <<Self::Table as Table>::PrimaryKey as EqAll<<<&'static Self as Identifiable>::Id as UnRef<'static>>::UnRefed>>::Output: AppearsOnTable<Self::Table> + NonAggregate + QueryFragment<DB>,
             PrimaryKeyArgument<'static, Self::Table, (), <&'static Self as Identifiable>::Id>: FromLookAheadValue,
             DB: HasSqlType<SqlTypeOfPlaceholder<Self::FieldList, DB, Self::PrimaryKeyIndex, Self::Table, Ctx>>,
             DB::QueryBuilder: Default,
             <Self::Table as QuerySource>::FromClause: QueryFragment<DB> { ... }
    fn build_query<'a>(
        _global_arguments: &[LookAheadArgument<'_, WundergraphScalarValue>],
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
    ) -> Result<BoxedQuery<'a, Self, DB, Ctx>>
       where Self::Table: BoxedDsl<'a, DB, Output = BoxedSelectStatement<'a, SqlTypeOf<<Self::Table as Table>::AllColumns>, Self::Table, DB>> + 'static,
             <Self::Filter as BuildFilter<DB>>::Ret: AppearsOnTable<Self::Table> { ... }
    fn get_select(
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
    ) -> Result<Box<dyn BoxableExpression<Self::Table, DB, SqlType = SqlTypeOfPlaceholder<Self::FieldList, DB, Self::PrimaryKeyIndex, Self::Table, Ctx>>>> { ... }
    fn apply_filter<'a>(
        query: BoxedQuery<'a, Self, DB, Ctx>,
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
    ) -> Result<BoxedQuery<'a, Self, DB, Ctx>>
       where Self::Table: 'static,
             <Self::Filter as BuildFilter<DB>>::Ret: AppearsOnTable<Self::Table> { ... }
    fn apply_order<'a>(
        query: BoxedQuery<'a, Self, DB, Ctx>,
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
    ) -> Result<BoxedQuery<'a, Self, DB, Ctx>>
       where Self::Table: 'static { ... }
    fn apply_limit<'a>(
        query: BoxedQuery<'a, Self, DB, Ctx>,
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
    ) -> Result<BoxedQuery<'a, Self, DB, Ctx>> { ... }
    fn apply_offset<'a>(
        query: BoxedQuery<'a, Self, DB, Ctx>,
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
    ) -> Result<BoxedQuery<'a, Self, DB, Ctx>> { ... }
}
```

## Required Associated Constants§