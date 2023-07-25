from setuptools import find_packages, setup
setup(
    name='learning_conf',
    packages=find_packages(include=['learning_conf']),
    version='0.1.0',
    description='A library to record and plot learning confidence levels',
    author='Joe Tang',
    license='MIT',
    install_requires=['plotly'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'
)