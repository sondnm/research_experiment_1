"""
Conversion functions for the NATO Phonetic Alphabet.
"""

# To save a lot of typing the code words are presented here
# as a dict, but feel free to change this if you'd like.
ALPHANUM_TO_NATO = {
    "A": "ALFA",
    "B": "BRAVO",
    "C": "CHARLIE",
    "D": "DELTA",
    "E": "ECHO",
    "F": "FOXTROT",
    "G": "GOLF",
    "H": "HOTEL",
    "I": "INDIA",
    "J": "JULIETT",
    "K": "KILO",
    "L": "LIMA",
    "M": "MIKE",
    "N": "NOVEMBER",
    "O": "OSCAR",
    "P": "PAPA",
    "Q": "QUEBEC",
    "R": "ROMEO",
    "S": "SIERRA",
    "T": "TANGO",
    "U": "UNIFORM",
    "V": "VICTOR",
    "W": "WHISKEY",
    "X": "XRAY",
    "Y": "YANKEE",
    "Z": "ZULU",
    "0": "ZERO",
    "1": "ONE",
    "2": "TWO",
    "3": "TREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINER",
}

NATO_TO_ALPHANUM = {v: k for k, v in ALPHANUM_TO_NATO.items()}

def transmit(message: str) -> str:
    """
    Convert a message to a NATO code word transmission.
    """
    return " ".join(
        ALPHANUM_TO_NATO[c] for c in message.upper() if c.isascii() and c.isalnum()
    )

def receive(transmission: str) -> str:
    """
    Convert a NATO code word transmission to a message.
    """
    return "".join(map(NATO_TO_ALPHANUM.get, transmission.split()))

ALPHANUM = "".join(ALPHANUM_TO_NATO.keys())
CAESAR = str.maketrans(ALPHANUM, ALPHANUM[-3:] + ALPHANUM[:-3])
RASEAC = {v: k for k, v in CAESAR.items()}

def transmit_encoded(plaintext: str) -> str:
    """
    Encode a message and transmit as NATO code words.
    """
    ciphertext = plaintext.upper().translate(CAESAR)
    return transmit(ciphertext)

def receive_encoded(ciphertext: str) -> str:
    """
    Receive an encoded message via NATO code word transmission.
    """
    return receive(ciphertext).translate(RASEAC)
