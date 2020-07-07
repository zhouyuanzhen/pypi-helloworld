from setuptools import setup, find_packages
import io

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='zyzhelloworld',
    license='Apache License 2.0',
    version='0.1.4',
    maintainer='Yuanzhen Zhou',
    maintainer_email='szrednick@gmail.com',
    packages=find_packages(include=['helloworld', 'helloworld.*']),
    zip_safe=False,
    include_package_data=True,
    url='https://github.com/zhouyuanzhen/pypi-helloworld',
    author='Yuanzhen Zhou',
    author_email='szrednick@gmail.com',
    description='A sample PyPI helloworld project',
    long_description=readme,
    install_requires=[],
        extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
