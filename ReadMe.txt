#Decrypting passwords from the password lists of Asley Madison, eHarmony and Formspring

1. Ashley Madison
Files Used=>
Given File: AshleyMadison.txt
Code: ashley.py
Output File: AshleyOutput.txt
Technique Used: For Ashley Madison, the password was extracted based on the position of the fourth
header i.e., userpassword, as mentioned in the given text file Ashley Madison.txt. The extracted
password has been stored in an output file as per the submission requirement.

2. eHarmony
Files Used=>
Given File: eHarmony.txt
Code: eHarmony.py
Wordlist: http://home.btconnect.com/md5decrypter/hlm/hk_hlm_founds.zip
Output File: eHarmonyOutput.txt
NOTE: Rename the downloaded Wordlist to md5.txt
Technique Used: The given file eHarmony.txt, has a series of hashed passwords which has been
encrypted using the MD5 algorithm. The following steps were taken to crack the passwords=>
1. In order to crack these passwords, a wordlist was downloaded from the above mentioned link. It
contains a series of plain text passwords that might correspond to the one’s in the hashed list.
2. The passwords in this wordlist were then hashed with MD5 and then, matched with the given
list of hashed passwords.
3. A match for 98 passwords were found as mentioned in the output file.

3. Formspring
Files Used=>
Given File: formspring.txt
Code: formspring.py
Wordlist: sha256.txt
Output File: formspringOutput.txt
Technique Used: The given file formspring.txt has a series of hashed passwords which has been
encrypted using the SHA256 algorithm along with salting. The original password has been salted by
appending a string of the range 00-99, before the password. The concatenated salt and password was
then hashed using SHA256. The following steps were taken to crack the passwords=>
1. In order to crack these passwords, the wordlist as mentioned in sha256.txt is being used. It
contains a series of plain text passwords that might correspond to the one’s in the hashed list.
2. The passwords in this wordlist were then salted by appending a string of the range 00-99, before
each of these passwords. Each of these combinations were then hashed using SHA256, and
matched with the given list of hashed passwords.
3. A match for some of the words were found as mentioned in the output file.
Comparison Between the Techniques used
Ashley Madison passwords were easy to extract as it was clear where the password is.
eHarmony simply used MD5 encryption and so it was not that difficult to crack as well. One of the majo r
backdrops of using just MD5 is that, it doesn't allow any 2 users to have the same password.
As for formspring, it was slightly difficult as salting was being done on the passwords along with sha256
encryption. This form of salting allows 2 users to have the same password, unlike the eHarmony case
mentioned above. This is because hashing after salting will produce different hashed passwords, even if
the password entered by two different users is the same.
Thus the security measures taken by formspring is more secure than eHarmony or Ashley Madison in
this case.
