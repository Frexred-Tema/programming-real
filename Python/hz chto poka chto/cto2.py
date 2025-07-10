fin  = int(input())
sen  = int(input())
thn = int(input())
fon  = int(input())
packed = fon << 8
packed = packed | thn
packed = packed << 8
packed = packed | sen
packed = packed << 8
packed = packed | fin

print(packed)