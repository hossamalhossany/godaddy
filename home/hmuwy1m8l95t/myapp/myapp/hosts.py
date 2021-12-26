
from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'myapp.hostsconf.urls', name='wildcard'),
)












# from django_hosts import patterns, host
# from django.conf import settings
#
# host_patterns = patterns('',
#                             host(r'www', settings.ROOT_URLCONF, name='www'),
#                             host(r'', 'myapp.urls', name=' '),
#                             host(r'myapp', 'myapp.myapp_urls', name='myapp'),
#                          )
#
#
