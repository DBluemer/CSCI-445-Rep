import urllib.request
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import os


########################### Read Me First ###############################
'''
------------------------------------------In DETAIL--------------------------------
This code is being borrowed from @waqasjamal, but is being updated to run in python 3, as the libraries used are 
no longer in use / updated.

To run properly, you must first 'pip install python-wordpress-xmlrpc' in your terminal


------------------------------------------In DETAIL--------------------------------		
'''


class Custom_WP_XMLRPC:
    def post_article(self, wpUrl, wpUserName, wpPassword, articleTitle, articleCategories, articleContent, articleTags,
                     PhotoUrl):
        self.path = os.getcwd() + "\\00000001.jpg"
        self.articlePhotoUrl = articlePhotoUrl
        self.wpUrl = wpUrl
        self.wpUserName = wpUserName
        self.wpPassword = wpPassword
        # Download File
        f = open(self.path, 'wb')
        f.write(urllib.request.urlopen(self.articlePhotoUrl).read())
        f.close()
        # Upload to WordPress
        client = Client(self.wpUrl, self.wpUserName, self.wpPassword)
        filename = self.path
        # prepare metadata
        data = {
            'name': 'picture.jpg',
            'type': 'image/jpg',
        }

        # read the binary file and let the XMLRPC library encode it into base64
        with open(filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
        response = client.call(media.UploadFile(data))
        attachment_id = response['id']
        # Post
        post = WordPressPost()
        post.title = articleTitle
        post.content = articleContent
        post.terms_names = {'post_tag': articleTags, 'category': articleCategories}
        post.post_status = 'publish'
        post.thumbnail = attachment_id
        post.id = client.call(posts.NewPost(post))
        print
        'Post Successfully posted. Its Id is: ', post.id


#########################################
# POST & Wp Credentials Detail #
#########################################

# Url of Image on the internet
articlePhotoUrl = 'https://media.istockphoto.com/photos/cute-blue-robot-giving-thumbs-up-3d-picture-id1350820098?b=1&k=20&m=1350820098&s=170667a&w=0&h=8gO4GcPH-wsEZS6PYn2WXbQN3ZPPv98vE6mBl-Ckwr8='
# Dont forget the /xmlrpc.php cause that's your posting address for XML Server
wpUrl = 'https://csciteam4bds.com/xmlrpc.php'
# WordPress Username
wpUserName = 'csciteam4bds'
# WordPress Password
wpPassword = '4adq Hxfs cNdo PQ3m 26dh'
# Post Title
articleTitle = 'post testing'
# Post Body/Description
articleContent = 'testing123'
# list of tags
articleTags = ['code', 'python']
# list of Categories
articleCategories = ['language', 'art']

#########################################
# Creating Class object & calling the xml rpc custom post Function
#########################################
xmlrpc_object: Custom_WP_XMLRPC = Custom_WP_XMLRPC()
# On Post submission this function will print the post id
xmlrpc_object.post_article(wpUrl, wpUserName, wpPassword, articleTitle, articleCategories, articleContent, articleTags,
                           articlePhotoUrl)
