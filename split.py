class Split():
    def __init__(self, text):
        self.text = text

    def split_tags(self):
        result = self.text.strip(",").split(",")
        return result