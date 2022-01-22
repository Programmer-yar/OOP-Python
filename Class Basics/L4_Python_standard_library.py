from collections import OrderedDict

""" - OrderedDict: A class which orders the
      key:value pairs in the arrangement they were added """

fav_lan=OrderedDict()

fav_lan['ahmad'] = 'python'
fav_lan['happy'] = None

for name , language in fav_lan.items():
    print(name.title(), 'favourite language is', language.title())
