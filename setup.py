#! /usr/bin/env python3

import setuptools

setuptools.setup(
    name='pytap2',
    version='0.2.0',

    description='Object-oriented wrapper around Linux TUN/TAP device',
    long_description=open('README.rst').read(),
    keywords=('tun', 'tap', 'networking'),

    author='John Hagen',
    author_email='johnthagen@gmail.com',
    url='https://github.com/johnthagen/pytap2',
    packages=setuptools.find_packages(),
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)