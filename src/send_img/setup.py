from setuptools import find_packages, setup

package_name = 'send_img'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #('share/' + package_name + '/resource', ['resource/img.png']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='umranmeryem',
    maintainer_email='umranmeryem16@gmail.com',
    description='send image',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_member = send_img.publisher_member:main',
            'subscriber_member = send_img.subscriber_member:main',
        ],
    },
)
