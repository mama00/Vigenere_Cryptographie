from Vigenere import encrypt_text,decrypt_text,crack_key

text= 'meseseseeeee'
key='mok'
cypher=encrypt_text(text,key)
# print(decrypt_text(cypher,key))
print(crack_key(cypher))