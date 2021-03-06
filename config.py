#this is just a list of cards, used to compare black-white pic sum and define card
#can be hard coded in software.py as well, once finished it shouldn't be changed 

cards = {
    '18615' : "2",
    '19380' : "2",
    '17595' : "3",
    '13515' : "4",
    '14790' : "4",
    '19125' : "5",
    '20910' : "6", # and 9!
    '13005' : "7",
    '13770' : "7",
    '19635' : "8",
    '22950': "T",
    '12240' : "J",
    '21930' : "Q",
    '22440' : "Q",
    '18870' : "K", 
    '19890' : "K",
    '17085' : "A",
    '20400' : "A"
}

colors = {
    "Red" : "Heart"[0],
    "Green" : "Spades"[0],
    "Blue" : "Diamonds"[0],
    "Black" : "Clubs"[0]
}

#this is used to detect thrash when checking for card value
not_a_card = ("35700","00")

#this is used to check for player turn
green_bar = [290,372,291,373]
green = [145,232,0]

#buttons - positions @board 1
check_button = [440,430,490,445]
raise_button = [540,425,610,435]
fold_button = [320,430,380,450]
call_button = [440,425,490,435]
all_in_button = [547,425,597,435]
bet_button = [560,425,590,435]

#buttons grayscale sum
raise_button_sum = 68594
fold_button_sum = 56688
check_button_sum = 54048
call_button_sum = 40306
bet_button_sum = 30877
all_in_button_sum = 40306

#hand - positions @board 1
my_card_1 = [284,300,294,314]
my_card_2 = [323,300,333,314]

token_pos = {
    "0" : [371,294,381,304], #gracz
    "1" : [165,265,175,275], #1 na lewo
    "2" : [146,160,156,170], #...
    "3" : [271,120, 281,130],
    "4" : [496,165,506,175],
    "5" : [470, 265, 480, 275]
}

in_game = [
    [325, 355, 335, 365], #gracz
    [65,280,75,285],
    [65,145,75,150],
    [300, 95, 310,100],
    [565,145,575,150],
    [565,280,575,285]
]

#in game player color (his money actualy)
in_game_rgb = [192,248,181]

# using simple token > 40k
#  token_rgb = 41838,41837,40679,41810,41815,41837,


opponent_positions = [
    [57, 260, 87, 272],
    [57,124,87,136],
    [290,72,320,84],
    [557,124,587,136],
    [557, 260, 587, 272]]

# move_fold = [56148, 57297, 58978, 62363, 62481, 62711, 63045, 63112, 63148, 64302, 64450, 64789, 64967, 66316, 68011, 68419, 68478, 69817, 71259, 71574, 72126, 72791, 73316, 74192, 74983, 74983, 75958, 77250, 79106]
# move_check = [78767, 101721]
# move_raise = [76302, 85492]
# move_postbb = [75228, 98839]
# move_postsb = 72190
# move_bet = 65456
# move_call = [69526, 94234, 101241]
# move_muck = [60776, 64175, 69198, 70662, 66115, 64848, 57953, 75972, 72999, 82714,74050, 77937]

# move_sitout = 55969

moves = {
"78767" : "check",
"76302" : "raise",
"75228" : "postbb",
"72190": "postsb",
"98839" : "postbb",
"65456" : "bet" ,
"69526" : "call",
"60776" : "fold",
"64175" : "fold",
"69198" : "fold",
"70662" : "fold",
"66115" : "fold",
"64848" : "fold",
"57953" : "fold",
"75972" : "fold",
"72999" : "fold",
"82714" : "fold",
"74050" : "fold",
"77937" : "fold",
"56148" : "fold",
"57297" : "fold",
"58978" : "fold",
"62363" : "fold",
"62481" : "fold",
"62711" : "fold",
"63045" : "fold",
"63112" : "fold",
"63148" : "fold",
"64302" : "fold",
"64450" : "fold",
"64789" : "fold",
"64967" : "fold",
"66316" : "fold",
"68011" : "fold",
"68419" : "fold",
"68478" : "fold",
"69817" : "fold",
"71259" : "fold",
"71574" : "fold",
"72126" : "fold",
"72791" : "fold",
"73316" : "fold",
"74192" : "fold",
"74983" : "fold",
"75958" : "fold",
"77250" : "fold",
"79106" : "fold",
"94234" :"call",
"101241" :"call",
"85492" : "raise",
"101721" : "check" }

#boards 0-5
opponents_positions = [[[57, 260, 87, 272], [57, 124, 87, 136], [290, 72, 320, 84], [557, 124, 587, 136], [557, 260, 587, 272]],
[[697, 260, 727, 272], [697, 124, 727, 136], [930, 72, 960, 84], [1197, 124, 1227, 136], [1197, 260, 1227, 272]],
[[1337, 260, 1367, 272], [1337, 124, 1367, 136], [1570, 72, 1600, 84], [1837, 124, 1867, 136], [1837, 260, 1867, 272]],
[[57, 800, 87, 812], [57, 664, 87, 676], [290, 612, 320, 624], [557, 664, 587, 676], [557, 800, 587, 812]],
[[697, 800, 727, 812], [697, 664, 727, 676], [930, 612, 960, 624], [1197, 664, 1227, 676], [1197, 800, 1227, 812]],
[[1337, 800, 1367, 812], [1337, 664, 1367, 676], [1570, 612, 1600, 624], [1837, 664, 1867, 676], [1837, 800, 1867, 812]]]







#move mock
    # "fold" : [60776, 64175, 69198, 70662, 66115, 64848, 57953, 75972, 72999, 82714,74050, 77937, 56148, 57297, 58978, 62363, 62481, 62711, 63045, 63112, 63148, 64302, 64450, 64789, 64967, 66316, 68011, 68419, 68478, 69817, 71259, 71574, 72126, 72791, 73316, 74192, 74983, 74983, 75958, 77250, 79106],
    # "check" : [78767, 101721],
    # "raise" : [76302, 85492],
    # "postbb" : [75228, 98839],
    # "postsb" : 72190,
    # "bet" : 65456,
    # "call" : [69526, 94234, 101241]
#move all_in

#6 boards placement on fullHD screen
displays = [
        [0,0,640,540], #x1,y1,x2,y2 (X2 = X1 + width!!!! (WEIRD FACT - counts from X1, NOT from 0!!!)
        [640,0,640,540],
        [1280,0,640,540],
        [0,540,640,540],
        [640,540,640,540],
        [1280,540,640,540]]

#5 cards on first display
card_on_first_display = [
        [212, 173, 222, 187],
        [257, 173, 267, 187],
        [302, 173, 312, 187],
        [346, 173, 356, 187],
        [392, 173, 402, 187]]

cards_on_each_display = [
[[212, 173, 222, 187], [257, 173, 267, 187], [302, 173, 312, 187], [346, 173, 356, 187], [392, 173, 402, 187]],
[[852, 173, 862, 187], [897, 173, 907, 187], [942, 173, 952, 187], [986, 173, 996, 187], [1032, 173, 1042, 187]],
[[1492, 173, 1502, 187], [1537, 173, 1547, 187], [1582, 173, 1592, 187], [1626, 173, 1636, 187], [1672, 173, 1682, 187]],
[[212, 713, 222, 727], [257, 713, 267, 727], [302, 713, 312, 727], [346, 713, 356, 727], [392, 713, 402, 727]],
[[852, 713, 862, 727], [897, 713, 907, 727], [942, 713, 952, 727], [986, 713, 996, 727], [1032, 713, 1042, 727]],
[[1492, 713, 1502, 727], [1537, 713, 1547, 727], [1582, 713, 1592, 727], [1626, 713, 1636, 727], [1672, 713, 1682, 727]] ]