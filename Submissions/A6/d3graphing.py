from twitter import *
import json
import time
# references https://github.com/ideoforms/python-twitter-examples#
access_token = "829763241068883968-WyE7fyJDMTqToDI8WwwnOfWsdyDvJI5"
access_token_secret = "qCGddiCfrdEVys0JPggkeV5I2AoV2tTYM1225CT0wLGWR"
consumer_key = "enM0tpExhEfj5OWqp9l6KoBh1"
consumer_secret = "mZUL70Vq8Nj0WTecsmvUXFjWACYPPQoqU4mNeBz3r9EExLUlYH"
twitter = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
#username = "phonedude_mln"
#arbitrarily chosen due to the 70 followers count they both follow the pdp
#username = "famato96"
#arbitrarily chosen due to the 54 followers count
username="CarmeTaika"
count=0
query = twitter.followers.ids(screen_name=username)
mainUserId=twitter.users.show(screen_name=username)
ids=query["ids"]
#add main user id to the id list at the beginning
ids.insert(0,mainUserId["id"])
sourceNotAppended=True
nodes= []
links=[]
#n=17
n=len(ids)
for i in range (0,n-1):
    for j in range(i+1,n):
        try:
            count=count+1
            print(count)
            result = twitter.friendships.show(source_id=ids[i],
                                         target_id=ids[j])
            source = result["relationship"]["source"]["screen_name"]
            print(source)
            follows = result["relationship"]["source"]["following"]
            target =result["relationship"]["target"]["screen_name"]
            followed_by =result["relationship"]["target"]["following"]
            if i<=0:
                if(sourceNotAppended):
                    nodes.append({"id": source})
                    sourceNotAppended=False
                nodes.append({"id": target})
            print("*--------------------------------------------------------------------*")
            print(source,"follows",target,follows)
            print(source,"followed by", target, followed_by)
            print("*---------------------------------------------------------------------*")
            if(follows):
                links.append({"source": source, "target": target})
            if(followed_by):
                links.append({"source": target, "target": source})
            time.sleep(5.08)
        except:
            continue


# create a json of screen names
print (json.dumps({"nodes": nodes, "links": links},indent=1, separators = (',', ': ')))
