from setuptools import setup, find_packages
setup(
    name="Campionato_calcio",
    version="1.0",
    packages=find_packages(),
    scripts=[],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.css', '*.js', '*.png'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Mattia Miceli",
    author_email="188478@studenti.unimore.it",
    description="Esame di Linguaggi Dinamici 2018/2019",
    keywords="Esame Linguaggi Dinamici Campionato Calcio",
    url="http://127.0.0.1:8000/Campionato",   # project home page, if any
    classifiers=[
        'License :: OSI Approved :: Python Software Foundation License'
    ]

    # could also include long_description, download_url, etc.
)
