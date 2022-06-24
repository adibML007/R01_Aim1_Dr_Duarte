library(dplyr, warn.conflicts = FALSE)
library(tidygeocoder)
library(readr)
rm(list=ls())
provider_list <- read_csv("C:/Users/rafsz/Desktop/Provider_FL_new.csv")
View(provider_list)
provider_list$add<-paste(provider_list$Address,
                         provider_list$City,
                         provider_list$State,sep=",")
X = provider_list
Y = geocode(X, address = add, method = "arcgis", verbose = TRUE)
write.csv(Y,'geocoded_address_FL_final.csv',row.names=FALSE)
