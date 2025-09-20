from io import open
from setuptools import setup

'''
:authors: pablo-chitaksa
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2025 pablo_cheater228
'''

version = '0.0.1'
long_description = '''Easy Game gives you easy method to program
                    games on pygame!'''

setup(
    name="easy-game-py",
    version=version,

    author='pablo-chitaksa',
    author_email='solidarnostyoutub@gmail.com',

    description=(u'Easy Game gives you easy method to program'
                 u'games on pygame!'),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url="https://github.com/pablo-chitaksa/easy-game-py",
    download_url="https://github.com/pablo-chitaksa/easy-game-py/v()/v().zip".format(
        version
    ),

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['easy-game-py'],
    install_requires=['pygame', 'time', 'sys'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
