import argparse
import base64

def read_usernames(file_path):
    """Read usernames from a file."""
    with open(file_path, 'r') as file:
        usernames = [line.strip() for line in file if line.strip()]
    return usernames

def generate_emails(usernames, domain):
    """Generate email addresses from usernames and domain."""
    return [f'{username}@{domain}' for username in usernames]

def save_to_file(email_list, file_path):
    """Save email addresses to a file."""
    with open(file_path, 'w') as file:
        for email in email_list:
            file.write(f'{email}\n')

def save_to_base64(email_list, file_path):
    """Save email addresses to a file in Base64 encoded format."""
    with open(file_path, 'wb') as file:
        for email in email_list:
            encoded_email = base64.b64encode(email.encode()).decode()
            file.write(f'{encoded_email}\n'.encode())

def main(args):
    # Read usernames from the file
    usernames = read_usernames(args.wordlist)
    
    # Generate email addresses
    email_list = generate_emails(usernames, args.domain)
    
    # Save emails in the specified format
    if args.base64:
        save_to_base64(email_list, args.output)
    else:
        save_to_file(email_list, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate email addresses from a list of usernames and domain name.')
    
    # Command-line arguments
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the file containing usernames')
    parser.add_argument('-d', '--domain', required=True, help='Domain to use for email addresses')
    parser.add_argument('-o', '--output', required=True, help='Output file path for the email addresses')
    parser.add_argument('-base64', action='store_true', help='Encode email addresses in Base64 format')
    
    # The -h option is automatically added by argparse
    args = parser.parse_args()
    
    main(args)
