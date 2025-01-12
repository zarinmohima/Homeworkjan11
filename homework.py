#Q1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
words = ['Thirty', 'Days', 'Of', 'Python']
# I need to Join the words with space separator, xplicit spaces (' ') 
result = ' '.join(words)
print(result)

#Q2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# words needs to be Listed to concatenate
words = ['Coding', 'For', 'All']
# Join + variable
result = ' '.join(words)
print(result)

#Q3.Declare a variable named company and assign it to an initial value "Coding For All".
# Declare a variable and assign the value Coding For All
company = "Coding For All"

#Q4.Print the variable company using print().
company = "company"
print(company)
#Q5.Print the length of the company string using len() method and print().
company = 'company'
print(len(company))

#Q6.Change all the characters to uppercase letters using upper() method.
company = 'company'
print(company.upper())
#Q7.Change all the characters to lowercase letters using lower() method.
company = 'company'
print(company.lower())
#Q8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company = "Coding For All"

# capitalize() 
print(company.capitalize())

# title()
print(company.title())
# swapcase() -Changes uppercase to lowercase and vice versa
print(company.swapcase())

#Q9.Cut(slice) out the first word of Coding For All string.
company = "Coding For All"
# Slice out the first word coding (up to the first space need to use 0)
first_word = company.split()[0]
print(first_word)

#Q10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
company = "Coding For All"
result = company.find("Coding")

if result != -1:
    print("The word 'Coding' is found at index:", result)
else:
    print("The word 'Coding' is not found.")

#Q11.Replace the word coding in the string 'Coding For All' to Python.
company = "Coding For All"
new_company = company.replace("Coding", "Python")
print(new_company)

#Q12.Change Python for Everyone to Python for All using the replace method or other methods.
text = "Python for Everyone"
new_text = text.replace("Everyone", "All")
print(new_text)

#Q13.Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
split_words = company.split()  # Default separator is space
print(split_words)

#Q14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")  # Split at the comma followed by space
print(split_companies)

#Q15.What is the character at index 0 in the string Coding For All.
company = "Coding For All"
char_at_index_0 = company[0]
print(char_at_index_0)

#Q16.What is the last index of the string Coding For All.
company = "Coding For All"
last_index = len(company) - 1  # This calculates the last index
print(last_index)

#Q17.What character is at index 10 in "Coding For All" string.
company = "Coding For All"
charindex_10 = company[10]
print(charindex_10)

#Q18.Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python For Everyone"  #create acronym 
name = name.split()  # Spliting the string into a list of words
acronym = ""  # Initializing an empty string to store the acronym

for i in name:  # Loop through each word in the list
    acronym += i[0].upper()  # Add the first letter of each word, converted to uppercase
print(acronym)  # Print the final acronym

#Q19.Create an acronym or an abbreviation for the name 'Coding For All'.
name = "Coding For All"
name = name.split()
acronym = ""
for i in name:
   acronym += i[0].upper()
print(acronym)

#Q20.Use index to determine the position of the first occurrence of C in Coding For All.
company = "Coding For All"
position = company.index("C")  # Find the index of the first occurrence of 'C'
print(position)


