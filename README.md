# GoonAuth #

goonauth is the code behind https://goonauth.cattes.us/. goonauth tries the solve the issue of somethingawful community websites verifying member status of new users on the SA forums by creating an easy to use OAuth2 based api that enables developers to look up registered goons and pull down information filled out by them for various outside services (such as steam and league of legends). 

## Registering an OAuth Application ##
To register an application create a new account at https://goonauth.cattes.us/ and log in. Click create new oauth application and fill in the fields with the proper information.

### API URLS ###
Access Token URL: https://goonauth.cattes.us/o/token/  
Authorize URL: https://goonauth.cattes.us/o/authorize/  
Get Current Authorized Accounts Profile: https://goonauth.cattes.us/api/user/  
  
NOTE: the above api method requires an authorized token to work. See the example app for an example. If the user isnt currently a verified goon this api method will return an empty JSON string (hopefully!)  
