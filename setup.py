from setuptools import setup

setup(
    name='protohype',
    packages=['protohype'],
    platforms='any',
    version='1.3.0',
    description='Hypothesis extension to allow generating protobuf messages matching a schema.',
    long_description=open('README.md').read(),
    author='Tharsus',
    author_email='nicholas.martin@tharsus.co.uk',
    url='https://github.com/tharsus-ltd/protohype',
    license='MIT',
    install_requires=[
        'hypothesis==6.10.0',
        'protobuf==3.15.8'
    ],
    tests_require=['pytest>=3.1.2', 'future>=0.16.0'],
    extras_require={'dev': ['pytest>=3.1.2', 'future>=0.16.0']},
    classifiers=[
        'Framework :: Hypothesis',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
