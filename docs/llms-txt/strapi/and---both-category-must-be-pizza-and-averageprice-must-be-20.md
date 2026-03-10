# and - both category must be "pizza" AND averagePrice must be < 20
{
  restaurants(filters: {
    and: [
      { category: { eq: "pizza" } },
      { averagePrice: { lt: 20 } }
    ]
  }) {
    name
  }
}