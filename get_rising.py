import os
import praw
import requests

def get_rising_images(subreddit):


    r = praw.Reddit('Download top pics of Day from earthporn')

    submissions = r.get_subreddit('earthporn').get_rising()


    for submission in submissions:
        url = submission.url
        if url.endswith(('jpg', 'png', 'jpeg')):
            yield url

def download_it(url):



    url_chars = url.split('/')[-1][-10:]

    file_name = 'sceneries_{chars}'.format(chars=url_chars)


    home_dir = os.path.expanduser('~')

    path = os.path.join(home_dir, 'sceneries')
    if os.path.exists(path):
        pass
    else:
        try:
            os.mkdir(path)
        except OSError as e:
            print(e)


    save_path = os.path.join(path, file_name)

    if os.path.exists(save_path):
        print ("{file_name} already downloaded".format(file_name=file_name))
    else:
        print ("Downloading to {save_path}".format(save_path=save_path))

        r = requests.get(url, stream=True)
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

if __name__ == "__main__":

    for img_url in get_rising_images('earthporn'):
        download_it(img_url)
