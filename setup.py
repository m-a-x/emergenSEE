from distutils.core import setup
setup(
  name = 'emergenSEE',
  packages = ['emergenSEE'], # this must be the same as the name above
  version = '0.1',
  description = 'Visualize NYC EMS Emergencies',
  author = 'Max Mattioli',
  author_email = 'm.max@columbia.edu',
  url = 'https://github.com/m-a-x/emergenSEE', # use the URL to the github repo
  license='MIT',
  classifiers = [
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        "Topic :: Software Development :: Libraries :: Python Modules"
  ],
  install_requires=['imageio==1.6',
                    'pandas',
                    'numpy',
                    'matplotlib',
                    'descartes',
                    'shapely',
                    'scikit-learn',
                      ]
)