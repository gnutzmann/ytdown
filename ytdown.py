# *** ytdown ***
# Script to download youtube videos
# Created by Diogo Gnutzmann Santos
# email: gnutzmann@gmail.com

# -*- coding: utf-8 -*-
import pytube as pyt
import sys
import validators as val

ERROR_MSG_INVALID_PARAM = 'Invalid param. Try ' + sys.argv[0] + ' -h'
WARNING_MSG_DOWNLOAD_START = 'Download started!'
WARNING_MSG_DOWNLOAD_END = 'Download finished!'


def verify_param(param_list):
    return len(param_list) > 0 and param_list[0] in ['-u', '-h']


def download_video(url):
    yt = pyt.YouTube(url)
    videos = yt.streams.first()
    videos.download()


def options(param_list):
    if len(param_list) >= 1:
        if param_list[0] == '-u' and (len(param_list) == 2):
            url = param_list[1]
            if val.url(url):
                print(WARNING_MSG_DOWNLOAD_START)
                download_video(url)
                print(WARNING_MSG_DOWNLOAD_END)
                return True
            else:
                return False
        elif param_list[0] == '-h':
            print('help')
            return True
    else:
        return False

def main():
    params = sys.argv[1:]

    if not (verify_param(params) and options(params)):
        print(ERROR_MSG_INVALID_PARAM)


main()
