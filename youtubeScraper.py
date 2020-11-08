#! python3

from pytube import YouTube

print("Please, paste the video's URL (web's address):")

try:
    # Get the video url
    ytVideoUrl = YouTube(input())
    print(ytVideoUrl.title)

    # Check if the video is the right one
    print('\nIs this the video you want to download? \nYes or No?')
    answer = input()
    if answer.lower() == 'yes' or answer.lower() == 'y':     
        print('Your download will begin in a moment...')
        ytDownload = ytVideoUrl.streams.filter(progressive=True, file_extension='mp4')
        ytDownload.get_highest_resolution().download()
        print('Video downloaded succesfully! Check it out.')
        
    else:
        print('I am sorry to hear it. Check your URL and try again.')

except Exception as error:
    print(error)
