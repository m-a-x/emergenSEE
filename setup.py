from distutils.core import setup

setup(
  name = 'emergenSEE',
  packages = ['emergenSEE'], # this must be the same as the name above
  version = '0.1',
  description = 'Visualize NYC EMS Emergencies',
  author = 'Max Mattioli',
  author_email = 'm.max@columbia.edu',
  url = 'https://github.com/m-a-x/emergenSEE', # use the URL to the github repo
  download_url = 'https://github.com/m-a-x/emergenSEE/tarball/0.1',
  license='MIT',
  classifiers = [],
  install_requires=['imageio==1.6',
                    'pandas',
                    'numpy',
                    'matplotlib',
                    'descartes',
                    'shapely',
                    'scikit-learn',
                      ]
)
