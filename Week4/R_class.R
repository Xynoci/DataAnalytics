## Set directory to YOUR computer and folder
setwd("C:/Users/Pudders/Desktop/MovieData")
#install.packages("RSQLite") #perhaps needed
library("RSQLite")
sqlite    <- dbDriver("SQLite")
moviesDB <- dbConnect(sqlite,"movies.db")
query <- dbSendQuery(moviesDB, "SELECT STATEMENT" )
budget80 <- dbFetch(query, n = -1)
dbClearResult(query)


### ADD MORE HERE
