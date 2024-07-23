# emailgenerator
This script helps you quickly create lists of email addresses, which can be handy for testing or administrative tasks. It takes a list of usernames and a domain name and generates email addresses for each username. Plus, it can save the results in a Base64 encoded format if you need it. This makes the process of generating and formatting email addresses much easier and more adaptable to different needs.
# Show all available options
`
python3 emailgenerator.py -h
`

# Besic example 1
`
python3 emailgenerator.py -d domain.com -w path-of-username-txt-file -o email.txt
`

# Encoding emails in base64 format
`
python3 emailgenerator.py -d domain.com -w path-of-username-txt-file -base64 -o email-base64.txt
`
