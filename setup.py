#from distutils.core import setup
#setup(name='TutoringExamples',
#      version='1.0',
#      packages=['matrices'],
#      intall_requires=['numpy'],
#      )

from setuptools import setup

setup(name='TutoringExamples',
      version='0.1',
      description='Tutoring Problems',
      url='http://github.com/dfmartin43/tutor',
      license='MIT',
      packages=['matrices','unknown_functions'],
      zip_safe=False,
      install_requires=['numpy']
      )
