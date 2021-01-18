import os

yaml_path = "_api"
html_path = "documents/_api_book_page"

if not os.path.exists(yaml_path):
    os.mkdir(yaml_path)
if not os.path.exists(html_path):
    os.mkdir(html_path)

for html in os.listdir(html_path):
    os.remove(os.path.join(html_path, html))

yamls = sorted([os.path.splitext(x)[0] for x in os.listdir(yaml_path) if x.endswith(".yaml")])

for i, yaml in enumerate(yamls):
    with open(os.path.join(html_path, f"{yaml}.html"), "w") as html:
        html.write("---\n")
        html.write("---\n")