from setuptools import setup, find_packages

DESCRIPTION = 'Pretty Colour Palettes'
LONG_DESCRIPTION = 'Defines aesthetically pleasing colour palettes.'


setup(
        name="PrettyCols",
        version="1.0.0",
        author="Nicola Rennie",
        author_email="nrennie35@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["colour>=0.1.5", "matplotlib>=3.5.1"],
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent"
        ]
)
