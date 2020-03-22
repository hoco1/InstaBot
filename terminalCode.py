from mainCode import *
from tabulate import tabulate
from docopt import docopt

 
usage = """
Name.
Instagram Bot and No PrivatePage Licence MohammadReza Norouzi 

Usage:
 terminalCode.py --signIn <userName> <passWord> [<msg>]
 terminalCode.py --follow  <listUserName>
 terminalCode.py --unfollow <listUserName>
 terminalCode.py --likeTagPhoto <listHashTag>
 terminalCode.py --likeUserPhoto <listUserName>
 terminalCode.py --member 
 terminalCode.py --report   <listUserName>
 terminalCode.py --block   <listUserName>
 terminalCode.py --followback <userName>
 terminalCode.py --follower <userName>
 terminalCode.py --following <userName>
 terminalCode.py --seenStory <listUserName>
 

Options:
  --countdown  display a count down
"""


args = docopt(usage)


if args['--signIn']:
    addUser(args['<userName>'],args['<passWord>'],args['<msg>'])
    print('Sign In Successfully')

if args['--follow']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn
    listUser = args['<listUserName>'].rsplit(sep=',')
    print(listUser)
    for user in listUser:
        ig.follow(user)
    ig.closeBrowser()
    print('Follow users Successfully')

if args['--unfollow']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn
    listUser = args['<listUserName>'].rsplit(sep=',')
    print(listUser)
    try:
        for user in listUser:
            ig.unFollow(user)
        ig.closeBrowser()
    except Exception:
        print('Error')
    print('UnFollow users Successfully')

if args['--block']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn
    listUser = args['<listUserName>'].rsplit(sep=',')
    print(listUser)

    try: 
        for user in listUser:
            ig.blockUser(user)
        ig.closeBrowser()
    except Exception:
        print('Error')
    print('Block users Successfully')


if args['--likeTagPhoto']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn
    listTag = args['<listHashTag>'].rsplit(sep=',')
    print(listTag)

    try:
        for tag in listTag:
            print(tag)
            ig.likeTagPhoto(tag)
        ig.closeBrowser()
    except Exception:
        sleep(5)
        ig.closeBrowser()
    print('Like Tags successfully')

if args['--likeUserPhoto']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('Password : ',password)
    ig = instabot(username,password)
    ig.SignIn
    listUser = args['<listUserName>'].rsplit(sep=',')
    print(listUser)
    try:
        for user in listUser:
            print(user)
            ig.likeUserPhoto(user)
        ig.closeBrowser()
    except Exception:
        sleep(5)
        ig.closeBrowser()
    print('Like Users Successfully')

if args['--member']:
    member , count = show()
    print(tabulate(member))
    print('Count : ',count)

if args['--follower']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn

    user = args['<userName>']

    listFollower = ig.getUserFollowers(user)
    print(listFollower)
    ig.closeBrowser()
    print('List Followers Successfully')

if args['--following']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn

    user = args['<userName>']

    listFollowing = ig.getUserFollowing(user)
    print(listFollowing)
    ig.closeBrowser()
    print('List Following Successfully')

if args['--followback']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn

    user = args['<userName>']

    listFollowing = ig.getUserFollowing(user)
    listFollower = ig.getUserFollowers(user)

    sleep(3)
    listFollowBack = []

    print('Followers : #1 ',listFollower)
    print('Following : #1 ',listFollowing)

    for follower in listFollower:
        for following in listFollowing:
            if follower == following:
                listFollowBack.append(follower)
                listFollowing.remove(following)
                listFollower.remove(follower)
        
    print('Followers : #2',listFollower)
    print('Following : #2',listFollowing)
    print('Follow Backe : ',listFollowBack)
    ig.closeBrowser()
    print('List FollowBack Successfully')

if args['--seenStory']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn
    listUser = args['<listUserName>'].rsplit(sep=',')
    print(listUser)

    for user in listUser:
        ig.seenStroy(user)
    
    ig.closeBrowser()
    print('Seen Story Successfully')

if args['--report']:
    username , password = lastJoin()
    print('UserName : ',username)
    print('PassWord : ',password)

    ig = instabot(username,password)
    ig.SignIn
    listUser = args['<listUserName>'].rsplit(sep=',')

    for user in listUser:
        ig.reportUser(user)
    
    ig.closeBrowser()
    print('Report Successfully')

    



    

