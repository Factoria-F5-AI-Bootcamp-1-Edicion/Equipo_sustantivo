# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from utils.comments import process_commets, make_csv

load_dotenv()
API_KEY = os.getenv("API_KEY") # Hay que meter la key de la pai de youtube en el .env

youtube = build(
    "youtube", "v3", developerKey = API_KEY)

def commet_threads(videoID, to_csv=True):

    comments_list = []

    request = youtube.commentThreads().list(
        part="id,replies,snippet",
        videoId=videoID,
        moderationStatus="published",
        maxResults=100
    )
    response = request.execute()
    comments_list.extend(process_commets(response['items']))

    while response.get('nextPageToken', None):
        request = youtube.commentThreads().list(
            part="id,replies,snippet",
            videoId=videoID,
            moderationStatus="published",
            maxResults=100,
            pageToken=response['nextPageToken']
        )
        response = request.execute()
        comments_list.clear()
        comments_list.extend(process_commets(response['items']))
    
    print(f'Finished fetching commets for {videoID}, {len(comments_list)} comments found.')

    if to_csv:
        make_csv(comments_list, videoID)

    return comments_list


def main():
    commet_threads("5vF4si3hoRA", to_csv=True)

if __name__ == "__main__":
    main()
