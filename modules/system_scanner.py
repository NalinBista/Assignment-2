import glob
import time
import sys
import os

# Detecting the operating system
os_name = sys.platform

# Global variables to store partitions, directories, and files
partitionen = []
verzeichnisse = []
files = []

# Function to find partitions on Windows


def partitions(sfsFolder):
    global partitionen
    big = 65

    if "win" in os_name:
        # Iterate through drive letters from A to Z
        for i in range(26):
            try:
                if glob.glob(str(chr(big + i)) + ":\\"):
                    # If a drive is found, append it to the list of partitions
                    partitionen.append(str(chr(big + i)) + ":\\")
            except:
                continue
        # Call the next function to list directories and files
        return indeces(sfsFolder)
    # For non-Windows systems, directly call the function to list directories and files
    if "win" not in os_name:
        return indeces(sfsFolder)

# Function to list directories and files


def indeces(sfsFolder):
    global verzeichnisse
    global files

    # Get a list of directories in the root
    if "win" in os_name:
        verzeichnisse2 = glob.glob("\\*")
    else:
        verzeichnisse2 = glob.glob("//*")
    verzeichnisse_tmp = []
    x = 1

    # For Windows systems
    if "win" in os_name:
        # Iterate through each partition
        for ind in range(len(partitionen)):
            # Iterate through directories in the current partition
            while verzeichnisse2 != []:
                verzeichnisse2 = glob.glob(partitionen[ind] + "\\*"*x)
                for i in range(len(verzeichnisse2)):
                    verzeichnisse.append(verzeichnisse2[i])
                x += 1
            x = 1

        # Separate files from directories
        for i in range(len(verzeichnisse)):
            if "." in verzeichnisse[i]:
                files.append(verzeichnisse[i])
        # Filter out directories from the list
        for i in range(len(verzeichnisse)):
            if not os.path.isfile(verzeichnisse[i]):
                verzeichnisse_tmp.append(verzeichnisse[i])
        verzeichnisse = verzeichnisse_tmp

        # Write the list of files to a file
        f = open(sfsFolder, "w", encoding="utf-8")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        # Wait for 3 seconds
        time.sleep(3)

    # For non-Windows systems
    if "win" not in os_name:
        # Iterate through directories
        while verzeichnisse2 != []:
            verzeichnisse = glob.glob("//*" * x)
            for i in range(len(verzeichnisse2)):
                verzeichnisse.append(verzeichnisse2[i])
            x += 1
        x = 1

        # Separate files from directories
        for i in range(len(verzeichnisse)):
            if "." in verzeichnisse[i]:
                files.append(verzeichnisse[i])
        # Filter out directories from the list
        for i in range(len(verzeichnisse)):
            if not os.path.isfile(verzeichnisse[i]):
                verzeichnisse_tmp.append(verzeichnisse[i])
        verzeichnisse = verzeichnisse_tmp

        # Write the list of files to a file
        f = open(sfsFolder, "w", encoding="utf-8")
        for i in range(len(files)):
            f.write(files[i] + "\n")
        f.close()
        # Wait for 3 seconds
        time.sleep(3)
