
import os
import re
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

base_dir = os.path.dirname(os.path.abspath(__file__))


def get_version(filename="seafoam/__init__.py"):
    with open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)


setup(
    name="seafoam",
    version=get_version(),
    description="Pelican theme, first used for Minchin.ca.",
    long_description="\n\n".join([open(os.path.join(base_dir, "README.rst")).read()]),
    author="W. Minchin",
    author_email="w_minchin@hotmail.com",
    url="https://github.com/MinchinWeb/seafoam",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pelican',
        'minchin.pelican.plugins.image_process>=1.0.1',
        'minchin.pelican.jinja_filters',
        # requires asset plugin, bundle? -- https://github.com/getpelican/pelican-plugins/tree/master/assets
        # and others, I'm sure...
        # pathlib2 on Python 2.7
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
