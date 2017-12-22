from setuptools import setup

# Runtime dependencies. See requirements.txt for development dependencies.
dependencies = [
    'requests',
]

version = '1.0.2'

setup(name='okex',
    version=version,
    description = 'Python client for the okex API',
    author = 'Winlin',
    author_email = 'pcliuguangtao@163.com',
    url = 'https://github.com/haobtc/okex',
    license = 'MIT',
    packages=['okex'],
    scripts = ['scripts/okex-poll-orderbook'],
    install_requires = dependencies,
    keywords = ['bitcoin', 'btc'],
    classifiers = [],
    zip_safe=True)
