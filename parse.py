#!/usr/bin/env python 
import json

header= "Name,Given Name,Family Name,Website 1 - Type,Website 1 - Value"

template = "%(name)s,%(first)s,%(last)s,Profile,http://www.google.com/%(profileid)s"

following_json = open("following.json")
friends = json.load(following_json)

#print friends
print header

for friend in friends["friends"]:
  #print json.dumps(friend)
  print template %{'name':friend['displayName'],
                   'first':friend['givenName'],
                   'last':friend['displayName'].split(friend['givenName'])[1].lstrip(),
                   'email':'',
                   'profileid':friend['profileIds'][0] if 'profileIds' in friend else '0'
                   } 

