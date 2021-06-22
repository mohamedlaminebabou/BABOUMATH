
from setuptools import setup, find_packages


import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


# Setting up
setup(
    name='BABOUMATH',
    version='0.0.1',
    description='Accelerate Product of matrices and Rectification of some function in numpy',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/mohamedlaminebabou/BABOUMATH',  
    author='Babou Mohamed Lamine',
    author_email='mohamedlaminebabou@gmail.com',
    license='MIT', 
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numba', 'numpy'],
    keywords=['python', 'matrix', 'Matrix product', 'Matrix analysis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)


 

