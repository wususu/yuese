import hashlib


def md5(strs):
    m = hashlib.md5()
    m.update(strs.encode('utf8'))
    return m.hexdigest()