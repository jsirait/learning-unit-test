from split import Split

class TestSplit(object):
    def test_single_no_comma(self):
        subject = Split("java")
        result = subject.split_tags()
        assert result == ["java"]

    def test_preceding_comma(self):
        subject = Split(",java")
        result = subject.split_tags()
        assert result == ["java"]
    

