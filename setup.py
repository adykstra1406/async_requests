from setuptools import setup

setup(name='async_requests',
      version='1.0',
      description='A simple wrapper for non-blocking requests methods.',
      author='Alex Dykstra',
      packages=['async_requests'],
      package_dir={'async_requests': 'async_requests'},
      install_requires=['requests==2.12.4',],
      zip_safe=False)