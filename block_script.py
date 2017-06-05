#need lib for download info from internet
import urllib2

#some blocklists
sites = [
    'http://www.mvps.org/winhelp2002/hosts.txt',
    'https://adaway.org/hosts.txt',
    'http://www.malwaredomainlist.com/hostslist/hosts.txt',
    'http://hosts-file.net/.\ad_servers.txt'
    ]

#function download all url in file /tmp/block_all
def get_lists(blocklists):
    attempts = 0
    while attempts < 3:
        try:
            for url in blocklists:
                response = urllib2.urlopen(url, timeout = 5)
                content = response.read()
                f = open( "/tmp/block_all", 'w' )
                f.write( content )
                f.close()
                break
        except urllib2.URLError as e:
            attempts += 1
            print type(e)

#function parsing
#def parse():

