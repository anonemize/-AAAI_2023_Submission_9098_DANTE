from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='splitPopulationSurvivalExploits',
      version='0.1',
      description="Package for Stochastic Point Process Information Extractor.\
                    Contains all the base classes for definining any point process along with accompanying features",
      long_description=long_description,
      author="anon",
      author_email="anon",
      packages=['',
                'core',
                'utils',
                'point_processes'],
      url="https://github.com/anonemize/AAAI_2023_Submission_9098_DANTE.git",
      package_dir={'': 'splitPopulationSurvivalExploits/src'},
      python_requires='>=3.6')
