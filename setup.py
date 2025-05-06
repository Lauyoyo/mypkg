from setuptools import setup, find_packages

setup(
    name='mypkg',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Lauyoyo',
    description='A test package hosted on GitHub',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Lauyoyo/mypkg',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
