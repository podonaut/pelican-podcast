from setuptools import setup
from setuptools import find_packages

version = __import__('pelican_podcast_feed').__version__
download_url = 'https://github.com/magnunleno/pelican-podcast-feed/archive/{}.zip'.format(version)

setup(name='pelican_podcast_feed',
      version=version,
      url='https://github.com/magnunleno/pelican-podcast-feed',
      download_url=download_url,
      author="Magnun Leno",
      maintainer="John Mercouris",
      maintainer_email="john@mercouris.email",
      description="This plugins adds a feed generator and feed writer for your podcast.",
      long_description=open("README.rst").read(),
      license='GPLV3',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      package_data={'': ['LICENSE', ]},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GPL V3',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing',
      ],
      zip_safe=True,
      )
