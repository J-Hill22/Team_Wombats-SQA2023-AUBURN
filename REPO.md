# Team Wombats Project Report

Members: Jarrett Hill, Elwood Hogan, Connor Wyatt, Aiden Green

## Aiden Green
- Worked on deliverable 4.c.
- Implemented forensics in 5 different methods located within parser.py.
- Lessons Learned: Built upon knowledge gained from implementing forensics in internship and previously in the class. Forensics is vital for large repos as not everyone using the code will know exactly how it works, this makes it much easier for debugging and overall understanding of a codebase.

## Jarrett Hill
- Worked on deliverable 4.a.
- Implemented a bandit script in /.git/hooks/precommit that recursively scans the entire project repo for security vulnerabilities and logs them in "vulnerabilities.csv"
- Lessons Learned: Reinforced knowledge gained from this course in regard to applying static analysis to a github repository and using a bandit script to scan for security vulnerabilities.

## Elwood Hogan
- Worked on deliverable 4.b.
- Implemented fuzzing for 5 different forms of calculations
- Lessons Learned: I understand the value of fuzzing, and how to apply it to methods

## Connor Wyatt
- Worked on deliverable 4.b. and checked deliverable 4.c.
- Implemented fuzzing actions that are automatically performed by Github Actions.
-   Also confirmed validity of fuzzing and logging methods.
- Lessons Learned: While having methods for improving the quality of our code is important, the implementation of this code into our workflow is also integral. Utilzing Continuous Integration via Github Actions, the chances of invalid or erroneous code getting onto the repository (and thus becoming harder to remove over time) drastically decreases.

