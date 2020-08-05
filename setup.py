import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'pyolxbrazil',
  packages = ['pyolxbrazil'],
  version = '1.0.2',
  license='MIT',
  description = 'Scrapper for OLX Brazil',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Luís Eduardo Pompeu',
  author_email = 'luiseduardobr1@hotmail.com',
  url = 'https://github.com/luiseduardobr1/pyolxbrazil',
  download_url = 'https://github.com/luiseduardobr1/pyolxbrazil/archive/v_102.tar.gz',
  keywords = ['Scrapper', 'OLX', 'Brazil', 'Portuguese'],
  install_requires=[
          'requests',
          'beautifulsoup4',
          'fake-useragent'
      ],
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)