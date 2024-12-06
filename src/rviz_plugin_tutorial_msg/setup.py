from setuptools import setup

package_name = 'rviz_plugin_tutorial_msg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    author_email='your.email@example.com',
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='RViz plugin tutorial with custom message',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
