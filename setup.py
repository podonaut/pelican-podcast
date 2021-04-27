from setuptools import setup
from setuptools import find_packages

version = __import__('pelican_podcast').__version__
download_url = 'https://github.com/podonaut/pelican-podcast/archive/{}.zip'.format(version)

setup(name='pelican_podcast',
      version=version,
      url='https://github.com/podonaut/pelican-podcast',
      download_url=download_url,
      author="Magnun Leno",
      maintainer="Douglas Kastle",
      maintainer_email="douglas.kastle@gmail.com",
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
