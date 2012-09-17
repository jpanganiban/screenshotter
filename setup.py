from setuptools import setup


def install_requires():
    with open('requirements') as f:
        install_requires = f.readlines()
    return install_requires


setup(name="screenshooter",
      package_dir={'': 'src'},
      install_requires=install_requires())
