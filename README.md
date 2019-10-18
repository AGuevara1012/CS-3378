# mini

To be able to run this on the university's Linux server, complete the following steps to initiate a virtual environment and install necessary packages.

In Linux:
$virtualenv -p python3 venv
$source venv/bin/activate
$pip install beautifulsoup4
Note: if you run into an issue with pip not being updated, input the following code:
$pip install --upgrade pip

To run the program:
$python ./AmberGuevara_mini.py

This will create three text files. To open each file:
$vim "Dr. Byron Gao.txt"
$vim "Dr. Qinjun Gu.txt"
$vim "Dr. Xiao Chen.txt"

This program scrapes an active URL and returns requested information into a text file using beautiful soup, requests, and regex.

The URLs are hard coded into the program, so there is no input needed to run the program.
