from oauthtwitter import OAuthApi  
  
class OauthRequest():  
    CONSUMER_KEY = "UsGVAZvCxNiZsO7eKkSZzA"  
    CONSUMER_SECRET = "M3lOLh3w9tsgEPG423EhPSkHobGHfinXR2Ju4lxkc"  
    AUTHORIZATION_URL = 'http://twitter.com/oauth/authorize'  
    REQUEST_TOKEN_URL = 'https://twitter.com/oauth/request_token'  
  
    def GetRequest(self):  
        vOauthApi = OAuthApi(self.CONSUMER_KEY, self.CONSUMER_SECRET)  
        self.mOauthRequestToken = vOauthApi.getRequestToken(self.REQUEST_TOKEN_URL)  
        self.mOauthRequestUrl = vOauthApi.getAuthorizationURL(self.mOauthRequestToken)  
