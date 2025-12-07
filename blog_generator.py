# blog_generator.py

# Blog title and author
blog_title = "The Future of Technology Blog"
author_name = "Your Name"

# Sections and subtopics
sections = {
    "Industry Trends": [
        ("AI & Machine Learning", "AI is being used everywhere. Example: Chatbots."),
        ("Remote Work Technologies", "Tools like Zoom and Slack are key for teams."),
        ("Cybersecurity Focus", "Protecting data is more important than ever."),
        ("Sustainable Tech", "Eco-friendly computing is trending.")
    ],
    "Innovative Technologies": [
        ("Blockchain", "Used beyond crypto for secure transactions."),
        ("IoT", "Smart devices connect and share data automatically."),
        ("5G Networks", "Enables faster connections for AR/VR."),
        ("AR/VR", "Transforming training and customer experiences.")
    ],
    "Best Practices": [
        ("Continuous Learning", "Keep learning through courses and webinars."),
        ("Adopt Agile Methodologies", "Agile improves team productivity."),
        ("Invest in Cyber Hygiene", "Updates, backups, secure passwords."),
        ("Networking and Collaboration", "Engage with peers and communities.")
    ]
}

# References
references = [
    ("Gartner Technology Trends", "https://www.gartner.com/en/newsroom/press-releases"),
    ("Forbes Tech Innovation", "https://www.forbes.com/innovation/"),
    ("World Economic Forum: Technology", "https://www.weforum.org/agenda/archive/technology/")
]

import os

# Create the HTML structure
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{blog_title}</title>
<style>
body {{ font-family: "Times New Roman", serif; background: #f7f7f7; margin:0; padding:0; color:#333; }}
header {{ background:#004080; color:white; text-align:center; padding:20px 0; }}
nav {{ background:#0066cc; padding:10px 0; text-align:center; }}
nav a {{ color:white; margin:0 15px; text-decoration:none; font-weight:bold; }}
nav a:hover {{ text-decoration:underline; }}
.container {{ max-width:900px; margin:20px auto; padding:20px; background:white; box-shadow:0 0 10px rgba(0,0,0,0.1);}}
h1,h2,h3{{ color:#004080;}}
footer {{ background:#004080; color:white; text-align:center; padding:15px 0; margin-top:20px;}}
ul {{ margin-left:20px; }}
a.cite-link {{ color:#0066cc; text-decoration:none; }}
a.cite-link:hover {{ text-decoration:underline; }}
</style>
</head>
<body>

<header>
<h1>{blog_title}</h1>
<p>Exploring Trends, Innovations, and Best Practices</p>
</header>

<nav>
"""

# Add navigation links
for section in sections.keys():
    html_content += f'<a href="#{section.replace(" ", "")}">{section}</a>'
html_content += '<a href="#About">About</a><a href="#References">References</a></nav>'

# Add sections and subtopics
for section, items in sections.items():
    html_content += f'<div class="container" id="{section.replace(" ", "")}"><h2>{section}</h2>'
    for subheading, text in items:
        html_content += f'<h3>{subheading}</h3><p>{text}</p>'
    html_content += '</div>'

# About section
html_content += f'<div class="container" id="About"><h2>About the Author</h2><p>Hello! I’m {author_name}, a student passionate about technology. This blog shares insights on trends, innovations, and best practices in tech.</p></div>'

# References section
html_content += '<div class="container" id="References"><h2>References</h2><ul>'
for name, link in references:
    html_content += f'<li><a href="{link}" target="_blank" class="cite-link">{name}</a></li>'
html_content += '</ul></div>'

# Footer
html_content += f'<footer><p>&copy; 2025 {blog_title}. All rights reserved.</p></footer></body></html>'

# Write HTML file to templates/blog.html
os.makedirs("templates", exist_ok=True)
with open("templates/blog.html", "w") as file:
    file.write(html_content)

print("Blog generated successfully! Open templates/blog.html in your browser.")
