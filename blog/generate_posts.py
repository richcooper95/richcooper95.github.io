#!/usr/bin/env python3

import json
import re
import yaml
from datetime import datetime, date
from pathlib import Path

def read_markdown_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Split front matter and content
    if content.startswith('---'):
        _, front_matter, content = content.split('---', 2)
        metadata = yaml.safe_load(front_matter)
    else:
        metadata = {}

    return metadata, content.strip()

def generate_slug(title):
    # Convert to lowercase and replace spaces with hyphens
    slug = title.lower()
    # Remove special characters
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    # Replace spaces with hyphens
    slug = re.sub(r'\s+', '-', slug)
    return slug

def format_date(date_value):
    if isinstance(date_value, (date, datetime)):
        return date_value.strftime('%Y-%m-%d')
    return str(date_value)

def format_display_date(date_value):
    if isinstance(date_value, (date, datetime)):
        return date_value.strftime('%B %d, %Y')
    try:
        if isinstance(date_value, str):
            parsed_date = datetime.strptime(date_value, '%Y-%m-%d')
        else:
            parsed_date = datetime.strptime(str(date_value), '%Y-%m-%d')
        return parsed_date.strftime('%B %d, %Y')
    except (ValueError, TypeError):
        return str(date_value)

def generate_post_html(metadata, content, slug):
    post_date = metadata.get('date', datetime.now().strftime('%Y-%m-%d'))
    formatted_date = format_date(post_date)
    display_date = format_display_date(post_date)

    # Define CSS separately to avoid f-string issues
    footnote_css = """
        /* Footnote styles */
        .footnotes {
            margin-top: 2rem;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
            padding-top: 1rem;
            font-size: 0.9rem;
        }

        .footnote {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
            text-indent: -1.5rem;
        }

        .footnote-backref {
            margin-left: 0.5rem;
            text-decoration: none;
        }
    """

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('title', 'Blog Post')}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="../../../static/style.css">
    <link rel="stylesheet" href="../../blog.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>📝</text></svg>">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,700;1,300;1,700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/marked-footnote/dist/index.umd.min.js"></script>
    <style>
{footnote_css}
    </style>
</head>
<body>
    <div class="background-container">
        <div class="background-image"></div>

        <main class="content-container blog-content">
            <div class="blog-header">
                <a href="../../" class="home-link">← Back to Blog</a>
            </div>

            <article class="blog-post">
                <h1>{metadata.get('title', 'Blog Post')}</h1>
                <div class="post-meta">
                    <time datetime="{formatted_date}">{display_date}</time>
                    {' '.join(f'<span class="tag">{tag}</span>' for tag in metadata.get('tags', []))}
                </div>
                <div class="post-content" id="content"></div>
            </article>
        </main>

        <footer class="copyright">
            © <span id="current-year"></span> by Rich Barton-Cooper
        </footer>
    </div>

    <script>
        // Render Markdown content
        const content = `{content.replace('`', '\\`')}`;
        document.getElementById('content').innerHTML = new marked.Marked()
            .use(markedFootnote())
            .parse(content);

        // Update copyright year
        document.getElementById('current-year').textContent = new Date().getFullYear();
    </script>
</body>
</html>'''

def main():
    posts_dir = Path('posts/generated')
    posts_dir.mkdir(exist_ok=True, parents=True)

    posts_data = []

    # Process each Markdown file
    for md_file in Path('posts').glob('*.md'):
        metadata, content = read_markdown_file(md_file)

        # Generate slug from title
        slug = generate_slug(metadata.get('title', 'Blog Post'))

        # Create post data for JSON
        post_data = {
            'title': metadata.get('title', 'Blog Post'),
            'date': format_date(metadata.get('date', datetime.now().strftime('%Y-%m-%d'))),
            'description': metadata.get('description', ''),
            'tags': metadata.get('tags', []),
            'slug': slug
        }
        posts_data.append(post_data)

        # Generate HTML file
        html_content = generate_post_html(metadata, content, slug)
        html_file = posts_dir / f'{slug}.html'
        with open(html_file, 'w') as f:
            f.write(html_content)

    # Sort posts by date
    posts_data.sort(key=lambda x: x['date'], reverse=True)

    # Write posts.json
    with open('posts.json', 'w') as f:
        json.dump(posts_data, f, indent=2)

if __name__ == '__main__':
    main()