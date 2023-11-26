# Random
getwd()
setwd("")
# --- random processes ---
PDFout = "231123-NILEdetPart.pdf"
TXTout = "231123-NILETXT.txt"
#------ input data
DTN <- Nile
TTT = length(DTN)
stYEAR = tsp(DTN)[1]; endYEAR = tsp(DTN)[2]
ROKy = stYEAR:endYEAR
