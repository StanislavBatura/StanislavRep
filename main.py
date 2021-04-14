pozyczka = float(input("Kwota pozyczki: "))
rata = float(input("Rata: "))
procent = float(input("Oprocentowanie: "))

number1 = ((1 + ((1.59282448436825 + 3)) / procent / 100) * pozyczka - rata)
number2 = ((1 + (-0.453509101 + 3)) * number1 - rata)
number3 = ((1 + (2.324671717 + 3)) * number2 - rata)
number4 = ((1 + (1.261254407 + 3)) * number3 - rata)
number5 = ((1 + (1.782526286 + 3)) * number4 - rata)
number6 = ((1 + (2.329384541 + 3)) * number5 - rata)
number7 = ((1 + (1.502229842 + 3)) * number6 - rata)
number8 = ((1 + (1.782526286 + 3)) * number7 - rata)
number9 = ((1 + (2.328848994 + 3)) * number8 - rata)
number10 = ((1 + (0.616921348 + 3)) * number9 - rata)
number11 = ((1 + (2.352295886 + 3)) * number10 - rata)
number12 = ((1 + (0.337779545 + 3)) * number11 - rata)
number13 = ((1 + (1.577035247 + 3)) * number12 - rata)
number14 = ((1 + (-0.292781443 + 3)) * number13 - rata)
number15 = ((1 + (2.48619659 + 3)) * number14 - rata)
number16 = ((1 + (0.267110318 + 3)) * number15 - rata)
number17 = ((1 + (1.417952672 + 3)) * number16 - rata)
number18 = ((1 + (1.054243267 + 3)) * number17 - rata)
number19 = ((1 + (1.480520104 + 3)) * number18 - rata)
number20 = ((1 + (1.577035247 + 3)) * number19 - rata)
number21 = ((1 + (-0.07742069 + 3)) * number20 - rata)
number22 = ((1 + (1.165733399 + 3)) * number21 - rata)
number23 = ((1 + (-0.404186718 + 3)) * number22 - rata)
number24 = ((1 + (1.499708521 + 3)) * number23 - rata)



print("Styczeń: \n"f'Twoja pozostała kwota kredytu to {number1},to na {pozyczka-number1} mniej niż w poprzednim miesiącu\n'
"Luty: \n"f'Twoja pozostała kwota kredytu to {number2},to na {number1-number2} mniej niż w poprzednim miesiącu\n'
"Marzec: \n"f'Twoja pozostała kwota kredytu to {number3},to na {number2-number3} mniej niż w poprzednim miesiącu\n'
"Kwiecień: \n"f'Twoja pozostała kwota kredytu to {number4},to na {number3-number4} mniej niż w poprzednim miesiącu\n'
"Maj: \n"f'Twoja pozostała kwota kredytu to {number5},to na {number4-number5} mniej niż w poprzednim miesiącu\n'
"Czerwiec: \n"f'Twoja pozostała kwota kredytu to {number6},to na {number5-number6} mniej niż w poprzednim miesiącu\n' 
"Lipiec: \n"f'Twoja pozostała kwota kredytu to {number7},to na {number6-number7} mniej niż w poprzednim miesiącu\n'
"Sierpnień: \n"f'Twoja pozostała kwota kredytu to {number8},to na {number7-number8} mniej niż w poprzednim miesiącu\n'
"Wrzesień: \n"f'Twoja pozostała kwota kredytu to {number9},to na {number8-number9} mniej niż w poprzednim miesiącu\n'
"Październik: \n"f'Twoja pozostała kwota kredytu to {number10},to na {number9-number10} mniej niż w poprzednim miesiącu\n'
"Listopad: \n"f'Twoja pozostała kwota kredytu to {number11},to na {number10-number11} mniej niż w poprzednim miesiącu\n'
"Grudzień: \n"f'Twoja pozostała kwota kredytu to {number12},to na {number11-number12} mniej niż w poprzednim miesiącu\n'
   "Styczeń: \n"f'Twoja pozostała kwota kredytu to {number13},to na {number12 - number13} mniej niż w poprzednim miesiącu\n'
   "Luty: \n"f'Twoja pozostała kwota kredytu to {number14},to na {number13 - number14} mniej niż w poprzednim miesiącu\n'
      "Marzec: \n"f'Twoja pozostała kwota kredytu to {number15},to na {number14 - number15} mniej niż w poprzednim miesiącu\n'
      "Kwiecień: \n"f'Twoja pozostała kwota kredytu to {number16},to na {number15 - number16} mniej niż w poprzednim miesiącu\n'
      "Maj: \n"f'Twoja pozostała kwota kredytu to {number17},to na {number16 - number17} mniej niż w poprzednim miesiącu\n'
      "Czerwiec: \n"f'Twoja pozostała kwota kredytu to {number18},to na {number17 - number18} mniej niż w poprzednim miesiącu\n'
      "Lipiec: \n"f'Twoja pozostała kwota kredytu to {number19},to na {number18 - number19} mniej niż w poprzednim miesiącu\n'
      "Sierpnień: \n"f'Twoja pozostała kwota kredytu to {number20},to na {number19 - number20} mniej niż w poprzednim miesiącu\n'
      "Wrzesień: \n"f'Twoja pozostała kwota kredytu to {number21},to na {number20 - number21} mniej niż w poprzednim miesiącu\n'
      "Październik: \n"f'Twoja pozostała kwota kredytu to {number22},to na {number21 - number22} mniej niż w poprzednim miesiącu\n'
      "Listopad: \n"f'Twoja pozostała kwota kredytu to {number23},to na {number22 - number23} mniej niż w poprzednim miesiącu\n'
      "Grudzień: \n"f'Twoja pozostała kwota kredytu to {number24},to na {number23 - number24} mniej niż w poprzednim miesiącu\n'
      )



