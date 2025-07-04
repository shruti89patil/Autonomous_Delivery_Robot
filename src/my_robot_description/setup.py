from setuptools import setup

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # ('share/' + package_name + '/launch', ['launch/robot_launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/my_robot.urdf.xacro']),
        ('share/' + package_name + '/launch', ['launch/robot_launch.py', 'launch/slam_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shruti',
    maintainer_email='shruti@todo.todo',
    description='URDF and launch files for autonomous delivery robot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
