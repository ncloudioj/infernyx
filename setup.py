from setuptools import setup, find_packages

setup(
    name='infernyx',
    version='0.1.41',
    packages=['infernyx'],
    url='',
    license='',
    author='tspurway',
    author_email='tspurway@mozilla.com',
    description='Inferno rules for Tiles Project',
    install_requires=['psycopg2', 'inferno', 'boto', 'geoip2', 'ua_parser', 'statsd', 'datadog'],
    scripts=['scripts/csdash.py'],
    zip_safe=False,
)
