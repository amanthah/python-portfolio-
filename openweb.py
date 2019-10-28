import subprocess
from subprocess import call
import webbrowser
websites = ['www.google.com', 'www.reddit.com', 'www.youtube.com']
for url in websites:
    webbrowser.open_new_tab(url)


# url_list = ['stackoverflow.com', 'google.com']
# for i in url_list:
#     subprocess.call("xdg-open {}".format(i))
