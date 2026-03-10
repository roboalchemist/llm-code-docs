# Use a loop to create and save 5 unique articles with predefined titles and bodies
titles = ["Welcome to Rails", "Exploring Rails", "Advanced Rails", "Rails Tips", "Rails in Production"]
bodies = [
  "This is your first step into Ruby on Rails.",
  "Dive deeper into the Rails framework.",
  "Explore advanced features of Rails.",
  "Quick tips for Rails developers.",
  "Managing Rails applications in production environments."
]

titles.each_with_index do |title, index|
  article = Article.new(title: title, body: bodies[index])
  article.save # Saves the entry to the database
end
```

## 8. Start searching

### Backend search

The backend search returns ORM-compliant objects reloaded from your database.

```Ruby theme={null}