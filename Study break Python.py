import webbrowser 
import time

total_breaks = 5
break_count = 0

print("This program started on "+time.ctime())
while(break_count < total_breaks):
    time.sleep(7200)
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open("https://www.youtube.com/watch?v=nrjPzPc1JiY")
    break_count = break_count +1
