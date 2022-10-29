from lxml import etree
import fact
import requests


class ScraperMeta(type):
    def __new__(cls, name, bases, dct):
        """
        Collect facts from a class dict
        """
        dct["_facts"] = {k: v for k, v in dct.items() if isinstance(v, fact.Fact)}
        return type.__new__(cls, name, bases, dct)

    def __call__(cls, url):
        # doc = etree.parse(url)
        # doc = lxml.html.parse(url)
        # parser = etree.HTMLParser()
        page = requests.get(url).content
        doc = etree.HTML(page)

        d = {}
        for name, afact in cls._facts.items():
            value = afact.get(doc)
            cleaner = getattr(cls, "clean_" + name, None)
            if callable(cleaner):
                value = cleaner(value)
            d[name] = value
        return d
