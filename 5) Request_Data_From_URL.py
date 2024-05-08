import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
issues = requests.get(url).json()

for issue in issues:
    user = issue.get('user', {}).get('login')
    print(f"User: {user}")
    followers_url = issue.get('user', {}).get('followers_url')
    if followers_url:
        for follower in requests.get(followers_url).json():
            follower_login = follower.get('login')
            print(f"  Follower: {follower_login}")
            subscriptions_url = follower.get('subscriptions_url')
            print(f"    Length of subscriptions_url: {len(subscriptions_url)}" if subscriptions_url else "    Follower does not have subscriptions_url")
    else:
        print("User does not have followers")
