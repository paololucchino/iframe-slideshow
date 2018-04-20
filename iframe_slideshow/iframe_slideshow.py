from jinja2 import Environment, PackageLoader
import os

class IFrameSlideshow():

    def __init__(self,src_list, label_list):

        self.src_list = src_list
        self.label_list = label_list

    def save(self, filename='temp.html'):

        j2_env = Environment(loader=PackageLoader('iframe_slideshow', 'templates'),
                             trim_blocks=True)
        rendered_html =  j2_env.get_template('template.html').render(
            src_list=self.src_list,
            label_list=self.label_list
        )

        with open(filename, 'w') as handle:
            handle.write(rendered_html)

        return rendered_html