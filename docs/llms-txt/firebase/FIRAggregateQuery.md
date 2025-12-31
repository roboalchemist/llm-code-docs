# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery.md.txt

# FirebaseFirestore Framework Reference

# FIRAggregateQuery


    @interface FIRAggregateQuery : NSObject

A query that calculates aggregations over an underlying query.
- `
  ``
  ``
  `

  ### [query](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery#/c:objc(cs)FIRAggregateQuery(py)query)

  `
  `  
  The query whose aggregations will be calculated by this object.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQuery.html *_Nonnull query;

- `
  ``
  ``
  `

  ### [-aggregationWithSource:completion:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuery#/c:objc(cs)FIRAggregateQuery(im)aggregationWithSource:completion:)

  `
  `  
  Executes this query.  

  #### Declaration

  Objective-C  

      - (void)aggregationWithSource:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRAggregateSource.html)source
                         completion:
                             (nonnull void (^)(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRAggregateQuerySnapshot.html *_Nullable,
                                               NSError *_Nullable))completion;

  #### Parameters

  |--------------------|---------------------------------------------------------------------------------------------------------------------|
  | ` `*source*` `     | The source from which to acquire the aggregate results.                                                             |
  | ` `*completion*` ` | a block to execute once the results have been successfully read. snapshot will be `nil` only if error is `non-nil`. |