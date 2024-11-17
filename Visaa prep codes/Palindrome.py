def palin(String):
    String = ''.join(char.lower() for char in String if char.isalnum())
    return String == String[::-1]
N =input()
if palin(N):
    print("TRUE")
else:
    print("FALSE")
