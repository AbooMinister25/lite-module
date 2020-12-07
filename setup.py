from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
      long_description = f.read()

setup(name='lite-module',
      version='0.0.2',
      description='Python package for creating Lite modules',
      long_description = long_description,
      long_description_content_type="text/markdown",
      author='Rayyan Cyclegar',
      author_email='aboominister@gmail.com',
      license='MIT',
      packages=['lite'],
      zip_safe=False,
      url="https://github.com/AbooMinister25/lite-module"
)