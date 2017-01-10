from multiprocessing.pool import ThreadPool
import requests


def request(method, url, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.request, (method, url), **kwargs)
    return result.get()


def get(url, params=None, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.get, (url, params), **kwargs)
    return result.get()


def head(url, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.head, (url,), **kwargs)
    return result.get()


def post(url, data=None, json=None, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.post, (url, data, json), **kwargs)
    return result.get()


def patch(url, data=None, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.patch, (url, data), **kwargs)
    return result.get()


def put(url, data=None, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.put, (url, data), **kwargs)
    return result.get()


def delete(url, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.delete, (url,), **kwargs)
    return result.get()


def options(url, **kwargs):
    pool = ThreadPool(processes=1)
    result = pool.apply_async(requests.options, (url,), **kwargs)
    return result.get()
