__author__ = 'Mac'

def smart_print(obj):
    print repr(obj).decode('unicode-escape').encode('latin-1')
