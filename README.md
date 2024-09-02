# pytest-simple-report
![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/pytest-simple-report)
![PyPI](https://img.shields.io/pypi/v/pytest-simple-report)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-simple-report)

Simple html report for pytest

## 安装方法
```shell
pip install pytest-simple-report
```
## 使用方式
```python
# filename: test_pytest_simple_report.py
def test_a():
    pass
    
def test_b():
    pass
```
使用以下命令指定归属人运行，支持指定多个归属人
```shell
pytest test_pytest_simple_report.py --report=report.html
```
另外，该插件提供了额外的名为owner的Fixture函数，以共获取当前指定的owner列表。
