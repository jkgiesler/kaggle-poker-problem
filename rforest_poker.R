test <- read.csv("~/Downloads/Poke/filtered_test.csv")
train <- read.csv("~/Downloads/Poke/filtered_train.csv")
train$target <- factor(train$target)
library(randomForest)
predictors=train[,1:9]
response=train[,10]
forest <- randomForest(x=predictors,
                       y=response,
                       mtry=9,
                       ntree=1500,
                       do.trace=10)

preds<-predict(forest,test)
sampleSubmission<-read.csv("~/Downloads/Poke/sampleSubmission.csv")
sampleSubmission$hand<-levels(train$target)[preds]

write.csv(sampleSubmission,file='second_poker.csv',row.names=F)
