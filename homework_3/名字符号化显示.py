line1={'L':' #          ','K':' #       # ','A':'        #        ','F':' #########  ','I':'  #####   ','U':'  #         #','O':'    #####    ','m':'   ##          ##   ',' ':'           '}
line2={'L':' #          ','K':' #     #   ','A':'       # #       ','F':' #          ','I':'    #     ','U':'  #         #','O':'  #       #  ','m':' #     #     #    # ',' ':'           '}
line3={'L':' #          ','K':' #   #     ','A':'      #   #      ','F':' #          ','I':'    #     ','U':'  #         #','O':' #         # ','m':'#         #        #',' ':'           '}
line4={'L':' #          ','K':' # #       ','A':'     #     #     ','F':' #########  ','I':'    #     ','U':'  #         #','O':' #         # ','m':'#                  #',' ':'           '}
line5={'L':' #          ','K':' # #       ','A':'    #########    ','F':' #          ','I':'    #     ','U':'  #         #','O':' #         # ','m':' #                # ',' ':'           '}
line6={'L':' #          ','K':' #   #     ','A':'   #         #   ','F':' #          ','I':'    #     ','U':'  #         #','O':' #         # ','m':'   #            #   ',' ':'           '}
line7={'L':' #          ','K':' #     #   ','A':'  #           #  ','F':' #          ','I':'    #     ','U':'   #       # ','O':'  #       #  ','m':'      #       #     ',' ':'           '}
line8={'L':' ########## ','K':' #       # ','A':' #             # ','F':' #          ','I':'  #####   ','U':'     #####   ','O':'    #####    ','m':'          #         ',' ':'           '}
line=[line1,line2,line3,line4,line5,line6,line7,line8]
name=raw_input('What do you want to type?')    # let the user to input characters
i,j=1,1          # set the loop variables
while i<=9 :     # this loop can display the charaters or some marks
    line_print = ''
    while j<=len(name) :
        line_print=line_print+line[i-1][name[j-1]]
        j=j+1
    print line_print
    j=1          # reset the loop variables.
    i=i+1

