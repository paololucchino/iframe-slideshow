import os
from setuptools import setup, find_packages

__version__ = '0.0.1'

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'iframe_slideshow',
    version = __version__,
    author = 'Paolo Lucchino',
    author_email = 'paololucchino@gmail.com',
    url = 'https://github.com/paololucchino/iframe-slideshow',
    description = 'Module rendering html file with iframe that loops thought url list and associated labels.',
    long_description=read('README.md'),
    license='MIT',
    keywords='python iframe slideshow',
    packages = find_packages(),
    include_package_data=True,
    package_data={
        'iframe_slideshow': ['templates/*.html'],
    },
    install_requires=['jinja2'],
)
