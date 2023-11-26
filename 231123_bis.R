getwd
getwd()
setwd("C:/Users/Rodrigo/Documents/ENVIRONMENTAL MODELLING MASTER/Subjects/3rd semester/Random processes/RP/")
# --- random processes ---
PDFout = "231123-NILEdetPart.pdf"
TXTout = "231123-NILETXT.txt"
#------ input data
DTN <- Nile
TTT = length(DTN)
stYEAR = tsp(DTN)[1]; endYEAR = tsp(DTN)[2]
ROKy = stYEAR:endYEAR
#-----parametric model
ROKy2 = ROKy^2

ROKy3 = ROKy^3
model0 <- lm(DTN~1) # simple constant model
model1 <- lm(DTN~ROKy) # includes a linear term using the ROKy variable
model2 <- lm(DTN~ROKy+ROKy2) # adds a quadratic term using ROKy2
model3 <- lm(DTN~ROKy+ROKy2+ROKy3) # includes both linear (ROKy) and quadratic (ROKy2) terms, as well as a cubic term (ROKy3).
jmModel = c("constant","line","quadratic","cubic")
jmModel
#------ computation of AIC
ModelAIC <- AIC(model0, model1, model2, model3) #The AIC function is used to compute the AIC for each of the four models
MINaic = min(ModelAIC[,"AIC"])
argMINaic = which.min(ModelAIC[,"AIC"])
#------periodicity
DTNres = model2$residuals # the differences between the observed values and the values predicted by the model
sink(TXTout)
cat("Usage of IC\n\n")
cat("AIC for", jmModel[1], "is", ModelAIC["Model0", "AIC"], "\n")
cat("AIC for", jmModel[2], "is", ModelAIC["Model1", "AIC"], "\n")
cat("AIC for", jmModel[3], "is", ModelAIC["Model2", "AIC"], "\n")
cat("AIC for", jmModel[4], "is", ModelAIC["Model3", "AIC"], "\n\n")
cat("According to AIC we decided for", jmModel[argMINaic], "quadratic model as convenient model for the deterministic part of TS- Nile")
sink()
#-----pictures

pdf(PDFout)
plot(DTN, main = "Nile", xlab = "years", ylab = "discharge")
lines(ROKy, model0$fitted.values, col = "orange")
lines(ROKy, model1$fitted.values, col = "darkblue")
lines(ROKy, model2$fitted.values, col = "red")
lines(ROKy, model3$fitted.values, col = "green")
plot(ROKy,DTNres, type = "l")
dev.off()

#-------Nile deterministic part----
