try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.1'

with open('requirements.txt') as requirements_file:
    requires = [item for item in requirements_file]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ffice',
    version=version,
    description=("Run webapps inside Firefox"),
    long_description=readme,
    author='Cléber Zavadniak',
    author_email='contato@cleber.solutions',
    url='https://github.com/cleber-solutions/ffice',
    license=license,
    packages=['ffice'],
    entry_points='''
        [console_scripts]
        ffice=ffice.main:run
    ''',
    package_data={'': ['AUTHORS.md', 'README.md']},
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    keywords='generic libraries',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
