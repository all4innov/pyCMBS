import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='PyCMBS',
      author='Houssem Medhioub',
      author_email='houssem.medhioub@it-sudparis.eu',
      version='0.1',
      description='PyCMBS: A Python implementation of a Message Brokering Service for Cloud',
      long_description=read('README'),
      url='http://www.example.com/PyCMBS',
      platforms=['any'],
      #packages=['pycmbs'],
      packages=find_packages(), #['pycmbs'],
      package_data = {
        # If any package contains *.txt or *.rst files, include them:
        'pycmbs': ['*.py', '*.conf'],
        # And include any *.msg files found in the 'pycmbs' package, too:
        'pycmbs': ['*.msg'],
        },
      install_requires=[
          'config',
          'configobj',
          'logging',
          'ordereddict',
          'simplejson',
          'jsonpickle',
          'sphinx',
          'ZODB3',
          'pyzmq',
          'CouchDB'
          #'pack>=0.97',
          #'pack'
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7'
      ]
)
