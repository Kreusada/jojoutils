import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="jojoutils",
    version="1.0.1.Dev",
    author="Jojo",
    description="Tools for Jojo's cogs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Just-Jojo/jojoutils",
    packages=setuptools.find_packages(),
    python_requires=">=3.8.1",
)
