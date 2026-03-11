# Source: https://learn.microsoft.com/en-us/ef/core/querying/user-defined-function-mapping

Title: User-defined function mapping - EF Core

URL Source: https://learn.microsoft.com/en-us/ef/core/querying/user-defined-function-mapping

Markdown Content:
EF Core allows for using user-defined SQL functions in queries. To do that, the functions need to be mapped to a CLR method during model configuration. When translating the LINQ query to SQL, the user-defined function is called instead of the CLR function it has been mapped to.

To illustrate how user-defined function mapping works, let's define the following entities:

```
public class Blog
{
    public int BlogId { get; set; }
    public string Url { get; set; }
    public int? Rating { get; set; }

    public List<Post> Posts { get; set; }
}

public class Post
{
    public int PostId { get; set; }
    public string Title { get; set; }
    public string Content { get; set; }
    public int Rating { get; set; }
    public int BlogId { get; set; }

    public Blog Blog { get; set; }
    public List<Comment> Comments { get; set; }
}

public class Comment
{
    public int CommentId { get; set; }
    public string Text { get; set; }
    public int Likes { get; set; }
    public int PostId { get; set; }

    public Post Post { get; set; }
}
```

And the following model configuration:

```
modelBuilder.Entity<Blog>()
    .HasMany(b => b.Posts)
    .WithOne(p => p.Blog);

modelBuilder.Entity<Post>()
    .HasMany(p => p.Comments)
    .WithOne(c => c.Post);
```

Blog can have many posts and each post can have many comments.

Next, create the user-defined function `CommentedPostCountForBlog`, which returns the count of posts with at least one comment for a given blog, based on the blog `Id`:

```
CREATE FUNCTION dbo.CommentedPostCountForBlog(@id int)
RETURNS int
AS
BEGIN
    RETURN (SELECT COUNT(*)
        FROM [Posts] AS [p]
        WHERE ([p].[BlogId] = @id) AND ((
            SELECT COUNT(*)
            FROM [Comments] AS [c]
            WHERE [p].[PostId] = [c].[PostId]) > 0));
END
```

To use this function in EF Core, we define the following CLR method, which we map to the user-defined function:

```
public int ActivePostCountForBlog(int blogId)
    => throw new NotSupportedException();
```

The body of the CLR method is not important. The method will not be invoked client-side, unless EF Core can't translate its arguments. If the arguments can be translated, EF Core only cares about the method signature.

Note

In the example, the method is defined on `DbContext`, but it can also be defined as a static method inside other classes.

This function definition can now be associated with user-defined function in the model configuration:

```
modelBuilder.HasDbFunction(typeof(BloggingContext).GetMethod(nameof(ActivePostCountForBlog), [typeof(int)]))
    .HasName("CommentedPostCountForBlog");
```

By default, EF Core tries to map CLR function to a user-defined function with the same name. If the names differ, we can use `HasName` to provide the correct name for the user-defined function we want to map to.

Now, executing the following query:

```
var query1 = from b in context.Blogs
             where context.ActivePostCountForBlog(b.BlogId) > 1
             select b;
```

Will produce this SQL:

```
SELECT [b].[BlogId], [b].[Rating], [b].[Url]
FROM [Blogs] AS [b]
WHERE [dbo].[CommentedPostCountForBlog]([b].[BlogId]) > 1
```

EF Core also allows for user-defined functions that get converted to a specific SQL. The SQL expression is provided using `HasTranslation` method during user-defined function configuration.

In the example below, we'll create a function that computes percentage difference between two integers.

The CLR method is as follows:

```
public double PercentageDifference(double first, int second)
    => throw new NotSupportedException();
```

The function definition is as follows:

```
// 100 * ABS(first - second) / ((first + second) / 2)
modelBuilder.HasDbFunction(
        typeof(BloggingContext).GetMethod(nameof(PercentageDifference), [typeof(double), typeof(int)]))
    .HasTranslation(
        args =>
            new SqlBinaryExpression(
                ExpressionType.Multiply,
                new SqlConstantExpression(100, new IntTypeMapping("int", DbType.Int32)),
                new SqlBinaryExpression(
                    ExpressionType.Divide,
                    new SqlFunctionExpression(
                        "ABS",
                        [
                            new SqlBinaryExpression(
                                ExpressionType.Subtract,
                                args.First(),
                                args.Skip(1).First(),
                                args.First().Type,
                                args.First().TypeMapping)
                        ],
                        nullable: true,
                        argumentsPropagateNullability: [true, true],
                        type: args.First().Type,
                        typeMapping: args.First().TypeMapping),
                    new SqlBinaryExpression(
                        ExpressionType.Divide,
                        new SqlBinaryExpression(
                            ExpressionType.Add,
                            args.First(),
                            args.Skip(1).First(),
                            args.First().Type,
                            args.First().TypeMapping),
                        new SqlConstantExpression(2, new IntTypeMapping("int", DbType.Int32)),
                        args.First().Type,
                        args.First().TypeMapping),
                    args.First().Type,
                    args.First().TypeMapping),
                args.First().Type,
                args.First().TypeMapping));
```

Once we define the function, it can be used in the query. Instead of calling database function, EF Core will translate the method body directly into SQL based on the SQL expression tree constructed from the HasTranslation. The following LINQ query:

```
var query2 = from p in context.Posts
             select context.PercentageDifference(p.BlogId, 3);
```

Produces the following SQL:

```
SELECT 100 * (ABS(CAST([p].[BlogId] AS float) - 3) / ((CAST([p].[BlogId] AS float) + 3) / 2))
FROM [Posts] AS [p]
```

If the user-defined function can only return `null` when one or more of its arguments are `null`, EFCore provides way to specify that, resulting in more performant SQL. It can be done by adding a `PropagatesNullability()` call to the relevant function parameters model configuration.

To illustrate this, define user function `ConcatStrings`:

```
CREATE FUNCTION [dbo].[ConcatStrings] (@prm1 nvarchar(max), @prm2 nvarchar(max))
RETURNS nvarchar(max)
AS
BEGIN
    RETURN @prm1 + @prm2;
END
```

and two CLR methods that map to it:

```
public string ConcatStrings(string prm1, string prm2)
    => throw new InvalidOperationException();

public string ConcatStringsOptimized(string prm1, string prm2)
    => throw new InvalidOperationException();
```

The model configuration (inside `OnModelCreating` method) is as follows:

```
modelBuilder
    .HasDbFunction(typeof(BloggingContext).GetMethod(nameof(ConcatStrings), [typeof(string), typeof(string)]))
    .HasName("ConcatStrings");

modelBuilder.HasDbFunction(
    typeof(BloggingContext).GetMethod(nameof(ConcatStringsOptimized), [typeof(string), typeof(string)]),
    b =>
    {
        b.HasName("ConcatStrings");
        b.HasParameter("prm1").PropagatesNullability();
        b.HasParameter("prm2").PropagatesNullability();
    });
```

The first function is configured in the standard way. The second function is configured to take advantage of the nullability propagation optimization, providing more information on how the function behaves around null parameters.

When issuing the following queries:

```
var query3 = context.Blogs.Where(e => context.ConcatStrings(e.Url, e.Rating.ToString()) != "https://mytravelblog.com/4");
var query4 = context.Blogs.Where(
    e => context.ConcatStringsOptimized(e.Url, e.Rating.ToString()) != "https://mytravelblog.com/4");
```

We get this SQL:

```
SELECT [b].[BlogId], [b].[Rating], [b].[Url]
FROM [Blogs] AS [b]
WHERE ([dbo].[ConcatStrings]([b].[Url], CONVERT(VARCHAR(11), [b].[Rating])) <> N'Lorem ipsum...') OR [dbo].[ConcatStrings]([b].[Url], CONVERT(VARCHAR(11), [b].[Rating])) IS NULL

SELECT [b].[BlogId], [b].[Rating], [b].[Url]
FROM [Blogs] AS [b]
WHERE ([dbo].[ConcatStrings]([b].[Url], CONVERT(VARCHAR(11), [b].[Rating])) <> N'Lorem ipsum...') OR ([b].[Url] IS NULL OR [b].[Rating] IS NULL)
```

The second query doesn't need to re-evaluate the function itself to test its nullability.

Note

This optimization should only be used if the function can only return `null` when it's parameters are `null`.

EF Core also supports mapping to a table-valued function using a user-defined CLR method returning an `IQueryable` of entity types, allowing EF Core to map TVFs with parameters. The process is similar to mapping a scalar user-defined function to a SQL function: we need a TVF in the database, a CLR function that is used in the LINQ queries, and a mapping between the two.

As an example, we'll use a table-valued function that returns all posts having at least one comment that meets a given "Like" threshold:

```
CREATE FUNCTION dbo.PostsWithPopularComments(@likeThreshold int)
RETURNS TABLE
AS
RETURN
(
    SELECT [p].[PostId], [p].[BlogId], [p].[Content], [p].[Rating], [p].[Title]
    FROM [Posts] AS [p]
    WHERE (
        SELECT COUNT(*)
        FROM [Comments] AS [c]
        WHERE ([p].[PostId] = [c].[PostId]) AND ([c].[Likes] >= @likeThreshold)) > 0
)
```

The CLR method signature is as follows:

```
public IQueryable<Post> PostsWithPopularComments(int likeThreshold)
    => FromExpression(() => PostsWithPopularComments(likeThreshold));
```

Tip

The `FromExpression` call in the CLR function body allows for the function to be used instead of a regular DbSet.

And below is the mapping:

```
modelBuilder.Entity<Post>().ToTable("Posts");
modelBuilder.HasDbFunction(typeof(BloggingContext).GetMethod(nameof(PostsWithPopularComments), [typeof(int)]));
```

Note

A queryable function must be mapped to a table-valued function and can't make use of `HasTranslation`.

When the function is mapped, the following query:

```
var likeThreshold = 3;
var query5 = from p in context.PostsWithPopularComments(likeThreshold)
             orderby p.Rating
             select p;
```

Produces:

```
SELECT [p].[PostId], [p].[BlogId], [p].[Content], [p].[Rating], [p].[Title]
FROM [dbo].[PostsWithPopularComments](@likeThreshold) AS [p]
ORDER BY [p].[Rating]
```
