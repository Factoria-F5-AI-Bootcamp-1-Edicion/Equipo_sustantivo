import csv
from datetime import datetime as dt

comments = []
today = dt.today().strftime('%d-%m-%Y')


def process_commets(response_items, csv_output=False):

    for res in response_items:
        
        comment = {}
        comment['CommentId'] = res['snippet']['topLevelComment']['id']
        comment['VideoId'] = res['snippet']['topLevelComment']['snippet']['videoId']
        comment['CommentDate'] = res['snippet']['topLevelComment']['snippet']['publishedAt']
        comment['CommentLikes'] = res['snippet']['topLevelComment']['snippet']['likeCount']
        comment['Text'] = res['snippet']['topLevelComment']['snippet']['textOriginal']

        comments.append(comment)

        if csv_output:
            make_csv(comments)

        print(f'Finished processing {len(comments)} comments.')

    return comments

def make_csv(comments, videoID=None):
    header = comments[0].keys()

    if videoID:
        filename = f'comments_{videoID}_{today}.csv'
    else:
        filename = f'comments_{today}.csv'

    with open(filename, 'w', encoding='utf8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(comments)
