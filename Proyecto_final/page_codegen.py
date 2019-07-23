from os import mkdir
from os.path import exists, dirname, join
import jinja2
from page_test import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    page_mm = get_entity_mm(debug)

    page_model = page_mm.model_from_file(join(this_folder, 'page.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in page_model.entities:
            return True
        else:
            return False
    
    def htmltype(s):        
        return {
                'float': 'number',
                'integer': 'number',
                'string': 'text',
                'bool': 'checkbox'
        }.get(s.name, s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['htmltype'] = htmltype

    template = jinja_env.get_template('html.template')

    for pagina in page_model.entities:
        # For each entity generate html file
        with open(join(srcgen_folder,
            "%s.html" % pagina.name.capitalize()), 'w') as f:
            f.write(template.render(entity=pagina))

    template = jinja_env.get_template('styles.template')
    with open(join(srcgen_folder, "Estilo.css"), 'w') as f:
        f.write(template.render())


if __name__ == "__main__":
    main()

"""
  https://es.wikipedia.org/wiki/Linux       
  https://docs.python.org/2/library/re.html       
  https://pypi.org/project/ply/       
  https://pypi.org/project/textX/       
  https://pypi.org/project/Jinja2/       
  https://docs.djangoproject.com/es/2.2/   
  https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  https://docs.python.org/3/
"""