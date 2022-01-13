Author:-
---------
Debanjan Sarkar


About the script:-
-------------------
This python 3 script can generate unique ids for user which are cryptographically secure. It uses the "random" module, and for the
asynchronous selection and generation if random characters, the methods of "random" module are being called by creating an instance
of random.SystemRandom() class, which ensures cryptographic security.

For each time script being executed, you can set the length(in terms of number of characters) of the user ids being generated, at the
beginning, which remains fixed till the programs ends.

Further more, when the ids being generated are of apt length(greater than or equal to 6), then weights are being assigned to the 
integers and alphabets accordingly, using probability, so that in no case the id contains only integers or only alphabets throughout.


Execution:-
------------
a. At the start, the user needs to mention the length of the ids that will get generated, which will be fixed till program ends.
   The  length assigned should be a valid positive integer(for being better, should be greater than equal to 6).

b. After that, user needs to select one of the two options: 1 or 2
   Input of 1 will generate unique id, and 2 will exit the program. Any character/option other than these two will be invalid option.

c. After selection of 1 , user needs to enter any user name, and after entering username, the program will show username alongwith
   the generated userid, and the date and time of the userId generation.

d. The whole program is operated by a loop, which means till the selection of Exit option, user can generate several unique ids.
