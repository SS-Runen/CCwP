"""
Requirements:
- Save the variables and file details created after analysing an English
text file to get baseline values of a true English text files.
Details to be saved:
    Name of text file analyzed.
    Full path of text file analyzed.
    Dictionary of English words used, stored as a list.
    If Dictionary used was a file, file name.
    If Dictionary used was a file, full file path.
    Metrics used to measure likelihood of target files being english,
        stored in a dictionary. String names of the measures will be keys.
        Values will be the metrics/results stored as floats. Ex:
        {"percent in dictionary": 30}.
- Analyze files wihtout having to get baseline metrics or create a dicitonary
every time the script is run.
- Allow the user to change the file and/or dictionary of words used to get
baseline data.
"""
