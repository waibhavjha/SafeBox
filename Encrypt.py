class UniqueCipher:
    def __init__(self, key):
        self.key = key

    def reverse(self, text):
        return text[::-1]

    def shift(self, text):
        shifted_text = ''
        for char in text:
            if char.isalpha():
                if char.islower():
                    shifted_text += chr(((ord(char) - ord('a') + self.key) % 26) + ord('a'))
                elif char.isupper():
                    shifted_text += chr(((ord(char) - ord('A') + self.key) % 26) + ord('A'))
            else:
                shifted_text += char
        return shifted_text

    def encrypt(self, plaintext):
        encrypted_text = self.reverse(plaintext)
        encrypted_text = self.shift(encrypted_text)
        return encrypted_text

    def decrypt(self, ciphertext):
        decrypted_text = self.shift(ciphertext)
        decrypted_text = self.reverse(decrypted_text)
        return decrypted_text
