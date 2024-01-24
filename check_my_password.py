import requests
import hashlib
import sys
# using k-anonymity


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error fetching: {response.status_code}, check api again')
    return response


def read_response_api(res_api):
    '''Reads all the hashes that match the beginning of our hashed password '''
    print(res_api.text)


def get_password_leaks(all_hashes, hash_to_check):
    hashes = (line.split(':') for line in all_hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    '''Converts our password to SHA1 using Hash functional library and returns it to the API function'''
    # print(password.encode('utf-8'))
    # print(hashlib.sha1(password.encode('utf-8')))
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    print(first5_char, tail)
    res = request_api_data(first5_char)
    # read_response_api(res)
    return get_password_leaks(res, tail)


def main(args):
    for password in args:
        print(password)
        count = pwned_api_check(password)
        if count:
            print(f'Password is FOUND {
                  count} number of times, you should probably change your password')
        else:
            print(f'Password is found {
                  count} number of times. Password is NOT exposed!')
    return 'done!'

# Reading password from terminal:
# if __name__ == '__main__':
#     sys.exit(main(sys.argv[1:]))


# Reading passwords from a file is a more secure way than reading from terminal:
if __name__ == '__main__':
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            file_contents = [line.rstrip('\n') for line in file.readlines()]
            print(f"Contents of {file}:\n{file_contents}")
            exit_code = main(file_contents)
            sys.exit(exit_code)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)
