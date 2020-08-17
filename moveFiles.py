import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import shutil
import glob
import os

# Program that watches the Documents directory. If a screenshot is taken, it moves the screenshot to Documents/Screenshots.

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    def on_created(event):
        # function to get name of last saved screenshot as a str
        def getName():
            list_of_files = glob.glob('/Users/chelsea.vizer/Documents/*.png') # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            latest_file = str(latest_file)
            print(latest_file)
            fileName = latest_file[31:]
            return fileName

        # x is the string of the screenshot name
        x = getName()

        # Assign path for original screenshot to variable "ogPath"
        ogPath = "/Users/chelsea.vizer/Documents/{}".format(x)

        # Assign path for new location of screenshot to variable "newPath"
        newPath = "/Users/chelsea.vizer/Documents/Screenshots/{}".format(x)

        # function that moves the file
        def moveFile():
            shutil.move(ogPath, newPath)

        print("The screenshot has been moved to Documents/Screenshots.")
        moveFile()

    my_event_handler.on_created = on_created

    path = "."
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()
