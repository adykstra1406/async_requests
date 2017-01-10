from setuptools import setup

setup(name='async_requests',
      version='1.0',
      description='A simple wrapper for non-blocking requests methods.',
      author='Alex Dykstra',
      packages=['async_requests'],
      package_dir={'async_requests': 'async_requests'},
      py_modules=['bacdb', 'bacnet'],
      package_data={'BTFEnvironment': ['bacdb/*',
                                       'bacnet/*']},
      requires=['requests'],
      zip_safe=False)