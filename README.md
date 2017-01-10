# async_requests
A simple wrapper around requests to make calls asynchronous. 


# Usage
    >>> async_r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    >>> r = async_r.get()  # This will then block so add time before to prevent blocking
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    u'{"type":"User"...'
    >>> r.json()
    {u'disk_usage': 368627, u'private_gists': 484, ...}