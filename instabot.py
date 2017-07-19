import requests
import urllib
import time


BASE_URL = "https://api.instagram.com/v1/"


calamities = ['flood', 'earthquake', 'tsunami', 'landslide', 'soil erosion', 'avalanche', 'cyclones', 'hurricane',
              'thunderstorm', 'drought']

#____________________________________________________________________________________________________________________________________________________________________
#this function print the userself information

def self_info():
    request_url = (BASE_URL + "users/self/?access_token=%s") % (APP_ACCESS_TOKEN)
    print "GET request url : %s" % (request_url)
    user_info = requests.get(request_url).json()

    if user_info["meta"]["code"] == 200:
        if len(user_info["data"]):
            print "Username: %s" % (user_info["data"]["username"])
            print "Numbers of followers: %s" % (user_info["data"]["counts"]["followed_by"])
            print "Numbers of people you are following: %s" % (user_info["data"]["counts"]["follows"])
            print "Numbers of posts: %s" % (user_info["data"]["counts"]["media"])
            time.sleep(2)
        else:
            print "User does not exist"
            time.sleep(2)
    else:
        print "Status code other than 200 received"
        time.sleep(2)



#__________________________________________________________________________________________________________________________________________________________________________
#This function fetches the information of selected user to perform further operations

def get_user_id(insta_username):
  request_url = (BASE_URL + "users/search?q=%s&access_token=%s") % (insta_username, APP_ACCESS_TOKEN)
  print "GET request url : %s" % (request_url)
  user_info = requests.get(request_url).json()
  print user_info

  if user_info["meta"]["code"] == 200:
      if len(user_info["data"]):
          return user_info["data"][0]["id"]
      else:
          return None
          time.sleep(2)
  else:
      print "Status code other than 200 received"
      time.sleep(2)




#_______________________________________________________________________________________________________________________
#this function print the information of a selected user
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print "User does not exist"
    exit()
  request_url = (BASE_URL + "users/%s?access_token=%s") % (user_id, APP_ACCESS_TOKEN)
  print "GET request url : %s" % (request_url)
  user_info = requests.get(request_url).json()

  if user_info["meta"]["code"] == 200:
    if len(user_info["data"]):
      print "Username: %s" % (user_info["data"]["username"])
      print "Number of followers: %s" % (user_info["data"]["counts"]["followed_by"])
      print "Number of people you are following: %s" % (user_info["data"]["counts"]["follows"])
      print "Number of posts: %s" % (user_info["data"]["counts"]["media"])
      time.sleep(2)
    else:
      print "There is no data for this user"
      time.sleep(2)
  else:
    print "Status code other than 200 received"
    time.sleep(2)



#_________________________________________________________________________________________________________
#this function is used to fetch the post
def get_own_post():
  request_url = (BASE_URL + "users/self/media/recent/?access_token=%s") % (APP_ACCESS_TOKEN)
  print "GET request url : %s" % (request_url)
  own_media = requests.get(request_url).json()

  if own_media["meta"]["code"] == 200:
      if len(own_media["data"]):
          image_name = own_media["data"][0]["id"] + ".jpeg"
          image_url = own_media["data"][0]["images"]["standard_resolution"]["url"]
          urllib.urlretrieve(image_url, image_name)
          print "Your image has been downloaded"
          time.sleep(2)
      else:
          print "Post does not exist"
          time.sleep(2)
  else:
      print "Status code other than 200 received!"
      time.sleep(2)



#_____________________________________________________________________________________________________________
#this function fetches the post of selected user
def get_user_post(insta_username):
      user_id = get_user_id(insta_username)
      if user_id == None:
          print "User does not exist"
          exit()
      request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s") % (user_id, APP_ACCESS_TOKEN)
      print "GET request url : %s" % (request_url)
      user_media = requests.get(request_url).json()

      if user_media["meta"]["code"] == 200:
          if len(user_media["data"]):
              image_name = user_media["data"][0]["id"] + '.jpeg'
              image_url = user_media["data"][0]["images"]["standard_resolution"]["url"]
              urllib.urlretrieve(image_url, image_name)
              print "Your image has been downloaded"
              time.sleep(2)

          else:
              print "There is no recent post"
              time.sleep(2)
      else:
          print "Status code other than 200 received"
          time.sleep(2)




#________________________________________________________________________________________________________________
#this function fetches the information of selected user to perform further operation
def get_post_id(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
            time.sleep(2)
        else:
            print 'There is no recent post of the user!'
            time.sleep(2)
    else:
        print 'Status code other than 200 received!'
        time.sleep(2)




#______________________________________________________________________________________________________________
#this function give a likes list
def get_like_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'get request url : %s' % (request_url)
    like_a_list = requests.get(request_url).json()
    print like_a_list
    if like_a_list['meta']['code'] == 200:
        likes = []
        if len(like_a_list["data"]):
            position = 1;
            for _ in like_a_list['data']:
                print "Username: %s" % (like_a_list["data"][position - 1]["username"])
                likes.append(like_a_list["data"][position - 1]["username"])
                position = position + 1
                #  print "type of user:%s " % (like_a_list["data"][0]["username"]["type"])
                # print "numbers of like:%d" %(like_a_list["data"][0]["id"])
                time.sleep(2)
        else:
            print 'there is no like'
            time.sleep(2)

    else:
        print 'Status code other than 200 received!'
        time.sleep(2)
    print 'Number of likes:' + str(position - 1)
    return likes
    time.sleep(2)




#_____________________________________________________________________________________________________________
#this function like a post selected by user
def like_a_post(insta_username):
  media_id = get_post_id(insta_username)
  request_url = (BASE_URL + 'media/%s/likes') % (media_id)
  payload = {"access_token": APP_ACCESS_TOKEN}
  print 'POST request url : %s' % (request_url)
  post_a_like = requests.post(request_url, payload).json()

  if post_a_like['meta']['code'] == 200:
      print 'Like was successful!'
      time.sleep(2)
  else:
      print 'Your like was unsuccessful. Try again!'
      time.sleep(2)


#_____________________________________________________________________________________
#this function delete a post selected by a user
def delete_a_like(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes/?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    print 'DEL request url : %s' % (request_url)
    delete_like = requests.delete(request_url).json()
    like_list = get_like_list(insta_username)
    if 'cutiepie8640' in like_list:
        if delete_like['meta']['code'] == 200:
            print 'successful delete like on post'
            time.sleep(2)
        else:
            print ' unsuccessful delete like on post. Try again!'
            time.sleep(2)
    else:
        print "like is not present"
        time.sleep(2)


#________________________________________________________________________________________
#this function show a list of comments
def get_comment_list(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s ') % (media_id,APP_ACCESS_TOKEN)
    print 'get request url : %s' % (request_url)
    comment_a_list = requests.get(request_url).json()

    if comment_a_list['meta']['code'] == 200:
        if len(comment_a_list["data"]):
            position = 1;
            for _ in comment_a_list['data']:
                print "Username: %s" % (comment_a_list["data"][position - 1]["from"]["username"])
                print "comment: %s" %(comment_a_list["data"][position-1]["text"])
                position = position + 1
                time.sleep(2)
        else:
            print 'there is no like'
            time.sleep(2)
    else:
        print 'Status code other than 200 received!'
        time.sleep(2)
    print 'Number of comments:' + str(position - 1)



#_________________________________________________________________________________________
#this function comment on a post selected by user
def post_a_comment(insta_username):
  media_id = get_post_id(insta_username)
  comment_text = raw_input("Your comment: ")
  payload = {"access_token": APP_ACCESS_TOKEN, "text" : comment_text}
  request_url = (BASE_URL + 'media/%s/comments') % (media_id)
  print 'POST request url : %s' % (request_url)
  make_comment = requests.post(request_url, payload).json()

  if make_comment['meta']['code'] == 200:
    print "Successfully added a new comment!"
    time.sleep(2)
  else:
    print "Unable to add comment. Try again!"
    time.sleep(2)
#_______________________________________________________________________________________
#this function delete a comment on a post selected by a user
def delete_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment_text = raw_input("Your comment: ")
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
    a = requests.get(request_url).json()
    b = a['data']
    comment_list = []

    for i in range(len(b)):
        split = b[i]['text'].split()

        if comment_text in split:
            comment_list.append(b[i]['id'])

    if len(comment_list):
        for i in comment_list:
            requests_url2 = (BASE_URL + 'media/%s/comments/%s?access_token=%s' % (media_id, i, APP_ACCESS_TOKEN))
            response = requests.delete(requests_url2).json()
        print str(len(comment_list)) + " Comment successfully deleted !"
        time.sleep(2)

    else:
        print "comment is not found"
        print "comment is not deleted"
        time.sleep(2)


#________________________________________________________________________________________________________
#this function show natural calamities
def get_natural_calamities(lat,lng):
    request_url = (BASE_URL + 'media/search?lat=%s&lng=%s&distance=500&access_token=%s') % (lat, lng, APP_ACCESS_TOKEN)
    print 'GET reques url: %s' % (request_url)
    user_location = requests.get(request_url).json()
    print user_location
    if user_location['meta']['code'] == 200:
        if len(user_location['data']):
            image=user_location['data'][0]['images']['standard_resolution']['url']
            print image
            for temp in calamities:
                if user_location['data'][0]['tags']==temp:
                 print user_location['data'][0]['tags']
                 print user_location['data'][0]['location']
            print 'Tags are:%s' % (user_location['data'][0]['tags'])
            print 'Location is:%s' % (user_location['data'][0]['location'])
            print '%s is going on at %s' %(user_location['data'][0]['tags'],user_location['data'][0]['location'])
            time.sleep(2)
        else:
            print'media not found'
            time.sleep(2)
    else:
        print 'Status code other than 200 received'
        time.sleep(2)



#_________________________________________________________________________________________________
#this function show the menu
def start_bot():
    while True:
        print '\n'
        print "Hello! Welcome to instaBot"
        print "Here are your menu options:"
        print "a.Get your own details\n"
        print "b.Get details of a user by username\n"
        print "c.Get your own recent post\n"
        print "d.Get the recent post of a user by username\n"
        print "e.Get like a list\n"
        print "f.like a post\n"
        print "g.delete a like on post\n"
        print "h.list of comments\n"
        print "i.comment on post\n"
        print "j.delete comment\n"
        print "k.Get Information about NATURAL CALAMITIES"
        print "l.exit\n"
        choice = raw_input("Enter you choice: ")
        if choice == "a":
            self_info()
        elif choice == "b":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_id(insta_username)
        elif choice == "c":
            get_own_post()
        elif choice == "d":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "e":
            insta_username = raw_input("Enter the username of the user: ")
            get_like_list(insta_username)
        elif choice == "f":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == "g":
            insta_username = raw_input("Enter username of user:")
            delete_a_like(insta_username)
        elif choice == "h":
            insta_username = raw_input("Enter the username of the user: ")
            get_comment_list(insta_username)
        elif choice == "i":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice == "j":
            insta_username= raw_input("Enter the username of the user")
            delete_a_comment(insta_username)
        elif choice == "k":
            try:
                lat = float(raw_input("Enter the latitude:"))
                lng = float(raw_input("Enter the longitude"))
            except ValueError:
                print "Error"
                exit()
            get_natural_calamities(lat, lng)
        elif choice == "l":
            exit()
        else:
            print "wrong choice"

start_bot()
#____________________________________________________________________________________________
 #end of code
