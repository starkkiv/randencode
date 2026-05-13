# RandEncode
RandEncode is an experimental Python project which explores byte transformations using repeated modular arithmetic and randomized key generation.
The goal of this project is not to invent secure encryption (yet) but to investigate how data can be transformed through layered encoding operations.

- encode.py script is the main algorithm performing the encryption
- decrypt.py script is for decription of encode.py outputs using any cipher and adjacent keys in order

# Important Notes
This project is currently not cryptographically secure.
It has multiple limitations:

- Encryption currently not secure for commercial use. 

- Keys are randomly generated externally and not managed for secure recovery.

- It is intended purely as a learning exercise in data transformation.

You will need to install "rich" library for visual design of the algorithm (use pip install rich or venv if externally-managed-environment error occurs)
