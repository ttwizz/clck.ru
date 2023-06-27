from setuptools import setup, find_packages

def README():
    with open("README.md", "r") as file:
        return file.read()

setup(
    name = "clck.ru",
    version = "1.0.0",
    author = "ttwiz_z",
    author_email = "moderkascriptsltd@gmail.com",
    description = "Shortens links and protects their contents.",
    long_description = README(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/ttwizz/clck.ru",
    packages = find_packages(),
    install_requires = ["requests>=2.31.0"],
    classifiers = [
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords = "clck.ru",
    project_urls = {
        "Author" : "https://github.com/ttwizz",
        "Organization" : "https://github.com/ModerkaScripts"
    },
    python_requires = ">=3.8"
)