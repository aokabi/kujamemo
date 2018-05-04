import twitter
from datetime import datetime

api = twitter.Api(
        consumer_key="",
        consumer_secret="",
        access_token_key="",
        access_token_secret="")

memo = "#くじゃメモ"
keyword = "@aokabit メモ"
recentmemo = ""

status = api.GetUser(screen_name="kujak58")

fils = api.GetStreamFilter(follow=str(status.id), track=[memo, keyword])

print("hoge\n" + str(datetime.now()))

for fil in fils:
    print(fil['text'])
    if fil['text'].count(memo):
        recentmemo = fil['text']
        print(fil['text'])
    elif fil['text'].count(keyword):
        print(recentmemo)
        api.PostUpdates(recentmemo + "\n" + str(datetime.now()))

