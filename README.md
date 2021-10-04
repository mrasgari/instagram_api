instagram python api
-------------------------------------------------------------------------
a simple api to get some information from instagram such as account detail

## how to use

first you need to set cookies from instagram account 
login in instagram in your browser
[instagram](https://www.instagram.com/,'instagram')
then complete config.txt with your information from cookies in instagram site

## example

```
import instagram

account_data=instagram.UserAccount('rambodjavan1')
name=account_data['graphql']['user']['full_name']
```
