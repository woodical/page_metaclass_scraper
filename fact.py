class Fact:
    def __init__(self, xpath):
        self.xpath = xpath

    def get(self, doc):
        return doc.xpath(self.xpath, current=doc)


class StringFact(Fact):
    def __init__(self, xpath):
        super().__init__(xpath)

    def get(self, doc):
        return "".join(p.text for p in super().get(doc))
