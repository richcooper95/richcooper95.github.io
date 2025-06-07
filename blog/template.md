---
title: Your Blog Post Title
date: YYYY-MM-DD
description: A brief description of your post
tags: [tag1, tag2]
---

Write your blog post content here in Markdown format.

## Headers work like this

- Lists work
- Like this

```python
# Code blocks work like this
def hello():
    print("Hello, world!")
```

And you can include [links](https://example.com) and *formatting* too.

## Adding Images

To add images to your blog posts:

1. Place your images in the `static/images` directory
2. Reference them in your Markdown using HTML:

```html
<!-- Center-aligned image (default) -->
<img src="../../../static/images/your-image.jpg" alt="Image description" class="align-center">

<!-- Left-aligned image -->
<img src="../../../static/images/your-image.jpg" alt="Image description" class="align-left">

<!-- Right-aligned image -->
<img src="../../../static/images/your-image.jpg" alt="Image description" class="align-right">

<!-- Image with caption -->
<img src="../../../static/images/your-image.jpg" alt="Image description">
<p class="image-caption">This is a caption for the image</p>
```

3. You can also use remote images by using their URL:

```html
<img src="https://example.com/image.jpg" alt="Remote image">
```