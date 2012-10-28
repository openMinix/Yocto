import twitter  
from oauthtwitter import OAuthApi  
  
class OauthAccess():  
  
    CONSUMER_KEY = "UsGVAZvCxNiZsO7eKkSZzA"  
    CONSUMER_SECRET = "M3lOLh3w9tsgEPG423EhPSkHobGHfinXR2Ju4lxkc"  
    ACCESS_TOKEN_URL = 'https://twitter.com/oauth/access_token'  
  
    mPin = ""  
    mOauthRequestToken = ""  
    mOauthAccessToken = ""  
    mUser = twitter.User  
    mTwitterApi = ""  
  
    def __init__(self, pOauthRequestToken, pPin):  
        self.mOauthRequestToken = pOauthRequestToken  
        self.mPin = pPin  
  
    def getOauthAccess(self):  
        self.mTwitterApi = OAuthApi(self.CONSUMER_KEY, self.CONSUMER_SECRET, self.mOauthRequestToken)  
        self.mOauthAccessToken = self.mTwitterApi.getAccessToken(self.mPin)  
        self.mAuthenticatedTwitterInstance = OAuthApi(self.CONSUMER_KEY, self.CONSUMER_SECRET, self.mOauthAccessToken)  
        self.mUser = self.mAuthenticatedTwitterInstance.GetUserInfo() 

