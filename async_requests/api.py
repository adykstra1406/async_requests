from multiprocessing.pool import ThreadPool
import requests


def request(method, url, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.request, (method, url), **kwargs)


def get(url, params=None, **kwargs):
    pool = ThreadPool(processes=1)
    return result = pool.apply_async(requests.get, (url, params), **kwargs)


def head(url, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.head, (url,), **kwargs)


def post(url, data=None, json=None, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.post, (url, data, json), **kwargs)


def patch(url, data=None, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.patch, (url, data), **kwargs)


def put(url, data=None, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.put, (url, data), **kwargs)


def delete(url, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.delete, (url,), **kwargs)


def options(url, **kwargs):
    pool = ThreadPool(processes=1)
    return pool.apply_async(requests.options, (url,), **kwargs)
