import pathlib
from setuptools import setup

version = pathlib.Path(__file__).parent.absolute()
version = version / 'thonnycontrib/thonny-shoebot/_version.py'
exec(open(version).read())

README = (pathlib.Path(__file__).parent / 'README.md').read_text()

setup(
  name='thonny-shoebot',
  version=__version__,
  description='shoebot plugin for Thonny',
  long_description=README,
  long_description_content_type='text/markdown',
  url='https://github.com/shoebot/thonny-shoebot',
  author='rlafuente',
  author_email='r@manufacturaindependente.org',
  license='GPL',
  classifiers=[
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    'Environment :: Plugins',
    'Topic :: Multimedia :: Graphics',
    'Topic :: Text Editors :: Integrated Development Environments (IDE)'
  ],
  packages=[
    'thonnycontrib.kyanite_theme_syntax',
    'thonnycontrib.kyanite_theme_ui',
    'thonnycontrib.thonny-shoebot',
    'thonnycontrib.thonny-shoebot.py5colorpicker.tkcolorpicker'
  ],
  install_requires=[
    'shoebot==1.4',
    'pyclip==0.7.0',
    'pyperclip'
  ]
)
