
# =============================================================================
# liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 
# quad_zahl = []
# 
# for zahl in liste:
#     if zahl%2 == 0:
#         quad_zahl.append(zahl)
#     else:
#       quad_zahl.append(zahl**2)
#       
# 
# print(quad_zahl)
# =============================================================================

quad_zahl = [zahl if zahl%2 == 0 else zahl for zahl in range(1,11)]
