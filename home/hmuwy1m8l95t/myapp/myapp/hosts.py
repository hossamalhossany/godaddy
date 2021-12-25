from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
                            host(r'www', settings.ROOT_URLCONF, name='www'),
                            host(r'', 'myapp.urls', name=' '),
                            host(r'myapp', 'myapp.myapp_urls', name='myapp'),
                         )



#
# host_patterns = patterns('',
#                          host(r'www', 'subdomains_tutorial.frontend_urls', name='www')
#                          ,host(r'admin', settings.ROOT_URLCONF, name='admin'),
#                          host(r'api', 'subdomains_tutorial.api_urls', name='api'),)
