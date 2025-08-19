# Blog System

This directory contains the blog system for the website, including Markdown posts, generation scripts, and styling.

## Writing a New Blog Post

Follow these steps to create and publish a new blog post:

### 1. Create a new Markdown file
Create a new file in the `blog/posts/` directory:
```
blog/posts/your-post-name.md
```

### 2. Add front matter
Add metadata at the top of your Markdown file:
```markdown
---
title: Your Blog Post Title
date: YYYY-MM-DD
description: A brief description of your post
tags: [tag1, tag2]
---
```

### 3. Write your content
Write your post content in Markdown below the front matter:
```markdown
# Your Blog Post Content

Write your post here using standard Markdown syntax.

## You can use headers

- Lists
- Work great

You can also include footnotes[^1] and images.

[^1]: This is a footnote.
```

### 4. Add images (if needed)
- Place images in the `static/images/` directory
- Reference them in your post using HTML:
```html
<img src="../../../static/images/your-image.jpg" alt="Description" class="align-center">
<p class="image-caption">Your caption here</p>
```

**Image alignment options:**
- `class="align-center"` - Center the image (default)
- `class="align-left"` - Float image to the left with text wrapping
- `class="align-right"` - Float image to the right with text wrapping

### 5. Generate the HTML files
Run the generation script to convert your Markdown to HTML:
```bash
cd blog
python3 generate_posts.py
```

### 6. Test locally (optional)
Start a local server to preview your changes:
```bash
cd ..
python3 -m http.server 8000
# Visit http://localhost:8000
```

### 7. Deploy
Commit and push your changes to GitHub:
```bash
git add .
git commit -m "Add new blog post: Your Post Title"
git push
```

## What the Script Does

The `generate_posts.py` script automatically:
- Generates an HTML file for each Markdown post in `posts/generated/`
- Updates the `posts.json` file with post metadata
- Makes your post appear on the blog index page
- Updates the homepage blog tile with recent posts

## Features Supported

- **Markdown syntax** - Headers, lists, links, emphasis, code blocks
- **Footnotes** - Use `[^1]` syntax for footnote references
- **Images** - Support for alignment, captions, and galleries
- **Front matter** - YAML metadata for title, date, description, and tags
- **Responsive design** - Optimized for desktop and mobile viewing

## File Structure

```
blog/
├── README.md              # This file
├── index.html             # Blog listing page
├── blog.css              # Blog-specific styles
├── generate_posts.py     # Script to generate HTML from Markdown
├── posts.json            # Generated metadata file
└── posts/
    ├── your-post.md      # Your Markdown files
    └── generated/
        └── your-post.html # Generated HTML files
```

## Tips

- Use descriptive filenames for your Markdown files
- Keep descriptions concise for better display in previews
- Test locally before deploying to catch any issues
- Use meaningful tags to help organize your content
- Optimize images before adding them to keep the site fast
