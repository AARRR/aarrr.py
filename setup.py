from setuptools import setup

setup(
    name='aarrr',
    version='0.1',
    description='aarrr',
    keywords='aarrr',
    url='http://github.com/AARRR/aarrr.py',
    author='Inndy',
    author_email='inndy.tw@gmail.com',
    license='MIT',
    packages=['aarrr'],
    zip_safe=False,
    scripts=['bin/aarrr'],
    entry_points = {
        'console_scripts': ['aarrr=aarrr.command_line:main'],
    }
)
