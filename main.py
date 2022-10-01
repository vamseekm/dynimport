import importlib.util
import sys
spec = importlib.util.spec_from_file_location("hello.mylib", "./mylib.py")
foo = importlib.util.module_from_spec(spec)
sys.modules["hello.mylib"] = foo
spec.loader.exec_module(foo)
foo.hello()
heck = foo.World()
heck.heck()
