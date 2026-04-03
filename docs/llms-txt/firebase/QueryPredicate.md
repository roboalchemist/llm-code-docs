# Source: https://firebase.google.com/docs/reference/swift/firebasefirestoreswift/api/reference/Enums/QueryPredicate.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate.md.txt

# FirebaseFirestore Framework Reference

# QueryPredicate

    public enum QueryPredicate

Query predicates that can be used to filter results fetched by [FirestoreQuery](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/FirestoreQuery.html).

Construct predicates using one of the following ways:  

    let onlyFavourites: QueryPredicate = .whereField("isFavourite", isEqualTo: true)
    let onlyFavourites2: QueryPredicate = .isEqualTo("isFavourite", true)
    let onlyFavourites3: QueryPredicate = .where("isFavourite", isEqualTo: true)

- `
  ``
  ``
  `

  ### [isEqualTo(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO9isEqualToyACSS_yptcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isEqualTo(_: String, _: Any)

- `
  ``
  ``
  `

  ### [isIn(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO4isInyACSS_SayypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isIn(_: String, _: [Any])

- `
  ``
  ``
  `

  ### [isNotIn(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO7isNotInyACSS_SayypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isNotIn(_: String, _: [Any])

- `
  ``
  ``
  `

  ### [arrayContains(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO13arrayContainsyACSS_yptcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case arrayContains(_: String, _: Any)

- `
  ``
  ``
  `

  ### [arrayContainsAny(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO16arrayContainsAnyyACSS_SayypGtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case arrayContainsAny(_: String, _: [Any])

- `
  ``
  ``
  `

  ### [isLessThan(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10isLessThanyACSS_yptcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isLessThan(_: String, _: Any)

- `
  ``
  ``
  `

  ### [isGreaterThan(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO13isGreaterThanyACSS_yptcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isGreaterThan(_: String, _: Any)

- `
  ``
  ``
  `

  ### [isLessThanOrEqualTo(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO19isLessThanOrEqualToyACSS_yptcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isLessThanOrEqualTo(_: String, _: Any)

- `
  ``
  ``
  `

  ### [isGreaterThanOrEqualTo(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO22isGreaterThanOrEqualToyACSS_yptcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case isGreaterThanOrEqualTo(_: String, _: Any)

- `
  ``
  ``
  `

  ### [orderBy(_:_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO7orderByyACSS_SbtcACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case orderBy(_: String, _: Bool)

- `
  ``
  ``
  `

  ### [limitTo(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO7limitToyACSicACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case limitTo(_: Int)

- `
  ``
  ``
  `

  ### [limitToLast(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO11limitToLastyACSicACmF)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      case limitToLast(_: Int)

- `
  ``
  ``
  `

  ### [whereField(_:isEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_9isEqualToACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String, isEqualTo value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:isIn:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_4isInACSS_SayypGtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String, isIn values: [Any]) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:isNotIn:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_7isNotInACSS_SayypGtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String, isNotIn values: [Any]) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:arrayContains:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_13arrayContainsACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String, arrayContains value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:arrayContainsAny:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_16arrayContainsAnyACSS_SayypGtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String,
                                    arrayContainsAny values: [Any]) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:isLessThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_10isLessThanACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String, isLessThan value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:isGreaterThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_13isGreaterThanACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String, isGreaterThan value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:isLessThanOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_19isLessThanOrEqualToACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String,
                                    isLessThanOrEqualTo value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [whereField(_:isGreaterThanOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO10whereField_22isGreaterThanOrEqualToACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func whereField(_ field: String,
                                    isGreaterThanOrEqualTo value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [order(by:descending:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5order2by10descendingACSS_SbtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func order(by field: String, descending value: Bool = false) -> QueryPredicate

- `
  ``
  ``
  `

  ### [limit(to:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5limit2toACSi_tFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func limit(to value: Int) -> QueryPredicate

- `
  ``
  ``
  `

  ### [limit(toLast:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5limit6toLastACSi_tFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func limit(toLast value: Int) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_9isEqualToACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, isEqualTo value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isIn:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_4isInACSS_SayypGtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, isIn values: [Any]) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isNotIn:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_7isNotInACSS_SayypGtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, isNotIn values: [Any]) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(field:arrayContains:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where5field13arrayContainsACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(field name: String, arrayContains value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:arrayContainsAny:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_16arrayContainsAnyACSS_SayypGtFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, arrayContainsAny values: [Any]) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isLessThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_10isLessThanACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, isLessThan value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isGreaterThan:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_13isGreaterThanACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, isGreaterThan value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isLessThanOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_19isLessThanOrEqualToACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String, isLessThanOrEqualTo value: Any) -> QueryPredicate

- `
  ``
  ``
  `

  ### [where(_:isGreaterThanOrEqualTo:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/QueryPredicate#/s:17FirebaseFirestore14QueryPredicateO5where_22isGreaterThanOrEqualToACSS_yptFZ)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      public static func `where`(_ name: String,
                                 isGreaterThanOrEqualTo value: Any) -> QueryPredicate