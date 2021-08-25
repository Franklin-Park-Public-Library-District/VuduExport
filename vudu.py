# Don't judge me I wrote this quickly.

# Create a file credentials.txt and put your email on the first line, and your password on the second.
# You may have to replace the @ in your email with %40, ie, foo@gmail.com would be foo%40gmail.com

import csv
import json
import requests

BASE_URL = 'https://api.vudu.com/api2/'

LOGIN_DATA = 'claimedAppId=myvudu&format=application/json&_type=sessionKeyRequest&followup=user&password=%s&userName=%s&weakSeconds=25920000&sensorData=sensorData'

LIST_DATA = 'claimedAppId=myvudu&format=application/json&_type=contentSearch&count=100&dimensionality=any&followup=ratingsSummaries&followup=totalCount&listType=%s&sessionKey=%s&sortBy=title&superType=movies&type=program&type=bundle&userId=%s&offset=%s'

LIST_TYPE_OWNED = ('rentedOrOwned', 'owned.csv')
LIST_TYPE_WANTED = ('wished', 'wanted.csv')

LIST_TYPES = [LIST_TYPE_OWNED, LIST_TYPE_WANTED]

def main():
    with open('credentials.txt', 'r') as creds:
        username = creds.readline().rstrip()
        password = creds.readline().rstrip()
    response = ApiRequest(LOGIN_DATA % (password, username))
    session_key = response['sessionKey'][0]['sessionKey'][0]
    user_id = response['sessionKey'][0]['userId'][0]

    for list_type, filename in LIST_TYPES:
        with open(filename, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Quality', 'Movie ID', 'Rating', 'Tomato Meter', 'Length', 'Poster URL', 'Release Date', 'Description'])
            there_are_more = True
            offset = 0
            while there_are_more:
                list_string = LIST_DATA % (list_type, session_key, user_id, offset)
                response = ApiRequest(list_string)
                # PrettyJson(response)
                for movie in response['content']:
                    mov_title = GetString(movie, 'title').encode('utf-8')
                    mov_quality = GetString(movie, 'bestDashVideoQuality')
                    mov_id = GetString(movie, 'contentId')
                    mov_rating = GetString(movie, 'mpaaRating')
                    mov_description = GetString(movie, 'description').encode('utf-8')
                    mov_length = GetString(movie, 'lengthSeconds')
                    mov_poster = GetString(movie, 'posterUrl')
                    mov_release_date = GetString(movie, 'releaseTime')
                    mov_tomato = GetString(movie, 'tomatoMeter')
                    mov_all = [mov_title, mov_quality, mov_id, mov_rating, mov_tomato, mov_length, mov_poster, mov_release_date, mov_description]
                    writer.writerow(mov_all)
                offset += 100
                there_are_more = response['moreBelow'][0] == 'true'


def GetString(json_obj, name):
    if not name in json_obj:
        return ''
    return json_obj[name][0]


def PrettyJson(json_obj):
  print json.dumps(json_obj, sort_keys=True, indent=4)


def ApiRequest(request):
  req = requests.get(BASE_URL, request)
  return json.loads(StripCruft(req.text))


def StripCruft(resp):
  prefix = '/*-secure-'
  suffix = '*/'
  start = resp.find(prefix)
  end = resp.rfind(suffix)
  return resp[start + len(prefix):end]


if __name__ == '__main__':
    main()