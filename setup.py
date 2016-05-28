from setuptools import setup

setup(name='pycon-tutorial-tbates',
      version='1.0',
      description='Test stuff for pycon project tutorial',
      py_modules=['wordcount_lib'],
      scripts=['wordcount'],
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
)

