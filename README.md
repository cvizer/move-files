# Watch Directory And Move Files

## Description

> The purpose of this program is to watch the Documents directory. Whenever a new screenshot is taken, it will automatically be moved to a different directory within the Documents directory. This program is meant to be run on a Mac, not a PC.

---

## How To Use

Save moveFiles.py to the Documents directory on your computer.

Create a directory within your Documents directory and name it "Screenshots".

On lines 18, 29, & 32, replace "Your user account" with the actual user account you're signed into on your mac.

```python
    def getName():
            list_of_files = glob.glob('/Users/<<Your user account>>/Documents/*.png') 
```

```python
    originalPath = "/Users/<<Your user account>>/Documents/{}".format(x)
```

```python
    newPath = "/Users/<<Your user account>>/Documents/Screenshots/{}".format(x)
```
Now open the command line, cd into your Documents folder, and run:

`python moveFiles.py`

Leave the program running and take a screenshot. You will see that the screenshot will automatically be moved into the Documents/Screenshots folder.

---

## Author Info

- Github - [github.com/cvizer](https://github.com/cvizer)
- Email - <chelseavizer@yahoo.com>

[Back To Top](#watch-directory-and-move-files)