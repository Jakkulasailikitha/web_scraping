l=[4,3,2,8]
a=[]
i=0
while i<len(l):
    j=i
    while j< len(l)-1:
        a.append(str(l[i])+str(l[j+1]))
        j=j+1
    i=i+1
print(a)


# a=[1,2,3,4]
# i=0
# while i<len(a)-1:
#     if a[0]>a[1]:
#         t=a[i]
#         a[i]=a[i+1]
#         a[i+1]=t
#     if a[3]>a[2]:
#         j=a[i]
#         a[i]=a[i+1]
#         a[i+1]=j
#     i=i+1
# print(a)
# # # l=[1,2,3,4,3,5]
# # # i=0
# # # c=[]
# # # while i<len(l):
# # #     l[i], l[i+1] = l[i+1], l[i]
# # #     c.extend([l[i],l[i+1]])
# # #     i+=2
# # # print(c)
# # a=[[4,5,1],[3,2,6],[9,6,3]]
# # c=[]
# # i=0

# # while i<len(a):
# #     b=a[i][-1]
# #     c.append(b)
# #     i=i+1
# # print(c)