#UCB

#importing the dataset
dataset<-read.csv('/Users/DK/Documents/Machine_Learning/Python-and-R/Machine_Learning_Projects/Reinforcement Learning/UCB/Ads_CTR_Optimisation.csv')

#implementing UCB
N<-10000
d<-10
total_reward<-0
selected_ads<-integer(0)
num_of_selected<-integer(d)
sums_of_rewards<-integer(d)

for (n in 1:N){
  max_bound<-0
  ad<-0
  for (i in 1:d){
    if(num_of_selected[i]>0){
      avg_reward<-sums_of_rewards[i]/num_of_selected[i]
      delta<-sqrt((3/2)*log(n)/num_of_selected[i])
      upper_bound<-avg_reward+delta
    }
    else{
      upper_bound<-1e400
    }
    if(upper_bound>max_bound){
      max_bound<-upper_bound
      ad<-i
    }
  }
  selected_ads<-append(selected_ads,ad)
  num_of_selected[ad]<-num_of_selected[ad]+1
  reward<-dataset[n,ad]
  sums_of_rewards[ad]<-sums_of_rewards[ad]+reward
  total_reward<-total_reward+reward
}

#visualisation
hist(selected_ads,
     col='blue',
     main='Histogram of Selected Ads',
     xlab='Ads',
     ylab='Number of times each ad was selected')
