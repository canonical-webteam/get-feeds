from setuptools import setup

setup(
    name='canonicalwebteam.get-feeds',
    version='0.1.0',
    author='Canonical Webteam',
    url='https://github.com/canonical-webteam/get-feeds',
    packages=[
        'canonicalwebteam.get-feeds'
    ],
    description=(
        'Functions and template tags for retrieving JSON '
        'or RSS feed content.'
    ),
    install_requires=[
        "Django >= 1.3",
    ],
)

