import urllib.request
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import xmlrpc
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import os


########################### Read Me First ###############################
'''
------------------------------------------In DETAIL--------------------------------
Description
===========
Add new posts to WordPress remotely using Python using XMLRPC library provided by the WordPress.
Installation Requirement
************************
Verify you meet the following requirements
==========================================
Install Python 2.7 (Don't download 3+, as most libraries dont yet support version 3). 
Install from PyPI using easy_install python-wordpress-xmlrpc 
Easy_Install Link: https://pypi.python.org/pypi/setuptools
==========================================
Windows Installation Guide
==========================
-Download and Install Easy_Install from above Link -Extract Downloaded File and from CMD go to the extracted directory and run 'python setup.py install'. This will install easy_install. -Go to %/python27/script and run following command easy_install python-wordpress-xmlrpc
Ubuntu Installation Guide
=========================
sudo apt-get install python-setuptools 
sudo easy_install python-wordpress-xmlrpc
Note: Script has its dummy data to work initially which you can change or integrate with your code easily for making it more dynamic.
****************************************
For Bugs/Suggestions
contact@waqasjamal.com
****************************************
------------------------------------------In DETAIL--------------------------------		
'''


class Custom_WP_XMLRPC:
    def post_article(self, wpUrl, wpUserName, wpPassword, articleTitle, articleCategories, articleContent, articleTags,
                     PhotoUrl):
        self.path = os.getcwd() + "\\00000001.jpg"
        self.articlePhotoUrl = "https://media.istockphoto.com/photos/cute-blue-robot-giving-thumbs-up-3d-picture-id1350820098?b=1&k=20&m=1350820098&s=170667a&w=0&h=8gO4GcPH-wsEZS6PYn2WXbQN3ZPPv98vE6mBl-Ckwr8='"
        self.wpUrl = "https://csciteam4bds.com/"
        self.wpUserName ="csciteam"
        self.wpPassword = "C5c!T3amF0ur"
        # Download File
        f = open(self.path, 'wb')
        f.write(urllib.request.urlopen(self.articlePhotoUrl).read())
        f.close()
        # Upload to WordPress
        client = Client(self.wpUrl, self.wpUserName, self.wpPassword)
        filename = self.path
        # prepare metadata
        data = {'name': 'picture.jpg', 'type': 'image/jpg', }

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
# Dont forget the /xmlrpc.php cause thats your posting adress for XML Server
wpUrl = 'https://csciteam4bds.com/xmlrpc.php'
# WordPress Username
wpUserName = 'csciteam'
# WordPress Password
wpPassword = 'C5c!T3amF0ur'
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
