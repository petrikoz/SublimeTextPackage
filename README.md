# SublimeTextPackage

My own package for Sublime Text 3 with few little utilities.

## Install

```shell

cd ~/.config/sublime-text-3/Packages
git clone https://github.com/petrikoz/SublimeTextPackage.git
```

## CopyFileName

Allow copy name of active file. Like built-in command 'Copy File Path', but copy only last part. Ex.: from `path/to/file.ext` will copy `file.ext`.
Can do it with context menu in file / tab / side bar.

## SuperPython

Adds tab-completion to Python's somewhat verbose super() construct. Just hit tab after a super keyword and a snippet will be inserted contained the likely current class and method name, with the existing arguments already filled.


```python

def function(arg, kwarg=None):
    # input `super` → press 'Tab':
    super().function(arg, kwarg=kwarg)


def function1(*args, **kwargs):
    # input `super` → press 'Tab':
    super().function1(*args, **kwargs)


def function2(foo, *args,
              bar='baz', **kwargs):
    # input `super` → press 'Tab':
    super().function2(foo, *args, bar=bar, **kwargs)


def function3():
    # input `super` → press 'Tab':
    super().function3()


class ClassName(object):
    """docstring for ClassName"""

    def method(self, arg, kwarg=None):
        # input `super` → press 'Tab':
        super().method(arg, kwarg=kwarg)

    def method1(self, *args, **kwargs):
        # input `super` → press 'Tab':
        super().method1(*args, **kwargs)

    def method2(self, foo, *args,
                bar='baz', **kwargs):
        # input `super` → press 'Tab':
        super().method2(foo, *args, bar=bar, **kwargs)

    @staticmethod
    def method3(*args, **kwargs):
        # input `super` → press 'Tab':
        super().method3(*args, **kwargs)

    @classmethod
    def method4(cls, *args, **kwargs):
        # input `super` → press 'Tab':
        super().method4(*args, **kwargs)
```
