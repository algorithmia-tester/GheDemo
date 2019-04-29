from . import GheDemo

def test_GheDemo():
    assert GheDemo.apply("Jane") == "hello Jane"
