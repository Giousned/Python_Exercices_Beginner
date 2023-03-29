# Your code here!!
def sing ():
    song = ""
    for i in range(10):
        if i == 4:
            song += "whisper words of wisdom, "
        if i == 9:
            song += "there will be an answer, let it be"
        else:
            song += "let it be, "

    return song

print(sing())

# SOLUCION DADA
# def sing():
#     song = ""
#     for i in range(11):
#         if i == 4:
#             song += "whisper words of wisdom, "
#         elif i == 10:
#             song += "there will be an answer, let it be"
#         else:
#             song += "let it be, "
#     return song