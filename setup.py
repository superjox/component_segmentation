from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='Schematize',
    version='0.1',
    description='Visualization of Graph Genomes.',
    author='Josiah Seaman, Simon Heumos, Torsten Pook, Toshiyuki Yokoyama, Joerg Hagmann, Ted Gibbons, Christian Kubica',
    author_email='josiah@newline.us',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=('data')),
    include_package_data=True,
    package_data={'matrixcomponent': ['data/*',]},
    scripts=['matrixcomponent/segmentation.py'],
    install_requires=[
        'rdflib==4.2.2',
        'nested-dict==1.61',
        'numpy==1.17.2',
        'scipy==1.3.1',
        'dataclasses==0.7',
    ],
    # extras_require = {'optimized_alignment': ['blist>=1.3.6']}, #for optional packages
    dependency_links=[],
    zip_safe=False,
    url='https://github.com/graph-genome/component_segmentation',
    download_url='https://github.com/graph-genome/component_segmentation',  # TODO: post a tarball
    keywords=['graph genome', 'bioinformatics', 'dna', 'fasta', 'alignment', 'species diversity'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)