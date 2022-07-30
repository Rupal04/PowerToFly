"""
File containing basic method and class for showing the cache implementation
"""


class CacheNameSpace(object):
    USER_LIST_PAGE_1 = ["user_list", 1800]


def get_user_list():
    return CacheNameSpace.USER_LIST_PAGE_1[0]