from setuptools import find_packages, setup

package_name = 'my_test_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    install_requires=['setuptools'],
    tests_require=['pytest'],  
    test_suite='tests',        
    zip_safe=True,
    maintainer='umranmeryem',
    maintainer_email='umranmeryem16@gmail.com',
    description='A sample package to demonstrate ROS2 Python testing',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [

        ],
    },
)
