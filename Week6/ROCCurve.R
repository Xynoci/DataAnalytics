library(ggplot2)
library(ROCR)
# create new column called "is_expensive" (true/false based on price > 2400)
diamonds$is_expensive <- diamonds$price > 2400
#create an uniform distrabution 
is_test <- runif(nrow(diamonds)) > 0.75
#try: 
#plot(runif(10000))

#create a training and testing set
train <- diamonds[is_test==FALSE,]
head(train)
test <- diamonds[is_test==TRUE,]
head(test)
#create a Fitting Generalized Linear Models
summary(fit <- glm(is_expensive ~ carat + cut + clarity, data=train))
#summary(fit <- glm(is_expensive ~ cut, data=train))

# do the prediction with the test data
prob <- predict(fit, newdata=test, type="response")
pred <- prediction(prob, test$is_expensive)
perf <- performance(pred, measure = "tpr", x.measure = "fpr")
# get the area under the curve (auc)
auc <- performance(pred, measure = "auc")
auc <- auc@y.values[[1]]

#plot, remember 1 is a perfect classification, .5 a guess, 0 just bad
roc.data <- data.frame(fpr=unlist(perf@x.values),tpr=unlist(perf@y.values),model="GLM")
ggplot(roc.data, aes(x=fpr, ymin=0, ymax=tpr)) +
    geom_ribbon(alpha=0.2) +
    geom_line(aes(y=tpr)) +
    ggtitle(paste0("ROC Curve w/ AUC=", auc))
