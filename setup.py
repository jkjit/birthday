from setuptools import setup

setup(
    name='birthday',
    version='1.0',
    packages=['com'],
    url='abc@and.com',
    license='',
    author='jayakumar',
    author_email='',
    description='birthday diary',
    entry_points={"console_scripts": ['birthday=com.birthday_main:main']}
)
