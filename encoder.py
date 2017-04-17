#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from encryption_resources import CodeMap

reload(sys)
sys.setdefaultencoding("utf-8")


class EncryptionHandler(object):
    """
    EncryptionHandler idea is to be as generic as it can,
    In the init level you can add your encode\decode function to it and if will be usable from the web page drop down.

    Simplicity is beautiful.
    """

    def __init__(self):
        self.codes = {'Morse encode': self.morse_encode,
                      'Morse decode': self.morse_decode,
                      'Caesar encode': self.caesar_encode,
                      'Caesar decode': self.caesar_decode,
                      'Hebrew char encode': self.hebrew_encode,
                      'Hebrew char decode': self.hebrew_decode,
                      }

    def apply_cipher(self, **kwargs):
        cipher_type = kwargs.get('cipher_type')
        return self.codes[cipher_type](**kwargs)

    def morse_encode(self, **kwargs):
        encoded_text = []
        message = (kwargs.get('text_to_cipher')).lower()
        for char in message:
            # try:
            if char.upper() in CodeMap.MORSE:
                encoded_text.append(CodeMap.MORSE[char.upper()])
                # except KeyError:
                #     encoded_text.append(char)
        return encoded_text

    #
    def morse_decode(self, **kwargs):
        encode_message = (kwargs.get('text_to_cipher')).split()
        message = []
        for char in encode_message:
            for key, value in CodeMap.MORSE.items():
                if value == char:
                    message.append(key)
        return message

    def hebrew_encode(self, **kwargs):
        encoded_text = []
        message = kwargs.get('text_to_cipher')
        for char in message:
            try:
                encoded_text.append(CodeMap.HEBREW[char.upper()])
            except KeyError:
                encoded_text.append(char)
        return encoded_text

    def hebrew_decode(self, **kwargs):
        encode_message = kwargs.get('text_to_cipher')
        message = []
        for char in encode_message:
            for key, value in CodeMap.HEBREW.items():
                if value == char:
                    message.append(key)
        return message

    def caesar_encode(self, **kwargs):
        encoded_text = ""
        msg = kwargs.get('text_to_cipher')
        try:
            shift = int(kwargs.get('cipher_args', 5))
        except ValueError, exc:
            shift = 5
        for char in msg:
            if ' ' in char:
                encoded_text += ' '
            elif char.isalpha():
                alpha_dec = ord(char.lower()) + shift
                if alpha_dec > ord('z'):
                    alpha_dec -= 26
                if alpha_dec < ord('a'):
                    alpha_dec += 26
                encoded_char = chr(alpha_dec)
                encoded_text += encoded_char
        return encoded_text

    def caesar_decode(self, **kwargs):
        encoded_text = ""
        encoded_msg = kwargs.get('text_to_cipher')
        try:
            shift = int(kwargs.get('cipher_args'))
        except ValueError, exc:
            shift = 5
        for char in encoded_msg:
            if char.isalpha():
                alpha_dec = ord(char) - shift
                if alpha_dec > ord('z'):
                    alpha_dec -= 26
                if alpha_dec < ord('a'):
                    alpha_dec += 26
            alpha_dec = abs(alpha_dec)
            encoded_char = chr(alpha_dec)
            encoded_text += encoded_char
        return encoded_text
