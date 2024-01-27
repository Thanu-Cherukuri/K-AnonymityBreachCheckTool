# K-AnonymityBreachCheckTool

## Description
This script is a password security checker that uses the k-anonymity model and Pwned Passwords API to determine if a password has been exposed in a data breach. It ensures that the actual passwords are never sent over the network, only using the first five characters of their SHA-1 hash. The script can check multiple passwords efficiently and securely.

## Features
- Uses k-anonymity for secure password checking.
- Hashes passwords with SHA-1.
- Checks multiple passwords from a file or command line.
- Reports on the exposure status of passwords.

## How to Use
1. Clone this repository.
2. Run the script with a file containing passwords, one per line: `python password_checker.py passwords.txt`.

## Requirements
- Python 3.x
- `requests`

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License
[MIT License](LICENSE)

## Contact
Thanuja Cherukuri - [thanujacherukuri111@gmail.com]
