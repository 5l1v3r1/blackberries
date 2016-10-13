# (c) Copyright [2016] Hewlett Packard Enterprise Development LP Licensed under
# the Apache License, Version 2.0 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of the License
# at  Unless required by applicable
# law or agreed to in writing, software distributed under the License is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

from setuptools import setup, find_packages

setup(
    name='ThreatCentral',
    author='Bart Otten',
    version='1.0',
    author_email='tc-support@hpe.com',
    description='Threat Central',
    license='Apache 2.0',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari == 1.1',
        'requests',
        'tldextract',
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
