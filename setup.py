from setuptools import setup


def readme():
    with open('README') as f:
        return f.read()

def requirements():
    with open('requirements.txt') as req:
        return req.read()


setup(name='pyRigolDP832',
      version='0.0.3',
      description='Controls instrument and logs data',
      long_description=readme(),
      url='None',
      author='Hunter Abraham',
      author_email='hjabraham@wisc.edu',
      license='MIT',
      packages=['pyRigolDP832'],
      install_requires=[],
      zip_safe=False,
      )