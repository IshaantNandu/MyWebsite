# /usr/local/bin/python3.13

from flask_sitemap import Sitemap  # type: ignore
from os import scandir
import markdown  # type: ignore
from flask import *
from markupsafe import Markup


def createApp():
    extensions = ["markdown.extensions.extra",
                  "markdown.extensions.abbr",
                  "markdown.extensions.attr_list",
                  "markdown.extensions.def_list",
                  "markdown.extensions.fenced_code",
                  "markdown.extensions.footnotes",
                  "markdown.extensions.md_in_html",
                  "markdown.extensions.tables",
                  "markdown.extensions.admonition",

                  "markdown.extensions.legacy_attrs",
                  "markdown.extensions.legacy_em",
                  "markdown.extensions.meta",
                  "markdown.extensions.nl2br",
                  "markdown.extensions.sane_lists",
                  "markdown.extensions.smarty",
                  "markdown.extensions.toc",
                  "markdown.extensions.wikilinks", "markdown_sub_sup",
                  'iconfonts',
                  'markdown_del_ins',
                  'kbdextension',
                  'markdown_checklist.extension',
                  'markdown.extensions.attr_list', 'pymdownx.extra',
                  'pymdownx.superfences',
                  'pymdownx.tabbed',
                  'pymdownx.tasklist',
                  'pymdownx.inlinehilite',
                  'pymdownx.emoji',"markdown.extensions.codehilite"]
    app: Flask = Flask(__name__)
    view_funcs = {}
    template: str = ''
    with open('./templates/index.htm') as t:
        template = t.read()

    def create_view_func(html_content):
        return lambda: html_content

    def routeMapping(dir='./templates/blogs'):
        app.register_error_handler(400,'Error')
        with scandir(dir) as entries:
            for entry in entries:
                try:
                    with open(entry.path) as f:
                        print(entry.path)
                        content = template.replace('{{content}}', markdown.markdown(f.read(),
                                                                                    extensions=extensions))

                        html = Markup(content)
                        view_func_name = f'view_{entry.name.replace(
                            ".", "_")}'  # Generate a unique name
                        unique_view_func = create_view_func(html)
                        app.add_url_rule(
                            f'/{entry.name.split(".")[0]}/' if not entry.name.split(".")[
                                0] == 'index' else '/',
                            endpoint=view_func_name,
                            view_func=unique_view_func)

                except Exception as e:
                    print(e)
                finally:
                    print("Registered Routes:")
                    for rule in app.url_map.iter_rules():
                        print(f"{rule}: {rule.endpoint}")
    routeMapping()
    ext = Sitemap(app=app)
    ext.app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS']=True
    return app


if __name__ == '__main__':
    server = createApp()

    server.run(port=5001, use_reloader=False)
