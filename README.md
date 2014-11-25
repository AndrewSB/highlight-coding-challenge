#Build instructions
- `git clone https://github.com/AndrewSB/highlight-coding-challenge.git`
- `cd highlight-coding-challenge`
- `python main.py`
- You'll see the program output in the console as well as in `results.txt` that will be added to the directory

#Explanation of solution
I wrote my solution in python because of it's simple and concise syntax. To solve the problem, I decided to create a data structure I called a `MultiStack`, the structure stores a stack for each user (danny, uncle joey, and dj) and runs code to make sure that if any two people are currently within 150ft of eachother, the entry will be examined further on the addition of any new dataentry.

I also created data types to store each data entry, `Entry` for any dataentry of the type seen in `userdata.txt` and `MatchEntry` for every matched dataentry that is to be put in the results.

#Output
See `results.txt`
