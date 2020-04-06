# Inputs from sensors, in binary form
analogInput1 = 2000
analogInput2 = 405
analogInput3 = 2098
analogInput4 = 4095
analogInput5 = 3098

# Variables to convert binary to decimal
zero = 0
span = 4095

trueSpan = span - zero

setZero = 0
setSpan = 450

setTrueSpan = setSpan - setZero

calculatedVar1 = analogInput1 * (setTrueSpan / trueSpan)
calculatedVar2 = analogInput2 * (setTrueSpan / trueSpan)
calculatedVar3 = analogInput3 * (setTrueSpan / trueSpan)
calculatedVar4 = analogInput4 * (setTrueSpan / trueSpan)
calculatedVar5 = analogInput5 * (setTrueSpan / trueSpan)
