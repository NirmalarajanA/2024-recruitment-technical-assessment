from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    nameList = []
    for file in files:
        # Using find() to check if its a file and not a folder as that is differentiated by a '.something'
        if file.name.find('.') > 0:
            nameList.append(file.name)

    return nameList

"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    # Create a Dictionary and store how many times a category appears 
    dic = {}
    for file in files:
        for categories in file.categories:
            if categories in dic:
                dic[categories] += 1
            else:
                dic[categories] = 1

    # Ensures that the k categories taken are sorted by number of and alphabetically 
    sortedDic = dict(sorted(dic.items(), key = lambda x: (-x[1], x[0])))

    # Take the first k elements in the sorted dictionary 
    returnList = []
    for key in sortedDic:
        returnList.append(key)
        if (len(returnList) == k):
            break

    return returnList

"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    childSizeDic = {}
    parentSizeDic = {}

    # Initialising Dictionaries 
    for file in files: 
        if file.parent == -1:
            parentSizeDic[file.id] = file.size 
        else: 
            childSizeDic[file.id] = file.size 
    
    # Find the total for all childs 
    for file in files: 
        if file.parent in childSizeDic: 
            childSizeDic[file.parent] += file.size 

    # Find the total for all parents 
    for file in files:
        if file.parent in parentSizeDic:
            parentSizeDic[file.parent] += childSizeDic[file.id]

    return max(parentSizeDic.values())


if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
