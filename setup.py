from setuptools import setup, find_packages

import sys

version = open("version.txt").read().rstrip()
requirements = [k.strip() for k in open("requirements.txt").read().split()]

setup(
    name='selFlow',
    version=version,
    description='Self-Supervised Learning of Optical Flow',
    long_description=open('README.md').read(),
    url='https://github.com/ppliuboy/SelFlow',
    license='GPLv3',

    author='Pengpeng liu, Michael R. Lyu, Irwin King, Jia Xu',
    author_email='ppliu@cse.cuhk.edu.hk',

    packages=find_packages(),
    include_package_data=True,

    install_requires=requirements,

    entry_points={

    },

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: System :: Clustering',
      ]
)
