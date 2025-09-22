from setuptools import setup, find_packages
setup(
    name = 'pipe1__Reformat_1',
    version = '1.0',
    packages = find_packages(include = ('git_sql_pyspark_test/pipelines/pipe1_jobs/pipe1__Reformat_1*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'pipe1__Reformat_1',
    install_requires = ['pyhocon==3.0.5', 'prophecy-libs==1.8.9'],
    entry_points = {
'console_scripts' : [
'main = git_sql_pyspark_test/pipelines/pipe1_jobs/pipe1__Reformat_1.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
